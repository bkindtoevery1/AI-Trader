# V134: Prior Opportunity History As Predictive Context

Declared October 6, 2026 before new context extraction or market fitting.
This is outcome-informed development, not independent validation.

## Reason And Precedents

V133 showed that smaller actual contracts alone did not repair stressed account
capacity. V132's terminal-return conjunction and V127's session VWAP/range
context did not improve their full account routes. Keep those failures intact.
Test whether a current Bollinger opportunity's payoff differs when similar or
opposite opportunities have repeatedly appeared recently. The hypothesis is
about information in the prior opportunity process, not a claim that repetition
caused any observed loss or that every repeated touch should be avoided.

V99 used five-close efficiency, V111 local 21-bar OHLC ordering, V123 local
traded-volume summaries and V127 session-anchored price location. Earlier
multi-horizon and overnight models are precedents, not new inventions here.
The new information is the prior broad V92 opportunity sequence, not another
bar timeframe, trade-count cap, cooldown, past account PnL or previous fills.
V55/V56 used raw Last-price-change arrival/transition statistics in the opening
half-hour and failed their development gates; they did not use this intraday
opportunity process. The bounded precedent review found no completed exact
context append, not proof of exhaustive novelty or predictive value.

## Frozen Context

Preserve each event's exact twelve V123 coordinates. Append three values using
ALL earlier broad opportunities on the same trade date, including unsupported,
unnominated and unfilled events. For decision D, only prior decisions in
`[D - 30 minutes, D)` enter the context:

1. Prior event count divided by 30 (the maximum one-event-per-minute slots).
2. `(same-current-side count - opposite-side count) / count`, zero if empty.
3. Seconds since the most recent opposite-side event divided by 1800, capped
   at one; one if no opposite event exists in the window.

Current event is excluded; history resets each date. The original broad census
starts at 10:30 ET, so the first half-hour has left-truncated opportunity history;
do not invent earlier events or normalize by a newly selected window length.
The 30-minute window is
fixed, not selected by results. No missing-data imputation: empty authentic
history has the stated structural values, while missing or malformed original
event records abort. Explicit contract, source event identity and ordered
minute-aligned clocks must match; no cross-contract history. Validate clocks
before reading future payloads. Full source-census authentication belongs to
the source adapter, not the feature hash. Receipt hashes bind supplied past
events, not provider provenance or live arrival availability.

Current direction determines same/opposite, but no outcome, execution, account
balance or postdecision price enters these features. No sign inversion or
hard event filter. The first twelve values remain bitwise identical. Report
the bundled information effect, not three individually identified causal effects.

## Estimation And Evaluation

Fit separate NQ and MNQ candidate HGB forecasts on the exact V129 own-product
one-contract net-cent targets in baseline, cost-only, latency-only and combined
stress. Features remain NQ opportunity context for BOTH product label sets.
Retain NQ original-capacity support and MNQ original narrowed <=140-tick stop
support, all losses/zeros, equal-date weights and original query masks.

Use the exact V126/V129 HGB recipe: squared error, 100 iterations, learning
rate 0.05, seven leaves, minimum 50 events per leaf, L2=10, no early stopping,
seed126. Training-only weighted X/Y StandardScalers and mean-one native weights
remain unchanged. Six new product/fold pipelines mean 24 response fits and
12 scaler fits. No grid, genetic algorithm, seed search or scoring-based fit.
Adding three coordinates increases available split choices even with the same
tree budget. Controls are the exact retained own-product V129 HGB forecasts,
not newly selected or refitted estimators.

Keep 181 development dates, mature 45/87/129-session prefixes, ten-session
purges and three 42-date scored blocks. No random split. All 126 scored dates
remain, including empty/no-supported-event dates. The 48 sealed dates stay
closed. Original prepared labels are authenticated, not freshly raw-replayed
or independently provider-verified in this forecast stage.

Reserve four comparisons before context extraction/fitting: two product
candidate cells and two own-HGB contrasts, total 13,250 to 13,254. Record every
native fit attempt/warning, save complete forecasts before attaching scoring
labels, bind all source/runtime/implementation bytes, and permit one supervised
attempt. Preserve actual process exits, immutable outputs and a no-fit saved
model/prediction/summary audit. No partial outcomes, retry or threshold rescue.

Report paired date-equal MSE/MAE by all four modes and every fold, alongside
descriptive selected-label means under unchanged all-four-positive nominations.
Overlapping labels are not executed trades, independent samples or account PnL.
No MSE cutoff authorizes a strategy pass. Economics is NOT_EVALUATED in this
stage; any subsequent complete account replay needs its own declared adapter,
comparison charge and full Evaluation-to-PA test. No favorable mode substitutes
for failed baseline-plus-stress robustness. Do not force activity to pass.

No account rules, fees, slippage, sizing, stop geometry, operational V63/V92,
Windows installation, login, schedule, Telegram, order or spending changes.
No actual payout, verified personal 50K pass or independent-validation claim.
