# IDEAS REPORT — 2026-08-07

## ① Regime: RISK_ON_TRENDING

SPY in confirmed uptrend and 2/3 macro checks risk-on — full idea generation.

| Signal | Reading | Rule | Verdict |
|---|---|---|---|
| Credit stress (HY OAS) | 2.75% | < 21d MA (2.75) and < p75 of 252d (2.95) | FAIL |
| Yield curve (10y-2y) | +0.44% (positive, steepening) | informational only in v1 | — |
| Volatility (VIX) | 15.8 | < 22 and < 50d MA (17.3) | PASS |
| Financial conditions (NFCI) | -0.53 | < 0.0 (loose) | PASS |
| SPY trend | 769 vs 200DMA 700 | Close > 200DMA, 50DMA > 200DMA, 200DMA slope up over 21d | PASS |
| SPY range check | 63d range 7.8% | ranging if < 8% and no MA alignment | — |

## ② Sector rotation

| ETF | Sector | 21d rel | 63d rel | RS-ratio | RS-mom | Quadrant | Selected |
|---|---|---|---|---|---|---|---|
| IGV | Software (breadth 54%) | +4.40% | +8.23% | 104.8 | +6.68% | Leading | #1 |
| XLF | Financials (breadth 89%) | +2.06% | +6.90% | 102.3 | +2.58% | Leading | #2 |
| XLV | Health Care | -1.78% | +8.60% | 100.1 | -0.98% | Weakening |  |
| XLK | Information Technology (breadth 54%) | -0.94% | +4.13% | 106.0 | -2.97% | Weakening |  |
| XLE | Energy | +1.50% | -2.23% | 94.9 | -0.14% | Lagging |  |
| XBI | Biotech | -8.30% | +7.32% | 105.6 | -9.73% | Weakening |  |
| XLI | Industrials | -0.70% | -0.28% | 98.4 | -0.92% | Lagging |  |
| XLB | Materials (breadth 73%) | +0.90% | -5.09% | 94.7 | +1.53% | Improving | #3 |
| XLP | Consumer Staples | -2.25% | -3.27% | 93.8 | -1.56% | Lagging |  |
| XLRE | Real Estate | -1.61% | -3.97% | 95.7 | -1.93% | Lagging |  |
| XLY | Consumer Discretionary | -0.68% | -6.28% | 94.8 | +1.74% | Improving |  |
| SMH | Semiconductors (breadth 54%) | -6.74% | -1.05% | 105.2 | -10.49% | Weakening |  |
| XLC | Communication Services | -1.54% | -10.01% | 90.9 | +0.84% | Improving |  |
| XLU | Utilities | -7.47% | -9.49% | 88.7 | -6.90% | Lagging |  |
| AI_INFRA | AI Infrastructure (breadth 47%) | -4.50% | -5.04% | 100.4 | -7.83% | Weakening | #4 |

## ③ Ranked ideas (5)

### 1. ZBRA — Acceptance breakout above value (score 73.4)

Zebra Technologies — acceptance breakout above value in Information Technology (sector rank #1), relative strength top 8% of candidates, flow confirming.

- **Entry:** 271.46 (Buy-stop on retest of VAH (270.11 + 0.5%))
- **Stop:** 250.83 (below anchored VWAP, 7.6% risk)
- **Target:** 368.99 (52-week high)
- **R:R:** 4.73  |  **Free-flow (+1R):** 292.09
- **Risks:**
  - (high) Extended 45% above anchored VWAP — heavy chase risk; wait for the limit level, do not buy at market.
  - (info) Stop sits 7.6% below entry (~1.3 ATR), below anchored VWAP.
  - (medium) At 52-week highs: target is a measured-move projection with no overhead volume reference — take partial profits mechanically.
  - (info) Entry limit sits 25.5% below current price — the order may never fill; do not chase if it runs away.

### 2. ANET — Acceptance breakout above value (score 69.0)

Arista Networks — acceptance breakout above value in Information Technology (sector rank #1), relative strength top 14% of candidates, flow confirming.

- **Entry:** 167.98 (Buy-stop on retest of VAH (167.14 + 0.5%))
- **Stop:** 157.37 (below anchored VWAP (widened to 1 ATR), 6.3% risk)
- **Target:** 197.31 (52-week high)
- **R:R:** 2.76  |  **Free-flow (+1R):** 178.59
- **Risks:**
  - (high) Extended 20% above anchored VWAP — heavy chase risk; wait for the limit level, do not buy at market.
  - (info) Stop sits 6.3% below entry (~1.0 ATR), below anchored VWAP (widened to 1 ATR).
  - (info) Reward/risk of 2.76 is close to the 2.5 floor — any slippage on entry meaningfully degrades the trade.
  - (info) Entry limit sits 12.7% below current price — the order may never fill; do not chase if it runs away.
  - (medium) AI-infrastructure basket is Weakening vs SPY — the theme tailwind is fading; this idea rests on stock-specific strength.
- **OODA (AI-infrastructure theme):**
  - *Observe:*
    - Profitable today: trailing 12m EPS 3.16, net margin 38%
    - Real demand: quarterly revenue growing +38% YoY
    - Order-book proxy: forward EPS 5.11 above trailing 3.16 — analysts see the pipeline growing
    - Price structure: acceptance breakout above value, flow confirming, +19.7% vs anchored VWAP.
    - Order-book data is not in free feeds — forward-vs-trailing EPS is the proxy.
  - *Orient:*
    - AI-infrastructure basket is Weakening vs SPY (RS-ratio 100.4, momentum -7.8%), included by config policy 'always'.
    - Regime RISK_ON_TRENDING: SPY in confirmed uptrend and 2/3 macro checks risk-on — full idea generation.
    - Theme breadth: 54% of basket members above their 50DMA.
  - *Decide:*
    - Earnings-backed: PASS — kept in the ranked list. Use the AI-infra filter above the ideas grid to exclude (or isolate) theme names if you judge the theme crowded.
  - *Act:*
    - Execute per the plan below — entry, structural stop, target, free-flow at +1R, and regime invalidation.

### 3. WRB — Pullback to value (score 20.7)

W. R. Berkley Corporation — pullback to value in Financials (sector rank #2), relative strength top 74% of candidates, flow confirming.

- **Entry:** 71.24 (Limit at high-volume node (71.24))
- **Stop:** 69.51 (below anchored VWAP (widened to 1 ATR), 2.4% risk)
- **Target:** 76.44 (52-week high)
- **R:R:** 3.0  |  **Free-flow (+1R):** 72.97
- **Risks:**
  - (info) Stop sits 2.4% below entry (~1.0 ATR), below anchored VWAP (widened to 1 ATR).

### 4. PGR — Pullback to value (score 14.2)

Progressive Corporation — pullback to value in Financials (sector rank #2), relative strength top 78% of candidates, flow neutral.

- **Entry:** 212.74 (Limit at high-volume node (212.74))
- **Stop:** 207.48 (below anchored VWAP (widened to 1 ATR), 2.5% risk)
- **Target:** 237.26 (52-week high)
- **R:R:** 4.66  |  **Free-flow (+1R):** 218.0
- **Risks:**
  - (info) No flow confirmation yet (daily close-vs-open volume proxy is flat).
  - (info) Stop sits 2.5% below entry (~1.0 ATR), below anchored VWAP (widened to 1 ATR).

### 5. NVDA — Acceptance breakout above value (score 3.3)

Nvidia — acceptance breakout above value in Information Technology (sector rank #1), relative strength top 96% of candidates, flow confirming.

- **Entry:** 209.88 (Buy-stop on retest of VAH (208.83 + 0.5%))
- **Stop:** 202.09 (below anchored VWAP (widened to 1 ATR), 3.7% risk)
- **Target:** 235.47 (52-week high)
- **R:R:** 3.28  |  **Free-flow (+1R):** 217.67
- **Risks:**
  - (medium) Trading 7% above anchored VWAP — mildly extended; prefer limit fills over market entries.
  - (info) Stop sits 3.7% below entry (~1.0 ATR), below anchored VWAP (widened to 1 ATR).
  - (info) Entry limit sits 4.2% below current price — the order may never fill; do not chase if it runs away.

## ④ Appendix

**Watch — no valid trade yet:**

- L (Financials, score 85.4): pullback to value but R:R 0.87 below 2.5 floor
- BALL (Materials, score 82.6): pullback to value but R:R 1.13 below 2.5 floor
- CSCO (Information Technology, score 80.0): acceptance breakout but R:R 0.78 below 2.5 floor
- CPAY (Financials, score 80.0): acceptance breakout but R:R 1.29 below 2.5 floor
- GL (Financials, score 80.0): acceptance breakout but R:R 1.41 below 2.5 floor
- AMCR (Materials, score 80.0): acceptance breakout but R:R 2.13 below 2.5 floor
- FCX (Materials, score 80.0): acceptance breakout but R:R 1.05 below 2.5 floor
- CINF (Financials, score 80.0): pullback to value but R:R 1.5 below 2.5 floor
- BRK-B (Financials, score 80.0): acceptance breakout but R:R 1.3 below 2.5 floor
- BEN (Financials, score 80.0): acceptance breakout but R:R 0.55 below 2.5 floor
- HIG (Financials, score 80.0): acceptance breakout but R:R 1.6 below 2.5 floor
- AAPL (Information Technology, score 80.0): pullback to value but R:R 1.64 below 2.5 floor
- ECL (Materials, score 80.0): acceptance breakout but R:R 1.57 below 2.5 floor
- TDY (Information Technology, score 80.0): acceptance breakout but R:R 1.66 below 2.5 floor
- VRSN (Information Technology, score 80.0): pullback to value but R:R 0.58 below 2.5 floor
- EG (Financials, score 80.0): pullback to value but R:R 1.03 below 2.5 floor
- HBAN (Financials, score 61.2): pullback to value but R:R 2.12 below 2.5 floor
- BNY (Financials, score 60.0): pullback to value but R:R 1.48 below 2.5 floor
- MTB (Financials, score 60.0): pullback to value but R:R 1.44 below 2.5 floor
- NTRS (Financials, score 60.0): pullback to value but R:R 0.36 below 2.5 floor
- FITB (Financials, score 60.0): pullback to value but R:R 0.41 below 2.5 floor
- MS (Financials, score 60.0): pullback to value but R:R 0.73 below 2.5 floor
- CFG (Financials, score 60.0): pullback to value but R:R 0.45 below 2.5 floor
- GS (Financials, score 60.0): pullback to value but R:R 1.32 below 2.5 floor
- C (Financials, score 60.0): pullback to value but R:R 2.14 below 2.5 floor
- USB (Financials, score 59.5): pullback to value but R:R 1.13 below 2.5 floor
- CB (Financials, score 45.5): breakout extended (16 sessions above VAH)
- FTNT (Information Technology, score 40.0): pullback to value but R:R 1.64 below 2.5 floor
- HPQ (Information Technology, score 40.0): breakout extended (13 sessions above VAH)
- TRV (Financials, score 40.0): breakout extended (32 sessions above VAH)
- ALL (Financials, score 40.0): breakout extended (32 sessions above VAH)
- MET (Financials, score 40.0): breakout extended (26 sessions above VAH)
- GPN (Financials, score 40.0): breakout extended (20 sessions above VAH)
- AIZ (Financials, score 40.0): breakout extended (39 sessions above VAH)
- PRU (Financials, score 40.0): breakout extended (16 sessions above VAH)
- STT (Financials, score 40.0): pullback to value but R:R 2.44 below 2.5 floor
- AMP (Financials, score 40.0): breakout extended (26 sessions above VAH)
- AON (Financials, score 40.0): breakout extended (26 sessions above VAH)
- SCHW (Financials, score 40.0): breakout extended (25 sessions above VAH)
- V (Financials, score 40.0): breakout extended (29 sessions above VAH)
- PNC (Financials, score 40.0): pullback to value but R:R 1.98 below 2.5 floor
- JPM (Financials, score 40.0): breakout extended (26 sessions above VAH)
- SW (Materials, score 40.0): no qualifying structure yet
- RJF (Financials, score 40.0): breakout extended (25 sessions above VAH)
- AFL (Financials, score 40.0): breakout extended (25 sessions above VAH)
- PKG (Materials, score 40.0): breakout extended (11 sessions above VAH)
- XYZ (Financials, score 40.0): no qualifying structure yet
- MSI (Information Technology, score 40.0): no qualifying structure yet
- WFC (Financials, score 40.0): pullback to value but R:R 1.78 below 2.5 floor
- STLD (Materials, score 40.0): breakout extended (11 sessions above VAH)
- PPG (Materials, score 39.7): pullback to value but R:R 2.38 below 2.5 floor
- BAC (Financials, score 39.6): breakout extended (39 sessions above VAH)
- TROW (Financials, score 39.4): breakout extended (29 sessions above VAH)
- PFG (Financials, score 38.8): no qualifying structure yet
- NUE (Materials, score 37.7): no qualifying structure yet
- ASML (Information Technology, score 23.6): no qualifying structure yet
- MCO (Financials, score 22.8): breakout extended (26 sessions above VAH)
- FFIV (Information Technology, score 20.0): no qualifying structure yet
- RF (Financials, score 20.0): closes above VAH but flow not confirming
- PANW (Information Technology, score 0.0): breakout extended (39 sessions above VAH)
- DELL (Information Technology, score 0.0): no qualifying structure yet
- CRWD (Information Technology, score 0.0): breakout extended (30 sessions above VAH)
- HPE (Information Technology, score 0.0): closes above VAH but flow not confirming
- NTAP (Information Technology, score 0.0): breakout extended (13 sessions above VAH)
- GEN (Information Technology, score 0.0): closes above VAH but flow not confirming
- APH (Information Technology, score 0.0): closes above VAH but flow not confirming
- IVZ (Financials, score 0.0): closes above VAH but flow not confirming
- ETN (AI Infrastructure, score 0.0): closes above VAH but flow not confirming

**Near-misses (failed exactly one screen filter):**

- DDOG (Information Technology): failed “near 52w high”
- ALAB (Information Technology): failed “near 52w high”
- WTW (Financials): failed “50DMA > 200DMA”
- MU (Information Technology): failed “near 52w high”
- CDW (Information Technology): failed “near 52w high”
- FDS (Financials): failed “near 52w high”
- AJG (Financials): failed “near 52w high”
- AMAT (Information Technology): failed “near 52w high”
- MRVL (Information Technology): failed “near 52w high”
- MSFT (Information Technology): failed “50DMA > 200DMA”
- ARM (Information Technology): failed “near 52w high”
- MRSH (Financials): failed “50DMA > 200DMA”
- MA (Financials): failed “50DMA > 200DMA”
- AMD (Information Technology): failed “near 52w high”
- COF (Financials): failed “50DMA > 200DMA”
- SHW (Materials): failed “50DMA > 200DMA”
- FSLR (Information Technology): failed “near 52w high”
- STX (Information Technology): failed “near 52w high”
- AXP (Financials): failed “50DMA > 200DMA”
- NDAQ (Financials): failed “50DMA > 200DMA”
- KLAC (Information Technology): failed “near 52w high”
- BLK (Financials): failed “50DMA > 200DMA”
- SYF (Financials): failed “50DMA > 200DMA”
- AVY (Materials): failed “50DMA > 200DMA”
- ACGL (Financials): failed “63d return beats SPY”
- TFC (Financials): failed “63d return beats SPY”
- AIG (Financials): failed “63d return beats SPY”
- KEY (Financials): failed “63d return beats SPY”
- IFF (Materials): failed “63d return beats SPY”
- HUBB (AI Infrastructure): failed “63d return beats SPY”
- APD (Materials): failed “63d return beats SPY”
- AVGO (Information Technology): failed “63d return beats SPY”
- IBKR (Financials): failed “63d return beats SPY”
- LIN (Materials): failed “63d return beats SPY”
- CF (Materials): failed “63d return beats SPY”
- EQIX (AI Infrastructure): failed “63d return beats SPY”
- DLR (AI Infrastructure): failed “63d return beats SPY”
- DD (Materials): failed “63d return beats SPY”
- IRM (AI Infrastructure): failed “63d return beats SPY”
- JBL (Information Technology): failed “63d return beats SPY”
- KEYS (Information Technology): failed “63d return beats SPY”
- GEV (AI Infrastructure): failed “63d return beats SPY”
- PWR (AI Infrastructure): failed “63d return beats SPY”

---
*Generated by Ideas Engine. Research tool — not investment advice.*