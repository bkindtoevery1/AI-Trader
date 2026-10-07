# V140 Technical Failure And Repair

October7,2026. The reserved V140 experiment stopped before model evaluation.
This is a software integration failure, not evidence that its trading
hypothesis succeeds or fails. The fitted model and account result do not exist.

## Actual Attempt

The supervisor started at05:42:41Z. ChildPID66710 exited1; the supervisor
also exited1. The terminal receipt was published at05:50:23Z, and both
processes were confirmed absent. Original source hashes remained unchanged.
Only claim/failure records exist: zero label-day files, zero fitted pipelines,
zero native fits, zero account replay and no result seal. All five reserved
comparisons remain charged, effective total13,277. No automatic retry occurred.

`prepare_nq_apex_giveback_unit_v140.py:380` required both the chronological
event stream and the envelope lookup to have identical dictionary insertion
order. Its predecessor, `nq_apex_baseline_nomination_replay_v117.py`, instead
requires ordered stream dates and exact envelope date membership. The failed
attempt had already passed that predecessor validation. Consequently the
new equality failed on envelope insertion order, not missing market dates.
Extraction stopped before the first `tape_for` call and before any new targets.

## Why Qualification Missed It

The original1,322 affected tests passed, but their source fixture constructed
envelope dictionaries in calendar order. The real-source preflight restored
and validated the source and replay snapshot, but did not execute this new
label-collector check. The numerical integration fixture also supplied
prebuilt labels. Those tests did not prove the first real extraction would
succeed; that coverage gap is now explicit rather than hidden by a green count.

## Integrity-Only Repair

The separate `nq_apex_giveback_unit_snapshot_v140r1.py` leaves all original
V140 source/test/design pins unchanged. It requires the same unique ordered
181-date calendar, exact ordered stream and exact envelope date set, then
rebuilds only the detached envelope lookup in calendar order. It does not
sort events, reorder receipts, drop dates, alter envelope values or admit a
new source. The original collector executes in a private function namespace;
no predecessor globals are patched. No model or financial rule changes.

The final25-case focused test run passed. It reproduces the original failure
using a reverse-order envelope lookup, runs the real repaired collector on
invented tapes and compares all181 label files and the complete manifest
byte-for-byte with the original chronological fixture. Additional cases
reject missing/extra dates, unordered streams, wrong receipts and changed
events before tape access. This is software evidence, not strategy evidence.

The first actual-source repair probe exposed a second fixture mismatch:
production envelopes are `_SnapshotEnvelope` objects, not JSON dictionaries.
An unnecessary JSON equality check raised TypeError before any labels or fits.
The repair now preserves each opaque value by object identity and never
serializes or reconstructs it. Tests instantiate the actual envelope classes
without file access and verify both dictionary and opaque-envelope collection.
The first affected regression was explicitly interrupted with exit2 before
this change; it is not reported as a pass. Its XML remains retained. The new
actual-source probe and affected regression use the corrected bytes.

The corrected actual-source probe exited0 at06:12:40Z. All181 calendar,
stream and envelope dates match; the original envelope order alone differs.
The corrected order matches without replacing any opaque value or other
snapshot member. All271 original source pins and the failed-attempt bytes
remain exact. No raw labels, fits, forecasts or account replays were run.
The receipt SHA256 is
`c93feaf939da22d5d76d582518821bbe12cbe47afed547ce7d56d7f16d934352`.

The complete affected regression exited0:1,347 unique cases passed with zero
failures/errors/skips in614.112 seconds. This is the original1,322-case surface
plus25 repair cases, not two independent passes to add together. Eleven
retained warnings come from predecessor numerical-edge fixtures. The immutable
repair qualification SHA256 is
`9ba667d5c0f2884d291e12ef71726f725f11a01fd9d28248c9d55c63f3bb218c`.

The adapter is qualified, but a separate supervised market execution path is
not yet qualified or started. No full-repository-green claim is made; the
previously disclosed13 unrelated residual test identities remain. Required
local test/probe processes are terminal. Source repair commit: `64f66e02`.

## Boundaries

Failed evidence stays under `reports/nq_apex_giveback_unit_v140/` and its
execution directory. New checks go only under
`reports/nq_apex_v140_order_repair_20261007/`. The original failure cannot be
overwritten or relabeled as an economic result. All48 holdout dates stay closed.
Windows startup, historical data archival and model evaluation remain separate
claims; this repair does not start Windows models or send signals/orders.
