# V113 Monotone Forecast Calibration

Implementation design only. No new market fit, claim, account replay, outcome,
or operational promotion. V112 is closed; ledger13,187 stays unchanged until
a separately admitted immutable claim. This is a declared successor experiment,
not another V112 setting or a reinterpretation of its failure.

## Question

V112 increased nominations and PA trades but lost more in all four modes,
including before execution costs. A constant residual correction shifts weak
and strong original forecasts equally. Test whether their conditional payoff
depends on the original signed forecast level enough to improve that correction.
Do not take its absolute value. This score is not a calibrated probability or
certainty of a trade, and the new mapping adds no information to that score.
With positive total slope it is exactly a learned threshold on the original
score; zero slope admits all available scores or none. This is a changed
learned decision boundary, not improved within-mode ranking or a threshold-free
method. No epsilon may turn a small positive slope into a flat gate.

Retain the exact V102 HGBs, their original nine features, targets, settings and
original uncorrected previous outer-fold predictions. No new feature discovery,
price sequence, direction classifier or HGB fit is proposed. The sole addition
to V112 calibration is one monotone affine slope per execution mode. V89 payoff
decomposition and V90 shared raw-feature slopes are different precedents, not
evidence that this candidate will work. This is not an exhaustive novelty claim.

## Learner

Use the exact V112 eligible prior-OOS population and full-calendar ten-session
purge. Validate every eligible label before feasibility filtering. Keep genuine
zero labels; absent predictions are not zero-valued observations. Empty dates
remain scheduled but contribute no residual. First scoring fold is exact
original passthrough, with no calibration. Fold3 never uses corrected fold2
predictions or the current model's repredictions of older training rows.

For each later fold and mode, assign every nonempty date total weight1 and
split that weight equally among its events. Let p be the original prediction,
u the original target, c its weighted prediction mean, and s its weighted
population standard deviation. Exact constant predictions use their original
value as c, s=1 and z=0; otherwise z=(p-c)/s. Transforms use training only.
Fit a,b to minimize sum(w*(u-p-a-b*z)^2)+20*(a^2+b^2), with b>=-s.
The corrected forecast is p+a+b*(p-c)/s. Its derivative in p is1+b/s>=0:
the fit may flatten but cannot invert the original ranking. No clipping of
negative outcomes, probability cutoff, slope search or fallback is allowed.

Use dense [sqrt(w),sqrt(w)*z] rows with two sqrt(20)*identity penalty rows,
zero penalty targets, and scipy.optimize.lsq_linear(method='bvls',
lsq_solver='exact',tol=1e-12,max_iter=100). This is a bounded convex least-squares
problem, not a hand-written optimizer. Independently verify each fitted pair
against the two-dimensional normal equations with its one active lower bound.
Solver failure/nonfinite output or changed input is a technical failure, not
a reason to retry with another estimator. Original input and exported transform,
coefficient, source-vintage and stage bindings must survive callback boundaries.

There are eight scalar estimator fits (four modes times two later folds),
16 learned coefficients and two four-mode forecast-transform groups. Original
feature scalers remain unchanged. Per fold record transform completion, start
and completion for each mode in original order, then model completion:20stages.
The regularization20 is retained from V112, not searched for this result.
In exact centered arithmetic a equals the V112 date-mean bias; finite-precision
equivalence requires numerical verification, not a byte-equality assertion.
The runner must verify that intercept against the authenticated V112 coefficient
using the identical population and fixed1e-10relative/absolute tolerance. Retain
V112's exact saved coefficients/forecasts for its actual control; no control
refit. A zero-slope synthetic conformance case must retain exact positive masks;
numerical near-zero boundary disagreement is not repaired by a selection epsilon.
The slope may correlate with multiple market regimes or vintage shifts; this
does not isolate any such cause or establish current-vintage calibration.

## Full Comparison

Three own-state arms: exact uncorrected V107 repair reference, exact completed
V112 constant calibration, and the new monotone correction. Restore all models
and complete forecasts; do not refit either control. Every arm retains original
NQ Evaluation, then MNQ PA with stop<=140, actual5:1nominal guard, half-headroom
sizing, NQ<=1/MNQ<=6, conservative fresh-PA5, costs/slippage/latency, unchanged
brackets, cooldown, activity, cash transitions and payout rules. All-four
strict-positive nomination syntax remains, but its learned boundary changes.
Targets remain original fresh-Evaluation-reference-exposure dollars, not current
PA quantity, dynamic capacity or net account payoff.

Run the same181explicit raw pairs/126scored dates over12books/1512scheduleddays.
Eight complete controls and four new Evaluation prefixes must reproduce. The
candidate must improve PA net trading PnL over BOTH controls in BOTH baseline
and combined stress, with no additional hard/MAE breach or earlier inactivity
for either contrast. Cost-only/latency-only are diagnostics, not rescue modes.
Positive absolute PA, modeled full route and payout remain separate gates.
An improvement over a losing control alone cannot establish viable operation.

At terminal publication also report date-equal all-opportunity squared forecast
loss against both controls, by later fold/mode and pooled, with first-fold
identity separate. Decompose prior residual covariance into within-date and
between-date contributions, report per-vintage contributions and original-score
support/extrapolation. These describe calibration failure and are not new gates
to substitute for economic failure. If account PnL improves without predictive
improvement, do not claim general conditional-payoff learning was established.
Added/removed all-four-positive nominations and execution exclusions must remain
separate. Threshold-equivalent masks are a diagnostic only; rounding cannot
alter the actual frozen forecast-based nomination path.

One policy plus two predeclared contrasts charges three comparisons13187to13190
only at a genuine market claim. Model source, executable runner, actual-source
admission, independent review and focused/full regression must be qualified
before claiming. Software fixtures are not market evidence. Do not launch a
trial from this design or component implementation alone. No partial outcome
publication, optional stopping, retry after claim or after-result tuning.

Historical reuse is development, not independent validation. Keep48holdoutdates
closed and disclose unpriced program fees/unverified personal Legacy cohort.
No Windows installation/activation, subscriptions, schedules, orders, Telegram
messages or fixed operational model replacement belongs to this study.

## Numerical Reference

[SciPy bounded least squares](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.lsq_linear.html)
documents the convex objective, bounds, BVLS algorithm and convergence fields.
The library contract supports numerical implementation, not a trading edge.
