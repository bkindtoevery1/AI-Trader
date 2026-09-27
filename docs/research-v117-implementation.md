# V117 Component Qualification

Completed 2026-09-22 UTC on the existing Mac data. Windows and new market
collection were not used. Latest completed economic evidence remains V116;
V117 has not produced a performance result or started an economic replay.

## Implemented

One policy candidate uses the unchanged original V102 baseline-head forecast
for PA nomination. Evaluation keeps the original all-four-head condition.
Both products' original four-head records are validated without substitution;
actual prices, fees, slippage, latency, sizing, stops, cooldown, activity and
payout remain the original account engine's responsibility. Long and short
are both supported. See `docs/research-v117-design.md` for the fixed contrast.

The adapter rejects recursive dispatch and restores caller state after callback
mutation or interruption. Independent tests discovered those two transaction
defects before any market claim; the first failing test logs remain preserved.
No frozen ancestor, original forecast or old result was rewritten.

## Verification

- Focused qualification: 477 passed, exit 0; 116 new cases and 361 ancestor cases.
- Source restoration: exit 0, 3,067 dependencies checked, six original model
  records and 252 forecast envelopes restored. The existing 181 raw-calendar
  dates support 126 scored dates and 3,747 events per product. This restoration
  does not evaluate V117 nominations or rescan raw pairs.
- Full regression: 18,609 passed, 2 preexisting failures, 1 skipped; actual exit 1.
  All 116 added cases pass; no new failure. The suite is not green.
- The old failures are the historical candidate-count assertion (4 versus 6)
  and missing `<TMP>/ai-trader-replay-wait-regression.xml` for V88.
- The strict frozen ZIP-fixture equivalence check accounts for two timestamp-only
  pytest ID changes. Raw XML and assertions are unchanged, and exact identity
  equivalence receipts are preserved.

Machine-readable evidence:
`reports/nq_apex_baseline_nomination_v117_implementation/component-evidence.json`
SHA256 `0b9575db9699e5e4bd203c3bf7901bf6e6f4ddf466db6c693640587b9d329884`.
It binds actual child PIDs/exits, unchanged source hashes, raw logs, JUnit,
source restoration, review and preserved unsuccessful qualification attempts.
After central-state publication, the focused state checks had 19 passes and the
same two preexisting failures (exit 1). All component artifacts and all 24 V116
immutable outputs remained unchanged; see the separate
`postpublication-state-verification.json` in the implementation directory.

## Outcome And Next Work

This is a policy ablation, not a new learner or better calibration claim.
Current new market fits, replays, candidate nominations and comparison charges
are all zero; total effective trials remain 13,199. More nominations are not
assumed to mean profitable or eligible PA trading.

Next implement and qualify the source-authenticated economic runner. It must
restore the original forecast vintages, freeze the design, reserve exactly two
comparisons once and run eight continuous books over the same existing data.
Require four exact V107 control reports, unchanged Evaluation prefixes and raw
own-product journal reconciliation. Do not refit, tune a threshold, choose a
favorable execution mode, open the 48 sealed dates, publish partial outcomes
or deploy this candidate to Windows. Account benefit and full-route success
remain separate. No credentials, orders, Telegram, spending or schedule changes
were made. The continuing research/Windows goals remain active and incomplete.
