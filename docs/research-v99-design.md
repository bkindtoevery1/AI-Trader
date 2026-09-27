# v99 Price-Path Information Ablation

This is a pre-execution design, not a fitted or validated result. The current
user account is Apex Legacy 50K Tradovate Evaluation, not the superseded 25K
goal text. Keep NQ at most one and MNQ at most six actual contracts, in separate
product accounts. No orders, operational promotion or Windows deployment.

## Hypothesis And Contrast

v98 increased feasible activity without improving account economics. Test
whether recent signed price-path persistence adds useful information to the
unchanged v97 threshold estimator. The idea was recorded before v97 outcomes in
`docs/research-execution-vs-forecast-review.md`; choosing it now nevertheless
remains outcome-informed development, not independent confirmation.

Append exactly one feature to the existing nine: with zero-based completed
minute closes in integer ticks, compute
`signal * (close[20] - close[15]) / sum(abs(close[i] - close[i-1]), i=16..20)`.
Use native Python integer arithmetic, convert the rational ratio once to
float64, and return positive `0.0` for a zero denominator. Reject booleans,
malformed anchors and incomplete minutes; do not clip, add epsilon or subtract
floating prices. Authenticate the original NQ anchor for both product models
before filtering infeasible quantities. Future ticks and MNQ closes do not
enter this feature.

Keep the first nine raw and scaled coordinates bitwise equal to the original
v94/v97 references. Reuse the authenticated nine-entry training-only scaler;
append the bounded tenth coordinate unscaled. Use a genuine ten-dimensional
native HGB model, exported trees and restored predictor, including split index
9. No monkeypatching or rewriting frozen models. The same fixed tree budget
does not imply unchanged flexibility after adding a feature.

## Bounded Training And Execution

Use the exact 181 admitted explicit-contract pairs from 2025-09-08 through
2026-06-12: 55 warmup dates and 126 scored dates in three 42-date folds. Preserve
the ten full-calendar-session purge, chronological expanding training prefixes,
all-mode label maturity and date weights. Validate the complete training prefix
before affordability filtering. Reuse the exact authenticated v97 labels and
v94 scaler/target references, not scoring labels in training. During replay,
recompute every original label and raw/window receipt and require exact equality.

Fit six product/fold bundles, four single-output HGB heads each, 64 trees each:
24 estimator fits, 24 learned heads, 1,536 trees. No new scaler, control fit,
hyperparameter search, seed search, horizon search or genetic algorithm. All
v97 estimator parameters remain unchanged, including seed 20260997, depth two,
maximum four leaves, minimum 100 rows per leaf, L2 ten and minimum five training
dates per leaf. Unsupported leaves abort the attempt; do not prune or retry.

Restore all 252 exact v97 threshold forecast rows before fitting. Score eight
candidate account paths and eight same-product control paths across baseline,
cost-only, latency-only and combined stress. Selection must precede the entry
tape. Preserve execution costs, risk limits, variable integer sizing, 300-second
cooldown and the existing absolute exit. No shared v98 product router or daily
fill-count cap. Require eight control accounts to reproduce exactly.

## Interpretation

For each product separately, primary absolute economic development viability
requires baseline AND combined-stress first-attempt numeric Evaluation success
and no hard breach or MAE violation. Assess PA survival and hypothetical payout
separately; do not make an Evaluation-only success a complete route success.
Program fees remain unpriced and numeric success does not prove real eligibility.

Separately report candidate-minus-own-v97 whole-calendar net-cent differences,
phase totals, selections, activity and concentration. Improvement in both
primary modes is descriptive evidence for incremental feature value, not a
randomized causal estimate. Do not mix NQ baseline with MNQ stress or select a
better mode after observation. No mandatory MSE, Sharpe or p-value superiority;
forecast errors are diagnostics, not profitability requirements. Repeatedly
observed development dates cannot establish independent validation. The 48
sealed dates from 2026-06-29 through 2026-09-02 remain closed.

## Evidence And Accounting

Freeze policy, source closure and implementation dependencies before execution.
Authenticate closed v97 and v98 separately. Claim once before any new fit, then
publish durable fit-stage receipts with actual completion acknowledgments. A
technical abort is not a performance failure; a claim still consumes its charge.
Do not restart a claimed attempt or expose partial candidate results.

There are two new selectable product policies and two matched comparisons:
four bookkeeping charges, taking 13,134 to 13,138 only on actual claim. This
ledger count does not estimate independent statistical trials. No reservation,
fit, evaluation pass or completed replay is implied by this design document.
Synthetic tests prove software behavior only. Run affected integration and full
regression before freeze; record code hashes and actual scope, not a case-count
target. Completion requires actual fitting, execution, source/control checks,
terminal result authentication and an independent result audit.
