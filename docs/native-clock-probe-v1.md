# Native Raw Clock Probe V1

## Reason and Boundary

The current V3 epoch stopped at `unspecified_time_basis_unconfirmed`, while the
NQ December chart still moved. V3 rejects that callback before recording its raw
Time. A separate diagnostic obtains the missing clock evidence without changing
the frozen collector, model, source admission or confirmation setting.

Production source is exactly these four files:

- `tools/windows/time_basis/TimeBasisProbeCoreV1.cs`
- `tools/windows/time_basis/TimeBasisProbeNativeV1.cs`
- `tools/windows/time_basis/AiTraderTimeBasisProbeV1.cs`
- `tools/windows/time_basis/TimeBasisProbeDispatchV1.cs`

Installation or AddOn activation only creates a New-menu item. An explicit Start
in **Raw Clock Probe** subscribes to the selected quarterly NQ/MNQ pair. The
default December 2026 maturity is the already observed chart, not an automatic
rollover decision. Capture stops after at most 120 seconds or 32 Last callbacks
per product. A product reaching its cap does not consume the other product's
budget. No history request, price/volume reading, order, account access,
credential access, network, disk write or automatic clipboard action occurs.

The finished read-only window shows JSON with raw DateTime ticks, `Kind`, roundtrip
text, callback receipt UTC and monotonic counter; configured NT/Windows timezone
IDs and serialized-rule hashes; and the diagnostic assembly MVID. Both the full
serialized timezone rules and their hashes are included. This is clock metadata,
not strategy evidence or normalized source input. Snapshot versus live-update
origin remains explicitly unclassified, including the first callback.

## Provider Snapshots

Windows preparation receipt SHA-256
`730a4e46b1d2fccbe69cad3682da66b8779b0a34afc19086a990a8d4f6fe1d35`
was independently stable-read, SHA and strict-JSON verified on Mac. It confirms
the existing UI displayed Seoul and price connection Connected, without editing
options. These facts do not establish raw callback semantics.

The same receipt binds static public-member metadata to installed Core DLL
SHA-256 `89d30ce74dfb21c26c0819db1f5979799b152d522bbfbc436a3b2cfb495b9408`:
`Instrument.GetMarketDataConnection()`, `Connection.Options`,
`ConnectOptions.Provider` and `Connection.PriceStatus`. The adapter reads only
the provider enum and price-status enum on the instrument dispatcher before
subscription and after removal. It never serializes Options, connection names or
accounts. Null/failing lookups stay explicit. These snapshots do **not** prove
atomic callback origin, failover behavior or vendor-documented clock semantics.

## Lifecycle and Tests

Only one core run can hold the same-assembly lease. Every dispatcher task completes
after the actual action returns. Cancellation or elapsed time makes callbacks
inert immediately, but does not replace registration/removal acknowledgments.
Close cancels and asynchronously joins; there is no UI-thread Wait/Result. If
cleanup fails, the lease stays held and a successor is rejected. A stuck native
dispatcher may therefore delay cleanup beyond the capture duration. This is not
claimed to be a process-wide/multi-assembly admission lock or native lifecycle
proof. The probe never grants admission regardless of the outcome.

`tests/windows/TimeBasisProbeCoreV1Harness.cs` contains 13 synthetic managed
cases: raw kind/tick preservation, caps, expiry, pre-cancel, late registration,
delayed removal, attach/context/callback failures, receipt UTC, one-shot use,
contract/budget validation and failed-cleanup latching. These are not market or
native-runtime tests. Compile the actual core plus this harness into a fresh
non-watched scratch executable with the existing Framework csc, C# 5,
warnings-as-errors and System/System.Core references. Execute that scratch exe.

Separately compile all four production sources into a fresh non-watched scratch
DLL using the installed NT Core/Gui, Framework/WPF and Newtonsoft.Json reference
assemblies. The adapter's actual event delegate and public API types must pass
this native-reference compile. Never load that scratch DLL. A native-reference
compile is still not evidence of a running AddOn or received callback.

Mac static preservation command:

```sh
env PYTHONPATH=src:tools PYTHONDONTWRITEBYTECODE=1 \
  /Users/bkindtoevery1/.local/share/ai-trader/runtime/v111-20260913/bin/python \
  -B -m pytest -q -p no:cacheprovider \
  tests/test_time_basis_probe_v1_source.py tests/test_nq_paper_last_feed_v3_source.py
```

Initial result: 63 cases passed, actual exit 0. Windows receipt
`8fe11d8fd82e3d65a5ed90ea8cb8ca8eaed025df1df04627a63bf9718dccb573`
was independently stable-read, strict-JSON and SHA verified. All 13 synthetic
cases and native-reference compilation passed with actual exit 0. A first
compiler invocation had an agent-owned argument-array error; corrected arguments
compiled the unchanged source. Scratch DLL SHA-256 was
`3cdb010f7efded90eb558ce2b6bf39a3a0d18d10ee83746bcc3a387d8f560fc4`.

The initial revision was NOT ready for installation. Windows source review found
that the adapter discarded the DispatcherOperation: shutdown after enqueue could
abort the delegate without completing its separate TaskCompletionSource. Capture
would stop, but the joined task and window close could hang forever. This is a
source-review defect, not an observed production incident. The next revision
observes the actual `DispatcherOperation.Task`, preserving action-return,
exception and cancellation completion. The separate
`TimeBasisProbeDispatchV1Harness.cs` exercises six cases on actual WindowsBase
STA dispatchers: queued work, delayed action return, action failure, queued
shutdown abort, already-shutdown dispatch and null dispatch. It does not load
NinjaTrader. A harness-only type-name shadowing risk was corrected by fully
qualifying two static Dispatcher calls before final qualification.
Installation, raw capture, source recovery and signal delivery remain unverified.

Final Windows offline receipt
`26560e8be12739c0a102a2d730be074beb13dba0db8b2bb14ead4f39cd50af6a`
was verified as 32336 stable regular bytes with exact SHA and strict JSON. All six
current source/harness pins match Mac. Parent verification also reproduced each
compiler/harness stdout/stderr byte hash and checked actual exits: 6 WPF cases,
13 core cases and the four-source native-reference compile all passed, exit 0.
Final scratch DLL SHA-256 is
`e20c76c1e2fdc2f667491670267761a4a66cf3c3f3d07f8d8ebb3a9722a67d05`.
The initial harness download rejected the superseded pin, as intended; the
authorized type-qualified revision was downloaded separately and originals were
preserved. No installation, F5, restart, native capture, model or message occurred.

Mac focused checks after the revision: 106 passed, exit 0, including the 42
new saved-label audit tests. A full-suite attempt against the initial source was
interrupted after the dispatcher revision: actual exit 2, 2428 passes and one
inherited historical candidate-count failure in its terminal output. Its XML has
an interrupted testcase and is not a complete regression result. The attempt
does not qualify the revised dispatcher. No green full-suite claim is made.

## After Capture

Preserve the exact source/loaded-assembly binding and original JSON. Validate
contract identity, before/after context, raw kind, monotonic progression, receipt
UTC and candidate clock interpretations. Do not substitute receipt UTC for
exchange time or automatically turn on `unspecified_time_basis_confirmed`.
If provider/clock semantics remain ambiguous, report that ambiguity.

Only a separately reviewed time-basis conclusion, current physical settings and
proven V3 retirement can authorize the existing disable/correct/enable recovery
sequence. Completed-minute input, causal context, unchanged model execution and
real signal delivery remain subsequent distinct gates. This diagnostic is not a
replacement for the user's continuous price-to-model-to-Telegram workflow.
