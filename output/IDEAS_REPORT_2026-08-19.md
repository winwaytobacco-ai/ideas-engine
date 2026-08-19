# IDEAS REPORT — 2026-08-19

## ① Regime: RISK_ON_TRENDING

SPY in confirmed uptrend and 3/3 macro checks risk-on — full idea generation.

| Signal | Reading | Rule | Verdict |
|---|---|---|---|
| Credit stress (HY OAS) | 2.75% | < 21d MA (2.75) and < p75 of 252d (2.95) | PASS |
| Yield curve (10y-2y) | +0.46% (positive, steepening) | informational only in v1 | — |
| Volatility (VIX) | 15.8 | < 22 and < 50d MA (16.9) | PASS |
| Financial conditions (NFCI) | -0.56 | < 0.0 (loose) | PASS |
| SPY trend | 769 vs 200DMA 704 | Close > 200DMA, 50DMA > 200DMA, 200DMA slope up over 21d | PASS |
| SPY range check | 63d range 8.2% | ranging if < 8% and no MA alignment | — |

## ② Sector rotation

| ETF | Sector | 21d rel | 63d rel | RS-ratio | RS-mom | Quadrant | Selected |
|---|---|---|---|---|---|---|---|
| XBI | Biotech (breadth 83%) | +6.96% | +28.77% | 114.7 | +4.95% | Leading | #1 |
| XLV | Health Care (breadth 83%) | +6.85% | +14.69% | 107.1 | +7.33% | Leading | #2 |
| IGV | Software (breadth 49%) | +9.19% | +6.75% | 107.5 | +9.01% | Leading | #3 |
| XLF | Financials | -0.34% | +7.79% | 101.9 | -0.00% | Weakening |  |
| XLE | Energy | +5.91% | -0.60% | 103.5 | +4.76% | Leading |  |
| XLB | Materials | +2.05% | +2.41% | 96.1 | +3.29% | Improving |  |
| XLI | Industrials | -0.94% | +3.01% | 97.2 | -0.63% | Lagging |  |
| XLK | Information Technology (breadth 49%) | -1.19% | +1.04% | 103.7 | -3.43% | Weakening |  |
| XLY | Consumer Discretionary | +0.46% | -1.78% | 95.8 | +2.67% | Improving |  |
| XLP | Consumer Staples | +0.17% | -3.86% | 96.3 | +1.71% | Improving |  |
| XLRE | Real Estate | -4.16% | -0.65% | 96.4 | -3.88% | Lagging |  |
| SMH | Semiconductors (breadth 49%) | -6.74% | -1.97% | 101.6 | -9.93% | Weakening |  |
| XLU | Utilities | -4.78% | -5.17% | 90.8 | -3.54% | Lagging |  |
| XLC | Communication Services | -3.17% | -8.98% | 91.8 | -0.58% | Lagging |  |
| AI_INFRA | AI Infrastructure (breadth 53%) | -4.20% | +0.85% | 97.5 | -6.67% | Lagging | #4 |

## ③ Ranked ideas (3)

### 1. TECH — Pullback to value (score 35.7)

Bio-Techne — pullback to value in Health Care (sector rank #1), relative strength top 11% of candidates, flow diverging.

- **Entry:** 71.15 (Limit at high-volume node (71.15))
- **Stop:** 66.17 (below anchored VWAP, 7.0% risk)
- **Target:** 91.5 (measured move (value-area width projected))
- **R:R:** 4.09  |  **Free-flow (+1R):** 76.12
- **Risks:**
  - (medium) Trading 10% above anchored VWAP — mildly extended; prefer limit fills over market entries.
  - (high) Volume-flow divergence: price made new highs that the flow line did not confirm — demand may be thinning.
  - (info) Stop sits 7.0% below entry (~17.8 ATR), below anchored VWAP.
  - (medium) At 52-week highs: target is a measured-move projection with no overhead volume reference — take partial profits mechanically.

### 2. CAH — Pullback to value (score 10.4)

Cardinal Health — pullback to value in Health Care (sector rank #1), relative strength top 74% of candidates, flow diverging.

- **Entry:** 234.85 (At market (price already inside ±1% of POC))
- **Stop:** 222.1 (below anchored VWAP, 5.4% risk)
- **Target:** 277.08 (measured move (value-area width projected))
- **R:R:** 3.31  |  **Free-flow (+1R):** 247.6
- **Risks:**
  - (medium) Trading 6% above anchored VWAP — mildly extended; prefer limit fills over market entries.
  - (high) Volume-flow divergence: price made new highs that the flow line did not confirm — demand may be thinning.
  - (info) Stop sits 5.4% below entry (~1.8 ATR), below anchored VWAP.

### 3. TDY — Pullback to value (score 1.9)

Teledyne Technologies — pullback to value in Information Technology (sector rank #3), relative strength top 96% of candidates, flow diverging.

- **Entry:** 648.63 (At market (price at high-volume node))
- **Stop:** 633.52 (below anchored VWAP (widened to 1 ATR), 2.3% risk)
- **Target:** 691.3 (52-week high)
- **R:R:** 2.82  |  **Free-flow (+1R):** 663.74
- **Risks:**
  - (high) Volume-flow divergence: price made new highs that the flow line did not confirm — demand may be thinning.
  - (info) Stop sits 2.3% below entry (~1.0 ATR), below anchored VWAP (widened to 1 ATR).
  - (info) Reward/risk of 2.82 is close to the 2.5 floor — any slippage on entry meaningfully degrades the trade.

## ④ Appendix

**Watch — no valid trade yet:**

- ASML (Information Technology, score 80.0): pullback to value but R:R 1.58 below 2.5 floor
- AAPL (Information Technology, score 60.0): pullback to value but R:R 1.84 below 2.5 floor
- WST (Health Care, score 59.9): pullback to value but R:R 0.28 below 2.5 floor
- MRNA (Health Care, score 40.0): no qualifying structure yet
- CRL (Health Care, score 40.0): breakout extended (38 sessions above VAH)
- NTAP (Information Technology, score 40.0): breakout extended (19 sessions above VAH)
- PANW (Information Technology, score 40.0): breakout extended (43 sessions above VAH)
- ZBRA (Information Technology, score 40.0): breakout extended (17 sessions above VAH)
- TMO (Health Care, score 40.0): breakout extended (20 sessions above VAH)
- DXCM (Health Care, score 40.0): breakout extended (14 sessions above VAH)
- MRK (Health Care, score 40.0): breakout extended (26 sessions above VAH)
- AMGN (Health Care, score 40.0): breakout extended (20 sessions above VAH)
- CRWD (Information Technology, score 40.0): breakout extended (38 sessions above VAH)
- LH (Health Care, score 40.0): breakout extended (21 sessions above VAH)
- BDX (Health Care, score 40.0): breakout extended (18 sessions above VAH)
- DGX (Health Care, score 40.0): breakout extended (20 sessions above VAH)
- WAT (Health Care, score 40.0): no qualifying structure yet
- RVTY (Health Care, score 40.0): no qualifying structure yet
- HSIC (Health Care, score 40.0): no qualifying structure yet
- JNJ (Health Care, score 40.0): breakout extended (22 sessions above VAH)
- BMY (Health Care, score 40.0): breakout extended (25 sessions above VAH)
- ETN (AI Infrastructure, score 40.0): pullback to value but R:R 1.32 below 2.5 floor
- EW (Health Care, score 40.0): breakout extended (13 sessions above VAH)
- CNC (Health Care, score 40.0): pullback to value but R:R 0.49 below 2.5 floor
- GEN (Information Technology, score 39.6): breakout extended (35 sessions above VAH)
- ZBH (Health Care, score 37.1): breakout extended (17 sessions above VAH)
- APH (Information Technology, score 33.9): no qualifying structure yet
- BAX (Health Care, score 20.0): breakout extended (39 sessions above VAH)
- INCY (Health Care, score 20.0): breakout extended (27 sessions above VAH)
- HUM (Health Care, score 20.0): no qualifying structure yet
- FTNT (Information Technology, score 20.0): breakout extended (39 sessions above VAH)
- DELL (Information Technology, score 0.0): no qualifying structure yet
- HPE (Information Technology, score 0.0): breakout extended (13 sessions above VAH)
- HPQ (Information Technology, score 0.0): breakout extended (19 sessions above VAH)
- IQV (Health Care, score 0.0): breakout extended (39 sessions above VAH)
- A (Health Care, score 0.0): breakout extended (21 sessions above VAH)
- ANET (Information Technology, score 0.0): no qualifying structure yet
- ABBV (Health Care, score 0.0): no qualifying structure yet
- VRTX (Health Care, score 0.0): no qualifying structure yet
- LLY (Health Care, score 0.0): breakout extended (11 sessions above VAH)
- MSI (Information Technology, score 0.0): no qualifying structure yet
- BIIB (Health Care, score 0.0): no qualifying structure yet
- SOLV (Health Care, score 0.0): breakout extended (16 sessions above VAH)

**Near-misses (failed exactly one screen filter):**

- MTD (Health Care): failed “50DMA > 200DMA”
- MRVL (Information Technology): failed “near 52w high”
- MU (Information Technology): failed “near 52w high”
- REGN (Health Care): failed “50DMA > 200DMA”
- CDW (Information Technology): failed “near 52w high”
- ABT (Health Care): failed “50DMA > 200DMA”
- DHR (Health Care): failed “50DMA > 200DMA”
- COO (Health Care): failed “50DMA > 200DMA”
- AMAT (Information Technology): failed “near 52w high”
- MDT (Health Care): failed “50DMA > 200DMA”
- ALAB (Information Technology): failed “near 52w high”
- TER (Information Technology): failed “near 52w high”
- MSFT (Information Technology): failed “50DMA > 200DMA”
- GILD (Health Care): failed “50DMA > 200DMA”
- STX (Information Technology): failed “near 52w high”
- SNDK (Information Technology): failed “near 52w high”
- NBIS (Information Technology): failed “near 52w high”
- AMD (Information Technology): failed “near 52w high”
- LRCX (Information Technology): failed “near 52w high”
- MCK (Health Care): failed “50DMA > 200DMA”
- PFE (Health Care): failed “50DMA > 200DMA”
- ARM (Information Technology): failed “near 52w high”
- STE (Health Care): failed “50DMA > 200DMA”
- DDOG (Information Technology): failed “near 52w high”
- KLAC (Information Technology): failed “near 52w high”
- SYK (Health Care): failed “50DMA > 200DMA”
- DLR (AI Infrastructure): failed “63d return beats SPY”
- EQIX (AI Infrastructure): failed “63d return beats SPY”
- VTRS (Health Care): failed “63d return beats SPY”
- UNH (Health Care): failed “63d return beats SPY”
- CVS (Health Care): failed “63d return beats SPY”
- FFIV (Information Technology): failed “63d return beats SPY”
- IRM (AI Infrastructure): failed “63d return beats SPY”
- ELV (Health Care): failed “63d return beats SPY”
- NVDA (Information Technology): failed “63d return beats SPY”
- CSCO (Information Technology): failed “63d return beats SPY”
- CI (Health Care): failed “63d return beats SPY”
- PWR (AI Infrastructure): failed “63d return beats SPY”
- KEYS (Information Technology): failed “63d return beats SPY”
- VRSN (Information Technology): failed “63d return beats SPY”

---
*Generated by Ideas Engine. Research tool — not investment advice.*