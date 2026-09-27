# V119 Status And Development Record

Updated 2026-09-27 UTC. **COMPLETED / FAILED_SPARSE_PA_ACTIVITY_AND_STRESS**.
The sole execution and postrun verification exited0; economic gates failed.
See the complete [results and retrospective](research-v119-results.md).

## Why This Version Exists

[V118](research-v118-results.md) abstained on all candidate PA decisions. It
tested utility at the allocator's maximum quantity, which may reject a trade
that has positive cost-adjusted utility at a smaller whole-contract quantity.
V119 isolates that decision-rule question; it does not refit a predictor or
lower execution costs to obtain a pass.

## Change And Retained Controls

The [frozen design](research-v119-design.md) enumerates flat and every permitted
integer quantity, chooses maximum worst-mode certainty equivalent, and uses
the smaller quantity on an exact tie. It retains the three V118 forests,
original chronological splits, original NQ Evaluation, PA MNQ route, actual
entry guard, costs, latency, cooldown, trailing threshold and activity rules.
Maximum permitted quantity remains a ceiling, not the mandatory trade size.

Existing181 explicit-contract paired sessions support126 scored dates. These
are repeatedly used development dates, not an independent holdout. The48-date
sealed holdout stays closed. Windows and future collection are not prerequisites.

## Evidence And History

- Local implementation commit: `f8e7eaf`; a local hash is not proof of a push.
- Before the September23 pause: selector118 and account56 synthetic tests
  passed. The final runner/replay/adversarial check passed27 tests, exit0.
- That review found missing focused/full test-census closure and incomplete
  quantity-journal reconciliation. Both were corrected before any market claim.
- The user resumed research on September27. The independent recorded-ledger
  auditor and its86 synthetic tests are implemented. Related focused regression
  passed485 tests, zero failures/skips, observed exit0 in54.269seconds; source
  hashes remained unchanged.
- Audit/qualification integration local commit: `af4c843`. The audit checks
  recorded arithmetic only, not independent tape or full lifecycle reconstruction.
- Full regression ended with observed exit1 in2845.712seconds:19689 unique
  passed cases,2failed and1skipped;19692 actual cases have unique IDs. The suite
  header declares19781; see the [count erratum](research-v119-test-count-erratum.md).
  Source/runtime hashes stayed unchanged and the predecessor census
  plus every focused case remained present. This is not an all-green suite.
- The two failing case IDs match the inherited baseline. The account-transition
  case initially stopped earlier on this turn's `Legacy50K` status spelling.
  Corrected to `Legacy 50K`; a separate observed two-case follow-up now fails
  only at the inherited V102 four-candidates-versus-six assertion and missing
  V88 temporary XML receipt. Original full-run evidence is not overwritten.
- Qualification was published with known suite failures, SHA256
  `2219b504c33f834589cd243cf76e58c75497e288afebc6dec8f390ad41826ba6`.
  Full terminal SHA256:
  `d148f1d7d647c9cea2f90457191d1eb67aa2f2b30fe7ab1da84ed86771847b81`.
  Metadata follow-up terminal SHA256:
  `0e36ccc2c152a5e0ceaf1005d5f09ea1990c51c1ae4c8d1b36137f8ca8221be7`.
- Historical execution ran2026-09-27T05:15:43Z through06:32:42Z; exclusive claim
  at05:15:47Z. New fits:0. Charged comparisons:3, current total13209. Four new
  account books and eight retained controls are complete. No partial outcomes
  were opened; separate postrun verification ended06:36:21Z.
- Preoutcome lock SHA256:
  `0d3f2fce73e3ade254cb8e446f511c71e20f226fc34247d211ba74b85efe5126`.
- PA PnL is+135.96/+72.00/-65.54/-68.50USD in baseline/cost/latency/stress;
  PA trades1/2/1/1, all one MNQ. All four books closed for inactivity. No payout.
- No verified account pass, operational deployment or live order is claimed.

## Next Decision

Both observed processes are terminal. Preserve the complete results, receipts
and13209charges; do not replay the closed run. Investigate genuinely new causal
payoff information before defining a successor. Do not rescue a completed
attempt by changing quantity preferences, costs, modes or account gates.

Publication records must distinguish the reviewed public source/docs from local
licensed data, fitted artifacts and private evidence. Preserve prior status
commits rather than rewriting history when new results become available.
