# V137 Outcome-Blind Performance Audit

October 7 KST / October 6 UTC. This is an execution-performance investigation,
not a new model, financial result, deployment or additional model comparison.
The original supervised V137 run remains unchanged and active. No partial
economic outcomes or sealed dates were opened.

## Prototype Evidence

The original execution is session 59712, parent 69853, child 69863. At
16:40:01 UTC it had five completed private label days, zero model artifacts,
no failure or terminal. Its 248 saved source hashes and V136 predecessor
dependencies reverified. The four reserved comparisons remain charged, total
13,262. No process was stopped, restarted or substituted.

An optional adapter reuses only complete validation proofs of immutable native
TickWindows within one event grid. It does not replace the execution kernel,
state/quantity/risk checks or financial arithmetic. A separate optional CPython
3.14 monitoring guard checks immutable code filename/name exclusions with
PY_START, PY_RESUME and PY_THROW rather than a per-call/return profiler.
Both are prototypes outside the frozen source inventory, not adopted runtime.

Parent-owned tests passed 343 unique cases: 95 adapter, 42 monitor, seven
probe-boundary, 27 original labels and 172 original targets. Zero failures,
errors or skips in 2.716 seconds. This is not a full-repository green claim.
Earlier overlapping counts must not be added to this total.

Three synthetic repetitions of a 20,000-tick flat complete-time-exit window
produced identical complete JSON in every mode. Median seconds:

| Product | Original + Frozen Profiler | Memo + Optional Monitor |
| --- | ---: | ---: |
| NQ | 0.842704 | 0.148044 |
| MNQ | 4.054912 | 0.834306 |

These are local invented-input timings, not market-performance evidence or a
whole-run speed guarantee. The [CPython monitoring documentation](https://docs.python.org/3.14/library/sys.monitoring.html)
and [PEP 669](https://peps.python.org/pep-0669/) describe local event disabling
and interpreter-wide monitoring. Testing on the actual 3.14.3 runtime showed
that releasing a tool does not reset previously disabled locations. Therefore
each new exclusive guard scope resets them; a cached allow decision must never
carry into a new deny policy. Generator handlers can catch an injected callback
error, so a separate denial latch still makes the entire scope fail.

## First Real-Day Equality Probe

The separate hash-only probe (session 4763, exit zero) finished
2026-10-06T16:44:17.828192Z. It re-established original source admission in
182.024432 seconds, then recomputed the first complete paired label day in
54.179873 seconds. Its original collector bytecode was retained in private
globals; only the optional label adapter and outer monitor differed.

The 2025-09-08 payload contains 33 original opportunities and 1,436,786 bytes.
All bytes matched the already completed original label artifact:
`196ca099120a116a2ff2bc91c8bd291a54f9ba7b6a5c58fab091ca3eb475f50b`.
The private receipt is
`reports/nq_apex_v137_acceleration_probe_20261007/result.json`.
Only equality, event count and timings were inspected. No label outcomes were
printed, no label files were published by the probe, no models were fitted,
and the original market run was not changed. One-day equality is NOT proof of
whole-population equivalence or permission to replace the frozen run.

## Independent Review Before Adoption

The narrow fresh-interpreter probe has no identified triggering defect, but
the prototype is NOT approved for generic production use. Independent review
identified five cases requiring fixes or enforced fail-closed exclusions:

- Custom instance dictionary subclasses can interfere with window bindings.
- Cached validation must not survive a changed or stateful class validator.
- Private clones must not silently retain rebound runtime validation globals.
- Other-thread profiling is not excluded by checking only the entering thread.
- A deny policy covering context-manager exit can prevent monitor cleanup.

The first three findings used dependency-isolated synthetic definitions; the
last two used fresh CPython 3.14.3 reproducers. No market data was used in review.
Fixes, focused and affected regression, and further hash-only source equality
checks must precede any separately recorded execution-integrity amendment.
No decision about that amendment has yet changed the running experiment.
