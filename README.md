# Ideas Engine

A daily swing-trading ideas generator: free market data in, a ranked watchlist of long ideas
out, published as a self-contained HTML dashboard. Runs in the cloud every day (GitHub
Actions) and locally on demand (`python3 main.py`). Architecture and commands for
contributors live in [CLAUDE.md](CLAUDE.md); full design rationale in
[IDEAS_ENGINE_PLAN.md](IDEAS_ENGINE_PLAN.md).

## The regime traffic light — how the engine decides how brave to be

Before looking at any single stock, the engine reads the **whole market's weather** and picks
one of four regimes. The regime controls how many ideas are published and which setup types
are trusted. If you only learn one part of this codebase, learn this — everything downstream
obeys it.

### The six dials (and their three very different jobs)

Not all signals vote. Each has one of three roles — mistaking an *info* dial for a failed
*gate* is the #1 misreading of the signal table:

| Dial | Reading it takes | Role |
|---|---|---|
| **Credit stress** (HY OAS) | below its 21-day average and 75th percentile = calm | 🗳️ **voting gate** |
| **Volatility** (VIX) | below 22 and below its 50-day average = calm | 🗳️ **voting gate** |
| **Financial conditions** (NFCI) | below 0 = loose | 🗳️ **voting gate** |
| **SPY trend** | close > 200DMA, 50DMA > 200DMA, 200DMA rising | 🚦 **trend test** (its own axis, not one of the 3 votes) |
| **Yield curve** (10y−2y) | positive / inverted | ℹ️ **info only** — displayed, never votes. It leads recessions by 6–24 months: far too slow for a daily switch (v1 decision) |
| **SPY range check** | 63-day range < 8% *and* MAs unaligned = "ranging" | 🔀 **tiebreaker** — only chooses *which flavor* of risk-on |

So the decision really rests on two axes: **macro health** (how many of the 3 voting gates
pass) and **trend** (the SPY trend test). The other two dials annotate and route.

### The decision tree — evaluated strictly in this order

```
1. KILL-SWITCH first:            SPY below 200DMA?  OR  credit AND VIX both stressed?
      └── yes → 🔴 RISK_OFF      zero ideas published. Nothing else is even evaluated.

2. Trend confirmed AND ≥2/3 macro votes pass?
      └── yes → 🟢 RISK_ON_TRENDING    full idea list, breakouts + pullbacks

3. Market ranging (tiebreaker) AND ≥2/3 macro votes pass?
      └── yes → 🟡 RISK_ON_RANGING     ideas flow, pullback-to-value preferred
                                       (breakouts fail inside ranges)

4. Anything else (signals disagree):
      └──       🟠 TRANSITION          idea list HALVED, sizes down
```

Worked example (2026-08-31): credit 2.63% ✓, VIX 14.5 ✓, NFCI −0.57 ✓ → 3/3 votes; SPY 771
vs 200DMA 707, aligned and rising → trend confirmed; curve +0.39% (info, no vote); range
8.1% ≥ 8% → not ranging. Step 1 no, step 2 yes → **RISK_ON_TRENDING**. The curve and range
rows showing `info` are *not* failures — one abstains by design, the other voted *for*
"trending" by ruling out "ranging".

### Rules that keep this honest

- **Every threshold lives in [config.yaml](config.yaml)** — never hard-code a tunable in
  `src/`. Changing a threshold is a tuning decision, not a bug fix.
- **RISK_OFF is a report, not an outage.** The run still completes and publishes an
  evidence-only dashboard with zero ideas. Downstream consumers (the paper-arena
  competition) treat the label as a claim and independently audit the inputs behind it.
- **Guard the inputs, not just the logic.** On 2026-08-31 Yahoo served a SPY bar with NaN
  prices; the unguarded `iloc[-1]` made the trend test read `nan vs nan`, failed it, and
  flipped the regime to a false RISK_OFF for two days. The fix (`_drop_incomplete` in
  [src/data_io.py](src/data_io.py)) drops any row with a NaN price at fetch *and* cache-read
  time. Lesson for future dials: a data gap must surface as "can't evaluate", never quietly
  become a bearish vote.
- **Changing a dial's role** (e.g. promoting the yield curve to a voting gate) changes what
  every published regime means historically — do it deliberately, versioned, with the
  downstream paper-arena reviews in mind, not as a drive-by edit.

## Verifying a change

There are no tests; verification = run a layer and eyeball it:

```bash
python3 -m src.regime     # prints the signal table + regime verdict (PASS/FAIL/info)
python3 main.py           # full pipeline → output/ (network-bound, a few minutes)
```
