# V111 Event Order In PA Learning

2026-09-13 UTC. Implementation design, not an admitted or frozen market run.
No claim, new market fit, replay or result exists. Completed V110 and fixed
Windows V102 remain unchanged. The draft precedent review is
docs/research-next-hypothesis-after-v110.md.

## Comparison

Use the exact completed V107 phase-micro account route in all three arms: original V102
NQ Evaluation, then MNQ PA. The reference retains original V102 MNQ forecasts.
Its authority is reports/nq_apex_phase_micro_v107_repair_v1, not the original
V107 directory containing the preserved technical abort.
Two new PA learners replace ONLY that MNQ forecast with a compact GRU:
chronological21-bar input versus deterministic order-erased input. Thus the
reference is unchanged V102 forecasting on the V107 route, not a claim to
reproduce V102's original separate-product account route.

All arms preserve stop<=140 nomination support, the nominal5:1 entry guard,
half-headroom sizing, NQ<=1/MNQ<=6, fresh-PA5/prior-day6 unlock, original targets,
all-four-positive nomination, cost/latency modes, uncapped fills, cooldown and
all continuous Evaluation/PA/billing/activity/payout state. No changed NQ
Evaluation forecast, fitted NQ model, additional PA capital or fallback product.

## Representation And Learner

Authenticate the existing21-bar completed NQ anchor without changing it. Each
row contains open/high/low/close offsets from the ORIGINAL decision close,
signed toward the nominated trade and divided by its known integer stop_ticks.
After short reflection, exchange transformed high/low so candle geometry stays
valid. Calculate integer differences before conversion to float64. Normalize
signed zero. Do not invent a21-bar volume series or read later prices.

For the order-erased arm, lexicographically sort complete four-coordinate rows
within each event. Preserve each event's multiset, duplicates, original final
close reference, nine context coordinates, timestamps, source identity and
execution geometry. This deterministic representation is permutation-invariant;
it has no selectable random shuffle, seed or sorting criterion. The ordered arm
retains chronology. Neither representation reconstructs a tradable reordered
price path. Only the added predictor input is changed.
The normalization is available only at the completed decision, not at earlier
positions within the sequence. Intermediate GRU states are not tradable
historical-minute forecasts. Canonical rows can still reveal some chronological
relationships through candle continuity; this comparison tests usefulness of
explicit chronological presentation, not information-theoretic destruction of
every clue about ordering or a randomized causal effect on market returns.

Both learners are the same PyTorch GRU: one unidirectional layer, four inputs,
four hidden units, zero initial hidden state PER event, no dropout. Concatenate
the terminal four hidden values with the unchanged nine context coordinates;
one linear13-to4 readout predicts four dollar payoffs. Total trainable parameters:
120 GRU plus56 readout =176. No encoder state crosses event/date/fold boundaries.

Use float64 CPU, one Torch thread, deterministic algorithms, a single fixed
seed20260111, and identical initial parameter bytes in both arms. Train exactly
128 full-prefix AdamW steps at learning rate0.003, weight decay0.01 and global
gradient-norm clipping1.0. No checkpoint selection, early stopping, seed search,
architecture grid, learning-rate search or post-result calibration.

The nine context coordinates reuse each original MNQ V102 fold's exact scaler
and original scaled-training binding. A shared training-only transform group
fits four sequence-channel means/scales and four target means/scales. Equal
total mass goes to each event date; within-date rows share that mass, and each
row's21 bars share its sequence mass equally. The same transforms are used for
both arms. Compute sequence moments in canonical row order to avoid numerical
dependence on event ordering. Exact constant dimensions are detected BEFORE
reduction and use their original value as mean, variance0 and scale1, including
unequal date weights. Train the
date-weighted mean squared standardized error, equally weighting four modes.
Invert target standardization for raw USD forecasts; never clip/invert them.

## Population And Charges

Reuse the complete original V102 MNQ populations and original unguarded
fresh-Evaluation-reference-exposure dollar targets. This is NOT V109's target
zeroing and NOT an estimate of current PA quantity or PnL. Validate all mature
source labels before the existing feasibility filter; preserve row IDs, dates,
weights, original nine features, four target heads and full-label hashes.
Source/coordinate authentication belongs to the runner, not invented component
fixtures. An actual pinned-source preflight must run before any claim or fit.

Keep the original181 explicit NQ/MNQ pairs,55 context dates,126 scored dates,
three42-date folds and ten-full-calendar-session purges. Six neural fits are
scheduled: two paired learners per fold, four outputs each. Three shared
transform groups mean three new sequence and three new target scaler fits;
the original nine-feature scalers are reused, not refitted. Preserve both
initial/final model states, paired transform identities and durable fit-stage
receipts. A partial technical failure is not a strategy loss and is not retried.

The two new policies plus two primary contrasts would charge four comparisons,
13181 to13185, ONLY upon a separate immutable market-run claim. Modes, epochs,
scalers and equality-only control replays are not independent selectable trials.
Twelve distinct continuous account books span1512 scheduled account-days.
All original control accounts and all NQ Evaluation prefixes must reproduce.

## Decision And Limits

The primary contrasts are ordered minus order-erased and ordered minus original
reference. Both must have positive PA trading-PnL differences in baseline AND
combined stress, no added hard/MAE breach and no earlier inactivity closure.
Report absolute PA PnL and full-route gates separately. A full route still needs
numerical Evaluation, observed PA survival, hypothetical payout eligibility and
no hard/MAE breach in both primary modes. Cost-only/latency-only and predictive
loss diagnostics cannot rescue failed primary economics. If only the unordered
arm improves, preserve that finding without selecting/deploying it as success
of the ordering hypothesis. It can only inform a separately charged future plan.

This changes learner family relative to HGB. Only the matched ordered-versus-
erased contrast can support an ordering interpretation; beating the old HGB
alone cannot. More events are not independent samples: original training
prefixes have45/87/129 dates. Historical reuse, adaptive choices and unpriced
program fees preclude an independent significance or after-program-fee profit
claim. Keep48 sealed holdout dates closed and all outcomes private until full
terminal publication. No Windows deployment, signal, order or Telegram change.

## Implementation Sources

Use the library's [GRU implementation](https://docs.pytorch.org/docs/2.14/generated/torch.nn.GRU.html)
instead of implementing recurrence/gradients. Deterministic local testing is
not cross-version or cross-platform equality; see
[PyTorch reproducibility](https://docs.pytorch.org/docs/2.14/notes/randomness.html).
These sources justify API use, not a trading edge. The isolated V111 environment
must not change the fixed V102 runtime or historical environment evidence.
