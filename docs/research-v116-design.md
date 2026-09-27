# V116 Prequential Cross-Product Forecast Stacking

Declared2026-09-22 after the audited V115 failure, before new source preparation,
fitting or model outcomes. One outcome-informed development candidate. Preserve
V115's46immutable outputs and its additive prose/metadata erratum. The ledger
remains13,196 until a qualified runner makes a separate exclusive claim.

## Question And Precedents

V110 blindly used NQ forecasts to nominate MNQ PA trades and failed both primary
comparisons. V113 learned a monotone map of only the original MNQ forecast;
both later stress slopes collapsed to zero and PA never traded. V115 appended
raw pair-context features to a direct HGB but failed both joint comparisons.
Test whether the ORIGINAL NQ forecast contains conditional information about
MNQ reference payoff beyond the original MNQ score, using a learned cross-product
combination rather than unconditional selector transfer or another HGB fit.

This is supervised forecast stacking, not a new learner family, independent
models/markets, or proof of useful diversification. Both models share event
features and training dates. Adding a correlated column also changes ridge
regularization geometry; the contrast does not isolate pure information gain.
Independent read-only V75-V104 review found no exact prior-OOS two-product score
calibrator, but generic OOF stacking was already proposed in the design-only
research-ensemble-reuse-plan.md. V75/V76 used fixed same-product blends; V89/V90
changed payoff decomposition/shared execution-mode slopes; V98 routed products
without learning; V101/V102 selected HGB settings through account utilities.
This is a narrow mechanism extension, not a claim that stacking is new here.

## Fixed Model

Reuse the V112/V113 original-MNQ prior-outer-OOS calibration population. Keep
all eligible mature original labels, including true zero labels, before the
original causal reference-capacity filter. Keep date-equal target weights,
three42-date outer folds and ten FULL exchange-calendar purge sessions.
No current-fold label, candidate history, final model backprediction or
surviving-account-only sample enters calibration. First fold is exact original
MNQ passthrough with no new fit. Only folds2and3 are fitted.

For mode m, let p be the original MNQ forecast, q the original same-event NQ
forecast and u the original MNQ fresh-Evaluation-reference-exposure USD target.
NQ q retains its own original dollar units: do not divide it by ten or pretend
it is the PnL of a current MNQ position. The learned coefficient handles units.
Fit

    prediction = p + a + b * z_M + c * z_N
    loss = sum(w * (u - prediction)^2) + 20 * (a^2 + b^2 + c^2)
    b >= -s_M, c >= 0

z_M=(p-mean_M)/s_M uses the exact V113 training transform. z_N=(q-mean_N)/s_N
uses the same target weights restricted to available NQ forecasts for its
training-only moments. Missing NQ forecasts contribute z_N=0, meaning no NQ
correction, not an observed zero-dollar q or a zero target. Keep the availability
mask and validate every source forecast/event pair before retaining MNQ rows.
Do not drop rows, renormalize target-date weights or learn a missingness gate.
The source must prove NQ availability equals its causal known-stop reference
capacity, not a future entry/exit outcome. Constant/absent NQ columns use scale1
and z_N=0, with coefficient exactly0. No scoring values enter either transform.

The total own-score slope is1+b/s_M>=0, and the available NQ score slope is
c/s_N>=0. These constraints cannot turn either signed forecast upside down.
Missing NQ uses the jointly fitted own term, not a claim to reproduce V113's
fallback. Intercept and slopes are not probabilities or position sizes.
Use the centered prediction form to preserve an exactly zero own slope without
cancellation; no epsilon, clipping, direction inversion or threshold adjustment.

Use scipy.optimize.lsq_linear with dense sqrt-weighted observations plus three
sqrt(20) penalty rows, method=bvls,lsq_solver=exact,tol=1e-12,max_iter=100.
Independently verify feasibility and convex KKT conditions against the original
matrix/targets. A nonconverged/nonfinite or inconsistent fit is a technical
failure; no alternate optimizer, seed, penalty or retry. The fixed20 comes from
V112/V113, not a new grid. At most8scalar fits learn24coefficients, with two
new NQ-forecast transform groups; original HGBs and original feature scalers
are never refitted. Caller-owned durable fit-stage receipts remain mandatory.

## Source And Comparison

Authenticate all six original source HGBs, both complete original forecast
sets, original labels, exact same-event IDs/times and original causal vintages.
Bind the current and prior NQ model hashes alongside the unchanged MNQ plan.
Self-computed array hashes alone are not source admission. Reuse the archived
original forecasts, never recompute past q with the current NQ fold model.
If all added columns are structurally constant, close as redundant before any
market claim instead of inventing a redundant trial. Report per-fold/mode
availability and constant-column support without inspecting scoring outcomes.

Three continuous arms: original V107-repair MNQ reference, exact completed V113
monotone calibration, and new cross-product stacking. All retain original NQ
Evaluation and change MNQ forecasting only after each own next-date PA start.
Keep stops<=140, actual5:1guard, half-headroom sizing, NQ<=1/MNQ<=6with stricter
plan caps, original brackets, four cost/latency modes, uncapped fills and300s
cooldown, cash transitions, activity, billing and payout rules. No forced trades.

One full181raw-pair/126scored-date replay has12books/1,512scheduled account-days.
Verify eight full original/V113 controls and four candidate Evaluation prefixes.
Both candidate-minus-original and candidate-minus-V113 must improve PA trading
net in BOTH baseline and combined stress, with no added hard/MAE breaches or
earlier inactivity. Absolute-positive PA, observed survival, payout and full
route remain separate. Cost-only/latency-only and lower prediction error cannot
rescue failed primary economics. A shared Evaluation pass is not new success.

One candidate plus two primary contrasts charges3only upon a genuine claim:
13,196to13,199. Component tests/source readiness alone charge zero. No actual
market fit before source/code admission, independent review, focused/full
qualification and a frozen run lock. No partial outcome publication, optional
stopping, restart or post-result calibration. Restore source forecasts and
independently reproduce recorded-account arithmetic after terminal completion.

## Limits

This still learns reference-exposure dollars, not evolving PA headroom utility.
Prior-vintage errors may not transfer to the current model. Historical adaptive
reuse, unpriced program fees and unverified personal Legacy cohort remain.
Keep48sealed holdout dates closed. No official50Ksuccess, Windows deployment,
Telegram, orders, spending, schedule or heartbeat change is authorized here.

The [SciPy bounded least-squares documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.lsq_linear.html)
supports the convex solver and KKT checks, not a trading-edge claim.
