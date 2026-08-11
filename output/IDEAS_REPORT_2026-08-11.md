# IDEAS REPORT — 2026-08-11

## ① Regime: RISK_ON_TRENDING

SPY in confirmed uptrend and 3/3 macro checks risk-on — full idea generation.

| Signal | Reading | Rule | Verdict |
|---|---|---|---|
| Credit stress (HY OAS) | 2.70% | < 21d MA (2.75) and < p75 of 252d (2.95) | PASS |
| Yield curve (10y-2y) | +0.48% (positive, steepening) | informational only in v1 | — |
| Volatility (VIX) | 15.5 | < 22 and < 50d MA (17.3) | PASS |
| Financial conditions (NFCI) | -0.53 | < 0.0 (loose) | PASS |
| SPY trend | 771 vs 200DMA 701 | Close > 200DMA, 50DMA > 200DMA, 200DMA slope up over 21d | PASS |
| SPY range check | 63d range 7.8% | ranging if < 8% and no MA alignment | — |

## ② Sector rotation

| ETF | Sector | 21d rel | 63d rel | RS-ratio | RS-mom | Quadrant | Selected |
|---|---|---|---|---|---|---|---|
| IGV | Software (breadth 54%) | +9.25% | +10.11% | 109.0 | +10.59% | Leading | #1 |
| XLV | Health Care (breadth 82%) | +1.23% | +13.48% | 102.1 | +1.92% | Leading | #2 |
| XBI | Biotech (breadth 82%) | -1.10% | +12.92% | 107.4 | -2.76% | Weakening |  |
| XLF | Financials (breadth 84%) | +0.23% | +8.83% | 102.2 | +0.69% | Leading | #3 |
| XLE | Energy | +4.53% | +2.85% | 99.1 | +3.00% | Improving |  |
| XLI | Industrials | +0.10% | +1.85% | 98.8 | +0.04% | Improving |  |
| XLB | Materials | +2.40% | -2.24% | 96.6 | +3.17% | Improving |  |
| XLK | Information Technology (breadth 54%) | -0.20% | +0.24% | 105.8 | -2.31% | Weakening |  |
| XLY | Consumer Discretionary | -0.10% | -4.41% | 95.7 | +2.26% | Improving |  |
| XLP | Consumer Staples | -2.74% | -2.21% | 93.4 | -1.71% | Lagging |  |
| XLRE | Real Estate | -4.24% | -4.73% | 94.0 | -4.34% | Lagging |  |
| SMH | Semiconductors (breadth 54%) | -5.02% | -5.08% | 104.6 | -8.65% | Weakening |  |
| XLC | Communication Services | -3.14% | -7.98% | 91.0 | -0.72% | Lagging |  |
| XLU | Utilities | -7.43% | -7.22% | 89.2 | -6.66% | Lagging |  |
| AI_INFRA | AI Infrastructure (breadth 53%) | -2.45% | -1.49% | 101.2 | -5.65% | Weakening | #4 |

## ③ Ranked ideas (6)

### 1. DXCM — Acceptance breakout above value (score 65.2)

Dexcom — acceptance breakout above value in Health Care (sector rank #2), relative strength top 9% of candidates, flow confirming.

- **Entry:** 75.48 (Buy-stop on retest of VAH (75.11 + 0.5%))
- **Stop:** 71.54 (below anchored VWAP, 5.2% risk)
- **Target:** 89.53 (52-week high)
- **R:R:** 3.56  |  **Free-flow (+1R):** 79.43
- **Risks:**
  - (high) Extended 25% above anchored VWAP — heavy chase risk; wait for the limit level, do not buy at market.
  - (info) Stop sits 5.2% below entry (~1.2 ATR), below anchored VWAP.
  - (medium) At 52-week highs: target is a measured-move projection with no overhead volume reference — take partial profits mechanically.
  - (info) Entry limit sits 15.7% below current price — the order may never fill; do not chase if it runs away.

### 2. TECH — Pullback to value (score 33.0)

Bio-Techne — pullback to value in Health Care (sector rank #2), relative strength top 8% of candidates, flow diverging.

- **Entry:** 70.93 (Limit at POC (70.93))
- **Stop:** 65.88 (below anchored VWAP, 7.1% risk)
- **Target:** 91.12 (measured move (value-area width projected))
- **R:R:** 4.0  |  **Free-flow (+1R):** 75.97
- **Risks:**
  - (medium) Trading 10% above anchored VWAP — mildly extended; prefer limit fills over market entries.
  - (high) Volume-flow divergence: price made new highs that the flow line did not confirm — demand may be thinning.
  - (info) Stop sits 7.1% below entry (~16.8 ATR), below anchored VWAP.
  - (medium) At 52-week highs: target is a measured-move projection with no overhead volume reference — take partial profits mechanically.

### 3. PFG — Pullback to value (score 21.3)

Principal Financial Group — pullback to value in Financials (sector rank #3), relative strength top 67% of candidates, flow confirming.

- **Entry:** 113.03 (At market (price already inside ±1% of POC))
- **Stop:** 102.73 (below anchored VWAP, 9.1% risk)
- **Target:** 141.18 (measured move (value-area width projected))
- **R:R:** 2.73  |  **Free-flow (+1R):** 123.33
- **Risks:**
  - (high) Extended 10% above anchored VWAP — heavy chase risk; wait for the limit level, do not buy at market.
  - (info) Stop sits 9.1% below entry (~4.1 ATR), below anchored VWAP.
  - (info) Reward/risk of 2.73 is close to the 2.5 floor — any slippage on entry meaningfully degrades the trade.

### 4. CNC — Pullback to value (score 19.7)

Centene Corporation — pullback to value in Health Care (sector rank #2), relative strength top 64% of candidates, flow neutral.

- **Entry:** 64.88 (At market (price at high-volume node))
- **Stop:** 56.18 (below anchored VWAP, 13.4% risk)
- **Target:** 95.06 (measured move (value-area width projected))
- **R:R:** 3.47  |  **Free-flow (+1R):** 73.58
- **Risks:**
  - (high) Extended 15% above anchored VWAP — heavy chase risk; wait for the limit level, do not buy at market.
  - (info) No flow confirmation yet (daily close-vs-open volume proxy is flat).
  - (medium) Wide structural stop (13.4% below entry) — halve position size so dollar risk stays constant.

### 5. PGR — Pullback to value (score 10.4)

Progressive Corporation — pullback to value in Financials (sector rank #3), relative strength top 83% of candidates, flow neutral.

- **Entry:** 212.35 (At market (price at high-volume node))
- **Stop:** 207.45 (below anchored VWAP (widened to 1 ATR), 2.3% risk)
- **Target:** 237.26 (52-week high)
- **R:R:** 5.08  |  **Free-flow (+1R):** 217.25
- **Risks:**
  - (info) No flow confirmation yet (daily close-vs-open volume proxy is flat).
  - (info) Stop sits 2.3% below entry (~1.0 ATR), below anchored VWAP (widened to 1 ATR).

### 6. ACGL — Pullback to value (score 0.6)

Arch Capital Group — pullback to value in Financials (sector rank #3), relative strength top 99% of candidates, flow neutral.

- **Entry:** 99.27 (Limit at high-volume node (99.27))
- **Stop:** 96.68 (below anchored VWAP (widened to 1 ATR), 2.6% risk)
- **Target:** 106.48 (52-week high)
- **R:R:** 2.78  |  **Free-flow (+1R):** 101.86
- **Risks:**
  - (info) No flow confirmation yet (daily close-vs-open volume proxy is flat).
  - (info) Stop sits 2.6% below entry (~1.0 ATR), below anchored VWAP (widened to 1 ATR).
  - (info) Reward/risk of 2.78 is close to the 2.5 floor — any slippage on entry meaningfully degrades the trade.

## ④ Appendix

**Watch — no valid trade yet:**

- HIG (Financials, score 89.1): pullback to value but R:R 1.79 below 2.5 floor
- ANET (Information Technology, score 80.0): acceptance breakout but R:R 2.49 below 2.5 floor
- CAH (Health Care, score 80.0): pullback to value but R:R 2.48 below 2.5 floor
- CSCO (Information Technology, score 80.0): acceptance breakout but R:R 0.68 below 2.5 floor
- PNC (Financials, score 80.0): pullback to value but R:R 2.24 below 2.5 floor
- GL (Financials, score 80.0): pullback to value but R:R 2.02 below 2.5 floor
- AIZ (Financials, score 80.0): pullback to value but R:R 0.56 below 2.5 floor
- SYF (Financials, score 80.0): acceptance breakout but R:R 1.75 below 2.5 floor
- TDY (Information Technology, score 80.0): acceptance breakout but R:R 0.93 below 2.5 floor
- BEN (Financials, score 80.0): acceptance breakout but R:R 1.38 below 2.5 floor
- MET (Financials, score 78.7): pullback to value but R:R 0.37 below 2.5 floor
- CB (Financials, score 74.1): pullback to value but R:R 2.41 below 2.5 floor
- KEY (Financials, score 62.0): pullback to value but R:R 0.6 below 2.5 floor
- HUM (Health Care, score 60.0): pullback to value but R:R 0.45 below 2.5 floor
- PRU (Financials, score 60.0): pullback to value but R:R 0.85 below 2.5 floor
- MTB (Financials, score 60.0): pullback to value but R:R 1.62 below 2.5 floor
- BNY (Financials, score 60.0): pullback to value but R:R 1.54 below 2.5 floor
- FITB (Financials, score 60.0): pullback to value but R:R 0.28 below 2.5 floor
- MRK (Health Care, score 60.0): pullback to value but R:R 1.43 below 2.5 floor
- ASML (Information Technology, score 60.0): pullback to value but R:R 1.18 below 2.5 floor
- MS (Financials, score 60.0): pullback to value but R:R 0.87 below 2.5 floor
- WST (Health Care, score 60.0): pullback to value but R:R 1.77 below 2.5 floor
- UNH (Health Care, score 60.0): pullback to value but R:R 0.89 below 2.5 floor
- USB (Financials, score 59.8): pullback to value but R:R 1.04 below 2.5 floor
- TROW (Financials, score 59.7): pullback to value but R:R 0.79 below 2.5 floor
- GS (Financials, score 59.4): pullback to value but R:R 2.09 below 2.5 floor
- TFC (Financials, score 58.7): pullback to value but R:R 1.23 below 2.5 floor
- HBAN (Financials, score 58.2): pullback to value but R:R 1.87 below 2.5 floor
- ZBRA (Information Technology, score 40.0): breakout extended (11 sessions above VAH)
- BAX (Health Care, score 40.0): breakout extended (34 sessions above VAH)
- IQV (Health Care, score 40.0): breakout extended (34 sessions above VAH)
- FTNT (Information Technology, score 40.0): pullback to value but R:R 1.65 below 2.5 floor
- HPQ (Information Technology, score 40.0): breakout extended (13 sessions above VAH)
- A (Health Care, score 40.0): breakout extended (16 sessions above VAH)
- GEN (Information Technology, score 40.0): breakout extended (13 sessions above VAH)
- HSIC (Health Care, score 40.0): breakout extended (24 sessions above VAH)
- BDX (Health Care, score 40.0): breakout extended (11 sessions above VAH)
- LH (Health Care, score 40.0): breakout extended (15 sessions above VAH)
- AMGN (Health Care, score 40.0): breakout extended (11 sessions above VAH)
- DGX (Health Care, score 40.0): breakout extended (15 sessions above VAH)
- GPN (Financials, score 40.0): breakout extended (20 sessions above VAH)
- STT (Financials, score 40.0): pullback to value but R:R 2.38 below 2.5 floor
- ABBV (Health Care, score 40.0): pullback to value but R:R 0.78 below 2.5 floor
- ALL (Financials, score 40.0): breakout extended (32 sessions above VAH)
- SCHW (Financials, score 40.0): breakout extended (28 sessions above VAH)
- DDOG (Information Technology, score 40.0): no qualifying structure yet
- AMP (Financials, score 40.0): breakout extended (29 sessions above VAH)
- JPM (Financials, score 40.0): breakout extended (29 sessions above VAH)
- RJF (Financials, score 40.0): breakout extended (28 sessions above VAH)
- WFC (Financials, score 40.0): pullback to value but R:R 1.62 below 2.5 floor
- MSI (Information Technology, score 40.0): pullback to value but R:R 0.57 below 2.5 floor
- WAT (Health Care, score 40.0): no qualifying structure yet
- CPAY (Financials, score 40.0): breakout extended (12 sessions above VAH)
- RVTY (Health Care, score 40.0): no qualifying structure yet
- BMY (Health Care, score 40.0): breakout extended (19 sessions above VAH)
- SOLV (Health Care, score 40.0): breakout extended (11 sessions above VAH)
- V (Financials, score 40.0): breakout extended (32 sessions above VAH)
- XYZ (Financials, score 40.0): no qualifying structure yet
- BRK-B (Financials, score 40.0): breakout extended (12 sessions above VAH)
- HUBB (AI Infrastructure, score 40.0): pullback to value but R:R 2.01 below 2.5 floor
- BAC (Financials, score 38.4): breakout extended (42 sessions above VAH)
- L (Financials, score 36.1): breakout extended (19 sessions above VAH)
- CINF (Financials, score 33.5): breakout extended (35 sessions above VAH)
- AFL (Financials, score 24.9): breakout extended (28 sessions above VAH)
- MCO (Financials, score 20.2): breakout extended (28 sessions above VAH)
- TRV (Financials, score 20.0): breakout extended (32 sessions above VAH)
- INCY (Health Care, score 20.0): breakout extended (34 sessions above VAH)
- RF (Financials, score 20.0): closes above VAH but flow not confirming
- CFG (Financials, score 20.0): breakout extended (20 sessions above VAH)
- JNJ (Health Care, score 20.0): breakout extended (32 sessions above VAH)
- NTRS (Financials, score 20.0): no qualifying structure yet
- FFIV (Information Technology, score 20.0): no qualifying structure yet
- AON (Financials, score 20.0): breakout extended (29 sessions above VAH)
- WRB (Financials, score 20.0): below anchored VWAP
- IBKR (Financials, score 20.0): no qualifying structure yet
- ALGN (Health Care, score 20.0): below anchored VWAP
- EG (Financials, score 20.0): breakout extended (32 sessions above VAH)
- PANW (Information Technology, score 0.0): breakout extended (42 sessions above VAH)
- DELL (Information Technology, score 0.0): no qualifying structure yet
- HPE (Information Technology, score 0.0): closes above VAH but flow not confirming
- NTAP (Information Technology, score 0.0): breakout extended (16 sessions above VAH)
- CRL (Health Care, score 0.0): no qualifying structure yet
- CRWD (Information Technology, score 0.0): breakout extended (32 sessions above VAH)
- APH (Information Technology, score 0.0): no qualifying structure yet
- LLY (Health Care, score 0.0): closes above VAH but flow not confirming
- VRTX (Health Care, score 0.0): closes above VAH but flow not confirming
- EW (Health Care, score 0.0): closes above VAH but flow not confirming
- IVZ (Financials, score 0.0): no qualifying structure yet
- ETN (AI Infrastructure, score 0.0): closes above VAH but flow not confirming
- C (Financials, score 0.0): closes above VAH but flow not confirming

**Near-misses (failed exactly one screen filter):**

- ALAB (Information Technology): failed “near 52w high”
- SHOP (Information Technology): failed “50DMA > 200DMA”
- WTW (Financials): failed “50DMA > 200DMA”
- TMO (Health Care): failed “50DMA > 200DMA”
- MTD (Health Care): failed “50DMA > 200DMA”
- CDW (Information Technology): failed “near 52w high”
- COO (Health Care): failed “50DMA > 200DMA”
- FDS (Financials): failed “near 52w high”
- COR (Health Care): failed “50DMA > 200DMA”
- AJG (Financials): failed “near 52w high”
- ARM (Information Technology): failed “near 52w high”
- DHR (Health Care): failed “50DMA > 200DMA”
- MCK (Health Care): failed “50DMA > 200DMA”
- MRVL (Information Technology): failed “near 52w high”
- SYK (Health Care): failed “50DMA > 200DMA”
- MDT (Health Care): failed “50DMA > 200DMA”
- ZBH (Health Care): failed “50DMA > 200DMA”
- MSFT (Information Technology): failed “50DMA > 200DMA”
- COF (Financials): failed “50DMA > 200DMA”
- MRSH (Financials): failed “50DMA > 200DMA”
- AMAT (Information Technology): failed “near 52w high”
- STE (Health Care): failed “50DMA > 200DMA”
- MRNA (Health Care): failed “near 52w high”
- MA (Financials): failed “50DMA > 200DMA”
- REGN (Health Care): failed “50DMA > 200DMA”
- AXP (Financials): failed “50DMA > 200DMA”
- MU (Information Technology): failed “near 52w high”
- KLAC (Information Technology): failed “near 52w high”
- APO (Financials): failed “50DMA > 200DMA”
- NDAQ (Financials): failed “50DMA > 200DMA”
- BLK (Financials): failed “50DMA > 200DMA”
- TEL (Information Technology): failed “50DMA > 200DMA”
- LRCX (Information Technology): failed “near 52w high”
- PFE (Health Care): failed “50DMA > 200DMA”
- AAPL (Information Technology): failed “63d return beats SPY”
- BIIB (Health Care): failed “63d return beats SPY”
- ELV (Health Care): failed “63d return beats SPY”
- AIG (Financials): failed “63d return beats SPY”
- CVS (Health Care): failed “63d return beats SPY”
- VRSN (Information Technology): failed “63d return beats SPY”
- NVDA (Information Technology): failed “63d return beats SPY”
- DLR (AI Infrastructure): failed “63d return beats SPY”
- JBL (Information Technology): failed “63d return beats SPY”
- AVGO (Information Technology): failed “63d return beats SPY”
- VTRS (Health Care): failed “63d return beats SPY”
- EQIX (AI Infrastructure): failed “63d return beats SPY”
- TXN (Information Technology): failed “63d return beats SPY”
- IRM (AI Infrastructure): failed “63d return beats SPY”
- GEV (AI Infrastructure): failed “63d return beats SPY”
- KEYS (Information Technology): failed “63d return beats SPY”
- ADI (Information Technology): failed “63d return beats SPY”
- PWR (AI Infrastructure): failed “63d return beats SPY”

---
*Generated by Ideas Engine. Research tool — not investment advice.*