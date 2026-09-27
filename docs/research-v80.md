# v80: Downside-Aware Payoff Models

This is the main user-authorized research task. The v79 minute-volume ablation
is a separate auxiliary experiment. Neither experiment changes the frozen v63
runtime, sends messages, selects an account provider, or enables orders.

## Frozen Design

Three new fixed pipelines learn the long and short **absolute net payoff**,
instead of only the difference between those payoffs:

1. Conditional 35th-percentile shallow gradient boosting.
2. RBF support-vector regression of exponential downside-sensitive utility.
3. A small Student-t likelihood neural network estimating location and scale;
   the action score subtracts one quarter of the fitted standard deviation.

The last score is a risk penalty, not a statistical confidence interval. A
strictly positive, unique maximum selects long or short; otherwise the model
stays flat. No genetic algorithm, hyperparameter, threshold, seed, or checkpoint
search is permitted. The neural model uses the fixed final epoch.

All three use the unchanged 30-dimensional v63 opening echo-state features.
They are freshly checked against the original source identity and cached values.
The source has 617 complete paired sessions ending 2026-06-12. Four chronological
fits use training prefixes of 325, 398, 471 and 544 sessions, followed by ten
purged sessions and 63 scored sessions. The previous fit continues over the
between-fold ten-session intervals, yielding 282 contiguous signal dates.

Training labels use minute OHLC paths, a 46.75-point stop from the slipped entry,
0.25-point adverse entry and exit fills, and $1.04 round-turn commission per MNQ.
Gap stops use the observed opening price rather than an assumed stop fill.
These labels approximate execution; they do not establish tick-level fills.

Final replay uses exactly the frozen v78 ordered-tick engine over the same 181
dates and explicit contract pairs. The unchanged v63 signals are replayed again
and every reference account journal must reproduce v78 exactly. Legacy 50K
Evaluation followed by a newly activated PA is primary; EOD 50K is comparison
only. Both baseline and mandatory stressed execution are reported. Evaluation
uses two MNQ, PA one MNQ, and at most two actual contracts may be open.

Direct one-MNQ daily PnL is also computed on **all** 181 dates, without account
guards but with the exact same stop, slippage and commission. This prevents an
early account closure from truncating the vector used to compare model quality.
It is separate from account survival, payout, and billing evidence.

## Inference Limits

The policy and executable dependencies must be locked before fitting or opening
new outcomes. A create-if-absent run marker reserves six comparisons: three
new pipelines times two account families. Mandatory stress is not a selectable
variant. The unchanged reference is a conformance check, not another search.
Together with v79's twelve reserved comparisons, the conservative historical
trial count is 12,969. This does not make the reused dates independent or restore
the missing all-history DSR distribution.

A development shortlist requires the prespecified Legacy evaluation, PA,
payout, return, coverage and diagnostic significance gates in the policy.
Even a shortlist pass is not a verified 50K pass or promotion evidence. Exact
program fees and PA fee plan, planned risk/reward and signal-service compliance,
manual reaction latency, and independent final confirmation remain separate
limitations. The sealed 2026-06-29 through 2026-09-02 holdout stays closed.

Results are withheld until the complete candidate family and all account paths
finish. Failed or interrupted runs remain terminal evidence; they are not
silently restarted or retuned.

## Implementation References

The quantile estimator uses scikit-learn's supported quantile loss, not a
hand-built tree implementation: [HistGradientBoostingRegressor documentation](https://scikit-learn.org/1.5/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html).
The likelihood uses PyTorch's StudentT distribution with an explicitly fixed
degree of freedom: [PyTorch distributions](https://docs.pytorch.org/docs/stable/distributions.html).
Library versions actually used are recorded in the preoutcome environment lock.
These references justify the implementation primitives, not investment returns.

## Completed Results

Completed 2026-09-07T02:46:48Z. All 181 explicit raw pairs and 402,041,614 events
were fully verified. Three pipelines were genuinely trained across four outer
folds: twelve pipeline fits, comprising twenty estimator fits. The unchanged
v63 feature values and both reference account families reproduced exactly.

The table is direct one-MNQ PnL over all 181 dates, after simulated execution
costs but **before unverified external program fees**. These are not the final
account balances or cumulative paid earnings.

| Model | Long/Short/Flat | Baseline USD | Stress USD | Baseline Sharpe |
|---|---:|---:|---:|---:|
| Quantile boosting | 0/0/181 | 0.00 | 0.00 | 0.000 |
| Utility SVM | 5/0/176 | -26.20 | 10.50 | -0.122 |
| Student-t MLP | 5/0/176 | -21.20 | -179.50 | -0.098 |
| Unchanged v63 reference | 109/37/35 | -431.34 | -628.00 | -0.252 |

All three new models failed Evaluation in both Legacy and EOD, never entered PA,
and never reached payout eligibility. Family-adjusted bootstrap p-values are
1.0. Their sparse or entirely flat outputs are insufficient for the account
objective; zero PnL with zero trades is a failure, not a risk-free success.
The training and raw replay were populated and completed. This is not a
zero-observation validation loop.

The prefrozen ranking lists utility SVM first, but none is shortlisted or
deployment-ready. Its positive stressed five-trade total is not robust evidence;
stress also changes execution time and can incidentally improve an individual
trade despite worse costs. Both cost modes are required. The reference's old
single baseline Evaluation pass still failed PA inactivity, as established in v78.

The result supports rejecting these fixed payoff-score designs for the current
goal. It does not identify whether the primary limitation is the opening-only
information set, the learner, or the risk penalty. Do not lower their thresholds,
invert signs, remove costs, or retune them after these outcomes. A future main
experiment must state a new substantive hypothesis and reserve new comparisons;
the volume study remains auxiliary and does not block that work.

Verification: 119 model/runner tests and five immutable-result tests passed.
The first full regression run passed 3,650 tests; the final post-bookkeeping
regression passed 3,660. The joint v79/v80 focused run passed 165 tests. All 330
v80 and 296 v79 frozen dependency hashes were reverified. Test success verifies
implementation and evidence handling, not strategy profitability.

Independent reports-only review found no concrete false pass or ledger/fill
error. It reconciled 1,448 direct journal rows (312 trades) and 2,883 account
journal rows (612 trades), including the reference, and confirmed training-prefix
hash consistency, twenty estimator fits, costs, sizing, floor and billing
arithmetic, and the six-plus-twelve trial accounting. It did not reopen raw
prices, the holdout or feature/target payloads; the parent's dependency rehash
and original full raw scan are distinct checks.
