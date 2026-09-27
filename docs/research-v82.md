# v82: Lagged Models and Signal-Strength Sizing

Status: COMPLETE at 2026-09-07T04:24:47Z, no Legacy50K development pass. Frozen
at04:16:10Z and started at04:16:21Z. All 245 focused mechanics tests and4003 full
regression tests passed before freeze. All181 raw pairs and402041614 events
passed integrity checks. Original v32 parameter/252-minute-vector checks and
v48/v63 complete account/direct reference journals reproduced exactly. Unit
tests are mechanics evidence, not strategy performance.

Final full regression:4003 passed in138.66s; post-bookkeeping focus54 passed.
Parent report-only arithmetic checks rehashed362 dependencies, reconciled2172
direct rows and2722 candidate account rows (1142 actual trades), checked all
recorded quantile-size decisions, and verified all eight Legacy zero-capacity
paths stayed flat. The additive `completion_audit.json` records scope and limits.
An independent agent confirmed fit/trial/skip counts but did not complete a
full statistics/hash/row audit. Neither review is independent strategy evidence.

## Complete Results

Direct signal diagnostics below are BEFORE account guards and program fees,
AFTER simulated commission, adverse fills and the matched stop. They are not
account cashflow or cash received. Adaptive quantities are the requested sizes;
actual account quantities may be lower, with earlier rule exits or no entry.

| Model and quantity | Baseline net USD | Stress net USD | Baseline max drawdown USD |
| --- | ---: | ---: | ---: |
| Original lagged ridge, fixed1 | 2732.26 | 1355.00 | 2778.66 |
| Original lagged ridge, strength1to6 | 464.42 | 1168.50 | 8809.98 |
| New kernel, fixed1 | -2015.98 | -2005.50 | 2792.76 |
| New kernel, strength1to6 | -2100.68 | -2779.50 | 8510.18 |

All eight Legacy candidate paths (four profiles times baseline/stress) failed
to finish Evaluation; no PA was activated and no payout qualified. EOD's four
adaptive paths numerically passed on attempts5/8 for ridge and4/7 for kernel,
then all closed PA for inactivity. The fixed EOD profiles did not pass. This
does not justify selecting EOD or switching the user's account from results.
All global HAC Bonferroni p-values are1; no independent final validation exists.
Eight outer fits contain59 underlying estimators (51 original alpha-search
fits, four original final fits, four kernel fits); sizing needs zero extra fits.

The important new failure attribution is zero entry capacity. The self-imposed
half-headroom budget and $200 reserve per MNQ require at least $400.01 remaining
headroom to trade even one contract. Once below that amount, all Legacy paths
remained flat at the same balance/floor for the rest of this fixed-stop run.
There was no automatic account replacement because no broker threshold was
breached; monthly subscription units continued. This is a research-policy
dead end, not an Apex prohibition, missing market data or proof of safety.

Ridge fixed1 had125 cap-skipped dates in each mode. Its adaptive profile had
169 baseline and174 stress skips, with only12/7 actual trades despite181
nonflat model intents. Kernel fixed1 had73/74 cap skips in addition to69
model-flat dates; adaptive had96/93 cap skips plus69 model-flat dates. In the
ridge baseline, fixed1 final account balance was48556.76 and adaptive48957.54,
but both failed Evaluation. Higher terminal balance from stopping sooner is
not demonstrated improvement. A bigger fitted score was not reliably a better
trade to leverage. Preserve this result; do not lower cutpoints, widen the
budget, shrink the stop or insert outcome-selected resets into this run.

## Authorization and Comparisons

The user requested signal-dependent position size for their actual Legacy 50K
Tradovate Evaluation. The new v2 authorization supersedes only the previous
two-contract restriction for this new MNQ study. Existing frozen v63/v27
protocols and runtimes are unchanged. No live orders or Telegram sends.

Two models each receive fixed1 and strength1to6 requested-size profiles. Both
profiles share the same account risk caps. This is four candidate policies,
with sixteen conservatively counted comparisons: (three original ridge alpha
choices plus one fixed kernel) times two sizing profiles times two account
families. The cumulative count including the immutable run-start reservation
is12,991 from12,975; the reservation preceded target loading.

The original v32 uses all 616 lagged feature sessions and its original nested
180/10/42 selection. Its four fitted parameter records and original 252-date
minute return vector must reproduce exactly. The new kernel uses 557 sessions
after prior60 warmup, training-only StandardScaler and target centering, RBF
gamma1/8 and ridge alpha100. These constants are a bounded hypothesis, not an
optimality claim. [KernelRidge documentation](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_ridge.KernelRidge.html).

Both generate the same 282-day causal schedule, including 30 previous-fit
bridge sessions. All 181 admitted explicit-pair raw dates are replayed in source
sequence. Controls v48 and v63 must reproduce the complete v81 account and
direct journals and raw scan receipts exactly. Source dates previously observed
are exploratory development, not new independent test data. The final 48-date
holdout stays sealed.

## Sizing Rules

For each outer training prefix, predict with that prefix's fitted model. Rank
absolute scores for nonflat training signals into six equal quantile bins using
linear quantiles. An inference score strictly above each cutpoint adds one MNQ;
ties stay in the lower bin. Fewer than20 active training scores falls back to1.
Flat direction remains flat. Bridges use the previous fitted thresholds.
This is an in-sample magnitude reference, not a calibrated probability or an
unbiased calibration validation. No outer outcomes select a threshold.

The common account cap uses at most half the remaining drawdown headroom,
minus a one-cent threshold margin, and also respects DLL/MAE with a one-cent
margin. Each MNQ reserves $200 for a 96.75-point stop plus conservative stress
costs. The actual quantity is the smallest of the request, six contracts,
conservative plan ceiling, and integer risk capacity. Capacity zero skips the
trade without cost or a counted trade day. This half-headroom ceiling is
aggressive research, not a live-trading recommendation or a loss guarantee.
Stops can gap; unrealized peak giveback can breach the trailing floor first.

Legacy PA initially uses a conservative ceiling of five actual MNQ. A PA EOD
balance strictly above52600 unlocks ten from the next session and latches.
EOD comparison applies two/three/four actual-MNQ ceilings at the published
profit tiers. These deliberately do not multiply micro limits by10; possible
broker capacity is underused, not assumed. The quoted Legacy size, balance
and consistency rules are not replaced by research thresholds.
[Legacy scaling](https://apextraderfunding.com/help-center/legacy-helpful-items/legacy-contract-scaling-rule/),
[EOD PA tiers](https://apextraderfunding.com/help-center/additional-helpful-items/scaling-levels-pa-explained/),
[Legacy consistency](https://apextraderfunding.com/help-center/legacy-helpful-items/what-are-the-consistency-rules-for-legacy-pa-and-funded-accounts/).

## Dynamic Stop Follow-Up

The latest user asked whether volume can make the fixed stop adaptive. Yes:
this is a distinct risk-policy experiment, not evidence that a larger stop
improves this model. Keep the present quantity ablation matched at96.75 points;
preregister a separate fixed-stop versus volatility-stop versus
volatility-plus-relative-minute-volume comparison. Use only completed bars
available before each decision. ATR measures price variability, while volume
is a separate conditioning feature; an increase in volume alone must not
automatically widen the stop. Wider initial stops require smaller quantity at
the same dollar budget. After entry, never widen a stop to accommodate losses.
ATR stop adaptation is described by
[Fidelity](https://www.fidelity.com/learning-center/trading-investing/technical-analysis/technical-indicator-guide/atr).

No adaptive-stop performance or chosen ATR/volume parameters exist yet. The
v79 failed volume predictor ablation does not answer the different stop-policy
question. Count any new stop-policy alternatives before reading their outcomes.

The Korean word for volume in the user's question may instead mean our own
contract quantity. In that interpretation, planned risk links quantity and
stop distance directly: quantity times stop points times point value plus
execution costs. Do not simply tighten an otherwise necessary stop to force
a larger quantity; determine the strategy's causal stop first, then take the
integer quantity affordable under the dollar budget, or remain flat.
[CME position sizing](https://www.cmegroup.com/education/courses/trade-and-risk-management/proper-position-size)
describes the stop-and-budget relation. Its general nominal-equity percentage
examples must not be applied to Apex's nominal50K as spendable risk capital;
remaining trailing headroom and the separate PA/DLL rules are binding here.

Literature context: Kaminski and Lo (2014), *When Do Stop-Loss Rules Stop
Losses?*, Journal of Financial Markets18,234-254, studies portfolio stop-loss
overlays and reports that some rules improve return/volatility at longer
sampling frequencies using daily index-futures data. The
[authors' MIT abstract](https://alo.mit.edu/publications/page/13/)
is motivation for testing risk overlays, not proof that an intraday MNQ ATR or
volume-based stop works, and not permission to transfer its settings to Apex.
