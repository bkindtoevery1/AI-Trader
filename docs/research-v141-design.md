# V141: Normalized Ridge On Giveback Unit Cash

Declared October 7, 2026 after the complete V140r1 result, before any V141
market fitting or predictions. This is outcome-informed historical development,
not new independent evidence. Windows V63/V92 operation is unchanged and remains
the immediate operational priority. Qualification on invented arrays is allowed;
market execution requires separate complete-source qualification and reservation.

## Question And Precedents

V140 matched one-contract training cash to its giveback exit but failed baseline
PA survival and stressed Evaluation. Both products' errors exceeded their
training-mean diagnostics in all four modes. Fold 3's nominated opportunities
lost in every mode for both products. Target alignment did not establish a
conditional advantage. Capacity was also binding: 179 of 200 stressed zero-size
attempts could not fund one NQ even using the entire recorded headroom. This
does not justify increasing risk or pretending that skipped opportunities won.

Test one fixed, substantially regularized linear mapping on the SAME V140
18 inputs and giveback-unit targets. The primary comparator is the exact saved
V140r1 HGB, not an older target or feature set. This isolates the learner change.

This is not a new algorithm family. V90 traded ridge and failed stress; V126
screened alpha-10 ridge on twelve original-exit features; V131/V132 learned
terminal movement for confirmation, not this executed cash target. V113 and
V116 calibrated prior forecasts and abstained. V129/V130's simpler hurdle model
improved forecast MSE but failed the account route. Those failures remain
counterevidence, not erased by a new version number.

V93/V94 already evaluated mean policies, with no successful route. V140's saved
24 fold/product/mode means are all negative; unchanged all-four-positive
nomination would necessarily abstain. Retain them as diagnostic forecast
controls, not another mean-policy account replay.

## Fixed Learner

Use sklearn Ridge, solver SVD, unpenalized intercept, one joint four-response
fit per product/fold. Let native sample weights be original date-equal weights
divided by their training-only mean. Set alpha to their sum, without a search.
For each standardized response the objective is:

`sum_i(w_i * (y_i - intercept - x_i @ beta)^2) / sum_i(w_i) + ||beta||^2`

This fixes effective lambda at 1 as training prefixes grow. V126's constant
alpha-10 sum-loss objective did not have this invariance. Both X and Y use the
same training-only weighted StandardScaler convention as V140. All eighteen
feature floats, four net-cent targets, retained event IDs, date weights and
support masks must be identical to V140 before a fit is allowed. Preserve
constant columns and outputs; no feature deletion, clipping or threshold tuning.

Return unrounded float64 own-product one-contract cents in baseline, cost-only,
latency-only, stress order. Preserve signs during cents-to-dollars conversion.
Six product/fold pipelines mean six multioutput ridge fits and twelve scaler
fits. Record each actual native start, completion, failure and warning. Do not
count four response coordinates as four separately fitted Ridge estimators.

## Chronology And Execution

Keep all 181 development dates, mature 45/87/129-date training prefixes, ten
purged sessions and three 42-date scored blocks. No scoring label enters
preprocessing or fitting. Preserve empty query dates and all 48 closed holdout
dates. Later folds may use only earlier now-mature development observations
under the unchanged chronological protocol. These reused dates remain reused.

Durably publish all 252 candidate product/date forecasts before diagnostics or
account replay. Reuse authenticated V140 giveback labels and completed controls;
do not re-extract labels, refit the HGB or replay its four books. The candidate
must receive the same source admission, minute features and original raw-tick
execution windows. Component tests do not substitute for this integration.

Four new books retain the exact V136 route: original NQ Evaluation to MNQ PA,
all-four-positive nomination, long/short support, integer size caps, dynamic
geometry, half-peak giveback, costs, delay, account guards, cooldown, withdrawals
and modeled lifecycle rules. Raising the contract ceiling or loosening PA
activity rules is not part of this experiment. Simulated activity closure means
insufficient qualifying profitable days, not simply no trades. Official current
account-cohort compliance and program fee prices are not inferred from this
frozen historical engine.

## Outcomes And Falsification

Show date-equal MSE against BOTH the exact V140 HGB and training mean for every
product, mode and fold, plus the pooled values. Report all-four-positive counts
and selected label means without treating overlapping opportunities as account
PnL. Be explicit when lower MSE comes from predictions that never nominate.

Failure to improve over the mean undermines conditional forecasting value;
smaller errors alone cannot establish trading benefit. The unchanged absolute
baseline-and-stress full-route gate remains primary: Evaluation pass, modeled
PA survival and the original payout/positive-PA requirements. A failed route,
abstention or merely fewer losses is not a pass.

Keep relative PA profit differences null whenever either book never reaches
PA. Report categorical full-route improvement separately from matched PA profit
benefit; V140 stress never entered PA. Do not invent a zero-profit control PA or
change missing-value rules so a candidate wins. No current live promotion or
verified real 50K pass follows from an historical development result.

Plan seven comparisons: two product candidates, four fixed forecast contrasts
(each product versus HGB and mean), one whole-account route contrast. None is
reserved yet; effective trials remain 13,277. An eventual qualified reservation
would make 13,284. No grid, seed sweep, fallback learner or post-result rescue.

## Required Component Evidence

Before source integration, independently solve the weighted centered normal
equations on invented arrays and match sklearn predictions. Test nonuniform
weights, uniform weight rescaling, duplicated observations with proportional
alpha, constant/collinear features and constant responses. Keep exact cent,
boolean/nonfinite/shape rejection, empty-query output, metadata isolation,
single-thread execution and actual native failure journaling. All market
source, trained models, ledgers, Windows tasks and Telegram state stay untouched
by this component work.

