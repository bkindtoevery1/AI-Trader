# Actual Continuation Tape Connection

October 8, 2026 UTC. This connects the continuation implementation to existing
Mac-resident development ticks. It is not a new fitted model, account result,
independent validation or Windows operational recovery.

## Connection

`tools/nq_apex_continuation_tape_v1.py` extracts the original V137 tape path into
one context-managed, contiguous horizon. Prepared content and original context
identities are checked first. Dates must be consecutive entries after the first
teacher's purge and no later than June 12, 2026, before any tape call occurs.
The V87 factory itself does not enforce that development fence, so its literal
`holdout_payload_loaded=False` is not treated as permission or proof.

Each date retains the original explicit NQ contract and matching MNQ maturity,
original events/anchors, full09:31-15:55 ET sessions and original baseline/delayed
event windows. Maturity may change between dates across a roll. Both original
raw and execution-window receipts must match exactly before frames are exposed.
The original scanner still validates complete files; no row filtering replaces
full scanning or before/after hashes.

Each reader is bound to its own date and product map. Reusing an immediate-use
loop closure would bind old frames to the last date. Mutated/foreign events are
rejected before event-window reads, and exported contexts/metadata are detached.
On success or failure all reader caches are cleared and further callback use
is rejected. Retained frame objects still own session tuples: callers must
discard them before loading another horizon. This is not a general guarantee
that all tape memory has been freed at context exit.

Prepared-source and code-byte authentication remain caller responsibilities.
Matching these original receipts does not reestablish upstream-provider
admission or create independent evidence. The existing current-content source
restoration scope is preserved.

## Actual First Window

`tools/verify_nq_apex_continuation_tape_v1.py` completed the fixed first ten
source dates, December3-16,2025, without predicting, fitting, labeling or running
an account. The original20 raw files were fully scanned, with40 complete-file
hash passes and10 envelope rechecks through the unchanged factory. Its full
receipts matched the prepared source. No market prices are published here.

| Measurement | Result |
| --- | ---: |
| NQ execution-session rows | 3,597,127 |
| MNQ execution-session rows | 10,084,508 |
| Combined execution-session rows | 13,681,635 |
| First-event product/delay windows checked | 40 |
| Session copy-constructor calls | 42 |
| Current-content source restoration | 178.315 seconds |
| Tape, copies and bounded event checks | 48.867 seconds |
| Combined measured duration | 227.182 seconds |
| Process high-water RSS | 4,141,924,352 bytes, about3.857GiB |
| Explicit diagnostic budget | 8GiB |

The process already had a3.073GiB high-water mark after source restoration.
RSS is the whole process's cumulative peak, not incremental tape memory or
current residency at each stage. These RTH execution rows are not the earlier
18,406,746 full23-hour source-row count for the same ten dates.

The probe retains the original horizon, a population-style horizon copy, a
fork-style horizon copy and the largest date's working pair simultaneously.
It also checks the first original event in each date for both products and
both delays. The sample is fixed by chronology and row count, not outcomes.
This reproduces one relevant ownership pattern, not a complete fork: it omits
account history, repeated target/branch execution, teacher inference and a full
event-cache population. Other32-window workloads and full training runtime are
not qualified by this result.

Static inspection found60 session-copy calls per successful ten-date action
pair. For `K` reachable targets, the current population path performs
`22 + 60K` such calls, excluding event windows. Repeated copies and historical
snapshot work remain concrete performance concerns before a large market run;
the evidence does not justify shortening horizons or changing targets.

The report is
`reports/nq_apex_continuation_tape_20261007/market-probe.json`, SHA256
`785aab733e8954ab82fe7efd551d91343db7ef102b0b847b781bec811007bf5f`.
Its source binding remains
`333f16a9d173fbd4747f94f1f16b8fdd2769088d27967e38f04331ceccb8fc5d`,
matching the prior restoration. Both probe implementation hashes still match
the report after completion. Actual tool session89741 exited0.

## Verification And Limits

The initial bridge test exposed a tuple/list calendar comparison error; the
internal source calendar is now normalized without relaxing declared input
types. A subsequent test corrected access to the original reader's wrapped
cache inspection API. Nineteen focused cases then passed; five additional
reader-lifetime and native-query checks were added for final qualification.

Two combined runs each reached367 passes, then exposed Python's lazy
`__slotnames__` cache first on the V136 control and then on a phase control.
The original fork test now initializes that standard interpreter cache for
every class it tracks before taking its namespace baseline. Every exact
namespace/member identity assertion remains. Production account/fork code and
the measured probe bytes are unchanged. The initial reports are retained.

The final affected rerun passed799 distinct cases in about263 seconds, exit0,
with no failures, errors or skips. This includes24 new bridge/probe cases and
the unchanged raw-store, native-window, mixed-account, V137 source/replay,
population and action-fork coverage. Earlier focused and partial counts overlap
this total and are not added. Full repository regression was not run.

Final JUnit:
`reports/nq_apex_continuation_tape_20261007/affected-slot-cache-qualified.xml`,
SHA256 `2741d6e017969eadf582b9012d96fe626e244fb31a378135a58ae028baa86844`.

No new market action pair, fitted model, account replay, statistical trial,
sealed holdout access, Windows change, Telegram message or order was produced.
Effective historical comparisons remain13,293. Registered market execution,
full-horizon target generation and complete learned-account evaluation remain.
