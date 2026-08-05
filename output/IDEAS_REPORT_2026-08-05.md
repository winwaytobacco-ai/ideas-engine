# IDEAS REPORT — 2026-08-05

## ① Regime: RISK_ON_TRENDING

SPY in confirmed uptrend and 3/3 macro checks risk-on — full idea generation.

| Signal | Reading | Rule | Verdict |
|---|---|---|---|
| Credit stress (HY OAS) | 2.73% | < 21d MA (2.75) and < p75 of 252d (2.95) | PASS |
| Yield curve (10y-2y) | +0.45% (positive, steepening) | informational only in v1 | — |
| Volatility (VIX) | 16.5 | < 22 and < 50d MA (17.3) | PASS |
| Financial conditions (NFCI) | -0.53 | < 0.0 (loose) | PASS |
| SPY trend | 770 vs 200DMA 699 | Close > 200DMA, 50DMA > 200DMA, 200DMA slope up over 21d | PASS |
| SPY range check | 63d range 7.8% | ranging if < 8% and no MA alignment | — |

## ② Sector rotation

| ETF | Sector | 21d rel | 63d rel | RS-ratio | RS-mom | Quadrant | Selected |
|---|---|---|---|---|---|---|---|
| IGV | Software (breadth 54%) | +4.67% | +8.16% | 106.7 | +7.19% | Leading | #1 |
| XLF | Financials (breadth 93%) | +0.53% | +6.19% | 102.5 | +1.14% | Leading | #2 |
| XLK | Information Technology (breadth 54%) | +0.80% | +5.75% | 106.3 | -1.29% | Weakening |  |
| XLV | Health Care | -3.12% | +6.85% | 99.7 | -2.32% | Lagging |  |
| XLI | Industrials | -0.78% | +1.72% | 99.1 | -1.04% | Lagging |  |
| XBI | Biotech | -9.58% | +7.85% | 104.5 | -11.05% | Weakening |  |
| SMH | Semiconductors (breadth 54%) | -4.97% | +2.36% | 104.9 | -8.93% | Weakening |  |
| XLB | Materials | -0.76% | -4.10% | 95.4 | -0.18% | Lagging |  |
| XLRE | Real Estate | -2.26% | -3.40% | 96.3 | -2.59% | Lagging |  |
| XLP | Consumer Staples | -2.40% | -4.42% | 93.8 | -1.82% | Lagging |  |
| XLE | Energy (breadth 38%) | +1.93% | -9.54% | 93.4 | +0.20% | Improving | #3 |
| XLY | Consumer Discretionary | -1.89% | -5.95% | 95.0 | +0.53% | Improving |  |
| XLC | Communication Services | -3.09% | -10.50% | 90.3 | -0.72% | Lagging |  |
| XLU | Utilities | -7.42% | -11.88% | 89.1 | -6.91% | Lagging |  |
| AI_INFRA | AI Infrastructure (breadth 67%) | -0.68% | -3.88% | 102.0 | -4.23% | Weakening | #4 |

## ③ Ranked ideas (5)

### 1. ZBRA — Acceptance breakout above value (score 71.4)

Zebra Technologies — acceptance breakout above value in Information Technology (sector rank #1), relative strength top 11% of candidates, flow confirming.

- **Entry:** 267.89 (Buy-stop on retest of VAH (266.56 + 0.5%))
- **Stop:** 249.81 (below anchored VWAP, 6.7% risk)
- **Target:** 368.99 (52-week high)
- **R:R:** 5.59  |  **Free-flow (+1R):** 285.97
- **Risks:**
  - (high) Extended 48% above anchored VWAP — heavy chase risk; wait for the limit level, do not buy at market.
  - (info) Stop sits 6.7% below entry (~1.1 ATR), below anchored VWAP.
  - (medium) At 52-week highs: target is a measured-move projection with no overhead volume reference — take partial profits mechanically.
  - (info) Entry limit sits 27.4% below current price — the order may never fill; do not chase if it runs away.

### 2. ANET — Acceptance breakout above value (score 38.2)

Arista Networks — acceptance breakout above value in Information Technology (sector rank #1), relative strength top 52% of candidates, flow confirming.

- **Entry:** 167.95 (Buy-stop on retest of VAH (167.12 + 0.5%))
- **Stop:** 156.88 (below anchored VWAP (widened to 1 ATR), 6.6% risk)
- **Target:** 197.31 (52-week high)
- **R:R:** 2.65  |  **Free-flow (+1R):** 179.02
- **Risks:**
  - (high) Extended 23% above anchored VWAP — heavy chase risk; wait for the limit level, do not buy at market.
  - (info) Stop sits 6.6% below entry (~1.0 ATR), below anchored VWAP (widened to 1 ATR).
  - (info) Reward/risk of 2.65 is close to the 2.5 floor — any slippage on entry meaningfully degrades the trade.
  - (medium) At 52-week highs: target is a measured-move projection with no overhead volume reference — take partial profits mechanically.
  - (info) Entry limit sits 14.9% below current price — the order may never fill; do not chase if it runs away.
  - (medium) AI-infrastructure basket is Weakening vs SPY — the theme tailwind is fading; this idea rests on stock-specific strength.
- **OODA (AI-infrastructure theme):**
  - *Observe:*
    - Profitable today: trailing 12m EPS 2.91, net margin 38%
    - Real demand: quarterly revenue growing +35% YoY
    - Order-book proxy: forward EPS 4.47 above trailing 2.91 — analysts see the pipeline growing
    - Price structure: acceptance breakout above value, flow confirming, +23.0% vs anchored VWAP.
    - Order-book data is not in free feeds — forward-vs-trailing EPS is the proxy.
  - *Orient:*
    - AI-infrastructure basket is Weakening vs SPY (RS-ratio 102.0, momentum -4.2%), included by config policy 'always'.
    - Regime RISK_ON_TRENDING: SPY in confirmed uptrend and 3/3 macro checks risk-on — full idea generation.
    - Theme breadth: 54% of basket members above their 50DMA.
  - *Decide:*
    - Earnings-backed: PASS — kept in the ranked list. Use the AI-infra filter above the ideas grid to exclude (or isolate) theme names if you judge the theme crowded.
  - *Act:*
    - Execute per the plan below — entry, structural stop, target, free-flow at +1R, and regime invalidation.

### 3. STT — Pullback to value (score 28.2)

State Street Corporation — pullback to value in Financials (sector rank #2), relative strength top 22% of candidates, flow diverging.

- **Entry:** 183.96 (Limit at high-volume node (183.96))
- **Stop:** 156.13 (below anchored VWAP, 15.1% risk)
- **Target:** 254.67 (measured move (value-area width projected))
- **R:R:** 2.54  |  **Free-flow (+1R):** 211.8
- **Risks:**
  - (high) Extended 20% above anchored VWAP — heavy chase risk; wait for the limit level, do not buy at market.
  - (high) Volume-flow divergence: price made new highs that the flow line did not confirm — demand may be thinning.
  - (medium) Wide structural stop (15.1% below entry) — halve position size so dollar risk stays constant.
  - (info) Reward/risk of 2.54 is close to the 2.5 floor — any slippage on entry meaningfully degrades the trade.
  - (medium) At 52-week highs: target is a measured-move projection with no overhead volume reference — take partial profits mechanically.

### 4. PFG — Pullback to value (score 27.7)

Principal Financial Group — pullback to value in Financials (sector rank #2), relative strength top 62% of candidates, flow confirming.

- **Entry:** 112.75 (Limit at high-volume node (112.75))
- **Stop:** 102.35 (below anchored VWAP, 9.2% risk)
- **Target:** 140.58 (measured move (value-area width projected))
- **R:R:** 2.68  |  **Free-flow (+1R):** 123.15
- **Risks:**
  - (high) Extended 12% above anchored VWAP — heavy chase risk; wait for the limit level, do not buy at market.
  - (info) Stop sits 9.2% below entry (~4.0 ATR), below anchored VWAP.
  - (info) Reward/risk of 2.68 is close to the 2.5 floor — any slippage on entry meaningfully degrades the trade.
  - (medium) At 52-week highs: target is a measured-move projection with no overhead volume reference — take partial profits mechanically.

### 5. WRB — Pullback to value (score 13.4)

W. R. Berkley Corporation — pullback to value in Financials (sector rank #2), relative strength top 83% of candidates, flow confirming.

- **Entry:** 71.24 (Limit at high-volume node (71.24))
- **Stop:** 69.46 (below anchored VWAP (widened to 1 ATR), 2.5% risk)
- **Target:** 76.44 (52-week high)
- **R:R:** 2.92  |  **Free-flow (+1R):** 73.02
- **Risks:**
  - (info) Stop sits 2.5% below entry (~1.0 ATR), below anchored VWAP (widened to 1 ATR).
  - (info) Reward/risk of 2.92 is close to the 2.5 floor — any slippage on entry meaningfully degrades the trade.

## ④ Appendix

**Watch — no valid trade yet:**

- L (Financials, score 86.7): pullback to value but R:R 0.98 below 2.5 floor
- CINF (Financials, score 82.5): pullback to value but R:R 1.91 below 2.5 floor
- BEN (Financials, score 80.0): acceptance breakout but R:R 0.55 below 2.5 floor
- AAPL (Information Technology, score 80.0): pullback to value but R:R 1.86 below 2.5 floor
- TDY (Information Technology, score 80.0): acceptance breakout but R:R 1.95 below 2.5 floor
- HIG (Financials, score 80.0): acceptance breakout but R:R 1.57 below 2.5 floor
- EG (Financials, score 80.0): pullback to value but R:R 0.83 below 2.5 floor
- BRK-B (Financials, score 79.8): acceptance breakout but R:R 1.76 below 2.5 floor
- MET (Financials, score 78.5): acceptance breakout but R:R 0.36 below 2.5 floor
- BNY (Financials, score 60.0): pullback to value but R:R 1.48 below 2.5 floor
- MTB (Financials, score 60.0): pullback to value but R:R 1.42 below 2.5 floor
- GS (Financials, score 60.0): pullback to value but R:R 1.09 below 2.5 floor
- FITB (Financials, score 60.0): pullback to value but R:R 1.56 below 2.5 floor
- NTRS (Financials, score 60.0): pullback to value but R:R 0.34 below 2.5 floor
- USB (Financials, score 59.3): pullback to value but R:R 1.06 below 2.5 floor
- HBAN (Financials, score 58.4): pullback to value but R:R 0.76 below 2.5 floor
- CB (Financials, score 46.9): breakout extended (15 sessions above VAH)
- HPQ (Information Technology, score 40.0): breakout extended (14 sessions above VAH)
- CPAY (Financials, score 40.0): no qualifying structure yet
- CSCO (Information Technology, score 40.0): no qualifying structure yet
- AIZ (Financials, score 40.0): breakout extended (39 sessions above VAH)
- TRV (Financials, score 40.0): breakout extended (31 sessions above VAH)
- GPN (Financials, score 40.0): breakout extended (19 sessions above VAH)
- ALL (Financials, score 40.0): breakout extended (32 sessions above VAH)
- PRU (Financials, score 40.0): breakout extended (15 sessions above VAH)
- AMP (Financials, score 40.0): breakout extended (25 sessions above VAH)
- XYZ (Financials, score 40.0): no qualifying structure yet
- SCHW (Financials, score 40.0): breakout extended (25 sessions above VAH)
- JPM (Financials, score 40.0): breakout extended (35 sessions above VAH)
- PNC (Financials, score 40.0): pullback to value but R:R 2.04 below 2.5 floor
- AON (Financials, score 40.0): breakout extended (25 sessions above VAH)
- V (Financials, score 40.0): breakout extended (28 sessions above VAH)
- RJF (Financials, score 40.0): breakout extended (24 sessions above VAH)
- AFL (Financials, score 40.0): breakout extended (24 sessions above VAH)
- VRSN (Information Technology, score 40.0): no qualifying structure yet
- NVDA (Information Technology, score 39.7): no qualifying structure yet
- BAC (Financials, score 39.3): breakout extended (25 sessions above VAH)
- PGR (Financials, score 36.9): closes above VAH but flow not confirming
- FFIV (Information Technology, score 20.0): no qualifying structure yet
- VLO (Energy, score 20.0): breakout extended (21 sessions above VAH)
- GL (Financials, score 20.0): closes above VAH but flow not confirming
- MS (Financials, score 20.0): no qualifying structure yet
- CFG (Financials, score 20.0): breakout extended (20 sessions above VAH)
- RF (Financials, score 20.0): closes above VAH but flow not confirming
- MPC (Energy, score 20.0): breakout extended (21 sessions above VAH)
- PSX (Energy, score 20.0): breakout extended (21 sessions above VAH)
- C (Financials, score 20.0): closes above VAH but flow not confirming
- TFC (Financials, score 20.0): no qualifying structure yet
- DELL (Information Technology, score 0.0): no qualifying structure yet
- PANW (Information Technology, score 0.0): breakout extended (38 sessions above VAH)
- DDOG (Information Technology, score 0.0): breakout extended (28 sessions above VAH)
- FTNT (Information Technology, score 0.0): breakout extended (33 sessions above VAH)
- HPE (Information Technology, score 0.0): closes above VAH but flow not confirming
- CRWD (Information Technology, score 0.0): breakout extended (38 sessions above VAH)
- NTAP (Information Technology, score 0.0): breakout extended (12 sessions above VAH)
- GEN (Information Technology, score 0.0): closes above VAH but flow not confirming
- APH (Information Technology, score 0.0): closes above VAH but flow not confirming
- IVZ (Financials, score 0.0): closes above VAH but flow not confirming
- TROW (Financials, score 0.0): breakout extended (29 sessions above VAH)
- ETN (AI Infrastructure, score 0.0): no qualifying structure yet

**Near-misses (failed exactly one screen filter):**

- ALAB (Information Technology): failed “near 52w high”
- MU (Information Technology): failed “near 52w high”
- AMD (Information Technology): failed “near 52w high”
- ARM (Information Technology): failed “near 52w high”
- WTW (Financials): failed “50DMA > 200DMA”
- AMAT (Information Technology): failed “near 52w high”
- FDS (Financials): failed “near 52w high”
- FLEX (Information Technology): failed “near 52w high”
- MRVL (Information Technology): failed “near 52w high”
- NBIS (Information Technology): failed “near 52w high”
- MSFT (Information Technology): failed “50DMA > 200DMA”
- COF (Financials): failed “50DMA > 200DMA”
- ASML (Information Technology): failed “near 52w high”
- MRSH (Financials): failed “50DMA > 200DMA”
- MA (Financials): failed “50DMA > 200DMA”
- WFC (Financials): failed “50DMA > 200DMA”
- WDC (Information Technology): failed “near 52w high”
- LRCX (Information Technology): failed “near 52w high”
- KLAC (Information Technology): failed “near 52w high”
- AXP (Financials): failed “50DMA > 200DMA”
- TER (Information Technology): failed “near 52w high”
- STX (Information Technology): failed “near 52w high”
- BLK (Financials): failed “50DMA > 200DMA”
- FSLR (Information Technology): failed “near 52w high”
- SYF (Financials): failed “50DMA > 200DMA”
- MCO (Financials): failed “50DMA > 200DMA”
- KEY (Financials): failed “63d return beats SPY”
- IBKR (Financials): failed “63d return beats SPY”
- ACGL (Financials): failed “63d return beats SPY”
- AIG (Financials): failed “63d return beats SPY”
- HUBB (AI Infrastructure): failed “63d return beats SPY”
- TRGP (Energy): failed “63d return beats SPY”
- JBL (Information Technology): failed “63d return beats SPY”
- DLR (AI Infrastructure): failed “63d return beats SPY”
- MSCI (Financials): failed “63d return beats SPY”
- XOM (Energy): failed “63d return beats SPY”
- EQIX (AI Infrastructure): failed “63d return beats SPY”
- OKE (Energy): failed “63d return beats SPY”
- AVGO (Information Technology): failed “63d return beats SPY”
- CVX (Energy): failed “63d return beats SPY”
- KMI (Energy): failed “63d return beats SPY”
- IRM (AI Infrastructure): failed “63d return beats SPY”
- EOG (Energy): failed “63d return beats SPY”
- WMB (Energy): failed “63d return beats SPY”
- KEYS (Information Technology): failed “63d return beats SPY”
- COP (Energy): failed “63d return beats SPY”
- GEV (AI Infrastructure): failed “63d return beats SPY”
- BKR (Energy): failed “63d return beats SPY”
- FANG (Energy): failed “63d return beats SPY”
- SLB (Energy): failed “63d return beats SPY”
- PWR (AI Infrastructure): failed “63d return beats SPY”

---
*Generated by Ideas Engine. Research tool — not investment advice.*