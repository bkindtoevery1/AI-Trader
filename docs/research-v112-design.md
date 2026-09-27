# V112 Prequential Bias Transfer

Implementation design at zero new market fits/claims. V111 is closed and its
failure is unchanged. Latest completed version remains 111 and the ledger is
13,185 until a separate immutable claim. Windows operational V102 is unchanged.

## Question And Precedents

Test one MNQ PA calibration policy on the exact completed V107 phase-micro
route. Keep the original V102 NQ Evaluation path and original HGB models.
Does the learning procedure's historical out-of-sample forecast error transfer
across vintages well enough to improve subsequent PA economics?

The independent read-only precedent review (Jason, 2026-09-13) found no exact
prior implementation within V80/V89-V102/V105/V106/V109 designs reviewed.
V90 learned a common net-R slope with training-mode means; it did not preserve
HGB heads and calibrate prior out-of-sample errors. V98 suggested calibration
as future work. V105/V106/V109 changed support or training targets. This is
not an exhaustive novelty claim and additive calibration is not a new method.

A two-gross-head shortcut was rejected before any fit or claim: in the frozen
V87 kernel, stressed slippage shifts entry, stop and target admission. Different
modes can have different fills/exits or a genuine zero-valued skip. Four mode
targets cannot generally be recovered by subtracting known costs from only
normal/delayed common gross outcomes. Existing V87 tests already demonstrate
this counterexample. V112 does not impose that invalid cost relationship.

## One Fixed Estimator

For every eligible nonempty date d and mode m, compute the equal-event mean
residual r[d,m] = original target minus ORIGINAL historical source forecast.
Fit b[m] = sum_d r[d,m] / (number_of_nonempty_dates + 20). Add b[m] to the
current original source forecast. The fixed 20 zero-residual pseudodates shrink
corrections toward the unchanged model; they are not real market observations.
No recent-window, shrinkage-strength, sign, clipping or threshold search.

Use the installed scikit-learn Ridge with alpha=20, solver=svd,
fit_intercept=False and a single constant input column. Its four coefficients
are four penalized intercept corrections, checked against the closed-form
date-mean equation. Two multioutput calibration fits learn eight scalars;
there are zero new HGB or scaler fits. The documented
[Ridge objective](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html)
supports this computation, not a trading-edge claim. No runtime upgrade.

The first outer fold is exactly unchanged and has no calibration fit. For
folds two and three, retain all PRIOR outer scored dates strictly before the
current fold's existing ten-full-session purge. Reconstruct the purge from the
complete exchange calendar, not raw-row/event counts. Include all original
opportunities with available own-product forecasts, not selected trades,
surviving accounts, future entry-geometry survivors or profitable subsets.
Empty dates remain in the schedule but are not observed zero residuals.

Validate all original four-mode labels, including true skips and infeasible
events, BEFORE filtering, with every resolution strictly before the cutoff.
Preserve original event identity, per-date weights and fresh-Evaluation-
reference-exposure dollar units. These are not current PA quantity/PnL labels.
The caller must authenticate the six original source models and all complete
original forecasts. Hashes of supplied inputs alone do not prove provenance.

Never re-predict past rows with the current source model: those rows can be
in its training/tuning prefix. Historical forecasts must come from their original
causal outer model. Fold three uses uncorrected original fold-two forecasts,
never this candidate's fold-two forecasts. Freeze each correction before its
whole current scoring fold; do not update it from that fold's later labels.

## Interpretation And Decision

Earlier vintages and market periods may not estimate the current model's bias.
This is NOT an independent calibration set for the current model. Adding a
correction is equivalent to moving its original decision boundary to -b[m],
despite retaining all-four-positive syntax. It can increase or decrease trades;
it is not calibrated confidence or proof of coherent cross-mode costs.

Preserve the actual original execution allocator, stop<=140 support, nominal
5:1 guard, own-product fills, commissions/slippage, latency, cooldown, carried
cash, PA activity and payout rules. No forced activity or use of historical PA
account state as a calibration feature. Residual calibration does not solve
the guard-free-target/current-PA-utility mismatch identified by V109.

One candidate plus one contrast reserves two comparisons, 13,185 to 13,187,
only at an authenticated preoutcome claim before any market calibration fit.
The full runner must retain 181 raw pairs, 126 scored dates and eight continuous
books / 1,008 scheduled book-days, reproducing four original controls and four
unchanged NQ Evaluation prefixes. No partial outcome publication or retry.

Candidate-minus-control PA trading net must improve in BOTH baseline and
combined stress, without added hard/MAE breach or earlier inactivity. Report
absolute PA net, Evaluation, PA survival and full-route/payout separately.
Forecast bias, more nominations or a favorable diagnostic mode cannot rescue
a failed economic gate. The 48 holdout dates stay closed; development reuse,
unpriced program fees and unverified personal Legacy cohort remain disclosed.

## Current Boundary

The component and separate claim-bound fit/forecast/account runner are
implemented, but implementation is not a market fit, claim, performance result
or Windows deployment. Focused/full regression, actual source-interface admission
and independent review must qualify their final bytes before freeze/claim.
The runner also reconciles original exit receipts and raw JUnit results; asserted
success fields without their evidence cannot authorize execution.

Review found and corrected resealed callback input replacement and incomplete
nested restoration receipts before any market fit. The fit pins its entry-time
input identity, and restoration validates complete intrinsic plan/input schemas.
Source authentication still belongs to the runner, not self-computed hashes.
No orders, Telegram, login, subscription, capacity or schedule action follows
from this design or synthetic software tests.
