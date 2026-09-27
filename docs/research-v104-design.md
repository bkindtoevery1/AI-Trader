# v104 Complementary Session Research Draft

Draft at zero market runs and zero new fits. Not frozen, not deployment
authority, and not independent validation. Read the completed v103 result first.

## Rejected Shortcut

The original v48 prior-session trend rule is a distinct mechanism from v102
intraday reversion. However, assigning the whole day to nonflat v48 at09:30
would retain HGB on only two NQ dates and zero MNQ dates in the shared126-date
development cohort. It is mostly replacement, not additive diversification.
Its original187-tick stop also exceeds initial Legacy PA NQ capacity. No raw
replay or performance trial is justified for a claim this support audit already
contradicts. The pure day-owner module is a diagnostic counterexample, not the
proposed executable ensemble. The completed support audit is recorded in
docs/research-v104-support.md; it calculates no new performance.

## New Candidate, Not Unchanged v48

Investigate one morning trend policy before the unchanged intraday HGB decision
window. Keep the original unanimous NQ/MNQ20/60 preceding-RTH-session direction.
At09:30 ET, use only the21 completed NQ minutes ending09:10 through09:30
(interval starts09:09 through09:29) to compute the existing exact rational
ATR20 stop: ceil(1.5 * ATR20_ticks). The09:30-start minute is not available yet.
Use a fixed target of twice that stop, anchored to actual slipped entry. A zero
trend consensus remains flat. No horizon, threshold, stop multiplier or target
grid is proposed; no fitting is implicit in this deterministic member.

Baseline/cost-only entry is09:31 ET; latency-only/combined-stress entry is09:34.
All modes have the same10:25 scheduled time exit. This leaves the existing
five-minute cooldown before the earliest10:30 HGB decision, but the actual
first exit tick can be late: the joint account must use actual exit time and
skip any still-busy HGB decision, never assume a scheduled flatten was filled.
The morning leg's time horizon, stop and target differ from v48. Its historical
profitability must be measured anew; old whole-day returns are not transferable.
The change is a combined policy hypothesis, not an isolated causal ablation.

Both NQ<=1 and MNQ<=6 require their own explicit same-maturity raw executions,
costs, slippage and evolving account sizing. A smaller ATR stop does not promise
capacity, safety or profit. The caller must verify completed-minute provenance,
contract identity and the original trend feature's exact preceding60 sessions.

## Full Study Still Required

The typed shared-account dispatcher is implemented for the morning leg and
existing HGB mean-reversion events. The finite runner now joins source admission,
all 32 account paths, exact controls and terminal publication. Before any
performance claim, complete its actual admission, freeze and replay. Reuse ordered tick fills,
Legacy Evaluation-to-PA lifecycle, MAE/DLL and v103 capacity, settling each date
exactly once. Keep one position owner, actual-time cooldown and combined costs.
Do not sum separately guarded accounts or settle the morning as a second day.

The HGB source has known nominal PA stop/target ratios above five. Any new PA
geometry guard must be explicit and have its own matched standalone HGB control;
it must not silently alter an exact v103 control. Define that treatment and the
complete finite comparison budget before freeze. The morning2R bracket alone
does not certify the full portfolio or official PA signal-service compliance.

## Declared Implementation Matrix

Implement these four policies independently for each product, not a router
that switches between NQ and MNQ:

| Policy | Morning member | HGB member | PA nominal guard |
| --- | --- | --- | --- |
| morning_hgb_guarded | Yes | Yes | Yes |
| morning_only | Yes | No | Yes |
| hgb_guard_only | No | Yes | Yes |
| exact_v103 | No | Yes | No, unchanged original control |

The guard skips an otherwise positive PA bracket when stop_ticks exceeds
five times target_ticks. Equality is allowed. It does not widen a target,
reduce a stop, change a forecast or substitute another trade. It is a modeled
nominal geometry check, not complete official-compliance certification.

Each policy/product owns four full paths: baseline, cost-only, latency-only and
combined stress. This is 24 new and eight exact control paths, 4,032 scheduled
account-days over the same 126-date development cohort. All 181 source pairs
must be verified. There are zero new estimator/scaler fits; HGB forecasts must
be restored and authenticated from the existing six model records/24 heads.

Declare three paired contrasts per product before performance: combined versus
guarded HGB alone; combined versus morning alone; guarded HGB versus exact v103.
Conservatively budget six new product policies plus six paired contrasts, or
12 charged comparisons. Exact conformance paths are not extra models. The
ledger remains 13,156 until a valid one-shot claim reserves this budget; only
then would it become 13,168. No reservation, freeze or replay exists yet.
Do not add or select configurations, modes, dates or horizons after this study's
outcomes. Baseline AND combined stress remain required; isolated cost/latency
success cannot replace either. This remains reused historical development,
not independent significance evidence or permission to open the sealed dates.

## Shared-Account Implementation Contract

Use a new MixedAccount derived from v103 PaCapacityAccount. Reuse v78
Account.process exactly once per date on a working copy, with commit only
after the complete day succeeds. The existing v87 process_day rejects morning
events, so its validation/lifecycle pattern is reusable but its entry point
cannot be called twice or patched to admit a new time window.

Carry immutable typed member intents, no preassigned quantity, and a read-only
window_for_times(entry_ns, exit_ns) callback returning an exact TickWindow.
Validate the entire event sequence, maturity, anchor and decision order first;
runner admission authenticates original features and all forecast envelopes
before any raw execution. Detach expected evidence before callbacks.

Reuse v85 ordered-tick execution and its trailing mark, MAE, DLL, model stop,
target and time-exit priority. Recompute quantity from current balance/floor
for every eligible entry, but preserve day-start DLL/MAE and prior-day PA
plan unlock. Aggregate both members into one daily row. Mixed long/short
directions may net to a zero daily signal without erasing actual activity.

Executed trades resolve at their actual exit timestamp. Geometry, nominal-guard
or capacity skips resolve at the actual first entry tick. Both consume the
existing five-minute cooldown; flat/unselected nominations consume none and
request no tick window. Do not replay skipped busy events later. Late callback
errors abort the whole day, not turn into selective strategy skips.

Keep exact v103 controls on the original PaCapacityAccount class and require
canonical equality of their complete reports. New standalone members own
their account state; never add standalone PnL to manufacture the combined
result. The new runner must handle v103 closure explicitly: v103 prepare()
expects closed v102 and cannot accept a v103 result as an interchangeable input.

Focused synthetic coverage must include actual-exit cooldown boundaries,
once-daily lifecycle and payout, event-time size after earlier PnL/floor marks,
unchanged day-start limits, exact 5:1 guard boundaries in both phases, both
products/four modes/both directions, callback rollback, flat and terminal days,
and preserved exact controls. Complete source admission, independent code
review, full regression, immutable freeze and the declared full replay remain
required. No executable ensemble or successful backtest is claimed yet.

Keep all48sealed dates closed, all attempted definitions recorded and the
historical development label explicit. No GA, orders, secrets, Windows/code
transfer, installation, service/schedule changes, purchases or push.
