# V140 Unit-Target Component Qualification

October7,2026. The [design](research-v140-design.md) is unchanged and publicly
recorded before market extraction. Status: COMPONENTS_QUALIFIED_NOT_MARKET_FITTED.
This is not a profitable model, a complete market runner or a trial reservation.

## Implemented

`nq_apex_giveback_unit_labels_v140.py` composes V136's private giveback dispatcher
with a fresh original signal-only account for each event/mode. It never changes
predecessor globals or source. Each full daily census produces four exact
one-contract cent targets per event without capacity/profit filtering. Original
geometry skips remain zero; missing/malformed complete windows abort. The
normal/delayed windows must share the exact provider-ordered suffix. Conservative
maturity uses the complete windows, not an earlier profitable exit.

New closed receipts separately bind the old journal hash, original event/census,
source identity, session/window bytes and giveback execution evidence. No source
admission or model authority is granted by a content hash. The adapter has no
market reader, fit, account lifecycle, order or network path.

`nq_apex_giveback_unit_population_v140.py` binds these new targets to exact old
V129 Prepared support rows through V139's original population checks. It first
validates all prefix records, including unsupported events, and rejects mature
timestamps at or beyond the fold cutoff. Old y is reconciled against original
journals and remains untouched. The new Targets object has a separate binding,
unchanged IDs/dates/weight hash, and irreversible byte-backed read-only y.

Independent review reproduced one integrity issue before qualification: merely
setting NumPy's writable flag false allowed a consumer to turn it back on.
The adapter now uses the established immutable-byte helper, and tests require
re-enabling writes to raise. This correction does not alter the frozen design.

## Verification

Final affected regression exec78368 exited0:637 unique tests, zero failures,
errors or skips,70.265seconds in JUnit. It includes149 new label cases and37
new population cases, plus451 predecessor label, giveback/account, tick-audit,
population, feature/source and maturity tests. No market data or fits were used.
The new tests cover both products/sides/four modes, first crossings, arming,
half-peak equality, target/stop priority, losses after gaps, equal timestamps,
suffix changes, immutable source snapshots, complete maturity, quantity scaling
and guarded counterexamples. Prefix tests retain original support and labels,
reject unsupported-row corruption, and distinguish manifest key order from
the ordered original event census.

Earlier binder smoke attempts found invented-fixture defects: nonpositive test
prices and an assumed empty first-fold date. They were corrected in the fixture,
not production admission. The revised binder smoke passed37 before the final
637-case regression. They are not model-selection trials or market failures.

All16 V139 own source pins and261 loaded preflight dependency pins rehash
unchanged. The prior full-repository failures remain disclosed; this scoped
component regression does not claim the entire repository suite is green.

JUnit: `reports/nq_apex_v140_component_qualification_20261007/affected-v1.xml`,
SHA256 `b339cbb220014482bb9418a06f7b12bf44c7aa8420afda2fe8ba8a232d58c42b`.
Qualification: `reports/nq_apex_v140_component_qualification_20261007/qualification.json`.

## Remaining Work

This is the earlier component checkpoint, superseded in implementation scope
by [training](research-v140-training.md) and
[execution integration](research-v140-execution.md). Those add the source/cache,
six-model learner, matched diagnostics, four-book replay, supervisor and saved
audit. Their complete qualification is required before reservation; this
component pin cannot substitute for it. Effective trials remain13,272 and all48
sealed dates remainclosed. No Windows/model deployment, order, schedule or
spending change was made here.
