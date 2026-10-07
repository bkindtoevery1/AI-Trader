# V4 Bounded Catch-Up V1

Implementation only, synthetic-tested; not installed or wired into a model.
No Windows operation, source admission, financial reset, signal, or order is
authorized. Only the new helper, its tests, and this note change.

## Contract

`tools/nq_v4_bounded_catchup_v1.py` supplies `BoundedCatchup`. Instantiate with
an explicit epoch root, separate private local `scratch_root`, and the actual
committed four-field `restore_cursor` (or `None` for genuine genesis). Use a
context manager to close and remove its private SQLite quarantine. No finance
database is opened. Draining records does not commit a financial cursor.

1. `stage(observed_ns, clock=actual_clock)` freezes exact stable `durable.json`
   bytes. It streams the chain from genesis, verifies the restore cursor rather
   than trusting it, and stages only subsequent records. Exact segment names,
   identities, sequence/hash chain, settings, wire timestamp constraints,
   capture-ready, receipts, and failure overrides must all pass before commit.
2. `next_batch()` returns at most 256 KiB of original LF-framed bytes by default
   (plus parsed records and original cursors). All rows are historical quarantine,
   even when their durable receipt happens to be fresh. No callbacks, inference,
   financial transitions, or delivery run. Timestamps and tick order are intact.
3. After draining, `stage()` can authenticate an appended prefix. Unchanged
   authenticated sealed files are identity/stamp checked; changes force hashing.
   The open prefix/new segments are streamed and rehashed before acceptance.
   It never chases a moving EOF, skips an unread prefix, or fabricates a cursor.
4. `verify_live_boundary()` separately requires the drained boundary to equal
   the current durable receipt and remain less than five seconds old at its
   observation checks. `BoundaryAdvanced` requires another stage/drain cycle.
   Other failures poison the reader. This is only raw durable liveness, not
   fresh NQ/MNQ trade health or permission to consume history as live signals.

All output authority flags stay false, including model input, provider/time
admission, financial updates, signal delivery, and orders. Old history is allowed
to be old; future evidence, terminal records and failure sidecars are not.
Even a failure sidecar whose last-durable diagnostic is old blocks release.

## Bounds And Integrity

Parser input is one <=128 KiB wire line, reads are 64 KiB, and SQLite's page
cache is configured to 1 MiB with mmap off and temporary storage on disk.
Segment inventory and staged rows are on disk, not epoch-sized Python lists.
Existing 16 MiB segment/32 GiB epoch limits are unchanged; no pending cap grows.
Scratch needs space for raw bytes plus SQLite/index/journal overhead. Disk errors
roll back the new stage and poison the reader. Scratch is disposable quarantine,
not a recovery checkpoint; reopen replays genesis against the real checkpoint.

Regular non-symlink/reparse paths and stable file/directory identities are checked
before/after reads. Initial/new prefixes are rehashed before staging commits;
release rechecks settings, failure, durable state, identities, and changed bytes.
This detects ordinary filesystem races, not a hostile kernel or process controlling
both the receipt and journal. SHA chains prove byte consistency, not source truth.
Checks cannot lock an external producer or guarantee future health after return.

The inspected V21 packet and root wire files currently match exactly:
`nq_v4_raw_source_v1.py` SHA256
`7019070a36f5b677a22ed90d4fdec78a6e5fe23e2ffd824e6b76a0c3f1960f92`;
`nq_v4_raw_journal_v1.py` SHA256
`6853e3c327d989f95ab9f2864146d8b27528e3b828c8d2722a6a2d839bcec654`.
Tests assert both pairs and replay synthetic output with the exact packet parser.

## Remaining Integration

This intentionally has no `poll()` compatibility alias. A reviewed successor to
the packaged ServiceV5/source configuration/startup route must explicitly consume
historical batches, bind native/source/owner evidence, retain unresolved economic
history, and atomically commit checkpoint/financial state without historical
signal emission. The October-6/short-capture-age startup route, external startup
qualification, current-day policy and current trade-pair health are not repaired
by this helper. The supplied static driver2f15 review also identifies an existing
`source-<epoch>` directory guard in `run_once`: a successor must reuse and
revalidate the exact already-reviewed candidate bytes/hashes at those paths,
not call old `source_candidates` regeneration, overwrite them, or invent a new
candidate identity. This driver observation is supplied integration evidence,
not a new driver audit or edit performed here.

The integration sequence is: authenticate the existing candidate/configuration
and retained financial checkpoint; pass only its actual raw cursor to this
helper; stage/drain history into an isolated, non-emitting preparation path;
atomically commit reviewed state and the corresponding real cursor; repeat for
new tails; then obtain fresh trade-pair/source/owner and live-boundary guards
at the final service commit. Never treat a drained cursor as a committed one,
or transplant this helper's private verifier into a source-admitted reader.

Runtime pins, Windows ACL/filesystem/latency/disk qualification,
exclusive ownership and a fresh commit-time live guard remain integration work.
No additional remote probe is needed to identify those known gaps.

Synthetic tests include >18 MiB/two >8 MiB segments with a <4 MiB traced Python
allocation assertion (not an OS RSS claim), full-chain rollback, mutation,
truncation, replacement, links, missing/duplicate/reordered records, exact restore,
boundary append/rotation, settings and stale/current/terminal failures, and
expired/no-premature publication. Predecessor wire files and bundles are untouched.
