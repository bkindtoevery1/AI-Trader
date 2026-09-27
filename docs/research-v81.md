# v81: Wick and Medium-Term Trend Information

Main research follows the latest user target, Legacy 50K Tradovate Evaluation
followed by a newly activated PA. EOD 50K remains a labelled comparison. The
old 25K goal banner and old model policy labels do not change the active target.

v80's three payoff learners produced insufficient activity and no validated
model. Their thresholds and outcomes remain frozen. v79's completed volume
ablation is auxiliary, not a prerequisite for the present study.

## Preregistered Comparison

1. **Unchanged v48 trend signal.** The zero-fit rule requires agreement between
   NQ and MNQ 20- and 60-session regular-session trend efficiencies. Only the
   signal and scheduled times are preserved while account/fill simulation changes
   to the locked 50K ordered-tick engine. Every cached
   feature is reproduced; no horizon, direction, weight or threshold is tuned.
2. **History-expanded v57 wick model.** Keep the original one-minute wick
   formula, NQ/MNQ directional consensus and single fitted orientation. Its old
   minute-only design unnecessarily restricted source history to 181 raw-tick
   dates. Expand prior minute training while keeping the new comparison's
   evaluation dates fixed. This is a new history-trained policy, not exact
   reproduction of v57's old fitted orientation or old two-fold results.
3. **New wick/trend interaction ridge.** Use the two wick scores, four trend
   efficiencies and four same-product wick/trend interactions. The ten-feature
   standardized ridge has fixed alpha 100, SVD solver, an intercept and a fixed
   6.5-point contrast dead zone. Its coefficients and scaler see training only.

The hypothesis is that opening candle rejection has different implications under
different preceding medium-term price trends. The experiment changes information
and history, not an exposed v80 threshold. Prefreeze independent review identified
that v48 originally uses 09:31-15:55 ET, not the v78 opening-only window. Preserve
v48's original baseline and 09:34-15:52 stress schedule; both other models and the
v63 control use 10:02-12:00 and 10:05-11:57. The same dates, engine and costs allow
policy comparison, but differing exposure horizons prevent attributing every
PnL difference solely to the features. No v81 outcome was loaded before this
correction. The fixed trend signal needs only prior RTH data at its earlier entry.

## Cohort and Execution

617 paired minute sessions end on 2026-06-12. Sixty strictly preceding regular
sessions are needed by the trend feature, leaving the **same 557-session cohort
for all three models**. Training prefixes contain 265, 338, 411 and 484 sessions,
then ten label-purged sessions and 63 validation sessions. Validation dates match
v77; prior fitted policies continue over the thirty between-fold dates to create
282 continuous signal dates. No surviving account resets at a fold boundary.

v48's within-contract regular-session returns never bridge contract prices.
v57's completed opening bars end at 09:31 through 10:00 ET. No current full-day
return, final volume, future scaler, or holdout information enters a predictor.

The learning target preserves the old minute stopped-action long-minus-short
contrast with a 46.75-point protective stop. Minute labels are approximations,
not proof of tick-level fills. Final account and full-calendar direct one-MNQ
diagnostics use all 181 fixed explicit raw pairs and the exact frozen v78 engine:
two MNQ in Evaluation, one MNQ in PA, at most two actual contracts, baseline and
mandatory stressed timing/commission/slippage. The v63 reference journals and
raw receipts must reproduce v78 exactly. No account type is selected from results.
One full integrity scan retains the earlier/later v48 window and derives all
four windows using original sequence order and the first Last at or after each
boundary; no sorting, interval truncation, or fabricated intrabar path is allowed.

## Accounting and Limits

Three model/account comparisons per family add six counted trials, bringing the
ledger from 12,969 to 12,975. There are four orientation fits and four ridge fits;
v48 is zero-fit. Reference conformance repeats add no trial. Freeze executable
dependencies, policy, environment and source metadata before loading new outcomes.
Publication is one-shot and create-if-absent. Never restart an observed or failed
run just because a tool wait expires.

Reuse v80's practical Legacy shortlist gates without weakening account, cost,
coverage or significance screens. A historical shortlist would still not prove
the full goal: reused dates are not independent validation, global DSR evidence
is unavailable, program fees and PA plan are not priced, and operational
compliance remains unverified. The 48-session holdout remains sealed, frozen
v63 runtime is unchanged, and no orders, messages, purchases or schedules run.

## Completed Result

The one-shot run finished at 2026-09-07T03:30:29Z. All 181 raw pairs and
402,041,614 events were verified, the v78 control accounts and receipts matched,
and all eight planned fits completed. The result is
`NO_WICK_TREND_50K_DEVELOPMENT_PASS`, not a data-availability failure.

| Policy | Direct one-MNQ baseline USD | Stress USD | Active sessions |
| --- | ---: | ---: | ---: |
| Unchanged v48 trend signal | 3,400.92 | 3,694.50 | 127 |
| History-expanded v57 wick | -2,535.14 | -3,883.50 | 166 |
| Wick/trend interaction ridge | -903.02 | -2,050.50 | 113 |
| Unchanged v63 control | -431.34 | -628.00 | 146 |

These 181-date signal diagnostics include simulated commissions, adverse fills
and model stops, but bypass account guards and exclude external program fees.
They are not the account balance, a payout, or net external earnings. Stress
also changes scheduled times; its higher v48 PnL does not mean costs help or
justify selecting the delayed window. The original v48 holding horizon differs
from the other models, as declared before freezing.

v48 was the strongest of these three development policies. Legacy baseline met
the numerical Evaluation target on 2025-12-18 and stress on 2025-12-31, each on
the **second attempt after a trailing-threshold failure**, not first-try passes.
The following PA paths both closed for inactivity and neither qualified for a
payout. A reports-only reconstruction identifies 2026-03-25 as the first failed
30-calendar-day activity check in both Legacy modes: the 2026-02-24 through
2026-03-25 window contained only one day earning at least USD 50, versus the
frozen two-day requirement. The balances were still USD 51,263.32 and
USD 51,900.50. Positive balance did not satisfy that separate activity condition.
The separately reported EOD paths also eventually passed Evaluation,
then closed for inactivity. Both learned wick policies failed to complete any
Evaluation. v48's family-adjusted bootstrap p-value was 0.1629 and its global
HAC Bonferroni p-value was 1.0; this is not independent statistical confirmation.

Keep all thresholds, horizons, account families and sizing frozen after this
result. The remaining research question is not whether data were evaluated:
they were. It is whether another preregistered model-risk policy can retain
predictive performance and satisfy the full Evaluation-to-PA route. More volume
maintenance or post-result loosening is not required to start substantive new
research. The sealed historical test remains closed.

## Independent Audit

A separate reports-only reviewer added 39 regression cases and found no
incorrect fills, integer ledger discrepancies or false-pass classification.
It reconciled 1,448 direct journal rows (1,104 executed trades) and 2,671 account
rows (2,008 executed trades), reproduced bootstrap/HAC calculations and
independently reconstructed the PA activity closure. Missing final evidence now
fails rather than silently skipping tests. The reviewer did not read raw prices,
feature caches or holdout payload. Separately, the parent reverified all 347
frozen dependency digests and the original 181-date source metadata. These
software checks do not convert the failed model into a strategy pass.

Final verification: 118 focused integration tests and 3,758 full regression
tests passed. No frozen implementation or market payload changed after the run.
The heartbeat prompt now points to the completed v81 evidence and the 12,975
trial ledger while preserving its existing schedule and blind v63 lineage.
