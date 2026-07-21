"""Layer 2 — Sector rotation via relative strength vs SPY (RRG-style).

Ranks the 11 SPDR sectors + thematic ETFs; keeps Leading/Improving
quadrant only; selects top N by composite relative return.
"""
from __future__ import annotations

from dataclasses import dataclass, field

import pandas as pd

from . import data_io
from .universe import THEMATIC_TO_GICS

SPDR_SECTORS = {
    "XLK": "Information Technology",
    "XLF": "Financials",
    "XLE": "Energy",
    "XLV": "Health Care",
    "XLI": "Industrials",
    "XLP": "Consumer Staples",
    "XLY": "Consumer Discretionary",
    "XLB": "Materials",
    "XLU": "Utilities",
    "XLRE": "Real Estate",
    "XLC": "Communication Services",
}
THEMATIC_NAMES = {"SMH": "Semiconductors", "IGV": "Software", "XBI": "Biotech"}


@dataclass
class SectorRow:
    etf: str
    name: str
    rel_21d: float       # 21d return minus SPY (pct points)
    rel_63d: float
    composite: float
    rs_ratio: float      # ETF/SPY ratio normalised to 100 over 126d
    rs_momentum: float   # 21d ROC of rs_ratio (pct)
    quadrant: str
    selected: bool = False
    rank: int | None = None
    breadth: float | None = None   # filled after Layer 3
    trail: list[dict] | None = None  # recent (rs_ratio, rs_momentum) pairs for RRG


@dataclass
class SectorResult:
    rows: list[SectorRow] = field(default_factory=list)

    @property
    def selected(self) -> list[SectorRow]:
        return [r for r in self.rows if r.selected]

    def selected_gics(self) -> list[str]:
        """GICS sector names the stock screen should keep (thematics mapped)."""
        out: list[str] = []
        for r in self.selected:
            gics = SPDR_SECTORS.get(r.etf) or THEMATIC_TO_GICS.get(r.etf)
            if gics and gics not in out:
                out.append(gics)
        return out


def _quadrant(ratio: float, mom: float) -> str:
    if ratio >= 100 and mom >= 0:
        return "Leading"
    if ratio < 100 and mom >= 0:
        return "Improving"
    if ratio >= 100:
        return "Weakening"
    return "Lagging"


def analyse(cfg: dict) -> SectorResult:
    sc = cfg["sectors"]
    etfs = list(SPDR_SECTORS) + list(sc.get("thematic_extra", []))
    data = data_io.get_ohlcv(etfs + ["SPY"], period="2y")
    spy = data["SPY"]["Close"]

    rows: list[SectorRow] = []
    for etf in etfs:
        if etf not in data:
            continue
        close = data[etf]["Close"]
        # align on common dates
        pair = pd.concat([close.rename("etf"), spy.rename("spy")], axis=1).dropna()
        c, s = pair["etf"], pair["spy"]
        if len(pair) < 150:
            continue

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
        rows.append(SectorRow(
            etf=etf,
            name=SPDR_SECTORS.get(etf, THEMATIC_NAMES.get(etf, etf)),
            rel_21d=float(rel21) * 100,
            rel_63d=float(rel63) * 100,
            composite=float(rel21 + rel63) / 2 * 100,
            rs_ratio=rr,
            rs_momentum=rm,
            quadrant=_quadrant(rr, rm),
            trail=trail,
        ))

    rows.sort(key=lambda r: r.composite, reverse=True)
    eligible = [r for r in rows if r.quadrant in ("Leading", "Improving")]
    for i, r in enumerate(eligible[: sc["top_n"]], start=1):
        r.selected = True
        r.rank = i

    # thematic pseudo-sector (AI infrastructure) — additive, never displaces
    # a top-N sector; selection policy in config themes.ai_infra.include_when
    from . import themes
    trow = themes.pseudo_sector_row(cfg)
    if trow is not None:
        policy = cfg["themes"]["ai_infra"].get("include_when", "leading_improving")
        if policy == "always" or trow.quadrant in ("Leading", "Improving"):
            trow.selected = True
            trow.rank = len([r for r in rows if r.selected]) + 1
        rows.append(trow)
    return SectorResult(rows)


if __name__ == "__main__":
    import yaml
    from pathlib import Path

    cfg = yaml.safe_load((Path(__file__).resolve().parent.parent / "config.yaml").read_text())
    res = analyse(cfg)
    print(f"{'ETF':<5} {'Name':<24} {'21d rel':>8} {'63d rel':>8} {'comp':>7} "
          f"{'RS-ratio':>9} {'RS-mom':>7}  Quadrant   Sel")
    for r in res.rows:
        print(f"{r.etf:<5} {r.name:<24} {r.rel_21d:>+7.2f}% {r.rel_63d:>+7.2f}% "
              f"{r.composite:>+6.2f}% {r.rs_ratio:>9.1f} {r.rs_momentum:>+6.2f}%  "
              f"{r.quadrant:<10} {'#' + str(r.rank) if r.selected else ''}")
    print("\nSelected GICS sectors:", res.selected_gics())
