# v91: Execution-Scale Feature Ablation

## Hypothesis And Limitation

The completed v90 reduced cross-mode contrasts without changing v88's common
prediction. Its more frequent trades did not pass Legacy50K Evaluation, and
both main risk-guarded stress accounts lost money. Do not retune that outcome.

v88 has six dimensionless shape/volume/time covariates, but no direct absolute
stop/volatility-scale covariate, not the absolute index price level. With a completed stop of s ticks, tick value V cents and
commission C cents per side, nominal round-trip commission divided by stop risk
is 2C/(V*s). A fixed S adverse ticks per side similarly contributes 2S/s when
both fills are compared to their raw ticks. This motivates ONE added predictor,
1/s, not an exact correction to realized PnL. Slipped-entry brackets, target
admission, gaps, account guards and latency make execution path-dependent; a
zero-fill label incurs no round-trip cost. The explicit filled-path deductions
are2.62/s and9.40/s for NQ,4.08/s and13.00/s for MNQ in baseline/cost-stress.
They are identities on that mode's actual path, not cross-mode translations.
Never subtract hypothetical costs
from skipped labels or assert baseline must dominate stress on every trade.

Scaling a valid completed price path and ATR by an integer can preserve the six
original ratios, family and clock while changing stop size. Rounding can spoil
exact invariance for arbitrary scale factors; the nonredundancy demonstration
must use compatible integer-tick examples. This is an information ablation,
not a larger data set or an independently discovered strategy. v84 used ATR
scale in different preopening features/stops/labels; it did not isolate this
missing scale on the frozen intraday v87 opportunities. This is not the first
use of stop-scale information anywhere in the project. There is no evidence
yet that its omission caused previous losses or that restoring it will help.

Wider stops lower explicit cost/R but require more dollar reserve and can
trigger RISK_CAP_FLAT. Actual account capacity and later opportunity cooldowns
must be replayed; independent unit-contract labels cannot settle this tradeoff.

## Fixed Design

Add inverse_stop_ticks to the exact six v88 features. Train separate four-mode
multioutput Ridge for NQ and MNQ using alpha10, SVD, unpenalized intercept and
training-only weighted StandardScaler. Every event date has total weight one,
split across all its events, including rejected and zero-fill counterfactuals.
Each event supplies four correlated targets, not four independent samples.
Use the strict v89 complete journal/identity/clock checks without its irrelevant
hit-branch support gate. No score clipping, cost-sign constraints, target
translation, parameter search, signal inversion or outcome-selected sizing.

Compare two execution-scale product policies to two exact v88 product controls.
The controls have six features, not an artificial all-zero seventh dimension.
Three expanding folds give six new estimators and six exact control estimators,
12 total fits and48 learned heads, zero derived heads. Four counted comparisons
raise13083 to13087 only at the once-only run claim before labels. Controls are
counted diagnostics, not new nomination candidates or independent discoveries.

Use617 full-calendar dates and the same181 admitted explicit-contract raw pairs,
55 warmup and126 scored dates in three42-date folds. Purge the preceding10 full
exchange-calendar sessions, not10 sparse raw dates. Require40 training events
on20 event dates per fold and30 structurally possible scored event dates before
any replay. These lower bounds are feasibility checks, not power guarantees.
Predict every scheduled event before reading that date's outcome tape. Folds
do not reset a simulated Evaluation/PA account. Keep final48 holdout dates closed.

Unchanged v87 quiet-late reentry/wick union, chronological nonoverlap,300-second
cooldown and no daily fill cap. Same completed1.5ATR stop, fixed mean target,
60/240-second entry delays and common decision+5460-second exit. NQ requests1,
MNQ up to6 with exact own-product ticks, fees, integer risk limits, DLL/MAE and
Legacy Evaluation-to-PA behavior. Separate baseline, cost-only, latency-only and
stress paths share the same all-four-positive prediction mask. No execution
parameter changes or claim of equal dollar exposure between products.

Keep baseline Sharpe>=0.5, stress Sharpe>0, positive signal PnL in all four modes,
at least30 baseline active dates, baseline HAC effective samples>=84, four-policy
block-bootstrap p<=0.20 (2000 draws, block10, seed20260991), and numeric Evaluation
success in baseline and stress. Assess PA survival/payout separately. Exact
program fees remain unpriced; numerical Evaluation is not approval or payout.

Report day-weighted all-opportunity per-mode squared losses versus each prefix's
mean and the exact v88 forecast, including unselected/unfilled events. Report
training inverse-stop ranges and scoring extrapolation counts. These are
diagnostics only, with no subrange selection, clipping, retuning or thresholds.
Loss improvement alone is not a development pass. Additional coefficients can
overfit the sparse, serially dependent opportunity dates, or extrapolate badly.

## Evidence And Operations

Preserve all frozen v90 bytes and require its completed seal/477 dependencies.
Extend the lock to this design, policy, model, runner, tests and immutable v90
stage/result/audit/completion evidence. Focused tests, full regression and a
separate design review precede freeze. Use one structural preflight, one run
claim,21 exact v88 source/control checks and atomic result publication. A lock
is reproducibility evidence, not recovery of unavailable global DSR evidence.
Repeatedly observed development dates remain outcome-informed exploration.

No genetic algorithms, purchases, account conversion, live orders, Telegram
sends, secrets, Windows/network work, unrelated schedules, frozen runtime edits
or human Replay Lab record changes. Current main authorization is Legacy50K;
older EOD25K/max-two protocols remain history, not the current account target.

Implementation reference: scikit-learn's official
[Ridge API](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html)
documents the weighted multioutput regression used here. This is not evidence
that the feature or trading strategy will be profitable.
