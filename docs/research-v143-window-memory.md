# V143 Cold Window Memory Remedy

October13,2026 UTC. Mac research only. The preceding batch0006 failed at the
unchanged8GiB high-water guard; accepted population remains32/256. This is an
optional execution-memory component, not a new model or collector recovery.

## Reason And Implementation

The existing immutable-window memo materializes full lists and replacement
tuples on each cold miss, then retains original and copied row bindings. The
candidate validates exact native closed fields and integer tuple rows, runs
the original date and full TickWindow validators, and shares only those
immutable rows. Every window shell remains detached. The cache retains at most
64 strong bindings and is cleared on success or failure. One binding per cold
copy replaces two distinct original/copy bindings; cache diagnostics therefore
differ intentionally. No mutable account history is shared or removed.

Private function views reuse the original population, action-fork and account
execution, qualified history copier, costs, sizing, rollbacks and callbacks.
Non-native shapes and unqualified runtimes take the live original copy path.
This preserves values and scientific behavior, not every immutable row-object
identity. It is not a concurrent-mutation sandbox or collector admission.

Independent review found that the new fast path also needed an explicit runtime
proof for its immutable-row predicate. This is now checked before copying,
after validation, after execution and after diagnostics. Predicate replacement
or bytecode mutation cannot admit mutable inner lists. Review also added
side-effectful fallback, date-fence and compound-error precedence tests.

## Software Evidence

Final affected run passes799 distinct tests, including84 candidate cases;
exit0,77.144s. Coverage includes complete ten-session population/pair/successor
equality after four roll-in days, all modes/phases/arms, callback order, native
and malformed copy behavior, runtime drift and caller rollback/cleanup.

The final full-repository attempt exits1 after1,179 passes,3 previously recorded
failures and1 skip,82.034s. It stops at maxfail3 before the new module, so only
the affected run establishes its coverage. The unresolved failures are the
deployment-loader manifest digest, existing broker.py versus V78 pin, and
missing historical v123 comparison field. No full-green or economic claim.

Earlier qualification had74 focused/789 related passes before review. The first
side-effectful-key test wrongly expected a hash callback from a dictionary fast
path. An equality-callback version then observed5 versus9 calls when comparing
different warmed interpreter states. A four-call read-only diagnostic observed
5/9/5/5 calls inside unchanged original code. The final test compares identical
fresh interpreters, preserving exact callback/error/source-mutation assertions;
the standalone test and final affected suite pass. Both earlier failures are
retained rather than counted as passes. Overlapping suites are not summed.

## Frozen Allocation Comparison

Source and protocol were committed at4099c0cb before measurement. The sole fixed
comparison used separate current/candidate child processes,10 synthetic dates,
both products,50,000 ticks/window and all20 output copies retained:1,000,000 rows.
Both complete output digests match:
59730071ea1bf328036f36ed0c67d8f1335386b6e6c44d4d276c842dc2218b0a.

| Metric | Current | Candidate |
| --- | ---: | ---: |
| Python allocation peak during copy, bytes | 85324368 | 424832 |
| Python retained allocation after copy, bytes | 80036344 | 24216 |
| Whole-process high-water RSS before, bytes | 396378112 | 396525568 |
| Whole-process high-water RSS after, bytes | 606388224 | 396558336 |
| Elapsed copy seconds with tracing | 3.582243 | 1.871838 |
| Cold misses / shared-row windows | 20 / 0 | 20 / 20 |

This demonstrates lower allocation in the fixed copy workload, not an overall
model speedup, exact failed-object attribution or proof that a complete market
cell fits8GiB. RSS includes interpreter/source memory, whereas traced allocation
starts after source construction. Both children prohibit model/source/account
entry points. No favorable rerun or new model comparison is involved.

## Original Window Canary

The single read-only canary exited0 on all20 original full-session NQ/MNQ
windows,13,878,745 tick rows over December9-22,2025. Every original raw and
execution-window receipt matched; all candidate fields and rows equaled the
original cold copies. Shells remained detached and only candidate rows shared
the input tuple. All20 calls were newly validated cold misses, zero fallbacks.

Probe elapsed218.633s; whole-process high-water RSS4,042,260,480bytes. This was
not a controlled per-arm RSS comparison and is not a reduction claim versus
the earlier source-only process. The full267 dependency inventory, source,
runtime, original authority, all99 failure artifacts and32-cell cursor remained
unchanged. No teacher restoration, prediction, label construction, student fit,
account replay, Windows or holdout access occurred. Original tape receipt:
94cf602ec14d053c3fa3469d9bf1562599be23b9f0fd797a8d01c3e8f10d95c7.

Decision: WINDOW_COMPONENT_QUALIFIED_NOT_COLLECTOR_ADOPTED. This passes the
frozen window canary, not whole-cell equality or recovery. Private evidence:
reports/nq_apex_continuation_window_memory_v143_20261013.json.

## Next Boundary

The complete-cell memory failure is not yet fixed in the active collector.
With the window canary passed, the next gate is a separately bounded full-cell
equality comparison against an already accepted original cell, then a reviewed
recovery root preserving all32 accepted cells and the failed99-file inventory.
Do not delete markers, shrink horizons, fit partial labels, change8GiB or retry
the failed producer unchanged. Historical comparisons remain13,300. Windows,
Telegram, live collectors, schedules, spending and orders remain untouched.
