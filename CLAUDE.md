# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A personal swing-trading ideas generator: a 5-layer funnel that turns free market data (FRED, yfinance, Wikipedia) into a ranked watchlist of long ideas, published as a self-contained HTML dashboard. No API keys required (FRED_API_KEY in `.env` is optional — a keyless CSV fallback is used otherwise). The full design rationale lives in `IDEAS_ENGINE_PLAN.md`.

## Commands

```bash
pip install -r requirements.txt          # setup (no lockfile; plain pip)

python3 main.py                          # full run (~ a few minutes, network-bound)
python3 main.py --top-n 4 --min-rr 3     # override config thresholds for one run
python3 main.py --sectors XLV,XLK        # force sector selection (skips Layer-2 choice)

python3 -m src.regime                    # run Layer 1 standalone (prints signal table)
python3 -m src.universe                  # rebuild/inspect the ticker universe
```

There are no tests and no linter. Verification = run the pipeline (or a single layer's `__main__` block) and eyeball the output. To iterate quickly without re-downloading, note that all fetches are cached under `data/cache/` (FRED 1 day, OHLCV 3 days, fundamentals 7 days) — delete specific cache files to force a refresh.

`run_ideas.command` is the double-click macOS launcher: it raises `ulimit -n`, runs the engine, then commits/pushes `output/` (with `git pull --rebase -X theirs` to reconcile with cloud-run commits). Don't break its non-interactive flow.

## Architecture

`main.py` orchestrates five layers, each a module in `src/`, executed strictly in order because each consumes the previous layer's result:

1. **`regime.py`** — macro gate from FRED series (HY OAS, VIX, NFCI, SPY trend). Returns a label: `RISK_ON_TRENDING` / `RISK_ON_RANGING` / `TRANSITION` / `RISK_OFF`. **`RISK_OFF` short-circuits layers 3–4**: the run still completes and writes an evidence-only report with zero ideas (this is expected behavior, not an outage — the dashboard shows a banner for it).
2. **`sectors.py`** — RRG-style relative strength of the 11 SPDR sector ETFs + thematics (SMH/IGV/XBI) vs SPY; selects top-N in Leading/Improving quadrants. **`themes.py`** injects the AI_INFRA pseudo-sector (curated basket, equal-weight, plus a fundamentals gate) into the same ranking.
3. **`screener.py`** — hard filters (price, liquidity, trend, leadership, relative strength) over universe members of the selected sectors; also computes per-sector breadth that gets fed back into the sector table.
4. **`structure.py`** — volume-profile / Auction Market Theory qualification per candidate; classifies each as `ACCEPTANCE_BREAKOUT`, `PULLBACK_TO_VALUE`, or `NO_SETUP`.
5. **`report.py`** — builds trades (entry/stop/target, R:R gate), ranks ideas, and writes every output; **`dashboard.py`** renders the interactive HTML (vanilla JS, zero dependencies, embedded JSON — must stay self-contained and work from a double-click).

Supporting modules: **`data_io.py`** (all network access + caching — FRED, yfinance OHLCV as per-ticker parquet) and **`universe.py`** (S&P 500 + NDX-100 scraped from Wikipedia, cached daily, falls back to last good cache).

**`config.yaml` is the single source of truth for every threshold.** Never hard-code a tunable number in `src/`; add it to config.yaml and read it from `cfg`.

## Output and publishing

`output/` is committed to git deliberately (only `data/cache/` is ignored). Each run writes dated files (`IDEAS_REPORT_*.md`, `dashboard_*.html`, `watchlist_*.csv`, `ideas_data_*.json`), appends to `IDEAS_LOG.csv` (append-only history — never rewrite it), and overwrites `output/index.html` (latest dashboard).

Publishing is GitHub Pages serving `output/` at https://winwaytobacco-ai.github.io/ideas-engine/, via two workflows:
- `daily-run.yml` — daily 21:30 UTC cloud run: executes the engine, commits output, and deploys Pages directly (GITHUB_TOKEN pushes don't trigger other workflows).
- `pages.yml` — deploys on any push touching `output/**` (i.e., after a local run is pushed).

Both local and cloud runs commit to `main`, so history regularly diverges; the launcher's `-X theirs` rebase is the conflict-resolution strategy for the shared files (`index.html`, `IDEAS_LOG.csv`).

## Gotchas

- FRED's CSV endpoint drops connections from browser-spoofed User-Agents but serves the `requests` default UA fine — don't add a custom UA in `data_io.py`.
- Wikipedia's NDX-100 table uses ICB industries, not GICS; `universe.py` maps ICB→GICS for NDX-only names.
- Tickers are normalized to yfinance format (`BRK.B` → `BRK-B`).
- Batch OHLCV downloads exceed macOS's default 256 open-file limit; both `main.py` and the launcher raise it — keep that if refactoring startup.
- yfinance/Yahoo rate-limits cloud IPs occasionally; the daily workflow's retry-once-after-5-min exists for that reason.
