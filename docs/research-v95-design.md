# v95: Fixed Additive Nonlinear Dollar Representation

Pre-outcome specification. No new v95 source support, label replay, fit or
trial reservation has occurred. Freeze code, tests, policy and exact dependency
membership before the one-shot attempt. Authority is Legacy50K, not old25K.

## Narrow Question

Append16 training-only RBF features to the exact nine standardized v94
predictors. Does this fixed representation improve the same paired dollar
forecasting task against exact v94 linear-dollar, matched-R and causal means?
This is not a capacity-matched comparison or isolation of nonlinearity from
regularization. The objective is weighted squared loss plus alpha10 times
the sum of squared linear and kernel coefficients, with an unpenalized
intercept. Correlated appended features change the induced penalty geometry.
No claim of optimality or expected profitability follows from the design.

v82's different lagged-session RBF failed; v93 interactions worsened prediction;
v94 dollar target rescaling also failed. Preserve those failures. This bounded
experiment is not the first kernel test, a broad architecture search or rescue
of a completed result. No genetic algorithms or neural hyperparameter sweep.

## Causal Training And Fixed Map

Reuse exactly the v94 feasible training universe, mature unit journals, integer
dollar targets, date weights and authenticated scaler for each product/fold.
Validate the complete original prefix BEFORE excluding q_ref0 events; all
original labels in all four modes must resolve strictly before09:00ET on the
first full-calendar purge session. Bind full/retained identities, features,
targets, weights, maturity and exact reused fit metadata. A missing/mismatched
control is an error, never a request to refit it. Keep at least40 feasible
events/20 dates. Reuse means from the same original training prefixes.

Weights are1 divided by feasible events on that date, totaling one per date;
do not normalize the whole training prefix to one. Reuse v94 mean/scale with
no new scaler fit or map-output scaling. The new design is exactly[z9,phi16].
Ridge(alpha10,solverSVD,interceptTrue) is fit on all retained rows and the four
original dollar targets. Four outputs are independent, as in v94's joint fit.
Dropping its unused R heads creates no cross-target sharing change.

Center ranking uses canonical sorted-key compact ASCII JSON with finite
numbers, SHA256 once, seed20260995 and product salting, but no fold salting.
Date key is digest([seed,product,"date",date]). Rank distinct feasible training
dates by(hash,date); keep16. Within each chosen date rank events by
(digest([seed,product,"event",date,event_id]),event_id); keep one. Center-bank
order is selected-date rank order. This uses immutable outcome-free identities
only, not current/future targets, embargo data or scoring features. Do not use
event abundance as extra sampling mass. Sixteen dates are not assumed to be
independent observations or sufficient statistical power.

Use the installed, environment-locked sklearn.Nystroem(kernelRBF,gamma1/9,
n_components16,random_state20260995,n_jobs1) fitted on exactly these16
standardized rows. All16 are used; preserve the library permutation and
normalization. Record selected IDs, center bank hash, permutation, components,
normalization, center Gram eigen/singular values and augmented matrix hash.
No original source/model data are mutated.

Duplicate standardized centers abort before map fit. Reject a nonfinite or
invalid Gram matrix, or s_min<=max(1e-12,16*float64_epsilon*s_max), before map
fit. These tests precede new fitting but follow the one-shot claim. If any
product/fold fails, preserve the claimed attempt and actual stage counters;
never pick replacements, reseed, reduce rank, change width/alpha, or fall back
to the linear control. Full rank of the combined25-column design is NOT
required: positive-alpha Ridge handles collinearity. No rank criterion is
chosen from observed v95 performance.

## Execution, Comparators And Counts

Exactly eight policies: two products times nonlinear_dollar, feasible_dollar,
matched_R and training_mean. The last three are exact reused v94 policies,
including predictions and full account/direct journals in all four modes.
Do not silently add the old v92 control as a ninth/tenth policy.
Schedule6new kernel-map fits and6new four-output Ridge fits,24new heads,
0new scalers/control fits. Reuse6joint fit records/scalers and24mean outputs;
means are not new fits. Record six stages per product/fold: model_started,
kernel_map_started/completed, estimator_started/completed, model_completed.
Eight comparisons at the claim raise13,105 to13,113; an aborted claim stays
counted. Coding or synthetic tests are not actual market trials.

Replay the same181 explicit-contract pairs in order,55warmup then126scored
dates across three42-session folds with10full-calendar purge sessions. Both
product prefixes are validated before either model fit. Every current-date
policy chooses before its raw outcome tape opens. Rebuild all unit journals;
require exact predecessor label/receipt/window/fit and three-control journal
conformance. q_ref0 predictions remain null, not zero returns. Each policy
selects using its own four strictly-positive outputs, never another model's
outputs. No clipping, inversion, calibration, mode selection or optional stop.

The unchanged v87 continuous account retains NQ<=1/MNQ<=6, its current reserve,
costs, latency, stops, mean targets,300-second cooldown and uncapped daily fills.
Never reset account state at an event/fold or change budget to rescue losses.
q_ref is still initial capacity, not later actual size or account utility.

## Preregistered Interpretation

Preserve v94 paired error criteria against matchedR and causal mean. ADD the
same comparison against exact v94 linear-dollar to support the representation
claim: lower average four-mode loss than ALL THREE controls in the same two
of three folds, and lower pooled average/baseline/stress than all three.
This additional predecessor-superiority condition is new, not described as
an unchanged gate. Use identical feasible event IDs and equal-weight nonempty
dates; report empty dates, never invent zero MSE. Keep all126account dates.

Keep the practical screens: baselineSharpe>=0.5, stressSharpe>0, positive net
in all four modes,30active baseline dates, HACeffective>=84, eight-policy
family p<=0.2, baseline AND stress numeric Evaluation. PA/payout separately.
Bootstrap uses the inherited exact integer-cent inclusive-tie method with
2000draws,10session blocks and separate fixedseed20261995. No seed search.
Guard-free fixed1NQ/6MNQ diagnostics are not actual-account profit.

These are outcome-informed development screens, not independent validation.
Global historicalDSR, fees, liquidity, compliance and a verifiedPA route remain
unproven. Keep the48-session June29-September2,2026 holdout closed. Do not use
prospective paper outcomes or human decisions as an unseen test. No orders,
purchases, secrets, operational deployment or frozen-runtime changes.
