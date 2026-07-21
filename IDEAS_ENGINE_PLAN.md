# IDEAS ENGINE — Implementation Plan (v1.0)

**Status:** LOCKED PLAN — seed context for Claude Code
**Owner:** Nelson
**Purpose:** Weekly systematic generation of 1–3 month position trade ideas (US equities)
**Date:** 2026-07-11

---

## 0. Scope & Hard Constraints

- **US stock market only.** Common stock listed on NYSE / NASDAQ / AMEX. No options, no futures, no crypto.
- ETFs are used **only as inputs** (sector rotation signals, SPY benchmark). ETFs are never output as trade ideas.
- **Long-only in v1.** Short ideas are a future extension (Section 12).
- Timeframe: **daily bars**, holding period 1–3 months. This is NOT an intraday tool.
- Output: a ranked idea report + watchlist CSV, produced by a single weekend run.
- Free data only in v1: FRED (`fredapi`) + `yfinance`. No IBKR dependency in v1.

## 1. Design Philosophy

Idea generation is a **funnel with hard gates**, consistent with the existing Valentini
stack (regime classifier as master gate; VP/CVD/VWAP only inside a favourable regime):

```
Layer 1  MACRO REGIME  ──gate──▶  Layer 2  SECTOR ROTATION  ──filter──▶
Layer 3  STOCK SCREEN  ──filter──▶  Layer 4  AMT STRUCTURE  ──score──▶
Layer 5  TRADE CONSTRUCTION + REPORT
```

Each layer only sees survivors of the previous layer. If Layer 1 says risk-off,
the run still completes but outputs "NO NEW LONG IDEAS" with the regime evidence.

## 2. Environment

- **Machine:** Windows, project root `C:\Users\leung\ideas_engine\` (sibling of `C:\Users\leung\demo\`).
- **Python:** 3.14 (same interpreter as the Valentini project). If any dependency
  fails to install on 3.14, fall back to a 3.12 virtual environment — decide in Phase 0.
- **Dependencies (requirements.txt):**
  `pandas`, `numpy`, `yfinance`, `fredapi`, `lxml` (Wikipedia table scrape),
  `pyyaml` (config), `matplotlib` (chart snapshots, optional).
- **Secrets:** FRED API key read from environment variable `FRED_API_KEY`
  (or a `.env` file loaded with `python-dotenv`). **Never hardcoded.**
- **Known pitfalls from previous projects (apply from day one):**
  - Use **relative paths / `pathlib.Path(__file__).parent`** everywhere. No hardcoded
    `C:\` or Linux paths.
  - yfinance returns timezone-aware indexes inconsistently → **normalise every
    downloaded frame** with `df.index = pd.DatetimeIndex(df.index).tz_localize(None)`
    before any `pd.concat`.
  - If matplotlib is used inside a library module, guard `matplotlib.use("Agg")`
    with `if __name__ == "__main__":` so it never hijacks another app's backend.
  - Python 3.14 asyncio: not needed in v1 (no `ib_async`). Keep v1 fully synchronous.

## 3. Project Structure

```
ideas_engine/
├── IDEAS_ENGINE_PLAN.md      ← this file (read-only seed context)
├── requirements.txt
├── config.yaml               ← ALL thresholds live here, nothing magic in code
├── run_ideas.bat             ← double-click launcher (weekend run)
├── main.py                   ← orchestrator: Layer 1 → 5, writes report
├── src/
│   ├── __init__.py
│   ├── data_io.py            ← yfinance/FRED download + local parquet cache
│   ├── regime.py             ← Layer 1
│   ├── universe.py           ← constituent lists (S&P 500 + Nasdaq-100)
│   ├── sectors.py            ← Layer 2
│   ├── screener.py           ← Layer 3
│   ├── structure.py          ← Layer 4 (VP, AVWAP, setup classification)
│   └── report.py             ← Layer 5 (markdown + CSV output)
├── data/
│   ├── cache/                ← OHLCV parquet cache (refreshed weekly)
│   └── universe/             ← cached constituent CSVs (fallback if scrape fails)
└── output/
    ├── IDEAS_REPORT_YYYY-MM-DD.md
    ├── watchlist_YYYY-MM-DD.csv
    └── IDEAS_LOG.csv          ← append-only audit trail, one row per idea
```

## 4. Layer 1 — Macro Regime (`regime.py`)

**Question answered:** Is the environment worth initiating long positions at all?

**Inputs (FRED unless noted):**

| Signal | Series | Rule (v1, rule-based & transparent) |
|---|---|---|
| Credit stress | `BAMLH0A0HYM2` (HY OAS) | Risk-on if latest < 21-day MA AND < 75th percentile of trailing 252 days |
| Yield curve | `T10Y2Y` | Informational flag only in v1 (log inverted/steepening state) |
| Volatility | `VIXCLS` | Risk-on if VIX < 22 AND VIX < its 50-day MA |
| Financial conditions | `NFCI` | Risk-on if NFCI < 0 (loose) |
| Equity trend | SPY via yfinance | Trending-bull if Close > 200DMA AND 50DMA > 200DMA AND 200DMA slope > 0 over 21 days |
| Range detection | SPY | Ranging if 63-day high-low range < 8% and no MA alignment |

**Regime classification logic:**
- `RISK_ON_TRENDING`  — equity trend bull + at least 2 of 3 macro checks (credit, VIX, NFCI) risk-on → **full idea generation**
- `RISK_ON_RANGING`   — macro fine but SPY ranging → generate ideas, flag "pullback-to-value setups preferred"
- `TRANSITION`        — mixed signals → generate ideas but halve the output list, add warning banner
- `RISK_OFF`          — credit + VIX both stressed, or SPY < 200DMA → **no new long ideas**; report shows evidence only

**Output:** `RegimeResult` dataclass: label, per-signal values, per-signal pass/fail, one-line
explanation. Serialised into the report header.

**v2 note (do NOT build in v1):** replace/augment rule-based classifier with the existing
HMM regime detector (`hmmlearn`, trending vs ranging) from `nvda_market_detection.py`.

## 5. Layer 2 — Sector Rotation (`sectors.py`)

**Inputs:** daily closes for the 11 SPDR sectors + thematic adds, vs SPY:
`XLK XLF XLE XLV XLI XLP XLY XLB XLU XLRE XLC` + `SMH IGV XBI` (thematics, config-extensible).

**Computation per ETF:**
1. **Relative return:** 21-day and 63-day total return minus SPY's return over same window.
2. **RS-Ratio proxy:** ratio series `ETF/SPY`, normalised to 100 over trailing 126 days.
3. **RS-Momentum proxy:** 21-day rate of change of the RS-Ratio.
4. **RRG quadrant:** Leading (ratio>100, mom>0), Improving (<100, >0), Weakening (>100, <0), Lagging (<100, <0).

**Selection rule:** rank by composite of 21d and 63d relative return (50/50 weight);
keep sectors in **Leading or Improving** quadrant only; take **top 3** (config: `sectors.top_n`).

**Breadth cross-check (computed from our own universe data, no paid feed):**
after Layer 3 downloads universe OHLCV, compute per-sector % of members above their 50DMA.
If a selected sector's breadth < 40%, flag it "narrow leadership" in the report (do not exclude in v1).

**Output:** ordered list of selected sector names + full ranking table for the report.

## 6. Layer 3 — Stock Screen (`screener.py`, `universe.py`)

**Universe construction (`universe.py`):**
- Scrape S&P 500 constituents from Wikipedia (`List of S&P 500 companies`) and
  Nasdaq-100 from Wikipedia — both tables include ticker + GICS sector. Use `pandas.read_html`.
- Deduplicate (~550 names). Convert tickers with dots for yfinance (`BRK.B` → `BRK-B`).
- Cache to `data/universe/universe_YYYY-MM-DD.csv`. If scrape fails, load the most recent cache.
- Map each GICS sector to its SPDR ETF so Layer 2's selected sectors filter the universe.

**Hard filters (all must pass; every threshold in `config.yaml`):**

| # | Filter | Default |
|---|---|---|
| 1 | Belongs to a Layer-2 selected sector | — |
| 2 | Price | > $10 |
| 3 | Liquidity: 21-day avg dollar volume | > $20M |
| 4 | Long-term trend: Close > 200DMA | — |
| 5 | MA alignment: 50DMA > 200DMA | — |
| 6 | Leadership: Close within 15% of 52-week high | 15% (loosen to 25% in RANGING regime) |
| 7 | Relative strength: 63-day return − SPY 63-day return | > 0 |
| 8 | Security type: common stock only (exclude anything the constituent lists mark otherwise) | — |

**Data handling:** batch-download OHLCV via `yfinance.download(tickers, period="2y", group_by="ticker")`,
write per-ticker parquet to `data/cache/`. On weekly rerun, only re-download if cache is > 3 days old.
Handle failed tickers gracefully (log and skip, never crash the run).

**Output:** `candidates` DataFrame (expect 15–40 names) with the metrics computed above.

## 7. Layer 4 — AMT Structure Qualification (`structure.py`)

Applies the Valentini toolkit on the **daily timeframe** to each candidate.

**7.1 Composite Volume Profile (126-day lookback):**
- Histogram of volume by price using 50 bins across the 126-day high-low range
  (volume of each day assigned to the bin containing that day's typical price
  `(H+L+C)/3`; v1 simplification, documented).
- **POC** = highest-volume bin. **Value Area** = smallest set of bins around POC
  containing 70% of volume → **VAH / VAL**.
- Identify HVNs (local volume peaks) and LVNs (local troughs) for target/stop logic.

**7.2 Volume-flow proxy (daily-timeframe CVD substitute):**
True CVD needs intraday delta — not available free. v1 proxy, documented as such:
- `daily_delta = sign(Close − Open) × Volume`; cumulative sum = **flow line**.
- Confirmation = flow line making higher highs alongside price over the last 21 days.
- Divergence (price higher high, flow lower high) = disqualify or penalise score.
- **v2 upgrade path:** real CVD from IBKR intraday data via `ib_async` (Section 12).

**7.3 Anchored VWAP:**
- Anchor at the lowest low of the 126-day window (major swing low).
- Volume-weighted mean of typical price from anchor to today.
- Requirement: Close > AVWAP.

**7.4 Setup classification (mutually exclusive):**

| Setup | Definition | Preferred regime |
|---|---|---|
| `ACCEPTANCE_BREAKOUT` | Close > VAH for ≥ 3 consecutive sessions, flow line confirming, breakout ≤ 10 sessions old | RISK_ON_TRENDING |
| `PULLBACK_TO_VALUE` | Uptrend intact (filters 4–5), price pulled back to within ±2% of POC or a marked HVN, holding above AVWAP | Any risk-on |
| `NO_SETUP` | Neither | — |

**7.5 Structure score (0–100):**
- Setup present: 40 pts
- Flow-line confirmation: 20 pts (divergence: −20)
- Distance above AVWAP 0–5%: 20 pts (further = extended, fewer points)
- Value area cleanliness (POC prominence, i.e. POC bin volume / mean bin volume): 20 pts

Candidates with `NO_SETUP` are dropped (listed in report appendix as "watch — no structure yet").

## 8. Layer 5 — Trade Construction & Report (`report.py`)

For each surviving name, construct the trade **mechanically**:

- **Entry:**
  - `PULLBACK_TO_VALUE` → limit at POC (or current price if already inside ±1% of POC).
  - `ACCEPTANCE_BREAKOUT` → buy-stop at retest of VAH (VAH + 0.5%).
- **Stop (structural, never %-based):** below VAL, or below AVWAP, whichever is nearer
  to entry but at least 1 ATR(14) away.
- **Target:** nearest overhead HVN above entry; if none, 52-week high; if at highs,
  measured move = value-area width projected from VAH.
- **R:R gate:** reject if reward/risk < 2.5 (config: `trade.min_rr`).
- **Free-flow marker:** price at which selling half the position returns original capital
  at the stop distance — printed per idea (consistent with existing NVDA/MU management style).

**Final ranking:** `total_score = structure_score × sector_rank_weight × RS_percentile`.
Report top 10 max (config: `report.max_ideas`; halved in TRANSITION regime).

**Outputs:**
1. `output/IDEAS_REPORT_YYYY-MM-DD.md` — sections: ① Regime verdict + evidence table,
   ② Sector rotation table, ③ Ranked ideas (thesis one-liner, setup type, entry/stop/target/RR,
   free-flow level), ④ Appendix: near-misses and no-setup watch names.
   Clean, minimal, single-page style — readable on iPad.
2. `output/watchlist_YYYY-MM-DD.csv` — ticker, setup, entry, stop, target, RR, score.
3. `output/IDEAS_LOG.csv` — append-only: run_date, regime, ticker, setup, entry, stop,
   target, rr, score, (outcome columns left blank for later manual audit).

## 9. Orchestration & Cadence

- `main.py` runs Layers 1→5 sequentially, prints progress per layer, total runtime target < 10 min.
- `run_ideas.bat` — activates the venv (if used) and runs `python main.py` (same pattern as `run_dashboard.bat`).
- **Cadence:** run every **weekend** (Saturday HKT). Weeknights: no rerun needed; act only on
  entries already defined in the report. Monthly: review `IDEAS_LOG.csv` hit rate per layer.

## 10. config.yaml (single source of truth)

Every number referenced above lives here. Skeleton:

```yaml
regime:
  vix_max: 22
  hyoas_percentile_max: 75
  nfci_max: 0.0
sectors:
  top_n: 3
  thematic_extra: [SMH, IGV, XBI]
screen:
  min_price: 10
  min_avg_dollar_vol: 20000000
  max_pct_from_52w_high: 0.15
structure:
  lookback_days: 126
  value_area_pct: 0.70
  vp_bins: 50
trade:
  min_rr: 2.5
report:
  max_ideas: 10
```

## 11. Implementation Phases for Claude Code

Work **one phase per session**. Each phase must pass its acceptance test before the next
begins. Explain each step before executing (owner is newer to Python — step-by-step preferred).

| Phase | Build | Acceptance test |
|---|---|---|
| **0** | Project scaffold, `requirements.txt`, `config.yaml`, `.env` handling, verify `fredapi` + `yfinance` work on Python 3.14 (fall back to 3.12 venv if not) | `python -c "import src"` clean; smoke script pulls VIXCLS and SPY without error |
| **1** | `data_io.py` + `regime.py` | `python -m src.regime` prints regime label + evidence table for today |
| **2** | `universe.py` + `sectors.py` | Prints top-3 sectors + full RRG ranking table; universe CSV cached |
| **3** | `screener.py` | Prints 15–40 candidates with all filter columns; graceful handling of failed tickers |
| **4** | `structure.py` | For 3 hand-picked tickers (e.g. NVDA, MU, AVGO): prints POC/VAH/VAL, AVWAP, setup label, score; spot-check against a TradingView chart manually |
| **5** | `report.py` + `main.py` + `run_ideas.bat` | Full end-to-end run < 10 min; markdown report + CSVs produced |
| **6 (opt)** | Polish: matplotlib chart snapshot per idea embedded in report | Charts render correctly |

**Kickoff prompt for the Claude Code session:**
> Read `IDEAS_ENGINE_PLAN.md` in full. We are implementing **Phase 0 only** today.
> Before writing any code, list the exact steps you will take and wait for my go-ahead.
> Follow the pitfalls in Section 2 strictly (relative paths, timezone normalisation).

## 12. Explicit Non-Goals (v1) / Future Extensions

- ❌ Options analysis of any kind (hard constraint — never).
- ❌ Intraday signals, live streaming, dashboards (the Valentini dashboard already covers monitoring).
- ❌ Short ideas — future v2, activated only in RISK_OFF regime with inverted filters.
- 🔜 v2: HMM regime classifier, real CVD via IBKR intraday bars (`ib_async` + Python 3.14 asyncio fix already known), earnings-date AVWAP anchor, ECAM-style offline HTML report, screen backtest against IDEAS_LOG outcomes.

---
*End of plan. This document is the contract: Claude Code implements what is written here and proposes changes as explicit amendments, not silent deviations.*
