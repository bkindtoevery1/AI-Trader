# V143 Detached History-Copy Qualification

October 12, 2026. Mac-only research; no Windows, live-system or trading action.
The preceding recovered cell remains 1/256, not a fitted or passing model.
This work reduces redundant copy calls without changing the strategy, targets,
ten-session horizons, costs, sizing, embargo or closed holdout. The original
interrupted root, completed first cell and 13,300 comparisons are preserved.

## Implementation And Rationale

The prior synthetic profile attributed substantially more time to account/
history deepcopy than to window copies. The new optional component is
tools/nq_apex_continuation_history_acceleration_v143.py. It combines the existing
64-binding immutable-window memo with private CPython 3.14 copy function clones.
Native list/dict loops reuse only CPython's exact atomic types; every mutable
history is still copied. The original deepcopy and reconstruction bytecode
retains alias/cycle memoization, keep-alive, reducers, custom protocols, tuples
and methods. Dict value-before-key callback order is preserved.

Private forwarding views also route the dynamically created continuation
account's process_day snapshot copies through the detached copier. No frozen
module, method, global dispatch table or copy registry is patched. Unqualified
public calls fall back to the live original; tracked drift during a qualified
call raises. The actual-data probe requires qualification and no fallback.
Shallow runtime checks are not a hostile concurrent-mutation sandbox. The
separate runner authenticates all original 250 dependencies and the explicitly
extended wrapper inventory before and after use.

## Synthetic Evidence

The first parent smoke exited 0: complete rows, evidence and successor match,
with qualification true before/after and 56 history copies, 1,121 dicts and
626 lists. The complete six-run dense benchmark also exited 0, session17773.
It uses the unchanged invented workload from the earlier copy benchmark:
ten dates, two events/date, 30,000 session ticks/product/date and 2,001 ticks
per execution window, with fixed original/candidate/candidate/original/
original/candidate order. No market data, teachers or fits are loaded.

All six outputs are exactly 77,818 bytes with SHA-256
36d1348a00c46b6efe7b7bc89c3c21e1cfed57635f4e13e4b49bf16a630fa66a.

| Implementation | Three Elapsed Times (seconds) | Median |
| --- | --- | ---: |
| Original | 2.957452, 2.988735, 2.970648 | 2.970648 |
| History + window adapter | 2.571068, 2.585741, 2.602098 | 2.585741 |

This is about 13.0% less median elapsed time (ratio1.148857), not a confidence
interval or a proven market speedup. Each candidate run performs 259 history
copies, 177,225 dict copies, 89,248 list copies, 171 window hits, 39 misses,
14 evictions and zero fallback. Whole-probe high-water RSS488,947,712 bytes is
not a per-implementation memory measurement. Machine load was not controlled.

The affected regression passes 1,215 unique tests, actual exit0/session33205,
57.871 seconds, no failures/errors/skips. This includes the agent's 205 new
cases; do not add the earlier overlapping agent run to the total. Coverage
includes graph/memo/protocol parity, callback order/errors, private account
wiring, all modes/phases/roll-ins, complete ten-date parity, rollback, detached
histories, runtime drift and cleanup. One initial test command named a missing
file and exited4 before running tests; the corrected complete run is above.
JUnit SHA-256:
ffb05f4a02eec35ae5861c7962c9a99e52256c2a85fc5048650ed5d6c0552f17.

The fresh full-suite attempt stopped at three previously documented failures:
1,179 passed, 3 failed, 1 skipped, actual exit1/session73417, 80.433 seconds.
The causes remain the isolated deployment-loader manifest mismatch, pre-existing
broker.py drift against V78 evidence, and absent v123_counted_comparisons in
the historical ledger. No unrelated evidence or source was weakened to pass.
JUnit SHA-256:
360730ddbb9a327e2989d285929c47c05a8781c38066a9c9564d15e91b9bf93d.
This is explicitly not a whole-repository green result.
After the two probe RSS fixes, a final full-suite attempt repeated the same
1,179 passes/3 failures/1 skip in80.541 seconds, actual exit1/session17512.
Final JUnit SHA-256:
9ad224f4f8c16f26f463dabf5b7c25130351537e4f2d54fba88e1b1f059168ac.

## Actual First-Cell Probe

The metadata-only procedure is frozen separately in
research-v143-history-probe-protocol.md. At this checkpoint the actual probe
has not run. A separate review reproduced two missing final RSS checks;
both were fixed before any market calculation. The new probe/recovery run
passes235 cases, actual exit0/session84477 in6.709 seconds, no failures/errors/
skips. Together with the affected run this is1,450 disjoint passing cases,
not1,450 model validations. Focused JUnit SHA-256:
764ea42eff14f4879ee834560f6c8f16772783789b50e37ce041fdcc6650d986.
The original-source/runtime/reference read-only preflight also passed,
actual exit0/session49482. The hash-bound central admission is recorded
before execution; independent final review found no remaining practical blocker.

The probe must match every first-cell row, pair record, successor and
tape receipt, preserve the original first-day account and exact query count,
and finish with external exit0 under the unchanged 8 GiB memory guard.
No later cells, student fit, economic pass or adapter adoption are inferred
from synthetic software tests.
