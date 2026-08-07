# IDEAS REPORT — 2026-08-07

## ① Regime: RISK_ON_TRENDING

SPY in confirmed uptrend and 3/3 macro checks risk-on — full idea generation.

| Signal | Reading | Rule | Verdict |
|---|---|---|---|
| Credit stress (HY OAS) | 2.71% | < 21d MA (2.75) and < p75 of 252d (2.95) | PASS |
| Yield curve (10y-2y) | +0.46% (positive, steepening) | informational only in v1 | — |
| Volatility (VIX) | 15.2 | < 22 and < 50d MA (17.3) | PASS |
| Financial conditions (NFCI) | -0.53 | < 0.0 (loose) | PASS |
| SPY trend | 773 vs 200DMA 700 | Close > 200DMA, 50DMA > 200DMA, 200DMA slope up over 21d | PASS |
| SPY range check | 63d range 7.8% | ranging if < 8% and no MA alignment | — |

## ② Sector rotation

| ETF | Sector | 21d rel | 63d rel | RS-ratio | RS-mom | Quadrant | Selected |
|---|---|---|---|---|---|---|---|
| IGV | Software (breadth 54%) | +6.52% | +7.08% | 107.5 | +8.50% | Leading | #1 |
| XLV | Health Care (breadth 80%) | -0.70% | +9.02% | 100.3 | +0.07% | Leading | #2 |
| XLF | Financials (breadth 91%) | +0.84% | +6.16% | 101.4 | +1.36% | Leading | #3 |
| XBI | Biotech (breadth 80%) | -7.07% | +11.89% | 106.8 | -8.50% | Weakening |  |
| XLK | Information Technology (breadth 54%) | -1.45% | +4.94% | 106.7 | -3.48% | Weakening |  |
| XLI | Industrials | -0.62% | +0.72% | 98.1 | -0.79% | Lagging |  |
| XLE | Energy | +2.02% | -2.46% | 93.3 | +0.46% | Improving |  |
| XLB | Materials | +2.31% | -2.74% | 95.5 | +2.95% | Improving |  |
| XLP | Consumer Staples | -0.56% | -3.91% | 93.4 | +0.21% | Improving |  |
| XLRE | Real Estate | -1.17% | -3.78% | 95.5 | -1.47% | Lagging |  |
| SMH | Semiconductors (breadth 54%) | -6.99% | +1.92% | 106.4 | -10.67% | Weakening |  |
| XLY | Consumer Discretionary | -0.29% | -5.79% | 95.7 | +2.13% | Improving |  |
| XLC | Communication Services | -2.20% | -10.95% | 90.5 | +0.20% | Improving |  |
| XLU | Utilities | -6.23% | -8.70% | 88.7 | -5.65% | Lagging |  |
| AI_INFRA | AI Infrastructure (breadth 47%) | -5.73% | -1.03% | 100.2 | -8.96% | Weakening | #4 |

## ③ Ranked ideas (10)

### 1. ZBRA — Acceptance breakout above value (score 75.7)

Zebra Technologies — acceptance breakout above value in Information Technology (sector rank #1), relative strength top 5% of candidates, flow confirming.

- **Entry:** 270.54 (Buy-stop on retest of VAH (269.19 + 0.5%))
- **Stop:** 251.91 (below anchored VWAP, 6.9% risk)
- **Target:** 376.49 (52-week high)
- **R:R:** 5.69  |  **Free-flow (+1R):** 289.16
- **Risks:**
  - (high) Extended 49% above anchored VWAP — heavy chase risk; wait for the limit level, do not buy at market.
  - (info) Stop sits 6.9% below entry (~1.1 ATR), below anchored VWAP.
  - (medium) At 52-week highs: target is a measured-move projection with no overhead volume reference — take partial profits mechanically.
  - (info) Entry limit sits 28.1% below current price — the order may never fill; do not chase if it runs away.

### 2. ANET — Acceptance breakout above value (score 67.2)

Arista Networks — acceptance breakout above value in Information Technology (sector rank #1), relative strength top 16% of candidates, flow confirming.

- **Entry:** 167.98 (Buy-stop on retest of VAH (167.14 + 0.5%))
- **Stop:** 156.92 (below anchored VWAP (widened to 1 ATR), 6.6% risk)
- **Target:** 197.31 (52-week high)
- **R:R:** 2.65  |  **Free-flow (+1R):** 179.04
- **Risks:**
  - (high) Extended 17% above anchored VWAP — heavy chase risk; wait for the limit level, do not buy at market.
  - (info) Stop sits 6.6% below entry (~1.0 ATR), below anchored VWAP (widened to 1 ATR).
  - (info) Reward/risk of 2.65 is close to the 2.5 floor — any slippage on entry meaningfully degrades the trade.
  - (info) Entry limit sits 11.0% below current price — the order may never fill; do not chase if it runs away.
  - (medium) AI-infrastructure basket is Weakening vs SPY — the theme tailwind is fading; this idea rests on stock-specific strength.
- **OODA (AI-infrastructure theme):**
  - *Observe:*
    - Profitable today: trailing 12m EPS 3.15, net margin 38%
    - Real demand: quarterly revenue growing +38% YoY
    - Order-book proxy: forward EPS 5.11 above trailing 3.15 — analysts see the pipeline growing
    - Price structure: acceptance breakout above value, flow confirming, +17.3% vs anchored VWAP.
    - Order-book data is not in free feeds — forward-vs-trailing EPS is the proxy.
  - *Orient:*
    - AI-infrastructure basket is Weakening vs SPY (RS-ratio 100.2, momentum -9.0%), included by config policy 'always'.
    - Regime RISK_ON_TRENDING: SPY in confirmed uptrend and 3/3 macro checks risk-on — full idea generation.
    - Theme breadth: 54% of basket members above their 50DMA.
  - *Decide:*
    - Earnings-backed: PASS — kept in the ranked list. Use the AI-infra filter above the ideas grid to exclude (or isolate) theme names if you judge the theme crowded.
  - *Act:*
    - Execute per the plan below — entry, structural stop, target, free-flow at +1R, and regime invalidation.

### 3. RVTY — Pullback to value (score 32.2)

Revvity — pullback to value in Health Care (sector rank #2), relative strength top 55% of candidates, flow confirming.

- **Entry:** 112.66 (Limit at high-volume node (112.66))
- **Stop:** 104.27 (below anchored VWAP, 7.5% risk)
- **Target:** 139.81 (measured move (value-area width projected))
- **R:R:** 3.23  |  **Free-flow (+1R):** 121.06
- **Risks:**
  - (medium) Trading 10% above anchored VWAP — mildly extended; prefer limit fills over market entries.
  - (info) Stop sits 7.5% below entry (~1.9 ATR), below anchored VWAP.

### 4. TECH — Pullback to value (score 31.4)

Bio-Techne — pullback to value in Health Care (sector rank #2), relative strength top 13% of candidates, flow diverging.

- **Entry:** 70.91 (Limit at POC (70.91))
- **Stop:** 65.68 (below anchored VWAP, 7.4% risk)
- **Target:** 91.67 (measured move (value-area width projected))
- **R:R:** 3.97  |  **Free-flow (+1R):** 76.14
- **Risks:**
  - (high) Extended 10% above anchored VWAP — heavy chase risk; wait for the limit level, do not buy at market.
  - (high) Volume-flow divergence: price made new highs that the flow line did not confirm — demand may be thinning.
  - (info) Stop sits 7.4% below entry (~17.4 ATR), below anchored VWAP.
  - (medium) At 52-week highs: target is a measured-move projection with no overhead volume reference — take partial profits mechanically.

### 5. CAH — Pullback to value (score 27.6)

Cardinal Health — pullback to value in Health Care (sector rank #2), relative strength top 20% of candidates, flow diverging.

- **Entry:** 236.4 (At market (price already inside ±1% of POC))
- **Stop:** 220.35 (below anchored VWAP, 6.8% risk)
- **Target:** 285.05 (measured move (value-area width projected))
- **R:R:** 3.03  |  **Free-flow (+1R):** 252.45
- **Risks:**
  - (medium) Trading 7% above anchored VWAP — mildly extended; prefer limit fills over market entries.
  - (high) Volume-flow divergence: price made new highs that the flow line did not confirm — demand may be thinning.
  - (info) Stop sits 6.8% below entry (~3.0 ATR), below anchored VWAP.
  - (medium) At 52-week highs: target is a measured-move projection with no overhead volume reference — take partial profits mechanically.

### 6. PFG — Pullback to value (score 22.3)

Principal Financial Group — pullback to value in Financials (sector rank #3), relative strength top 65% of candidates, flow confirming.

- **Entry:** 113.4 (At market (price already inside ±1% of POC))
- **Stop:** 102.57 (below anchored VWAP, 9.6% risk)
- **Target:** 141.18 (measured move (value-area width projected))
- **R:R:** 2.57  |  **Free-flow (+1R):** 124.23
- **Risks:**
  - (high) Extended 11% above anchored VWAP — heavy chase risk; wait for the limit level, do not buy at market.
  - (info) Stop sits 9.6% below entry (~4.2 ATR), below anchored VWAP.
  - (info) Reward/risk of 2.57 is close to the 2.5 floor — any slippage on entry meaningfully degrades the trade.
  - (medium) At 52-week highs: target is a measured-move projection with no overhead volume reference — take partial profits mechanically.

### 7. PGR — Pullback to value (score 11.7)

Progressive Corporation — pullback to value in Financials (sector rank #3), relative strength top 80% of candidates, flow neutral.

- **Entry:** 212.74 (Limit at high-volume node (212.74))
- **Stop:** 207.7 (below anchored VWAP (widened to 1 ATR), 2.4% risk)
- **Target:** 237.26 (52-week high)
- **R:R:** 4.87  |  **Free-flow (+1R):** 217.78
- **Risks:**
  - (info) No flow confirmation yet (daily close-vs-open volume proxy is flat).
  - (info) Stop sits 2.4% below entry (~1.0 ATR), below anchored VWAP (widened to 1 ATR).

### 8. WRB — Acceptance breakout above value (score 7.8)

W. R. Berkley Corporation — acceptance breakout above value in Financials (sector rank #3), relative strength top 89% of candidates, flow confirming.

- **Entry:** 71.75 (Buy-stop on retest of VAH (71.39 + 0.5%))
- **Stop:** 70.0 (below anchored VWAP (widened to 1 ATR), 2.4% risk)
- **Target:** 76.44 (52-week high)
- **R:R:** 2.68  |  **Free-flow (+1R):** 73.5
- **Risks:**
  - (info) Stop sits 2.4% below entry (~1.0 ATR), below anchored VWAP (widened to 1 ATR).
  - (info) Reward/risk of 2.68 is close to the 2.5 floor — any slippage on entry meaningfully degrades the trade.

### 9. VRSN — Pullback to value (score 1.7)

Verisign — pullback to value in Information Technology (sector rank #1), relative strength top 98% of candidates, flow confirming.

- **Entry:** 294.56 (At market (price at high-volume node))
- **Stop:** 262.59 (below anchored VWAP, 10.9% risk)
- **Target:** 375.45 (measured move (value-area width projected))
- **R:R:** 2.53  |  **Free-flow (+1R):** 326.53
- **Risks:**
  - (high) Extended 12% above anchored VWAP — heavy chase risk; wait for the limit level, do not buy at market.
  - (info) Stop sits 10.9% below entry (~2.8 ATR), below anchored VWAP.
  - (info) Reward/risk of 2.53 is close to the 2.5 floor — any slippage on entry meaningfully degrades the trade.

### 10. NVDA — Acceptance breakout above value (score 0.9)

Nvidia — acceptance breakout above value in Information Technology (sector rank #1), relative strength top 99% of candidates, flow confirming.

- **Entry:** 209.88 (Buy-stop on retest of VAH (208.83 + 0.5%))
- **Stop:** 202.05 (below anchored VWAP (widened to 1 ATR), 3.7% risk)
- **Target:** 235.47 (52-week high)
- **R:R:** 3.27  |  **Free-flow (+1R):** 217.71
- **Risks:**
  - (medium) Trading 9% above anchored VWAP — mildly extended; prefer limit fills over market entries.
  - (info) Stop sits 3.7% below entry (~1.0 ATR), below anchored VWAP (widened to 1 ATR).
  - (info) Entry limit sits 6.3% below current price — the order may never fill; do not chase if it runs away.

## ④ Appendix

**Watch — no valid trade yet:**

- CB (Financials, score 90.0): pullback to value but R:R 1.55 below 2.5 floor
- L (Financials, score 87.2): pullback to value but R:R 1.13 below 2.5 floor
- CINF (Financials, score 84.9): pullback to value but R:R 2.36 below 2.5 floor
- CSCO (Information Technology, score 80.0): acceptance breakout but R:R 0.79 below 2.5 floor
- CPAY (Financials, score 80.0): acceptance breakout but R:R 1.27 below 2.5 floor
- ABBV (Health Care, score 80.0): pullback to value but R:R 1.31 below 2.5 floor
- GL (Financials, score 80.0): pullback to value but R:R 1.84 below 2.5 floor
- VRTX (Health Care, score 80.0): pullback to value but R:R 1.19 below 2.5 floor
- SOLV (Health Care, score 80.0): acceptance breakout but R:R 0.86 below 2.5 floor
- BEN (Financials, score 80.0): acceptance breakout but R:R 1.36 below 2.5 floor
- BRK-B (Financials, score 80.0): acceptance breakout but R:R 1.32 below 2.5 floor
- TDY (Information Technology, score 80.0): acceptance breakout but R:R 1.69 below 2.5 floor
- AAPL (Information Technology, score 80.0): pullback to value but R:R 1.51 below 2.5 floor
- HIG (Financials, score 80.0): acceptance breakout but R:R 1.63 below 2.5 floor
- MSI (Information Technology, score 80.0): pullback to value but R:R 0.56 below 2.5 floor
- EG (Financials, score 80.0): pullback to value but R:R 0.86 below 2.5 floor
- SYF (Financials, score 80.0): acceptance breakout but R:R 2.12 below 2.5 floor
- LLY (Health Care, score 77.4): acceptance breakout but R:R 1.73 below 2.5 floor
- CVS (Health Care, score 69.0): pullback to value but R:R 1.67 below 2.5 floor
- BNY (Financials, score 60.0): pullback to value but R:R 1.58 below 2.5 floor
- MTB (Financials, score 60.0): pullback to value but R:R 1.48 below 2.5 floor
- NTRS (Financials, score 60.0): pullback to value but R:R 0.47 below 2.5 floor
- FITB (Financials, score 60.0): pullback to value but R:R 0.38 below 2.5 floor
- MS (Financials, score 60.0): pullback to value but R:R 0.86 below 2.5 floor
- GS (Financials, score 60.0): pullback to value but R:R 1.33 below 2.5 floor
- UNH (Health Care, score 60.0): pullback to value but R:R 0.6 below 2.5 floor
- WST (Health Care, score 60.0): pullback to value but R:R 1.67 below 2.5 floor
- TFC (Financials, score 60.0): pullback to value but R:R 1.14 below 2.5 floor
- ELV (Health Care, score 60.0): pullback to value but R:R 1.35 below 2.5 floor
- USB (Financials, score 59.6): pullback to value but R:R 1.22 below 2.5 floor
- HBAN (Financials, score 58.8): pullback to value but R:R 2.36 below 2.5 floor
- WFC (Financials, score 40.9): pullback to value but R:R 2.04 below 2.5 floor
- BAX (Health Care, score 40.0): breakout extended (32 sessions above VAH)
- FTNT (Information Technology, score 40.0): pullback to value but R:R 1.71 below 2.5 floor
- HPQ (Information Technology, score 40.0): breakout extended (14 sessions above VAH)
- DXCM (Health Care, score 40.0): no qualifying structure yet
- IQV (Health Care, score 40.0): breakout extended (32 sessions above VAH)
- TRV (Financials, score 40.0): breakout extended (33 sessions above VAH)
- AMGN (Health Care, score 40.0): breakout extended (12 sessions above VAH)
- ALL (Financials, score 40.0): breakout extended (33 sessions above VAH)
- DGX (Health Care, score 40.0): breakout extended (13 sessions above VAH)
- STT (Financials, score 40.0): pullback to value but R:R 2.43 below 2.5 floor
- AIZ (Financials, score 40.0): breakout extended (40 sessions above VAH)
- LH (Health Care, score 40.0): breakout extended (13 sessions above VAH)
- PRU (Financials, score 40.0): breakout extended (41 sessions above VAH)
- INCY (Health Care, score 40.0): breakout extended (32 sessions above VAH)
- GPN (Financials, score 40.0): breakout extended (21 sessions above VAH)
- A (Health Care, score 40.0): no qualifying structure yet
- AMP (Financials, score 40.0): breakout extended (27 sessions above VAH)
- SCHW (Financials, score 40.0): breakout extended (26 sessions above VAH)
- COHR (Information Technology, score 40.0): pullback to value but R:R 0.9 below 2.5 floor
- JNJ (Health Care, score 40.0): breakout extended (30 sessions above VAH)
- BMY (Health Care, score 40.0): breakout extended (17 sessions above VAH)
- PNC (Financials, score 40.0): pullback to value but R:R 1.99 below 2.5 floor
- WAT (Health Care, score 40.0): no qualifying structure yet
- RJF (Financials, score 40.0): breakout extended (26 sessions above VAH)
- MRK (Health Care, score 40.0): pullback to value but R:R 1.24 below 2.5 floor
- AON (Financials, score 40.0): breakout extended (27 sessions above VAH)
- V (Financials, score 40.0): breakout extended (30 sessions above VAH)
- XYZ (Financials, score 40.0): no qualifying structure yet
- AFL (Financials, score 40.0): breakout extended (26 sessions above VAH)
- BAC (Financials, score 39.7): breakout extended (40 sessions above VAH)
- TROW (Financials, score 39.5): breakout extended (30 sessions above VAH)
- GEN (Information Technology, score 38.9): breakout extended (11 sessions above VAH)
- MET (Financials, score 38.7): breakout extended (27 sessions above VAH)
- HUM (Health Care, score 20.0): breakout extended (45 sessions above VAH)
- CNC (Health Care, score 20.0): closes above VAH but flow not confirming
- FFIV (Information Technology, score 20.0): no qualifying structure yet
- ASML (Information Technology, score 20.0): no qualifying structure yet
- CFG (Financials, score 20.0): breakout extended (21 sessions above VAH)
- RF (Financials, score 20.0): closes above VAH but flow not confirming
- EW (Health Care, score 20.0): closes above VAH but flow not confirming
- DELL (Information Technology, score 0.0): no qualifying structure yet
- PANW (Information Technology, score 0.0): breakout extended (40 sessions above VAH)
- HPE (Information Technology, score 0.0): closes above VAH but flow not confirming
- CRWD (Information Technology, score 0.0): breakout extended (31 sessions above VAH)
- NTAP (Information Technology, score 0.0): breakout extended (14 sessions above VAH)
- CRL (Health Care, score 0.0): breakout extended (32 sessions above VAH)
- HSIC (Health Care, score 0.0): breakout extended (22 sessions above VAH)
- APH (Information Technology, score 0.0): closes above VAH but flow not confirming
- IVZ (Financials, score 0.0): no qualifying structure yet
- JPM (Financials, score 0.0): breakout extended (27 sessions above VAH)
- ETN (AI Infrastructure, score 0.0): closes above VAH but flow not confirming
- BIIB (Health Care, score 0.0): no qualifying structure yet

**Near-misses (failed exactly one screen filter):**

- ALAB (Information Technology): failed “near 52w high”
- MRVL (Information Technology): failed “near 52w high”
- MU (Information Technology): failed “near 52w high”
- WTW (Financials): failed “50DMA > 200DMA”
- ARM (Information Technology): failed “near 52w high”
- AMAT (Information Technology): failed “near 52w high”
- FDS (Financials): failed “near 52w high”
- TMO (Health Care): failed “50DMA > 200DMA”
- CDW (Information Technology): failed “near 52w high”
- DDOG (Information Technology): failed “near 52w high”
- AJG (Financials): failed “near 52w high”
- MRNA (Health Care): failed “near 52w high”
- COO (Health Care): failed “50DMA > 200DMA”
- MSFT (Information Technology): failed “50DMA > 200DMA”
- AMD (Information Technology): failed “near 52w high”
- FSLR (Information Technology): failed “near 52w high”
- BDX (Health Care): failed “50DMA > 200DMA”
- ZBH (Health Care): failed “50DMA > 200DMA”
- MRSH (Financials): failed “50DMA > 200DMA”
- MCK (Health Care): failed “50DMA > 200DMA”
- COF (Financials): failed “50DMA > 200DMA”
- MA (Financials): failed “50DMA > 200DMA”
- KLAC (Information Technology): failed “near 52w high”
- STE (Health Care): failed “50DMA > 200DMA”
- REGN (Health Care): failed “50DMA > 200DMA”
- SWKS (Information Technology): failed “near 52w high”
- LRCX (Information Technology): failed “near 52w high”
- MTD (Health Care): failed “50DMA > 200DMA”
- AXP (Financials): failed “50DMA > 200DMA”
- TER (Information Technology): failed “near 52w high”
- BLK (Financials): failed “50DMA > 200DMA”
- NDAQ (Financials): failed “50DMA > 200DMA”
- STX (Information Technology): failed “near 52w high”
- KEY (Financials): failed “63d return beats SPY”
- C (Financials): failed “63d return beats SPY”
- IBKR (Financials): failed “63d return beats SPY”
- MCO (Financials): failed “63d return beats SPY”
- HUBB (AI Infrastructure): failed “63d return beats SPY”
- ACGL (Financials): failed “63d return beats SPY”
- AVGO (Information Technology): failed “63d return beats SPY”
- AIG (Financials): failed “63d return beats SPY”
- ALGN (Health Care): failed “63d return beats SPY”
- TXN (Information Technology): failed “63d return beats SPY”
- DLR (AI Infrastructure): failed “63d return beats SPY”
- CI (Health Care): failed “63d return beats SPY”
- EQIX (AI Infrastructure): failed “63d return beats SPY”
- JBL (Information Technology): failed “63d return beats SPY”
- IRM (AI Infrastructure): failed “63d return beats SPY”
- KEYS (Information Technology): failed “63d return beats SPY”
- ADI (Information Technology): failed “63d return beats SPY”
- VTRS (Health Care): failed “63d return beats SPY”
- PWR (AI Infrastructure): failed “63d return beats SPY”

---
*Generated by Ideas Engine. Research tool — not investment advice.*