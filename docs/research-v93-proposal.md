# v93 Proposal: Family-Conditional Regime Payoff

Status: `NOT_FROZEN_NOT_RUN`. Outcome-informed planning only, not admission.
No v93 fit, calibration, replay, reservation, feasibility result or performance
claim exists. This draft reads documentation/source only, not market data,
price rows, predictions or sealed holdout. Independent v63/v92 operational
paper books continue under their own authority; v93 neither changes nor joins
them. No operational action, ensemble, routing or promotion is proposed here.

## Evidence And One Primary Hypothesis

Sources: `docs/RESEARCH_CURRENT.md`, `docs/research-v92.md`,
`docs/research-retrospective-v86.md`, `docs/research-v92-design.md`, and the
frozen `tools/nq_apex_soft_regime_v92.py` / `tools/nq_apex_opportunity_model_v88.py`.
The documented v92 result broadened opportunities without broad executed
coverage; five of eight mode losses exceeded their causal training means.
NQ account risk caps also blocked later guard-free recovery. Neither weakness
is repaired by lowering activity requirements or treating direct PnL as cash.

Primary hypothesis: reentry and wick-rejection opportunities have different
regime/payoff slopes, which v92's additive family indicator cannot express.
This is a testable explanation for predictive failure, not an established cause.
Keep all nine v92 features and append exactly three raw-feature interactions:
`w*s`, `w*v`, `w*b`, where `w` is the existing wick-family indicator, `s` is
signed slope/ATR, `v` is log relative volume, and `b` is log previous bandwidth
over preceding-20-width q20. Standardize the resulting twelve columns on train
only. Retain date-weighted Ridge(alpha=10, SVD, intercept), four separate actual
unit-contract net-R targets, and all-four-mode strict-positive selection.
The sole model change is family-dependent slopes for these three covariates;
there is no new event filter, direction, target, stop, model class or size rule.
No threshold sweep, feature search, leverage increase or genetic algorithm.

## Fixed Controls And Execution

- C1: exact broad-event v92 main policy for each product, using verified sealed
  evidence on the identical calendar/event IDs; never relaunch completed v92.
- C2: each mode's date-weighted causal training mean, with the same four-mode
  positivity rule and account execution. This is a counted diagnostic policy.

Apply the primary and these two controls separately to NQ and MNQ; no product
switcher, winner substitution, extra narrow-population comparison or ensemble.
Compare forecast losses on every common opportunity, including skipped/zero
labels, never only selected trades. A control is not a replacement lead.
Preserve v92's broad 10:30-14:00 stream, NQ x1 / MNQ up to 6 sizing, ATR stop,
immutable mean target, nonoverlap, 300-second cooldown and all account guards.
Retain the full baseline/cost-only/latency-only/stress factorial: entry delays
+60/+240 seconds and common decision+5460-second exit deadline. Report trading
fees/slippage separately from latency and their interaction, including changed
admissibility. External program fees remain unpriced, with renewal units separate;
net trading PnL is not net program cashflow. Do not choose a favorable cost mode.

## Chronology And Closed Data

No hyperparameter tuning or probability calibration is proposed. Fit scaling,
coefficients and mean controls solely on each expanding chronological training
prefix, with one total weight per event date. Keep the 55-date warmup, three
42-date scoring folds and ten-session purge on the full 617-session calendar.
Prior fits continue between refits; account cash, peaks and cooldowns never reset
at fold boundaries. Any later tuning/calibration would require a separately
declared train-only inner chronological split with the same purge, before freeze.
Completed-minute inputs and 20 strictly earlier same-clock volume dates only;
all products' predictions precede opening that date's raw outcome tape. Labels
must match the actual stop/target/cost/delay and mature before training eligibility.
Hash-bind source prefixes, dates, event IDs, labels, model and execution receipts;
assert prefix invariance and no future-volume, cross-fold or postentry leakage.
The final 48-session holdout stays closed. Reused development dates are not new
independent validation; operational paper outcomes must not tune this proposal.

## Feasibility And Falsification

Before any future outcome replay/fit, a separately authorized preflight must
verify exact v92 event identity, causal feature availability, finite interactions,
at least 40 training events/20 dates per fold and 20 training dates per family.
Require three independent added columns after projecting out the retained
design under a predeclared numerical rank rule; insufficient support aborts.
Require at least 30 structurally possible scored dates. Check unit-stop risk plus
cost/slippage reserves against inherited account capacity, tick/contract rounding
and flat-state affordability. Synthetic losing-path checks must expose inability
to resume without weakening guards. Neither opportunity nor affordability bounds
prove 30 executed days; path-dependent tradability remains an outcome criterion.
Falsify the predictive hypothesis for a product unless equal-mode-average,
date-weighted MSE beats BOTH controls in at least two of three scoring folds and
pooled scoring, with pooled baseline and stress MSE each also beating both.
Even predictive success fails as a candidate unless unchanged v92 development
screens and numeric Evaluation in baseline/stress pass on risk-guarded accounts.
Preserve 30 active dates, HAC effective samples>=84, baseline Sharpe>=0.5,
stress Sharpe>0 and positive net all modes; account dormancy cannot be rescued
by guard-free profit. PA survival/payout are separate, not inferred from Evaluation.

## Selection Accounting And Next Boundary

Before authorization, enumerate and freeze every primary/control/product policy,
execution comparison, estimator/scaler fit, learned head and any inner trial;
reconcile actual ledger history rather than inventing a final trial count here.
Count inspected controls, failed/aborted attempts and any outcome-informed revision.
Retain the block-bootstrap gate p<=0.20, 2000 samples/10-date blocks, with a frozen
seed and familywise comparison set reflecting this catalog, not v92's four-policy
set. Correlated modes/events are not independent samples; historical DSR remains
unavailable. No reservations occur in this draft. Freeze reviewed code/tests and
protocol before any new data access; one-shot failures confer no retry authority.
