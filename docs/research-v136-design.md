# V136: Causal Trade-Profit Giveback Protection

Declared October 6, 2026 before any V136 market replay. This is an
outcome-informed historical execution-policy experiment, not a new estimator
fit, independent validation or permission to deploy.

## Reason And Precedent

V135's opportunity-history forecasts failed to reach Evaluation in every
execution mode. Unrealized gains raised account trailing floors while later
giveback left insufficient capacity for another indivisible NQ contract.
This motivates a path-dependent exit question, not evidence of its success.

V83 already tested ATR/volume initial stops without intratrade trailing stops.
V86 tested fixed target geometry. V98 product routing and V133 all-MNQ sizing
did not establish robustness. Account trailing-floor enforcement and entry
break-even filters are not protective trade-profit exits. A bounded review
found no completed test of the exact policy below; no exhaustive novelty claim.

## One Frozen Treatment

Use both exact V134 own-product forecasts, as executed by V135: NQ in
Evaluation and MNQ in PA. Preserve every nomination, support restriction,
initial stop, fixed target, account guard, integer sizing, five-minute exit
cooldown, latency and fee setting. No retraining, inversion or forecast fallback.

For each actual trade, define its known initial risk unit in cents as
`R = original_reserve(product, initial_stop_ticks) * actual_quantity`.
The unchanged reserve is `500 * stop_ticks + 4700` for NQ and
`50 * stop_ticks + 650` for MNQ, before quantity. It is the conservative
entry-sizing reserve, not an ex-post loss or a mode-fitted parameter.

At each observed Last tick compute the liquidation net PnL with the actual
entry fill, adverse exit slippage, both commissions and actual quantity.
Maintain only the greatest such PnL observed so far in THIS trade. Arm once
that peak reaches R. Once armed, exit at the first observed tick satisfying
`2 * current_liquidation_net_cents <= peak_liquidation_net_cents`.
This is exactly one-half of the positive peak, using integer comparison,
without rounding a synthetic stop price or guaranteeing a floor fill.

Preserve existing precedence: account trailing breach, per-trade MAE, daily
loss limit, initial stop, fixed target, then the new giveback exit, then time.
Keep the original interim account mark (entry commission only) unchanged;
the separate liquidation-net calculation must not alter its trailing floor.
Use the actual triggering tick and adverse exit fill. A gap may still cause
a loss or hard breach. Never widen the initial stop, use a future maximum,
read beyond the scheduled exit, or carry a peak into the next trade.

The 1R arm threshold and half-peak fraction are fixed without a sweep. Do not
add break-even-only, target-completion liquidation, a second threshold or a
favorable forecast recipe after seeing this experiment's outcomes. Existing
forecast targets describe the old exit policy; retained predictions are entry
gates here, not newly calibrated expected returns for the new exit.

## Full Account Test

Replay eight independent account books: four V135 control books and four
giveback books. All use identical forecasts. The modes remain baseline,
cost-only, latency-only and combined stress. Match all four controls exactly
to the sealed V135 accounts. Keep the original Legacy50K modeled lifecycle,
NQ <=1/MNQ <=6, PA caps, renewals/resets, inactivity and hypothetical payout.
Actual quantities, next opportunities and phase dates may differ as causal
consequences of changed exits; do not rescale old trade PnL as a substitute.

Scan all181 complete development raw pairs and reconcile their original raw
and execution-window receipts. Score the same126 dates from three42-session
purged folds. Preserve the admitted unit-journal hashes without rebuilding
training labels. The ten outer embargo sessions and48 sealed holdout dates
stay closed. Inputs, including unused product/date forecasts, remain validated.

Full-route success requires BOTH baseline and combined-stress Evaluation
numeric pass, PA entry, observed PA survival, positive PA trading PnL,
hypothetical payout eligibility and no hard/MAE breach. Diagnostic modes do
not rescue either primary mode. No validation-gate relaxation is planned.
Relative PA benefit additionally requires positive candidate-minus-control
PA differences in both primary modes when both actually reached PA. Otherwise
the unavailable PA-dollar contrast is null. Report unequal phase exposure.

Report causal protection activations and exits, their actual fills, residual
headroom and complete failure reasons alongside all account results. Activation
or reduced loss alone is not an Evaluation/PA success. Last-tick replay lacks
bid/ask liquidity and does not establish live execution quality.

## Freeze And Completion Evidence

Reserve two comparisons before outcomes: one policy and one V135 contrast,
moving13,256 to13,258. Keep both charges even if execution aborts. Freeze the
design, code and tests and publish the design before the sole supervised run.
Run focused software tests, affected regression and actual source preflight.
Describe their actual scope; do not claim an unrun full repository suite.

Bind exact V135 closure, actual successful terminal, audit and unchanged
V134/V130 source lineage, code, runtime, source envelopes and forecasts.
No fits, inference, label construction or model deserialization is allowed.
Persist a claim before market execution. Publish only complete outputs after
all181 pairs and eight books. Observe child and supervisor terminal states,
verify immutable pins and audit saved summaries without a second raw replay.
Shared-code consistency is not independent numerical validation. No automatic
retry, partial outcome release or post-outcome implementation repair.

No official current-cohort compliance, personal50K pass or actual payout is
claimed. Program fee units remain counted but prices unverified. No Windows,
login, schedule, Telegram, purchase, secret, order or operational-model change.
