# IDEAS REPORT — 2026-08-10

## ① Regime: RISK_ON_TRENDING

SPY in confirmed uptrend and 3/3 macro checks risk-on — full idea generation.

| Signal | Reading | Rule | Verdict |
|---|---|---|---|
| Credit stress (HY OAS) | 2.70% | < 21d MA (2.75) and < p75 of 252d (2.95) | PASS |
| Yield curve (10y-2y) | +0.47% (positive, steepening) | informational only in v1 | — |
| Volatility (VIX) | 14.9 | < 22 and < 50d MA (17.3) | PASS |
| Financial conditions (NFCI) | -0.53 | < 0.0 (loose) | PASS |
| SPY trend | 773 vs 200DMA 701 | Close > 200DMA, 50DMA > 200DMA, 200DMA slope up over 21d | PASS |
| SPY range check | 63d range 7.8% | ranging if < 8% and no MA alignment | — |

## ② Sector rotation

| ETF | Sector | 21d rel | 63d rel | RS-ratio | RS-mom | Quadrant | Selected |
|---|---|---|---|---|---|---|---|
| IGV | Software (breadth 52%) | +11.24% | +10.16% | 109.8 | +12.89% | Leading | #1 |
| XLV | Health Care (breadth 87%) | +2.33% | +12.84% | 102.0 | +3.03% | Leading | #2 |
| XLE | Energy (breadth 76%) | +6.86% | +3.75% | 97.6 | +5.20% | Improving | #3 |
| XLF | Financials | +1.37% | +8.15% | 101.8 | +1.85% | Leading |  |
| XBI | Biotech (breadth 87%) | -3.02% | +12.36% | 107.1 | -4.63% | Weakening |  |
| XLI | Industrials | -0.92% | +1.77% | 97.8 | -1.01% | Lagging |  |
| XLB | Materials | +2.11% | -1.60% | 96.1 | +2.83% | Improving |  |
| XLK | Information Technology (breadth 52%) | -2.10% | +1.21% | 105.7 | -4.12% | Weakening |  |
| XLP | Consumer Staples | -1.41% | -3.46% | 93.3 | -0.51% | Lagging |  |
| XLY | Consumer Discretionary | -0.32% | -5.31% | 95.6 | +2.07% | Improving |  |
| XLRE | Real Estate | -2.51% | -4.22% | 94.3 | -2.73% | Lagging |  |
| XLC | Communication Services | -2.22% | -9.19% | 91.1 | +0.17% | Improving |  |
| SMH | Semiconductors (breadth 52%) | -9.21% | -4.56% | 103.8 | -12.68% | Weakening |  |
| XLU | Utilities | -7.42% | -8.01% | 87.8 | -6.76% | Lagging |  |
| AI_INFRA | AI Infrastructure (breadth 47%) | -5.14% | -1.07% | 100.0 | -8.30% | Weakening | #4 |

## ③ Ranked ideas (7)

### 1. ZBRA — Acceptance breakout above value (score 73.4)

Zebra Technologies — acceptance breakout above value in Information Technology (sector rank #1), relative strength top 8% of candidates, flow confirming.

- **Entry:** 270.54 (Buy-stop on retest of VAH (269.19 + 0.5%))
- **Stop:** 252.73 (below anchored VWAP, 6.6% risk)
- **Target:** 378.08 (52-week high)
- **R:R:** 6.04  |  **Free-flow (+1R):** 288.34
- **Risks:**
  - (high) Extended 50% above anchored VWAP — heavy chase risk; wait for the limit level, do not buy at market.
  - (info) Stop sits 6.6% below entry (~1.1 ATR), below anchored VWAP.
  - (medium) At 52-week highs: target is a measured-move projection with no overhead volume reference — take partial profits mechanically.
  - (info) Entry limit sits 28.4% below current price — the order may never fill; do not chase if it runs away.

### 2. ANET — Acceptance breakout above value (score 63.0)

Arista Networks — acceptance breakout above value in Information Technology (sector rank #1), relative strength top 21% of candidates, flow confirming.

- **Entry:** 167.98 (Buy-stop on retest of VAH (167.14 + 0.5%))
- **Stop:** 156.91 (below anchored VWAP (widened to 1 ATR), 6.6% risk)
- **Target:** 197.31 (52-week high)
- **R:R:** 2.65  |  **Free-flow (+1R):** 179.05
- **Risks:**
  - (high) Extended 19% above anchored VWAP — heavy chase risk; wait for the limit level, do not buy at market.
  - (info) Stop sits 6.6% below entry (~1.0 ATR), below anchored VWAP (widened to 1 ATR).
  - (info) Reward/risk of 2.65 is close to the 2.5 floor — any slippage on entry meaningfully degrades the trade.
  - (info) Entry limit sits 12.3% below current price — the order may never fill; do not chase if it runs away.
  - (medium) AI-infrastructure basket is Weakening vs SPY — the theme tailwind is fading; this idea rests on stock-specific strength.
- **OODA (AI-infrastructure theme):**
  - *Observe:*
    - Profitable today: trailing 12m EPS 3.15, net margin 38%
    - Real demand: quarterly revenue growing +38% YoY
    - Order-book proxy: forward EPS 5.16 above trailing 3.15 — analysts see the pipeline growing
    - Price structure: acceptance breakout above value, flow confirming, +18.9% vs anchored VWAP.
    - Order-book data is not in free feeds — forward-vs-trailing EPS is the proxy.
  - *Orient:*
    - AI-infrastructure basket is Weakening vs SPY (RS-ratio 100.0, momentum -8.3%), included by config policy 'always'.
    - Regime RISK_ON_TRENDING: SPY in confirmed uptrend and 3/3 macro checks risk-on — full idea generation.
    - Theme breadth: 52% of basket members above their 50DMA.
  - *Decide:*
    - Earnings-backed: PASS — kept in the ranked list. Use the AI-infra filter above the ideas grid to exclude (or isolate) theme names if you judge the theme crowded.
  - *Act:*
    - Execute per the plan below — entry, structural stop, target, free-flow at +1R, and regime invalidation.

### 3. CAH — Pullback to value (score 47.2)

Cardinal Health — pullback to value in Health Care (sector rank #2), relative strength top 34% of candidates, flow confirming.

- **Entry:** 237.18 (At market (price already inside ±1% of POC))
- **Stop:** 220.65 (below anchored VWAP, 7.0% risk)
- **Target:** 285.05 (measured move (value-area width projected))
- **R:R:** 2.9  |  **Free-flow (+1R):** 253.71
- **Risks:**
  - (medium) Trading 7% above anchored VWAP — mildly extended; prefer limit fills over market entries.
  - (info) Stop sits 7.0% below entry (~3.0 ATR), below anchored VWAP.
  - (info) Reward/risk of 2.9 is close to the 2.5 floor — any slippage on entry meaningfully degrades the trade.
  - (medium) At 52-week highs: target is a measured-move projection with no overhead volume reference — take partial profits mechanically.

### 4. VRTX — Acceptance breakout above value (score 35.4)

Vertex Pharmaceuticals — acceptance breakout above value in Health Care (sector rank #2), relative strength top 51% of candidates, flow confirming.

- **Entry:** 484.31 (Buy-stop on retest of VAH (481.90 + 0.5%))
- **Stop:** 468.29 (below anchored VWAP (widened to 1 ATR), 3.3% risk)
- **Target:** 529.59 (52-week high)
- **R:R:** 2.83  |  **Free-flow (+1R):** 500.33
- **Risks:**
  - (high) Extended 12% above anchored VWAP — heavy chase risk; wait for the limit level, do not buy at market.
  - (info) Stop sits 3.3% below entry (~1.0 ATR), below anchored VWAP (widened to 1 ATR).
  - (info) Reward/risk of 2.83 is close to the 2.5 floor — any slippage on entry meaningfully degrades the trade.
  - (medium) At 52-week highs: target is a measured-move projection with no overhead volume reference — take partial profits mechanically.
  - (info) Entry limit sits 7.6% below current price — the order may never fill; do not chase if it runs away.

### 5. BDX — Acceptance breakout above value (score 34.2)

Becton Dickinson — acceptance breakout above value in Health Care (sector rank #2), relative strength top 52% of candidates, flow confirming.

- **Entry:** 162.4 (Buy-stop on retest of VAH (161.59 + 0.5%))
- **Stop:** 157.39 (below anchored VWAP, 3.1% risk)
- **Target:** 175.46 (nearest overhead high-volume node)
- **R:R:** 2.61  |  **Free-flow (+1R):** 167.4
- **Risks:**
  - (high) Extended 14% above anchored VWAP — heavy chase risk; wait for the limit level, do not buy at market.
  - (info) Stop sits 3.1% below entry (~1.1 ATR), below anchored VWAP.
  - (info) Reward/risk of 2.61 is close to the 2.5 floor — any slippage on entry meaningfully degrades the trade.
  - (medium) At 52-week highs: target is a measured-move projection with no overhead volume reference — take partial profits mechanically.
  - (info) Entry limit sits 9.6% below current price — the order may never fill; do not chase if it runs away.

### 6. TECH — Pullback to value (score 31.3)

Bio-Techne — pullback to value in Health Care (sector rank #2), relative strength top 13% of candidates, flow diverging.

- **Entry:** 70.93 (Limit at POC (70.93))
- **Stop:** 65.81 (below anchored VWAP, 7.2% risk)
- **Target:** 91.12 (measured move (value-area width projected))
- **R:R:** 3.95  |  **Free-flow (+1R):** 76.04
- **Risks:**
  - (medium) Trading 10% above anchored VWAP — mildly extended; prefer limit fills over market entries.
  - (high) Volume-flow divergence: price made new highs that the flow line did not confirm — demand may be thinning.
  - (info) Stop sits 7.2% below entry (~17.1 ATR), below anchored VWAP.
  - (medium) At 52-week highs: target is a measured-move projection with no overhead volume reference — take partial profits mechanically.

### 7. OXY — Pullback to value (score 8.9)

Occidental Petroleum — pullback to value in Energy (sector rank #3), relative strength top 74% of candidates, flow diverging.

- **Entry:** 57.83 (Limit at high-volume node (57.83))
- **Stop:** 55.92 (below anchored VWAP (widened to 1 ATR), 3.3% risk)
- **Target:** 65.94 (52-week high)
- **R:R:** 4.24  |  **Free-flow (+1R):** 59.74
- **Risks:**
  - (high) Volume-flow divergence: price made new highs that the flow line did not confirm — demand may be thinning.
  - (info) Stop sits 3.3% below entry (~1.0 ATR), below anchored VWAP (widened to 1 ATR).

## ④ Appendix

**Watch — no valid trade yet:**

- AAPL (Information Technology, score 83.1): pullback to value but R:R 1.76 below 2.5 floor
- DXCM (Health Care, score 80.0): acceptance breakout but R:R 1.26 below 2.5 floor
- DDOG (Information Technology, score 80.0): pullback to value but R:R 1.83 below 2.5 floor
- CSCO (Information Technology, score 80.0): acceptance breakout but R:R 0.68 below 2.5 floor
- ABBV (Health Care, score 80.0): pullback to value but R:R 1.02 below 2.5 floor
- MSI (Information Technology, score 80.0): acceptance breakout but R:R 0.46 below 2.5 floor
- SOLV (Health Care, score 80.0): acceptance breakout but R:R 0.73 below 2.5 floor
- TDY (Information Technology, score 80.0): acceptance breakout but R:R 1.5 below 2.5 floor
- EOG (Energy, score 80.0): pullback to value but R:R 1.02 below 2.5 floor
- CVX (Energy, score 80.0): pullback to value but R:R 1.37 below 2.5 floor
- LLY (Health Care, score 77.4): acceptance breakout but R:R 1.8 below 2.5 floor
- CVS (Health Care, score 69.2): pullback to value but R:R 1.67 below 2.5 floor
- OKE (Energy, score 63.3): pullback to value but R:R 1.97 below 2.5 floor
- UNH (Health Care, score 60.0): pullback to value but R:R 0.52 below 2.5 floor
- WST (Health Care, score 60.0): pullback to value but R:R 1.74 below 2.5 floor
- TRGP (Energy, score 60.0): pullback to value but R:R 0.66 below 2.5 floor
- ELV (Health Care, score 60.0): pullback to value but R:R 1.11 below 2.5 floor
- FANG (Energy, score 59.0): pullback to value but R:R 1.21 below 2.5 floor
- BAX (Health Care, score 40.0): breakout extended (33 sessions above VAH)
- FTNT (Information Technology, score 40.0): pullback to value but R:R 1.66 below 2.5 floor
- IQV (Health Care, score 40.0): breakout extended (33 sessions above VAH)
- HPQ (Information Technology, score 40.0): breakout extended (12 sessions above VAH)
- GEN (Information Technology, score 40.0): breakout extended (12 sessions above VAH)
- A (Health Care, score 40.0): breakout extended (15 sessions above VAH)
- DGX (Health Care, score 40.0): breakout extended (14 sessions above VAH)
- LH (Health Care, score 40.0): breakout extended (14 sessions above VAH)
- AMGN (Health Care, score 40.0): breakout extended (13 sessions above VAH)
- INCY (Health Care, score 40.0): breakout extended (33 sessions above VAH)
- BMY (Health Care, score 40.0): breakout extended (18 sessions above VAH)
- APA (Energy, score 40.0): no qualifying structure yet
- WAT (Health Care, score 40.0): no qualifying structure yet
- RVTY (Health Care, score 40.0): no qualifying structure yet
- XOM (Energy, score 40.0): no qualifying structure yet
- COP (Energy, score 40.0): pullback to value but R:R 1.1 below 2.5 floor
- HUM (Health Care, score 20.0): breakout extended (44 sessions above VAH)
- CNC (Health Care, score 20.0): closes above VAH but flow not confirming
- FFIV (Information Technology, score 20.0): no qualifying structure yet
- ASML (Information Technology, score 20.0): no qualifying structure yet
- PANW (Information Technology, score 0.0): breakout extended (41 sessions above VAH)
- DELL (Information Technology, score 0.0): no qualifying structure yet
- HPE (Information Technology, score 0.0): closes above VAH but flow not confirming
- CRWD (Information Technology, score 0.0): breakout extended (31 sessions above VAH)
- NTAP (Information Technology, score 0.0): breakout extended (15 sessions above VAH)
- CRL (Health Care, score 0.0): breakout extended (33 sessions above VAH)
- VLO (Energy, score 0.0): breakout extended (30 sessions above VAH)
- MPC (Energy, score 0.0): breakout extended (24 sessions above VAH)
- APH (Information Technology, score 0.0): no qualifying structure yet
- PSX (Energy, score 0.0): breakout extended (24 sessions above VAH)
- HSIC (Health Care, score 0.0): breakout extended (23 sessions above VAH)
- JNJ (Health Care, score 0.0): breakout extended (31 sessions above VAH)
- MRK (Health Care, score 0.0): breakout extended (19 sessions above VAH)
- EW (Health Care, score 0.0): closes above VAH but flow not confirming
- ETN (AI Infrastructure, score 0.0): closes above VAH but flow not confirming
- BIIB (Health Care, score 0.0): no qualifying structure yet

**Near-misses (failed exactly one screen filter):**

- ALAB (Information Technology): failed “near 52w high”
- SHOP (Information Technology): failed “50DMA > 200DMA”
- CDW (Information Technology): failed “near 52w high”
- TMO (Health Care): failed “50DMA > 200DMA”
- COO (Health Care): failed “50DMA > 200DMA”
- MTD (Health Care): failed “50DMA > 200DMA”
- ARM (Information Technology): failed “near 52w high”
- COR (Health Care): failed “50DMA > 200DMA”
- MRVL (Information Technology): failed “near 52w high”
- DHR (Health Care): failed “50DMA > 200DMA”
- MSFT (Information Technology): failed “50DMA > 200DMA”
- SYK (Health Care): failed “50DMA > 200DMA”
- AMAT (Information Technology): failed “near 52w high”
- MCK (Health Care): failed “50DMA > 200DMA”
- ZBH (Health Care): failed “50DMA > 200DMA”
- MDT (Health Care): failed “50DMA > 200DMA”
- STE (Health Care): failed “50DMA > 200DMA”
- MU (Information Technology): failed “near 52w high”
- REGN (Health Care): failed “50DMA > 200DMA”
- MRNA (Health Care): failed “near 52w high”
- FSLR (Information Technology): failed “near 52w high”
- PFE (Health Care): failed “50DMA > 200DMA”
- ALGN (Health Care): failed “63d return beats SPY”
- HUBB (AI Infrastructure): failed “63d return beats SPY”
- VRSN (Information Technology): failed “63d return beats SPY”
- NVDA (Information Technology): failed “63d return beats SPY”
- KMI (Energy): failed “63d return beats SPY”
- BKR (Energy): failed “63d return beats SPY”
- WMB (Energy): failed “63d return beats SPY”
- SLB (Energy): failed “63d return beats SPY”
- DVN (Energy): failed “63d return beats SPY”
- DLR (AI Infrastructure): failed “63d return beats SPY”
- AVGO (Information Technology): failed “63d return beats SPY”
- EQIX (AI Infrastructure): failed “63d return beats SPY”
- CI (Health Care): failed “63d return beats SPY”
- VTRS (Health Care): failed “63d return beats SPY”
- IRM (AI Infrastructure): failed “63d return beats SPY”
- JBL (Information Technology): failed “63d return beats SPY”
- KEYS (Information Technology): failed “63d return beats SPY”
- ADI (Information Technology): failed “63d return beats SPY”

---
*Generated by Ideas Engine. Research tool — not investment advice.*