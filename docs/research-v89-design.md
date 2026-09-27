# v89 Target-Hit And Conditional Payoff

## Failure Hypothesis

v88 selected a profitable baseline NQ tail but failed coverage, family evidence
and stress Evaluation. Its all-opportunity squared forecast error was worse
than training means in all four modes. v89 tests a new objective decomposition,
not a rescue of its observed threshold, alpha, risk size or calendar. This is
outcome-informed exploratory development on already observed dates.

For each product and execution mode, fit the probability of an actual
MODEL_TARGET exit. Separately regress the signed, actual net-R conditional on
target-hit and on every other outcome. Recombine as
`E[net_R|x] = p(hit|x) * mu_hit(g) + (1-p(hit|x)) * mu_other(g)`.
Target-hit is not the same as profit. Keep time exits, losses and zero-payoff
admission skips; never replace payoffs by assumed +target/-stop amounts.

The two main product policies use the original six causal features for hit
probability. A counted geometry-only control uses just original target/stop
distance g. The two branches' payoff heads use only g and are SHARED by both
probability variants. Two more controls reproduce exact v88 conditional ridge.
Six counted policies add to 13,073 only at reservation, producing 13,079.
Diagnostics, execution stresses and exact source conformance are not selectable
extra policies. A control cannot be nominated as a new main discovery.

## Frozen Estimators

Use a single training-only day-weighted StandardScaler on the unchanged six
v88 features. Geometry-only inputs use its first transformed column. Each event
date has total training weight one divided among all its original events.

For each of four modes, fit full-feature and geometry-only binary logistic
models with C=0.1, lbfgs, tolerance 1e-10, maximum 2,000 iterations, L2 penalty,
unpenalized intercept and no class balancing. The weighted objective is
sum(w * negative log likelihood) + 5 * squared coefficient norm. No separate
calibration fit or probability cutoff is selected. Convergence warnings fail.

The shared hit and other payoff regressions use Ridge(alpha=10, solver=svd)
with an intercept on geometry only. Retain original per-date event weights
when subsetting a branch; do not renormalize them to inflate small branches.
Every product/fold/mode must have both branches represented on at least five
training dates BEFORE any new batch fit. This is feasibility, not power.

There are six new fitted product/fold objects: 48 probability fits and 48
conditional-payoff fits. Six exact v88 multioutput control fits add 24 heads.
Total: 102 underlying estimator fits and 120 output heads. Scaler fits are
reported separately, not called additional trading-model comparisons.

## Chronology And Execution

Preserve all 181 raw dates, the last 126 scored dates in three contiguous
42-date blocks, 55 warmup dates and a ten-session purge derived from the full
617-session exchange calendar. Fit only each fold's entire original training
prefix. Before freezing, only synthetic fitting is allowed. After freezing,
structural preflight may inspect the already sealed v88 TRAINING subsets for
branch feasibility. These are previously observed outcomes, not fresh evidence;
no new raw labels or models are loaded at that stage.

During the new run, generate every day's decisions before opening that day's
raw tape. Fit only labels generated from earlier fully processed days and
append today's labels after predictions and execution. Reproduce the complete
v88 label collection, fits, selected-event predictions, raw receipts and
conditional-ridge direct/account journals. A mismatch is a terminal integrity
failure; no retry with changed execution rules or model constants.

All four predicted mode expectations must be strictly positive for selection.
Every mode uses the same selected events. No outcome clipping, sign inversion,
feature search, score-based sizing or fit after seeing a scored block.
Retain actual NQ1 or MNQ-up-to6, frozen ATR stop and mean target, 60/240-second
entry delay, common decision+5460-second exit, uncapped daily entries,
five-minute post-resolution cooldown, all account admission guards and costs.
Accounts initialize once at score start and never reset at fold boundaries.

## Evidence And Stop Rules

Use the same practical screen as v88: baseline Sharpe >=0.5, stress Sharpe >0,
positive net in all four modes, at least30 baseline active dates, HAC effective
samples >=84, family-adjusted block-bootstrap p<=0.20 and numeric Evaluation
pass in baseline and stress. Use all six registered policies in the family,
2,000 samples, ten-date blocks and fixed seed20260989. Assess PA survival,
payout and adverse excursion separately. Global historical multiplicity,
unpriced program fees and operational compliance are not solved by this model.

Publish all-event, day-weighted net-R MSE for every policy against prefix means.
For the new probability heads also publish Brier score and log loss against
training hit rates, plus geometry-control differences. Log-loss diagnostics
use numerical probability clipping only, never prediction/selection clipping.
These diagnose the stated hypothesis, not a posthoc policy-selection rule.
Do not claim general predictive improvement if full-feature forecasts fail to
beat the simpler geometry or training-mean benchmark. Overlapping event labels
are not independent trades; financial tests use chronological daily vectors.

Freeze code, tests, policy, environment and dependencies before the one-shot
preflight and reservation. No partial metrics, optional stopping, reruns,
threshold rescue, holdout opening, order placement or deployment changes.
A development screen pass is not a verified funded account or actual payout.

Estimator references: [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)
and [Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html),
official scikit-learn documentation, checked for the installed 1.9.0 runtime.
