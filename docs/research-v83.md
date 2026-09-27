# v83: Causal Initial Stops

## Authority And Status

The user's active account is Legacy50K Tradovate Evaluation. New research permits
up to six actual MNQ contracts, with unchanged conservative plan ceilings and
half-headroom, DLL and MAE risk caps. Existing frozen v63 and other deployments
are not changed. No orders, Telegram messages, purchases or account conversion.

Current status: COMPLETE at2026-09-07T05:17:13Z,
`NO_DYNAMIC_STOP_50K_DEVELOPMENT_PASS`. All outcomes were withheld until the
complete replay and source/dependency rechecks. Post-result regression:
all4123 full tests and135 focused integration tests passed. The final373-file
lock and source metadata recheck passed after testing. Additive completion
audit: `reports/nq_apex_dynamic_stop_research_v83/completion_audit.json`,
SHA256 `e1411c4d473fb9383998688b7ad259595ae8b99038ab14f1085c98e517f15961`.
All120 focused tests passed (feature47, replay36, orchestration37), and all4123
full regression tests passed before freeze.373 dependencies were locked at
2026-09-07T05:04:12Z; all32 comparisons were reserved at05:04:30Z before new
outcomes, bringing the ledger to13023. Do not restart or modify locked bytes.
The previous cycle v82 had12991 effective comparisons and no verified50K pass.
v83 brings the count to13023. The goal remains active. This is exploratory development, not
independent validation; the48-date sealed holdout remains closed.

## Matched Comparison

Reuse exact sealed v82 directions and requested quantities from both base models:
the original nested v32 and prior-session RBF kernel. Compare fixed1 and
strength1to6 quantities under two new initial-stop rules, ATR and ATR plus
volume conditioning. Eight new policies; all four fixed-stop v82 candidate
paths are exact conformance controls, not new trials. Legacy is primary and
EOD is reported separately. No direction refitting or account-type selection.

Reserve32 comparisons before new targets are read: (3 inherited v32 alpha
choices +1 kernel) times2 sizing times2 new stops times2 account families.
The cumulative count becomes13023 when execution starts. Baseline and stress
are paired execution conditions, not independently selected candidates.

## Predictors And Training

Use the previously admitted617 complete explicit-contract NQ/MNQ minute pairs,
ending2026-06-12. Minute timestamps denote interval starts. Each date uses only
75 completed minutes starting08:15 through09:29 ET. Aggregate fifteen5-minute
bars; the first supplies previous close for the following14 true ranges. ATR
is their simple mean, not Wilder's recursive smoothing, floored at0.25point.
Use the greater NQ/MNQ ATR.

Volume is the sum of completed09:00 through09:29 intervals, divided separately
by each product's median of the previous20 admitted same-explicit-maturity
session sums. Average the two log ratios. Reset history on maturity changes;
warmup uses a neutral volume modifier, without dropping dates. Append current
volume after extracting the feature. No post0930 price or volume predictors.

For each exact v82 model-specific training prefix, calibrate median ATR and
linear q10/q90 ATR bounds. On volume-ready training dates, fit StandardScaler
and Ridge(alpha100, intercept, SVD) to log(holding-window range / preentry ATR).
The range label covers baseline09:31-15:55 and is used only in training.
Fewer than40 ready observations or constant volume yields an explicit neutral
fallback. At most eight risk ridge fits; zero new direction fits.

Initial stop is ceil(387 times clipped ATR ratio times volume modifier), in
quarter-point ticks. The ATR profile uses modifier1. Volume modification is
relative to the training median log-volume reference, bounded0.5-2.0; final
ratio is bounded by the training ATR q10/median and q90/median. A fitted
negative volume coefficient can narrow the stop: high volume does not imply
automatic widening. Validation labels never tune these parameters.

Preserve the original four folds,10-session purge,63 scored dates per fold,
and30 prior-fit bridge dates.282 continuous intents cover181 available raw
replay dates. All these historical dates are already observed development.

## Execution And Evidence

Bind each initial stop before entry; never widen after entry. Keep baseline
09:31-15:55 and stress09:34-15:52 ET. Per-contract stress reserve is
50 times stop_ticks plus650 cents. Actual size is bounded by requested size,
six contracts, conservative plan ceiling and the unchanged dollar-risk budget.
Changing future initial stops can restore zero capacity on a quieter date;
it cannot change past trades, repair balance or trigger an unapproved reset.

Ordered raw ticks, source receipts and all fixed-stop control journals must
reproduce v82 exactly. Guard-free unit fills may be scaled for direct
diagnostics; account paths must execute independently with quantity-dependent
floors, costs, stops, DLL and MAE checks. Gaps remain capable of breaches.

Freeze policy, implementation, tests, dependencies, runtime and source
metadata before the one-shot run. Reserve all32 at run start. No retries or
partial result publication; publish final status, failure attribution and seal
only after complete replay and dependency rechecks. Use preregistered8-policy
block-bootstrap diagnostics and13023-trial HAC adjustment. Global DSR remains
unavailable. No automatic promotion, even if a development shortlist passes.

Focused and full regression tests are required before freezing and after
completion. Exact program fees, PA plan, planned risk/reward, signal-service
compliance and independent final validation remain unresolved.

## Complete Results

All181 raw pairs and402041614 events passed; all373 dependencies and all four
fixed-stop control direct/account journals plus source/window receipts matched.
The two sealed direction models were reused without refitting. Eight risk
ridge fits generated the eight new stop/sizing policies.

Guard-free direct PnL in USD after simulated execution costs, before account
guards and program fees. Each cell is baseline / stress; these are not actual
account cashflows, realized payouts, or independent validation.

| Model and requested size | Fixed v82 | ATR | ATR plus volume |
| --- | ---: | ---: | ---: |
| v32 fixed1 | 2732.26 / 1355.00 | 3.76 / 1838.50 | 1378.76 / 2170.50 |
| v32 strength1to6 | 464.42 / 1168.50 | -6746.08 / 613.00 | -1249.08 / 1624.50 |
| Kernel fixed1 | -2015.98 / -2005.50 | -1343.98 / -2041.50 | -1225.48 / -1968.50 |
| Kernel strength1to6 | -2100.68 / -2779.50 | 3582.32 / 1221.00 | 5975.32 / 1179.00 |

Dynamic stops ranged58.75-188.75 points across the available replay dates and
both models. The v32 ATR median was134.5 points; its volume-conditioned median
was132.0. Kernel medians were131.25 and128.75. All eight fitted volume
coefficients were negative, conditional on the selected log(range/ATR) target;
this is not evidence that high volume universally calls for a tighter stop.

The16 new Legacy baseline/stress paths all encountered risk-cap skips; the
changing initial stop enabled32 later resumptions without altering past
balances or resetting an account. Avoiding permanently zero capacity did not
establish robust success.

Only v32 fixed1 ATR baseline numerically passed Legacy Evaluation, on2026-06-05
after a2025-09-08 start. It retained one purchase and nine renewal units in the
conservative billing ledger, including the possible post-pass activation-day
renewal; exact fees and refund eligibility remain unverified. Stress did not
pass. The PA started2026-06-08 and is right-censored with only four observed
trade dates throughJune12, all losing374.54USD, total-1498.16USD, final
balance48501.84USD. Its observed no-breach flag is not meaningful long-run PA
survival, payout eligibility, or a validated route.

All eight new adaptive EOD paths numerically passed Evaluation after four
attempts, then closed PA for inactivity. No new path qualified for a payout.
The kernel adaptive volume profile's5975.32USD direct baseline gain came with
11055.02USD direct drawdown and no Legacy Evaluation pass. Do not select this
profile or switch accounts on the strength of the headline PnL.

No policy met all development gates. All global HAC Bonferroni p-values are1;
new-policy family-adjusted bootstrap p-values range0.515-0.998. Volume improved
some direct comparisons, but neither volume superiority nor practical
robustness is established. This cycle contains no intratrade trailing stop.

Parent report-only audit verified4344 direct rows,5212 new-policy account
rows,2072 actual account trades,1128 schedule-bound checks, costs, dollar-risk
caps and EOD after-close floor reconstruction. It did not re-read raw market
payloads or independently recompute statistical p-values. No independent
strategy pass is claimed. Do not retune the exposed v83 parameters or rerun
the one-shot cycle; a genuinely new hypothesis needs a separate preregistered
exploratory experiment. Frozen live runtimes and the48-date holdout stay closed.
