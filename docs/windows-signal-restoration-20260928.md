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
