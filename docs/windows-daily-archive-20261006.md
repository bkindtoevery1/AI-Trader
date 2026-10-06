# Windows Daily Raw Archive

User request: inspect the powered-on Windows collector and retain collected
NQ/MNQ data on the Mac every day. Archival is separate from strategy admission.
No collector restart, compilation, login, order, key or firewall change was
requested or performed by the Mac in this work.

## Verified Backfill

At 2026-10-06T12:34:47Z the Mac independently verified 159 published snapshots,
20,903 file references and 11,986,423,924 referenced bytes. These aggregates
exactly match the Windows initial transfer inventory. Content-addressed storage
contains 19,492 unique objects / 10,968,966,386 bytes. Every referenced object
was hashed in full using bounded reads. Ten snapshots are in the conflict lane;
149 are in the ordinary raw-backup lane. No in-flight partials remained.
These are backup snapshots, NOT 159 unique market dates or new model samples.

| Source | Snapshots | File References | Referenced Bytes |
| --- | ---: | ---: | ---: |
| Full-session collector | 21 | 1,920 | 2,833,072,114 |
| Predecision collector | 21 | 1,413 | 1,394,557,078 |
| PaperLast V2 | 1 | 2 | 66,401 |
| PaperLast V3 | 19 | 40 | 49,081,223 |
| PaperLast V4 | 26 | 347 | 4,360,465,616 |
| NinjaTrader native tick | 13 | 15,109 | 3,333,144,648 |
| NinjaTrader native minute | 27 | 2,035 | 15,953,056 |
| NinjaTrader native day | 31 | 37 | 83,788 |

Destination: `data/nq/windows_daily_archive_v1/incoming/` in the AI-Trader
worktree. `objects/<sha256>` holds immutable bytes. Each
`releases/<manifest-sha256>/manifest.json` maps original relative filenames to
objects. `manifest.ready.json` is published only after object verification.
`conflicts/` preserves differing versions instead of selecting a latest winner;
`partials/` is not completion evidence. Native files remain opaque backups.

The five conflict dates are September 28, 29, 30 and October 2, 5, each seen in
full-session and predecision sources. Original invalid markers and source files
are retained. No historical/model/holdout promotion occurs: every manifest and
ready marker has complete_session, model_input_allowed,
holdout_promotion_allowed and orders_allowed set to false.

## Existing Copies And Limits

Earlier transfer was not wholly absent. The Mac already had 13 predecision
staging dates and eight inspection releases. The eight inspected partial
releases represent 21,758,935 rows / 1,047 Parquet files; all their file hashes
were rechecked. Collectors overlap; those counts are not additive unique ticks.

The additional 41.48 GB historical CSV backlog is the same 256 batches already
represented on Mac by 512 Parquet files / 3,405,562,837 bytes. All 256 source
manifest hashes, batch identities and 512 declared CSV hash/size pairs match.
All 512 Mac Parquet payloads were rehashed. Raw CSV bytes themselves are NOT
retained on Mac; the Windows originals remain untouched. The reconciliation
does not claim fresh CSV rehashing, byte-identical CSV restoration or independent
re-decoding of 590,292,939 recorded events. It avoids a redundant CSV transfer,
not deletion of the only CSV originals. No holdout outcomes were opened.

## Operating State

The existing QuantDataPlatform-NinjaTraderInspectionDaily task was updated,
not duplicated. Its principal and action were preserved. The daily anchor is
08:00 KST with a 30-minute repetition for 24 hours, plus current-owner logon
with a two-minute delay. StartWhenAvailable and network availability checks
are enabled. It remains Interactive/Limited/IgnoreNew with a one-hour task
limit. Windows must be logged in; it does not run before login after boot.
Network recovery is picked up by a later poll, not an immediate network event.

An actual Task Scheduler invocation at 2026-10-06 21:35:45 KST exited zero.
Its inventory reconciled all 159 snapshots with zero pending, failed, missing
root or attention items. The observed next timer was 22:00 KST; future timer,
cold-boot and network-reconnect execution were not experimentally observed.
Twenty-four focused Windows tests passed. No full-repository pass is claimed.
An exact remote replay sent zero payload bytes; concurrent queue contention
was rejected with exit 75. Seven delivered source artifacts were hash-verified.

MSIX and scheduled-task filesystem views had differed. The sender now resolves
physical/package source roots and uses one shared state under the Windows
user's local Documents/AI-Trader/QuantDataPlatform/daily_archive_v1 directory.
The 649 metadata files were copied and verified; originals were retained.
Each serial run is limited to 2 GiB, 1,200 seconds and 8 MiB/second; transient
transport attempts use 0/10/30-second delays. Remote free-space reserve is
20 GiB. Receipt publication is last and existing object bytes cannot be replaced.

Windows reported a 35 MB sender working-set snapshot during the transfer;
this is not a measured peak-memory bound. Source files are streamed serially.

The rotating PaperLast journals select old stable segments individually, not
by the mtime of the entire epoch. Current/open segments must be explicitly
reported as deferred, including all-current groups, with persistent first-seen
and 24-hour overdue evidence. This behavior is covered by the delivered tests
and final run. Only two 36-byte October 6 invalid markers remain deferred,
one per V27 collector: COLLECTOR_ARMED_AFTER_SESSION_START. They are not prices.

Final evidence reports V3 startup IOException/latched startup_failed at
19:21:14 KST and V4 enabled=false, unchanged. The latest retained V4 durable
observation is 2026-10-05T14:32:11Z; fresh collection is not verified. This is
NOT proof of a recovered collector, live feed, model worker or Telegram signal.

## Evidence

Private audit artifacts under `reports/windows_daily_archive_20261006/`:

- `published_snapshot_audit_final.json`: all 159 published snapshots and object
  hashes, strict UTF-8 / no BOM / no duplicate keys, regular non-symlink stable
  file reads, manifest identities, byte counts, flags and conflict lanes.
  SHA256 `9fd89c2621f27786543688cf3949e64a4e8a0457d0e14ab55ee1849a849c3092`.
- `historical_raw_tick_parquet_inventory.json`: all 256 prior source/Parquet
  mappings. SHA256 `7ed454e6e69902580a5b175fa88331f518e2461ed731eaf406a3cb5b7833a836`.
- `historical_reconciliation.json`: Windows source index versus existing Mac
  archive; no mismatches and no permission to delete Windows originals.
- `prior_partial_payload_audit.json`: prior inspection payload hash verification.
- `completion_audit.json`: all 159 source memberships and manifest identities
  reconciled with Windows bulk/replay and scheduled-run evidence, 24 focused
  test passes, shared-state/queue checks, and schedule/collector boundaries.
  SHA256 `b05348320d02cce88936dc1e6a080d202e610bd1bea58911b08f6251cd76e6bf`.

Final Windows receipt SHA256 is
`53159292ac68591303c44e710ba5989173ceb96dc51f3b7f83cd4325c046763c`.
It is retained as windows-data.oct6-daily-archive-plan.<sha256>.json under
reports/nq_v92_native_volume_host_v1/incoming/.windows-native-host.sXQKvia1/.

The independent audit verifies byte identity, not provider authenticity,
record-level native formats, market-date semantics or complete session coverage.
Preliminary ad-hoc checks assumed day labels; they were corrected to allow
descriptive epoch/contract labels and opaque native snapshots. No stored data,
admission policy or trading rule changed in that diagnostic correction.

## Latest Read-Only Recheck

At 2026-10-06 23:20 KST, Windows reported that the existing daily task had run
automatically at 23:00 KST and returned exit zero; its next timer was 23:30 KST.
No schedule change or manual task start was needed. The 23:00 completed archive
pass retained 159 acknowledged snapshots, with zero pending, failed, unattempted
or overdue-attention items and no newly acknowledged snapshots. Queue figures
describe that completed pass, not a new source inventory at 23:20.

Seven current-date files totaling 5,709 bytes were deferred until rollover:
three invalid markers and four metadata/control records from the failed V4
epoch. This supersedes the earlier two-file deferred count; it is not evidence
of fresh market ticks or a transfer failure. The separate legacy inspection
queue still has 15 historical source-content warnings, not archive transport
failures; they have not been waived. No UI, connection, login, collector,
rearm, order or source-state changes were performed during this recheck.

The Mac recounted 19,492 object files and 159 published ready manifests and
verified the earlier completion-audit and full-payload-audit hashes unchanged.
The fresh Windows receipt's complete-byte SHA256 is
`8d132b5baad69e15cb884ad9e6e72f11d639bec4c8706da7bd38f32ef1bb2937`;
its content-addressed filename uses the same private incoming directory and
`windows-data.oct6-daily-archive-plan.<sha256>.json` convention above.

## October 7 Midnight Recheck

The existing Windows task automatically ran at 2026-10-07 00:00 KST and
finished with exit zero. At 00:10 KST it remained enabled and Ready, with
zero missed runs and the next run scheduled for 00:30 KST. Its daily anchor,
30-minute repeat and delayed owner-logon trigger were unchanged. No manual
transfer or duplicate schedule was necessary.

A fresh Windows inventory at 2026-10-06T15:10:58Z matched all 159 acknowledged
groups, 20,903 file references and 11,986,423,924 referenced bytes. Missing or
invalid acknowledgements, missing roots, pending items and overdue items were
all zero. The completed midnight pass also reported zero failures and zero
new acknowledgements. This inventory did not rehash Windows source bodies.

The Mac independently streamed and rehashed all 19,492 referenced objects,
10,968,966,386 unique bytes, completing at 2026-10-06T15:10:30Z. All content
hashes, manifest identities, sizes and raw-backup-only flags matched; 149
ordinary and ten conflict snapshots were preserved, with zero partial files.
The private local receipt is
`reports/windows_daily_archive_20261006/mac_payload_recheck_20261006T151030Z.json`.
The fresh Windows receipt SHA256 is
`afe4c78d7dee41b11c582b26f9fd19fd4ae52078011700d2f5c6313f0dbcf6b7`.

Seven files / 5,709 bytes remained deferred: three invalid markers and four
failed-startup metadata/control files, not verified new prices. Archive
eligibility uses UTC calendar dates, so Korean midnight does not release
current-UTC-day files; the next UTC midnight is 09:00 KST. This supersedes
any implication that the previous paragraph's rollover meant KST midnight.

The latest full-session NQ/MNQ raw chunks had filesystem modification times
of October 5, 23:30 KST; predecision chunks were last modified at 23:00 KST.
These timestamps are not a market-content or completeness audit. Daily backup
is operating, but continued fresh collection and live signals remain unproven.
No UI, Connect, rearm, F5, login, collector, model, order or schedule changes
were performed. This recheck changed documentation only, not executable code.
