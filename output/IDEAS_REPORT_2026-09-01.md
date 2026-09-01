# IDEAS REPORT — 2026-09-01

## ① Regime: RISK_ON_TRENDING

SPY in confirmed uptrend and 3/3 macro checks risk-on — full idea generation.

| Signal | Reading | Rule | Verdict |
|---|---|---|---|
| Credit stress (HY OAS) | 2.60% | < 21d MA (2.71) and < p75 of 252d (2.95) | PASS |
| Yield curve (10y-2y) | +0.41% (positive, flattening) | informational only in v1 | — |
| Volatility (VIX) | 14.4 | < 22 and < 50d MA (16.5) | PASS |
| Financial conditions (NFCI) | -0.57 | < 0.0 (loose) | PASS |
| SPY trend | 767 vs 200DMA 708 | Close > 200DMA, 50DMA > 200DMA, 200DMA slope up over 21d | PASS |
| SPY range check | 63d range 8.2% | ranging if < 8% and no MA alignment | — |

## ② Sector rotation

| ETF | Sector | 21d rel | 63d rel | RS-ratio | RS-mom | Quadrant | Selected |
|---|---|---|---|---|---|---|---|
| XBI | Biotech (breadth 72%) | +7.86% | +20.35% | 109.1 | +5.36% | Leading | #1 |
| XLV | Health Care (breadth 72%) | +2.24% | +14.48% | 104.4 | +2.76% | Leading | #2 |
| XLE | Energy (breadth 95%) | +4.73% | +11.05% | 104.2 | +4.17% | Leading | #3 |
| IGV | Software | +13.60% | +0.75% | 114.2 | +11.19% | Leading |  |
| XLF | Financials | -1.33% | +11.22% | 102.5 | -1.06% | Weakening |  |
| XLB | Materials | +1.80% | +2.48% | 97.3 | +3.52% | Improving |  |
| XLP | Consumer Staples | -2.76% | +2.93% | 95.7 | -0.51% | Lagging |  |
| XLK | Information Technology | +3.68% | -6.00% | 104.6 | +0.91% | Leading |  |
| XLRE | Real Estate | -4.81% | +1.45% | 95.2 | -3.83% | Lagging |  |
| XLC | Communication Services | +0.29% | -4.72% | 93.1 | +2.89% | Improving |  |
| XLY | Consumer Discretionary | -2.25% | -2.54% | 95.1 | -0.35% | Lagging |  |
| XLI | Industrials | -5.30% | +0.45% | 94.4 | -4.17% | Lagging |  |
| SMH | Semiconductors | +0.30% | -9.80% | 100.0 | -3.03% | Lagging |  |
| XLU | Utilities | -7.46% | -2.78% | 88.3 | -5.12% | Lagging |  |
| AI_INFRA | AI Infrastructure (breadth 27%) | -3.49% | -7.83% | 94.8 | -4.96% | Lagging | #4 |

## ③ Ranked ideas (3)

### 1. TECH — Pullback to value (score 36.9)

Bio-Techne — pullback to value in Health Care (sector rank #1), relative strength top 8% of candidates, flow diverging.

- **Entry:** 71.07 (Limit at high-volume node (71.07))
- **Stop:** 66.44 (below anchored VWAP, 6.5% risk)
- **Target:** 91.4 (measured move (value-area width projected))
- **R:R:** 4.39  |  **Free-flow (+1R):** 75.69
- **Risks:**
  - (medium) Trading 9% above anchored VWAP — mildly extended; prefer limit fills over market entries.
  - (high) Volume-flow divergence: price made new highs that the flow line did not confirm — demand may be thinning.
  - (info) Stop sits 6.5% below entry (~21.0 ATR), below anchored VWAP.
  - (medium) At 52-week highs: target is a measured-move projection with no overhead volume reference — take partial profits mechanically.

### 2. CAH — Pullback to value (score 35.8)

Cardinal Health — pullback to value in Health Care (sector rank #1), relative strength top 40% of candidates, flow neutral.

- **Entry:** 237.17 (Limit at POC (237.17))
- **Stop:** 222.94 (below anchored VWAP, 6.0% risk)
- **Target:** 277.08 (measured move (value-area width projected))
- **R:R:** 2.8  |  **Free-flow (+1R):** 251.41
- **Risks:**
  - (medium) Trading 5% above anchored VWAP — mildly extended; prefer limit fills over market entries.
  - (info) No flow confirmation yet (daily close-vs-open volume proxy is flat).
  - (info) Stop sits 6.0% below entry (~2.9 ATR), below anchored VWAP.
  - (info) Reward/risk of 2.8 is close to the 2.5 floor — any slippage on entry meaningfully degrades the trade.

### 3. CVS — Pullback to value (score 7.4)

CVS Health — pullback to value in Health Care (sector rank #1), relative strength top 90% of candidates, flow neutral.

- **Entry:** 93.91 (At market (price already inside ±1% of POC))
- **Stop:** 92.03 (below anchored VWAP (widened to 1 ATR), 2.0% risk)
- **Target:** 103.77 (nearest overhead high-volume node)
- **R:R:** 5.25  |  **Free-flow (+1R):** 95.79
- **Risks:**
  - (info) No flow confirmation yet (daily close-vs-open volume proxy is flat).
  - (info) Stop sits 2.0% below entry (~1.0 ATR), below anchored VWAP (widened to 1 ATR).

## ④ Appendix

**Watch — no valid trade yet:**

- KMI (Energy, score 94.8): pullback to value but R:R 1.78 below 2.5 floor
- DGX (Health Care, score 80.0): pullback to value but R:R 0.37 below 2.5 floor
- HUM (Health Care, score 80.0): pullback to value but R:R 0.24 below 2.5 floor
- SLB (Energy, score 80.0): acceptance breakout but R:R 1.52 below 2.5 floor
- WAT (Health Care, score 80.0): pullback to value but R:R 2.14 below 2.5 floor
- XOM (Energy, score 80.0): pullback to value but R:R 0.8 below 2.5 floor
- BIIB (Health Care, score 78.7): acceptance breakout but R:R 1.67 below 2.5 floor
- PFE (Health Care, score 78.0): acceptance breakout but R:R 1.07 below 2.5 floor
- WMB (Energy, score 68.0): pullback to value but R:R 1.7 below 2.5 floor
- EW (Health Care, score 64.7): pullback to value but R:R 1.32 below 2.5 floor
- MTD (Health Care, score 60.0): pullback to value but R:R 0.67 below 2.5 floor
- HSIC (Health Care, score 60.0): pullback to value but R:R 1.89 below 2.5 floor
- CNC (Health Care, score 60.0): pullback to value but R:R 0.43 below 2.5 floor
- LLY (Health Care, score 44.3): pullback to value but R:R 2.0 below 2.5 floor
- CRL (Health Care, score 40.0): breakout extended (20 sessions above VAH)
- VEEV (Health Care, score 40.0): breakout extended (26 sessions above VAH)
- MPC (Energy, score 40.0): breakout extended (39 sessions above VAH)
- VLO (Energy, score 40.0): breakout extended (46 sessions above VAH)
- IQV (Health Care, score 40.0): breakout extended (28 sessions above VAH)
- PSX (Energy, score 40.0): breakout extended (39 sessions above VAH)
- AMGN (Health Care, score 40.0): breakout extended (28 sessions above VAH)
- BDX (Health Care, score 40.0): breakout extended (25 sessions above VAH)
- LH (Health Care, score 40.0): breakout extended (28 sessions above VAH)
- MRK (Health Care, score 40.0): breakout extended (29 sessions above VAH)
- INCY (Health Care, score 40.0): breakout extended (28 sessions above VAH)
- RVTY (Health Care, score 40.0): no qualifying structure yet
- TMO (Health Care, score 40.0): breakout extended (28 sessions above VAH)
- BMY (Health Care, score 40.0): breakout extended (30 sessions above VAH)
- ABBV (Health Care, score 40.0): no qualifying structure yet
- SOLV (Health Care, score 40.0): no qualifying structure yet
- JNJ (Health Care, score 40.0): breakout extended (20 sessions above VAH)
- COP (Energy, score 40.0): breakout extended (12 sessions above VAH)
- APA (Energy, score 40.0): breakout extended (16 sessions above VAH)
- OKE (Energy, score 40.0): breakout extended (16 sessions above VAH)
- TRGP (Energy, score 40.0): breakout extended (12 sessions above VAH)
- A (Health Care, score 40.0): no qualifying structure yet
- GILD (Health Care, score 40.0): breakout extended (13 sessions above VAH)
- CVX (Energy, score 40.0): breakout extended (11 sessions above VAH)
- EOG (Energy, score 40.0): breakout extended (16 sessions above VAH)
- DVN (Energy, score 40.0): pullback to value but R:R 0.81 below 2.5 floor
- OXY (Energy, score 40.0): no qualifying structure yet
- DXCM (Health Care, score 38.4): pullback to value but R:R 1.11 below 2.5 floor
- UNH (Health Care, score 26.4): no qualifying structure yet
- VTRS (Health Care, score 24.4): no qualifying structure yet
- BAX (Health Care, score 20.0): breakout extended (27 sessions above VAH)
- WST (Health Care, score 20.0): no qualifying structure yet
- ANET (AI Infrastructure, score 19.7): no qualifying structure yet
- VRTX (Health Care, score 0.0): breakout extended (17 sessions above VAH)
- ZBH (Health Care, score 0.0): breakout extended (19 sessions above VAH)

**Near-misses (failed exactly one screen filter):**

- MRNA (Health Care): failed “near 52w high”
- REGN (Health Care): failed “50DMA > 200DMA”
- RMD (Health Care): failed “50DMA > 200DMA”
- MDT (Health Care): failed “50DMA > 200DMA”
- COR (Health Care): failed “50DMA > 200DMA”
- MCK (Health Care): failed “50DMA > 200DMA”
- DHR (Health Care): failed “50DMA > 200DMA”
- BKR (Energy): failed “63d return beats SPY”
- FANG (Energy): failed “63d return beats SPY”
- DLR (AI Infrastructure): failed “63d return beats SPY”
- ETN (AI Infrastructure): failed “63d return beats SPY”
- EQIX (AI Infrastructure): failed “63d return beats SPY”
- DELL (AI Infrastructure): failed “63d return beats SPY”
- ELV (Health Care): failed “63d return beats SPY”
- IRM (AI Infrastructure): failed “63d return beats SPY”
- CSCO (AI Infrastructure): failed “63d return beats SPY”

---
*Generated by Ideas Engine. Research tool — not investment advice.*