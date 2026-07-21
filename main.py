"""Ideas Engine orchestrator: Layer 1 → 5, weekend run.

Usage:
    python main.py                          # full run with config.yaml
    python main.py --top-n 4 --min-rr 3     # override thresholds for this run
    python main.py --sectors XLV,XLK        # force specific sector ETFs

All outputs land in output/: markdown report, watchlist CSV, IDEAS_LOG.csv,
ideas_data JSON, and the interactive dashboard_YYYY-MM-DD.html (open in any
browser — the UI for filtering ideas by sector/setup/score/R:R).
"""
from __future__ import annotations

import argparse
import logging
import time
from pathlib import Path

import yaml

try:
    # macOS/Linux Terminal sessions often default to a 256 open-file limit,
    # which the batch OHLCV downloads (dozens of tickers) plus yfinance's
    # own sqlite cache can exceed regardless of how main.py is launched.
    import resource
    soft, hard = resource.getrlimit(resource.RLIMIT_NOFILE)
    target = min(4096, hard) if hard != resource.RLIM_INFINITY else 4096
    if soft < target:
        resource.setrlimit(resource.RLIMIT_NOFILE, (target, hard))
except (ImportError, ValueError, OSError):
    pass  # not available on Windows; not fatal if the OS refuses the raise

from src import dashboard, report, screener, sectors as sectors_mod
from src.regime import classify
from src.sectors import SPDR_SECTORS
from src.universe import THEMATIC_TO_GICS, load_universe

ROOT = Path(__file__).resolve().parent


def parse_args():
    p = argparse.ArgumentParser(description="Ideas Engine weekend run")
    p.add_argument("--top-n", type=int, help="number of sectors to select")
    p.add_argument("--min-rr", type=float, help="minimum reward/risk gate")
    p.add_argument("--max-ideas", type=int, help="max ideas in the report")
    p.add_argument("--sectors", help="comma-separated sector ETFs to force (e.g. XLV,XLK)")
    return p.parse_args()


def main():
    args = parse_args()
    cfg = yaml.safe_load((ROOT / "config.yaml").read_text())
    if args.top_n:
        cfg["sectors"]["top_n"] = args.top_n
    if args.min_rr:
        cfg["trade"]["min_rr"] = args.min_rr
    if args.max_ideas:
        cfg["report"]["max_ideas"] = args.max_ideas

    t0 = time.time()
    logging.basicConfig(level=logging.INFO, format="  %(message)s")

    print("[1/5] Macro regime …")
    regime = classify(cfg)
    print(f"      {regime.label} — {regime.explanation}")

    print("[2/5] Sector rotation …")
    sec = sectors_mod.analyse(cfg)
    if args.sectors:
        forced = [s.strip().upper() for s in args.sectors.split(",")]
        for r in sec.rows:
            r.selected = r.etf in forced
            r.rank = forced.index(r.etf) + 1 if r.selected else None
        print(f"      forced sectors: {forced}")
    print(f"      selected: {[f'#{r.rank} {r.etf}' for r in sec.selected]}"
          f" -> GICS {sec.selected_gics()}")

    print("[3/5] Universe + stock screen …")
    universe = load_universe()
    if not regime.allows_ideas:
        print("      REGIME IS RISK_OFF — no new long ideas; writing evidence-only report.")
        scr = screener.ScreenResult(
            candidates=__import__("pandas").DataFrame(),
            near_misses=__import__("pandas").DataFrame(),
            breadth={}, ohlcv={}, n_screened=0)
        structures = []
    else:
        theme_cfg = cfg.get("themes", {}).get("ai_infra", {})
        trow = next((r for r in sec.rows if r.etf == "AI_INFRA"), None)
        theme = None
        if trow is not None and theme_cfg.get("enabled"):
            theme = {"label": trow.name, "members": theme_cfg["members"],
                     "selected": trow.selected}
        scr = screener.run(universe, sec.selected_gics(), regime.label, cfg, theme)
        print(f"      {scr.n_screened} screened -> {len(scr.candidates)} candidates")
        for r in sec.rows:   # feed breadth back into the sector table
            g = (SPDR_SECTORS.get(r.etf) or THEMATIC_TO_GICS.get(r.etf)
                 or (r.name if r.etf == "AI_INFRA" else None))
            if g in scr.breadth:
                r.breadth = scr.breadth[g]

        print("[4/5] AMT structure qualification …")
        from src import structure as structure_mod
        structures = [structure_mod.analyse(t, scr.ohlcv[t], cfg)
                      for t in scr.candidates["ticker"] if t in scr.ohlcv]
        n_setup = sum(1 for s in structures if s.setup != "NO_SETUP")
        print(f"      {n_setup}/{len(structures)} names have a qualifying setup")

    print("[5/5] Trade construction + report …")
    data = report.assemble(regime, sec, scr, structures, cfg, len(universe))
    md = report.write_markdown(data)
    csv_path = report.write_watchlist_csv(data)
    log_path = report.append_ideas_log(data)
    json_path = report.write_json(data)
    dash = dashboard.write_dashboard(data)

    print(f"\nDone in {time.time() - t0:.0f}s — {len(data['ideas'])} ideas.")
    for p in (md, csv_path, log_path, json_path, dash):
        print(f"  {p.relative_to(ROOT)}")
    print(f"\nOpen the dashboard:  open \"{dash}\"")


if __name__ == "__main__":
    main()
