# V92 / V3 Native PAPER Service V1

## Boundary: One Epoch Only

**This is not a complete continuous operational restoration. New-day or new-epoch
handoff is unsupported, even after clean park. Preserve the existing SQLite
ledger and its fault marker; do not delete them or select a new empty database
to obtain fresh 50K books. There is no reset, migration, recovery, or handoff
command.** Run results expose `handoff_supported: false` and
`boundary: SINGLE_EPOCH_ONLY_PRESERVE_LEDGER`. A different configuration against
the same database fails closed. A parked service remains parked; an active
service cannot process beyond its captured New York calendar day.

This addition owns only:

- `tools/nq_v92_native_service_v1.py`: single-epoch consumer and detached state validator.
- `tools/run_nq_v92_native_service_v1.py`: consumer, separate context attachment, and separate publisher CLI.
- `tests/test_nq_v92_native_service_v1.py`: synthetic integration/conformance tests.
- This document.

Existing/frozen files are unchanged. In particular, the existing
`run_nq_v92_windows_paper_v3` remains the cutoff wrapper over its original V2
consumer and `nt-last-v2` identity. It is not relabeled or imported here.
There is no V102 inference or service dependency, model research, fitting,
historical price/holdout access, broker-order path, secret access, network,
schedule, Windows control, deployment, or bundle generation in this addition.

## Preserved V92 Behavior

The artifact must match
`72b42c3ae01d693703e25f33583072cc0494938c61bdb457117298b37a8e24cd` exactly.
Both original `FixedModel` instances are loaded through V92 `load_models`.
`nq_v92_minute_judgment_v1.process_batch` owns all minute aggregation,
nomination and PAPER math. `contexts`, `handoff.validate_park`, and the original
`risk_commit_deadlines` are reused, not reimplemented.

The original independent virtual 50K NQ/MNQ books and NQ <= 1 / MNQ <= 6 limits
remain. The growing NQ prefix is exactly 09:00 through 14:00 New York time,
300 completed minutes; decisions run from 10:30 through 14:00 inclusive.
No current-minute or manufactured missing-minute input is introduced.
Both authentic source capture and first consumer/durable attachment must be
observed before 09:00. A fresh service cannot attach late and backdate itself
to a source's pre09 capture. A restart verifies genesis through the committed
cursor without re-evaluating previously committed judgments/events.

## Admission and Persistence

`nq_v3_source_admission_v1.admit_source` is the sole V3 admission entry point.
The consumer requires its exact `SourceConfiguration`, repeats full admission
to reject fabricated cached configurations, and uses only `open_reader` and
its exact V3 `resume_cursor`. All selected input paths and hashes, native
epoch/contracts/time basis, configuration hash, source ID `nt-last-v3`, and
cursor bytes/record hashes remain bound. All pinned files are checked again
before each poll and at processing/commit boundaries. The V3 reader retains
its own chain, gap, provider timestamp, stop, freshness and boundary checks.
`model_admission_verified` and `orders_allowed` remain false.

Each journal record commits its judgment, cursor, events and evidence in one
existing `PaperStore` transaction. Runtime/artifact binding is separately
immutable. The consumer uses `busy_timeout=0` for both BEGIN and COMMIT, and
checks fresh source state and original new-risk deadlines immediately before
commit. It never waits behind a SQLite reader after a freshness check.
The unchanged store bounds each transaction to ten evidence items; an
oversized multi-minute backlog that exceeds that bound fails closed, rather
than silently dropping evidence or pretending replay was live.

Source errors poison the reader and create a content-addressed, fsynced local
`v92-v3-fault.*.ready.json` latch in the private database directory before
attempting the fault-only SQLite transaction. That marker blocks restart even
if database lock contention prevented the fault transaction. `lstat` detects
existing files and dangling links at the exact marker path; symlink/reparse
and non-private parent directories are rejected by the existing helpers.
No automatic fault clearance exists. A disk/filesystem failure can prevent
durable fault recording; external supervision and explicit reconciliation
remain necessary. The marker is not source evidence or a Telegram event.

At/after 15:31, open/pending risk keeps the consumer in `DRAINING_RISK`.
Only genuine authenticated own-product ticks can produce exits. A heartbeat
or the other product's tick cannot invent a fill. Clean park requires all
300 minutes, both products observed, flat unhalted books, the committed durable
boundary, and `handoff.validate_park`. Source faults do not create synthetic
exits; committed exits remain available to the independent publisher. Internal
minute/PAPER halts remain sticky in the original engine and can drain existing
risk only while source admission is still valid.

## Context and Publication

Use a separate `attach-context` invocation after 09:00. The pinned context must
contain exactly the existing five-field volume/calendar schema and the prior
20 eligible complete sessions of 300 volume values each. The access intent is
recorded before reading; the context is immutable for the session and restored
from SQLite without rereading its original file. Attachment commits no ticks,
judgments or trade events. A transaction must not cross a minute boundary
while attaching context.

Only future completed-minute decisions can use the newly attached context.
If a source record includes a completion older than the context admission,
that entire record is conservatively processed without history. It is never
replayed later to nominate missed risk. This may suppress a later completion
in the same unusually large record. Context validation verifies structure and
the caller's pinned bytes, not upstream provenance; authentic independent
volume/calendar review is still required. The existing structural validation
flags remain false for upstream/source proof.

Run `publish` in a separate process. It opens an ordinary `PaperStore` with
this new `validate_state`, then uses the unchanged `OutboxPublisher`. It needs
only the database, runtime hash, and private local output directory, not source,
model artifact or context files. Publication is bounded (32 events per poll)
and content-addressed/idempotent after restart. It writes local ready files;
it does not send Telegram or claim delivery. Existing independently operated
sync/relay/delivery components remain responsible for Telegram.

## CLI

Run from the repository with `PYTHONPATH=src:tools` and the approved offline
Python environment. All file/directory inputs must be explicit local absolute
paths; private database/output directories must already exist (mode 0700 on
POSIX). Trusted packet hashes must come from independent review, not from
self-hashing an untrusted packet as an approval.

```sh
python -B tools/run_nq_v92_native_service_v1.py --help
```

`--action run` requires:

```text
--state-path --runtime-sha256 --artifact-path
--epoch-root --source-path --verifier-bundle
--native-admission-path --native-admission-sha256 --source-settings-path
--capacity-admission-path --capacity-admission-sha256
--activation-evidence-path --time-basis-evidence-path
--source-connection-evidence-path --capacity-approval-evidence-path
```

`--once` performs one bounded poll instead of the same-epoch loop. Both paths
drain cutoff risk before clean park. `attach-context` uses the same explicit
consumer inputs plus `--context-path --context-sha256`, attaches once and exits.
Context arguments on `run` are rejected. The new module imports the old V92
runner only for its unchanged risk deadline helper, never its admission/service.

The source-independent publisher is runnable with:

```sh
python -B tools/run_nq_v92_native_service_v1.py --action publish \
  --state-path /ABS/PRIVATE/paper.sqlite3 \
  --runtime-sha256 REVIEWED_RUNTIME_SHA256 \
  --outbox /ABS/PRIVATE_OUTBOX --once
```

Omit `--once` for the separate publisher loop. CLI failure returns 1 with
`FAILED_CLOSED`; interruption returns 130 and latches an active consumer.
Clean park returns normally but explicitly reports the unsupported handoff
boundary, not successful multi-day operations. No examples were executed
against live source roots or real volume context.

## Verification Scope

Tests reuse the existing V3 synthetic packet/journal infrastructure, V92
minute/PAPER fixtures and invented calendar/volume helpers. A full 300-minute
test retains the exact artifact and both real models, compares every committed
judgment/evidence/event to direct original `j.process_batch`, and compares
all 211 eligible minute statuses to original V92 nominations. Separate clearly
labeled synthetic inference fixtures force entry/exit/deadline/cutoff cases.
These are plumbing/math conformance tests, not native evidence or market proof.

Additional cases cover exact V3 identity, altered admission/pins/cursors,
stale poll/commit and source stop, first pre09 attachment, immutable causal
context, atomic rollback, restart/event/publication idempotency, SQLite
SHARED-reader and writer contention, sticky restart markers, unsafe latch
links, detached type substitutions, genuine own-tick cutoff draining, CLI
execution, and rejection of successor epochs without ledger reset.

Native runtime compatibility, host-clock evidence, genuine source/volume
provenance, sustained throughput, Windows deployment, future financial-ledger
handoff, and Telegram delivery are not established by these tests.
