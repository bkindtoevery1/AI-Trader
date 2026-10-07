# V142: Matched Giveback Stop-Risk Target Ablation

Declared October 7, 2026, after the complete V141 result and before any V142
market fit, prediction or replay. This is outcome-informed development on reused
dates, not independent validation. It does not authorize an operational model
change or override the Windows restart restriction.

## Reason And Counterevidence

V141 reduced cash MSE relative to V140r1 HGB but still lost to a training-only
cash mean and lost money in every executed scenario. Changing contract ceilings,
thresholds or reported success rules cannot establish the missing conditional
edge. A narrower unresolved question is whether its cash-coordinate objective
overemphasizes high-stop-dollar observations when event risk varies.

Risk-unit regression is NOT new to this project. V84 used a cost-inclusive
reserve and failed all eight candidates. V88-V93 used own-product initial-stop
risk, with weak forecast and stressed account results. V94 directly compared
dollar and R targets with query-risk inversion; all32 account scenarios failed
Evaluation. V126 cash Ridge and V141's normalized-penalty version also failed.
These results reduce the plausibility of a rescue. This experiment isolates a
single coordinate change on the later giveback target, eighteen inputs and
lambda-one recipe; it does not erase those failures or claim a new model family.

## Frozen Change

For each original event let `s` be the positive integer stop distance from its
21 completed NQ minutes, known at decision. For a single own-product contract:

`D_cents = s * (500 for NQ, 50 for MNQ)`

`training_R[mode] = original_giveback_unit_net_cents[mode] / D_cents`

`predicted_net_cents[mode] = query_D_cents * predicted_R[mode]`

The same positive denominator applies to all four modes. It is NOT the
cost-inclusive reserve `500*s+4700` or `50*s+650`, not a guaranteed loss cap,
and not account headroom, proposed quantity, delayed-entry geometry, future
realized MAE or peak profit. Costs already present in the cash label are not
subtracted again. Gap losses below minus-one R and positive/negative forecasts
remain unrounded and unclipped. No product conversion uses an NQ outcome as an
MNQ outcome. Query inversion precedes the existing cents-to-dollars conversion.

Keep V141's eighteen input floats, support rows, date weights and fixed SVD
multioutput Ridge with effective lambda1. Fit X and R weighted StandardScalers
only on each mature prefix; alpha remains the sum of mean-one native weights.
Six pipelines mean six joint four-response Ridge fits and twelve scaler fits.
There is no hyperparameter, denominator, threshold, seed or feature search.

This is not merely numerical conditioning: fitting `cash/D` changes the
cash-coordinate prediction function to `D*f(X)` and relative squared-error
weighting toward smaller denominators. Positive inversion cannot itself change
the signs used by nomination. Constant-D predictions should match V141 cash
Ridge within numerical tolerance, an independently testable limiting case.

## Comparators And Chronology

Retain all181 development dates, the mature45/87/129-date prefixes, ten-session
purges and three42-session score blocks. All48 sealed holdout dates remain
closed. Neither denominator nor scaler is estimated from scoring outcomes.
Full-window label maturity, zero geometry-skip labels, actual product support
and all original event identities remain unchanged.

The primary fitted comparator is the exact saved V141 candidate, never refit.
Two forecast controls are the training-only cash mean and training-only R mean
inverted with query D. Report date-equal cash MSE for all three contrasts, all
products/modes/folds, as well as R-space diagnostics. A better R-space error
cannot substitute for cash or account results. No mean-policy account replay.

Publish all252 candidate product/date forecast sets before opening scoring
diagnostics or account outcomes. Reuse authenticated V140 labels; do not extract
new labels or turn an observed date into a new independent holdout. Replay four
candidate account books under the unchanged V136/V141 route and compare exact
saved V141 books. NQ Evaluation, MNQ PA, all-four-positive nomination, integer
caps, long/short directions, giveback, stops, execution costs/delay, cooldown,
account guards, withdrawals and modeled lifecycle rules remain unchanged.

Primary success remains the full baseline-and-stress Evaluation-to-PA route.
PA contrasts stay null if a book never reached PA. Official current account
cohort compliance and program fees are not established by this experiment.
All results must be reported, including fewer trades, right-censoring or loss.
No outcome-conditioned rescue, automatic retry, inversion or live promotion.

Plan nine comparisons: two product candidates, six fixed forecast contrasts
(each product versus saved V141, cash mean and R mean), and one whole-account
route contrast. None is reserved at declaration; total remains13,284. Qualified
execution would charge13,293 before the first fit, not after viewing results.

## Implementation Qualification

First verify constant-D equivalence, independent weighted normal equations,
own-product cent/R inversion, training-only scaling, original date weights,
empty queries, signs, gaps beyond one R, numeric/type rejection, input isolation,
native fit journaling and no-refit prediction on invented arrays. Separately
join stop geometry to authenticated original event anchors and exact training/
query support, without deriving risk from label or account fields.

Pure components alone do not qualify market execution. The integrated runner
must bind those exact risk vectors, saved V141 controls and untouched V140
labels, persist complete models/forecasts, restore them without refitting and
verify the complete account result. No synthetic component result is strategy
evidence and no market fit is authorized merely by this design document.
