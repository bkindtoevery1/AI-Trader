# V127: Session Context For Existing Intraday Opportunities

Declared October 6, 2026 before new V127 feature extraction or fitting. This is
outcome-informed development, not independent validation or live deployment.

## Hypothesis And Precedents

V126's three direct learners did not improve global forecast error on twelve
local price/minute-volume inputs. Rather than retune them, ask whether the
same local Bollinger event has different expected payoffs depending on the
completed regular-hours path since 09:30 ET. Session-wide and local price
locations can differ on persistent-trend versus reverting days. This is an
untested hypothesis in this event representation, not an established cause.

V76 already used an activity-weighted OHLC proxy in a daily 10:00 task. V123
uses the event's preceding 21 minutes, V111 tested that local price ordering,
and V120 tested last-minute tick pressure. V127 is not the first VWAP, volume,
regime or intraday model; its change is session-anchored context for the same
10:30..14:00 events, versus the retained twelve-input V126 boosting forecasts.
V75 already tested recency ridge, so generic recency weighting is not selected.

## Fixed Inputs

Keep all original V123 events and twelve coordinates. Add exactly three:

1. `signal * (last_close_ticks - session_proxy_ticks) / stop_ticks`.
2. `signal * (local21_proxy_ticks - session_proxy_ticks) / stop_ticks`.
3. `signal * (2*last_close_ticks - running_high_ticks - running_low_ticks)
   / (running_high_ticks - running_low_ticks)`, with a zero-range value of zero.

Each proxy is sum(volume*(high+low+close))/(3*sum(volume)). It is a minute HLC3
volume-weighted proxy, NOT exact trade-level VWAP or order-book liquidity.
Formula convention: [TradingView's indicator documentation](https://www.tradingview.com/support/solutions/43000502018-volume-weighted-average-price-vwap/).
The reference documents a calculation, not evidence of profitability.

The session prefix begins exactly 09:30 America/New_York on the event's trade
date, with DST handled by the existing timezone-aware clock. It ends exactly
at the decision; all intervals are complete, contiguous one-minute bars with
the original explicit NQ contract. Match the last 21 rows to every original
anchor OHLC/end timestamp. Require nonnegative integer volume, positive total
session and local volume, and valid quarter-point OHLC. Missing rows, a contract
switch, invalid source volume or mismatched anchors are errors, not imputation
or favorable event removal. The source adapter must inspect only timestamps
outside the prefix: include bars starting at 09:30 and ending by D, exclude
the bar starting at D. Do not use the old full-300-minute payload validator
as the feature-prefix adapter. Poison-access tests must reject future reads.

Use exact integer/rational arithmetic until final float conversion. The first
two coordinates are finite, unbounded ratios without clipping; the third is in
[-1,1]. Positive volume rescaling and common price translation cannot change
the values. Stop, target, entry/exit geometry and original direction stay fixed.

## Learner And Source

One fifteen-input HGB candidate keeps the exact V126 histogram learner settings,
including seed126: four squared-error heads, 100 iterations, rate0.05, seven
leaves, minimum50 events, L2=10, no early stopping. Training-only weighted X/Y
StandardScalers and normalized estimator weights also match V126. Control is
the exact completed V126 twelve-input HGB predictions, not a refitted winner.
Adding coordinates changes available splits: this tests the context bundle,
not a causal isolation of VWAP or unchanged effective model capacity.

Use authenticated V123 prepared labels and original development minute source.
Retain 181 original dates, mature 45/87/129-date training prefixes, ten-session
purges and three 42-date scoring blocks. Preserve all losses/zeros and the
original support mask. Never fit a scaler or learner using its scoring outcomes.
The 48 sealed dates remain closed; these development dates were already seen.

Three candidate pipelines imply six scaler fits and twelve HGB head fits.
One candidate plus one retained-control contrast proposes two comparison charges,
13,227 to 13,229, reserved only at the later exclusive market claim. No grid,
seed selection, fallback, genetic search, solver retry or same-attempt refit.

## Evaluation Scope

Publish complete forecasts before attaching scoring outcomes. Report paired
date-equal MSE/MAE in all four modes, every chronological block, and descriptive
net labels at the unchanged strictly-positive-all-four-heads decision threshold.
Selected-label means are event-weighted: sum original net cents over all selected
events divided by selected event count, separately per mode. No selections gives
null, not zero. Report selected-event count, selected-date count and all scheduled
dates; keep days with no selections in the calendar and coverage denominator.
These means do not reweight dates and are explicitly distinct from date-equal
MSE/MAE. There is no forecast-stage economic pass/advancement cutoff.
Retain empty dates and disclose overlap. Global regression error is diagnostic,
not a universal necessary/sufficient condition for profitability. No retrospective
V126 pass is created by that distinction, and no new score cutoff is tuned.

The economic hypothesis ultimately requires a separate continuous account replay
of candidate and matched control with original fees, latency, stops, capacity,
carried account state, cooldown, trailing loss, PA activity and payout rules.
It must first declare an identical forecast-to-action adapter for both point-
forecast arms; V126 has no account book and point forecasts cannot replace the
V119 joint empirical distributions without a separately declared policy change.
Overlapping event labels are never summed into a fictitious equity curve.
Feature readiness and forecast completion are explicitly intermediate evidence,
not proof of account viability or authorization to replace V63/V92.

Before market fitting: test causal prefix access, DST, explicit contract identity,
source completeness, native volume types, invariant transformations, original
feature preservation, training/scoring separation and retained-control binding.
Record source/runtime hashes, every fit attempt, immutable complete outputs and
the actual terminal exit. No raw-tick replay is represented as completed by a
prepared-label forecast comparison. Failed runs retain their charge and evidence.

## Reviewed Execution Boundary

Before fitting, the reservation binds this design, all V127 implementation and
tests, and the reused V126 model/runner/summary dependencies. Retained-control
claim parameters, numerical runtime, prepared-source identity and ordered plan
hashes must agree. The new local21 context hash must equal the original V123
receipt, not merely reproduce similar feature values.

The old source guard forbids fitting and applies only to source preparation.
Candidate learning runs in the distinct guard that forbids executing changed
unrelated application modules. Every native scaler/head start, completion or
failure is durably journaled, including warnings. No partial head fallback.

Use `--execute`, which launches a single `--run` child and records the exact
command, PID, source pins, stdout/stderr hashes and observed terminal exit in
a separate execution directory. An observer exception terminates and reaps
the child, escalates to kill after a bounded wait, and retains failure evidence.
The postrun `--audit` requires a successful bound terminal receipt before
accepting sealed outputs and recomputing saved diagnostics. This remains a
shared-code arithmetic check, not independent raw/numerical validation.
