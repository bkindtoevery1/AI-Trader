# v104 Shared Account Implementation

This records an implemented execution component and a completed morning-input
audit. It is not a completed market experiment, model promotion, live signal
release or verified Apex pass. The latest completed performance study is v103.
The declared v104 matrix and comparison budget remain in research-v104-design.md.

## Implemented Boundary

`tools/nq_apex_mixed_account_v104.py` supplies immutable `MixedIntent` records,
`morning_member()` and `hgb_member()` factories, and `MixedAccount.process_day()`.
Policy names are `combined`, `morning_only` and `hgb_guard_only`. Each product
has its own account; there is no NQ/MNQ router or simultaneous cross-product
position. Exact v103 controls must still use the original `PaCapacityAccount`.

The adapter calls the original v78 account lifecycle once per date on a working
copy. It commits only after complete-day success. Both members share cash,
equity peak, trailing floor, daily activity and payout state. Each eligible
entry recomputes quantity using v103 allocation, current cash/floor and that
entry's stop. Day-start DLL/MAE and prior-day PA size unlock remain unchanged
through all trades that day. Morning profit cannot enlarge them intraday.

Actual exit time, or the first entry tick for a geometry/risk skip, starts the
five-minute cooldown. Busy decisions are skipped, not queued. A one-nanosecond
late morning time exit therefore excludes the 10:30 HGB decision. Flat and
disabled members request no execution window. The complete supplied intent
population is validated even when a standalone policy disables a member.

The original ordered-tick engine retains trailing, MAE, DLL, stop, target and
time-exit precedence, adverse fills, per-product fees and latency modes. The
new nominal PA guard skips positive brackets with stop > 5 * target; equality
passes. It neither adjusts the bracket nor alters exact v103 controls. This
does not certify all official PA or signal-service rules.

Canonical immutable JSON, completed anchors, typed scalars, explicit maturity,
strict chronological decisions and exact TickWindow identities are validated.
Detached working inputs and callback guards prevent a callback changing the
parent account or admitted input and committing a partial day. The adapter is
not a sandbox against arbitrary hostile Python execution. The runner still
owns complete source/model authentication and globally first-tick provenance.

## Focused Verification

Initial component verification passed 96 synthetic cases (exec 35262), then
99 with final-fill/MAE coverage (exec 54781), and 100 with the original qualified
HGB receipt schema (exec 37590). All exited 0. The final focused run, exec 69884,
passed 249 cases: 102 mixed-account cases plus 147 previous v104 cases.

Tests cover both products, four modes and both directions, original-executor
conformance, unchanged HGB Evaluation report fields, once-daily settlement,
actual-time cooldown, PA 5:1 boundary, loss-dependent size, day-start MAE,
prior-day plan unlock, one hypothetical payout, next-day phase transition,
Evaluation reset, between-date PA inactivity, final-cost breach, immutable
input and callback rollback. A qualified synthetic event also passes the
original source receipt validator and v102 masks_for() before hgb_member().
Synthetic data are software fixtures, never strategy evidence.

Independent read-only review found no actionable defect in the component.
The three identified nonblocking coverage gaps, reset, inactivity between dates
and mask integration, received the added final cases. Whole-repository test
status is recorded separately in the central state; focused passes cannot
establish economic performance. Full exec 90656 completed with exit 1:
11,777 unique testcase passes and the one unchanged frozen legacy metadata
failure (v102 four candidate records versus six policy/contrast charges).
No new failure occurred, and all eight captured code/test hashes matched after
the run. The original XML aggregate attribute exceeds testcase nodes by 89,
as in previous saved runs; the unexplained discrepancy is not counted as extra
passes. This is not an unrestricted green suite. Durable verification:
`reports/nq_apex_mixed_account_v104/verification.json`, SHA-256
`f5e5ea14086e3de3ece4d970868dfc58eb347500336886677cc57c24ef67f156`.
Post-update metadata exec 83320 also completed: 25 passes, the same preserved
legacy failure and no new failure. Its original XML is stored beside the
focused/full evidence as `metadata.xml`.

## Real Morning Inputs

Parent read-only audit exec 65355 exited 0. Report:
`reports/nq_apex_mixed_account_v104/morning_inputs.json`, SHA-256
`02a1a37b3c865e609864e7c81bd4a7b185a968c3e7772277a0f8bafbd6f1f143`.
All 126 development dates have 21 completed morning bars, 2,646 total. Their
126 complete 300-minute windows, 37,800 rows, match the saved window hashes.
Twenty-one selected source/implementation files were rechecked. No price
rows, fresh PnL, fitted model or account replay were published by this audit.

Use v82 load_inputs() and its existing readonly/query-only SQLite loader for
`data/nq/ninjatrader_minutes.sqlite3`. The admitted source metadata hash is
`3909947b412865ebd19e027ef48954d39a665b3abbafc2f72467d80fa0e93a2e`.
The stored window map is **v87**, not v92:
`reports/nq_apex_intraday_opportunities_v87/structural_preflight.json`, hash
`6d93572d95d56e92319d57725094f93edf1bdc6d6d74c310e2b9a792329f753c`,
bound by the authenticated v103 dependency map. Its path inside the JSON is
`signals.audit.sessions`, containing 617 unique 300-minute receipts.

For each scored day, v87 `_window(session, day)` validates the full 300 rows;
its original v85 hash must equal `source_window_sha256`. Only `rows[9:30]`,
interval starts 09:09 through 09:29, enter the morning anchor. Convert starts
to ends with `(epoch + 60) * 10**9`; the last completed minute ends at 09:30.
The entire longer window is used for integrity, not to construct morning
predictors or choose a direction. The exact original prior-session trend
cache, saved schedule and per-date feature hashes are separately validated.

The earlier v92 `signals.broad.audit.sessions` reference was an in-memory
path, not a persisted field of v92 structural_preflight.json. The actual v87
saved map removes the need to regenerate all broad signals for this morning
value check. It cannot replace v92 broad event population/model admission.

## Complete Runner

`tools/run_nq_apex_mixed_account_v104.py` implements `source_authority()`,
`prepare()`, `replay()`, `summarize()` and the mutually exclusive preflight,
freeze and one-shot run commands. The explicit policy is
`config/nq-apex-mixed-account-v104.json`. The original v103 closure is checked
separately; only its bound closed-v102 input is passed to the original v103
model loader. Morning anchors are rebuilt from actual minute prefixes and
compared with the saved audit before tape access.

All 32 accounts retain their own chronological state. Eight exact v103 controls
must reproduce complete saved account reports. Complete input nominations and
their evidence are captured before external callbacks, all 181 raw pairs are
checked, and final raw/window receipts and original labels must match. Same-class
method replacement is rejected, not merely replacement of the class object.

Independent read-only review found no blocking runner defect. The noted direct
nonfinite-result test gap received six cases: NaN and positive/negative infinity
in actual result accounts or summaries must abort without publishing a status.
Software and source-preflight results are recorded in the rolling central state.
This implementation does not claim the actual full experiment has completed.

## Remaining Work

Run the complete source wrapper: authenticate closed v103, restore
the exact HGB native forecasts through their closed v102 lineage, preserve the
300-minute receipt and 21-bar prefix bindings, and reverify all 181 raw pairs.
Then freeze the declared six new product policies and six contrasts, reserve
12 comparisons once, and execute all 32 account paths/4,032 scheduled days.
Keep all output metrics closed until complete terminal publication and audit.

No new fits, market replays or charges have occurred; the ledger remains 13,156.
All 48 sealed dates remain closed. Full raw-tick admission, fresh HGB admission,
full transitive runtime authentication, independent performance and official
compliance are not established by the component or morning audit. No orders,
deployment, Windows transfer, secret/session/schedule changes or push occurred.
