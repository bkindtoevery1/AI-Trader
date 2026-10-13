# V143 Accepted Cell Window Copy Verification

October 13, 2026 UTC. Complete accepted-cell equivalence passed. The proposed
window-copy path did not demonstrate a whole-process memory reduction, so it
does not resolve the failed next cell or authorize collector recovery.
Research remains Mac-only, with 32 of 256 cells accepted and 13,300 comparisons.

## Why This Check

The preceding component test reduced synthetic cold-copy allocation and matched
20 original full-session windows. Neither result established that a complete
teacher-driven account continuation retained all original results. This check
therefore used the last accepted cell, not a selected favorable outcome:
December 8, 2025, cash_plus_headroom, stress, with December 8-19's ten original
source sessions. All 32 accepted cells were semantically validated before
restoring the target account from its same-arm/mode predecessor at index 23.

The unchanged source, teachers, features, actions, costs, sizing, horizons and
account rules were bound before execution by commit
`66083fc3241a9f776aea9c9d61a3fc3f2da30436` and the
[frozen protocol](research-v143-window-cell-protocol.md). The independent test
agent found one genuine defect before execution: sanitized failure artifacts
still allowed private exception text through the CLI traceback. The CLI was
fixed to exit nonzero without that traceback. No scientific rule changed.

## Actual Evidence

The producer started at 16:33:44 UTC and completed at 17:42:26 UTC with actual
exit 0. A separate saved-evidence audit also exited 0 and confirmed:

- Exact byte equality for all rows, evidence, successor state and tape receipt,
  totaling 11,610,675 canonical bytes. This was not a comparison of chosen metrics.
- The original per-cell query delta, NQ 15,187 and MNQ 0, not the preceding
  eight-condition cumulative counter. Zero MNQ calls apply to this fixed cell,
  not the entire research population.
- 67 validated shared cold misses, 2,603 cache hits, zero fallback copies,
  64 retained bindings and three evictions; 17,812 history-copy operations.
- All 270 dependencies and all 99 reference artifacts unchanged, the original
  32-cell cursor retained, and the producer absent after completion.

No new label population, student fit, account score, trial, independent
validation, Windows action or order was produced. The existing failed-root
artifacts, including the incomplete cell 32 marker, remain untouched.

## Resource Limits And Interpretation

| Measurement | Original cell record | New isolated cell probe |
| --- | ---: | ---: |
| Calculation seconds | 3,977.563 | 3,907.604 |
| Process high-water bytes | 5,891,489,792 | 5,974,835,200 |

The new run stayed below the unchanged 8 GiB limit and 5,400-second invocation
limit. Its high-water RSS did not decrease. The modest timing difference and
different process histories do not establish a material speedup or a causal
memory change. In particular, the earlier synthetic 99.5% copy-allocation
reduction must not be advertised as a whole-model memory reduction.

Full-cell semantics are qualified, but the fifth-anchor resource failure is
still unresolved. Next investigate the lifetime of completed temporary fork
results without changing their contents or accounting. Do not automatically
retry the failed root, raise the memory cap, shorten the horizon, discard
labels, or fit only the partial population.

## Regression Record

Focused tests passed 202/202. The final related suite passed 1,285 distinct
tests including those same 202 cases; these counts are not additive. The full
suite attempt retained 1,179 passes, three known out-of-scope failures and one
skip, stopping at the three-failure limit. It is not a green full-suite result.
The same failures concern the older loader's external manifest, the old V78
broker pin, and the historical V123 comparison-ledger field.

An earlier overly broad 2,149-test selection was deliberately interrupted in
the unrelated complete-256 assembly integration after 107 finished passes and
627 seconds. Exit 2 is retained, not represented as a passed suite. The final
selection covers the changed copy/probe paths and existing recovery/checkpoint
dependencies. Financial gates and data requirements were not relaxed.

Private machine-readable receipt:
`reports/nq_apex_continuation_window_cell_v143_20261013.json`.
It retains actual command IDs, exit statuses, artifact and test hashes, the
separate audit source, and full metadata. No market prices or partial financial
outputs belong in the public documentation.
