# V115 Completion Erratum

The frozen [completion report](research-v115-completion.md), Failure Attribution
item4, states13.00USD round-trip commission for five MNQ contracts. The exact
amount under the recorded stress assumptions is **12.50USD**, not13.00USD.
This excludes the separate modeled slippage cost.

Independent recorded-account evidence contains32,000commission cents over128
completed contract round trips:250cents each, hence1,250cents for five. The
stress account correctly used320.00USD total commission and512.00USD slippage;
119.00-320.00-512.00=-713.00USD. No stored economic number, model, verdict or
comparison charge changes. This corrects prose only.

Preserve the original hash-bound report and publish this erratum additively:

- Completion report SHA69b469c900feac521c53a39a33826bd16bbdd2798dfbc02ff690221b75908a9e.
- Completion packet SHAe0df26c2c7f68189596d4fa4203147c4224e6a256d76078c74df13bf9e8352be.
- Independent account report SHAa6d622523c5baf1b3854e5ab1b59cc5d652b629916c35229fd66085f141ed805.

The central V115 state links this correction. No market rerun, refit, raw replay,
account recalculation, live order or new comparison was performed for it.

## Central-State Integration

Postpublication state checks initially found a missing terminal-status alias;
the subsequent run exposed a missing claim-path alias. Added the truthful
terminal status/exit, claim/lock and completion references, and the established
`Completed v115` prefix for the central finding. These amend only the mutable
index. The frozen completion writer remains preserved as actually executed;
its output needs these compatibility fields, so do not reuse it unchanged for
another cycle. Original report/result/model bytes remain intact.

Initial state-check handles81548and17963closedexit1. Final check31837closedexit1:
19passed,2exact pre-existing failures. The current completed-run/lineage contract
now passes. The remaining failures concern an older comparison-count assertion
and the missing V88temporary XML, not V115 economic performance. The original
core qualification's18,027passes/2failures/1skip remains a separate historical
test run; no new full-suite run is claimed after these metadata-only changes.

Postpublication verification also rehashed all46immutable outputs and32frozen
completion dependencies, checked both actual auditor exits and confirmed the
commission correction arithmetically. All passed, with zero new model fits or
raw replays. JSON formatting preserved unrelated central state values/order.
