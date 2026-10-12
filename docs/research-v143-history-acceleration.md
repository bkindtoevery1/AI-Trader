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
research-v143-history-probe-protocol.md. The pre-execution checkpoint was
committed at26ee71a4 before the actual probe. A separate review reproduced two missing final RSS checks;
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

## Completed Actual Comparison

The sole probe finished at07:18:31UTC, actual exit0/session5307/PID55010.
The retained app command record is exec-d2c8ac42-96b8-48a3-80d0-d8f39049d963,
status completed, duration2,448,886ms. This is external terminal evidence,
not a success flag inferred only from the child's JSON. The process is absent.
A separate saved-metadata/source audit exited0; command record
exec-0d2183de-521d-4f92-8d7d-40db0888b972. All original250 source bindings,
extended source pins, numeric runtime, original interruption, seven recovery
files and the central admission remain unchanged.

Every row, pair record, successor account and original raw/window receipt in
the complete ten-session first cell is byte-identical:1,319,221 canonical bytes,
SHA-256 fb6adf8cbc0d8b87b55501f07bd5eb7314f2cc4a90d142486e0dee6dcff16c77.
The original first roll-in day and13,968 NQ/zero MNQ teacher-query count agree.
The adapter actually ran:16,226 detached history copies,165,644,486 dicts,
147,972,267 lists;2,160 window hits,67 misses,70 evictions,zero fallback.

Calculation time was2,243.675537s (37.39min), compared with the earlier original
2,714.562703s (45.24min):17.35% lower observed elapsed time. Different processes
and uncontrolled machine load mean this is not a controlled speedup estimate
or a guarantee for later cells. Peak process RSS4,801,773,568 bytes (4.472GiB)
stayed below8GiB; earlier original4,898,029,568 bytes. No general memory-saving
claim follows from these two high-water measurements.

Only metadata was published in the new probe root, no new market labels:
attempt.json SHA-256 fb1272cc4062c8f0a4657c54204d39822902e1b5446da82a9100bee7b19eb4da;
completion.json SHA-256 adc2e92d650d818afaf10a02c2999dea5b98cafdb56b75a63fb77e278ccac203.
There is no failure or incomplete temporary artifact. Original scientific
progress remains1/256 cells,0 student fits and0 scored V143 account replays.
No new comparison charge, prospective observation, holdout access or promotion.

The narrow actual first-cell qualification is now COMPLETE. Broad adapter
adoption is still false. Next integrate the qualified path into a bounded
continuation collector without replacing the original prefix, then complete
the remaining255 cells before the unchanged support/fit/75-date account gates.
Do not spend another trial or rerun this cell merely to improve its timing.
