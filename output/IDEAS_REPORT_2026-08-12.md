# IDEAS REPORT — 2026-08-12

## ① Regime: RISK_ON_TRENDING

SPY in confirmed uptrend and 3/3 macro checks risk-on — full idea generation.

| Signal | Reading | Rule | Verdict |
|---|---|---|---|
| Credit stress (HY OAS) | 2.72% | < 21d MA (2.75) and < p75 of 252d (2.95) | PASS |
| Yield curve (10y-2y) | +0.48% (positive, steepening) | informational only in v1 | — |
| Volatility (VIX) | 15.3 | < 22 and < 50d MA (17.3) | PASS |
| Financial conditions (NFCI) | -0.55 | < 0.0 (loose) | PASS |
| SPY trend | 772 vs 200DMA 702 | Close > 200DMA, 50DMA > 200DMA, 200DMA slope up over 21d | PASS |
| SPY range check | 63d range 7.8% | ranging if < 8% and no MA alignment | — |

## ② Sector rotation

| ETF | Sector | 21d rel | 63d rel | RS-ratio | RS-mom | Quadrant | Selected |
|---|---|---|---|---|---|---|---|
| IGV | Software (breadth 62%) | +7.34% | +10.35% | 107.8 | +8.47% | Leading | #1 |
| XLV | Health Care (breadth 85%) | +3.66% | +11.08% | 102.1 | +4.26% | Leading | #2 |
| XBI | Biotech (breadth 85%) | -0.21% | +13.34% | 107.9 | -1.90% | Weakening |  |
| XLF | Financials (breadth 86%) | +0.35% | +7.77% | 102.1 | +0.78% | Leading | #3 |
| XLE | Energy | +4.42% | +1.86% | 99.0 | +2.96% | Improving |  |
| XLK | Information Technology (breadth 62%) | +0.11% | +3.01% | 106.9 | -2.03% | Weakening |  |
| XLI | Industrials | -0.13% | +1.23% | 98.6 | -0.32% | Lagging |  |
| XLB | Materials | +1.00% | -2.70% | 95.1 | +1.71% | Improving |  |
| XLP | Consumer Staples | -0.76% | -3.46% | 93.7 | +0.32% | Improving |  |
| SMH | Semiconductors (breadth 62%) | -5.33% | -0.72% | 106.3 | -8.86% | Weakening |  |
| XLRE | Real Estate | -2.23% | -3.94% | 94.6 | -2.39% | Lagging |  |
| XLY | Consumer Discretionary | -1.77% | -6.72% | 94.3 | +0.63% | Improving |  |
| XLC | Communication Services | -3.55% | -10.46% | 89.9 | -1.13% | Lagging |  |
| XLU | Utilities | -6.80% | -7.29% | 89.5 | -5.98% | Lagging |  |
| AI_INFRA | AI Infrastructure (breadth 73%) | -1.10% | +3.60% | 104.6 | -4.54% | Weakening | #4 |

## ③ Ranked ideas (4)

### 1. ANET — Acceptance breakout above value (score 71.2)

Arista Networks — acceptance breakout above value in Information Technology (sector rank #1), relative strength top 11% of candidates, flow confirming.

- **Entry:** 169.98 (Buy-stop on retest of VAH (169.13 + 0.5%))
- **Stop:** 158.27 (below anchored VWAP (widened to 1 ATR), 6.9% risk)
- **Target:** 210.5 (52-week high)
- **R:R:** 3.46  |  **Free-flow (+1R):** 181.69
- **Risks:**
  - (high) Extended 30% above anchored VWAP — heavy chase risk; wait for the limit level, do not buy at market.
  - (info) Stop sits 6.9% below entry (~1.0 ATR), below anchored VWAP (widened to 1 ATR).
  - (medium) At 52-week highs: target is a measured-move projection with no overhead volume reference — take partial profits mechanically.
  - (info) Entry limit sits 19.2% below current price — the order may never fill; do not chase if it runs away.
  - (medium) AI-infrastructure basket is Weakening vs SPY — the theme tailwind is fading; this idea rests on stock-specific strength.
- **OODA (AI-infrastructure theme):**
  - *Observe:*
    - Profitable today: trailing 12m EPS 3.17, net margin 38%
    - Real demand: quarterly revenue growing +38% YoY
    - Order-book proxy: forward EPS 5.16 above trailing 3.17 — analysts see the pipeline growing
    - Price structure: acceptance breakout above value, flow confirming, +30.0% vs anchored VWAP.
    - Order-book data is not in free feeds — forward-vs-trailing EPS is the proxy.
  - *Orient:*
    - AI-infrastructure basket is Weakening vs SPY (RS-ratio 104.6, momentum -4.5%), included by config policy 'always'.
    - Regime RISK_ON_TRENDING: SPY in confirmed uptrend and 3/3 macro checks risk-on — full idea generation.
    - Theme breadth: 62% of basket members above their 50DMA.
  - *Decide:*
    - Earnings-backed: PASS — kept in the ranked list. Use the AI-infra filter above the ideas grid to exclude (or isolate) theme names if you judge the theme crowded.
  - *Act:*
    - Execute per the plan below — entry, structural stop, target, free-flow at +1R, and regime invalidation.

### 2. TECH — Pullback to value (score 31.3)

Bio-Techne — pullback to value in Health Care (sector rank #2), relative strength top 13% of candidates, flow diverging.

- **Entry:** 70.93 (Limit at POC (70.93))
- **Stop:** 65.73 (below anchored VWAP, 7.3% risk)
- **Target:** 91.71 (measured move (value-area width projected))
- **R:R:** 4.0  |  **Free-flow (+1R):** 76.12
- **Risks:**
  - (medium) Trading 10% above anchored VWAP — mildly extended; prefer limit fills over market entries.
  - (high) Volume-flow divergence: price made new highs that the flow line did not confirm — demand may be thinning.
  - (info) Stop sits 7.3% below entry (~16.8 ATR), below anchored VWAP.
  - (medium) At 52-week highs: target is a measured-move projection with no overhead volume reference — take partial profits mechanically.

### 3. CAH — Pullback to value (score 26.1)

Cardinal Health — pullback to value in Health Care (sector rank #2), relative strength top 27% of candidates, flow diverging.

- **Entry:** 237.17 (Limit at POC (237.17))
- **Stop:** 221.1 (below anchored VWAP, 6.8% risk)
- **Target:** 278.64 (measured move (value-area width projected))
- **R:R:** 2.58  |  **Free-flow (+1R):** 253.25
- **Risks:**
  - (medium) Trading 6% above anchored VWAP — mildly extended; prefer limit fills over market entries.
  - (high) Volume-flow divergence: price made new highs that the flow line did not confirm — demand may be thinning.
  - (info) Stop sits 6.8% below entry (~2.4 ATR), below anchored VWAP.
  - (info) Reward/risk of 2.58 is close to the 2.5 floor — any slippage on entry meaningfully degrades the trade.

### 4. LLY — Pullback to value (score 21.6)

Lilly (Eli) — pullback to value in Health Care (sector rank #2), relative strength top 36% of candidates, flow diverging.

- **Entry:** 1205.41 (Limit at high-volume node (1205.41))
- **Stop:** 1106.02 (below anchored VWAP, 8.2% risk)
- **Target:** 1461.66 (measured move (value-area width projected))
- **R:R:** 2.58  |  **Free-flow (+1R):** 1304.79
- **Risks:**
  - (high) Extended 10% above anchored VWAP — heavy chase risk; wait for the limit level, do not buy at market.
  - (high) Volume-flow divergence: price made new highs that the flow line did not confirm — demand may be thinning.
  - (info) Stop sits 8.2% below entry (~2.4 ATR), below anchored VWAP.
  - (info) Reward/risk of 2.58 is close to the 2.5 floor — any slippage on entry meaningfully degrades the trade.
  - (medium) At 52-week highs: target is a measured-move projection with no overhead volume reference — take partial profits mechanically.

## ④ Appendix

**Watch — no valid trade yet:**

- DXCM (Health Care, score 80.0): acceptance breakout but R:R 2.21 below 2.5 floor
- CSCO (Information Technology, score 80.0): acceptance breakout but R:R 0.69 below 2.5 floor
- AIZ (Financials, score 80.0): pullback to value but R:R 0.56 below 2.5 floor
- GL (Financials, score 80.0): pullback to value but R:R 0.57 below 2.5 floor
- TDY (Information Technology, score 80.0): acceptance breakout but R:R 0.92 below 2.5 floor
- BEN (Financials, score 80.0): acceptance breakout but R:R 1.37 below 2.5 floor
- SYF (Financials, score 80.0): acceptance breakout but R:R 1.77 below 2.5 floor
- PFG (Financials, score 79.1): pullback to value but R:R 2.41 below 2.5 floor
- MET (Financials, score 78.8): pullback to value but R:R 0.26 below 2.5 floor
- CB (Financials, score 78.4): pullback to value but R:R 1.61 below 2.5 floor
- TRV (Financials, score 60.0): pullback to value but R:R 0.46 below 2.5 floor
- PRU (Financials, score 60.0): pullback to value but R:R 0.79 below 2.5 floor
- ABBV (Health Care, score 60.0): pullback to value but R:R 0.93 below 2.5 floor
- MTB (Financials, score 60.0): pullback to value but R:R 1.48 below 2.5 floor
- ASML (Information Technology, score 60.0): pullback to value but R:R 1.05 below 2.5 floor
- FITB (Financials, score 60.0): pullback to value but R:R 0.35 below 2.5 floor
- MS (Financials, score 60.0): pullback to value but R:R 0.44 below 2.5 floor
- WST (Health Care, score 60.0): pullback to value but R:R 1.64 below 2.5 floor
- KEY (Financials, score 60.0): pullback to value but R:R 0.61 below 2.5 floor
- ELV (Health Care, score 60.0): pullback to value but R:R 1.11 below 2.5 floor
- GS (Financials, score 59.5): pullback to value but R:R 1.96 below 2.5 floor
- HBAN (Financials, score 58.3): pullback to value but R:R 1.61 below 2.5 floor
- BRK-B (Financials, score 42.5): breakout extended (13 sessions above VAH)
- HUBB (AI Infrastructure, score 40.8): pullback to value but R:R 1.84 below 2.5 floor
- ZBRA (Information Technology, score 40.0): breakout extended (11 sessions above VAH)
- CRWD (Information Technology, score 40.0): breakout extended (33 sessions above VAH)
- FTNT (Information Technology, score 40.0): pullback to value but R:R 1.7 below 2.5 floor
- HPQ (Information Technology, score 40.0): breakout extended (14 sessions above VAH)
- IQV (Health Care, score 40.0): breakout extended (33 sessions above VAH)
- CPAY (Financials, score 40.0): breakout extended (13 sessions above VAH)
- AMGN (Health Care, score 40.0): breakout extended (12 sessions above VAH)
- GEN (Information Technology, score 40.0): breakout extended (14 sessions above VAH)
- GPN (Financials, score 40.0): breakout extended (21 sessions above VAH)
- LH (Health Care, score 40.0): breakout extended (17 sessions above VAH)
- DGX (Health Care, score 40.0): breakout extended (14 sessions above VAH)
- SCHW (Financials, score 40.0): breakout extended (29 sessions above VAH)
- AMP (Financials, score 40.0): breakout extended (27 sessions above VAH)
- ALL (Financials, score 40.0): breakout extended (34 sessions above VAH)
- BDX (Health Care, score 40.0): breakout extended (11 sessions above VAH)
- JPM (Financials, score 40.0): breakout extended (30 sessions above VAH)
- PNC (Financials, score 40.0): pullback to value but R:R 2.23 below 2.5 floor
- RVTY (Health Care, score 40.0): no qualifying structure yet
- SOLV (Health Care, score 40.0): breakout extended (11 sessions above VAH)
- WAT (Health Care, score 40.0): no qualifying structure yet
- RJF (Financials, score 40.0): breakout extended (26 sessions above VAH)
- BMY (Health Care, score 40.0): breakout extended (19 sessions above VAH)
- V (Financials, score 40.0): breakout extended (33 sessions above VAH)
- BAC (Financials, score 39.8): breakout extended (43 sessions above VAH)
- L (Financials, score 35.6): breakout extended (17 sessions above VAH)
- CINF (Financials, score 34.8): breakout extended (34 sessions above VAH)
- AFL (Financials, score 25.8): breakout extended (27 sessions above VAH)
- HUM (Health Care, score 20.0): breakout extended (45 sessions above VAH)
- INCY (Health Care, score 20.0): breakout extended (32 sessions above VAH)
- FFIV (Information Technology, score 20.0): no qualifying structure yet
- CNC (Health Care, score 20.0): closes above VAH but flow not confirming
- JNJ (Health Care, score 20.0): breakout extended (33 sessions above VAH)
- CFG (Financials, score 20.0): breakout extended (22 sessions above VAH)
- RF (Financials, score 20.0): closes above VAH but flow not confirming
- AON (Financials, score 20.0): breakout extended (28 sessions above VAH)
- IBKR (Financials, score 20.0): closes above VAH but flow not confirming
- WRB (Financials, score 20.0): below anchored VWAP
- PGR (Financials, score 20.0): below anchored VWAP
- TROW (Financials, score 19.8): breakout extended (31 sessions above VAH)
- TFC (Financials, score 18.8): no qualifying structure yet
- DELL (Information Technology, score 0.0): no qualifying structure yet
- HPE (Information Technology, score 0.0): closes above VAH but flow not confirming
- PANW (Information Technology, score 0.0): breakout extended (43 sessions above VAH)
- NTAP (Information Technology, score 0.0): breakout extended (15 sessions above VAH)
- CRL (Health Care, score 0.0): breakout extended (33 sessions above VAH)
- BAX (Health Care, score 0.0): breakout extended (33 sessions above VAH)
- NBIS (Information Technology, score 0.0): no qualifying structure yet
- APH (Information Technology, score 0.0): no qualifying structure yet
- HSIC (Health Care, score 0.0): breakout extended (22 sessions above VAH)
- A (Health Care, score 0.0): breakout extended (15 sessions above VAH)
- STT (Financials, score 0.0): no qualifying structure yet
- BNY (Financials, score 0.0): breakout extended (30 sessions above VAH)
- WFC (Financials, score 0.0): no qualifying structure yet
- VRTX (Health Care, score 0.0): closes above VAH but flow not confirming
- NTRS (Financials, score 0.0): no qualifying structure yet
- MRK (Health Care, score 0.0): breakout extended (21 sessions above VAH)
- USB (Financials, score 0.0): breakout extended (35 sessions above VAH)
- EW (Health Care, score 0.0): closes above VAH but flow not confirming
- IVZ (Financials, score 0.0): no qualifying structure yet
- ETN (AI Infrastructure, score 0.0): closes above VAH but flow not confirming
- C (Financials, score 0.0): closes above VAH but flow not confirming
- BIIB (Health Care, score 0.0): no qualifying structure yet
- MSI (Information Technology, score 0.0): closes above VAH but flow not confirming

**Near-misses (failed exactly one screen filter):**

- ALAB (Information Technology): failed “near 52w high”
- WTW (Financials): failed “50DMA > 200DMA”
- MRVL (Information Technology): failed “near 52w high”
- TMO (Health Care): failed “50DMA > 200DMA”
- ARM (Information Technology): failed “near 52w high”
- AJG (Financials): failed “near 52w high”
- AMAT (Information Technology): failed “near 52w high”
- COO (Health Care): failed “50DMA > 200DMA”
- CDW (Information Technology): failed “near 52w high”
- FDS (Financials): failed “near 52w high”
- DHR (Health Care): failed “50DMA > 200DMA”
- MDT (Health Care): failed “50DMA > 200DMA”
- SYK (Health Care): failed “50DMA > 200DMA”
- COF (Financials): failed “50DMA > 200DMA”
- MSFT (Information Technology): failed “50DMA > 200DMA”
- DDOG (Information Technology): failed “near 52w high”
- MRNA (Health Care): failed “near 52w high”
- MU (Information Technology): failed “near 52w high”
- ZBH (Health Care): failed “50DMA > 200DMA”
- MRSH (Financials): failed “50DMA > 200DMA”
- MCK (Health Care): failed “50DMA > 200DMA”
- KLAC (Information Technology): failed “near 52w high”
- LRCX (Information Technology): failed “near 52w high”
- REGN (Health Care): failed “50DMA > 200DMA”
- TER (Information Technology): failed “near 52w high”
- MA (Financials): failed “50DMA > 200DMA”
- STE (Health Care): failed “50DMA > 200DMA”
- AXP (Financials): failed “50DMA > 200DMA”
- BLK (Financials): failed “50DMA > 200DMA”
- MTD (Health Care): failed “50DMA > 200DMA”
- STX (Information Technology): failed “near 52w high”
- NDAQ (Financials): failed “50DMA > 200DMA”
- AMD (Information Technology): failed “near 52w high”
- SWKS (Information Technology): failed “near 52w high”
- MCO (Financials): failed “63d return beats SPY”
- JBL (Information Technology): failed “63d return beats SPY”
- HIG (Financials): failed “63d return beats SPY”
- XYZ (Financials): failed “63d return beats SPY”
- EG (Financials): failed “63d return beats SPY”
- ACGL (Financials): failed “63d return beats SPY”
- ALGN (Health Care): failed “63d return beats SPY”
- UNH (Health Care): failed “63d return beats SPY”
- AAPL (Information Technology): failed “63d return beats SPY”
- VRSN (Information Technology): failed “63d return beats SPY”
- NVDA (Information Technology): failed “63d return beats SPY”
- DLR (AI Infrastructure): failed “63d return beats SPY”
- CVS (Health Care): failed “63d return beats SPY”
- KEYS (Information Technology): failed “63d return beats SPY”
- AVGO (Information Technology): failed “63d return beats SPY”
- EQIX (AI Infrastructure): failed “63d return beats SPY”
- IRM (AI Infrastructure): failed “63d return beats SPY”
- GEV (AI Infrastructure): failed “63d return beats SPY”
- CI (Health Care): failed “63d return beats SPY”
- VTRS (Health Care): failed “63d return beats SPY”
- LITE (Information Technology): failed “63d return beats SPY”
- ADI (Information Technology): failed “63d return beats SPY”
- PWR (AI Infrastructure): failed “63d return beats SPY”

---
*Generated by Ideas Engine. Research tool — not investment advice.*