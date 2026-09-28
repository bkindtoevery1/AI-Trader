# Windows Signal Restoration: September 28

## Outcome

Native diagnostic collection succeeded: 32 actual callbacks each from explicit
NQ/MNQ December 2026 contracts. This is clock metadata, not synthetic market data
or strategy-performance evidence. Operational V63/V92 signal restoration has
not yet succeeded. No orders or test Telegram signals were sent.

Fresh Windows metadata found the latest Last-feed epoch terminal with zero
accepted ticks. V63's service is running, but has no valid session input package
or signal. V92 remains statically staged and is not executing. A running process
or successful diagnostic must not be reported as a working model signal path.

## Cause And Retrospective

The raw callback clocks have unspecified .NET Kind and are approximately nine
hours ahead of receipt UTC, consistent with configured Korea Standard Time.
That observation is not a provider timezone guarantee. The official
[MarketDataEventArgs reference](https://static.ninjatrader.com/support/helpGuides/nt8/marketdataeventargs.htm)
describes Time as DateTime without specifying this provider's Kind semantics.

The native sample also contains 22, 30 and 42 millisecond event-time backsteps,
and one event 2.9724 milliseconds ahead of receipt under the KST hypothesis.
Frozen producer, journal reader, minute aggregation and virtual execution expect
ordered event clocks. Changing only the confirmation flag would therefore fail
again. The diagnostic approval issue is resolved; duplicate installation,
compilation or approval requests are not the next step.

## Implementation And Verification

A read-only audit now verifies receipt and original JSON hashes, strict JSON,
context/rule hashes, paired contracts, sample sequence and exact .NET 100ns
arithmetic. It independently reproduces the first product-specific rejections.
The audit and related existing source checks pass 92 focused tests. No full
repository rerun or end-to-end signal success is claimed.

The next correction must preserve original event/receipt clocks and callback
sequence, define bounded disorder and minute/execution ordering explicitly,
and retain causal decision/fill timing. Frozen models, old failed epochs,
invalid-session markers and financial ledgers remain unchanged. Short diagnostic
samples do not establish a safe maximum disorder or prove the historical cause
of a separate legacy chunk-order failure.

Private implementation checkpoint: `8b6bf10`. This public note contains no
credentials, account identifiers, raw market payloads or remote-access settings.

## V4 Correction Implemented

Private implementation checkpoint `e0a7e2b` adds an isolated V4 collection
source, schema3 raw verifier, durable reader and event-time minute aggregation.
Frozen V3 and the trained model artifacts remain unchanged.

The new source preserves original event and receipt clocks, raw .NET Time/Kind,
monotonic receipt ticks and callback sequence. Explicit policy bounds allow up
to 250ms event lead, 10s receipt age and 2s backstep from product high water.
These bounds are not claimed as empirical maxima of provider disorder.
Real receipt-clock regression, larger violations and changed timezone offsets
remain failures. No timestamps are clamped or callbacks deduplicated.

Minute open/close use event time with original callback sequence as tie-breaker.
The first next-minute callback cannot prematurely finalize the preceding minute;
closure waits for the product's event high-water minus the full disorder bound.
Local timers do not fabricate completeness, and missing minutes do not create
empty bars. Current outputs are quarantined, not automatically model-admitted.

Verification: 409 focused tests and a separate 398-case legacy compatibility
suite pass. A credential-free, model-free package was sent to the existing
Windows task for its actual 44-case C#5 harness, isolated Python smoke and scratch
compilation against NinjaTrader references. The task was confirmed running;
Windows executable results and native installation are not yet verified.

Remaining work includes native qualification, atomic running-consumer state,
explicit virtual-fill ordering, original V63/V92 input integration and verified
Mac Telegram signal delivery. Collection alone is not completion of the user's
operational objective. No new model fitting, orders or test signals occurred.

## Windows Runtime And Atomic Persistence

Private checkpoint `d70da3f` adds a separate raw-minute consumer and a pure
bridge to the unchanged V63/V92 prediction functions. Cursor, pending buckets
and completed bars commit together; restarts retain genuine consumer start
time and cannot re-emit a committed prefix. The bridge preserves exact model
hashes and complete-prefix timing, including V92's pre09 consumer requirement.
Its outputs remain unsized and quarantined, not tradable signals.

Independent review found hot-journal recovery, fatal-latch contention and
stored-bar corruption defects in the initial consumer. These were fixed with
sealed database identity, immutable fault evidence separate from SQLite locks,
and sticky integrity handling. Ordinary read contention remains retryable by
explicit reopen, not a fabricated fatal source error. Crash-injection and real
SQLite lock tests are included. The final focused/legacy integration suite
passes **1,222 cases**, including 30 consumer and 306 prediction-bridge cases.
These counts overlap earlier runs; this is not a full-repository test or model
performance result.

Actual Windows qualification now passes: **44/44 C#5/.NET Framework harness
cases**, Python3.12 smoke and scratch compilation against installed NinjaTrader
references. The unchanged harness initially failed under a 279-character
temporary path; it passed in 6.12 seconds when paths were limited to231characters.
Both attempts are retained. This supports a test-environment path-length cause,
not a directly captured production exception. Mac also verified original
C#-serialized synthetic journal bytes independently.

Native installation is still incomplete. The initial source-folder preflight
was overbroad: known OneDrive CloudFiles tags and SYSTEM ownership were not
themselves proof of redirection or access denial. Exact tags and ordinary access
checks resolved that issue without permission changes. A subsequent actual raw
directory creation did reveal package AppData virtualization: its physical
location differs from the location expected by NinjaTrader.

The next correction is to qualify an ordinary shared local document directory
and change only the new producer's storage root, preserving existing artifacts,
security settings, old data and financial ledgers. The documented distinction
between AppData virtualization and permitted writes elsewhere in the user
profile is described by [Microsoft](https://learn.microsoft.com/en-us/windows/msix/desktop/flexible-virtualization).
No alternate executor, elevated access, ACL change or virtualized market spool
is being used. Native collection, actual model execution and Telegram delivery
remain unverified. No new fitting, historical trial, order or test signal was
performed in this checkpoint.

## Shared-Root Fix Prepared

Private checkpoint `c9a7ab2` applies the two-line producer-root correction after
read-only Windows checks confirmed the shared local directory and ordinary
access for both existing processes. No new executor or privilege is involved.
The new exact archive preserves old artifacts and changes only the producer
root expression, design note and derived manifest. Its 91 targeted and 1,222
integration tests pass (overlapping counts). Windows is qualifying these exact
new bytes before the requested native install and real collection check; old
source test success is not substituted for that evidence.

Continuous model integration remains unfinished: expected exchange maintenance
breaks, producer epoch changes and genuine model observation windows require
explicit orchestration. A late attachment or a raw-only consumer is not proof
of tomorrow's full model coverage. No working signal or Telegram delivery is
claimed by this checkpoint.

## Native Files Installed; Model Adapters Tested

Private checkpoint `652b997` integrates an explicitly dated 09:00..14:00 ET
predictor window into the raw-minute consumer. Every raw callback is still
validated. Off-window intervals produce no invented bars; missing required
minutes still fail. Genuine capture/start/emission clocks and exact model
artifacts remain unchanged. Day and producer-epoch orchestration is not yet
complete.

A separate receipt-time virtual accounting adapter now delegates unchanged V92
financial math while retaining both original clocks and callback identity.
Fresh traces whose event and receipt times coincide exactly match the legacy
financial results. Disordered traces make no event-time performance or actual
broker-fill claim. Original-event staleness cannot be hidden by a newer receipt;
invalid batches roll back and missing-tick exits are never fabricated. The new
route remains simulation-only and does not authenticate or publish itself.

Verification: **1,634 related cases passed**, including 170 adapter cases and
51 window/store cases. Counts overlap previous component runs. A full repository
run was attempted and deliberately interrupted after 197 seconds, with 1,970
passes and one existing metadata test failure, exit 2. That assertion expects
`Legacy 50K` in unchanged operational-priority goal prose. It is not a new model
performance failure or a green full-suite result; the preceding full run took
approximately one hour.

Windows has independently qualified the revised shared-root producer with its
44-case harness and native-reference compilation. Actual creation of the shared
local raw directory now resolves correctly. The exact new source and settings
are installed, and the old source is unchanged. Fresh UI observations identify
the Seoul timezone and explicit same-maturity contracts.

Native activation and actual Last collection remain unverified: the latest
screen still shows the new AddOn trust warning, despite the reported manual
Yes click. No automated security-prompt interaction, manual compile repetition,
reboot, order, forced model entry or Telegram test was performed. The producer
root contains settings only. Installed files, offline checks and a connected
status are not a completed model-to-Telegram workflow.
