# Fixed-Session Continuation Targets

October 7, 2026 UTC. Research implementation, not a fitted strategy, market
experiment, validation pass, Windows recovery or permission to send orders.

## Research Purpose

The [sequential trace](research-sequential-trace-v1.md) records actual successors.
This component makes their subsequent realized trading returns usable as
explicit supervised responses. A zero-return abstention can precede profitable
later trades; conversely, an immediately profitable attempt can be followed by
a losing continuation. Neither observation supplies the unchosen action's
return or establishes that changing the policy improves the account.

`tools/nq_apex_sequential_targets_v1.py` consumes completed traces, the caller's
entire declared calendar, a strict training cutoff, and an explicit integer
horizon from1 through63 declared sessions. There is no default, horizon search,
fit or market runner. The horizon and calendar must be frozen before market
labels are generated; this range is an API bound, not63 model trials.

## Target Definition

The current session counts as the first. Every eligible recorded decision gets
one row, including abstentions and original forced zero-capacity attempts. Its
scored interval begins at that decision and ends at the requested session's
conservative17:00ET endpoint. Prior actions are excluded. Empty declared
sessions count; weekends or missing source dates are not invented.

Net trading PnL is summed from the original resolved edges after their modeled
commissions and slippage. Immediate-action and later-continuation PnL reconcile
exactly to that total. Account balance changes and hypothetical withdrawals
are separate diagnostic fields, not additional rewards. Evaluation resets or
fresh PA balances must not create artificial profits or losses. Purchase,
renewal and activation fees remain unpriced; this is not all-in profitability.

A true absorbing account terminal completes the remaining horizon early.
Pending Evaluation resets and PA activation do not. If a live account's
observed calendar ends too early, retain the decision with `RIGHT_CENSORED`
and a null target. Do not turn it into a terminal, zero, partial return or a
bootstrap estimate. Every complete response matures strictly before the
training cutoff, not at it.

Product-specific behavior model/population hashes and training cutoffs must
stay constant across the declared trajectory, including recorded empty days.
Every decision must match its own product/mode/arm and behavior bindings, whose
cutoffs cannot be later than that decision. The binding check does not prove
that a callback actually loaded those bytes; artifact/source admission remains
the caller's responsibility. Pre-trajectory account history is not relabeled
as part of this target horizon.

`input` contains only the original causal node identity, event identity,
decision time and date. Future endpoint identifiers, maturity, terminal state
and return values stay under `target`. A later learner must resolve and project
the original decision snapshot, never feed target/edge fields into features.
Rows and the complete envelope have deterministic content hashes; these are
integrity references, not independent source authentication.

## Remaining Model Work

These are returns under one fixed recorded behavior policy, not two-action
Q-labels or an off-policy evaluation dataset. Missing TAKE/ABSTAIN alternatives
cannot be recovered by treating behavior correlation as a causal advantage.
Changing the policy requires actual same-state action forks, unchanged future
execution/lifecycle mechanics, a declared continuation policy, and complete
chronological evaluation of the resulting account.

Horizon feasibility also matters. The predecessor's first chronological fit
has45 training dates. A63-session target would leave no full-horizon training
responses there except early terminal cases. Training only those cases would
introduce informative-censoring selection, not solve the data limitation.
The component deliberately does not select a horizon or automatically fit the
subset. The older45/87/129-date prefixes and subsequent expanding fits must be
reconsidered explicitly when a concrete sequential study is preregistered.
See [the predecessor design](research-v137-design.md).

Overlapping decisions, modes, state replicas and returns are not independent
observations. Future fitting requires date/group mass preservation and purging
against the entire label interval, not merely the entry timestamp. All48 sealed
dates remain closed. No comparison reservation, new market label, fit, replay
or trial is made by this component; historical total remains13,293.

## Verification

An independent test author found that an equal-valued floating-point decision
cutoff passed equality with the native integer behavior cutoff. Its failing
regression remains enabled; the source now explicitly requires a native integer.
The initial independent run was237passed/1failed, not a successful qualification.

The final parent affected run is **780passed**, exit0,8.03s:238new independent
target cases plus542unchanged trace/account cases. JUnit independently contains
780unique cases and no failures, errors or skips. Separate invocations overlap
and are not added. Actual parent tool session5763 is terminal with exit0.

The tests compare target sums with retained original attempts rather than the
implementation's prefix sum, exercise all cost/latency modes and both sides,
and cover horizon/cutoff types,63-session genuine zero versus censoring,
abstention/geometry/zero-capacity continuations, empty dates, Evaluation-to-PA
and reset transitions, withdrawals, true PA terminal/inactivity, terminal-tail
immutability, fixed behavior, pre-trajectory history, causal input invariance,
detached outputs and rehashed tampering.

- Source SHA256: `9a0787204e27e3f00825021e79a479f47dd59ca5477ed8d783bbe653d03f529b`.
- Test SHA256: `ec728fd2e2696c4d18007a5b1f007c44af17b7d389df9204e9b8f981ae1b3ee2`.
- JUnit: `reports/nq_apex_sequential_targets_20261007/affected-final.xml`.
- JUnit SHA256: `af94df5c5f6cb538adb7f055750c1b4dc1210efd97045412abedb2863b6e899b`.

Original trace, V137/V136/V87 account and Windows runtime code are unchanged.
The full repository regression was not run. No Windows-host measurement,
recovery, live model inference, Telegram request or order was made by this work.
