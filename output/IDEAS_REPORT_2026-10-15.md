# IDEAS REPORT — 2026-10-15

## ① Regime: RISK_ON_TRENDING

SPY in confirmed uptrend and 2/3 macro checks risk-on — full idea generation.

| Signal | Reading | Rule | Verdict |
|---|---|---|---|
| Credit stress (HY OAS) | 3.16% | < 21d MA (2.95) and < p75 of 252d (2.97) | FAIL |
| Yield curve (10y-2y) | +0.37% (positive, steepening) | informational only in v1 | — |
| Volatility (VIX) | 15.3 | < 22 and < 50d MA (15.5) | PASS |
| Financial conditions (NFCI) | -0.49 | < 0.0 (loose) | PASS |
| SPY trend | 778 vs 200DMA 721 | Close > 200DMA, 50DMA > 200DMA, 200DMA slope up over 21d | PASS |
| SPY range check | 63d range 7.0% | ranging if < 8% and no MA alignment | — |

## ② Sector rotation

| ETF | Sector | 21d rel | 63d rel | RS-ratio | RS-mom | Quadrant | Selected |
|---|---|---|---|---|---|---|---|
| XLE | Energy (breadth 81%) | +2.25% | +16.32% | 109.7 | +3.59% | Leading | #1 |
| IGV | Software (breadth 57%) | +1.56% | +14.81% | 110.2 | -0.77% | Weakening |  |
| XLK | Information Technology (breadth 57%) | +4.13% | +4.89% | 103.9 | +0.81% | Leading | #2 |
| XLV | Health Care | -0.98% | +4.26% | 102.9 | -0.80% | Weakening |  |
| SMH | Semiconductors (breadth 57%) | +6.10% | -3.78% | 98.6 | +2.05% | Improving | #3 |
| XLP | Consumer Staples | -2.12% | -1.80% | 97.0 | +0.30% | Improving |  |
| XLB | Materials | -3.58% | -4.42% | 93.7 | -1.01% | Lagging |  |
| XLC | Communication Services | -4.61% | -3.97% | 96.2 | -1.93% | Lagging |  |
| XLY | Consumer Discretionary | -2.72% | -7.08% | 93.4 | -0.26% | Lagging |  |
| XLU | Utilities | -1.65% | -10.06% | 92.2 | +3.02% | Improving |  |
| XLF | Financials | -6.04% | -6.06% | 96.9 | -5.04% | Lagging |  |
| XLI | Industrials | -2.98% | -9.40% | 92.3 | -0.84% | Lagging |  |
| XLRE | Real Estate | -4.68% | -8.67% | 92.2 | -2.40% | Lagging |  |
| XBI | Biotech | -9.36% | -9.36% | 95.3 | -9.90% | Lagging |  |
| AI_INFRA | AI Infrastructure (breadth 67%) | +4.76% | +0.85% | 100.3 | +3.99% | Leading | #4 |

## ③ Ranked ideas (2)

### 1. PWR — Pullback to value (score 11.4)

Quanta Services — pullback to value in AI Infrastructure (sector rank #4), relative strength top 82% of candidates, flow confirming.

- **Entry:** 688.88 (At market (price already inside ±1% of POC))
- **Stop:** 651.7 (below anchored VWAP, 5.4% risk)
- **Target:** 784.99 (52-week high)
- **R:R:** 2.58  |  **Free-flow (+1R):** 726.06
- **Risks:**
  - (medium) Trading 6% above anchored VWAP — mildly extended; prefer limit fills over market entries.
  - (info) Stop sits 5.4% below entry (~1.5 ATR), below anchored VWAP.
  - (info) Reward/risk of 2.58 is close to the 2.5 floor — any slippage on entry meaningfully degrades the trade.
- **OODA (AI-infrastructure theme):**
  - *Observe:*
    - Profitable today: trailing 12m EPS 8.73, net margin 4%
    - Real demand: quarterly revenue growing +41% YoY
    - Order-book proxy: forward EPS 19.86 above trailing 8.73 — analysts see the pipeline growing
    - Price structure: pullback to value, flow confirming, +5.7% vs anchored VWAP.
    - Order-book data is not in free feeds — forward-vs-trailing EPS is the proxy.
  - *Orient:*
    - AI-infrastructure basket is Leading vs SPY (RS-ratio 100.3, momentum +4.0%), included by config policy 'always'.
    - Regime RISK_ON_TRENDING: SPY in confirmed uptrend and 2/3 macro checks risk-on — full idea generation.
    - Theme breadth: 67% of basket members above their 50DMA.
  - *Decide:*
    - Earnings-backed: PASS — kept in the ranked list. Use the AI-infra filter above the ideas grid to exclude (or isolate) theme names if you judge the theme crowded.
  - *Act:*
    - Execute per the plan below — entry, structural stop, target, free-flow at +1R, and regime invalidation.

### 2. KMI — Acceptance breakout above value (score 8.9)

Kinder Morgan — acceptance breakout above value in Energy (sector rank #1), relative strength top 89% of candidates, flow confirming.

- **Entry:** 32.22 (Buy-stop on retest of VAH (32.06 + 0.5%))
- **Stop:** 31.55 (below anchored VWAP (widened to 1 ATR), 2.1% risk)
- **Target:** 33.99 (52-week high)
- **R:R:** 2.64  |  **Free-flow (+1R):** 32.89
- **Risks:**
  - (info) Stop sits 2.1% below entry (~1.0 ATR), below anchored VWAP (widened to 1 ATR).
  - (info) Reward/risk of 2.64 is close to the 2.5 floor — any slippage on entry meaningfully degrades the trade.
  - (medium) At 52-week highs: target is a measured-move projection with no overhead volume reference — take partial profits mechanically.
  - (info) Entry limit sits 3.6% below current price — the order may never fill; do not chase if it runs away.

## ④ Appendix

**Watch — no valid trade yet:**

- CSCO (Information Technology, score 86.5): pullback to value but R:R 2.22 below 2.5 floor
- NTAP (Information Technology, score 80.0): acceptance breakout but R:R 0.47 below 2.5 floor
- FFIV (Information Technology, score 80.0): acceptance breakout but R:R 0.54 below 2.5 floor
- DDOG (Information Technology, score 80.0): acceptance breakout but R:R 1.32 below 2.5 floor
- ADI (Information Technology, score 80.0): pullback to value but R:R 1.27 below 2.5 floor
- APH (Information Technology, score 75.5): acceptance breakout but R:R 1.88 below 2.5 floor
- FANG (Energy, score 69.6): pullback to value but R:R 1.56 below 2.5 floor
- OKE (Energy, score 62.0): pullback to value but R:R 1.03 below 2.5 floor
- HPQ (Information Technology, score 60.0): pullback to value but R:R 1.08 below 2.5 floor
- CDW (Information Technology, score 60.0): pullback to value but R:R 1.21 below 2.5 floor
- VRSN (Information Technology, score 59.9): pullback to value but R:R 0.89 below 2.5 floor
- PTC (Information Technology, score 40.0): pullback to value but R:R 0.28 below 2.5 floor
- VLO (Energy, score 40.0): breakout extended (32 sessions above VAH)
- ZBRA (Information Technology, score 40.0): breakout extended (19 sessions above VAH)
- SHOP (Information Technology, score 40.0): no qualifying structure yet
- MSFT (Information Technology, score 40.0): breakout extended (37 sessions above VAH)
- TWLO (Information Technology, score 40.0): no qualifying structure yet
- LITE (Information Technology, score 40.0): breakout extended (11 sessions above VAH)
- CRWD (Information Technology, score 40.0): breakout extended (22 sessions above VAH)
- XOM (Energy, score 40.0): no qualifying structure yet
- ANET (Information Technology, score 40.0): pullback to value but R:R 0.56 below 2.5 floor
- FTNT (Information Technology, score 40.0): no qualifying structure yet
- KEYS (Information Technology, score 40.0): breakout extended (14 sessions above VAH)
- AMD (Information Technology, score 40.0): breakout extended (17 sessions above VAH)
- NVDA (Information Technology, score 40.0): pullback to value but R:R 1.31 below 2.5 floor
- TRGP (Energy, score 40.0): pullback to value but R:R 1.82 below 2.5 floor
- AAPL (Information Technology, score 40.0): no qualifying structure yet
- MSI (Information Technology, score 22.7): no qualifying structure yet
- CRM (Information Technology, score 20.0): no qualifying structure yet
- DELL (Information Technology, score 20.0): closes above VAH but flow not confirming
- COP (Energy, score 20.0): closes above VAH but flow not confirming
- CVX (Energy, score 20.0): closes above VAH but flow not confirming
- DVN (Energy, score 20.0): no qualifying structure yet
- OXY (Energy, score 20.0): no qualifying structure yet
- EOG (Energy, score 20.0): closes above VAH but flow not confirming
- ETN (AI Infrastructure, score 13.4): no qualifying structure yet
- P (Information Technology, score 0.0): no qualifying structure yet
- MPC (Energy, score 0.0): breakout extended (11 sessions above VAH)
- PLTR (Information Technology, score 0.0): breakout extended (22 sessions above VAH)
- PSX (Energy, score 0.0): breakout extended (31 sessions above VAH)
- HPE (Information Technology, score 0.0): closes above VAH but flow not confirming
- APA (Energy, score 0.0): breakout extended (33 sessions above VAH)
- PANW (Information Technology, score 0.0): no qualifying structure yet

**Near-misses (failed exactly one screen filter):**

- IT (Information Technology): failed “near 52w high”
- SMCI (Information Technology): failed “near 52w high”
- CTSH (Information Technology): failed “near 52w high”
- SWKS (Information Technology): failed “near 52w high”
- NOW (Information Technology): failed “near 52w high”
- WDAY (Information Technology): failed “near 52w high”
- MRVL (Information Technology): failed “near 52w high”
- SNPS (Information Technology): failed “50DMA > 200DMA”
- GDDY (Information Technology): failed “near 52w high”
- TER (Information Technology): failed “near 52w high”
- TRI (Information Technology): failed “near 52w high”
- TEL (Information Technology): failed “50DMA > 200DMA”
- ROP (Information Technology): failed “near 52w high”
- MU (Information Technology): failed “near 52w high”
- NBIS (Information Technology): failed “near 52w high”
- WMB (Energy): failed “63d return beats SPY”
- EQIX (AI Infrastructure): failed “63d return beats SPY”
- TXN (Information Technology): failed “63d return beats SPY”
- GEV (AI Infrastructure): failed “63d return beats SPY”
- ASML (Information Technology): failed “63d return beats SPY”
- IRM (AI Infrastructure): failed “63d return beats SPY”

---
*Generated by Ideas Engine. Research tool — not investment advice.*