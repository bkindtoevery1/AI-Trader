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

## V3 Advancing-Clock Qualification

Private checkpoint `fc1f11d` adds an exact credential-free V3 qualification
package. All 39 qualified V2 members and the reviewed production runtime remain
unchanged. A closed inventory contains 45 payload files and one manifest. Its
C# file is inert identity material, not permission to install or activate anything.

Mac exact-extracted verifier, smoke and isolated service-help all exited zero
with empty stderr. The smoke took 10.126 seconds. Unlike the earlier V2 test,
this run does not replace the production V63 callback. Explicitly invented
private source/context fixtures exercise 712 ticks, 90 complete minutes, virtual
entry/stop, atomic rollback, two once-only restarts and preserved context timing.
The original V92 heads execute without admitting risk or altering their books.
A separate empty invented journal checks 133 records in three transactions and
restart under the actual advancing wall clock. Neither branch is native proof,
a performance result or a sustained market-throughput benchmark. Generated
fixture approvals are removed and cannot be reused as operational evidence.

Verification: **197 focused tests and 2,700 related tests across 30 files pass**,
in 27.55 and 164.56 seconds respectively. The worker's initial broader run used
an environment missing a scientific dependency; that failure is retained and
the parent reran the related scope using the existing qualified environment.
No packages were installed. Counts overlap earlier tests; the prior non-green
full-repository result is not superseded.

The exact offline request was sent to the existing Windows task and an active
execution was observed. Windows evidence remains distinct from Mac results.
The request excludes native UI, trust prompts, real source roots, login, account
state, schedules, orders and Telegram. Actual operation is still unverified.

Private evidence record `6e83d08`: the original Windows coordination turn
subsequently completed, but its original
command outputs and receipt did not arrive. A result-only recovery request was
observed active; later the Windows task was no longer readable or listed. This
does not establish whether the qualification commands succeeded, failed or ran.
It also does not prove the machine shut down. Existing handles are preserved;
no qualification rerun or executor workaround was requested. Windows V3 remains
unqualified until authentic original execution evidence can be recovered.

### Recovered Windows Result

Private checkpoint `fddce5f`: coordination returned and original evidence
resolved the interruption. Independent
archive verification/extraction had passed, but another direct user request took
priority before any of the three supplied commands ran. This was not a test
failure. Mac checked the original preflight outputs and all 46 member pins;
only the unexecuted commands were then continued in the same unchanged stage.

The exact V3 verifier, smoke and isolated service-help now all exit zero on
Windows, with empty stderr and no retries or timeouts. Smoke took **39.817 seconds**.
Mac independently checked all six original output blobs, before/after identities
of all 46 files, the archive, manifest and unchanged interpreter. All non-runtime
results agree with Mac within `1e-9`; the largest floating difference is about
`3.56e-15`. Integer cents and event counts agree exactly. The actual advancing-
clock probe, production V63 callback, atomic rollback and once-only restarts pass.

No original test was rerun, package installed, native collector activated or
actual signal delivered. Private invented approvals were removed. This supersedes
the missing-result state above for **offline qualification only**. Real source
activation, V92 volume-history ownership, daily financial carry and authenticated
Mac Telegram delivery remain unfinished. The full operational goal is not complete.

## Approved Native Collection And Durable Carry

Private checkpoint `059554d`: after the user's Windows approval, fresh native
UI shows both connection and price status **Connected**, with no trust warning.
A bounded 40.228-second observation confirms actual same-maturity NQ/MNQ raw
collection advancing in both sampled intervals. Windows verifies committed hash
chains, product sequences and receipt-clock progression without a failure or
terminal record. Mac checks the original diagnostic output and three original
durable anchors, including exact integer timestamps. This is real collection
evidence, not an inference from task status or file growth alone.

Coverage is limited to those committed prefixes. Raw market rows were not
published or independently replayed on Mac. Loaded managed-binary/source binding,
provider timestamp semantics, complete-session coverage and production source
admission remain separate. The late capture is not backfilled into an earlier
prediction window. No F5, restart, settings or schedule change was needed for
this observation; no model service, order or Telegram send was started.

An additive V4 service implements explicit clean-session financial carry in one
durable database. It preserves V92 losses, cash and trailing state, and separately
accumulates settled original V63 costs and PnL. New-day source clocks, sequences
and context remain genuine; existing databases are not reset or migrated. Exact
qualified V3 payloads and both original fitted models remain byte-identical.

Independent review found five predeployment defects: checkpoint replacement,
stale-owner failure latches, nonsticky park failures, missing-ledger inception
reset and hot-journal recovery. Fixes add transactional state commitments,
checkpoint-scoped latches, durable park errors, refusal to recreate established
accounts and a mandatory latch recheck after sealed SQLite recovery. The final
review found no further blockers.

**144 focused/adversarial tests pass in 235.85 seconds; 2,700 related tests across
30 files pass in 168.55 seconds.** Tests use invented private inputs, including
actual crash subprocesses. The prior non-green full-repository result remains
documented. These are software checks, not model profitability or an Apex pass.

V4 has not been packaged, qualified or deployed on Windows. Automatic multi-day
source management, genuine V92 context ownership and authenticated Mac Telegram
delivery are unfinished. No new fitting, historical search or holdout observation
was performed. The operational goal remains active and incomplete.

## V4 Exact Lifecycle Package

Private checkpoint `5929ef9` packages the reviewed V4 runtime while preserving
all 45 exact V3 payload members. The credential-free archive has 50 payload
files and one closed manifest; all installation, service, source, delivery and
order authority flags remain false. No native collector or existing paper
ledger is replaced by this package.

Mac exact-extracted verification, standalone smoke and isolated help pass with
empty stderr. The smoke takes **85.328 seconds** and matches the worker's stdout
byte-for-byte. The unchanged production V63 callback and real ledger service
consume 1,154 invented ticks, close 300 minutes per product, park, and carry a
simulated loss of **20,408 cents** into one later fixture session exactly once.
Five restarts preserve evidence and three outbox events; zero deliveries occur.
All 50 files stay unchanged and private invented approval scratch is removed.
V92 context is absent and its head evaluation count is zero: this run does not
qualify V92 decisions, real sources or market throughput.

**112 focused tests pass in 3.81 seconds; 2,298 related checks across 29 files
pass in 398.32 seconds.** Counts overlap and are not strategy trials. The prior
interrupted non-green full-repository result remains documented.

A distinct Windows existing-evidence audit identifies missing owner-to-epoch /
loaded-assembly linkage and current instrument-routing metadata in the actual
source. Older clock samples support Seoul empirically but do not establish the
provider-specific timestamp contract. This is an implementation/evidence gap,
not missing user consent. No repeat live canary, F5, restart, source or schedule
change occurred; the collector was left untouched.

The exact new archive was dispatched to the existing Windows task, whose active
handle was verified. Windows qualification remains pending its original outputs,
not inferred from Mac success. Preserve that handle and do not duplicate the job
because an observation times out. Native admission, V92 history ownership and
actual model-to-Telegram delivery remain unfinished. No fit, holdout observation,
order, Telegram send or strategy-pass claim was made.

## Windows V4 Pass And Prospective Owner Binding

Private checkpoint `154618c` records the exact Windows lifecycle package result
and adds the missing prospective native owner observation. The original Windows
job completed normally; it was not duplicated when observation waits expired.

Windows independent preflight, verifier, lifecycle smoke and help exit0, with
empty stderr and no retries/timeouts. Smoke takes222.901seconds. Mac independently
checks original output bytes, all51 archive/before/after pins and runtime
identity. The54 integer results match exactly; only OS, architecture and timezone
package availability differ. Both hosts record399cycles,1154invented ticks,
five restarts, one financial carry and no duplicate carry. Invented approval
scratch is removed. V92 head evaluations remain zero: this is software lifecycle
qualification, not V92 decision validation, strategy performance or live service.

The current collector still lacks owner-to-epoch/loaded-assembly linkage. A
separate replacement candidate captures that context from its actual owner,
then publishes an immutable bounded observation after the first two raw records
are durable and before subscribing to prices. It records per-instrument
connection snapshots and both timezone contexts. Missing file or route facts
remain unknown; file hashes do not prove loaded-memory identity, and connection
snapshots do not prove callback-atomic routing or provider clock semantics.

An independent Python reader checks the exact original initial records,
settings, schema/types, chronology and file bounds, but never grants source or
model admission. Existing collectors, model packages and fitted models remain
unchanged. A review caught an oversized time constant in the synthetic C#
harness before dispatch; a regression now catches out-of-range long literals.

**823 related tests across10 files pass in3.30seconds**, including69 C# static
checks. These are not actual C# execution; the previous non-green full-repository
result remains documented. Exact candidate and15-case executable harness were
sent for bounded offline Windows compilation/execution, with the task confirmed
active. No native replacement or restart was performed. Real source admission,
original V92 context ownership and authenticated model-to-Telegram operation
remain incomplete. No new fitting, holdout observation, order or test message
occurred. Model operation remains the priority, not completion by diagnostics.

## Native Candidate Qualified; Application Not Completed

Private checkpoint `1932fd8` records actual Windows qualification of the exact
prospective owner-binding candidate: C# harness compile, all15 executable cases
and native-reference scratch compile pass. Mac independently verified the six
original output streams, source/reference pins and original C#-emitted synthetic
sidecar/settings/initial-record bytes. The read-only Python checker accepts
their structure without granting native or model authority. A focused recheck
passes179cases; the previous non-green full-suite result remains unchanged.

Native application did not occur. The current user approved the bounded
single-source replacement and one F5 in the Mac task, but the Windows executor
could not independently retrieve that user turn. An initial hostless lookup
searched Windows only; a corrected inventory still exposed no Mac task there.
Windows' latest retrieved direct approval concerned the earlier AddOn, not this
new replacement. This is asymmetric task visibility, not proof of a network
failure or a claim that the user withheld consent. No alternate executor or
permission bypass was used. Backup/replacement/F5 counts remain zero.

The next requirement is a directly available current answer in the Windows
task or supported retrieval of the Mac user turn, not another offline test or
reapproval of the old trust dialog. Both follow-up tasks completed; no native
application job is still running. Original V63/V92 real-data signal operation
and Telegram delivery remain unfinished. No order, test message, new fit,
historical trial or holdout outcome access occurred.

A separate V92 integration audit identifies actual implementation gaps:
same-owner deferred context attachment, durable pre-read intent and a V4-specific
receipt callback. Its required prior20 volume sessions need genuine provenance;
they do not inherently require waiting20 new trading days. No substitute model,
invented context or relaxed statistical gate was introduced.

## Deferred V92 Context Read Barrier

Private checkpoint `6ceecff` adds an in-process controller for the exact running
V4 service. It durably records a single session-scoped context-read intent before
the existing loader reads history. It preserves genuine pre09 startup and first
successful context availability. Interrupted reads can retry only the same path,
digest and helper/runtime identity; prior attachments cannot acquire retroactive
intent. Existing service, session, model and qualified archive bytes are unchanged.

Independent review identified postcommit foreign-checkpoint adoption and clock
regression between attempts. Both are corrected. Tests exercise separate SQLite
connections, rollback, competing owners before/after commit, restarted attachment,
explicit object identity, actual-clock bounds and continued synthetic model
cycles. **37 focused cases and 697 related cases across nine files pass**; the
final related run takes174.57seconds. These are invented software fixtures, not
market/strategy validation. The full repository suite was not rerun.

The controller returns structure-only results and grants no V92 paper admission.
Automatic deferred launcher integration, genuine volume-acquisition/conversion
lineage, the V4-specific V92 receipt callback, new-source admission and actual
Windows-to-Telegram operation remain incomplete. Windows supplied no new native
application result during this work. No new fit, order, live context read,
holdout outcome access, connection or schedule change was performed.

## Original V92 Receipt Controller

Private checkpoint `a5e3285` implements the missing metadata binding and original
V92 paper receipt controller on the exact existing V4 owner. Frozen models,
services, collectors and previously qualified packages remain unchanged.
The metadata loader joins native/converter intent and terminal evidence with
reviewed prior20 dates, explicit contracts, calendar, timezone and raw pins.
It reads no historical result or context file. Hash equality is not provenance;
an independently authenticated deployment/source/volume bootstrap is still needed.

The controller attaches context through the existing durable read barrier and
joins both raw and canonical identities to the committed attachment. Inside its
owned transaction, the receipt callback recomputes the unchanged V92 prediction
on the exact prefix, calendar and history. Cursor, financial state, receipts and
outbox commit together. Original costs, sizing and final decision/entry deadlines
remain enforced. These are paper events, not broker fills or delivery authority.

Independent review found restore-before-poll, parked-reopen, preflight-fault and
orphaned-registration gaps, plus cached authority surviving damage to attachment
evidence. The implementation now checks original dependencies inside transactions
and commit guards, requires explicitly pinned restoration before consuming new
prefixes, detects retained checkpoint witnesses, and preserves the winning ledger
when a stale owner fails. Tests also confirm a post-cost unprofitable entry is
still refused; the implementation does not force an entry to satisfy a test.

**146 focused cases pass in173.89seconds; 1,237 separate related cases across11
files pass in259.07seconds.** All use invented source/volume fixtures and trust
roots. One path retains the original forecasts; positive-forecast branch tests
are explicitly synthetic control-flow tests, not evidence that V92 is profitable.
The previously recorded non-green full-suite result is not relabeled as a pass.

No new Windows native installation result arrived; the existing task is idle,
not an active installation job. Genuine volume authority, the reviewed successor
source binding, launcher and authenticated context delivery, Windows qualification
and actual model-to-Telegram operation remain incomplete. No new model fitting,
historical search, holdout outcome access, actual order or test message occurred.

## Same-Owner Launcher And Exact V5 Package

Private checkpoint `9a57b0a` adds the executable original V92 paper launcher.
One externally authenticated command can arrive while the same service keeps
polling. Command, original metadata observation and registration plan are durable;
partial recovery retains both original observation clocks rather than inventing
earlier availability. Restart checks the same source, code and ledger identities.
The original metadata loader, models and qualified V4 payload remain unchanged.
An input pipe and matching hashes do not independently authenticate provenance.

Combined launcher/package/volume/runtime tests pass 208 cases in 184.36 seconds;
standalone smoke tests pass 44 cases in 33.05 seconds; V4/V5 package regression
passes 105 cases in 2.31 seconds. Counts overlap. The full repository suite was not
rerun and its previous non-green result remains unchanged.

The exact 412,828-byte V5 archive has 64 payload members plus its manifest.
All 50 qualified V4 payload members are preserved. A newly extracted Mac payload
passed verifier, smoke and standalone help with exit zero, empty stderr and
unchanged before/after hashes for all 65 files. Smoke took 14.88073 seconds and
exercised 101 virtual cycles. Original V92 evaluated all four heads once per
product and correctly made no selection on invented data. The actual Launcher
also exercised deferred binding and restart after invented input removal.
These are software tests, not performance or real-market operation evidence.

Windows received the exact credential-free offline qualification request, and
the task was confirmed in progress. This is not a native installation or a live
model job. Current user consent remains recorded; no repeated approval request
or native confirmation bypass was made. A later status lookup returned no
readable remote task, so completion must be checked from the returned receipt,
not inferred from that transient observation failure or assumed successful.

Genuine prior-volume authority, reviewed successor source admission,
authenticated cross-host control delivery, native application and sustained
model-to-Telegram operation remain incomplete. No model search, holdout outcome
access, actual order, forced selection or test message occurred.

## Windows V5 Qualification Completed

Private checkpoint `65af3df` records the independently verified Windows result.
The exact archive passed independent preflight, self-verifier, original V92 and
Launcher smoke, and standalone help. Supplied commands exited zero in 0.2430405,
50.5647334 and 3.2739193 seconds. All stderr was empty; no supplied command
timed out or retried. Synthetic scratch was removed after child completion.

Mac verified the 65,415-byte receipt, eight original output streams and all 65
member length/hash pairs against its exact archive. Original inference and
Launcher recovery agree across hosts: all 33 integer leaves match, and one
forecast scalar differs by only 4.44e-16. Both products correctly reject selection
on invented input. Expected platform differences are OS and timezone package.
This is software qualification, not model profitability or live operation.

The initial audit recognized a null-versus-string timezone-package field after
first stopping on it; no evidence was changed or Windows command repeated.
Windows had also shortened a planned scratch path before any supplied execution.
No runtime, frozen model or qualified package bytes changed in this follow-up.

The completed qualification job is no longer described as running. A separate
bounded native follow-up was dispatched and independently confirmed active. It
checks newly available user answers before any previously requested source
replacement/F5, honors the existing action-time confirmation boundary, and must
return a concrete blocker once if that answer still cannot be retrieved.
There is no repeated approval question or substitute offline testing loop.
Native deployment, real model execution and actual signal delivery remain
unverified; the broader goal is not complete.

## Correction: Approval Was Earlier Than The New Candidate

Private checkpoint `6542807` corrects the previous approval interpretation.
The coordinator inspected its actual user message through supported task
retrieval: that recheck/approval statement was at 18:37:58 UTC. The newly added
candidate's replacement/F5 action-time question came later, at 20:16:36 UTC.
Treating the earlier statement as subsequently received confirmation was wrong.
Restoring cross-host visibility would not make it confirmation of that later
action. The prior AddOn consent remains valid for its original scope.

The bounded native follow-up completed without changes. Mac verified its
4,317-byte receipt and expected installed-source, settings and candidate pins.
No native replacement, F5, model start or Telegram send occurred. The correction
was sent to Windows with no further diagnostic, approval question or execution.
The job is terminal, not running or silently proceeding toward deployment.

A genuinely new direct action-time answer is necessary for that later native
application. Repeated lookup, offline testing and old consent are not substitutes.
The exact Windows V5 offline qualification remains valid, but real model-to-signal
operation remains incomplete. No runtime or frozen model code changed here.

At 22:20:28 UTC the goal API confirmed `blocked`, with both original objectives
unchanged (private checkpoint `00aed96`). The same external confirmation boundary
persisted across three consecutive turns; the Windows task is terminal, not a
live wait. Qualified artifacts remain intact. No repeated lookup, synthetic
qualification or new historical search substitutes for the missing native action.
Resume on a genuinely new direct confirmation or material external evidence;
native application, authentic context and real signal delivery remain unproven.

## September 29: Native Applied, First Two Models Prioritized

A new direct user confirmation resolved the previous native action-time blocker.
The exact reviewed collector replacement was installed and a new actual owner
appeared before the planned compile input, so no redundant F5 or restart was
performed. Mac independently verified the original metadata bytes, loaded-owner
identity, unchanged settings and advancing explicit-contract NQ/MNQ streams.
This supersedes the earlier native-blocked readiness assessment, not its history.

Private checkpoints `06fe7cb` and `5d3ed53` introduce and record a separate
observed-source policy for receipt-time shadow simulation. Formal provider
callback binding and vendor timestamp guarantees remain unclaimed; original
native flags remain false. The package explicitly replaces the admission API
implementation while preserving the original fitted V63/V92 models, inference,
sizing, costs, stops, decision windows and exact prior qualified archive. A
separate owner supervisor retains a one-command reviewed context channel without
restarting the inference owner when genuine volume context arrives later.

Private checkpoint `92500b9` adds independent V63/V92 committed-event publishing,
SSH transport and Mac-only Telegram delivery. Whole source-bound wrappers remain
intact, each model has its own pinned identity, SQLite writer contention retries
without advancing an unprocessed row, and uncertain Telegram sends require
reconciliation. Korean messages distinguish NQ/MNQ, long/short, entry/full exit,
quantity and conditional stop/target P&L. There are no broker orders or fabricated
signals. Telegram credentials remain exclusively on the Mac.

Focused verification: 512 source/package/owner/delivery tests plus 110 provenance
tests passed. The full repository attempt was stopped after 2,574 passes and
three unrelated failures in 438.95 seconds: two old research seals expect the
historical broker source bytes, and one assertion expects account wording in
the operational-priority goal. Existing user edits and historical seals were
not rewritten to turn those assertions green. This is not a complete full-suite
pass, nor a model profitability result.

The Mac bot identity was confirmed without sending a message, and its new relay
is running with an empty separate inbox. Windows model-owner and signal-sidecar
execution requests were dispatched; actual operation and end-to-end delivery
still require returned evidence. Genuine V92 prior20 volume context is not yet
admitted. The latest user explicitly prioritizes completing V63 and V92 before
any V102 addition. No new model fitting or historical outcome trials occurred.

### Actual First Start Failed

Returned Windows evidence supersedes the launch-requested status above. Source
admission passed, but the first actual model-owner start failed before committing
any source cursor, model attempt or signal. A separate read-only diagnostic
reproduced the frozen 8 MiB live pending-budget error on the accumulated startup
journal. Shutdown also exposed a buffered-stdin daemon-thread defect. The failed
ledger and original logs remain preserved; no reset, increased live limit or
automatic retry was performed. The Mac relay waiting on an empty inbox is not
end-to-end success. V63/V92 initialization repair is in progress, and V102 remains
deferred until both original operational signal paths are demonstrated.

Private checkpoint `aae34f8` implements the narrowly scoped recovery: V7 retains
every V6 member, audits a pinned zero-activity failed predecessor without editing
it, validates the original raw prefix in bounded memory, and commits pre09 raw
anchors without retroactive bars, predictions or fills. Genuine observation times,
original live pending/freshness limits and all fitted-model bytes stay unchanged.
An independent review identified commit-time quote aging and a clock-regression
gap; both were fixed with rollback regressions. The separate v2 control reader
uses unbuffered descriptors to avoid the shutdown defect.

Focused verification: 468 passed. A further whole-repository attempt stopped
after 1,509 passes and the same three unrelated failures in 155.97 seconds; it is
not a full-suite pass. The exact V7 request authorizes one actual Windows launch
only after package/source/predecessor verification. A new V7-pinned Mac relay is
running with no test message; the obsolete owned V6 relay was stopped only after
its inbox was confirmed empty. Windows runtime and end-to-end delivery still need
returned evidence. V92 additionally has an unadmitted genuine prior20 context and
a frozen calendar-day restriction conflicting with the overnight native capture.
Neither problem is hidden by falsifying dates, resetting the source, or claiming
two working models. Operational success also does not mean a profitability pass.
