# V119 Status And Development Record

Updated 2026-09-27 UTC. **NOT_EVALUATED**: no V119 historical execution, model
fit or economic verdict exists at this checkpoint.

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
  passed cases,2failed and1skipped;19781JUnit execution records include repeated
  case IDs. Source/runtime hashes stayed unchanged and the predecessor census
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
- Historical execution: **NOT_RUN**. New fits:0. New comparison charges:0.
  Planned charge:3, only on a genuine exclusive claim. Current total:13206.
- PA PnL, trades, survival and payout: **NOT_MEASURED for V119**.
- No verified account pass, operational deployment or live order is claimed.

## Next Decision

Qualification and metadata follow-up are terminal. Recheck the pinned evidence,
freeze exact dependencies, and execute the one fixed policy over the complete
existing calendar. Record failure as well as success. Do not rescue a completed
attempt by changing quantity preferences, costs, modes or account gates.

Publication records must distinguish the reviewed public source/docs from local
licensed data, fitted artifacts and private evidence. Preserve prior status
commits rather than rewriting history when new results become available.
