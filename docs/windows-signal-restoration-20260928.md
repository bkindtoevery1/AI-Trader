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

A separate verified clarification identifies an explicit Windows automation
rule against acting on security/privacy permission requests. The observed
AddOn trust wording was classified under that rule. This is not missing user
installation consent; no backend refusal or OS privilege change was proven.
No click or bypass was attempted. Direct user handling followed by a fresh
native observation is the remaining installation step, not another diagnostic.

## Durable Fixed-Model Session

Private checkpoint `980691f` joins the raw reader, bounded model-window bars,
unchanged V63/V92 calculations and explicitly receipt-time virtual state.
Cursor, decisions, model/virtual state, evidence and outbox commit atomically.
Restarts preserve the genuine attachment clock and processed input identity;
SQLite contention/crash recovery does not reset a financial book. Final model
deadlines are checked again before commit.

Adjacent original journal records are grouped, bounded by 4,096 callbacks or
64 records, without dropping or reordering. This avoids repeating whole-state
work for every small producer flush. It is not yet a measured sustained Windows
throughput guarantee. Earlier prefixes are not retrospectively traded.

Verification: **1,707 related tests pass in 22.69 seconds**, including 19 durable
service and 38 pure-session cases. Invented raw journals feed the real unchanged
model functions in the integration tests; these are not strategy results.
The largest tested serialized evidence is 3,174,646 bytes for 4,096 callbacks
and 600 bars, below the 4 MiB store bound without truncation. Counts overlap
earlier suites. The interrupted non-green full-repository result remains recorded;
no new full-suite pass is claimed.

The runnable service does not manufacture native source receipts, admit new
paper risk or send Telegram. V63 remains its own prediction evidence, not a
V92 accounting substitute. Genuine native/context admission, V63 execution,
daily/epoch carry, Windows runtime capacity and authenticated delivery still
require completion. No fit, historical strategy trial, holdout access or order
was performed.

A fresh read-only Windows observation at 15:52 UTC confirms unchanged installed
pins, the visible trust prompt and zero collection epochs/journals. This is an
explicit unresolved operating state, not a running service wait or signal success.

## Windows Fixed-Model Offline Execution

Private checkpoint `64c2ef5` adds a credential-free, closed-inventory runtime
bundle and isolated smoke runner. Original V63/V92 artifacts remain unchanged;
the archive includes no credentials, market history, native installation,
financial ledgers, settings or scheduling actions. Deterministic publication,
strict member hashes and externally pinned archive identity are tested.

**1,732 related cases passed in 43.48 seconds.** The exact extracted archive
also self-verifies and executes on both Mac and Windows. Windows uses an
existing CPython 3.14.3 environment with the specified package versions; no
package installation or environment modification was needed.

Windows returned original outputs from an independent package check, bundle
self-verifier and one smoke run. All three exited zero, with no retries,
timeouts or stderr. Mac independently checked the six output blobs and every
one of the 34 archive members. Frozen-model outputs agree across platforms
within absolute tolerance `1e-9` on the same invented input.

The smoke exercised 722 invented raw callbacks, 90 complete minutes per product,
once-only fixed-model predictions and two state-preserving restarts. The outbox
and accounting event counts remained zero. V92 rejected the invented nominations
at its unchanged payoff gate. This is **offline software execution evidence**,
not a model-performance result, real market observation or admitted paper trade.

Remaining: native source activation, genuine input/context admission, separate
V63 execution, daily/epoch carry and authenticated Mac Telegram delivery.
Ordinary scheduled-task access to the existing environment is not yet proven.
No security prompt, ACL, privilege, login, schedule, broker order or Telegram
test was changed. End-to-end operational restoration is still incomplete.
The prior interrupted, non-green full-repository test result is unchanged.

## Separate V63 Virtual Execution

Private checkpoint `c1ad5a1` connects a separate V63 virtual book to the durable
model session. It does not send V63 through V92's trading logic. Original V63
size, stop, decision/entry/exit clocks and frozen fee/slippage assumptions remain
unchanged. Long sell-to-exit and short buy-to-exit retain distinct side/action
fields, contract identity, quantity and failed-validation shadow labels.

The new V2 database persists both books, original raw cursor, evidence and
outbox together. Restart cannot duplicate a committed fill or reset an old
ledger. Final commit checks include both event/receipt freshness and original
entry/exit deadlines. A delayed entry commit rolls back instead of being
represented as timely. Existing V1 files and its Windows-qualified ZIP remain
byte-identical; there is no automatic financial migration.

An overstrict assumption was corrected before deployment: V63 can consume its
complete original producer opening prefix after collection began, provided the
consumer observes the original timely prediction. It does not inherit V92's
different pre-opening consumer condition. Pre-admission catchup never fills a
trade; stale active risk and actual source gaps still fail closed.

Verification: **2,145 related tests pass in 67.27 seconds**, including 132 V63
sidecar, 20 combined-session and 22 new durable-service cases. Differential
tests use the existing pure settlement arithmetic as oracle. These are invented
input software checks, not new model trials or an Apex pass. The previous
interrupted non-green full-repository result remains recorded.

Fresh read-only Windows evidence at 16:34 UTC still shows the native trust
warning and zero collection epochs/journals. No explicit connection fields
were visible, so a green indicator was not treated as proof of connectivity.
The production V2 service has no source-admission callback enabled and is not
Windows-qualified. Native activation, actual context, daily carry and real
Mac Telegram delivery remain incomplete. No order or Telegram test was sent.

## V2 Windows Offline Qualification

Private checkpoint `9d29811` adds an isolated V2 qualification bundle without
changing any original model, qualified V1 member or reviewed V2 runtime byte.
The additive archive has 40 entries. Its explicit, closed inventory and externally
supplied archive hash are checked before executing the payload.

The same extracted archive now passes on Mac and the existing Windows CPython
3.14.3 environment. Windows independent verification, bundle self-verification
and one smoke each exited zero, without retry, timeout or stderr. Mac decoded
and checked all six original output blobs and all 40 member identities. Fixed
model diagnostics agree within absolute tolerance `1e-9`; the largest observed
floating-point difference was approximately `3.56e-15`. Windows smoke took
32.346 seconds. No package installation or execution-context change was needed.

The production-service branch uses invented raw data and retains absent source
receipts and an empty outbox. A separately labeled test-only callback exercises
original V63 virtual entry, stop, cent arithmetic, atomic rollback and restart.
The callback is restored and the unchanged V92 financial books remain separate.
These are software mechanics, not native authentication, strategy performance,
market observations or actual paper trades. Test outputs were not sent as signals.

Verification: **36 focused cases and 2,181 related cases across 26 files pass**.
Counts overlap prior suites. Initial Mac extraction through a symbolic-link path
was rejected; identical bytes qualified through the physical path without
weakening the policy. The failed invocation is preserved. The previous
interrupted, non-green full-repository result remains unchanged.

Native activation, genuine context/admission, daily carry and authenticated
Mac Telegram delivery are still incomplete. This handoff did not inspect or act
on the native trust window, start a live service, change schedules or send orders.
Bounded Windows qualification does not establish sustained operation or ordinary
scheduled-task accessibility. Operational restoration remains in progress.

## Source-Bound V63 Service V3

Private checkpoint `c1bddb8` adds a separately identified V3 execution service.
It connects the original V63 prediction to the production virtual-execution
callback only when explicitly reviewed native and capacity evidence is supplied.
Ten pinned inputs are revalidated at consumption and final commit. Hash matching
alone does not prove authentic activation, provider clocks or a connection.
Raw timestamps and false authority flags, fitted models and qualified V1/V2
files remain unchanged. Both books, cursor, evidence and outbox commit together.

Adversarial review found two inherited defects that fixed-clock offline tests
missed: a healthy advancing clock could be rejected after an earlier boundary
check, and an identical context reattached after restart acquired a conflicting
availability timestamp. V3 uses the latest checked clock and preserves the
original exact context evidence. A standalone import-path failure was also
fixed through isolated supplied-module resolution. The qualified V2 bytes are
preserved as offline evidence, not silently relabeled as production-ready.

Verification: **322 focused cases and 2,503 related cases across 28 files pass**,
in 34.41 and 137.22 seconds respectively. Counts overlap; these are software
checks with explicitly invented inputs, not model trials or actual trades.
The V2 archive and all 39 current members were rehashed and remain identical.
An existing goal-prose metadata test still fails independently. No full-repository
pass is claimed, and the operational goal was not rewritten just to pass it.

Fresh read-only Windows evidence at 17:26 UTC still shows the native trust
warning and no collection epochs, journals, durable files or producer lock.
Explicit connection fields remain unknown. No prompt was acted on, no real
approval packet was generated, and this V3 has not been qualified or deployed
on Windows. Genuine V92 volume-chain ownership, daily/epoch financial carry
and authenticated Mac Telegram remain unfinished. No new model fits, market
trials, orders, schedules or Telegram tests occurred. Restoration remains active.
