"""Thematic pseudo-sectors (v1: AI infrastructure).

The theme is an equal-weight basket of curated members that runs through the
SAME relative-strength math as the SPDR sectors (RS-ratio / RS-momentum /
quadrant vs SPY). Selection is additive: if the basket sits in Leading or
Improving, its members join the stock screen alongside the top-N sectors.

Every theme member must additionally pass a fundamentals gate — "backed by
real earnings and orders from buyers". Free-data proxies (documented):
positive trailing EPS, quarterly YoY revenue growth, and forward EPS above
trailing (rising analyst estimates stand in for order-book/backlog data,
which no free feed provides).
"""
from __future__ import annotations

import json
import logging
import time
from pathlib import Path

import pandas as pd

from . import data_io
from .sectors import SectorRow, _quadrant

log = logging.getLogger("ideas_engine.themes")

THEME_KEY = "AI_INFRA"
FUND_CACHE_DAYS = 7.0


def _basket_series(members: list[str], data: dict[str, pd.DataFrame]) -> pd.Series:
    """Equal-weight index: each member's close normalised to 1.0, then averaged."""
    closes = pd.concat(
        {t: data[t]["Close"] for t in members if t in data}, axis=1).dropna()
    normed = closes / closes.iloc[0]
    return normed.mean(axis=1)


def pseudo_sector_row(cfg: dict) -> SectorRow | None:
    """Run the theme basket through the Layer-2 math; None if disabled/no data."""
    tc = cfg.get("themes", {}).get("ai_infra", {})
    if not tc.get("enabled"):
        return None
    members = tc["members"]
    data = data_io.get_ohlcv(members + ["SPY"], period="2y")
    have = [t for t in members if t in data]
    if len(have) < 5:
        log.warning("AI-infra theme: only %d members downloadable — skipping", len(have))
        return None

    basket = _basket_series(have, data)
    spy = data["SPY"]["Close"]
    pair = pd.concat([basket.rename("b"), spy.rename("spy")], axis=1).dropna()
    c, s = pair["b"], pair["spy"]
    if len(pair) < 150:
        return None

    rel21 = (c.iloc[-1] / c.iloc[-22] - 1) - (s.iloc[-1] / s.iloc[-22] - 1)
    rel63 = (c.iloc[-1] / c.iloc[-64] - 1) - (s.iloc[-1] / s.iloc[-64] - 1)
    ratio = c / s
    rs_ratio = ratio / ratio.rolling(126).mean() * 100
    rs_mom = (rs_ratio / rs_ratio.shift(21) - 1) * 100
    rr, rm = float(rs_ratio.iloc[-1]), float(rs_mom.iloc[-1])
    trail = [
        {"r": round(float(rs_ratio.iloc[-1 - k]), 2), "m": round(float(rs_mom.iloc[-1 - k]), 2)}
        for k in range(0, 40, 8)
    ][::-1]

    return SectorRow(
        etf=THEME_KEY,
        name=tc.get("label", "AI Infrastructure"),
        rel_21d=float(rel21) * 100,
        rel_63d=float(rel63) * 100,
        composite=float(rel21 + rel63) / 2 * 100,
        rs_ratio=rr,
        rs_momentum=rm,
        quadrant=_quadrant(rr, rm),
        trail=trail,
    )


# ------------------------------------------------------------- fundamentals --

def _fund_cache(ticker: str) -> Path:
    return data_io.CACHE_DIR / f"fundamentals_{ticker}.json"


def get_fundamentals(ticker: str) -> dict:
    """Fetch (or read cached) fundamental snapshot from yfinance."""
    cache = _fund_cache(ticker)
    if cache.exists() and (time.time() - cache.stat().st_mtime) < FUND_CACHE_DAYS * 86400:
        return json.loads(cache.read_text())

    import yfinance as yf
    out: dict = {"ticker": ticker}
    try:
        info = yf.Ticker(ticker).info or {}
        for k in ("trailingEps", "forwardEps", "revenueGrowth", "earningsGrowth",
                  "profitMargins", "totalRevenue"):
            v = info.get(k)
            out[k] = float(v) if isinstance(v, (int, float)) else None
    except Exception as e:
        log.warning("fundamentals fetch failed for %s: %s", ticker, e)
        out["error"] = str(e)
    cache.write_text(json.dumps(out))
    return out


def earnings_backed(f: dict, cfg: dict) -> tuple[bool, list[str], list[str]]:
    """Apply the "real earnings + orders" gate. Returns (passed, evidence, failures)."""
    rules = cfg["themes"]["ai_infra"]["fundamentals"]
    evidence, failures = [], []

    te, fe = f.get("trailingEps"), f.get("forwardEps")
    rg, eg = f.get("revenueGrowth"), f.get("earningsGrowth")

    if te is None or (rules.get("require_positive_eps") and te <= 0):
        failures.append("no positive trailing EPS — the AI story is not yet in the income statement"
                        if te is not None else "trailing EPS unavailable")
    else:
        evidence.append(f"Profitable today: trailing 12m EPS {te:.2f}"
                        + (f", net margin {f['profitMargins']:.0%}" if f.get("profitMargins") else ""))

    if rg is None or rg < rules["min_revenue_growth"]:
        failures.append(
            f"revenue growth {rg:+.0%} below the {rules['min_revenue_growth']:.0%} bar"
            if rg is not None else "revenue growth unavailable")
    else:
        evidence.append(f"Real demand: quarterly revenue growing {rg:+.0%} YoY")

    if fe is not None and te is not None and fe > te:
        evidence.append(f"Order-book proxy: forward EPS {fe:.2f} above trailing {te:.2f} "
                        "— analysts see the pipeline growing")
    elif eg is not None and eg > 0.10:
        evidence.append(f"Earnings growing {eg:+.0%} YoY (forward estimates unavailable)")
    else:
        failures.append("forward estimates do not exceed trailing earnings — "
                        "no visible order momentum")

    return (len(failures) == 0, evidence, failures)


if __name__ == "__main__":
    import yaml
    cfg = yaml.safe_load((Path(__file__).resolve().parent.parent / "config.yaml").read_text())
    row = pseudo_sector_row(cfg)
    if row:
        print(f"{row.etf}: {row.quadrant} | RS-ratio {row.rs_ratio:.1f} "
              f"RS-mom {row.rs_momentum:+.2f}% | 21d {row.rel_21d:+.2f}% 63d {row.rel_63d:+.2f}%")
    for t in cfg["themes"]["ai_infra"]["members"][:5]:
        f = get_fundamentals(t)
        ok, ev, fail = earnings_backed(f, cfg)
        print(f"\n{t}: {'BACKED' if ok else 'NOT BACKED'}")
        for e in ev:
            print(f"  + {e}")
        for x in fail:
            print(f"  - {x}")
