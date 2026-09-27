# v93: Fixed Family-Regime Payoff Interactions

## Authority and Purpose

This document and `config/nq-apex-family-regime-v93.json` become immutable
dependencies of the v93 preoutcome lock. This is outcome-informed development
on previously observed dates, not a new independent test or a verified account
pass. The manual user authority is Apex Legacy 50K Tradovate Evaluation.
Operational v63/v92 paper accounting is separate and cannot change this design.
The final 48-session historical holdout remains closed. No genetic algorithm,
hyperparameter search, model inversion, postoutcome retuning or order is allowed.

## Single Hypothesis

v92 used additive family membership with shared regime slopes. Add exactly
three interactions to its unchanged nine causal predictors: `w*s`, `w*v`,
`w*b`, where `w` is wick-family membership, `s` is signed slope/ATR, `v` is
log relative volume and `b` is log previous bandwidth/preceding20 bandwidth
20th percentile. Form products before scaling. All predictors, including
volume normalization, are available at the decision time; no future bars or
held-out data may supply warmup. The two unchanged families are band reentry
and wick rejection. Keep every v92 broad opportunity, direction, stop, target,
decision time and cost mode unchanged.

Fit one date-weighted StandardScaler and multioutput Ridge(alpha=10,
solver="svd", fit_intercept=True) per product and fold. Each training event
date contributes total weight one, divided equally among its events. The four
heads predict net R for baseline, cost-only, latency-only and combined stress.
An event is selected only if all four predictions are strictly positive.
The identical selection mask feeds all four execution modes.

## Schedule and Counts

Use the exact sealed v92 181 explicit-contract raw pairs, September 8, 2025
through June 12, 2026: 55 initial warmup dates followed by three contiguous
42-session scoring folds. Training expands chronologically. Purge the ten
full-calendar sessions before each scoring fold using the exact 617-session
source calendar, not the sparsely available raw-date index. Require complete
counterfactual labels for every training opportunity and all four modes,
resolved before the first embargo session's predictor window. Both product
training inputs must validate before either product's fold fit.

The fixed comparison family has six policy/product members:

- Primary family-regime NQ and MNQ.
- C1: exact previously frozen v92 broad-policy predictions, NQ and MNQ.
- C2: date-weighted training means derived from primary fit metadata, NQ and MNQ.

Reserve six comparisons before any new fit or raw replay: inherited 13,091
becomes 13,097. Actual new work is six estimator fits, six scaler fits and
24 output heads. C1 loads six historical fits with exact training-lineage
and prediction hashes; it never refits them. C2 derives 24 scalar outputs
without another estimator or scaler. Controls are counted comparisons, not
eligible primary candidates. Neither a zero-fit structural abort nor the
training means may be misreported as new estimator fits.

## Preflight Before Outcomes

Freeze source dependencies, package versions, supported single-thread runtime
pools, executable catalog and this design before predictor-only preflight.
Inherit exactly the 509 dependency paths recorded in the hash-pinned completed
v92 lock, rehashing every file and verifying the current v92 policy, catalog,
environment and supported runtime pools. Do not re-expand ancestral filesystem
globs: two unrelated operational-paper modules added after v92 are not members
of its frozen closure. No frozen dependency is removed or changed. Use the
unchanged v78 metadata-only raw-envelope loader and require its entire manifest
to equal v92's pinned source metadata. New v93 dependencies are separately bound.
Require the inherited minimum 40 events and 20 event dates in every training
fold, 20 distinct dates for each family per fold, and at least 30 scoring dates
with structural opportunities. Also require at least 30 scored dates per
product with an event affordable from the initial unchanged account risk
state. This last check uses only stop size and fixed cost reserves, not trade
outcomes, and does not prove subsequent path-dependent affordability.

Check that all three added columns supply independent training information.
Using date weights, center and population-scale all 12 columns (zero scale
becomes one), append an intercept, and multiply rows by square-root weight.
Residualize added columns against the retained nine plus intercept with
`numpy.linalg.lstsq(rcond=1e-10)`. All three residual singular values must be
strictly greater than `1e-10 * max(1, largest full-design singular value)`.
Report singular values and family support. No labels, scaler estimator fit,
Ridge fit or performance metric is allowed at this stage. A failed structural
gate closes this version; it is not relaxed after seeing feasibility.

## Paired Prediction and Execution Tests

Score prediction MSE on every common opportunity, not only selected trades.
Average squared errors within each nonempty event date, then weight dates
equally. Empty dates are not zero errors. Evaluate all four modes separately.
For each product the primary must beat both controls on the equal-four-mode
average in at least two of three folds and pooled. Its pooled baseline and
pooled stress MSE must each also beat both controls strictly. These are
descriptive, preregistered development comparisons, not independent p-values.

Replay direct diagnostic and continuous account paths separately. Keep NQ
at most one and MNQ at most six actual contracts, inherited stop-risk sizing,
half-headroom reserve, inclusive breach floor, commissions/slippage, common
absolute exit decision+5,460 seconds, cooldown 300 seconds and no daily fill
cap. A paper notional increase cannot substitute for affordable execution.
C1 must exactly reproduce both products' four-mode direct journals and
continuous account reports, all original raw receipts, window receipts,
counterfactual labels and predictions. Any mismatch is an integrity failure.

Keep the inherited practical screens: at least 30 baseline active dates,
baseline HAC effective samples at least 84, baseline Sharpe at least 0.5,
positive stress Sharpe and positive direct net in all four modes, and
six-policy family block-bootstrap p <= 0.20 (2,000 samples, block10,
seed20260993). Require baseline and stress Evaluation success. PA survival,
payout and complete route are separately reported, not inferred from
Evaluation. Both paired prediction and account screens must pass for a
development shortlist. No outcome is a verified 50K pass; program fees,
liquidity, operational compliance and future confirmation remain limitations.

## Execution and Completion

Use exclusive immutable preflight/run claims. No rerun after a claimed failure,
partial metric exposure or optional stopping. Reverify input and dependency
hashes before and after the one-shot run. A process timeout is not permission
to start another run. Persist outcome-free product/fold receipts for model,
scaler and estimator starts/completions. Starts are invocation intents, not
proof of completed fitting; absent acknowledgements remain unknown after a
crash. Terminal failures record completed lower-bound counts and the exact
publication stage, including whether a complete status became visible before
result-seal failure. Never describe an exposed status as unexposed. Publish
outcomes only after the complete schedule,
21 exact predecessor comparisons, fit counts, paired diagnostics and account
screens finish. Seal results and audit completion independently. Record
failures and actual attempts centrally; synthetic tests prove software behavior
only. Preserve every predecessor's immutable bytes and sealed holdout.
