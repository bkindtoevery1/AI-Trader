# V109 PA-Guard-Aligned MNQ Learning

Status: target/learner implementation. No market fit, trial claim, replay,
performance result or operational promotion has occurred.

## Hypothesis

The V107 phase route uses original V102 MNQ forecasts in PA, but the original
labels are guard-free unit-trade outcomes. Actual PA entry additionally rejects
otherwise positive-net brackets with stop_ticks > 5*target_ticks. V105 kept
guard-free labels after an NQ support mask, and V106 applied a log transform to
those same NQ labels. Neither aligns MNQ targets to this fixed execution guard.

One new MNQ learner will estimate the payoff of the state-independent guarded
opportunity. For each original MNQ training row and mode, preserve the original
initial-Evaluation-exposure net-dollar target unless the actual original entry
geometry would fail the fixed nominal PA guard. For that rejection use zero:
no hypothetical position, commission or PnL would have been admitted. Existing
geometry-zero labels remain zero. A rejected loss also becomes zero; this is not
a positive-payoff clipping treatment. Do not change the guard threshold.

Validate every source row and all four mode journals before transformation,
including initially infeasible rows. Reconstruct geometry from the completed
anchor and original first-entry tick metadata. Labels must resolve strictly
before the original outer purge start. Future geometry is a TARGET input only:
it must never enter features, training membership, scoring nomination, ranking,
hyperparameter choice or a predictor-time shortcut. Preserve original feasible
population rows, nine causal features, per-date weights and dollar units.

The target is not current-PA account PnL. It ignores current capacity, sequential
busy/cooldown, drawdown and terminal state. Those remain the account replay's
job; target conformance alone cannot establish PA profitability or survival.

## Fixed Comparison

Use exact completed V107 phase-micro accounts as control. Both arms keep its
NQ Evaluation, MNQ PA, stop<=140 nomination support and actual 5:1 guard. V108's
1486 cutoff is NOT applied: its single incremental saved nomination did not
justify a support-only economic replay. V109 tests a different, explicitly
learned target while keeping the existing execution support unchanged.

Reuse each original MNQ V102 fold's already causally selected HGB setting. First
fold uses the untuned anchor; later setting snapshots must predate that fold's
purge. Do not run a new grid, retune, invert, add features or drop rejected rows.
Three folds need at most 12 estimator fits and zero new scaler fits,
with durable stage receipts after one unique preoutcome claim. Identical target
arrays require exact source-model/forecast reuse, not a redundant fit. A study
with all identical training targets should close structurally without a claim.
Reuse exact original mean/scale bytes and require the original scaled-training
matrix hash, original per-mode target hashes, weights and row dates to match
before any fit or identical-target reuse. Synthetic unchanged-target conformance
must establish that the shared fitter reproduces the original anchor export;
no extra market control refits are authorized. This implementation refinement
precedes any market fit, claim or new scored prediction.

Before fitting, the runner must authenticate source populations, original
models/settings/forecasts, dependency closure, original V107 repair outcome
lineage and calendar. Freeze the whole design and every required file. One new
policy and one primary contrast would reserve two comparisons:13177 to13179.
The implementation and training-support audit alone reserve nothing.

Replay the fixed 181 explicit NQ/MNQ raw pairs, including 55 context dates and
126 reused scored development dates. Retain four execution modes and eight
separate account state objects. Verify all four exact V107 controls, unchanged
candidate Evaluation prefixes, and original unit-journal/raw receipts. Reject
technical defects without outcome-driven retries or an integrity successor.
Publish complete results only after every date, mode and integrity check.

Primary learning benefit requires positive candidate-minus-control PA PnL in
both baseline and combined stress, no added hard/MAE breach and no earlier
inactivity. Disclose absolute PA profitability separately. A modeled full route
also needs numeric Evaluation pass, observed PA survival, payout eligibility
and no hard/MAE breach in both modes. Cost-only/latency-only are diagnostics.
These historical development comparisons are not independent validation;
48 sealed holdout dates stay closed. Program fees remain unpriced and official
compliance is not certified. The fixed operational model remains unchanged.
