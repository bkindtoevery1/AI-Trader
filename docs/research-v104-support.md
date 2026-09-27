# v104 Predictor Support Audit

This is a completed saved-input diagnostic, not a model backtest, account
simulation, prospective result or deployment authorization. The executable
morning-trend/HGB ensemble remains unfinished. The latest completed performance
experiment remains v103; neither NQ nor MNQ has a verified full-route pass.

## Observed Support

The authenticated common cohort contains 126 development dates from
2025-12-03 through 2026-06-12. All 557 original trend-feature rows, the saved
282-date zero-fit trend schedule and 252 original HGB forecast envelopes were
checked. All 3,747 events per product were validated, including unselected
events. Candidate forecast copies were not used.

| Product | Trend-only dates | HGB-only dates | Both | Neither |
| --- | ---: | ---: | ---: | ---: |
| NQ | 66 | 2 | 32 | 26 |
| MNQ | 78 | 0 | 20 | 28 |

Assigning the entire day to nonflat trend at 09:30 would suppress 108 of 110
selected NQ HGB events and all 45 selected MNQ HGB events. The apparent increase
in nominated dates does not prove more executable trades, additive returns or
diversification. This whole-day owner rule is rejected as the proposed additive
ensemble; it remains a recorded diagnostic counterexample.

In one fixed fresh-PA reference state, the original 187-tick NQ stop requires
a 98,200-cent unit reserve while usable MAE is 74,999 cents: zero NQ contracts
are affordable under this research allocator. MNQ permits five in that reference
state, not six because the initial PA plan ceiling also applies. Neither value
is a current account recommendation or a loss guarantee. Original trend has no
nominal target, so its stop/target ratio is unavailable, not verified compliant.

## Evidence And Repair

Report: `reports/nq_apex_ensemble_support_v104/support.json`.
SHA-256: `052fa272ef3d63ce63eea9e2a164a5d24271f3d4caf67db02bde87b856aec47e`.
Successful audit exec 60375 exited 0. Parent readback verified all 15 recorded
source/implementation hashes with zero mismatches. Publication is exclusive
and atomic; there was no existing report to replace.

The first audit, exec 52752, exited 1 before publication: the new auditor
incorrectly assumed that old dependency maps flattened the original builder
and base-cache pins. The builder is bound through the authenticated v48 lock;
the base-cache hash is bound through the authenticated trend cache. The repair
follows those existing bindings and checks the actual four source files and
their readback. No frozen source, market result or admission criterion changed.
The synthetic fixture now reproduces that nested structure instead of hiding
the defect with invented flattened entries.

Parent focused verification passed 147 synthetic software cases (exec 73416,
exit 0, `reports/nq_apex_ensemble_support_v104/focused.xml`). Independent read-only
review found no actionable defect in the corrected binding path or the morning
proposal. Direct mutation tests for authenticated contradictory nested pins
and reversed v48/v81 chronology remain nonblocking test gaps; the current
checks reject those conditions. Repaired full regression exec 77438 terminated
exit 1: 11,675 individual cases passed and one frozen legacy metadata case
failed because it equates four v102 candidates with six charged comparisons.
All 147 new v104 cases passed. No test was skipped or altered to hide the
failure; the unrestricted suite is not green. Six implementation/test hashes
were unchanged during the run. See `verification.json` and `full.xml` in the
same report directory.

The JUnit aggregate tests attribute is 11,765 but there are 11,676 unique
testcase elements. The earlier v103 full XML has the same 89-count discrepancy.
The cause is not established here; counts above use individual elements and
do not invent 89 additional unique passes. Original XML bytes are preserved.

The initial full run, exec 85416, was intentionally interrupted after discovering
the source-binding defect. It terminated with KeyboardInterrupt and a pytest
fixture-teardown KeyError, exit 1, and is not a completed regression. No passing
suite is claimed from that attempt. A separate full run uses repaired bytes.

## Scope

This audit checks authenticated saved predictors and selected dependency bytes.
It does not restore native model predictions, revalidate the entire transitive
runtime, recompute raw-market provenance, calculate PnL, run accounts, fit models
or open the 48 sealed dates. Those broader claims remain outside its evidence.
New fits, account replays and charged performance comparisons are all zero;
the ledger stays at 13,156. Existing v103 results remain unchanged.

The next implementation is the explicitly new morning ATR/2R policy described
in `docs/research-v104-design.md`, not unchanged v48. Its shorter horizon and
new bracket need their own complete development replay and shared-account
controls before any performance claim. Old trend profits cannot be transferred
to it by assumption.
