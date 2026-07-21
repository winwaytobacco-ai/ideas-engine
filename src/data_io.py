"""Data access layer: FRED macro series + yfinance OHLCV, with local caching.

FRED: uses `fredapi` when FRED_API_KEY is set (env or .env); otherwise falls
back to FRED's public keyless CSV endpoint (fredgraph.csv).
OHLCV: batch yfinance downloads cached per-ticker as parquet; re-downloaded
only when the cache is older than `max_age_days`.
"""
from __future__ import annotations

import io
import logging
import os
import time
from pathlib import Path

import pandas as pd
import requests

try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).resolve().parent.parent / ".env")
except ImportError:
    pass

ROOT = Path(__file__).resolve().parent.parent
CACHE_DIR = ROOT / "data" / "cache"
CACHE_DIR.mkdir(parents=True, exist_ok=True)

log = logging.getLogger("ideas_engine.data_io")

FRED_CSV_URL = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}&cosd={start}"
FRED_LOOKBACK_YEARS = 3
# FRED drops connections from browser-spoofed UAs but serves the requests
# default UA fine — send no custom User-Agent here.
_UA: dict[str, str] = {}


def _tz_naive(df: pd.DataFrame) -> pd.DataFrame:
    df.index = pd.DatetimeIndex(df.index).tz_localize(None)
    return df


def _cache_fresh(path: Path, max_age_days: float) -> bool:
    return path.exists() and (time.time() - path.stat().st_mtime) < max_age_days * 86400


# ---------------------------------------------------------------- FRED ------

def get_fred_series(series_id: str, max_age_days: float = 1.0) -> pd.Series:
    """Return a FRED series as a tz-naive, NaN-dropped pd.Series."""
    cache = CACHE_DIR / f"fred_{series_id}.csv"
    if _cache_fresh(cache, max_age_days):
        df = pd.read_csv(cache, index_col=0, parse_dates=True)
        return df.iloc[:, 0].dropna()

    start = (pd.Timestamp.today() - pd.DateOffset(years=FRED_LOOKBACK_YEARS)).date().isoformat()
    api_key = os.environ.get("FRED_API_KEY")
    if api_key:
        from fredapi import Fred
        s = Fred(api_key=api_key).get_series(series_id, observation_start=start)
        s.name = series_id
    else:
        url = FRED_CSV_URL.format(sid=series_id, start=start)
        last_err = None
        for attempt in range(3):
            try:
                resp = requests.get(url, headers=_UA, timeout=60)
                resp.raise_for_status()
                break
            except requests.RequestException as e:
                last_err = e
                log.warning("FRED fetch %s attempt %d failed: %s", series_id, attempt + 1, e)
                time.sleep(2 * (attempt + 1))
        else:
            raise last_err
        raw = pd.read_csv(io.StringIO(resp.text))
        raw.columns = ["date", series_id]
        raw["date"] = pd.to_datetime(raw["date"])
        raw[series_id] = pd.to_numeric(raw[series_id], errors="coerce")
        s = raw.set_index("date")[series_id]

    s = s.dropna()
    s.index = pd.DatetimeIndex(s.index).tz_localize(None)
    s.to_frame().to_csv(cache)
    return s


# --------------------------------------------------------------- OHLCV ------

def _ticker_cache(ticker: str) -> Path:
    return CACHE_DIR / f"{ticker.replace('/', '-')}.parquet"


def _extract_single(batch: pd.DataFrame, ticker: str) -> pd.DataFrame | None:
    """Pull one ticker's OHLCV frame out of a (possibly MultiIndex) batch."""
    try:
        if isinstance(batch.columns, pd.MultiIndex):
            if ticker not in batch.columns.get_level_values(0):
                return None
            df = batch[ticker].copy()
        else:
            df = batch.copy()
    except (KeyError, TypeError):
        return None
    df = df.dropna(how="all")
    if df.empty or "Close" not in df.columns:
        return None
    return _tz_naive(df)


def get_ohlcv(
    tickers: list[str],
    period: str = "2y",
    max_age_days: float = 3.0,
    chunk_size: int = 100,
) -> dict[str, pd.DataFrame]:
    """Download (or read cached) daily OHLCV for each ticker.

    Failed tickers are logged and skipped — never crash the run.
    """
    import yfinance as yf

    out: dict[str, pd.DataFrame] = {}
    to_download: list[str] = []

    for t in tickers:
        cache = _ticker_cache(t)
        if _cache_fresh(cache, max_age_days):
            try:
                out[t] = pd.read_parquet(cache)
                continue
            except Exception:
                cache.unlink(missing_ok=True)
        to_download.append(t)

    for i in range(0, len(to_download), chunk_size):
        batch_tickers = to_download[i : i + chunk_size]
        log.info("downloading %d tickers (%d/%d done)", len(batch_tickers), i, len(to_download))
        try:
            batch = yf.download(
                batch_tickers, period=period, group_by="ticker",
                auto_adjust=True, threads=True, progress=False,
            )
        except Exception as e:
            log.warning("batch download failed (%s); falling back to singles", e)
            batch = None

        for t in batch_tickers:
            df = _extract_single(batch, t) if batch is not None else None
            if df is None:
                try:
                    single = yf.download(t, period=period, auto_adjust=True, progress=False)
                    df = _extract_single(single, t)
                except Exception:
                    df = None
            if df is None or len(df) < 60:
                log.warning("skipping %s: no usable data", t)
                continue
            df.to_parquet(_ticker_cache(t))
            out[t] = df

    return out
