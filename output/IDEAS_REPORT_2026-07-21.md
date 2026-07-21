# IDEAS REPORT — 2026-07-21

## ① Regime: RISK_ON_TRENDING

SPY in confirmed uptrend and 2/3 macro checks risk-on — full idea generation.

| Signal | Reading | Rule | Verdict |
|---|---|---|---|
| Credit stress (HY OAS) | 2.69% | < 21d MA (2.73) and < p75 of 252d (2.95) | PASS |
| Yield curve (10y-2y) | +0.39% (positive, steepening) | informational only in v1 | — |
| Volatility (VIX) | 18.6 | < 22 and < 50d MA (17.3) | FAIL |
| Financial conditions (NFCI) | -0.54 | < 0.0 (loose) | PASS |
| SPY trend | 748 vs 200DMA 694 | Close > 200DMA, 50DMA > 200DMA, 200DMA slope up over 21d | PASS |
| SPY range check | 63d range 7.7% | ranging if < 8% and no MA alignment | — |

## ② Sector rotation

| ETF | Sector | 21d rel | 63d rel | RS-ratio | RS-mom | Quadrant | Selected |
|---|---|---|---|---|---|---|---|
| XBI | Biotech (breadth 78%) | +9.55% | +6.23% | 109.2 | +6.75% | Leading | #1 |
| XLV | Health Care (breadth 78%) | +7.28% | +3.07% | 99.6 | +8.30% | Improving | #2 |
| XLE | Energy (breadth 62%) | +9.15% | +0.92% | 98.6 | +7.24% | Improving | #3 |
| SMH | Semiconductors | -11.71% | +20.02% | 112.7 | -17.35% | Weakening |  |
| XLF | Financials | +4.86% | +1.09% | 101.8 | +6.25% | Leading |  |
| XLK | Information Technology | -5.70% | +11.21% | 107.4 | -8.04% | Weakening |  |
| IGV | Software | +3.02% | +0.73% | 98.8 | +7.28% | Improving |  |
| XLRE | Real Estate | +3.73% | -3.73% | 99.3 | +3.31% | Improving |  |
| XLP | Consumer Staples | +1.41% | -3.12% | 94.7 | +1.54% | Improving |  |
| XLI | Industrials | -1.21% | -2.87% | 97.9 | -2.01% | Lagging |  |
| XLU | Utilities | +0.67% | -7.16% | 94.0 | +0.87% | Improving |  |
| XLC | Communication Services | +0.94% | -12.63% | 91.3 | +3.36% | Improving |  |
| XLY | Consumer Discretionary | -2.05% | -9.92% | 93.3 | +0.11% | Improving |  |
| XLB | Materials | -3.00% | -9.43% | 93.2 | -3.12% | Lagging |  |
| AI_INFRA | AI Infrastructure (breadth 33%) | -4.47% | +0.60% | 104.1 | -8.28% | Weakening | #4 |

## ③ Ranked ideas (2)

### 1. VRTX — Pullback to value (score 17.0)

Vertex Pharmaceuticals — pullback to value in Health Care (sector rank #1), relative strength top 74% of candidates, flow neutral.

- **Entry:** 474.18 (Limit at high-volume node (474.18))
- **Stop:** 458.51 (below anchored VWAP (widened to 1 ATR), 3.3% risk)
- **Target:** 529.59 (52-week high)
- **R:R:** 3.54  |  **Free-flow (+1R):** 489.85
- **Risks:**
  - (info) No flow confirmation yet (daily close-vs-open volume proxy is flat).
  - (info) Stop sits 3.3% below entry (~1.0 ATR), below anchored VWAP (widened to 1 ATR).

### 2. GEV — Pullback to value (score 7.7)

GE Vernova — pullback to value in AI Infrastructure (sector rank #4), relative strength top 84% of candidates, flow neutral.

- **Entry:** 1078.6 (At market (price already inside ±1% of POC))
- **Stop:** 941.07 (below anchored VWAP, 12.8% risk)
- **Target:** 1482.67 (measured move (value-area width projected))
- **R:R:** 2.94  |  **Free-flow (+1R):** 1216.13
- **Risks:**
  - (high) Extended 15% above anchored VWAP — heavy chase risk; wait for the limit level, do not buy at market.
  - (info) No flow confirmation yet (daily close-vs-open volume proxy is flat).
  - (medium) Narrow sector leadership: only 33% of sector members are above their 50DMA — the sector move rests on few names.
  - (medium) Wide structural stop (12.8% below entry) — halve position size so dollar risk stays constant.
  - (info) Reward/risk of 2.94 is close to the 2.5 floor — any slippage on entry meaningfully degrades the trade.
  - (medium) AI-infrastructure basket is Weakening vs SPY — the theme tailwind is fading; this idea rests on stock-specific strength.
- **OODA (AI-infrastructure theme):**
  - *Observe:*
    - Profitable today: trailing 12m EPS 34.21, net margin 24%
    - Real demand: quarterly revenue growing +16% YoY
    - Earnings growing +1816% YoY (forward estimates unavailable)
    - Price structure: pullback to value, flow neutral, +14.6% vs anchored VWAP.
    - Order-book data is not in free feeds — forward-vs-trailing EPS is the proxy.
  - *Orient:*
    - AI-infrastructure basket is Weakening vs SPY (RS-ratio 104.1, momentum -8.3%), included by config policy 'always'.
    - Regime RISK_ON_TRENDING: SPY in confirmed uptrend and 2/3 macro checks risk-on — full idea generation.
    - Theme breadth: 33% of basket members above their 50DMA.
  - *Decide:*
    - Earnings-backed: PASS — kept in the ranked list. Use the AI-infra filter above the ideas grid to exclude (or isolate) theme names if you judge the theme crowded.
  - *Act:*
    - Execute per the plan below — entry, structural stop, target, free-flow at +1R, and regime invalidation.

## ④ Appendix

**Watch — no valid trade yet:**

- MPC (Energy, score 80.0): acceptance breakout but R:R 1.39 below 2.5 floor
- PSX (Energy, score 80.0): acceptance breakout but R:R 1.35 below 2.5 floor
- CAH (Health Care, score 63.7): pullback to value but R:R 2.17 below 2.5 floor
- HUM (Health Care, score 60.0): pullback to value but R:R 1.0 below 2.5 floor
- RVTY (Health Care, score 60.0): pullback to value but R:R 0.59 below 2.5 floor
- WAT (Health Care, score 60.0): pullback to value but R:R 0.82 below 2.5 floor
- LLY (Health Care, score 59.8): pullback to value but R:R 1.42 below 2.5 floor
- DELL (AI Infrastructure, score 40.0): no qualifying structure yet
- DVA (Health Care, score 40.0): pullback to value but R:R 1.12 below 2.5 floor
- CVS (Health Care, score 40.0): breakout extended (32 sessions above VAH)
- VLO (Energy, score 40.0): breakout extended (14 sessions above VAH)
- CSCO (AI Infrastructure, score 40.0): no qualifying structure yet
- ELV (Health Care, score 40.0): pullback to value but R:R 1.05 below 2.5 floor
- INCY (Health Care, score 40.0): breakout extended (19 sessions above VAH)
- HSIC (Health Care, score 40.0): breakout extended (19 sessions above VAH)
- FANG (Energy, score 39.1): no qualifying structure yet
- WST (Health Care, score 20.0): breakout extended (33 sessions above VAH)
- ABBV (Health Care, score 20.0): no qualifying structure yet
- BIIB (Health Care, score 20.0): no qualifying structure yet
- JNJ (Health Care, score 20.0): breakout extended (17 sessions above VAH)
- MRK (Health Care, score 20.0): closes above VAH but flow not confirming
- CNC (Health Care, score 0.0): breakout extended (38 sessions above VAH)
- UNH (Health Care, score 0.0): breakout extended (32 sessions above VAH)
- TRGP (Energy, score 0.0): breakout extended (11 sessions above VAH)
- VTRS (Health Care, score 0.0): no qualifying structure yet
- CRL (Health Care, score 0.0): breakout extended (20 sessions above VAH)
- SOLV (Health Care, score 0.0): no qualifying structure yet
- EOG (Energy, score 0.0): no qualifying structure yet
- OKE (Energy, score 0.0): closes above VAH but flow not confirming

**Near-misses (failed exactly one screen filter):**

- TECH (Health Care): failed “50DMA > 200DMA”
- BAX (Health Care): failed “near 52w high”
- DXCM (Health Care): failed “near 52w high”
- MRNA (Health Care): failed “near 52w high”
- DGX (Health Care): failed “63d return beats SPY”
- AMGN (Health Care): failed “63d return beats SPY”
- IRM (AI Infrastructure): failed “63d return beats SPY”
- CVX (Energy): failed “63d return beats SPY”
- ANET (AI Infrastructure): failed “63d return beats SPY”
- WMB (Energy): failed “63d return beats SPY”
- LH (Health Care): failed “63d return beats SPY”
- BMY (Health Care): failed “63d return beats SPY”
- OXY (Energy): failed “63d return beats SPY”
- CI (Health Care): failed “63d return beats SPY”
- EW (Health Care): failed “63d return beats SPY”
- XOM (Energy): failed “63d return beats SPY”
- KMI (Energy): failed “63d return beats SPY”
- COP (Energy): failed “63d return beats SPY”
- ETN (AI Infrastructure): failed “63d return beats SPY”
- DVN (Energy): failed “63d return beats SPY”
- EQIX (AI Infrastructure): failed “63d return beats SPY”
- ALGN (Health Care): failed “63d return beats SPY”
- HUBB (AI Infrastructure): failed “63d return beats SPY”
- DLR (AI Infrastructure): failed “63d return beats SPY”

---
*Generated by Ideas Engine. Research tool — not investment advice.*