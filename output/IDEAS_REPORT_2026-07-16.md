# IDEAS REPORT — 2026-07-16

## ① Regime: RISK_ON_TRENDING

SPY in confirmed uptrend and 2/3 macro checks risk-on — full idea generation.

| Signal | Reading | Rule | Verdict |
|---|---|---|---|
| Credit stress (HY OAS) | 2.72% | < 21d MA (2.72) and < p75 of 252d (2.97) | FAIL |
| Yield curve (10y-2y) | +0.40% (positive, flattening) | informational only in v1 | — |
| Volatility (VIX) | 16.5 | < 22 and < 50d MA (17.3) | PASS |
| Financial conditions (NFCI) | -0.54 | < 0.0 (loose) | PASS |
| SPY trend | 754 vs 200DMA 693 | Close > 200DMA, 50DMA > 200DMA, 200DMA slope up over 21d | PASS |
| SPY range check | 63d range 8.8% | ranging if < 8% and no MA alignment | — |

## ② Sector rotation

| ETF | Sector | 21d rel | 63d rel | RS-ratio | RS-mom | Quadrant | Selected |
|---|---|---|---|---|---|---|---|
| XBI | Biotech (breadth 83%) | +14.87% | +6.27% | 110.0 | +12.07% | Leading | #1 |
| SMH | Semiconductors (breadth 35%) | -7.12% | +21.16% | 113.6 | -13.59% | Weakening |  |
| IGV | Software (breadth 35%) | +1.62% | +9.30% | 99.5 | +6.18% | Improving | #2 |
| XLK | Information Technology (breadth 35%) | -3.76% | +13.75% | 107.3 | -6.30% | Weakening |  |
| XLF | Financials (breadth 89%) | +4.45% | +0.72% | 101.7 | +6.01% | Leading | #3 |
| XLV | Health Care (breadth 83%) | +1.67% | -1.81% | 97.9 | +2.80% | Improving |  |
| XLI | Industrials | +0.44% | -4.83% | 97.8 | -0.50% | Lagging |  |
| XLRE | Real Estate | -2.83% | -5.37% | 97.3 | -3.13% | Lagging |  |
| XLP | Consumer Staples | -3.81% | -5.51% | 93.4 | -3.64% | Lagging |  |
| XLY | Consumer Discretionary | -1.33% | -8.13% | 94.0 | +0.81% | Improving |  |
| XLU | Utilities | +0.49% | -10.72% | 94.1 | +0.74% | Improving |  |
| XLE | Energy | -3.38% | -7.50% | 94.7 | -4.95% | Lagging |  |
| XLC | Communication Services | -0.44% | -11.65% | 92.4 | +2.02% | Improving |  |
| XLB | Materials | -4.48% | -11.10% | 93.2 | -4.82% | Lagging |  |
| AI_INFRA | AI Infrastructure (breadth 40%) | +0.16% | -1.42% | 103.4 | -3.93% | Weakening | #4 |

## ③ Ranked ideas (2)

### 1. EW — Pullback to value (score 13.9)

Edwards Lifesciences — pullback to value in Health Care (sector rank #1), relative strength top 83% of candidates, flow confirming.

- **Entry:** 86.99 (Limit at high-volume node (86.99))
- **Stop:** 83.95 (below anchored VWAP, 3.5% risk)
- **Target:** 95.18 (52-week high)
- **R:R:** 2.7  |  **Free-flow (+1R):** 90.03
- **Risks:**
  - (info) Stop sits 3.5% below entry (~1.3 ATR), below anchored VWAP.
  - (info) Reward/risk of 2.7 is close to the 2.5 floor — any slippage on entry meaningfully degrades the trade.

### 2. ANET — Pullback to value (score 3.9)

Arista Networks — pullback to value in Information Technology (sector rank #2), relative strength top 89% of candidates, flow diverging.

- **Entry:** 171.51 (At market (price at high-volume node))
- **Stop:** 157.1 (below anchored VWAP, 8.4% risk)
- **Target:** 208.71 (measured move (value-area width projected))
- **R:R:** 2.58  |  **Free-flow (+1R):** 185.93
- **Risks:**
  - (medium) Trading 9% above anchored VWAP — mildly extended; prefer limit fills over market entries.
  - (high) Volume-flow divergence: price made new highs that the flow line did not confirm — demand may be thinning.
  - (medium) Narrow sector leadership: only 35% of sector members are above their 50DMA — the sector move rests on few names.
  - (info) Stop sits 8.4% below entry (~1.3 ATR), below anchored VWAP.
  - (info) Reward/risk of 2.58 is close to the 2.5 floor — any slippage on entry meaningfully degrades the trade.
  - (medium) AI-infrastructure basket is Weakening vs SPY — the theme tailwind is fading; this idea rests on stock-specific strength.
- **OODA (AI-infrastructure theme):**
  - *Observe:*
    - Profitable today: trailing 12m EPS 2.90, net margin 38%
    - Real demand: quarterly revenue growing +35% YoY
    - Order-book proxy: forward EPS 4.46 above trailing 2.90 — analysts see the pipeline growing
    - Price structure: pullback to value, flow diverging, +9.2% vs anchored VWAP.
    - Order-book data is not in free feeds — forward-vs-trailing EPS is the proxy.
  - *Orient:*
    - AI-infrastructure basket is Weakening vs SPY (RS-ratio 103.4, momentum -3.9%), included by config policy 'always'.
    - Regime RISK_ON_TRENDING: SPY in confirmed uptrend and 2/3 macro checks risk-on — full idea generation.
    - Theme breadth: 35% of basket members above their 50DMA.
  - *Decide:*
    - Earnings-backed: PASS — kept in the ranked list. Use the AI-infra filter above the ideas grid to exclude (or isolate) theme names if you judge the theme crowded.
  - *Act:*
    - Execute per the plan below — entry, structural stop, target, free-flow at +1R, and regime invalidation.

## ④ Appendix

**Watch — no valid trade yet:**

- NTAP (Information Technology, score 80.0): acceptance breakout but R:R 0.78 below 2.5 floor
- BEN (Financials, score 80.0): pullback to value but R:R 2.23 below 2.5 floor
- AAPL (Information Technology, score 80.0): acceptance breakout but R:R 1.14 below 2.5 floor
- GL (Financials, score 80.0): pullback to value but R:R 1.03 below 2.5 floor
- PRU (Financials, score 80.0): acceptance breakout but R:R 0.78 below 2.5 floor
- MSCI (Financials, score 80.0): acceptance breakout but R:R 1.32 below 2.5 floor
- RF (Financials, score 80.0): acceptance breakout but R:R 1.17 below 2.5 floor
- WAT (Health Care, score 80.0): pullback to value but R:R 0.92 below 2.5 floor
- HBAN (Financials, score 80.0): pullback to value but R:R 0.64 below 2.5 floor
- KEY (Financials, score 80.0): acceptance breakout but R:R 0.56 below 2.5 floor
- XYZ (Financials, score 78.0): acceptance breakout but R:R 1.52 below 2.5 floor
- BIIB (Health Care, score 62.5): pullback to value but R:R 2.02 below 2.5 floor
- AMD (Information Technology, score 60.0): pullback to value but R:R 1.5 below 2.5 floor
- CDNS (Information Technology, score 60.0): pullback to value but R:R 1.0 below 2.5 floor
- ASML (Information Technology, score 60.0): pullback to value but R:R 0.75 below 2.5 floor
- SOLV (Health Care, score 60.0): pullback to value but R:R 1.4 below 2.5 floor
- ADI (Information Technology, score 58.9): pullback to value but R:R 1.8 below 2.5 floor
- TXN (Information Technology, score 58.8): pullback to value but R:R 0.89 below 2.5 floor
- DDOG (Information Technology, score 40.0): breakout extended (41 sessions above VAH)
- DELL (Information Technology, score 40.0): breakout extended (32 sessions above VAH)
- PANW (Information Technology, score 40.0): breakout extended (42 sessions above VAH)
- FTNT (Information Technology, score 40.0): breakout extended (40 sessions above VAH)
- CRWD (Information Technology, score 40.0): breakout extended (42 sessions above VAH)
- DVA (Health Care, score 40.0): breakout extended (15 sessions above VAH)
- FFIV (Information Technology, score 40.0): breakout extended (43 sessions above VAH)
- CSCO (Information Technology, score 40.0): no qualifying structure yet
- WST (Health Care, score 40.0): breakout extended (29 sessions above VAH)
- CRL (Health Care, score 40.0): breakout extended (16 sessions above VAH)
- ELV (Health Care, score 40.0): pullback to value but R:R 1.21 below 2.5 floor
- AIZ (Financials, score 40.0): breakout extended (28 sessions above VAH)
- NTRS (Financials, score 40.0): no qualifying structure yet
- VTRS (Health Care, score 40.0): no qualifying structure yet
- RVTY (Health Care, score 40.0): pullback to value but R:R 0.64 below 2.5 floor
- FITB (Financials, score 40.0): breakout extended (16 sessions above VAH)
- ABBV (Health Care, score 40.0): no qualifying structure yet
- V (Financials, score 40.0): breakout extended (13 sessions above VAH)
- PNC (Financials, score 40.0): breakout extended (16 sessions above VAH)
- CPAY (Financials, score 40.0): no qualifying structure yet
- HSIC (Health Care, score 40.0): breakout extended (15 sessions above VAH)
- MTB (Financials, score 40.0): breakout extended (16 sessions above VAH)
- ALL (Financials, score 40.0): breakout extended (16 sessions above VAH)
- TRV (Financials, score 40.0): breakout extended (16 sessions above VAH)
- HUM (Health Care, score 0.0): breakout extended (46 sessions above VAH)
- CNC (Health Care, score 0.0): breakout extended (46 sessions above VAH)
- CVS (Health Care, score 0.0): breakout extended (28 sessions above VAH)
- UNH (Health Care, score 0.0): breakout extended (46 sessions above VAH)
- STT (Financials, score 0.0): no qualifying structure yet
- GS (Financials, score 0.0): breakout extended (38 sessions above VAH)
- IBKR (Financials, score 0.0): breakout extended (26 sessions above VAH)
- LLY (Health Care, score 0.0): breakout extended (13 sessions above VAH)
- MS (Financials, score 0.0): breakout extended (38 sessions above VAH)
- TROW (Financials, score 0.0): breakout extended (28 sessions above VAH)
- BNY (Financials, score 0.0): breakout extended (37 sessions above VAH)
- IVZ (Financials, score 0.0): no qualifying structure yet
- MET (Financials, score 0.0): closes above VAH but flow not confirming
- PFG (Financials, score 0.0): no qualifying structure yet
- INCY (Health Care, score 0.0): breakout extended (15 sessions above VAH)
- BAC (Financials, score 0.0): breakout extended (25 sessions above VAH)
- USB (Financials, score 0.0): breakout extended (16 sessions above VAH)
- JPM (Financials, score 0.0): breakout extended (20 sessions above VAH)
- CI (Health Care, score 0.0): closes above VAH but flow not confirming
- CFG (Financials, score 0.0): breakout extended (17 sessions above VAH)

**Near-misses (failed exactly one screen filter):**

- ALAB (Information Technology): failed “near 52w high”
- HPE (Information Technology): failed “near 52w high”
- MU (Information Technology): failed “near 52w high”
- SNDK (Information Technology): failed “near 52w high”
- ARM (Information Technology): failed “near 52w high”
- FLEX (Information Technology): failed “near 52w high”
- INTC (Information Technology): failed “near 52w high”
- MRVL (Information Technology): failed “near 52w high”
- STX (Information Technology): failed “near 52w high”
- AMAT (Information Technology): failed “near 52w high”
- GEN (Information Technology): failed “near 52w high”
- WDC (Information Technology): failed “near 52w high”
- QCOM (Information Technology): failed “near 52w high”
- AKAM (Information Technology): failed “near 52w high”
- NXPI (Information Technology): failed “near 52w high”
- MRNA (Health Care): failed “near 52w high”
- ON (Information Technology): failed “near 52w high”
- HPQ (Information Technology): failed “near 52w high”
- BAX (Health Care): failed “near 52w high”
- KLAC (Information Technology): failed “near 52w high”
- TECH (Health Care): failed “50DMA > 200DMA”
- NBIS (Information Technology): failed “near 52w high”
- LRCX (Information Technology): failed “near 52w high”
- IQV (Health Care): failed “50DMA > 200DMA”
- DXCM (Health Care): failed “near 52w high”
- MCO (Financials): failed “50DMA > 200DMA”
- MCHP (Information Technology): failed “near 52w high”
- AMP (Financials): failed “50DMA > 200DMA”
- GPN (Financials): failed “50DMA > 200DMA”
- A (Health Care): failed “50DMA > 200DMA”
- RJF (Financials): failed “50DMA > 200DMA”
- AXP (Financials): failed “50DMA > 200DMA”
- AON (Financials): failed “50DMA > 200DMA”
- PWR (AI Infrastructure): failed “near 52w high”
- AFL (Financials): failed “63d return beats SPY”
- IRM (AI Infrastructure): failed “63d return beats SPY”
- NVDA (Information Technology): failed “63d return beats SPY”
- TFC (Financials): failed “63d return beats SPY”
- VRTX (Health Care): failed “63d return beats SPY”
- EG (Financials): failed “63d return beats SPY”
- GEV (AI Infrastructure): failed “63d return beats SPY”
- CINF (Financials): failed “63d return beats SPY”
- APH (Information Technology): failed “63d return beats SPY”
- CAH (Health Care): failed “63d return beats SPY”
- DGX (Health Care): failed “63d return beats SPY”
- JNJ (Health Care): failed “63d return beats SPY”
- C (Financials): failed “63d return beats SPY”
- MRK (Health Care): failed “63d return beats SPY”
- CB (Financials): failed “63d return beats SPY”
- AMGN (Health Care): failed “63d return beats SPY”
- ETN (AI Infrastructure): failed “63d return beats SPY”
- L (Financials): failed “63d return beats SPY”
- ACGL (Financials): failed “63d return beats SPY”
- BMY (Health Care): failed “63d return beats SPY”
- VRSN (Information Technology): failed “63d return beats SPY”
- ALGN (Health Care): failed “63d return beats SPY”
- KEYS (Information Technology): failed “63d return beats SPY”
- EQIX (AI Infrastructure): failed “63d return beats SPY”
- TDY (Information Technology): failed “63d return beats SPY”
- GILD (Health Care): failed “63d return beats SPY”
- DLR (AI Infrastructure): failed “63d return beats SPY”
- HUBB (AI Infrastructure): failed “63d return beats SPY”

---
*Generated by Ideas Engine. Research tool — not investment advice.*