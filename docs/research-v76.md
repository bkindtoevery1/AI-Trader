# Apex 25K regime research v76

The user's requests for both new models and extensions of prior research were
combined before any market outcome was loaded. Four policies were implemented:

1. Two-component PLS direction prediction from a new economic-state feature set.
2. Shallow extra trees predicting separate absolute long and short net payoffs.
3. Two-part logistic payoff models combining win probabilities and training-only
   conditional positive/nonpositive payoff means.
4. A fixed 50:50 blend of the new PLS contrast and a v63-style echo ridge contrast.

The new 32-feature information set covers current overnight and opening state,
the previous 20 complete sessions' RTH trend and volatility, activity, and an
explicit contract-roll indicator. Cross-contract price gaps are not treated as
returns. Current features need no price after 10:00 ET. The activity-weighted
OHLC price is a proxy, not exact tick VWAP or order-book information.

## Results

| Model | Baseline USD | Stress USD | Baseline Sharpe | Continuous payout |
|---|---:|---:|---:|---|
| Regime PLS | -1427.74 | -1275.50 | -0.728 | No |
| Absolute-payoff trees | -2394.74 | -2845.00 | -1.117 | No |
| Hurdle payoff | -2910.16 | -3162.00 | -1.656 | No |
| Regime plus echo extension | -1958.84 | -1848.00 | -0.983 | No |

Every candidate failed. None replaces v63 or qualifies as a verified 25K model.
The ledger increases from 12,938 to 12,942 comparisons. No parameter changes,
direction inversions or weighting searches were made after observing results.

Direct PnL uses one actual MNQ with commission and slippage. It excludes account
purchase/activation fees and is not payout cashflow. Account journeys separately
use two MNQ in Evaluation and one in PA, with the unchanged 46.75-point stop and
the existing Apex EOD 25K rule snapshot. No account was actually bought or traded.

## What Changed

Training uses 305/378/451/524 chronological sessions after a fixed 20-session
feature warmup. Four 63-session OOS folds retain the previous validation dates
and ten-session label embargo. These dates were previously observed in other
research, so the result remains exploratory rather than independent evidence.

In addition to the unchanged fold-based screens, account state was carried over
282 available sessions with the 30 between-fold embargo sessions explicitly flat.
The continuous practical screen was declared before outcomes. It still requires
positive predictive/stress evidence, baseline payout and survival, stress PA
survival, and no PA EOD breach. It did not rescue any model.

The initial lock was retired before any market run when a synthetic integration
test found that the fold guard wrongly demanded the old training-start date
despite the feature warmup. The active `preoutcome-v2.lock.json` binds the preserved
initial lock. Validation dates, candidate definitions and scoring were unchanged.

## Failure Attribution

Three continuous baseline journeys reached PA but closed with no PA EOD breach.
The locked engine's only other closure condition is inactivity. Thus these are
inactivity closures, not drawdown breaches or merely short-fold censoring.
The fourth model never reached PA on the continuous path.

Apex's current published PA activity requirement is at least two days with
USD 50 net profit in a rolling 30-day period.
[Official inactivity policy](https://apextraderfunding.com/help-center/billing/inactivity-policy-on-performance-accounts-pa/).
The Evaluation remains a 30-calendar-day assessment with a 25K target of USD 1,500.
[Official EOD Evaluation rules](https://apextraderfunding.com/help-center/eod-trailing-drawdown-accounts/eod-evaluations/).

The embargo-imposed no-trade calendar may contribute to inactivity. It is not
proven to be the only cause, and every direct return series was also negative.
The absolute-tree model's first place in the mechanical ranking is not a
recommendation: its stress PA survived only three observed sessions before the
end of data, so that outcome is right-censored.

## Next Research Direction

The user explicitly excluded genetic algorithms on 2026-09-07 KST. Do not use
genetic search for models, features, hyperparameters or ensemble weights.
Small causal TCN and GRU models remain planning candidates alongside extensions
of the earlier research. Neither neural architecture has been trained in this
cycle. Keep model selection and early stopping inside chronological training
splits, count all comparisons, and preserve the sealed test and deployed v63.

Extend prior research by separating **training-label purge** from **trading
shutdown**. A previously fitted model can remain causal while issuing signals
during dates whose labels are withheld from the next fit. Any such experiment
must be a newly counted and separately frozen policy, not a rewrite of v75/v76.
Do not relax Apex activity rules or reinterpret the failed models as passes.

Implementation: `tools/run_nq_apex_regime_research_v76.py`.
Evidence: `reports/nq_apex_regime_research_v76/`.
The v63 deployment and sealed historical/prospective data remain unchanged.

## Methods

- [PLSRegression documentation](https://scikit-learn.org/1.9/modules/generated/sklearn.cross_decomposition.PLSRegression.html).
- [Probability calibration documentation](https://scikit-learn.org/stable/modules/calibration.html). The hurdle probabilities are not claimed to be independently calibrated; no random calibration folds were used.
