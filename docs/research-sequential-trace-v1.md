# Sequential Decision Trace: Research Component V1

October 7, 2026. Implemented and synthetic-tested; no new fitted model, market
experiment, strategy return, independent validation, deployment or Apex pass.

## Why This Component

V106 already used headroom utility; V118/V119 already used current account
capacity and an explicit flat alternative. V137 learns isolated cash/floor
transitions from numerical state anchors, and V138 directly learns the same
one-step utility. None of those establishes continuation-value learning.

A bounded independent review found no equivalent linked successor-state
research implementation. The distinction here is the recorded action-dependent
next decision and lifecycle state, not account-state features, abstention or
whole-account replay by themselves. This does not establish that a future
sequential learner will outperform the completed failed policies.

## Implemented Behavior

`tools/nq_apex_sequential_trace_v1.py` instruments the unchanged V137 nomination,
V136 giveback execution and inherited Legacy50K Evaluation-to-PA lifecycle.
Function-local copies bind only the trace hook; original modules/classes,
control paths, predictions, sizing, fees, stops and cooldown remain unchanged.
This retains the predecessor's1NQ/6MNQ phase route; it does not introduce a new
global position limit or change Windows V63/V92.

Each completed day contains09:00ET start, actual eligible-decision nodes and a
conservative17:00ET end. A decision records detached own-account history and
the completed21-minute anchor before forecasting/future entry reads. Callback
objects, transient bindings and the future day tape are excluded. Intraday
attempt history includes only resolutions strictly before that decision.

Edges distinguish ABSTAIN, ATTEMPT, forced zero-capacity attempts and lifecycle
changes. Abstention can reach the next minute; an attempt resolves first and
retains the original five-minute cooldown, including geometry/risk skips.
Busy or unsupported census opportunities remain explicit omissions, not
fabricated actions or omitted profitable observations.

Whole days are atomic. A bad late callback or mutation restores both account
and prior trace. Day joining requires the complete declared ordered calendar,
exact predecessor/successor account continuity and a strict mature-before-cutoff
boundary. Hash/type/schema and node/edge reconciliation are checked against the
retained daily evidence. Hash consistency does not authenticate source data or
prevent a coordinated forgery of every underlying record; caller admission is
still required.

Realized trading PnL is separate from account cash changes. Evaluation-to-PA
initialization and hypothetical withdrawals are not mislabeled trade losses.
The fee-unpriced flag means purchase/renewal/activation charges; modeled trade
commissions and slippage remain included in net trading PnL. Real account
closure is distinguished from an unfinished, right-censored final observation.
Pending Evaluation reset or PA activation is not a terminal label.

## Verification

Independent synthetic tests cover all four modes, both phases, both arms and
both sides, exact original reports/executions, giveback behavior, causal clocks,
zero-capacity and geometry cooldown, empty dates, full Evaluation-to-PA links,
hypothetical payout, inactivity closure, failure rollback, detached results,
calendar/cutoff rejection, and rehashed schema/node/edge tampering.

Parent final affected run: **542passed**, exit0,4.20s. This includes the160new
cases and382unchanged account cases; standalone runs overlap and are not added.
The full repository regression was not run. An initial test-only substring
assertion was corrected by the independent test author before the final run.

- Source SHA256: `3d9ea55f7588938052ccb65d8dd813b59f88b9ad3d4752400f59975f171bbee3`.
- Test SHA256: `4f7ba5fc0b6a14fbc1db501e903b764ebaf060b3b29c85c6e9c9a6640fae27bb`.
- JUnit: `reports/nq_apex_sequential_trace_20261007/affected-final.xml`.
- JUnit SHA256: `1617388109f5d2ee9c37c373081023609126e85a3bebf0b0e959301624f5902c`.
- Parent terminal tool session49212 exited0. The original account/runtime files
  have no task changes.

## Not Yet A Sequential Learner

The trace contains only the behavior policy's realized actions. It does not
supply missing-action counterfactuals, prove Markov sufficiency, price unmodeled
account fees, fit a value function or certify source admission. The declared
calendar and source/model artifacts must be bound by the future research
runner, not selected after outcomes. Nodes, state replicas and overlapping
opportunities are not independent statistical observations.

Before market work, define and test an action-coverage scheme, causal feature
projection, target/reward/horizon, censored-tail handling and chronological fit
protocol. Then freeze source/model dependencies and comparisons before fitting,
and evaluate the complete unchanged account route. Do not train directly on
future-labelled edge fields or reinterpret this component as a passed strategy.

New market labels, fits, replays and trial charges:0. Historical total remains
13,293; all48sealed dates remain closed. Windows has no new observation or
recovery from this work. Its last confirmed stopped-execution observation is
still20:42UTC; no restart, schedule, signal, Telegram request or order occurred.
