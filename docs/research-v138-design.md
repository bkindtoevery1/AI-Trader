# V138 Direct Transition Utility Learning

October 7, 2026 KST. Outcome-informed development design, not independent
validation, a current-cohort Apex pass or deployment permission. Market fitting
is NOT authorized until the complete source adapter, immutable runner, tests,
dependency pins, publication and comparison reservation are complete.

## Question

V137's cash-plus-headroom arm nominated two of 3,682 baseline queries and made
one trade per mode. Its separate cash heads have date-equal pooled MSE above
the training-mean anchor in every product/mode; the floor heads have lower MSE.
That anchor is not state conditional, so floor error improvement alone does
not establish useful market information. See the completed
[V137 record](research-v137-performance-audit.md#completed-market-run).

Test whether fitting the declared one-step score directly is a better finite-
sample estimator than combining two separately fitted response heads. Keep
the economic objective exactly `U = 2 * cash_delta - floor_delta`, in cents.
This is cash change plus headroom change, not continuation value, a learned
risk preference or a new source of market information. Conditional expectation
is linear: without prediction projection, its population mean equals twice
the cash conditional mean minus the floor conditional mean. Finite HGB trees
can choose different partitions when trained on this combined target.

This distinction matters because V106/V118 utility transforms, V113 score
calibration, V116 blending and V117 baseline-only nomination already failed
their economic tests. In particular, more nominations are not success and
V117's extra PA trading made every mode worse. V138 changes estimation only;
it does not drop a blocking mode, change the unit floor penalty, shift the
positivity threshold, promote V137 cash-only or relax execution costs.

Prediction loss need not match the downstream decision objective; this is a
general motivation in Elmachtoub and Grigas,
[Smart Predict then Optimize](https://arxiv.org/abs/1710.08005). V138 is NOT an
implementation of SPO/SPO+ or reinforcement learning. That paper's consistency
results do not establish a trading edge, a sequential account guarantee or
validity for this reused historical population.

## Learner And Population

Use the exact authenticated V137 counterfactual labels and original broad-event
census, without replaying raw ticks or selecting its executed trades. All
181 development dates, the 45/87/129-date training prefixes, ten-session purges,
126 scored dates and 48 unopened sealed dates remain unchanged. Every state and
mode replica of one event stays with its original date and maturity cutoff.
Previously scored dates may enter later expanding training prefixes, never an
earlier fit. Reused development dates are not new independent evidence.

Retain the original 15 causal market features, four known account coordinates,
six NQ and 26 MNQ numerical state anchors, source support exclusions, genuine
zero labels, exact costs and V136 giveback execution. These numerical anchors
are not independent observations or certified reachable account paths. Each
nonempty date has unit mass, each supported event equal mass within its date,
and its replicas split that event's weight. Estimator mass remains original
event count; minimum leaf rows remain `50 * replicas`.

Fit six product/fold pipelines. Each contains two training-only scalers and
four HGB response heads, one per unchanged cost/latency mode: 24 response fits
and 12 scaler fits, 36 native fits total. Use squared error, 100 iterations,
learning rate .05, seven maximum leaves, L2=10, random state 126, no early
stopping and one native thread. Do not tune these values. Validate the original
eight integer-cent labels before deriving the four direct targets; reject
overflow, impossible floor increments or lost exact-cent representability.
Do not encode the utility score as fake cash/floor predictions.

## Matched Forecast Comparison

Restore the exact six V137 model artifacts without refitting. On every supported
grid query, compare the direct candidate to the raw V137 score `2*cash-floor`.
Also report V137's deployed projected-floor score separately: projection makes
that comparator nonlinear and prevents calling every difference a pure linear
estimation effect. No projection toggle is selected after observing results.

Add a training-only state-conditioned arithmetic mean as a diagnostic anchor.
For each fixed state and original response, average supported events equally
inside each nonempty training date, then average dates equally. Derive its
utility mean with the same fixed formula. It uses no market features and is
defined only at the exact declared state anchors, not an interpolated account
policy. Six sets of means are estimated; they are not six extra independent
samples or deployed strategies. Keep the unconditional training-mean anchor too.

Report raw combined-target MSE/MAE for every mode, product and chronological
fold, with equal mass per nonempty scored date. Preserve all empty dates with
null loss. Give state-level diagnostic breakdowns without selecting a state,
mode, product or fold. The comparative errors and nomination counts are
descriptive; do not add overlapping labels into an account equity curve.
Publish the entire fixed forecast census before joining scoring labels.

Plan four forecast comparisons before any market fit: NQ and MNQ direct versus
raw separate-head utility, and NQ and MNQ direct versus the state-only anchor.
This forecast stage is not an economic pass or a basis to replace a live model.
The separately specified account comparison below adds one planned comparison,
for five total. The charged comparison total is still 13,262: V138 is not yet
reserved or market fitted. Account and forecast comparisons are dependent, not
five independent experiments or a reconstructed global DSR count.

## Economic Follow Through

A separately declared whole-account execution stage is still required, whatever
the forecast error result. It must use causal own-account state, all four direct
scores strictly above zero, known-zero-capacity bypass, original NQ Evaluation
to MNQ PA routing, at most one NQ or six MNQ, actual support, busy/cooldown rules,
all execution stress modes, and the unchanged lifecycle and risk guards.
Report comparison with the frozen V137 route and the projection distinction.
No loss threshold, quantity, time window or payout rule is weakened.

The exact account reference is the saved V137 cash-plus-headroom route, in all
four modes. It remains its real projected-floor policy, not a reconstructed raw
score policy. Authenticate those saved bytes and reconcile their journals; do
not fit or replay the predecessor again. The candidate has four new account
books, with raw ticks and its own evolving state. The raw separate-head forecast
comparator is diagnostic only. Eight reported books are not eight new fits or
eight independent samples. Unequal PA exposure is explicit and an absent PA
contrast remains null rather than zero profit. There is no MSE-based early stop.

Full-route evidence still requires baseline and stress Evaluation, positive
PA economics, observed survival, hypothetical payout eligibility and no hard
or MAE breaches. Program fees and current-cohort compliance remain separate
unresolved requirements. No continuation value, independent validation, live
orders, successful account or actual payout is claimed by this component.

## Execution Boundaries

Authenticate predecessor claim, result seal, terminal, completed supervisor
audit, every label/model hash and frozen source/runtime before reusing bytes.
Source restoration is the established V123 route, not renewed independent
provider authentication. Keep all original failures and supersession evidence.
Retain durable native-fit attempts, all warnings and a single immutable result;
recompute predictions and summaries in a no-fit saved-result audit. No automatic
retry, interim result selection, threshold rescue or sealed-date access.

No Windows collector, signal worker, Telegram route, credential, login, network,
schedule or order setting changes are authorized by this research design.

## Implementation Checkpoint

The learner, purged preparation, sealed-predecessor source adapter, direct-score
account dispatcher, economic journal reconciliation and fixed forecast pipeline
are implemented. The direct dispatcher uses the original V137 daily execution
and rollback bytecode with private namespace bindings; predecessor namespaces
and methods are not changed. It journals four actual utility predictions and
does not fabricate eight cash/floor heads to pass the old interface.

The forecast pipeline writes all six product/fold cells and all 252 product-date
records before its manifest. Scoring verifies that entire manifest, rebuilds
each causal query and recomputes every saved prediction before opening the first
scoring-label payload. Training references use only each fit's admitted prefix.
This content protocol still needs the surrounding exclusive runner to prove
durable publication order and authenticated restored model bytes.

The whole-account replay driver, immutable fit journal/supervisor, dependency
lock, market-run reservation and final saved-result audit remain unfinished.
No V138 market fit, market account replay, strategy result or deployment exists.
Synthetic software tests do not constitute strategy evidence. The closed 48-date
holdout and V137 terminal artifacts remain unchanged.
