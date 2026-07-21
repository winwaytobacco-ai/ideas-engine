"""Universe construction: S&P 500 + Nasdaq-100 constituents from Wikipedia.

Cached to data/universe/universe_YYYY-MM-DD.csv; falls back to the most
recent cache if the scrape fails.
"""
from __future__ import annotations

import io
import logging
from datetime import date
from pathlib import Path

import pandas as pd
import requests

ROOT = Path(__file__).resolve().parent.parent
UNIVERSE_DIR = ROOT / "data" / "universe"
UNIVERSE_DIR.mkdir(parents=True, exist_ok=True)

log = logging.getLogger("ideas_engine.universe")

WIKI_SP500 = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
WIKI_NDX = "https://en.wikipedia.org/wiki/List_of_NASDAQ-100_companies"
_WIKI_UA = {"User-Agent": "ideas-engine/1.0 (personal research tool; contact: local)"}

GICS_TO_ETF = {
    "Information Technology": "XLK",
    "Financials": "XLF",
    "Energy": "XLE",
    "Health Care": "XLV",
    "Industrials": "XLI",
    "Consumer Staples": "XLP",
    "Consumer Discretionary": "XLY",
    "Materials": "XLB",
    "Utilities": "XLU",
    "Real Estate": "XLRE",
    "Communication Services": "XLC",
}
# Thematic ETFs map onto the GICS sector whose members they overlap most,
# so a selected thematic still filters the stock universe sensibly.
THEMATIC_TO_GICS = {
    "SMH": "Information Technology",
    "IGV": "Information Technology",
    "XBI": "Health Care",
}


# Wikipedia's NASDAQ-100 list uses ICB industries, not GICS. Only NDX-only
# names fall through to this mapping (dual-listed names keep S&P 500 GICS).
ICB_TO_GICS = {
    "Technology": "Information Technology",
    "Telecommunications": "Communication Services",
    "Health Care": "Health Care",
    "Consumer Discretionary": "Consumer Discretionary",
    "Consumer Staples": "Consumer Staples",
    "Industrials": "Industrials",
    "Financials": "Financials",
    "Basic Materials": "Materials",
    "Energy": "Energy",
    "Utilities": "Utilities",
    "Real Estate": "Real Estate",
}


def _read_tables(url: str) -> list[pd.DataFrame]:
    resp = requests.get(url, headers=_WIKI_UA, timeout=30)
    resp.raise_for_status()
    return pd.read_html(io.StringIO(resp.text))


def _find_constituent_table(tables: list[pd.DataFrame]) -> pd.DataFrame:
    for t in tables:
        cols = [str(c) for c in t.columns]
        has_ticker = any(c in ("Symbol", "Ticker") for c in cols)
        has_sector = any("GICS Sector" in c or "ICB Industry" in c for c in cols)
        if has_ticker and has_sector and len(t) > 50:
            return t
    raise ValueError("no constituent table found")


def _normalise(t: pd.DataFrame, index_name: str) -> pd.DataFrame:
    cols = {str(c): c for c in t.columns}
    ticker_col = cols.get("Symbol", cols.get("Ticker"))
    name_col = next((cols[c] for c in ("Security", "Company") if c in cols), ticker_col)
    sector_col = next(cols[c] for c in cols if "GICS Sector" in c or "ICB Industry" in c)
    sectors = t[sector_col].astype(str).str.strip()
    if "ICB Industry" in str(sector_col):
        sectors = sectors.map(lambda x: ICB_TO_GICS.get(x, x))
    df = pd.DataFrame({
        "ticker": t[ticker_col].astype(str).str.strip(),
        "name": t[name_col].astype(str).str.strip(),
        "sector": sectors,
    })
    df["index_membership"] = index_name
    return df


def load_universe() -> pd.DataFrame:
    """Return DataFrame [ticker, name, sector, sector_etf, index_membership]."""
    cache = UNIVERSE_DIR / f"universe_{date.today().isoformat()}.csv"
    if cache.exists():
        return pd.read_csv(cache)

    try:
        sp500 = _normalise(_find_constituent_table(_read_tables(WIKI_SP500)), "SP500")
        ndx = _normalise(_find_constituent_table(_read_tables(WIKI_NDX)), "NDX100")
        uni = pd.concat([sp500, ndx], ignore_index=True)
        # keep first occurrence; note dual membership
        dual = set(sp500["ticker"]) & set(ndx["ticker"])
        uni = uni.drop_duplicates(subset="ticker", keep="first").copy()
        uni.loc[uni["ticker"].isin(dual), "index_membership"] = "SP500+NDX100"
        # yfinance ticker format (BRK.B -> BRK-B)
        uni["ticker"] = uni["ticker"].str.replace(".", "-", regex=False)
        uni["sector_etf"] = uni["sector"].map(GICS_TO_ETF)
        uni = uni.dropna(subset=["sector_etf"]).reset_index(drop=True)
        uni.to_csv(cache, index=False)
        return uni
    except Exception as e:
        log.warning("universe scrape failed (%s); using most recent cache", e)
        caches = sorted(UNIVERSE_DIR.glob("universe_*.csv"))
        if not caches:
            raise RuntimeError("universe scrape failed and no cache exists") from e
        return pd.read_csv(caches[-1])


if __name__ == "__main__":
    u = load_universe()
    print(f"{len(u)} names")
    print(u["sector"].value_counts())
    print(u.head())
