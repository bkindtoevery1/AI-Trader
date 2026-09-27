# v84: Risk-Aligned Absolute Payoffs

## Status And Hypothesis

Implementation completed before outcomes. The previous goal turn made
concrete progress: all122 new focused tests and4245 full regression tests
passed, and a separate read-only model/runner review found no concrete
blocker. This verifies mechanics, not strategy performance.
Frozen384 dependencies at2026-09-07T05:55:52Z. The one-shot run started at
05:56:10Z and reserved16 comparisons before targets; cumulative ledger13039.
Lock SHA256: d406862a5a7fa296a89c07666d73d8ad4191697b1ec26a319332777333e834d4.
Completed at2026-09-07T06:10:56Z, exit0; no partial outcomes were published.
Status: NO_RISK_ALIGNED_PAYOFF_50K_DEVELOPMENT_PASS. All181 raw pairs and
402041614 events were verified, and all eight v83 direct/account controls,
source receipts and execution windows matched exactly. Sixteen multioutput
fits and32 action heads completed; no new risk-model fits.
Legacy50K Evaluation is primary under the user's
newer authorization; the old25K/max2 goal banner does not override it.

v83 changed initial stops while preserving directions trained for a96.75-point
stop and a long-minus-short label. This does not answer whether either side
has a positive absolute expected payoff under the changed stop. v84 tests
that target/feature alignment, not another search over exposed stop knobs.
Flat is permitted when neither estimated action is profitable.

Use multioutput linear Ridge and RBF KernelRidge, both alpha100, each with ATR
and ATR-volume stops and fixed1/strength1to6 sizing. Four model/stop pipelines,
eight new policies,16 outer multioutput fits (32 fitted action heads). No
hyperparameter search or early stopping. Count16 comparisons, bringing the
ledger to13039 only when the one-shot run starts before targets. Repeat all
eight v83 new-policy controls exactly; conformance repetitions are not trials.

Both estimators support two-output regression in their official APIs:
[Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html)
and [KernelRidge](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_ridge.KernelRidge.html).
These are implementation references, not evidence of investment performance.

## Causal Construction

Use the same617 admitted minute pairs ending2026-06-12. The eight verified v82
prior-session/trend features need60 sessions of history, leaving557 feature
dates. Add four preentry covariates: log(paired ATR /0.25), log relative volume,
volume readiness and initial stop points / paired ATR. All current-session
predictors end09:30 ET before the09:31 baseline entry.

Reuse, without refitting, the four sealed v83 kernel risk-prefix calibrations
because their60-session warmup and265/338/411/484 training counts match these
features. This reference is determined by training geometry, not the best
v83 result. Require fresh predictor hashes and all282 inference stop values
to reproduce v83. Within each outer training prefix, apply its fixed risk
calibration to that prefix's training dates to construct labels. This is a
two-stage training procedure, not independent OOF risk calibration. No inner
selection consumes these labels, and no validation range or return enters
either fitted stage.

Training targets are separate LONG and SHORT baseline one-MNQ net PnL divided
by per-contract reserve:50 times stop_ticks plus650 cents. Use09:31 entry-open
and15:55 exit-open, one adverse tick on each side and52c commission per side.
Anchor the protective stop to the slipped entry. Reuse the existing timed
minute-day and protective-stop helpers. Holding intervals include09:31 through
15:54; inspect only the15:55 bar's open for the scheduled exit. Validate
explicit contracts, quarter ticks, OHLC and contiguous ordered timestamps.
Intrabar level fills are minute approximations, not proof of raw stop-gap
fills; final validation remains on ordered Last ticks with stress.

Learn StandardScaler only on the training prefix. Linear Ridge uses SVD and
an intercept; RBF uses gamma1/12 and training-only per-action target centering.
Choose the strictly positive winning action; positive ties and two nonpositive
predictions stay flat. Requested1-6 sizing uses only training fitted positive
winner-score quantiles, with20-active-observation fallback to1. It is not a
calibrated probability or unbiased confidence estimate. Fixed1 is the matched
sizing comparison, with no extra estimator fit.

Preserve the four outer folds,10-session purges,252 scored dates plus30
previous-fit bridge dates, and181 available raw validation pairs. Repeat all
eight v83 control direct/account paths and receipts. Stop, account caps,
baseline/stress windows, costs and actual-contract limits do not change.
Never multiply an account PnL path to simulate larger size.

## Boundaries

Historical nomination and dates are already outcome-informed exploratory
research; no independent confirmation, global DSR recovery or promotion is
claimed. The48-date holdout remains sealed. Keep all frozen sources and
src/aitrader module bytes unchanged. Implement only new tools/config/tests,
then run focused and full tests before freezing. Reserve16 at run start;
publish no partial metrics and do not restart or retune after observation.

No orders, Telegram changes, purchases, secrets, Windows work, schedule
changes, genetic algorithms or account conversion. The goal remains active;
exact program fees, PA plan, planned risk/reward compliance, signal-service
compliance and independent final validation remain unfinished requirements.

## Product Scope

The user clarified that NQ is preferred for its lower commission per dollar
of exposure. MNQ-only v84 is a bounded research design choice, not evidence
that MNQ outperforms NQ or a user prohibition on researching NQ. Preserve this
batch's product and exact controls. Separately assess a matched-dollar-risk
NQ/MNQ hypothesis with actual product ticks and fees; do not multiply an MNQ
account path or shorten a stop merely to make one NQ affordable. No such
comparison has yet run or reserved trials.

## Completed Findings

All eight new candidates fail the unchanged Legacy50K development gates.
No single candidate passes Legacy Evaluation in both baseline and stress.
Linear ATR fixed1 passes baseline Evaluation on2026-02-03, then PA closes for
inactivity after23 actual PA trades and232.08USD PA net trade profit. Linear
ATR-volume fixed1 passes only stress Evaluation on the same date, then closes
for inactivity after33 actual PA trades and152.50USD PA net trade profit.
Neither becomes payout-eligible. These are simulated numerical account paths,
not actual funded accounts, sustained survival, or verified model passes.

The separate EOD comparison has9 numerical Evaluation-pass paths and9 later
PA inactivity closures. Four linear adaptive-sizing paths reach a simulated
first-payout threshold before closure. Eligibility is not approval or cash
received; all actual-payout flags remain false. Do not select EOD from these
outcomes or turn a temporary payout event into a surviving model claim.

Guard-free signal-path net USD after execution costs, before account limits
or program fees; these are not account balances or attainable account profits:

| Estimator | Stop | Size | Baseline | Stress |
| --- | --- | --- | ---: | ---: |
| Linear | ATR | fixed1 | -206.26 | 1691.50 |
| Linear | ATR | strength1to6 | -3649.66 | 2116.50 |
| Linear | ATR-volume | fixed1 | 1050.86 | 3726.00 |
| Linear | ATR-volume | strength1to6 | -1260.60 | 3511.00 |
| RBF | ATR | fixed1 | -4099.24 | -4422.50 |
| RBF | ATR | strength1to6 | 98.94 | -1655.50 |
| RBF | ATR-volume | fixed1 | -3357.74 | -3436.50 |
| RBF | ATR-volume | strength1to6 | 801.32 | -366.00 |

Linear ATR-volume fixed1 ranks first under the frozen exploratory ordering,
but baseline Sharpe0.307 and family-adjusted p0.760 do not pass. Its stronger
delayed stress window is timing sensitivity, not a selectable better entry.
Linear directions produce141/144 active raw dates, not zero-trade rejection.
RBF directions are short on165/167 of181 dates; their training action means
favor short in all four prefixes, but realized raw generalization is poor.
Do not invert or retune the RBF direction from this observed result.

Adaptive score sizing worsens both linear baseline variants; high fitted
scores did not establish trustworthy out-of-sample size allocation. All16
new Legacy account paths encounter risk-cap skips. Their aggregate544 actual
trades and2808 journal rows show populated execution and path-dependent risk
restrictions, not missing data. Target alignment alone did not establish an
edge or a sustainable Evaluation-to-PA route.

The additive numerical cross-check independently reproduces32 baseline/stress
vectors' Sharpe, drawdown, HAC effective samples and baseline global HAC
Bonferroni values, plus the eight-candidate2000-draw block-bootstrap correction.
It uses a Bartlett Toeplitz quadratic form, erfc normal tail and sampled-count
matrix, not the production lag/block-sum algorithms. Source:
`tools/audit_nq_apex_risk_aligned_payoff_v84.py`; result:
`reports/nq_apex_risk_aligned_payoff_v84/numerical_crosscheck.json`, SHA256
54bf6fb42cac9f4da5f9ebd067eca1db55de93a32edfbd1bcd77dc48b5ce3647.
Its16 synthetic tests and104 separate completed-evidence tests passed.
This is independent numerical implementation checking, not independent market
validation or recovery of unavailable global DSR evidence. The48-date sealed
holdout remains closed. Post-completion257 focused integration tests and4365
full regression tests passed (full124.10 seconds). The initial post-result
run found only a stale v83 expectation in an unfrozen central-state test;
after updating the current-version/count expectations the full suite reran.
All384 dependency commitments and181 source metadata records reverified.
Completion audit: `reports/nq_apex_risk_aligned_payoff_v84/completion_audit.json`,
SHA256 ed98cb2920b419cff3b2c1696a9f231c1a6b731cd9430ecb888a6584d8c098a2.
It reconciles5792 direct journal rows,5161 new-candidate account rows and2203
actual account trades. Historical training labels are hash-bound, not freshly
reconstructed by this completion audit; independent strategy validation is
still absent. The research goal remains active.
