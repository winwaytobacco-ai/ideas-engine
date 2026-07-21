"""Layer 5 — Trade construction, ranking, risk remarks, and all outputs.

Outputs: markdown report, watchlist CSV, append-only IDEAS_LOG.csv,
ideas_data.json + self-contained HTML dashboard (the UI).
"""
from __future__ import annotations

import csv
import json
from datetime import date, datetime
from pathlib import Path

import pandas as pd

from .regime import RegimeResult
from .sectors import SectorResult, SPDR_SECTORS
from .screener import ScreenResult
from .structure import StructureResult
from .universe import THEMATIC_TO_GICS

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

SETUP_HUMAN = {
    "ACCEPTANCE_BREAKOUT": "Acceptance breakout above value",
    "PULLBACK_TO_VALUE": "Pullback to value",
}


# ------------------------------------------------------- trade construction --

def build_trade(s: StructureResult, cfg: dict) -> dict | None:
    """Mechanical entry/stop/target per plan §8. Returns None if no valid trade."""
    p = s.profile
    tol = cfg["structure"]["pullback_poc_tolerance"]

    if s.setup == "ACCEPTANCE_BREAKOUT":
        entry = p.vah * 1.005
        entry_type = f"Buy-stop on retest of VAH ({p.vah:.2f} + 0.5%)"
    else:  # PULLBACK_TO_VALUE
        near_poc = abs(s.close - p.poc) / p.poc <= tol
        if abs(s.close - p.poc) / p.poc <= 0.01:
            entry, entry_type = s.close, "At market (price already inside ±1% of POC)"
        elif near_poc:
            entry, entry_type = p.poc, f"Limit at POC ({p.poc:.2f})"
        else:
            # pullback qualified via an HVN: limit at the nearest HVN below/at price
            hvns_below = [h for h in p.hvns if h <= s.close * (1 + tol)]
            level = max(hvns_below) if hvns_below else p.poc
            if abs(s.close - level) / level <= 0.01:
                entry, entry_type = s.close, "At market (price at high-volume node)"
            else:
                entry, entry_type = level, f"Limit at high-volume node ({level:.2f})"

    # Stop: below VAL or AVWAP, whichever is nearer to entry, min 1 ATR away
    stop_candidates = [x for x in (p.val, s.avwap) if x < entry]
    stop_ref_name = None
    if stop_candidates:
        stop = max(stop_candidates)
        stop_ref_name = "VAL" if stop == p.val else "anchored VWAP"
    else:
        stop = entry - s.atr
    if entry - stop < s.atr:
        stop = entry - s.atr
        stop_ref_name = f"{stop_ref_name} (widened to 1 ATR)" if stop_ref_name else "1 ATR"

    # Target: nearest *meaningful* overhead HVN (at least 1.5 ATR / 2% away —
    # closer nodes are noise, not destinations); else 52w high; at highs ->
    # measured move (value-area width projected from VAH)
    measured = max(p.vah + (p.vah - p.val), entry + (p.vah - p.val))
    min_target = entry + max(1.5 * s.atr, entry * 0.02)
    hvns_above = [h for h in p.hvns if h >= min_target]
    if entry >= s.hi52 * 0.98:
        target, target_ref = measured, "measured move (value-area width projected)"
    elif hvns_above:
        target, target_ref = min(hvns_above), "nearest overhead high-volume node"
    elif s.hi52 >= min_target:
        target, target_ref = s.hi52, "52-week high"
    else:
        target, target_ref = measured, "measured move (value-area width projected)"

    risk = entry - stop
    if risk <= 0:
        return None
    rr = (target - entry) / risk
    free_flow = entry + risk   # sell half here -> stopped remainder = breakeven

    return {
        "entry": round(entry, 2), "entry_type": entry_type,
        "stop": round(stop, 2), "stop_ref": stop_ref_name or "structural",
        "target": round(target, 2), "target_ref": target_ref,
        "rr": round(rr, 2), "free_flow": round(free_flow, 2),
        "stop_pct": round(risk / entry * 100, 1),
        "stop_atr": round(risk / s.atr, 1) if s.atr else None,
    }


# ------------------------------------------------------------ risk remarks --

def risk_remarks(s: StructureResult, trade: dict, breadth: float | None,
                 regime_label: str, pct_from_high: float, cfg: dict) -> list[dict]:
    risks: list[dict] = []

    if s.avwap_dist > 0.10:
        risks.append({"level": "high", "text":
            f"Extended {s.avwap_dist:.0%} above anchored VWAP — heavy chase risk; "
            "wait for the limit level, do not buy at market."})
    elif s.avwap_dist > 0.05:
        risks.append({"level": "medium", "text":
            f"Trading {s.avwap_dist:.0%} above anchored VWAP — mildly extended; "
            "prefer limit fills over market entries."})

    if s.flow_state == "diverging":
        risks.append({"level": "high", "text":
            "Volume-flow divergence: price made new highs that the flow line did not "
            "confirm — demand may be thinning."})
    elif s.flow_state == "neutral":
        risks.append({"level": "info", "text":
            "No flow confirmation yet (daily close-vs-open volume proxy is flat)."})

    if breadth is not None and breadth < cfg["sectors"]["breadth_min"]:
        risks.append({"level": "medium", "text":
            f"Narrow sector leadership: only {breadth:.0%} of sector members are above "
            "their 50DMA — the sector move rests on few names."})

    if trade["stop_pct"] > 12:
        risks.append({"level": "medium", "text":
            f"Wide structural stop ({trade['stop_pct']:.1f}% below entry) — halve position "
            "size so dollar risk stays constant."})
    else:
        risks.append({"level": "info", "text":
            f"Stop sits {trade['stop_pct']:.1f}% below entry (~{trade['stop_atr']} ATR), "
            f"below {trade['stop_ref']}."})

    if trade["rr"] < 3.0:
        risks.append({"level": "info", "text":
            f"Reward/risk of {trade['rr']} is close to the {cfg['trade']['min_rr']} floor — "
            "any slippage on entry meaningfully degrades the trade."})

    if pct_from_high < 0.02:
        risks.append({"level": "medium", "text":
            "At 52-week highs: target is a measured-move projection with no overhead "
            "volume reference — take partial profits mechanically."})

    if regime_label == "TRANSITION":
        risks.append({"level": "medium", "text":
            "Regime is TRANSITION — mixed macro signals; the engine halved its list. "
            "Treat every idea as half-size."})
    if regime_label == "RISK_ON_RANGING" and s.setup == "ACCEPTANCE_BREAKOUT":
        risks.append({"level": "medium", "text":
            "Breakout setup inside a ranging market — failure rate is elevated; "
            "pullback entries are preferred in this regime."})

    if trade["entry"] < s.close * 0.97:
        risks.append({"level": "info", "text":
            f"Entry limit sits {(1 - trade['entry'] / s.close):.1%} below current price — "
            "the order may never fill; do not chase if it runs away."})

    return risks


def execution_steps(s: StructureResult, trade: dict) -> list[str]:
    return [
        f"Entry — {trade['entry_type']}. Working level: {trade['entry']:.2f}.",
        f"Stop — {trade['stop']:.2f} ({trade['stop_pct']:.1f}% risk, ~{trade['stop_atr']} ATR), "
        f"placed below {trade['stop_ref']}. Structural, never percentage-based.",
        f"Target — {trade['target']:.2f} ({trade['target_ref']}); "
        f"reward/risk {trade['rr']:.1f}.",
        f"Free-flow — at {trade['free_flow']:.2f} (+1R) sell half; the remainder then "
        "rides at breakeven-or-better even if stopped.",
        "Invalidation — idea is void on a daily close below the stop reference or if "
        "the weekly regime turns RISK_OFF.",
    ]


# ----------------------------------------------------------------- assembly --

def assemble(regime: RegimeResult, sectors: SectorResult, screen: ScreenResult,
             structures: list[StructureResult], cfg: dict,
             universe_size: int) -> dict:
    """Rank qualified names, construct trades, and produce the run's data dict."""
    from . import themes as themes_mod

    gics_rank: dict[str, int] = {}
    theme_row = None
    for r in sectors.selected:
        if r.etf == themes_mod.THEME_KEY:
            theme_row = r
            gics_rank[r.name] = r.rank   # pseudo-sector keyed by its label
            continue
        g = SPDR_SECTORS.get(r.etf) or THEMATIC_TO_GICS.get(r.etf)
        if g and g not in gics_rank:
            gics_rank[g] = r.rank
    if theme_row is None:   # theme shown in table but not selected
        theme_row = next((r for r in sectors.rows if r.etf == themes_mod.THEME_KEY), None)

    weights = cfg["report"]["sector_rank_weights"]
    max_ideas = cfg["report"]["max_ideas"]
    if regime.label == "TRANSITION":
        max_ideas = max(1, max_ideas // 2)

    cand = screen.candidates.set_index("ticker")
    ideas, watch = [], []

    for s in structures:
        row = cand.loc[s.ticker]
        is_theme = bool(row.get("theme", False))

        # "backed by real earnings and orders" gate for AI-infra theme names
        fund, backed, evidence, failures = None, True, [], []
        if is_theme:
            fund = themes_mod.get_fundamentals(s.ticker)
            backed, evidence, failures = themes_mod.earnings_backed(fund, cfg)
            if not backed:
                watch.append({"ticker": s.ticker, "name": str(row["name"]),
                              "sector": str(row["sector"]), "score": s.score,
                              "note": "AI-infra name not earnings-backed: "
                                      + "; ".join(failures)})
                continue

        if s.setup == "NO_SETUP":
            watch.append({"ticker": s.ticker, "name": str(row["name"]),
                          "sector": str(row["sector"]), "score": s.score,
                          "note": "; ".join(s.notes) or "no qualifying structure yet"})
            continue
        trade = build_trade(s, cfg)
        if trade is None:
            continue
        if trade["rr"] < cfg["trade"]["min_rr"]:
            watch.append({"ticker": s.ticker, "name": str(row["name"]),
                          "sector": str(row["sector"]), "score": s.score,
                          "note": f"{s.setup.lower().replace('_', ' ')} but R:R "
                                  f"{trade['rr']} below {cfg['trade']['min_rr']} floor"})
            continue

        sector = str(row["sector"])
        rank = gics_rank.get(sector, len(weights))
        weight = weights[min(rank - 1, len(weights) - 1)]
        rs_pct = float(row["rs_percentile"])
        total = round(s.score * weight * rs_pct, 1)
        breadth = screen.breadth.get(sector)
        pct_from_high = float(row["pct_from_52w_high"])

        spark_df = screen.ohlcv[s.ticker].tail(cfg["structure"]["lookback_days"])
        thesis = (f"{row['name']} — {SETUP_HUMAN[s.setup].lower()} in {sector} "
                  f"(sector rank #{rank}), relative strength top {(1 - rs_pct):.0%} "
                  f"of candidates, flow {s.flow_state}.")

        trade_risks = risk_remarks(s, trade, breadth, regime.label, pct_from_high, cfg)
        ooda = None
        if is_theme:
            if theme_row and theme_row.quadrant in ("Weakening", "Lagging"):
                trade_risks.append({"level": "medium", "text":
                    f"AI-infrastructure basket is {theme_row.quadrant} vs SPY — the theme "
                    "tailwind is fading; this idea rests on stock-specific strength."})
            orient = []
            if theme_row:
                orient.append(
                    f"AI-infrastructure basket is {theme_row.quadrant} vs SPY "
                    f"(RS-ratio {theme_row.rs_ratio:.1f}, momentum "
                    f"{theme_row.rs_momentum:+.1f}%), included by config policy "
                    f"'{cfg['themes']['ai_infra'].get('include_when', 'leading_improving')}'.")
            orient.append(f"Regime {regime.label}: {regime.explanation}")
            if breadth is not None:
                orient.append(f"Theme breadth: {breadth:.0%} of basket members above their 50DMA.")
            ooda = {
                "observe": evidence + [
                    f"Price structure: {SETUP_HUMAN[s.setup].lower()}, flow {s.flow_state}, "
                    f"{s.avwap_dist:+.1%} vs anchored VWAP.",
                    "Order-book data is not in free feeds — forward-vs-trailing EPS is the proxy."],
                "orient": orient,
                "decide": [
                    "Earnings-backed: PASS — kept in the ranked list. Use the AI-infra "
                    "filter above the ideas grid to exclude (or isolate) theme names "
                    "if you judge the theme crowded."],
                "act": ["Execute per the plan below — entry, structural stop, target, "
                        "free-flow at +1R, and regime invalidation."],
            }

        ideas.append({
            "ticker": s.ticker, "name": str(row["name"]), "sector": sector,
            "sector_rank": rank, "setup": s.setup,
            "setup_human": SETUP_HUMAN[s.setup],
            "score": s.score, "total_score": total,
            "rs_percentile": round(rs_pct * 100),
            "thesis": thesis,
            **trade,
            "close": round(s.close, 2), "poc": round(s.profile.poc, 2),
            "vah": round(s.profile.vah, 2), "val": round(s.profile.val, 2),
            "avwap": s.avwap, "avwap_dist": round(s.avwap_dist * 100, 1),
            "atr": s.atr, "flow_state": s.flow_state,
            "pct_from_52w_high": round(pct_from_high * 100, 1),
            "breadth": None if breadth is None else round(breadth * 100),
            "theme": "AI Infrastructure" if is_theme else None,
            "fundamentals": None if fund is None else {
                k: fund.get(k) for k in ("trailingEps", "forwardEps",
                                         "revenueGrowth", "earningsGrowth",
                                         "profitMargins")},
            "ooda": ooda,
            "risks": trade_risks,
            "execution": execution_steps(s, trade),
            "spark": {
                "dates": [d.strftime("%Y-%m-%d") for d in spark_df.index],
                "close": [round(float(c), 2) for c in spark_df["Close"]],
            },
        })

    ideas.sort(key=lambda i: i["total_score"], reverse=True)
    ideas = ideas[:max_ideas]

    near = screen.near_misses
    return {
        "run_date": date.today().isoformat(),
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "regime": {
            "label": regime.label, "explanation": regime.explanation,
            "signals": [{"name": s.name, "value": s.value, "rule": s.rule,
                         "passed": s.passed} for s in regime.signals],
        },
        "sectors": {
            "rows": [{
                "etf": r.etf, "name": r.name, "rel_21d": round(r.rel_21d, 2),
                "rel_63d": round(r.rel_63d, 2), "composite": round(r.composite, 2),
                "rs_ratio": round(r.rs_ratio, 1), "rs_momentum": round(r.rs_momentum, 2),
                "quadrant": r.quadrant, "selected": r.selected, "rank": r.rank,
                "breadth": r.breadth, "trail": r.trail,
            } for r in sectors.rows],
            "selected_gics": sectors.selected_gics(),
        },
        "funnel": {
            "universe": universe_size, "screened": screen.n_screened,
            "candidates": len(screen.candidates),
            "qualified": sum(1 for s in structures if s.setup != "NO_SETUP"),
            "ideas": len(ideas),
        },
        "ideas": ideas,
        "watch": sorted(watch, key=lambda w: w["score"], reverse=True),
        "near_misses": [] if near.empty else near[
            ["ticker", "name", "sector", "failed_filter"]].to_dict("records"),
        "config": {
            "min_rr": cfg["trade"]["min_rr"], "max_ideas": cfg["report"]["max_ideas"],
            "top_n_sectors": cfg["sectors"]["top_n"],
        },
    }


# ------------------------------------------------------------------ outputs --

def write_markdown(data: dict) -> Path:
    d = data["run_date"]
    lines = [f"# IDEAS REPORT — {d}", ""]
    r = data["regime"]
    lines += [f"## ① Regime: {r['label']}", "", r["explanation"], "",
              "| Signal | Reading | Rule | Verdict |", "|---|---|---|---|"]
    for s in r["signals"]:
        verdict = "—" if s["passed"] is None else ("PASS" if s["passed"] else "FAIL")
        lines.append(f"| {s['name']} | {s['value']} | {s['rule']} | {verdict} |")

    lines += ["", "## ② Sector rotation", "",
              "| ETF | Sector | 21d rel | 63d rel | RS-ratio | RS-mom | Quadrant | Selected |",
              "|---|---|---|---|---|---|---|---|"]
    for row in data["sectors"]["rows"]:
        sel = f"#{row['rank']}" if row["selected"] else ""
        b = f" (breadth {row['breadth']:.0%})" if row.get("breadth") is not None else ""
        lines.append(f"| {row['etf']} | {row['name']}{b} | {row['rel_21d']:+.2f}% | "
                     f"{row['rel_63d']:+.2f}% | {row['rs_ratio']} | "
                     f"{row['rs_momentum']:+.2f}% | {row['quadrant']} | {sel} |")

    lines += ["", f"## ③ Ranked ideas ({len(data['ideas'])})", ""]
    if not data["ideas"]:
        lines.append("**No qualifying ideas this run.**")
    for i, idea in enumerate(data["ideas"], 1):
        lines += [
            f"### {i}. {idea['ticker']} — {idea['setup_human']} "
            f"(score {idea['total_score']})", "",
            idea["thesis"], "",
            f"- **Entry:** {idea['entry']} ({idea['entry_type']})",
            f"- **Stop:** {idea['stop']} (below {idea['stop_ref']}, "
            f"{idea['stop_pct']}% risk)",
            f"- **Target:** {idea['target']} ({idea['target_ref']})",
            f"- **R:R:** {idea['rr']}  |  **Free-flow (+1R):** {idea['free_flow']}",
            "- **Risks:**",
        ]
        lines += [f"  - ({rk['level']}) {rk['text']}" for rk in idea["risks"]]
        if idea.get("ooda"):
            lines.append("- **OODA (AI-infrastructure theme):**")
            for phase in ("observe", "orient", "decide", "act"):
                lines.append(f"  - *{phase.capitalize()}:*")
                lines += [f"    - {x}" for x in idea["ooda"][phase]]
        lines.append("")

    lines += ["## ④ Appendix", "", "**Watch — no valid trade yet:**", ""]
    for w in data["watch"]:
        lines.append(f"- {w['ticker']} ({w['sector']}, score {w['score']}): {w['note']}")
    lines += ["", "**Near-misses (failed exactly one screen filter):**", ""]
    for n in data["near_misses"]:
        lines.append(f"- {n['ticker']} ({n['sector']}): failed “{n['failed_filter']}”")
    lines += ["", "---", "*Generated by Ideas Engine. Research tool — not investment advice.*"]

    path = OUTPUT_DIR / f"IDEAS_REPORT_{d}.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def write_watchlist_csv(data: dict) -> Path:
    path = OUTPUT_DIR / f"watchlist_{data['run_date']}.csv"
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["ticker", "setup", "entry", "stop", "target", "rr", "score"])
        for i in data["ideas"]:
            w.writerow([i["ticker"], i["setup"], i["entry"], i["stop"],
                        i["target"], i["rr"], i["total_score"]])
    return path


def append_ideas_log(data: dict) -> Path:
    path = OUTPUT_DIR / "IDEAS_LOG.csv"
    new = not path.exists()
    with path.open("a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["run_date", "regime", "ticker", "setup", "entry", "stop",
                        "target", "rr", "score", "outcome", "outcome_r", "notes"])
        for i in data["ideas"]:
            w.writerow([data["run_date"], data["regime"]["label"], i["ticker"],
                        i["setup"], i["entry"], i["stop"], i["target"], i["rr"],
                        i["total_score"], "", "", ""])
    return path


def write_json(data: dict) -> Path:
    path = OUTPUT_DIR / f"ideas_data_{data['run_date']}.json"
    path.write_text(json.dumps(data, indent=1), encoding="utf-8")
    return path
