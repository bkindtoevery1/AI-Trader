# V138 Complete Execution Path

October 7, 2026 KST. This continues the fixed
[direct-utility design](research-v138-design.md), not a new model selection.
The earlier [component checkpoint](research-v138-implementation.md) remains
historical evidence. Market fits/replays and reservation are still zero at this
implementation checkpoint; the effective-trial count remains 13,262.

## Account Evaluation

The new replay scans all 181 original paired raw-tick dates and processes four
candidate mode books over all 126 scored dates: 504 scheduled account-days.
Each decision uses its own current account state and the correct purged fold.
The fixed 15 market and four state features produce four raw utility scores,
without fake cash/floor heads or projection. Busy/cooldown, integer capacity,
costs, latency, initial stop, giveback, NQ Evaluation-to-MNQ PA routing and
economic gates are unchanged. Negative forecasts do not skip the account stage.

The four comparator books are authenticated saved V137 projected-joint books.
They are not refitted or replayed. Eight reported books mean four new books
and four reused controls, not eight new trials or independent observations.
The saved-result audit reconstructs every nonzero-capacity own-state query,
recomputes its raw four scores and reconciles the original opportunity census,
model/fold bindings, explicit contracts, cash, execution and lifecycle journals.
Model-byte authentication remains the runner's responsibility.

## One Attempt

The journal records six serial pipelines / 36 native fits in 84 ordered events.
Each pipeline has two scalers and four response estimators. Original population,
plan/source binding, train-only reference, artifact and warnings are reconciled.
Publication is create-if-absent, mode 0600, with stable regular-file checks,
file and directory fsync, and no overwrite or retry after partial failure.
All six artifacts are authenticated before any deserialization. The journal
does not claim provider or source admission by itself.

The supervisor authenticates the reservation, qualification, source pins and
parent/child relationship; records the actual child exit; and runs the terminal
saved-result audit. A fixed 252-record forecast census is published before
scoring labels are joined. The account stage runs regardless of forecast error.
No partial score, retuning, fallback selection or new holdout access is allowed.

All final outcomes and completion status are in one atomically published
`result_seal.json`: `results.accounts`, `results.diagnostics`, `results.status`.
Its `files` mapping binds 345 causal/model/journal payloads. There are no separate
account, diagnostics or completed-status files that can be exposed piecemeal.
The audit checks every payload, all three result sections and the unchanged
closure again. The supervisor authenticates the complete result seal.

## Pre-Market Corrections

Independent review found that sequential outcome publication could leave an
account file or completed status without the final seal after a late I/O error.
The single-publication format above fixes that before any market fit. Tests
inject a bad final census, pre-link failure and a partial write, and verify that
no subset of results is published. Static re-review found no remaining concrete
closure or regression issue. This is not an external validation of profitability.

The first source-only preflight rejected code/runtime drift while that reviewed
fix was being applied. Its actual exit was one; it was not mistaken for success
or a model failure. The final preflight, exec27370, finished exit zero with
181 dates, 5,485 original events and four exact saved controls. It verified
20 own pins and 259 loaded dependencies, with no new fit, raw-label generation
or account replay. Receipt `source-preflight-v2.json` under
`reports/nq_apex_v138_execution_qualification_20261007/` has SHA256
`c02366306013263111367c4ab8580de7966bf72558050201c6f761c9a3f1e171`.

## Qualification Status

- Replay-focused synthetic tests: 29 passed.
- Journal-focused tests, including six native synthetic pipelines: 112 passed.
- Final runner/process/publication tests: 61 passed.
- Initial combined 198-case execution-path run passed, but predates the final
  publication correction and is not the final qualification evidence.
- Complete affected transition/monitor regression: exec91092 finished exit zero,
  2,519 unique cases in 703.97 seconds: 743 V138, 1,729 V137 transition and
  47 execution-monitor cases. The nine retained warnings are the previously
  covered synthetic weighted-constant-column sklearn warnings; none is hidden.
- Whole-repository regression: not rerun here; the previously disclosed broad
  suite is not green. No full-repository pass is claimed.

The final qualification JSON has SHA256
`69d5cc00936ac78518fa7873a6bdb57b400b93ce7adf6ec0753404b77cf9620c`.
The complete regression JUnit has SHA256
`3d23356e70d0c8340145a20bebbd1a113590b4b63bc6efc76c3da9426683fb9f`.
Both are retained in the private qualification directory above. The record
binds the 20 own source/test/design pins and 259 loaded dependency hashes.

Synthetic fits and positive fixture gates are software checks, not strategy
evidence. Qualification, publication and the five-comparison reservation must
precede any actual market fit. Both V137 attempts and reservations are retained;
all 48 sealed dates remain closed. No order, Windows UI, connection, schedule,
credential or spending change is included in this implementation.
