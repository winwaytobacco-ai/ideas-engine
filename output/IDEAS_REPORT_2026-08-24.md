# IDEAS REPORT — 2026-08-24

## ① Regime: RISK_ON_TRENDING

SPY in confirmed uptrend and 3/3 macro checks risk-on — full idea generation.

| Signal | Reading | Rule | Verdict |
|---|---|---|---|
| Credit stress (HY OAS) | 2.70% | < 21d MA (2.75) and < p75 of 252d (2.95) | PASS |
| Yield curve (10y-2y) | +0.46% (positive, steepening) | informational only in v1 | — |
| Volatility (VIX) | 15.1 | < 22 and < 50d MA (16.7) | PASS |
| Financial conditions (NFCI) | -0.56 | < 0.0 (loose) | PASS |
| SPY trend | 763 vs 200DMA 705 | Close > 200DMA, 50DMA > 200DMA, 200DMA slope up over 21d | PASS |
| SPY range check | 63d range 8.2% | ranging if < 8% and no MA alignment | — |

## ② Sector rotation

| ETF | Sector | 21d rel | 63d rel | RS-ratio | RS-mom | Quadrant | Selected |
|---|---|---|---|---|---|---|---|
| XBI | Biotech (breadth 85%) | +5.78% | +22.16% | 111.5 | +3.60% | Leading | #1 |
| IGV | Software (breadth 43%) | +13.13% | +6.34% | 107.5 | +11.92% | Leading | #2 |
| XLV | Health Care (breadth 85%) | +4.14% | +14.41% | 107.3 | +4.53% | Leading | #3 |
| XLF | Financials | +0.07% | +9.83% | 103.9 | +0.32% | Leading |  |
| XLE | Energy | +2.53% | +4.20% | 103.4 | +1.69% | Leading |  |
| XLB | Materials | +1.20% | +4.29% | 99.0 | +2.61% | Improving |  |
| XLP | Consumer Staples | +0.63% | +1.19% | 98.3 | +2.33% | Improving |  |
| XLY | Consumer Discretionary | +4.80% | -3.20% | 96.5 | +6.78% | Improving |  |
| XLC | Communication Services | +2.34% | -5.12% | 93.7 | +4.89% | Improving |  |
| XLI | Industrials | -5.32% | +1.81% | 96.6 | -4.66% | Lagging |  |
| XLK | Information Technology (breadth 43%) | -0.95% | -2.72% | 102.1 | -3.23% | Weakening |  |
| XLRE | Real Estate | -4.67% | -0.04% | 98.0 | -4.14% | Lagging |  |
| SMH | Semiconductors (breadth 43%) | -5.89% | -7.78% | 99.3 | -8.87% | Lagging |  |
| XLU | Utilities | -9.95% | -6.74% | 90.1 | -8.21% | Lagging |  |
| AI_INFRA | AI Infrastructure (breadth 40%) | -8.41% | -6.06% | 95.4 | -10.22% | Lagging | #4 |

## ③ Ranked ideas (5)

### 1. TECH — Pullback to value (score 38.2)

Bio-Techne — pullback to value in Health Care (sector rank #1), relative strength top 5% of candidates, flow diverging.

- **Entry:** 71.15 (Limit at high-volume node (71.15))
- **Stop:** 66.34 (below anchored VWAP, 6.8% risk)
- **Target:** 91.5 (measured move (value-area width projected))
- **R:R:** 4.24  |  **Free-flow (+1R):** 75.95
- **Risks:**
  - (medium) Trading 9% above anchored VWAP — mildly extended; prefer limit fills over market entries.
  - (high) Volume-flow divergence: price made new highs that the flow line did not confirm — demand may be thinning.
  - (info) Stop sits 6.8% below entry (~17.2 ATR), below anchored VWAP.
  - (medium) At 52-week highs: target is a measured-move projection with no overhead volume reference — take partial profits mechanically.

### 2. HSIC — Pullback to value (score 38.2)

Henry Schein — pullback to value in Health Care (sector rank #1), relative strength top 52% of candidates, flow confirming.

- **Entry:** 89.51 (At market (price at high-volume node))
- **Stop:** 81.77 (below anchored VWAP, 8.6% risk)
- **Target:** 109.09 (measured move (value-area width projected))
- **R:R:** 2.53  |  **Free-flow (+1R):** 97.25
- **Risks:**
  - (medium) Trading 9% above anchored VWAP — mildly extended; prefer limit fills over market entries.
  - (info) Stop sits 8.6% below entry (~4.1 ATR), below anchored VWAP.
  - (info) Reward/risk of 2.53 is close to the 2.5 floor — any slippage on entry meaningfully degrades the trade.
  - (medium) At 52-week highs: target is a measured-move projection with no overhead volume reference — take partial profits mechanically.

### 3. APH — Pullback to value (score 24.6)

Amphenol — pullback to value in Information Technology (sector rank #2), relative strength top 64% of candidates, flow neutral.

- **Entry:** 157.28 (Limit at high-volume node (157.28))
- **Stop:** 151.51 (below anchored VWAP (widened to 1 ATR), 3.7% risk)
- **Target:** 176.32 (52-week high)
- **R:R:** 3.3  |  **Free-flow (+1R):** 163.05
- **Risks:**
  - (info) No flow confirmation yet (daily close-vs-open volume proxy is flat).
  - (info) Stop sits 3.7% below entry (~1.0 ATR), below anchored VWAP (widened to 1 ATR).

### 4. CAH — Pullback to value (score 11.5)

Cardinal Health — pullback to value in Health Care (sector rank #1), relative strength top 73% of candidates, flow diverging.

- **Entry:** 235.61 (Limit at high-volume node (235.61))
- **Stop:** 222.35 (below anchored VWAP, 5.6% risk)
- **Target:** 277.08 (measured move (value-area width projected))
- **R:R:** 3.13  |  **Free-flow (+1R):** 248.87
- **Risks:**
  - (high) Volume-flow divergence: price made new highs that the flow line did not confirm — demand may be thinning.
  - (info) Stop sits 5.6% below entry (~1.9 ATR), below anchored VWAP.

### 5. ETN — Pullback to value (score 1.8)

Eaton Corporation — pullback to value in AI Infrastructure (sector rank #4), relative strength top 95% of candidates, flow diverging.

- **Entry:** 402.45 (Limit at POC (402.45))
- **Stop:** 389.13 (below anchored VWAP (widened to 1 ATR), 3.3% risk)
- **Target:** 459.96 (52-week high)
- **R:R:** 4.32  |  **Free-flow (+1R):** 415.77
- **Risks:**
  - (high) Volume-flow divergence: price made new highs that the flow line did not confirm — demand may be thinning.
  - (info) Stop sits 3.3% below entry (~1.0 ATR), below anchored VWAP (widened to 1 ATR).
  - (medium) AI-infrastructure basket is Lagging vs SPY — the theme tailwind is fading; this idea rests on stock-specific strength.
- **OODA (AI-infrastructure theme):**
  - *Observe:*
    - Profitable today: trailing 12m EPS 9.81, net margin 13%
    - Real demand: quarterly revenue growing +21% YoY
    - Order-book proxy: forward EPS 16.03 above trailing 9.81 — analysts see the pipeline growing
    - Price structure: pullback to value, flow diverging, +2.6% vs anchored VWAP.
    - Order-book data is not in free feeds — forward-vs-trailing EPS is the proxy.
  - *Orient:*
    - AI-infrastructure basket is Lagging vs SPY (RS-ratio 95.4, momentum -10.2%), included by config policy 'always'.
    - Regime RISK_ON_TRENDING: SPY in confirmed uptrend and 3/3 macro checks risk-on — full idea generation.
    - Theme breadth: 40% of basket members above their 50DMA.
  - *Decide:*
    - Earnings-backed: PASS — kept in the ranked list. Use the AI-infra filter above the ideas grid to exclude (or isolate) theme names if you judge the theme crowded.
  - *Act:*
    - Execute per the plan below — entry, structural stop, target, free-flow at +1R, and regime invalidation.

## ④ Appendix

**Watch — no valid trade yet:**

- PANW (Information Technology, score 80.0): pullback to value but R:R 0.42 below 2.5 floor
- CNC (Health Care, score 80.0): pullback to value but R:R 0.55 below 2.5 floor
- GILD (Health Care, score 80.0): acceptance breakout but R:R 1.31 below 2.5 floor
- UNH (Health Care, score 60.0): pullback to value but R:R 0.7 below 2.5 floor
- WST (Health Care, score 59.9): pullback to value but R:R 0.27 below 2.5 floor
- EW (Health Care, score 45.2): breakout extended (16 sessions above VAH)
- CRL (Health Care, score 40.0): breakout extended (23 sessions above VAH)
- IQV (Health Care, score 40.0): breakout extended (41 sessions above VAH)
- ZBRA (Information Technology, score 40.0): breakout extended (20 sessions above VAH)
- TMO (Health Care, score 40.0): breakout extended (23 sessions above VAH)
- NTAP (Information Technology, score 40.0): breakout extended (21 sessions above VAH)
- A (Health Care, score 40.0): breakout extended (23 sessions above VAH)
- AMGN (Health Care, score 40.0): breakout extended (23 sessions above VAH)
- LH (Health Care, score 40.0): breakout extended (23 sessions above VAH)
- BDX (Health Care, score 40.0): breakout extended (20 sessions above VAH)
- RVTY (Health Care, score 40.0): no qualifying structure yet
- DXCM (Health Care, score 40.0): breakout extended (17 sessions above VAH)
- HUM (Health Care, score 40.0): no qualifying structure yet
- DGX (Health Care, score 40.0): breakout extended (24 sessions above VAH)
- MRK (Health Care, score 40.0): breakout extended (28 sessions above VAH)
- WAT (Health Care, score 40.0): no qualifying structure yet
- JNJ (Health Care, score 40.0): breakout extended (24 sessions above VAH)
- BMY (Health Care, score 40.0): breakout extended (25 sessions above VAH)
- ASML (Information Technology, score 40.0): no qualifying structure yet
- GEN (Information Technology, score 39.7): breakout extended (38 sessions above VAH)
- ZBH (Health Care, score 38.3): breakout extended (11 sessions above VAH)
- BAX (Health Care, score 20.0): breakout extended (43 sessions above VAH)
- INCY (Health Care, score 20.0): breakout extended (30 sessions above VAH)
- FTNT (Information Technology, score 20.0): breakout extended (42 sessions above VAH)
- DELL (Information Technology, score 0.0): no qualifying structure yet
- HPE (Information Technology, score 0.0): no qualifying structure yet
- VRTX (Health Care, score 0.0): no qualifying structure yet
- ABBV (Health Care, score 0.0): no qualifying structure yet
- ANET (Information Technology, score 0.0): no qualifying structure yet
- MSI (Information Technology, score 0.0): closes above VAH but flow not confirming
- SOLV (Health Care, score 0.0): no qualifying structure yet
- LLY (Health Care, score 0.0): breakout extended (14 sessions above VAH)
- HPQ (Information Technology, score 0.0): breakout extended (22 sessions above VAH)
- BIIB (Health Care, score 0.0): closes above VAH but flow not confirming

**Near-misses (failed exactly one screen filter):**

- MRNA (Health Care): failed “near 52w high”
- ABT (Health Care): failed “50DMA > 200DMA”
- REGN (Health Care): failed “50DMA > 200DMA”
- MTD (Health Care): failed “50DMA > 200DMA”
- DHR (Health Care): failed “50DMA > 200DMA”
- MU (Information Technology): failed “near 52w high”
- COO (Health Care): failed “50DMA > 200DMA”
- CDW (Information Technology): failed “near 52w high”
- MDT (Health Care): failed “50DMA > 200DMA”
- COR (Health Care): failed “50DMA > 200DMA”
- MRVL (Information Technology): failed “near 52w high”
- MSFT (Information Technology): failed “50DMA > 200DMA”
- CRWD (Information Technology): failed “near 52w high”
- MCK (Health Care): failed “50DMA > 200DMA”
- AMAT (Information Technology): failed “near 52w high”
- STE (Health Care): failed “50DMA > 200DMA”
- PFE (Health Care): failed “50DMA > 200DMA”
- ELV (Health Care): failed “63d return beats SPY”
- CVS (Health Care): failed “63d return beats SPY”
- TDY (Information Technology): failed “63d return beats SPY”
- AAPL (Information Technology): failed “63d return beats SPY”
- VTRS (Health Care): failed “63d return beats SPY”
- DLR (AI Infrastructure): failed “63d return beats SPY”
- CI (Health Care): failed “63d return beats SPY”
- EQIX (AI Infrastructure): failed “63d return beats SPY”
- NVDA (Information Technology): failed “63d return beats SPY”
- IRM (AI Infrastructure): failed “63d return beats SPY”
- FFIV (Information Technology): failed “63d return beats SPY”
- VRSN (Information Technology): failed “63d return beats SPY”
- CSCO (Information Technology): failed “63d return beats SPY”

---
*Generated by Ideas Engine. Research tool — not investment advice.*