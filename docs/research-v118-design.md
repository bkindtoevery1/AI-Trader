# V118: Conditional Outcomes With State-Adaptive Risk Tolerance

Declared before any V118 market fit, claim or replay. V117 is closed and failed;
it will not be retuned. Existing Mac data are sufficient inputs for this study.
Windows and newly collected sessions are not prerequisites. This document and
the pure learning components do not authorize a market claim by themselves.

## Hypothesis And Prior Art

V117 increased baseline PA fills from 22 to 57 but worsened PA PnL in every
execution mode. V112 global correction also increased activity without edge;
V113 monotone calibration did not improve ranking. V80 already used exponential
utility SVR and a Student-t distribution; V106 used fixed-headroom log targets.
Neither exponential utility nor risk-sensitive learning is new here.

Test a conditional empirical distribution of one-contract MNQ outcomes, then
evaluate that same distribution at the current candidate account's own planned
quantity and remaining headroom. This is a distributional payoff model with
state-adaptive risk tolerance, NOT a learned account-state transition/value
model. It predicts a proxy from guard-free unit outcomes. State-dependent
trailing-floor and MAE exits can make actual account PnL differ from q times
the unit outcome. Only the full unchanged account replay tests actual economics.

## Fixed Learner

Train three joint four-response RandomForestRegressor models, one per original
chronological fold, using the original nine event features and actual one-MNQ
net-PnL journals in cents for all four execution modes. Do not use the existing
reference-quantity-multiplied dollar target. Validate every original eligible
label before known initial-capacity and PA stop<=140 filtering; genuine zero
outcomes remain. Do not filter training rows by future entry feasibility or a
profitable control's selected trade subset.

Use original training prefixes of 45/87/129 dates, full-calendar ten-session
purges and 42 scored dates per fold. Every training label must resolve before
the purge-start cutoff in every mode. All 181 raw pairs are existing admitted
same-maturity NQ/MNQ data; 55 context and 126 scored dates remain unchanged.

Parameters: 64 trees, squared_error, depth2, max_leaf_nodes4, min_samples_leaf100,
max_features3 (sqrt of nine), bootstrap=False, random_state202609118, n_jobs1.
No bootstrap multiplicities, scaler, hyperparameter/seed search, early stopping
or fallback. A nonempty training date has total weight1, split equally across
its retained events. Each fitted leaf must contain at least five distinct
training dates; insufficient support aborts rather than deleting a leaf.

For a query, route through each tree and normalize original date weights inside
that leaf, then average these event masses over all 64 trees. Preserve the
actual four-dimensional outcome vectors and their alignment. This is not the
dispersion of 64 tree means. Splits still optimize squared-error means, not a
distributional loss; many trees do not create independent observations or
establish tail calibration. Unobserved tail losses receive no empirical mass.

Sklearn performs all fitting. Exported numeric routing uses its float32 input
conversion, validates graph/support/weights, and must reproduce native leaf
assignments and conditional means. Caller-owned source authentication, causal
plans and complete durable fit receipts remain required before market fitting.

## Fixed Decision And Account Timing

Let Y_i,m be a historical one-contract net outcome in cents, w_i(x) its empirical
conditional mass, q the planned quantity, and H the chosen risk tolerance.
Compute CE_m = -H * log(sum_i w_i(x) * exp(-q*Y_i,m/H)).
Nominate only if all four CE values are strictly positive. Use stable numerical
evaluation; do not clip losses, replace absent outcomes with zero, use tree-mean
dispersion, or introduce a selection epsilon. CE is not expected PnL.

Three own-state paths per execution mode:

1. Exact original V107 all-head control, unchanged model and account behavior.
2. New empirical forest, fixed H=250000 cents (initial research headroom scale).
3. The same fitted forest, H=current balance minus current trailing floor.

Both learned policies use their own current q from the unchanged allocator.
The fixed-H arm is fixed risk tolerance, not state-blind. Never borrow control
balances, quantities, future fills, account termination or PA dates. Each uses
the unchanged original NQ Evaluation, then its own MNQ PA transition.

Evaluate state only after day-stop/busy/cooldown eligibility and after any
previous trade has actually resolved by this decision. Use the known stop and
day-start MAE/DLL, before reading a future entry tick. A positive planned q is
not a guarantee of executable target geometry. The unchanged actual-entry
nominal guard and sizing remain downstream. A zero-capacity event must retain
the existing capacity-skip attempt/cooldown semantics, not become cost-free
model abstention. That timing adapter is still required; the pure learner alone
does not provide it.

Important limitation: while half-headroom sizing binds, q is approximately
H/(2*reserve), so q/H approximately cancels. Headroom adaptation can matter
under contract or MAE caps and integer sizing steps, which can also make its
effect nonmonotonic. Require synthetic non-equivalence and exact cancellation
examples under the frozen allocator before any claim. Do not tune H or resize
to defeat cancellation after market outcomes.

## Complete Comparison

Twelve books cover 1,512 scheduled account-days and all four execution modes.
Retain costs, adverse slippage, latency, stop<=140, actual-entry 5:1 guard,
half-headroom sizing, NQ<=1/MNQ<=6, conservative fresh-PA ceiling5, five-minute
cooldown, uncapped daily fill count, activity, trailing rules and payouts.
All four original control reports and eight candidate Evaluation prefixes
must reproduce. Neither operational V63 nor V92/V102 is replaced.

Primary contrasts: own-H minus original, and own-H minus fixed-H. Both must
improve PA trading PnL strictly in BOTH baseline and combined stress, without
additional hard/MAE violations or earlier inactivity. Fixed-H minus original
is a declared diagnostic contrast, not a rescue gate. Report absolute PA
profitability, numeric Evaluation, PA survival, hypothetical payout and modeled
full-route results separately for every arm. No-trade zero PnL is not success.

Two policies plus three declared contrasts budget FIVE new comparison charges,
13201 to13206, only at a later genuine exclusive claim. Exactly three native
forest fits produce 192 trees, shared between the two learned policies; no
control refit or forecast substitution. Market fitting, full replay, terminal
source verification and independent recorded-account reconciliation remain
pending. Synthetic software training is not a market trial or strategy evidence.

Do not expose partial economics, retry a claim, select a favorable mode, or
rescue a completed result. Reused historical development is not independent
statistical validation. Keep48sealed dates closed and disclose unpriced program
fees/unverified personal cohort. No new data purchase, Windows activation,
order, Telegram test, secret transfer or schedule change belongs to this study.

## References

Conditional forest outcome weights are motivated by
[Meinshausen, Quantile Regression Forests (JMLR, 2006)](https://www.jmlr.org/papers/v7/meinshausen06a.html).
This shallow, date-weighted, nonbootstrap implementation does not inherit the
paper's asymptotic guarantees for dependent financial events.

Fitting and apply/predict behavior use
[scikit-learn RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html).
The installed implementation is pinned and tested as sklearn1.9.0; current
web documentation is not a substitute for local runtime evidence.
