# v95 Proposal: Bounded Nonlinear Payoff Features

Status: SUPERSEDED_BY_PREFREEZE_IMPLEMENTATION. Preserve this original draft;
the reviewed implementation specification is `research-v95-design.md` and
`config/nq-apex-nonlinear-exposure-v95.json`. Zero new actual-data fits,
source-support inspections, raw replays or comparison reservations. v94 remains
the latest completed experiment. Independent design review required exact
v94-dollar superiority, fixed singular-center aborts and authenticated scaler
reuse; it rejected any claim to isolate nonlinearity from regularization.

## Question And Prior Failures

Can a small, training-only nonlinear feature map add predictive value to the
same feasible-dollar task where v94's linear predictor failed? This tests a
representation change, not a new risk budget, target, universe or entry gate.

- v94 lost all paired fold gates and all8 pooled product/mode losses to causal
  means. Its primary baseline risk-cap skips were0. Changing target units or
  relaxing account constraints alone is not an evidence-backed rescue.
- v93's three family-regime interactions worsened all8 pooled losses versus
  v92. More coefficients need not produce useful conditional information.
- v82 already tested an RBF kernel on a different lagged-session direction
  task. It failed Legacy50K, with negative direct kernel PnL and later zero
  account capacity. Do not label this the first kernel test or assume that
  a nonlinear method will work. Read `research-v82.md` before refining this.
- A bounded map is proposed instead of a broad deep-learning or hyperparameter
  search. This is a capacity-control choice, not proof of optimal architecture.

## Draft Comparison

Use the exact v94 causal nine predictors, feasible events, date weights and
four dollar targets from integer unit journals. Reuse each authenticated v94
training-only scaler. Append a small Nystroem RBF map to the nine standardized
linear coordinates, then fit the existing weighted four-output Ridge objective.
The map is fit on each training prefix only, without labels in basis selection.

Draft constants are16 components, gamma1/9, Ridge alpha10, one fixed seed and
no search. These constants are not frozen or selected from v95 outcomes.
The review must assess their effective complexity relative to45 initial
training dates, event clustering, duplicate centers and covariance conditioning.
Use a proven library implementation; do not hand-roll a kernel solver.

Two product-specific primary policies would be compared with exact v94 linear
dollar, matched unit-R and causal mean controls for each product. This would
be8 conservatively counted policy comparisons only when a new run is claimed.
The two linear target controls share the same reused joint-fit authority;
do not count them as two new estimator calls. Record kernel-map fits separately
from regressors, reused scalers, output heads and derived means.

All controls and primary policies must use the same scoring dates and account
execution: NQ<=1/MNQ<=6, current risk reserve, costs, latency, stops, targets,
cooldown, uncapped daily fills and no event/fold account resets. Gate each
policy with only its own four predictions. Keep loss denominators paired and
the existing predictive, practical Evaluation and separate PA/payout criteria.
The model's initial exposure remains a proxy, not later account capacity.

## Required Before Freeze

1. Finish v94 numerical audit, full regression and completion evidence first.
2. Independently review whether the comparison can isolate the narrow question;
   reject or refine the draft before any new support inspection or fitting.
3. Specify exact map/scaler reuse, seed, rank/degeneracy handling, fit counts,
   support, chronological full-calendar purge, cost targets and paired controls.
4. Implement synthetic leakage, output-routing and numerical regression tests.
   Freeze a bounded catalog and hash closure before a one-shot claim.

Never tune rank, width, alpha, gates or risk limits after seeing this version's
results. An insufficient or degenerate prefix is not permission to select a
replacement using validation outcomes. Repeated development remains observed
development; final48 sessions2026-06-29 through2026-09-02 stay closed. No genetic
algorithm, orders, purchases, secret transfer or paper-model promotion.
