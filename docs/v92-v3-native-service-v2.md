# V92 V3 Native Service V2

Offline code successor only. No deployment, extraction, execution on Windows,
native approval, new archive, model research, or continuous-operation completion
is implied. V1 remains immutable and single-epoch. This successor removes the
explicit financial-handoff blocker; it is not an unattended multi-day supervisor.

## Boundary

- Only original V92 NQ/MNQ virtual books. Fixed artifact SHA256:
  `72b42c3ae01d693703e25f33583072cc0494938c61bdb457117298b37a8e24cd`.
- The service subclasses V1, retaining its `j.process_batch`, context attachment,
  receipt construction, risk commit deadlines, processing and park behavior.
  There is no V102 model dependency or global monkeypatch in production.
- State has schema version 2, scope `V92_V3_NATIVE_SERVICE_V2`, and closed lineage.
  V1 ledger conversion and consumer-binding runtime changes are rejected. Never
  use a fresh database as recovery for a faulted or previously funded ledger.
- Normal restart restores the bound V3 resume cursor and retains exact database
  bytes when there is no new input. Identities for inputs and evidence are scoped
  by configuration hash, avoiding singleton journal/context/park collisions.

## Explicit Operation

Use `tools/run_nq_v92_native_service_v2.py --help` for the full input list.
`--action run` requires the explicit epoch root, pinned source and verifier,
native and capacity admissions plus their hashes, settings, all four evidence
paths, the fixed artifact, private state path, and unchanged runtime SHA256.
No source paths or approvals are discovered or generated.

For a later session, select a separately prequalified configuration and pass
`--new-session --action run` with the **same V2 state path and runtime binding**.
Without that flag a changed session is rejected. The flag never creates a ledger.
Retrying with an already committed exact configuration is a normal restart, not
another financial carry. An actually changed configuration must satisfy:

1. The old session is cleanly PARKED: complete 300-minute window, flat books,
   no pending risk, no halt, no trailing breach, and post-15:31 park observation.
2. The new canonical New York day is strictly later and producer epoch differs.
   Capture follows the old park. The actual attachment observation is pre-09:00.
3. Exact `SourceConfiguration` re-admission, pinned-input checks and the genuine
   `V3Reader` verify the new source, capture barrier and live durable prefix.
   Both products have actual contiguous native ticks starting at sequence 1.
   A heartbeat or one-product prefix alone is insufficient.
4. The unchanged judgment engine prepares a pre-09 prefix without context,
   nominations or events. `nq_v92_session_handoff_v1.carry_epoch` copies **every**
   financial field, including losses, cash, closed-trade counts, trailing state,
   last nomination/decision and cooldown. Native marks and contracts come only
   from the new admitted ticks. No fills, sequence rebasing or account funding
   are synthesized.
5. A single compare-and-swap transaction commits state, resume cursor, carry
   proof, prior state snapshot/hash, both source configuration hashes, prepared
   judgment/hash, record-hash summary and durable boundary. New source inputs,
   live boundary, fault markers and actual clock are rechecked before commit;
   crossing 09:00 rolls everything back. Competing prepared carries are rejected,
   including byte-identical competing proposals.

Old source files/settings need not remain readable after clean park. The prior
validated immutable ledger snapshot supplies the carry proof; the new source is
fully checked. Old context is retained only in historical handoff evidence, never
used for new-day decisions. Existing outbox, delivery state, and consumer-binding
runtime remain in the same database and are not rewritten by handoff.

Use `--action attach-context` separately after 09:00, with the current explicit
source configuration and `--context-path` / `--context-sha256`. Context cannot be
supplied to `run` or carried into the next day. Use `--action publish --outbox ...`
in a separate process for local publication of committed outbox events. Publication
is source-independent and does not send Telegram or contact a broker.

## Faults And Limits

Consumer startup, processing and handoff use SQLite timeout/busy timeout zero.
A held SHARED reader can reject COMMIT; state, evidence, input identity and cursor
then roll back together. Active-consumer failures retain V1's independent durable
fault latch even when SQLite cannot persist a halt. Markers bind state path,
epoch and configuration, and stale owners cannot halt or alter the successor.
A late old-epoch marker cannot poison the new epoch. Existing current/parent
faults, including unsafe marker paths, are never cleared or bypassed by handoff.

An unsuccessful **uncommitted candidate** handoff leaves the already parked old
ledger unchanged; it does not relabel it as an active source fault or latch the
winning successor on behalf of a losing CAS contender. Any retry must pass every
new-source admission and freshness check again. This is not fault recovery.

The separate publisher deliberately retains the existing `PaperStore` startup
behavior, including its initial ten-second SQLite connection timeout; the
consumer/handoff no-wait guarantee does **not** cover publisher startup.

`run` loops within the selected session and exits at PARKED/HALTED. A later epoch
still requires explicit prequalified inputs and invocation. No source discovery,
automatic approvals, native lifecycle/rearm, schedules, broker or simulator
orders, network, secrets, real market rows, historical trials or holdout reads
are added. Windows source admission remains an external unmet deployment gate.

## Verification

Final focused run: **119 passed in 75.66 seconds; process exit code 0**. The
consumer and CLI add 332 production lines. V1 service, V1 CLI, V1 service tests
and the carry primitive have no diff against commit `77270c7`. No bundle,
deployment or native/source approval was produced.

Parent integration independently passed **583 tests in82.98seconds, exit0**,
including both service versions, carry, V3 admission, minute judgment, store,
outbox publisher and signal route/sync. These sets overlap the119 component
tests and must not be added together. No full-repository rerun is claimed.

All test packets, prices, trades and volume context are invented local fixtures.
The full-window integration uses the exact fixed artifact and actual V3 reader
through 300 completed minutes, clean park and later-epoch handoff. Fast adverse
cases seed an explicitly synthetic old financial snapshot using the existing
V92 pure financial primitive and its fixture-only model; these are not native
source evidence or strategy-performance results.

Focused command (also run with the unchanged V1 and carry suites):

```sh
env PYTHONPATH=src:tools PYTHONDONTWRITEBYTECODE=1 \
  python \
  -B -m pytest -o addopts= -q -p no:cacheprovider \
  tests/test_nq_v92_native_service_v2.py \
  tests/test_nq_v92_native_service_v1.py \
  tests/test_nq_v92_session_handoff_v1.py
```
