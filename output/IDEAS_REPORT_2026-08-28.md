# IDEAS REPORT — 2026-08-28

## ① Regime: RISK_ON_TRENDING

SPY in confirmed uptrend and 3/3 macro checks risk-on — full idea generation.

| Signal | Reading | Rule | Verdict |
|---|---|---|---|
| Credit stress (HY OAS) | 2.67% | < 21d MA (2.73) and < p75 of 252d (2.95) | PASS |
| Yield curve (10y-2y) | +0.47% (positive, steepening) | informational only in v1 | — |
| Volatility (VIX) | 15.2 | < 22 and < 50d MA (16.6) | PASS |
| Financial conditions (NFCI) | -0.57 | < 0.0 (loose) | PASS |
| SPY trend | 771 vs 200DMA 707 | Close > 200DMA, 50DMA > 200DMA, 200DMA slope up over 21d | PASS |
| SPY range check | 63d range 8.1% | ranging if < 8% and no MA alignment | — |

## ② Sector rotation

| ETF | Sector | 21d rel | 63d rel | RS-ratio | RS-mom | Quadrant | Selected |
|---|---|---|---|---|---|---|---|
| XBI | Biotech (breadth 77%) | +8.03% | +21.38% | 112.6 | +5.37% | Leading | #1 |
| IGV | Software (breadth 51%) | +13.72% | +12.87% | 114.2 | +11.40% | Leading | #2 |
| XLV | Health Care (breadth 77%) | -2.50% | +11.77% | 104.4 | -1.86% | Weakening |  |
| XLE | Energy | +0.50% | +7.72% | 101.0 | -0.09% | Weakening |  |
| XLF | Financials | -3.59% | +10.84% | 102.3 | -3.16% | Weakening |  |
| XLK | Information Technology (breadth 51%) | +7.52% | -1.39% | 105.5 | +4.47% | Leading | #3 |
| SMH | Semiconductors (breadth 51%) | +7.93% | -6.92% | 102.6 | +3.94% | Leading |  |
| XLB | Materials | -2.83% | +1.58% | 97.6 | -1.11% | Lagging |  |
| XLI | Industrials | -4.50% | +0.68% | 95.7 | -3.47% | Lagging |  |
| XLY | Consumer Discretionary | -1.88% | -7.32% | 93.9 | +0.10% | Improving |  |
| XLP | Consumer Staples | -8.32% | -0.98% | 95.0 | -6.00% | Lagging |  |
| XLRE | Real Estate | -8.54% | -1.01% | 95.8 | -7.44% | Lagging |  |
| XLC | Communication Services | -3.97% | -6.71% | 92.4 | -1.26% | Lagging |  |
| XLU | Utilities | -9.56% | -5.08% | 89.5 | -7.21% | Lagging |  |
| AI_INFRA | AI Infrastructure (breadth 40%) | +5.22% | -2.19% | 97.8 | +2.94% | Improving | #4 |

## ③ Ranked ideas (3)

### 1. TECH — Pullback to value (score 34.7)

Bio-Techne — pullback to value in Health Care (sector rank #1), relative strength top 13% of candidates, flow diverging.

- **Entry:** 71.07 (Limit at high-volume node (71.07))
- **Stop:** 66.37 (below anchored VWAP, 6.6% risk)
- **Target:** 91.99 (measured move (value-area width projected))
- **R:R:** 4.45  |  **Free-flow (+1R):** 75.76
- **Risks:**
  - (medium) Trading 9% above anchored VWAP — mildly extended; prefer limit fills over market entries.
  - (high) Volume-flow divergence: price made new highs that the flow line did not confirm — demand may be thinning.
  - (info) Stop sits 6.6% below entry (~18.8 ATR), below anchored VWAP.
  - (medium) At 52-week highs: target is a measured-move projection with no overhead volume reference — take partial profits mechanically.

### 2. CAH — Pullback to value (score 21.5)

Cardinal Health — pullback to value in Health Care (sector rank #1), relative strength top 64% of candidates, flow neutral.

- **Entry:** 235.13 (At market (price already inside ±1% of POC))
- **Stop:** 222.69 (below anchored VWAP, 5.3% risk)
- **Target:** 277.08 (measured move (value-area width projected))
- **R:R:** 3.37  |  **Free-flow (+1R):** 247.57
- **Risks:**
  - (medium) Trading 6% above anchored VWAP — mildly extended; prefer limit fills over market entries.
  - (info) No flow confirmation yet (daily close-vs-open volume proxy is flat).
  - (info) Stop sits 5.3% below entry (~1.9 ATR), below anchored VWAP.

### 3. ASML — Pullback to value (score 12.2)

ASML Holding — pullback to value in Information Technology (sector rank #2), relative strength top 83% of candidates, flow confirming.

- **Entry:** 1735.01 (At market (price at high-volume node))
- **Stop:** 1650.66 (below anchored VWAP, 4.9% risk)
- **Target:** 1986.87 (52-week high)
- **R:R:** 2.99  |  **Free-flow (+1R):** 1819.36
- **Risks:**
  - (medium) Trading 5% above anchored VWAP — mildly extended; prefer limit fills over market entries.
  - (info) Stop sits 4.9% below entry (~1.7 ATR), below anchored VWAP.
  - (info) Reward/risk of 2.99 is close to the 2.5 floor — any slippage on entry meaningfully degrades the trade.

## ④ Appendix

**Watch — no valid trade yet:**

- INCY (Health Care, score 80.0): pullback to value but R:R 1.24 below 2.5 floor
- HUM (Health Care, score 80.0): pullback to value but R:R 2.29 below 2.5 floor
- MSI (Information Technology, score 80.0): acceptance breakout but R:R 0.33 below 2.5 floor
- LITE (Information Technology, score 80.0): pullback to value but R:R 1.79 below 2.5 floor
- CNC (Health Care, score 80.0): pullback to value but R:R 0.4 below 2.5 floor
- PFE (Health Care, score 80.0): acceptance breakout but R:R 1.11 below 2.5 floor
- BIIB (Health Care, score 78.6): acceptance breakout but R:R 1.65 below 2.5 floor
- EW (Health Care, score 68.1): pullback to value but R:R 0.96 below 2.5 floor
- UNH (Health Care, score 60.2): pullback to value but R:R 0.99 below 2.5 floor
- HPE (Information Technology, score 60.0): pullback to value but R:R 0.4 below 2.5 floor
- MTD (Health Care, score 60.0): pullback to value but R:R 0.47 below 2.5 floor
- HSIC (Health Care, score 60.0): pullback to value but R:R 1.75 below 2.5 floor
- WST (Health Care, score 60.0): pullback to value but R:R 0.29 below 2.5 floor
- FFIV (Information Technology, score 60.0): pullback to value but R:R 0.38 below 2.5 floor
- VTRS (Health Care, score 60.0): pullback to value but R:R 0.83 below 2.5 floor
- VEEV (Health Care, score 40.0): breakout extended (24 sessions above VAH)
- CRL (Health Care, score 40.0): breakout extended (23 sessions above VAH)
- IQV (Health Care, score 40.0): breakout extended (44 sessions above VAH)
- CRWD (Information Technology, score 40.0): breakout extended (43 sessions above VAH)
- NTAP (Information Technology, score 40.0): breakout extended (23 sessions above VAH)
- AMGN (Health Care, score 40.0): breakout extended (26 sessions above VAH)
- TMO (Health Care, score 40.0): breakout extended (26 sessions above VAH)
- LH (Health Care, score 40.0): breakout extended (26 sessions above VAH)
- RVTY (Health Care, score 40.0): no qualifying structure yet
- BDX (Health Care, score 40.0): breakout extended (23 sessions above VAH)
- MRK (Health Care, score 40.0): breakout extended (27 sessions above VAH)
- DGX (Health Care, score 40.0): breakout extended (26 sessions above VAH)
- GEN (Information Technology, score 40.0): breakout extended (25 sessions above VAH)
- DXCM (Health Care, score 40.0): pullback to value but R:R 1.1 below 2.5 floor
- SOLV (Health Care, score 40.0): no qualifying structure yet
- BMY (Health Care, score 40.0): breakout extended (28 sessions above VAH)
- A (Health Care, score 40.0): no qualifying structure yet
- JNJ (Health Care, score 40.0): breakout extended (27 sessions above VAH)
- WAT (Health Care, score 40.0): no qualifying structure yet
- GILD (Health Care, score 40.0): breakout extended (11 sessions above VAH)
- ZBH (Health Care, score 38.3): breakout extended (14 sessions above VAH)
- LLY (Health Care, score 37.8): pullback to value but R:R 1.78 below 2.5 floor
- ETN (AI Infrastructure, score 22.5): no qualifying structure yet
- APH (Information Technology, score 20.8): no qualifying structure yet
- DELL (Information Technology, score 20.0): breakout extended (19 sessions above VAH)
- PANW (Information Technology, score 20.0): breakout extended (44 sessions above VAH)
- ZBRA (Information Technology, score 20.0): breakout extended (23 sessions above VAH)
- BAX (Health Care, score 20.0): breakout extended (25 sessions above VAH)
- CDW (Information Technology, score 20.0): no qualifying structure yet
- HPQ (Information Technology, score 20.0): breakout extended (25 sessions above VAH)
- ANET (Information Technology, score 19.6): no qualifying structure yet
- FTNT (Information Technology, score 0.0): breakout extended (22 sessions above VAH)
- VRTX (Health Care, score 0.0): breakout extended (15 sessions above VAH)
- ABBV (Health Care, score 0.0): no qualifying structure yet
- NVDA (Information Technology, score 0.0): no qualifying structure yet

**Near-misses (failed exactly one screen filter):**

- MRNA (Health Care): failed “near 52w high”
- CRM (Information Technology): failed “50DMA > 200DMA”
- SHOP (Information Technology): failed “50DMA > 200DMA”
- REGN (Health Care): failed “50DMA > 200DMA”
- PLTR (Information Technology): failed “50DMA > 200DMA”
- MDT (Health Care): failed “50DMA > 200DMA”
- DHR (Health Care): failed “50DMA > 200DMA”
- MSFT (Information Technology): failed “50DMA > 200DMA”
- MRVL (Information Technology): failed “near 52w high”
- MCK (Health Care): failed “50DMA > 200DMA”
- DDOG (Information Technology): failed “near 52w high”
- AMAT (Information Technology): failed “near 52w high”
- ELV (Health Care): failed “63d return beats SPY”
- EQIX (AI Infrastructure): failed “63d return beats SPY”
- DLR (AI Infrastructure): failed “63d return beats SPY”
- AAPL (Information Technology): failed “63d return beats SPY”
- VRSN (Information Technology): failed “63d return beats SPY”
- TDY (Information Technology): failed “63d return beats SPY”
- CI (Health Care): failed “63d return beats SPY”
- IRM (AI Infrastructure): failed “63d return beats SPY”
- KEYS (Information Technology): failed “63d return beats SPY”
- CSCO (Information Technology): failed “63d return beats SPY”

---
*Generated by Ideas Engine. Research tool — not investment advice.*