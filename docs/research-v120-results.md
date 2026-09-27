# V120 Technical Abort, Not A Trading Verdict

The one actual market child exited1 at2026-09-27T10:18:48Z. Six causal forests,
384 trees and18 durable fit stages completed. The runner then failed in
validate_learned, before calling the account replay. There are no new account
results, no published economic outcomes and no evidence of a V120 trading pass
or trading failure. The four reserved comparisons remain charged: total13213.

## Cause

The frozen forest stores exact integer-cent targets in a float64 array and exports
JSON float values. The frozen daily-distribution contract requires JSON integers,
so the pipeline converts those already integral values to int. The runner's added
arm/fold protection incorrectly compared canonical JSON bytes for these targets.
For example, a synthetic120.0 and120 have equal exact cent value but different
JSON bytes. This is a boundary-validation defect, not changed financial values.

A read-only audit validated all six pinned exports. Their row counts are1335,
1335,2372,2372,3391,3391, each with four target columns. All56784 cells are finite,
exactly integral and bounded by2**53. Integer conversion preserved every numeric
value and changed the encoded representation in every export. No target values,
predictions or partial economics were printed by this audit.

## Why Tests Missed It

The standalone pipeline tests used actual synthetic fits and valid integer daily
outputs. The runner's separate boundary fixture used invented integer forest
targets on both sides. It therefore tested substitution but not the real
pipeline-to-runner representation difference. Full software qualification was
20594pass/2knownfail/1skip, focused888pass; those counts do not prove integration
coverage that was absent. Retain this gap instead of describing the model as bad.

## Preserved Evidence

- Failure SHA256:753844c6d856a2445c7ab86e9e21a147b4e6478d5d891fcf38ef4495d075c0e6.
- Actual market terminal SHA256:e494694283ce7eb2cc349b787884d476f2278c8017c07cc88797fa4528a0dc20.
- Read-only failure audit: reports/nq_apex_tick_pressure_v120_execution/terminal-failure-audit-v1.json.
- Audit SHA256:0ad840111fc5f3b003aa391059b1c08da1ee7afeefd14976d4256338231e8d1b.

The audit rechecked qualification, process receipts, the unchanged source/runtime
bindings,3848 dependencies, the exact27-file failed-output census, six model
receipts and eighteen ordered stages. It made no fits, predictions or raw market
replay. Original failed outputs and qualified V120 source bytes remain immutable.
V119 remains the latest completed economic comparison and failed.

## Follow-Up Boundary

Do not rerun V120, refund its reservation, refit or tune against this failure.
A separately reviewed integrity-only successor may retain these exact forests,
reconstruct deterministic forecasts from the same bound causal inputs and perform
the first account replay. It must compare strict integer cent values without
tolerances or rounding, retain all model/arm/fold/source bindings, and explicitly
test actual synthetic pipeline output against the execution boundary. This work
is not itself a replay authorization, a new result or a weaker economic gate.
