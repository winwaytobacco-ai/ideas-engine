"""Layer 1 — Macro regime gate.

Rule-based, transparent. Answers: is the environment worth initiating
long positions at all? See IDEAS_ENGINE_PLAN.md §4.
"""
from __future__ import annotations

from dataclasses import dataclass, field

import pandas as pd

from . import data_io


@dataclass
class Signal:
    name: str
    value: str          # human-readable latest reading
    rule: str           # the rule being applied
    passed: bool | None # None = informational only


@dataclass
class RegimeResult:
    label: str
    explanation: str
    signals: list[Signal] = field(default_factory=list)

    @property
    def allows_ideas(self) -> bool:
        return self.label != "RISK_OFF"


def _credit_signal(cfg: dict) -> Signal:
    s = data_io.get_fred_series("BAMLH0A0HYM2")
    latest = float(s.iloc[-1])
    ma21 = float(s.rolling(21).mean().iloc[-1])
    pctl_max = cfg["hyoas_percentile_max"]
    pctl_val = float(s.tail(252).quantile(pctl_max / 100))
    ok = latest < ma21 and latest < pctl_val
    return Signal(
        "Credit stress (HY OAS)",
        f"{latest:.2f}%",
        f"< 21d MA ({ma21:.2f}) and < p{pctl_max} of 252d ({pctl_val:.2f})",
        ok,
    )


def _curve_signal() -> Signal:
    s = data_io.get_fred_series("T10Y2Y")
    latest = float(s.iloc[-1])
    prior = float(s.iloc[-22]) if len(s) > 22 else latest
    state = "inverted" if latest < 0 else "positive"
    trend = "steepening" if latest > prior else "flattening"
    return Signal("Yield curve (10y-2y)", f"{latest:+.2f}% ({state}, {trend})",
                  "informational only in v1", None)


def _vix_signal(cfg: dict) -> Signal:
    s = data_io.get_fred_series("VIXCLS")
    latest = float(s.iloc[-1])
    ma50 = float(s.rolling(50).mean().iloc[-1])
    ok = latest < cfg["vix_max"] and latest < ma50
    return Signal("Volatility (VIX)", f"{latest:.1f}",
                  f"< {cfg['vix_max']} and < 50d MA ({ma50:.1f})", ok)


def _nfci_signal(cfg: dict) -> Signal:
    s = data_io.get_fred_series("NFCI")
    latest = float(s.iloc[-1])
    ok = latest < cfg["nfci_max"]
    return Signal("Financial conditions (NFCI)", f"{latest:+.2f}",
                  f"< {cfg['nfci_max']} (loose)", ok)


def _spy_state(cfg: dict) -> tuple[Signal, Signal, bool, bool, bool]:
    spy = data_io.get_ohlcv(["SPY"], period="2y")["SPY"]
    close = spy["Close"]
    ma50 = close.rolling(50).mean()
    ma200 = close.rolling(200).mean()
    last = float(close.iloc[-1])
    above_200 = last > float(ma200.iloc[-1])
    aligned = float(ma50.iloc[-1]) > float(ma200.iloc[-1])
    slope_up = float(ma200.iloc[-1]) > float(ma200.iloc[-22])
    trending_bull = above_200 and aligned and slope_up

    hi63 = float(spy["High"].tail(63).max())
    lo63 = float(spy["Low"].tail(63).min())
    range_pct = (hi63 - lo63) / last
    ranging = range_pct < cfg["spy_range_pct"] and not aligned

    trend_sig = Signal(
        "SPY trend", f"{last:.0f} vs 200DMA {float(ma200.iloc[-1]):.0f}",
        "Close > 200DMA, 50DMA > 200DMA, 200DMA slope up over 21d",
        trending_bull,
    )
    range_sig = Signal(
        "SPY range check", f"63d range {range_pct:.1%}",
        f"ranging if < {cfg['spy_range_pct']:.0%} and no MA alignment",
        None,
    )
    return trend_sig, range_sig, trending_bull, ranging, above_200


def classify(cfg: dict) -> RegimeResult:
    rc = cfg["regime"]
    credit = _credit_signal(rc)
    curve = _curve_signal()
    vix = _vix_signal(rc)
    nfci = _nfci_signal(rc)
    trend_sig, range_sig, trending_bull, ranging, spy_above_200 = _spy_state(rc)

    signals = [credit, curve, vix, nfci, trend_sig, range_sig]
    macro_passes = sum(1 for s in (credit, vix, nfci) if s.passed)

    if (not credit.passed and not vix.passed) or not spy_above_200:
        label = "RISK_OFF"
        why = ("SPY below its 200DMA" if not spy_above_200
               else "credit and volatility both stressed")
        expl = f"No new long ideas: {why}."
    elif trending_bull and macro_passes >= 2:
        label = "RISK_ON_TRENDING"
        expl = (f"SPY in confirmed uptrend and {macro_passes}/3 macro checks risk-on "
                "— full idea generation.")
    elif ranging and macro_passes >= 2:
        label = "RISK_ON_RANGING"
        expl = ("Macro is supportive but SPY is range-bound — "
                "pullback-to-value setups preferred.")
    else:
        label = "TRANSITION"
        expl = (f"Mixed signals ({macro_passes}/3 macro risk-on, "
                f"trend {'intact' if trending_bull else 'unconfirmed'}) — "
                "output list halved, size down.")

    return RegimeResult(label, expl, signals)


if __name__ == "__main__":
    import yaml
    from pathlib import Path

    cfg = yaml.safe_load((Path(__file__).resolve().parent.parent / "config.yaml").read_text())
    r = classify(cfg)
    print(f"\nREGIME: {r.label}\n{r.explanation}\n")
    for s in r.signals:
        mark = "·" if s.passed is None else ("PASS" if s.passed else "FAIL")
        print(f"  [{mark:>4}] {s.name}: {s.value}  — rule: {s.rule}")
