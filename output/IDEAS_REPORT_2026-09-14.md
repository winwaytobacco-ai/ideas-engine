# IDEAS REPORT — 2026-09-14

## ① Regime: RISK_ON_TRENDING

SPY in confirmed uptrend and 3/3 macro checks risk-on — full idea generation.

| Signal | Reading | Rule | Verdict |
|---|---|---|---|
| Credit stress (HY OAS) | 2.65% | < 21d MA (2.68) and < p75 of 252d (2.95) | PASS |
| Yield curve (10y-2y) | +0.32% (positive, flattening) | informational only in v1 | — |
| Volatility (VIX) | 15.8 | < 22 and < 50d MA (16.1) | PASS |
| Financial conditions (NFCI) | -0.56 | < 0.0 (loose) | PASS |
| SPY trend | 761 vs 200DMA 713 | Close > 200DMA, 50DMA > 200DMA, 200DMA slope up over 21d | PASS |
| SPY range check | 63d range 8.3% | ranging if < 8% and no MA alignment | — |

## ② Sector rotation

| ETF | Sector | 21d rel | 63d rel | RS-ratio | RS-mom | Quadrant | Selected |
|---|---|---|---|---|---|---|---|
| XLE | Energy (breadth 81%) | +7.87% | +10.09% | 105.9 | +7.58% | Leading | #1 |
| XBI | Biotech (breadth 67%) | +2.66% | +15.07% | 105.7 | +0.33% | Leading | #2 |
| IGV | Software (breadth 49%) | +2.52% | +14.75% | 111.1 | +0.79% | Leading | #3 |
| XLV | Health Care (breadth 67%) | +1.81% | +6.70% | 103.7 | +2.28% | Leading |  |
| XLC | Communication Services | +4.42% | +0.49% | 98.1 | +7.32% | Improving |  |
| XLF | Financials | +0.07% | +4.45% | 102.0 | -0.02% | Weakening |  |
| XLP | Consumer Staples | +0.35% | -3.79% | 96.7 | +2.74% | Improving |  |
| XLK | Information Technology (breadth 49%) | -1.22% | -3.01% | 103.0 | -3.80% | Weakening |  |
| XLB | Materials | -1.29% | -5.72% | 94.7 | +0.45% | Improving |  |
| XLY | Consumer Discretionary | -2.54% | -5.87% | 93.7 | -0.70% | Lagging |  |
| XLRE | Real Estate | -2.25% | -6.95% | 94.5 | -0.94% | Lagging |  |
| XLU | Utilities | -2.86% | -8.33% | 89.5 | +0.17% | Improving |  |
| XLI | Industrials | -6.35% | -6.15% | 93.1 | -4.97% | Lagging |  |
| SMH | Semiconductors (breadth 49%) | -5.90% | -15.50% | 96.6 | -8.97% | Lagging |  |
| AI_INFRA | AI Infrastructure (breadth 20%) | -5.59% | -4.33% | 95.9 | -6.57% | Lagging | #4 |

## ③ Ranked ideas (2)

### 1. TECH — Pullback to value (score 45.4)

Bio-Techne — pullback to value in Health Care (sector rank #2), relative strength top 16% of candidates, flow neutral.

- **Entry:** 71.1 (Limit at high-volume node (71.10))
- **Stop:** 66.81 (below anchored VWAP, 6.0% risk)
- **Target:** 91.46 (measured move (value-area width projected))
- **R:R:** 4.74  |  **Free-flow (+1R):** 75.4
- **Risks:**
  - (medium) Trading 8% above anchored VWAP — mildly extended; prefer limit fills over market entries.
  - (info) No flow confirmation yet (daily close-vs-open volume proxy is flat).
  - (info) Stop sits 6.0% below entry (~25.3 ATR), below anchored VWAP.
  - (medium) At 52-week highs: target is a measured-move projection with no overhead volume reference — take partial profits mechanically.

### 2. NVDA — Pullback to value (score 0.7)

Nvidia — pullback to value in Information Technology (sector rank #3), relative strength top 98% of candidates, flow diverging.

- **Entry:** 210.96 (At market (price already inside ±1% of POC))
- **Stop:** 203.22 (below anchored VWAP (widened to 1 ATR), 3.7% risk)
- **Target:** 235.2 (52-week high)
- **R:R:** 3.13  |  **Free-flow (+1R):** 218.7
- **Risks:**
  - (high) Volume-flow divergence: price made new highs that the flow line did not confirm — demand may be thinning.
  - (info) Stop sits 3.7% below entry (~1.0 ATR), below anchored VWAP (widened to 1 ATR).

## ④ Appendix

**Watch — no valid trade yet:**

- BMY (Health Care, score 82.9): pullback to value but R:R 1.52 below 2.5 floor
- CAH (Health Care, score 80.9): pullback to value but R:R 1.28 below 2.5 floor
- JNJ (Health Care, score 80.0): pullback to value but R:R 0.67 below 2.5 floor
- WST (Health Care, score 80.0): pullback to value but R:R 0.41 below 2.5 floor
- HUM (Health Care, score 80.0): acceptance breakout but R:R 2.21 below 2.5 floor
- SWKS (Information Technology, score 80.0): acceptance breakout but R:R 2.37 below 2.5 floor
- ELV (Health Care, score 80.0): pullback to value but R:R 1.45 below 2.5 floor
- FFIV (Information Technology, score 80.0): pullback to value but R:R 0.82 below 2.5 floor
- ZBRA (Information Technology, score 60.0): pullback to value but R:R 0.28 below 2.5 floor
- LH (Health Care, score 60.0): pullback to value but R:R 1.11 below 2.5 floor
- DGX (Health Care, score 60.0): pullback to value but R:R 1.97 below 2.5 floor
- NTAP (Information Technology, score 60.0): pullback to value but R:R 0.63 below 2.5 floor
- WAT (Health Care, score 60.0): pullback to value but R:R 1.95 below 2.5 floor
- ANET (Information Technology, score 60.0): pullback to value but R:R 0.84 below 2.5 floor
- EOG (Energy, score 60.0): pullback to value but R:R 1.2 below 2.5 floor
- ZBH (Health Care, score 59.6): pullback to value but R:R 1.21 below 2.5 floor
- FANG (Energy, score 58.2): pullback to value but R:R 1.15 below 2.5 floor
- AMGN (Health Care, score 46.9): breakout extended (37 sessions above VAH)
- VEEV (Health Care, score 40.0): breakout extended (35 sessions above VAH)
- MPC (Energy, score 40.0): breakout extended (25 sessions above VAH)
- VLO (Energy, score 40.0): breakout extended (42 sessions above VAH)
- IQV (Health Care, score 40.0): breakout extended (35 sessions above VAH)
- CRWD (Information Technology, score 40.0): no qualifying structure yet
- HPQ (Information Technology, score 40.0): breakout extended (29 sessions above VAH)
- DELL (Information Technology, score 40.0): no qualifying structure yet
- REGN (Health Care, score 40.0): breakout extended (31 sessions above VAH)
- GEN (Information Technology, score 40.0): no qualifying structure yet
- RVTY (Health Care, score 40.0): no qualifying structure yet
- APA (Energy, score 40.0): breakout extended (21 sessions above VAH)
- GILD (Health Care, score 40.0): breakout extended (22 sessions above VAH)
- VRTX (Health Care, score 40.0): breakout extended (26 sessions above VAH)
- MCK (Health Care, score 40.0): breakout extended (15 sessions above VAH)
- MSI (Information Technology, score 40.0): pullback to value but R:R 0.64 below 2.5 floor
- CDW (Information Technology, score 40.0): no qualifying structure yet
- CVX (Energy, score 40.0): breakout extended (11 sessions above VAH)
- SOLV (Health Care, score 40.0): no qualifying structure yet
- DVN (Energy, score 40.0): pullback to value but R:R 0.88 below 2.5 floor
- HSIC (Health Care, score 40.0): pullback to value but R:R 2.36 below 2.5 floor
- PFE (Health Care, score 40.0): breakout extended (19 sessions above VAH)
- CNC (Health Care, score 40.0): no qualifying structure yet
- BIIB (Health Care, score 39.0): no qualifying structure yet
- VRSN (Information Technology, score 38.5): pullback to value but R:R 0.78 below 2.5 floor
- CRL (Health Care, score 20.0): breakout extended (29 sessions above VAH)
- PANW (Information Technology, score 20.0): no qualifying structure yet
- TMO (Health Care, score 20.0): breakout extended (37 sessions above VAH)
- MSFT (Information Technology, score 20.0): breakout extended (32 sessions above VAH)
- BDX (Health Care, score 20.0): breakout extended (34 sessions above VAH)
- MRK (Health Care, score 20.0): breakout extended (25 sessions above VAH)
- FTNT (Information Technology, score 20.0): breakout extended (13 sessions above VAH)
- ABBV (Health Care, score 20.0): no qualifying structure yet
- A (Health Care, score 20.0): no qualifying structure yet
- INCY (Health Care, score 20.0): breakout extended (35 sessions above VAH)
- TRGP (Energy, score 20.0): breakout extended (21 sessions above VAH)
- DXCM (Health Care, score 18.5): no qualifying structure yet
- XOM (Energy, score 17.7): closes above VAH but flow not confirming
- PSX (Energy, score 0.0): breakout extended (25 sessions above VAH)
- COP (Energy, score 0.0): closes above VAH but flow not confirming
- HPE (Information Technology, score 0.0): no qualifying structure yet
- AAPL (Information Technology, score 0.0): no qualifying structure yet
- OXY (Energy, score 0.0): no qualifying structure yet
- OKE (Energy, score 0.0): breakout extended (24 sessions above VAH)

**Near-misses (failed exactly one screen filter):**

- MRNA (Health Care): failed “near 52w high”
- CRM (Information Technology): failed “50DMA > 200DMA”
- WDAY (Information Technology): failed “near 52w high”
- NOW (Information Technology): failed “near 52w high”
- PLTR (Information Technology): failed “near 52w high”
- TRI (Information Technology): failed “near 52w high”
- SHOP (Information Technology): failed “near 52w high”
- SMCI (Information Technology): failed “near 52w high”
- ROP (Information Technology): failed “near 52w high”
- MDT (Health Care): failed “50DMA > 200DMA”
- COR (Health Care): failed “50DMA > 200DMA”
- BAX (Health Care): failed “near 52w high”
- MTD (Health Care): failed “close > 200DMA”
- DHR (Health Care): failed “near 52w high”
- APH (Information Technology): failed “63d return beats SPY”
- VTRS (Health Care): failed “63d return beats SPY”
- ETN (AI Infrastructure): failed “63d return beats SPY”
- LLY (Health Care): failed “63d return beats SPY”
- WMB (Energy): failed “63d return beats SPY”
- EW (Health Care): failed “63d return beats SPY”
- DLR (AI Infrastructure): failed “63d return beats SPY”
- CI (Health Care): failed “63d return beats SPY”
- KMI (Energy): failed “63d return beats SPY”
- SLB (Energy): failed “63d return beats SPY”
- EQIX (AI Infrastructure): failed “63d return beats SPY”
- UNH (Health Care): failed “63d return beats SPY”
- CVS (Health Care): failed “63d return beats SPY”

---
*Generated by Ideas Engine. Research tool — not investment advice.*