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
  hashes remained unchanged. Full regression is running, not yet a pass.
- Audit/qualification integration local commit: `af4c843`. The audit checks
  recorded arithmetic only, not independent tape or full lifecycle reconstruction.
- Historical execution: **NOT_RUN**. New fits:0. New comparison charges:0.
  Planned charge:3, only on a genuine exclusive claim. Current total:13206.
- PA PnL, trades, survival and payout: **NOT_MEASURED for V119**.
- No verified account pass, operational deployment or live order is claimed.

## Next Decision

Finish full regression and source-pinned qualification,
freeze exact dependencies, and execute the one fixed policy over the complete
existing calendar. Record failure as well as success. Do not rescue a completed
attempt by changing quantity preferences, costs, modes or account gates.

Publication records must distinguish the reviewed public source/docs from local
licensed data, fitted artifacts and private evidence. Preserve prior status
commits rather than rewriting history when new results become available.
