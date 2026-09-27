# V114 Pair Context

Declared September13 2026 UTC before new pair-feature extraction, fitting or
account replay. This is a finite outcome-informed development experiment, not
an independent validation. V113 is closed and is not refitted or rescued.
Policy: config/nq-apex-pair-context-v114.json. Implementation and source
qualification must precede an exclusive market claim; declaration is not a run.

## Hypothesis

The existing MNQ model predicts its own execution payoff from nine NQ-derived
event coordinates. V89 already decomposed hit probability/payoff, V94 compared
dollars with unit-R, V99 added efficiency, and V111 tested21-bar OHLC ordering.
V112 used global residual bias and V113 original-score-only affine calibration.
Another normalization, generic sequence network or threshold change is not the
new question. V114 asks whether contemporaneous **own-product context**, which
those predictors do not contain, explains residual MNQ execution economics.
This is not an asserted failure cause, arbitrage edge or assured improvement.
Paired predictors in general are not new: V32 used NQ/MNQ session efficiencies
and V63 a paired opening sequence. The bounded precedent review found no exact
Last-gap/age/print-count treatment, not proof of an exhaustive novelty search.
V114 is V112's learner/target with three new covariates, not a new learner family.
Their bundled contribution is tested; individual causal effects are not identified.

## Fixed Inputs

For each original completed NQ event at D, consume only original-sequence Last
records in [D-60seconds,D) from its same-expiry NQ and MNQ raw pair. A print at
D is excluded. Equal timestamps use the final original sequence before D.
Both products must have at least one print; insufficient coverage aborts the
attempt, never drops a row, imputes zero, or falls back to the reference.

The three added coordinates are:

1. signal*(last_MNQ_ticks-last_NQ_ticks)/known_stop_ticks.
2. (D-last_MNQ_timestamp_ns)/60,000,000,000.
3. log1p(MNQ_window_print_count)-log1p(NQ_window_print_count).

Prices remain integer ticks until subtraction. No postdecision geometry,
fill, outcome, quote depth, bid/ask classification or future observation enters
the features. Print count is neither contract volume nor signed order flow.
Separate same-product collector copies cannot become extra observations.
The source loader owns full file/sequence/provenance authentication; a feature
receipt only binds consumed supplied prefixes. Historical exchange/event time
does not establish that a live feed delivered every print before the decision.

## Estimation

Reuse exactly the V112 purged prior-vintage OOS residual populations: first42
scored dates pass through the original; folds2/3 calibrate only admissible past
original forecasts and mature labels. Never repredict old rows with the current
HGB or feed candidate forecasts into its own training history. Keep the full
exchange-calendar ten-session purge and original per-date equal event weights.

Fit one training-only StandardScaler on the three new coordinates per later
fold. Constant coordinates have scale1. Fit sklearn Ridge(alpha20,solver=svd,
fit_intercept=False) to original_target-original_forecast using columns
[1,standardized_pair_coordinates] and the same date weights. All four columns,
including the intercept, are penalized. Two multioutput estimators learn32
coefficients total. The original forecast's coefficient remains exactly1;
there is no score inversion, score-slope fit, clipping, grid or early stopping.
Output units remain reference-exposure USD, not current-account payoff.

Compare three complete arms: exact original, exact saved V112 bias correction,
and the pair-context candidate. V113 is failure history, not an additional
selectable comparator. The single conditional Ridge shares parameters and
weights with the global-bias mechanism but adds genuinely new covariates.
It need not improve; a predictive diagnostic cannot substitute for economics.

## Economic Test

Preserve181raw pairs,126scored dates,12continuous books and1,512scheduled days.
The unchanged NQ Evaluation routes to MNQ PA with actual risk-limited sizing,
all four execution modes, costs, latency, stops, nominal guard, cooldown,
inactivity and payouts. All-four-positive nomination is unchanged. Restore
eight saved controls and four candidate Evaluation prefixes exactly.

Both candidate-minus-original and candidate-minus-V112 must improve PA net in
baseline AND combined stress without added hard/MAE breaches or earlier
inactivity. Absolute positive PA and full-route/payout gates remain separate.
Do not call avoided losses, MSE improvement or Evaluation alone a pass.

Charge three comparisons before fitting (13,190 to13,193), never on a mere
synthetic test or design declaration. No partial economics or scored loss is
published. All48holdout dates stay closed. Missing context is a data/input
failure, solver error an implementation/numerical failure, and valid zero
nominations an economic/model result. Preserve these distinct causes.
No Windows activation, operational model replacement, orders or Telegram test.

## Sources

CME documents NQ and MNQ as separately specified E-mini and Micro contracts;
that relationship does not prove this proposed timing/payoff hypothesis:
https://www.cmegroup.com/articles/faqs/frequently-asked-questions-micro-e-mini-equity-index-futures.html

The learner uses the established weighted Ridge objective and SVD solver:
https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html

No marketing, course-sales or clickbait source is used as model evidence.
