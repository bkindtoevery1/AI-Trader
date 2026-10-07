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

## Integration Review

An independent read-only review on October7 identified four concrete integration
hazards. The packaged launch target is the patched `model_service_v4` alias,
not simply the separately supplied V5 source. Its initial path expects one
complete genesis poll and processes it through paper tick engines; suppressing
output alone would not undo historical position or risk changes. The existing
non-emitting Pre09Anchor has revision-zero financial state, whereas existing
carry evidence requires real positive paper revisions. Never fabricate those
counters to reuse that carry contract.

Ordinary `open_reader(restore_cursor=...)` also replays genesis and imposes the
five-second freshness guard on that scan. Handing a drained prefix back to it
recreates the bottleneck. Runtime hashes are part of the financial binding, so
installing a successor is not an exact same-binding resume.

The required successor therefore needs a genuinely non-emitting pre09 reducer,
explicit new-epoch versus exact same-session modes, and a versioned preparation
proof. Preserve prior UNKNOWN dispositions and financial values independently
of new raw watermarks. A source-owned streaming priming path must independently
verify the prefix rather than borrow this helper's private verifier. Final
commit must atomically bind the prepared state, real cursor, original history,
owner and evidence; only then enter the live loop. Existing source-candidate
bytes stay separate from new runtime qualification. Post09 missed economics
cannot be treated as pre09 preparation. The outer driver's restrictions remain
supplied evidence, not an independent source audit.

No integration or deployment was performed by this review. At05:59:19Z a fresh
Windows metadata receipt showed enabled collection but a last durable timestamp
of05:28:45Z, sequence23,340 and no named V63/V92 worker process. The05:30 automatic
archive run exited0 with pending0, failed0 and128 deferred files/53,384,108 bytes.
Those queue counts are from that completed run, not a new inventory. Receipt
SHA256 is `b8f264c62ba720b19b3bfb8a4c0a278f77e11a320c717f2a35fa995ffe336623`.
It contains no price rows. Stale collection and startup integration are now
separate known gaps; no cause, recovery or model health is inferred.

At06:03Z a second bounded metadata diagnosis found no NinjaTrader process.
Selected logs and05:25-05:35Z power/crash events did not establish why it exited;
memory exhaustion was not proven. With the existing settings unchanged, one
application launch restored a responding process, but the15:10KST observation
showed the username/password login screen. No credential was read or entered,
no connection menu was clicked and no new collector epoch or advancing durable
was verified. The user was asked to complete authentication. No automatic
restart loop, financial-state reset or model start occurred. Launch receipt
SHA256: `03c8e761637a001e021858a8bfde23aa4227303b8dd2a6ced2b224f2361c3787`.
