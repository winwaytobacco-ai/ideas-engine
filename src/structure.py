"""Layer 4 — AMT structure qualification on the daily timeframe.

Composite volume profile (POC/VAH/VAL, HVN/LVN), daily volume-flow proxy
(true CVD needs intraday data — documented v1 simplification), anchored
VWAP from the 126-day swing low, setup classification, structure score.
"""
from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd


@dataclass
class VolumeProfile:
    poc: float
    vah: float
    val: float
    hvns: list[float]
    lvns: list[float]
    poc_prominence: float          # POC bin volume / mean bin volume
    bin_centers: list[float] = field(default_factory=list)
    bin_volumes: list[float] = field(default_factory=list)


@dataclass
class StructureResult:
    ticker: str
    setup: str                     # ACCEPTANCE_BREAKOUT | PULLBACK_TO_VALUE | NO_SETUP
    score: float
    profile: VolumeProfile
    avwap: float
    avwap_dist: float              # (close - avwap) / avwap
    flow_state: str                # confirming | diverging | neutral
    atr: float
    close: float
    hi52: float
    breakout_age: int | None = None
    notes: list[str] = field(default_factory=list)


def volume_profile(df: pd.DataFrame, lookback: int, bins: int, va_pct: float) -> VolumeProfile:
    w = df.tail(lookback)
    tp = (w["High"] + w["Low"] + w["Close"]) / 3
    vol = w["Volume"].to_numpy(dtype=float)
    lo, hi = float(w["Low"].min()), float(w["High"].max())
    hist, edges = np.histogram(tp.to_numpy(dtype=float), bins=bins, range=(lo, hi), weights=vol)
    centers = (edges[:-1] + edges[1:]) / 2

    poc_i = int(hist.argmax())
    total = hist.sum()

    # Value area: expand from POC toward the higher-volume neighbour
    in_va = {poc_i}
    acc = hist[poc_i]
    lo_i, hi_i = poc_i, poc_i
    while acc < va_pct * total and (lo_i > 0 or hi_i < bins - 1):
        below = hist[lo_i - 1] if lo_i > 0 else -1.0
        above = hist[hi_i + 1] if hi_i < bins - 1 else -1.0
        if above >= below:
            hi_i += 1
            acc += hist[hi_i]
            in_va.add(hi_i)
        else:
            lo_i -= 1
            acc += hist[lo_i]
            in_va.add(lo_i)

    # HVN/LVN: significant peaks/troughs only — a peak must dominate its
    # +/-2 bin neighbourhood and clear 1.2x mean volume, otherwise every
    # ripple in a 50-bin histogram becomes a "node" and targets collapse.
    smooth = np.convolve(hist, np.ones(3) / 3, mode="same")
    mean_v = smooth.mean()
    hvns, lvns = [], []
    for i in range(2, bins - 2):
        window = smooth[i - 2 : i + 3]
        if smooth[i] == window.max() and smooth[i] > 1.2 * mean_v:
            hvns.append(float(centers[i]))
        if smooth[i] == window.min() and smooth[i] < 0.8 * mean_v:
            lvns.append(float(centers[i]))

    return VolumeProfile(
        poc=float(centers[poc_i]),
        vah=float(edges[max(in_va) + 1]),
        val=float(edges[min(in_va)]),
        hvns=hvns, lvns=lvns,
        poc_prominence=float(hist[poc_i] / hist.mean()) if hist.mean() > 0 else 0.0,
        bin_centers=[float(c) for c in centers],
        bin_volumes=[float(v) for v in hist],
    )


def flow_line(df: pd.DataFrame) -> pd.Series:
    """Daily CVD proxy: cumulative sign(Close-Open) * Volume."""
    delta = np.sign(df["Close"] - df["Open"]) * df["Volume"]
    return delta.cumsum()


def flow_state(df: pd.DataFrame, flow: pd.Series, window: int = 21) -> str:
    half = window // 2
    price_recent = float(df["Close"].iloc[-half:].max())
    price_prior = float(df["Close"].iloc[-window:-half].max())
    flow_recent = float(flow.iloc[-half:].max())
    flow_prior = float(flow.iloc[-window:-half].max())
    price_hh = price_recent > price_prior
    flow_hh = flow_recent > flow_prior
    if price_hh and flow_hh:
        return "confirming"
    if price_hh and not flow_hh:
        return "diverging"
    return "neutral"


def anchored_vwap(df: pd.DataFrame, lookback: int) -> float:
    w = df.tail(lookback)
    anchor = w["Low"].idxmin()
    seg = df.loc[anchor:]
    tp = (seg["High"] + seg["Low"] + seg["Close"]) / 3
    return float((tp * seg["Volume"]).sum() / seg["Volume"].sum())


def atr(df: pd.DataFrame, period: int) -> float:
    hl = df["High"] - df["Low"]
    hc = (df["High"] - df["Close"].shift()).abs()
    lc = (df["Low"] - df["Close"].shift()).abs()
    tr = pd.concat([hl, hc, lc], axis=1).max(axis=1)
    return float(tr.rolling(period).mean().iloc[-1])


def _breakout_state(close: pd.Series, vah: float, min_sessions: int, max_age: int):
    """Return (is_acceptance_breakout, streak_length) for closes above VAH."""
    above = (close > vah).to_numpy()
    streak = 0
    for v in above[::-1]:
        if v:
            streak += 1
        else:
            break
    return (min_sessions <= streak <= max_age), streak


def analyse(ticker: str, df: pd.DataFrame, cfg: dict) -> StructureResult:
    st = cfg["structure"]
    lookback = st["lookback_days"]

    vp = volume_profile(df, lookback, st["vp_bins"], st["value_area_pct"])
    av = anchored_vwap(df, lookback)
    flow = flow_line(df.tail(lookback))
    fstate = flow_state(df, flow)
    close = float(df["Close"].iloc[-1])
    a = atr(df, cfg["trade"]["atr_period"])
    hi52 = float(df["Close"].tail(252).max())
    avwap_dist = (close - av) / av

    ma50 = float(df["Close"].rolling(50).mean().iloc[-1])
    ma200 = float(df["Close"].rolling(200).mean().iloc[-1])
    uptrend = close > ma200 and ma50 > ma200
    above_avwap = close > av

    is_bo, streak = _breakout_state(df["Close"], vp.vah, st["breakout_min_sessions"],
                                    st["breakout_max_age"])
    tol = st["pullback_poc_tolerance"]
    near_poc = abs(close - vp.poc) / vp.poc <= tol
    near_hvn = any(abs(close - h) / h <= tol for h in vp.hvns)

    notes: list[str] = []
    if is_bo and fstate == "confirming":
        setup = "ACCEPTANCE_BREAKOUT"
        notes.append(f"{streak} consecutive closes above VAH with flow confirmation")
    elif uptrend and above_avwap and (near_poc or near_hvn):
        setup = "PULLBACK_TO_VALUE"
        notes.append("pullback holding value area within uptrend, above AVWAP")
    else:
        setup = "NO_SETUP"
        if is_bo and fstate != "confirming":
            notes.append("closes above VAH but flow not confirming")
        if streak > st["breakout_max_age"]:
            notes.append(f"breakout extended ({streak} sessions above VAH)")
        if not above_avwap:
            notes.append("below anchored VWAP")

    score = 0.0
    if setup != "NO_SETUP":
        score += 40
    if fstate == "confirming":
        score += 20
    elif fstate == "diverging":
        score -= 20
    if 0 <= avwap_dist <= 0.05:
        score += 20 * (1 - avwap_dist / 0.05)
    score += min(vp.poc_prominence / 3.0, 1.0) * 20
    score = max(0.0, min(100.0, score))

    return StructureResult(
        ticker=ticker, setup=setup, score=round(score, 1), profile=vp,
        avwap=round(av, 2), avwap_dist=avwap_dist, flow_state=fstate,
        atr=round(a, 2), close=close, hi52=hi52,
        breakout_age=streak if streak else None, notes=notes,
    )


if __name__ == "__main__":
    import yaml
    from pathlib import Path
    from . import data_io

    cfg = yaml.safe_load((Path(__file__).resolve().parent.parent / "config.yaml").read_text())
    data = data_io.get_ohlcv(["NVDA", "MU", "AVGO"], period="2y")
    for t, df in data.items():
        r = analyse(t, df, cfg)
        p = r.profile
        print(f"\n{t}: close {r.close:.2f} | POC {p.poc:.2f} VAH {p.vah:.2f} VAL {p.val:.2f} "
              f"| AVWAP {r.avwap:.2f} ({r.avwap_dist:+.1%}) | flow {r.flow_state} "
              f"| ATR {r.atr:.2f}\n  setup={r.setup} score={r.score} notes={r.notes}")
