# IDEAS REPORT — 2026-09-09

## ① Regime: RISK_ON_TRENDING

SPY in confirmed uptrend and 3/3 macro checks risk-on — full idea generation.

| Signal | Reading | Rule | Verdict |
|---|---|---|---|
| Credit stress (HY OAS) | 2.67% | < 21d MA (2.68) and < p75 of 252d (2.95) | PASS |
| Yield curve (10y-2y) | +0.40% (positive, flattening) | informational only in v1 | — |
| Volatility (VIX) | 15.7 | < 22 and < 50d MA (16.1) | PASS |
| Financial conditions (NFCI) | -0.56 | < 0.0 (loose) | PASS |
| SPY trend | 762 vs 200DMA 711 | Close > 200DMA, 50DMA > 200DMA, 200DMA slope up over 21d | PASS |
| SPY range check | 63d range 8.2% | ranging if < 8% and no MA alignment | — |

## ② Sector rotation

| ETF | Sector | 21d rel | 63d rel | RS-ratio | RS-mom | Quadrant | Selected |
|---|---|---|---|---|---|---|---|
| XLE | Energy (breadth 90%) | +9.90% | +10.92% | 106.9 | +9.51% | Leading | #1 |
| XBI | Biotech (breadth 60%) | +2.23% | +17.73% | 107.0 | -0.15% | Weakening |  |
| XLF | Financials (breadth 43%) | +0.08% | +5.44% | 101.9 | +0.10% | Leading | #2 |
| XLV | Health Care (breadth 60%) | +0.27% | +4.54% | 102.7 | +0.69% | Leading | #3 |
| IGV | Software | -1.65% | +5.87% | 106.0 | -3.48% | Weakening |  |
| XLK | Information Technology | +2.21% | +0.35% | 105.2 | -0.42% | Weakening |  |
| XLC | Communication Services | +0.48% | -4.03% | 94.0 | +3.17% | Improving |  |
| XLB | Materials | -1.99% | -2.11% | 95.9 | -0.24% | Lagging |  |
| SMH | Semiconductors | +2.23% | -6.53% | 102.7 | -1.01% | Weakening |  |
| XLU | Utilities | +0.93% | -5.45% | 91.2 | +3.87% | Improving |  |
| XLP | Consumer Staples | -0.86% | -4.27% | 94.7 | +1.47% | Improving |  |
| XLRE | Real Estate | -0.85% | -6.33% | 94.7 | +0.41% | Improving |  |
| XLY | Consumer Discretionary | -4.65% | -6.46% | 92.9 | -2.90% | Lagging |  |
| XLI | Industrials | -5.56% | -5.63% | 93.7 | -4.23% | Lagging |  |
| AI_INFRA | AI Infrastructure (breadth 47%) | +1.76% | +0.34% | 100.2 | +0.65% | Leading | #4 |

## ③ Ranked ideas (4)

### 1. TECH — Pullback to value (score 29.1)

Bio-Techne — pullback to value in Health Care (sector rank #3), relative strength top 9% of candidates, flow diverging.

- **Entry:** 71.1 (Limit at high-volume node (71.10))
- **Stop:** 66.66 (below anchored VWAP, 6.3% risk)
- **Target:** 91.46 (measured move (value-area width projected))
- **R:R:** 4.58  |  **Free-flow (+1R):** 75.55
- **Risks:**
  - (medium) Trading 8% above anchored VWAP — mildly extended; prefer limit fills over market entries.
  - (high) Volume-flow divergence: price made new highs that the flow line did not confirm — demand may be thinning.
  - (info) Stop sits 6.3% below entry (~27.8 ATR), below anchored VWAP.
  - (medium) At 52-week highs: target is a measured-move projection with no overhead volume reference — take partial profits mechanically.

### 2. PGR — Pullback to value (score 17.3)

Progressive Corporation — pullback to value in Financials (sector rank #2), relative strength top 74% of candidates, flow neutral.

- **Entry:** 215.5 (At market (price at high-volume node))
- **Stop:** 211.45 (below anchored VWAP (widened to 1 ATR), 1.9% risk)
- **Target:** 234.48 (52-week high)
- **R:R:** 4.69  |  **Free-flow (+1R):** 219.55
- **Risks:**
  - (info) No flow confirmation yet (daily close-vs-open volume proxy is flat).
  - (info) Stop sits 1.9% below entry (~1.0 ATR), below anchored VWAP (widened to 1 ATR).

### 3. NDAQ — Pullback to value (score 13.4)

Nasdaq, Inc. — pullback to value in Financials (sector rank #2), relative strength top 72% of candidates, flow diverging.

- **Entry:** 94.22 (At market (price at high-volume node))
- **Stop:** 92.21 (below anchored VWAP (widened to 1 ATR), 2.1% risk)
- **Target:** 100.3 (52-week high)
- **R:R:** 3.03  |  **Free-flow (+1R):** 96.23
- **Risks:**
  - (high) Volume-flow divergence: price made new highs that the flow line did not confirm — demand may be thinning.
  - (info) Stop sits 2.1% below entry (~1.0 ATR), below anchored VWAP (widened to 1 ATR).

### 4. SYF — Pullback to value (score 12.3)

Synchrony Financial — pullback to value in Financials (sector rank #2), relative strength top 77% of candidates, flow neutral.

- **Entry:** 77.35 (At market (price at high-volume node))
- **Stop:** 73.35 (below anchored VWAP, 5.2% risk)
- **Target:** 87.38 (52-week high)
- **R:R:** 2.51  |  **Free-flow (+1R):** 81.35
- **Risks:**
  - (medium) Trading 5% above anchored VWAP — mildly extended; prefer limit fills over market entries.
  - (info) No flow confirmation yet (daily close-vs-open volume proxy is flat).
  - (info) Stop sits 5.2% below entry (~1.9 ATR), below anchored VWAP.
  - (info) Reward/risk of 2.51 is close to the 2.5 floor — any slippage on entry meaningfully degrades the trade.

## ④ Appendix

**Watch — no valid trade yet:**

- WMB (Energy, score 90.1): pullback to value but R:R 1.68 below 2.5 floor
- EG (Financials, score 80.9): pullback to value but R:R 1.15 below 2.5 floor
- BMY (Health Care, score 80.3): pullback to value but R:R 1.22 below 2.5 floor
- STT (Financials, score 80.0): pullback to value but R:R 1.78 below 2.5 floor
- XYZ (Financials, score 80.0): pullback to value but R:R 2.3 below 2.5 floor
- DGX (Health Care, score 80.0): pullback to value but R:R 0.49 below 2.5 floor
- MCK (Health Care, score 80.0): pullback to value but R:R 1.57 below 2.5 floor
- CAH (Health Care, score 80.0): pullback to value but R:R 0.86 below 2.5 floor
- AIZ (Financials, score 80.0): pullback to value but R:R 0.82 below 2.5 floor
- HUM (Health Care, score 80.0): acceptance breakout but R:R 2.18 below 2.5 floor
- WAT (Health Care, score 80.0): pullback to value but R:R 1.94 below 2.5 floor
- WRB (Financials, score 79.9): pullback to value but R:R 1.63 below 2.5 floor
- GL (Financials, score 70.3): pullback to value but R:R 1.38 below 2.5 floor
- BRK-B (Financials, score 67.2): pullback to value but R:R 1.45 below 2.5 floor
- BLK (Financials, score 65.5): pullback to value but R:R 1.81 below 2.5 floor
- IBKR (Financials, score 62.0): pullback to value but R:R 1.14 below 2.5 floor
- PNC (Financials, score 60.8): pullback to value but R:R 0.78 below 2.5 floor
- GPN (Financials, score 60.0): pullback to value but R:R 1.19 below 2.5 floor
- MRK (Health Care, score 60.0): pullback to value but R:R 0.26 below 2.5 floor
- AMP (Financials, score 60.0): pullback to value but R:R 0.28 below 2.5 floor
- TRV (Financials, score 60.0): pullback to value but R:R 0.87 below 2.5 floor
- INCY (Health Care, score 60.0): pullback to value but R:R 1.53 below 2.5 floor
- RJF (Financials, score 60.0): pullback to value but R:R 1.7 below 2.5 floor
- MA (Financials, score 60.0): pullback to value but R:R 1.01 below 2.5 floor
- JPM (Financials, score 60.0): pullback to value but R:R 0.3 below 2.5 floor
- CPAY (Financials, score 60.0): pullback to value but R:R 0.34 below 2.5 floor
- V (Financials, score 60.0): pullback to value but R:R 0.6 below 2.5 floor
- ABBV (Health Care, score 60.0): pullback to value but R:R 1.61 below 2.5 floor
- DVN (Energy, score 60.0): pullback to value but R:R 0.69 below 2.5 floor
- NTRS (Financials, score 60.0): pullback to value but R:R 0.39 below 2.5 floor
- BEN (Financials, score 60.0): pullback to value but R:R 0.53 below 2.5 floor
- CFG (Financials, score 60.0): pullback to value but R:R 1.05 below 2.5 floor
- RF (Financials, score 60.0): pullback to value but R:R 1.38 below 2.5 floor
- BAC (Financials, score 59.8): pullback to value but R:R 0.46 below 2.5 floor
- MTB (Financials, score 59.0): pullback to value but R:R 0.97 below 2.5 floor
- FANG (Energy, score 58.5): pullback to value but R:R 0.96 below 2.5 floor
- USB (Financials, score 56.9): pullback to value but R:R 0.48 below 2.5 floor
- HIG (Financials, score 56.6): pullback to value but R:R 2.22 below 2.5 floor
- MCO (Financials, score 46.3): no qualifying structure yet
- VEEV (Health Care, score 40.0): breakout extended (32 sessions above VAH)
- MPC (Energy, score 40.0): breakout extended (22 sessions above VAH)
- VLO (Energy, score 40.0): breakout extended (45 sessions above VAH)
- DELL (AI Infrastructure, score 40.0): no qualifying structure yet
- IQV (Health Care, score 40.0): breakout extended (32 sessions above VAH)
- REGN (Health Care, score 40.0): no qualifying structure yet
- APA (Energy, score 40.0): breakout extended (22 sessions above VAH)
- TMO (Health Care, score 40.0): breakout extended (34 sessions above VAH)
- RVTY (Health Care, score 40.0): no qualifying structure yet
- ALL (Financials, score 40.0): pullback to value but R:R 0.62 below 2.5 floor
- VRTX (Health Care, score 40.0): breakout extended (23 sessions above VAH)
- GILD (Health Care, score 40.0): breakout extended (19 sessions above VAH)
- IVZ (Financials, score 40.0): breakout extended (29 sessions above VAH)
- CVX (Energy, score 40.0): breakout extended (17 sessions above VAH)
- AMGN (Health Care, score 40.0): breakout extended (34 sessions above VAH)
- JNJ (Health Care, score 40.0): breakout extended (23 sessions above VAH)
- MET (Financials, score 40.0): pullback to value but R:R 0.44 below 2.5 floor
- PFE (Health Care, score 40.0): breakout extended (16 sessions above VAH)
- WFC (Financials, score 40.0): no qualifying structure yet
- HSIC (Health Care, score 40.0): pullback to value but R:R 2.09 below 2.5 floor
- SOLV (Health Care, score 40.0): no qualifying structure yet
- PFG (Financials, score 40.0): pullback to value but R:R 0.66 below 2.5 floor
- BIIB (Health Care, score 39.0): no qualifying structure yet
- CRL (Health Care, score 20.0): breakout extended (26 sessions above VAH)
- ANET (AI Infrastructure, score 20.0): no qualifying structure yet
- BAX (Health Care, score 20.0): breakout extended (33 sessions above VAH)
- WTW (Financials, score 20.0): no qualifying structure yet
- SCHW (Financials, score 20.0): breakout extended (35 sessions above VAH)
- LH (Health Care, score 20.0): breakout extended (34 sessions above VAH)
- BDX (Health Care, score 20.0): breakout extended (31 sessions above VAH)
- PRU (Financials, score 20.0): breakout extended (39 sessions above VAH)
- XOM (Energy, score 20.0): no qualifying structure yet
- TRGP (Energy, score 20.0): breakout extended (18 sessions above VAH)
- OXY (Energy, score 20.0): no qualifying structure yet
- EOG (Energy, score 20.0): breakout extended (22 sessions above VAH)
- MRSH (Financials, score 20.0): below anchored VWAP
- A (Health Care, score 20.0): no qualifying structure yet
- DXCM (Health Care, score 18.4): breakout extended (28 sessions above VAH)
- ZBH (Health Care, score 3.6): no qualifying structure yet
- PSX (Energy, score 0.0): breakout extended (39 sessions above VAH)
- COP (Energy, score 0.0): breakout extended (18 sessions above VAH)
- BNY (Financials, score 0.0): no qualifying structure yet
- OKE (Energy, score 0.0): breakout extended (21 sessions above VAH)
- CB (Financials, score 0.0): below anchored VWAP
- CINF (Financials, score 0.0): below anchored VWAP

**Near-misses (failed exactly one screen filter):**

- MRNA (Health Care): failed “near 52w high”
- HOOD (Financials): failed “near 52w high”
- PYPL (Financials): failed “near 52w high”
- COR (Health Care): failed “50DMA > 200DMA”
- COF (Financials): failed “near 52w high”
- FDS (Financials): failed “near 52w high”
- MDT (Health Care): failed “50DMA > 200DMA”
- AJG (Financials): failed “near 52w high”
- MTD (Health Care): failed “close > 200DMA”
- ICE (Financials): failed “50DMA > 200DMA”
- BX (Financials): failed “near 52w high”
- ACGL (Financials): failed “close > 200DMA”
- ARES (Financials): failed “near 52w high”
- ETN (AI Infrastructure): failed “63d return beats SPY”
- FITB (Financials): failed “63d return beats SPY”
- MS (Financials): failed “63d return beats SPY”
- TROW (Financials): failed “63d return beats SPY”
- DLR (AI Infrastructure): failed “63d return beats SPY”
- C (Financials): failed “63d return beats SPY”
- SLB (Energy): failed “63d return beats SPY”
- VTRS (Health Care): failed “63d return beats SPY”
- TFC (Financials): failed “63d return beats SPY”
- KMI (Energy): failed “63d return beats SPY”
- WST (Health Care): failed “63d return beats SPY”
- BKR (Energy): failed “63d return beats SPY”
- GS (Financials): failed “63d return beats SPY”
- AFL (Financials): failed “63d return beats SPY”
- KEY (Financials): failed “63d return beats SPY”
- APO (Financials): failed “63d return beats SPY”
- EQIX (AI Infrastructure): failed “63d return beats SPY”
- CVS (Health Care): failed “63d return beats SPY”
- EW (Health Care): failed “63d return beats SPY”
- LLY (Health Care): failed “63d return beats SPY”
- CNC (Health Care): failed “63d return beats SPY”
- UNH (Health Care): failed “63d return beats SPY”
- CI (Health Care): failed “63d return beats SPY”
- ELV (Health Care): failed “63d return beats SPY”
- IRM (AI Infrastructure): failed “63d return beats SPY”

---
*Generated by Ideas Engine. Research tool — not investment advice.*