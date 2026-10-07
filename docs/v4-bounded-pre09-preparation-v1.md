# V4 Bounded PRE09 Preparation V1

Implementation and synthetic verification only. This is an integration step for
V63/V92, not a Windows model-start result, deployment, source admission, paper
execution, financial commit, or replacement live reader. Only the new helper,
its test module, and this note are changed.

## API And Modes

`tools/nq_v4_bounded_pre09_preparation_v1.py` exports
`BoundedPre09Preparation`, `NEW_EPOCH`, `SAME_SESSION_RESUME`,
`PreparationError`, and `UnsupportedMode`. There is no CLI or `poll()` alias.

Construct a candidate with explicit mode, actual trade date, producer epoch,
normalized NQ/MNQ contracts, capture-ready time, and original consumer-start
time. Call `candidate.run(reader, clock=actual_utc_ns_clock)` with an exact
`BoundedCatchup` instance in its context manager. The existing session import
closure requires both tools and tools/windows to be importable, as in the
existing packaged launcher; this module does not rewrite import paths or
packaged module globals.

- `NEW_EPOCH` supports genuine genesis only. Use `restore_cursor=None` in
  BoundedCatchup and omit previous session/context. It uses the actual pure
  `Pre09Anchor`, leaving all session and paper revisions at zero. Any supplied
  prior session, cursor, or context, even an empty object, explicitly rejects
  this mode. It is not a migration of an existing account or session.
- `SAME_SESSION_RESUME` requires the complete validated `previous_session`,
  its actual committed four-field `restore_cursor`, and unchanged identity,
  including consumer start. Pass that identical restore cursor to BoundedCatchup.
  The caller must already authenticate the session/cursor/context association
  and its freshness as a checkpoint. Hashes and session validation do not prove
  that association or anti-rollback. Raw sequence/receipt continuity is checked
  against the retained session. An empty tail must still equal its durable
  boundary and have a fresh genuine retained pair.
- Resume only accepts entirely pre09 states without V92 position/pending risk
  or any V63 intent. It preserves flat financial values, realized PnL, trailing
  risk, cooldowns, halts, UNKNOWN reasons, model state, all existing revisions,
  consumer start, and bounded opaque `retained_context` without resetting them.
  Context is detached native JSON, not interpreted, authorized, or reconstructed.
  Raw tick counts/sequences advance; financial/model/risk counters do not.
- Different date/epoch/contracts/capture/consumer identity, post09 progress,
  active/pending exposure, or incompatible validators reject rather than reset.
  There is no implicit fallback from resume to genesis.

The packaged carry contract still requires positive paper revisions and an
inner paper revision equal to the consumed tick count. A revision-zero anchor
cannot meet that contract honestly. New-epoch carry of prior financial/model/
context state remains unsupported. The exact packaged `_prepared` validator
is exercised by a rejection test; no counters are fabricated to satisfy it.

## Reduction And Bounds

The helper stages through BoundedCatchup, drains original bounded batches,
then separately obtains its fresh raw boundary. It uses only public reader
methods: `stage`, `next_batch`, and `verify_live_boundary`. It does not read,
borrow, transplant, or publish a private journal verifier or source reader.

Every LF-framed record is checked against its parsed copy, original hash,
contiguous record sequence, previous hash, exact segment name/byte offset,
epoch/contracts, and frozen stage. All records, including startup and health,
are consumed in original order. No sorting, deduplication, filtering, clock
relabeling, or dropping an intermediate offending tick occurs. BoundedCatchup
authenticates the full wire contract, startup sequence, settings, original
restore cursor, disk identities, and failure sidecars. It is not bypassed.

The actual pure minute reducer and receipt raw-tick validator enforce original
per-product sequences, global receipt UTC/monotonic order, bounded event
backsteps/lead/lag, and raw timestamp/offset binding. Both each raw event and
receipt must belong to the actual trade session and precede 09:00 ET. Actual clock
observations must be nondecreasing and in that session's pre09 window. The
session opens at 18:00 New York on the preceding calendar day, using the
byte-equivalent packaged session-date utility; this is not holiday admission.

The resume reducer advances only raw coverage and observation fields in a
detached session, seals with the existing pure APIs, validates the complete
session, and compares the entire non-raw partition against its original.
It never calls a paper tick engine, inference, model loader, receipt builder,
admission, or delivery. No bars or partial minute buckets are allowed.

Defaults are 256 KiB and 256 records per released batch. Accepted budgets remain
128 KiB+1 through 1 MiB and 1 through 1024 records, matching BoundedCatchup. Each
line is at most 128 KiB plus LF. State/context use the existing bounded JSON
validators; the complete returned object must fit 4 MiB. History is never held
as an epoch-sized Python list. Catchup's existing disk/epoch limits are unchanged.
At most 16 stage/drain/live-boundary passes and strictly less than 300 seconds
of actual elapsed clock are allowed. A moving durable boundary is restaged,
never skipped. This is a clock/I/O budget, not a hard real-time latency guarantee.

At completion the original durable receipt must still be younger than 5 seconds.
Both genuine final product ticks must have receipt and event ages strictly
below 60 seconds; heartbeat freshness cannot substitute for either product.
The original bounded future-lead rule is preserved, not normalized away.
Any exception, interruption, invalid clock, stale pair, mutation, or partial
reduction poisons the candidate. No partial result is published. Discard it
and reopen BoundedCatchup from the real committed checkpoint; drained rows
are not committed finance. Successful candidates are also one-shot.

## Result And Integration

The detached result contains `session`, `retained_context`, and a version1
`token`. The token binds prior/prepared session digests, retained-context
digest, actual restore/prepared cursors, durable/settings digests, observation,
and counts plus SHA256 of the exact consumed LF bytes. Resume counts/hash cover
the consumed suffix, not a claim that financial history was replayed.

All authority flags are false, including source/provider/time/model/risk
admission, financial update/commit, carry admission, source-reader priming,
delivery, and orders. Model calls, paper calls, and accounting events are zero.
The preparation digest is an integrity checksum, not a financial/source token
of authority. There is no persisted checkpoint or preparation-token loader.

The parent runner still needs independently reviewed source-owned streaming
priming, runtime and owner qualification, exact candidate-byte reuse, retained
UNKNOWN economic history, a new carry contract where necessary, and an atomic
commit of state/context/evidence with the real cursor. Installing new runtime
hashes is not exact same-binding resume. Recheck current source/owner evidence,
both product health, the actual trade date/pre09 cutoff, and durable boundary
at final commit. This helper cannot guarantee source health after its final
observation and does not authorize entering a live loop.

## Byte Equivalence And Verification

Tests compare complete root and V21/mac-d493 packaged bytes, plus SHA256, for
26 modules covering the actual anchor, session V1/V2, minute/receipt/paper
reducers, session-date utility, raw wire/source, and pure transitive model
definitions. Models are never loaded or called in this suite.

Two distinctions are explicit: the root carry file differs from the packet's
session-open-aware carry file, so the carry-rejection test loads the exact
packaged pure module separately; the transitive
`build_nq_v92_windows_inference_bundle_v2.py` I/O helper differs because the
packet wraps durable receipts with a Windows snapshot implementation. No
whole-runtime byte equivalence or Windows filesystem qualification is claimed.
No source pin, package, original model, or existing module is modified.

All new tests use synthetic journals and actual session/reducer classes, with
inference, fitting, paper processing, and admission entry points guarded against
calls. Invented nonzero checkpoint revisions/financial values in the tests are
validation fixtures, not fabricated execution evidence in the implementation.
Coverage includes bounds, multi-batch memory, original bytes, gaps/duplicates/
ordering, overnight trade dates, every-tick and actual-clock 09:00 cutoff, stale
final pairs, partial-failure poisoning, caller/output mutation, retained-state
preservation, unsupported carry/exposure, tail restaging, and false authority.

The required runtime is
`/Users/bkindtoevery1/.local/share/ai-trader/runtime/v102-20260912/bin/python`,
with `PYTHONPATH=src:tools:tests` and `-B`. No network, Windows actions,
credentials, schedules, orders, commits, financial databases, or market data
are used by this work.

Final focused command (exit 0, **72 passed in 5.70s**):

```sh
env PYTHONPATH=src:tools:tests /Users/bkindtoevery1/.local/share/ai-trader/runtime/v102-20260912/bin/python -B -m pytest -o addopts='' -q -p no:cacheprovider tests/test_nq_v4_bounded_pre09_preparation_v1.py
```

Expanded focused plus predecessor command (exit 0, **488 passed, 1 deselected
in 12.30s**, including 416 predecessor cases):

```sh
env PYTHONPATH=src:tools:tests /Users/bkindtoevery1/.local/share/ai-trader/runtime/v102-20260912/bin/python -B -m pytest -o addopts='' -q -p no:cacheprovider tests/test_nq_v4_bounded_pre09_preparation_v1.py tests/test_nq_v4_bounded_catchup_v1.py tests/test_nq_v4_pre09_anchor_v1.py tests/test_nq_v4_session_minutes_v1.py tests/test_nq_v4_raw_journal_v1.py tests/test_nq_v4_raw_source_v1.py tests/test_nq_v4_session_date_v1.py -k 'not later_real_tick_uses_unchanged_session_engine'
```

The deselected anchor test intentionally invokes the real paper/model processing
path and loads fixed model artifacts. It was excluded to keep this verification
non-inferencing. A predecessor-only attempt before the expanded command exited
2 with one collection error: the existing anchor imports its session before its
test helper adds tools/windows. Collecting the new test module first supplies
that existing dependency path while preserving the required PYTHONPATH. No
predecessor file was edited. Development runs also caught and corrected two
test assumptions: root carry byte equivalence, and a synthetic pending intent
outside the existing validator's permitted decision window.

The bounded memory test checks traced Python allocations below 4 MiB, not OS RSS
or Windows latency. These local synthetic checks do not cover authenticated
source/checkpoint binding, exclusive ownership, actual runtime qualification,
crash-atomic financial commits, Windows filesystem behavior, or live model start.
The parent owns those integration concerns; this component neither rebinds an
old source candidate to a new epoch nor treats the new epoch as an old session.
