# v90 Shared Conditional Payoff Effect

## Hypothesis And Limits

v88 and v89 forecast errors exceeded prefix means; v89's four-mode intersection
selected four NQ and zero MNQ events. The next experiment tests a different
inductive constraint, not a lower acceptance threshold: execution conditions
share one conditional feature slope but retain four separate training means.
Use the exact v87 causal events, six features, products, calendar and execution.
No new entry filter, quantity change, hit-probability model or stress removal.

This is outcome-informed exploratory development on previously observed dates.
Sharing reduces variance only if conditional effects are sufficiently similar;
opposite or differently scaled effects can cause negative transfer. Four mode
labels are correlated counterfactuals for one event, never four independent
samples. Baseline and cost stress can have different exits or admission skips.
The model does NOT assert deterministic cost subtraction or monotone returns.

## Estimator

Each event date has total training weight one, divided among all original events.
Let y_im be actual one-contract net-R for event i and mode m, retaining every
loss, zero skip and time exit. Fit weighted StandardScaler on training features
only. Fit one Ridge(alpha=10, solver=svd, intercept=True) to the per-event mean
over four y_im, without stacking or renormalizing weights. The objective is
sum_i w_i (mean_m y_im - b - z_i beta)^2 + 10 ||beta||^2.

For mode m, predict its weighted training mean plus
Ridge.predict(z) minus the weighted training grand mean. This is the equal-mode
constrained least-squares model with one six-dimensional beta and four free
intercepts, rather than v88's 24 slopes and four intercepts. It is also the
projection of equal-alpha v88 ridge slopes onto a common slope; it is not a
new nonlinear architecture. No mode offset is fitted from scoring data.

Its average-mode prediction is algebraically identical to v88. Any possible
variance reduction comes only from replacing feature-dependent mode contrasts
with fixed training offsets; mean-target MSE cannot establish an improvement.
With d_alpha=trace(S(S+10I)^-1), S=Z'WZ, effective regression degrees of freedom
change from 4+4*d_alpha to 4+d_alpha, not from quadrupling the sample count.
The equivalent summed-four-mode-loss constrained objective has penalty40;
using penalty10 on stacked rows would silently change effective alpha to2.5.

All four expectations must still be strictly positive for a shared selection.
The minimum training mean therefore determines the constant per-fold mode
bottleneck. This may still produce sparse or zero trading; never force trades.
Do not clip, invert, reorder mode forecasts or select whichever mode performs
best. Diagnostics must expose bias from the common-slope constraint.

Two main product policies and two exact v88 controls are four counted policies.
Six new one-head fits plus six old four-output control fits give 12 estimators
and 30 learned output heads. The 24 derived mode outputs of the new fits are
not 24 independently learned heads. Four added comparisons move 13,079 to
13,083 only at reservation. No parameter catalog or hidden alternative fit.

## Frozen Evaluation

Keep 181 explicit-contract raw dates, 55 warmup and 126 scored dates in three
contiguous 42-date folds. Purge ten sessions from the full 617-session exchange
calendar. The final 48-session holdout stays sealed. Predictor-only structural
preflight checks original full training prefixes and the 30-active-date upper
bound; hit/other branch counts are irrelevant to this continuous-target model.

Fit only fully processed prior training dates. Every current-day prediction
precedes current-day raw-tick access. Recreate the exact v88 counterfactual
labels, control fits/predictions, raw receipts and all direct/account journals.
Any conformance mismatch fails the complete batch. Costs, entry delay60/240s,
common exit decision+5460s, ATR stop, completed mean target, 300s cooldown,
uncapped entries, non-overlap and NQ1/MNQ-up-to6 account sizing stay unchanged.
Account paths start once and never reset at a fold boundary.

Keep baseline Sharpe>=0.5, stress Sharpe>0, positive net in all four modes,
30 baseline active dates, HAC effective samples>=84, four-policy adjusted
block-bootstrap p<=0.20 (2000 samples, ten-date blocks, seed20260990) and numeric
Evaluation pass in baseline and stress. Assess PA and payout separately.
These development screens do not resolve missing global DSR, unpriced account
fees, liquidity assumptions or signal-service compliance.

Report day-weighted all-event per-mode MSE against prefix means and exact v88.
For each of six mode pairs, also report squared error of the predicted payoff
contrast against the actual contrast. No within-mode agreement diagnostic is
success merely because common slopes impose it algebraically. Opposite-slope
synthetic tests must demonstrate potential negative transfer. Prediction and
contrast losses are diagnostics only, not extra strategies or tuning criteria.
Require common-mean prediction identity with the exact v88 control (absolute
tolerance 1e-10) on every scored event; also report the maximum deviation and
the common-slope versus averaged-control-coefficient deviation. This is model
algebra conformance, not market-performance evidence.

Freeze policy, code, tests, environment and predecessor evidence before one-shot
preflight and reservation. No partial performance, optional stopping, refit,
rescue threshold, holdout opening, live orders or operational deployment.

References: [Caruana, Multitask Learning (1997)](https://www.cs.cornell.edu/~caruana/mlj97.pdf)
motivates shared representation, not a profitability claim for this model.
The linear constraint above is our explicitly derived hypothesis. Implementation
uses official [scikit-learn Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html),
checked against the installed 1.9.0 runtime.
