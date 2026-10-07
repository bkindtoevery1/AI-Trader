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

## October 7 02:20 KST Recheck

Windows was reachable and returned a fresh read-only receipt at
2026-10-07T02:20:46+09:00. The existing enabled task had automatically run at
02:00 KST with exit zero, zero missed runs, and its next timer at 02:30 KST.
The completed pass retained 159 acknowledged snapshots and reported zero
pending, failed, unattempted, missing-root or overdue items. No duplicate task,
schedule change, manual bulk transfer or collector/UI action was performed.

The Mac independently recounted 19,492 object files / 10,968,966,386 bytes,
159 ready manifests and zero partial files. This was a filesystem recount,
not a repeat payload hash sweep; the earlier complete-payload hash audit
remains the byte-integrity evidence. The new Windows receipt was hashed in
full and matched its content-addressed filename:
`2672aa640d0c5fd10da4f13f50ae0a2352807cb6b6f36e0107e70f554dacaf40`.

Seven files / 5,709 bytes remained deferred under the UTC-date rule. The
latest full-session NQ/MNQ raw chunks still had October 5, 23:30 KST mtimes;
the predecision chunks still had 23:00 KST mtimes. No fresh live-collection
success or newly completed archive payload was observed. Daily archival is
operating, but it must not be described as proof of current tick collection,
model execution or signal delivery. Windows must remain logged in and able
to reach the Mac for its existing Interactive task to transfer data.

## October 7 05:00 KST Recheck

The fresh Windows receipt observed the enabled task at 05:00:27 KST. Its
05:00 automatic run finished with exit zero, zero missed runs and a Ready
state; the next timer was 05:30 KST. The completed pass retained all 159
acknowledged snapshots / 20,903 source references / 11,986,423,924 referenced
bytes. Pending, failed, unattempted, missing-root and overdue counts were zero.
Seven current-UTC-day control/invalid-marker files, 5,709 bytes, remained
deferred. No new snapshot or market-data payload was acknowledged.

The Mac independently recounted the same 19,492 unique object files /
10,968,966,386 bytes, 149 ordinary and ten conflict ready manifests, and zero
partial files. Previous completion and full-payload audit hashes were unchanged;
this recheck did not repeat the complete payload hash sweep. The fresh Windows
receipt was hashed in full and matched its content-addressed filename:
`030850df6cf75552a49b25ed1100d37b8f043089eb1f91e36836e1082b83f7ee`.

Full-session raw-chunk mtimes still ended at October 5, 23:30 KST and
predecision mtimes at 23:00 KST. The V4 journal metadata also remained
unchanged. These observations confirm continued automatic backup, not fresh
market collection or the current UI connection state. No schedule, UI,
connection, collector, account, key or order setting was changed, and no
duplicate archive task or historical CSV transfer was started.

## October 7 06:15 KST User-Requested Recheck

Windows was reachable and returned a fresh configured-root inventory at
2026-10-06T21:15:23.624420Z. All 159 source groups / 20,903 source references /
11,986,423,924 referenced bytes matched existing valid acknowledgements.
Eligible unacknowledged files and bytes, missing roots, invalid acknowledgements
and overdue items were zero. This was a metadata inventory reconciliation,
not a fresh hash sweep of the Windows source bodies.

The existing enabled daily task automatically ran at 06:00 KST and exited zero.
It was Ready with zero missed runs and a next timer of 06:30 KST. Its daily
08:00 anchor, 30-minute repetition, two-minute delayed owner-logon trigger,
StartWhenAvailable and network requirement were intact. No duplicate task,
schedule repair, manual archive run or payload retransmission was necessary.
Windows still needs an interactive logged-in owner and connectivity to the Mac.

The Mac independently recounted and hashed all 19,492 stored objects again:
10,968,966,386 unique bytes, zero content-address mismatches and command exit
zero. There were 149 ordinary and ten conflict ready manifests, and no partial
files. Prior completion-audit and full-manifest-audit hashes were unchanged.
This recheck did not independently parse market rows or repeat full manifest
semantic admission. The fresh Windows receipt was hashed in full and its
content-addressed filename matched SHA256
`720dcfe0e96c7c768d35060d40b269cb778c47c4777175061311d9b95e64b011`.

Eight files / 5,733 bytes remained deferred under the UTC-date rule. The one
additional 24-byte file was a full-session SESSION_ALREADY_INVALID marker,
not a price payload. The other deferred files remained control/invalid records.
The next UTC-day boundary is 09:00 KST; eligibility is not based on KST midnight.
Latest full-session NQ/MNQ raw-chunk mtimes remained October 5, 23:30 KST, with
predecision mtimes at 23:00 KST. No fresh collection, model execution or signal
delivery was established. No UI, Connect, rearm, F5, login, account, key, order,
source deletion or admission change was performed. Executable code was not
changed; this was a live archive integrity and schedule check, not a new
software-regression run.

## October 7 06:55 KST Recheck

The Windows task automatically ran at 06:30 KST and exited zero. At 06:54 KST
it was enabled and Ready, with zero missed runs and the next timer at 07:00.
A fresh configured-root inventory matched all 159 acknowledged groups /
20,903 source references / 11,986,423,924 referenced bytes. Eligible
unacknowledged files and bytes, invalid acknowledgements, missing roots and
overdue items were zero. No schedule repair, duplicate task, manual sender
run or payload retransmission was needed.

The Mac recounted 19,492 objects / 10,968,966,386 bytes, 149 ordinary and ten
conflict ready manifests, and zero partial files. Prior full-payload and
completion audit hashes were unchanged. This was a recount, not another
complete payload hash sweep. The new Windows metadata receipt was hashed
in full and matched its content-addressed filename:
`249c946115135254f26cbaeef47ff3a9e47d7c8a4f8bc68ead2fa5a81ae34865`.

Eight files / 5,733 bytes remained deferred until the UTC-date boundary:
four invalid markers / 120 bytes and four prior failed-V4 control files /
5,613 bytes. Full-session raw-chunk mtimes still ended at October 5, 23:30 KST;
predecision mtimes at 23:00 KST. The latest V4 epoch metadata had not grown.
These metadata observations do not prove current UI connection state, fresh
price collection, model execution or Telegram delivery. Backups require the
Windows owner to remain logged in and the Mac reachable. No UI, connection,
collector, login, order, source, admission or schedule setting changed.
No executable code changed, so no new regression-test pass is claimed.

## October 7 UTC Rollover

The existing 09:00 KST scheduled invocation finished at 09:00:22 with exit
zero. Its 09:04 snapshot was enabled/Ready, missed runs zero and next run
09:30. A fresh 09:05 metadata/ACK reconciliation reported 162 acknowledged
snapshots, 20,911 references / 11,986,429,657 referenced bytes, with zero
eligible unacknowledged files, deferred files, overdue items or missing roots.
No manual transfer, schedule repair or UI action was performed.

All eight previously deferred control/invalid files became eligible at UTC
midnight. Three new manifests reference 5,733 bytes; 120 bytes reused existing
invalid-marker objects and only 5,613 payload bytes were newly transmitted.
This is metadata rollover evidence, not fresh prices or a complete session.
The Windows receipt SHA256 is
`4e3649557e63c0f4995e61d06c9de24022b9b799e4f656a911d20264a5fc51a9`.

The Mac independently hashed the three new manifests and all six distinct
referenced objects, matching their content addresses. Ready markers retain
RAW_BACKUP_ONLY_V1 and all four session/model/holdout/order permissions false.
A recount found 19,496 objects / 10,968,971,999 bytes, 152 ordinary plus ten
conflict ready manifests and zero partials. This is a targeted new-object hash
check plus full inventory recount, not another full archive rehash or admission.

Collector price-chunk mtimes remained October 5, 23:30 KST (full-session) and
23:00 (predecision). V4's latest mixed/control record remained October 6,
22:02:53 KST. Fresh collection, model execution and Telegram delivery remain
unverified. No executable code changed and no new test pass is claimed.

## October 7 11:33 KST User-Requested Recheck

Windows returned a fresh configured-root metadata/ACK reconciliation at
2026-10-07T02:33:33.961914Z. The existing enabled task automatically ran at
11:30:01 KST and finished at 11:30:20 with exit zero. It was Ready with zero
missed runs and next execution at 12:00. The daily 08:00 anchor, 30-minute
repetition, owner-specific logon plus two-minute trigger, Interactive principal,
network requirement and StartWhenAvailable remained intact. No duplicate
schedule or manual sender run was necessary.

All 162 source groups / 20,911 file references / 11,986,429,657 referenced bytes
matched existing transfer acknowledgements. Eligible unacknowledged, deferred,
overdue, invalid-ACK and missing-root counts were zero. No source growth was
detected relative to the 09:00 inventory. This covers configured archive roots,
not every file on the Windows computer, and uses metadata/ACKs rather than new
source-body hashing. Windows originals, including the historical CSVs described
above, remain untouched.

The Mac independently recounted 19,496 objects / 10,968,971,999 bytes,
152 ordinary and ten conflict ready manifests, and zero partial files at
02:32:03Z. The fresh 5,888-byte Windows receipt was read as a stable regular
file, decoded as UTF-8 and hashed; SHA256
`157bfc63544b4de9e5f09320f0540bcfcfa9e0257a01a507aded27b0ef9f8547`
matches its content-addressed filename in the existing private incoming folder.
No new complete payload hash sweep or market-row admission was performed.

Full-session price-chunk mtimes still end at October 5, 23:30 KST; predecision
at 23:00 KST. The most recent V4 mixed/control journal remains October 6,
22:02:53 KST. These are file timestamps, not last-trade timestamps. Daily backup
works, but fresh live collection, model execution and Telegram delivery remain
unverified. No UI, Connect, rearm, F5, login, collector, model, order or schedule
setting changed. This was an operational check and documentation update, not a
software change; no new regression-test pass is claimed.

## October 7 12:04 KST Recheck

The existing 12:00:01 KST automatic run finished at 12:00:20 with exit zero.
At 12:04 the task was enabled/Ready with zero missed runs and next execution
at 12:30. Fresh configured-root metadata matched all 162 transfer ACKs:
20,911 file references / 11,986,429,657 referenced bytes. Unacknowledged,
deferred, failed, overdue, invalid-ACK and missing-root counts were zero.
Neither inventory totals nor the 13 latest collector/native file series grew
since 11:33. This is not evidence of fresh prices, model execution or signals.

The Mac recounted 19,496 objects / 10,968,971,999 bytes, 152 ordinary plus ten
conflict ready manifests, and zero partial files. The new metadata receipt's
full SHA256 matched its content-addressed filename:
`65a8504d2a22806909d4b0b49d19978f490809f57d74ddf4b19cb5cddddf1fdf`.
No new payload hash sweep, manual transfer, monitor, schedule change, source
deletion, UI action or collector restart was performed. The existing daily
archive schedule already satisfies the requested recurring storage. Windows
owner login and Mac connectivity remain required. No executable code changed.

## October 7 12:36 KST Final User-Requested Check

Windows returned a fresh read-only inventory at 03:36:02Z. The existing
12:30:01 KST automatic invocation completed at 12:30:20 with exit zero.
The task remained enabled/Ready, with zero missed runs and the next timer at
13:00. Daily execution, 30-minute repetition and delayed owner-logon triggers
were intact. No duplicate task, manual market-data transfer or schedule change
was needed. All 162 groups / 20,911 source references / 11,986,429,657 referenced
bytes had valid acknowledgements. Unacknowledged, deferred, failed, overdue,
invalid-acknowledgement and missing-root counts were zero.

The Mac independently recounted 19,496 unique objects / 10,968,971,999 bytes,
152 ordinary and ten conflict ready manifests, and zero partial files.
The new receipt was hashed in full and matched its content-addressed filename:
`4e25473a4d57d1ab630959139031de4cef0a63e65414e0228ee15941afca9a86`.
This was an inventory recount and receipt check, not a fresh full-payload hash
sweep or market-data admission. Existing Windows originals remain retained.

All 13 compared latest-file series were unchanged since 12:04. Full-session
NQ/MNQ price-container mtimes still end at October 5, 23:30 KST. These are
filesystem timestamps, not audited last-trade timestamps. Backup is working;
fresh collection, model execution and Telegram delivery remain unverified.
Windows must remain logged in and able to reach the Mac. No UI, login,
Connect, F5, rearm, collector, model or order action was performed.

## October 7 Collector Diagnosis

A separate read-only diagnosis beginning at12:47:54KST examined relevant
V3/V4 lifecycle/error evidence, current settings and disk-headroom conditions.
The metadata-only receipt was delivered after the completed diagnosis; the
checks were not repeated for delivery. Its full SHA256 matches its filename:
`a0016c7d2cf6b9f737238facb3e3f548b99f2c7810e3f58a5fbc974bdd0cade4`.

NinjaTrader PID13432 was running, with process start October6 at09:49:06KST.
That proves neither a collecting writer nor the current feed connection.
Current AddOn supervisor liveness and loaded-memory DLL binding remain unknown.
No fresh lifecycle/recovery evidence was found in the relevant logs.

V4 remains `enabled=false`. The settings hash matches the prior rollback after
one bounded re-enable attempt ending in `startup_fresh_pair_timeout`; it is not
a newly imposed pause in this diagnosis. Current free space is58,046,357,504
bytes, while the configured startup calculation requires60,064,037,989 bytes:
40GiB root budget minus4,360,471,451 owned bytes plus20GiB reserve. The deficit
is2,017,680,485 bytes, so about2.1GB additional free space is a prerequisite.
This current guard failure does not prove the cause of the earlier timeout.

V3 settings remain enabled but its recorded failure is latched `startup_failed`.
The startup catch retained only the simple type `IOException`, not message,
stack, HResult or exact failing path. Neither the original failing physical
path nor a historical disk-full cause can be established from that record.
Logical and explicit MSIX-package views must not be conflated.

The minimum first recovery step is to obtain the missing free space without
deleting original market data or weakening the configured reserve. That step
does not require F5, NinjaTrader UI or restart, but was not performed. Space
alone is insufficient: connection/supervisor state and subsequent V4 activation
still need verification. No blind rearm or claim of working model signals is
authorized by this diagnosis. UI, login, settings, schedules, executables,
source data, models and orders were unchanged; only the diagnostic receipt
was written and delivered through the existing owned-Mac transport.
