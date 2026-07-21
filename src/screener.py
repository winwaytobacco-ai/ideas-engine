"""Layer 3 — Stock screen over the members of the Layer-2 selected sectors.

Eight hard filters (all thresholds in config.yaml). Also computes per-sector
breadth (% of members above 50DMA) as the Layer-2 cross-check.
"""
from __future__ import annotations

import logging
from dataclasses import dataclass, field

import pandas as pd

from . import data_io

log = logging.getLogger("ideas_engine.screener")

FILTER_NAMES = {
    "f_sector": "in selected sector",
    "f_price": "price > min",
    "f_liquidity": "avg $ volume > min",
    "f_trend": "close > 200DMA",
    "f_alignment": "50DMA > 200DMA",
    "f_leadership": "near 52w high",
    "f_rel_strength": "63d return beats SPY",
}


@dataclass
class ScreenResult:
    candidates: pd.DataFrame          # passed all filters, with metrics
    near_misses: pd.DataFrame         # failed exactly one filter
    breadth: dict[str, float]         # GICS sector -> % members above 50DMA
    ohlcv: dict[str, pd.DataFrame] = field(default_factory=dict)
    n_screened: int = 0


def run(universe: pd.DataFrame, selected_gics: list[str], regime_label: str,
        cfg: dict, theme: dict | None = None) -> ScreenResult:
    """theme = {"label": str, "members": [tickers], "selected": bool} or None."""
    sc = cfg["screen"]
    members = universe[universe["sector"].isin(selected_gics)].copy()
    theme_set: set[str] = set()
    theme_label = None
    if theme and theme.get("selected"):
        theme_set = set(theme["members"])
        theme_label = theme["label"]
        extra = universe[universe["ticker"].isin(theme_set)
                         & ~universe["ticker"].isin(members["ticker"])].copy()
        extra["sector"] = theme_label   # pseudo-sector for screening purposes
        members = pd.concat([members, extra], ignore_index=True)
    tickers = members["ticker"].tolist()
    log.info("screening %d members of %s%s", len(tickers), selected_gics,
             f" + {theme_label}" if theme_label else "")

    data = data_io.get_ohlcv(tickers + ["SPY"], period="2y")
    spy_close = data["SPY"]["Close"]
    spy_ret63 = float(spy_close.iloc[-1] / spy_close.iloc[-64] - 1)

    max_from_high = (sc["max_pct_from_52w_high_ranging"]
                     if regime_label == "RISK_ON_RANGING"
                     else sc["max_pct_from_52w_high"])

    rows = []
    above_50 = {g: [0, 0] for g in selected_gics}   # sector -> [above, total]
    if theme_label:
        above_50[theme_label] = [0, 0]

    for _, m in members.iterrows():
        t = m["ticker"]
        df = data.get(t)
        if df is None or len(df) < 210:
            continue
        close = df["Close"]
        last = float(close.iloc[-1])
        ma50 = float(close.rolling(50).mean().iloc[-1])
        ma200 = float(close.rolling(200).mean().iloc[-1])
        adv21 = float((close * df["Volume"]).rolling(21).mean().iloc[-1])
        hi52 = float(close.tail(252).max())
        pct_from_high = (hi52 - last) / hi52
        ret63 = float(last / close.iloc[-64] - 1)
        rel63 = ret63 - spy_ret63

        b = above_50[m["sector"]]
        b[1] += 1
        if last > ma50:
            b[0] += 1
        if theme_label and t in theme_set and m["sector"] != theme_label:
            tb = above_50[theme_label]   # theme breadth counts dual members too
            tb[1] += 1
            if last > ma50:
                tb[0] += 1

        checks = {
            "f_sector": True,   # membership guaranteed by construction
            "f_price": last > sc["min_price"],
            "f_liquidity": adv21 > sc["min_avg_dollar_vol"],
            "f_trend": last > ma200,
            "f_alignment": ma50 > ma200,
            "f_leadership": pct_from_high <= max_from_high,
            "f_rel_strength": rel63 > 0,
        }
        rows.append({
            "ticker": t, "name": m["name"], "sector": m["sector"],
            "theme": bool(t in theme_set),
            "price": last, "adv21": adv21, "ma50": ma50, "ma200": ma200,
            "pct_from_52w_high": pct_from_high, "ret63": ret63, "rel63": rel63,
            **checks,
            "n_failed": sum(1 for v in checks.values() if not v),
        })

    all_rows = pd.DataFrame(rows)
    breadth = {g: (v[0] / v[1] if v[1] else float("nan")) for g, v in above_50.items()}
    if all_rows.empty:
        return ScreenResult(all_rows, all_rows, breadth, {}, 0)

    candidates = all_rows[all_rows["n_failed"] == 0].copy()
    near = all_rows[all_rows["n_failed"] == 1].copy()
    near["failed_filter"] = near.apply(
        lambda r: next(FILTER_NAMES[k] for k in FILTER_NAMES if not r[k]), axis=1)

    # RS percentile among candidates (used in final ranking)
    if not candidates.empty:
        candidates["rs_percentile"] = candidates["rel63"].rank(pct=True)

    ohlcv = {t: data[t] for t in candidates["ticker"] if t in data}
    return ScreenResult(
        candidates.sort_values("rel63", ascending=False).reset_index(drop=True),
        near.sort_values("rel63", ascending=False).reset_index(drop=True),
        breadth, ohlcv, len(all_rows),
    )


if __name__ == "__main__":
    import yaml
    from pathlib import Path
    from .universe import load_universe
    from . import sectors as sectors_mod

    logging.basicConfig(level=logging.INFO, format="%(message)s")
    cfg = yaml.safe_load((Path(__file__).resolve().parent.parent / "config.yaml").read_text())
    sec = sectors_mod.analyse(cfg)
    res = run(load_universe(), sec.selected_gics(), "RISK_ON_TRENDING", cfg)
    print(f"\nScreened {res.n_screened}; {len(res.candidates)} candidates, "
          f"{len(res.near_misses)} near-misses")
    print("Breadth:", {k: f"{v:.0%}" for k, v in res.breadth.items()})
    cols = ["ticker", "sector", "price", "pct_from_52w_high", "rel63"]
    print(res.candidates[cols].to_string(index=False))
