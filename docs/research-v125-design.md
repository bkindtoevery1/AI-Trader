# V125: Local Joint Outcome Distributions

Declared 2026-10-01 after completed V124 and before any V125 market fit,
forecast or replay. This is one outcome-informed development candidate, not an
independent test, account pass or replacement for operational V63/V92.

## Reason

V124 changed the shallow forest's split objective, but all 2,210 PA choices
remained flat and cost-only forecast error worsened 0.1354%. Every limiting
conditional mean was negative before its risk penalty. This does not establish
that the true conditional edge is negative, nor that model underfitting is the
cause. Do not remove an adverse mode or force trades to resolve inactivity.

Test a different conditional-distribution estimator: local training analogs
instead of averaging depth-two tree leaves. The hypothesis is that coarse
partitions can average distinct contexts together. A local estimator can also
overfit noise, especially in twelve dimensions; a favorable result would not
prove that this was the cause of V124's failure.
Scaling, distance geometry and the removal of label-directed partitions change
together; this is not an isolated causal test of smoothing alone.

This is not the first nearest-neighbor model. V75/V77 tested 63-neighbor daily
direction analogs on a different 25K task and failed their account screens.
V82/V84/V95 tested other kernel representations. The new intervention is local
joint four-mode unit-outcome mass in the existing V123/V124 PA account route.

## Fixed Estimator

Keep exactly the same twelve causal inputs, complete mature one-MNQ four-mode
integer-cent outcomes, event population and date-equal original weights as
V123/V124. Preserve all negative and zero labels. Use the original 181 dates,
45/87/129 training prefixes, ten-session purges and three 42-date scored blocks.
No label, feature, calendar, stop-support or source extraction change is proposed.

Fit one `StandardScaler` per original training prefix, with original weights
1/(training events on the date), centering and population-standard-deviation
scaling. Use all twelve coordinates, float64 throughout, native handling of
constant/near-constant columns and no clipping or query-dependent normalization.
Query features, purge dates and scoring dates cannot enter these statistics.
The locked installed sklearn 1.9.0 is the numerical authority, not the version
of online documentation. Restoration verifies original training moments without
calling an estimator fit again.

Compute Euclidean distances with sklearn's `DistanceMetric`, not a handwritten
nearest-neighbor engine. For each query choose the smallest radius containing
at least 100 original events AND at least five distinct training dates. Include
every exact computed-distance tie at that radius. Both support minima inherit
the forest's prior nonroot leaf constraints, not a search over new outcomes.
Date-support expansion is label-blind and fixed before this experiment; it is
not a retry, tuning choice or permission to select only profitable neighbors.

Within the selected neighborhood normalize the ORIGINAL training date weights;
do not re-equalize dates within the selected subset, inverse-distance weight,
drop zero-distance peers, or average the four outcome coordinates separately.
Keep joint empirical outcome vectors and retain a complete mass vector over
the original training population. Store radius, support count, distinct-date
count and effective date-mass concentration as diagnostics. Five distinct dates
are not five independent samples or a minimum effective-sample guarantee.

No alternate k, metric, scaling, seed, representation, recency window or fallback.
Numerical failures abort; missing evidence is not a zero forecast. Exact ties
may expand to the full population. There is no distance confidence threshold:
a distant analog remains an uncertain extrapolation, not evidence of support
from similar market conditions. This limitation must remain visible in results.

## Decision And Comparison

Retain V119's original positive-integer quantity choice using all four certainty
equivalents, with flat winning unless the worst CE is strictly positive. Retain
NQ Evaluation, MNQ PA, original study caps, actual account capacity, fees,
slippage/latency, stops, activity, cooldown, MAE, trailing and payout accounting.
The user's broader contract authorization is not reduced by this study's caps.

Compare one candidate against the exact completed V124 books, not refitted
controls. Propose two counted comparisons, 13,219 to 13,221, only at a later
exclusive market claim. Three scaler fits, zero response-regressor/tree fits,
three stored analog banks, four new continuous books and four retained controls
are planned. No charge, market fit or backtest exists at this declaration.

Require strictly better PA net than V124 in baseline AND combined stress,
without additional hard/MAE breaches or earlier inactivity. Separately report
absolute profit, activity, Evaluation, PA survival and hypothetical payout.
Merely trading more, better forecast loss or beating zero is not a full-route
pass. Inherited Evaluation prefixes are not a gain from the new learner.

After complete observed execution, report date-equal forecast errors in all
four modes, radius/support concentration, mean/risk rejection attribution and
complete accounts. Keep all 126 dates, including empty dates, visible. No
partial selection, optional stop, refit or same-attempt rescue. The sealed
48-date holdout remains closed. No new statistical significance is claimed from
reused development dates or 13,000-plus prior comparisons.

## Implementation Boundary

First implement and verify the pure estimator using invented inputs, then the
causal source-bound pipeline and retained-control account adapter. A finite
one-shot runner, scoped qualification, original source/runtime pins, observed
execution and separate complete-result audit are required before any result.
Component tests are not historical performance or execution qualification.
Focused and affected regression should scale with changed behavior; the prior
non-green full suite remains disclosed. Do not rerun 30,000 unrelated cases for
each pure-helper edit or manufacture a passing central projection.

No orders, market-data purchase, Windows restart, schedule change, Telegram test,
credential transfer or operational-model change belongs to this candidate.

## Implemented Component And Causal Pipeline

`tools/nq_apex_local_distribution_v125.py` now implements the fixed estimator,
closed typed export, native weighted-moment restoration, full joint masses and
radius/date-support diagnostics. `tools/nq_apex_local_distribution_pipeline_v125.py`
reuses the unchanged V123 complete source/population snapshot. It validates all
three mature prefixes before the first scaler and uses only those populations.
The frozen account envelope and its original unsupported mask remain unchanged;
diagnostic records are separate. All 126 scheduled dates, including empty days,
are retained. Model callbacks get detached records and fail without retries.

Independent design/code review found no further concrete production issue after
one numerical repair: native weighted moments can contain tiny negative roundoff
on constant columns. Restoration now retains the exact native variance and uses
the exact native constant mask's scale of one. It does not clip targets, fit a
different scaler or introduce a tuned epsilon. Two native sqrt warnings remain
visible in the successful fixture; original and restored transforms agree.

The first combined fixture run had 53 passes and six setup errors because the
inherited pure-population guard correctly prohibited the scaler's internal
`partial_fit`. The fixture now permits it only inside the observed prefix fit,
after checking exact training coordinates/weights, then restores the guard.
The second run exposed the numerical issue above, also 53 passes/six errors.
Neither was a market attempt or a policy change. The third run passed 60 cases.

Final affected regression passed **1,012 distinct cases**, zero failures/errors/
skips, in 124.705 seconds with actual exit zero. It includes 64 V125 cases
(51 component, 13 pipeline) and twelve-coordinate, maturity/plan, forest,
distribution-account, quantity and utility ancestors. These counts overlap;
do not add the earlier runs. The final JUnit SHA-256 is
`57ce7e9054387539bd206f843d47bea68d644cdfa248dbb6c1a1f577a3b90e23`.
The prior full-repository non-green result remains disclosed; this component
checkpoint did not rerun it or qualify a historical market execution.

All fits above used invented data. Actual V125 market fits, bank construction,
account replays and comparison charges are **zero**. Ledger remains **13,219**.
The finite runner, source/runtime admission, exclusive claim, actual complete
market evaluation and separate completed-result audit remain to do.
V124 remains the latest completed study and failed. A functioning pure predictor
does not make the requested operational route or research goal complete.

## Account Adapter And Alternate Selection Audit

The new `nq_apex_local_distribution_replay_v125.py` translates only the arm-map
and contrast names around the frozen V124 adapter. It retains four exact V124
candidate control books without replaying them, and constructs four new books
through unchanged V119 rules. Caller authentication, rather than an arm label,
establishes which completed controls and learned masses may enter. No ancestor
globals, costs, quantity choice, account rule or evaluation prefix is changed.
Independent read-only review found no semantic blocker with this bounded reuse.
The affected replay/account tests passed 128 distinct cases in 79.259 seconds,
actual exit zero, without failures, errors or skips; JUnit SHA-256
`8706bd68365ad14d43c8c1b1f883ec734d1db2a03d4abd8471fc4f791e89e182`.

`audit_nq_apex_local_neighborhoods_v125.py` checks saved complete masses using
the maximum of two order statistics: the 100th event distance and fifth-smallest
per-date minimum distance. This differs from the production sorted-event scan.
It checks all boundary ties, original date weights, exact integer targets,
unsupported slots, radius and date concentration without fitting or calling
production selection. Distance arithmetic and model validation remain shared;
this is not independent numerical implementation or source authentication.

The combined pipeline/audit test run passed 49 distinct cases in 17.162 seconds,
actual exit zero, without failures, errors or skips. It includes all 126 invented
evaluation dates and an empty date, with fit, production selection and scaler
transform forbidden during the alternate audit. JUnit SHA-256
`899ca6c6977ae8a1e126e1c4baa1bcd9d2b158fc3ee521523c3fab655e1aaf29`.
The earlier standalone 35-case audit run overlaps this count. These and the
previous 1,012-case checkpoint overlap; they are not cumulative unique tests.
The finite runner is being integrated separately. None of these checks is a
market trial, backtest pass, claim or authority to change operational models.

## Primary References

[StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)
defines training mean/variance normalization and weighted fitting; it is
sensitive to outliers. [DistanceMetric](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DistanceMetric.html)
provides the pairwise Euclidean implementation. These software references do
not establish financial predictive power, account compliance or profitability.
