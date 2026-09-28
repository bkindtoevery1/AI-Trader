# Existing Models: 50K Account-Type Reassessment

## Scope

The user's September 28 request authorizes a bounded evaluation of already
trained models under Apex EOD and Intraday Evaluation rules. This supersedes
the research pause only for this comparison. It does not authorize new model
fits, hyperparameter selection, a holdout opening, account purchases, orders,
Windows changes or operational promotion.

Account size is 50K, provider Tradovate. Original model weights, predictions,
products, costs and contract quantities remain unchanged. Evaluation is the
primary question; PA survival and payouts are not silently added to the pass
definition and are not certified by this comparison.

## Rules Checked September 28

Both evaluations have a $3,000 profit target, $2,000 maximum drawdown and a
30-calendar-day access period, with no multi-day trading minimum. Contract
limits are six minis or sixty micros; this is not permission to enlarge the
models' frozen positions. Tradovate Evaluation trailing does not stop at the
PA floor cap.

EOD recalculates the floor from the highest end-of-day balance, with the floor
enforced intraday. Its $1,000 daily loss limit includes open PnL and liquidates
positions, then stops trading for the session; DLL alone does not fail the
account. Intraday follows realized and unrealized equity peaks continuously
and has no Evaluation DLL. Touching the applicable total floor fails either
account. Costs remain in modeled trading equity; program fees are unpriced.

Official sources:

- https://apextraderfunding.com/help-center/eod-trailing-drawdown-accounts/eod-evaluations/
- https://apextraderfunding.com/help-center/evaluation-accounts-ea/intraday-trailing-drawdown-evaluations/
- https://apextraderfunding.com/help-center/eod-trailing-drawdown-accounts/eod-drawdown-explained/
- https://apextraderfunding.com/help-center/intraday-trailing-drawdown-accounts/intraday-trailing-drawdown-explained/
- https://apextraderfunding.com/help-center/additional-helpful-items/daily-loss-limit-explained/
- https://apextraderfunding.com/?picker_balance=50k&picker_type=intraday-trail&picker_vendor=Tradovate

## Two Evidence Levels

1. Broad saved-execution screen: completed v78-v122 reports, plus their retained
   older model descendants, checked against their result seals. Repeated exact
   Evaluation schedules are deduplicated while every version/book alias is
   retained. Recorded quantities/fills remain fixed. First recorded starts and
   every fully observed rolling 30-calendar-day window are reported; overlapping
   windows are not independent attempts or estimates of real pass probability.
2. V63 ordered-tick replay: reuse the original saved signal schedule and
   admitted development raw ticks, without fitting. A separate Evaluation-only
   simulation applies the new rules to actual ordered marks and adverse fills.
   Its report must distinguish initial purchase, later hypothetical purchases,
   right censoring, DLL pauses and drawdown failures. No purchase is executed.

The broad screen cannot replace a model's adaptive account replay. New floors
can change sizing, route choices, skipped signals and subsequent trades.
An old DLL exit cannot reveal what the no-DLL strategy would have done later.
Consequently a recorded-schedule pass is not a verified model pass. Unknown
peak/adverse order and counterfactual DLL liquidations remain unresolved rather
than being counted as losses or passes. A fixed upper peak bound is never used
as proof of an Intraday breach. PA trades and account resets are never joined
to fabricate an Evaluation profit curve.

Older v2-v77 daily return vectors do not contain sufficient account-path
evidence for these rules. They are not marked failed merely for that reason.
Original v32/v48/v57/v63 descendants are covered by the later tick reports where
available. V95, original V107, V108 and V120 technical/preflight aborts are not
completed strategy failures; completed V96, V107 repair and V121 are distinct
preserved evidence.

All comparison outcomes reuse development dates ending June 12, 2026. The
June 29-September 2 holdout remains sealed. This study provides no independent
statistical validation and cannot justify hindsight selection, retuning or live
deployment. New rule-transfer comparison counts are reported separately from
the existing 13,215 historical model-search ledger; no estimator fit is added.

## Results

Completed the saved-path screen and separate V63 tick replay, not a full
counterfactual tick replay of every historical model. No old report/model changed.

The final screen authenticated 42 completed reports, retained 888 version/book
aliases and deduplicated them into 337 account-context-specific Evaluation
schedules. Those are not 337 independent fitted models. Each schedule was
screened under both families; 35,324 overlapping full-window schedules per family
were also inspected descriptively. No pass-probability inference is justified.

| Initial recorded schedule | EOD | Intraday |
| --- | ---: | ---: |
| Below target at 30-day expiry | 322 | 272 |
| Recorded-path drawdown breach | 13 | 55 |
| Unresolved intratrade order | 0 | 8 |
| Conditional recorded-schedule target pass | 2 | 2 |

These statuses describe unchanged saved executions, not each model's newly
resized account. Every numeric outcome assumes no trading on dates absent from
the supplied schedule. Missing weekdays are explicitly retained, including
possible holidays; they are not invented zero-return market observations.

### Bollinger Reentry

Both initially passing schedules were V85 `bb_reentry_base`, baseline only,
one NQ and six MNQ. A second check covered all 18 V85 Bollinger product policies
under both modes and account families: 72 first-attempt sizing proofs. It checks
all signaled days, including previously skipped trades, using the original
hash-bound risk reserve formula and the new account's available capacity.

- **Six MNQ baseline:** exact quantities remain unchanged and conservative
  intraday bounds establish numerical compliance under both EOD and Intraday.
  Recorded profit is **$3,500.40**, reached October 1, 2025, from a September 8
  start, before the October 7 deadline. This is 15 represented sessions.
  **The pass is conditional on no trading September 11, 15 and 22, which are
  absent from the supplied data.** It is not complete-calendar, independent,
  stress-robust or official-compliance evidence.
- **Six MNQ stress:** EOD reaches only **-$225.50** by expiry. Intraday sizing
  diverges September 12 (six original versus five new contracts), so its full
  counterfactual outcome remains uncomputed. Baseline success is not robust.
- **One NQ:** both account families require a new adaptive execution replay.
  EOD changes an originally skipped September 25 entry into one contract;
  Intraday disallows the original September 10 entry. The apparent $3,275.90
  saved-path pass must not be advertised as a transferred-model pass.

This is a rule-based Bollinger policy, not a newly trained AI model. Across the
72 proofs, two are conditional numerical passes, 31 expire below target and 39
require replay after sizing divergence. A missing replay is not a strategy loss.

### V63 Exact Tick Replay

Frozen signals and two MNQ, unchanged stop/cost/timing rules. All 181 paired
development dates and 402,041,614 source events were verified. One shared scan
fed four books, finishing in 171.748 seconds with exit zero.

| Evaluation book | Pass | Drawdown failure | Expired | Right-censored |
| --- | ---: | ---: | ---: | ---: |
| EOD baseline | 0 | 1 | 8 | 1 |
| EOD stress | 0 | 0 | 9 | 1 |
| Intraday baseline | 0 | 2 | 7 | 1 |
| Intraday stress | 0 | 0 | 9 | 1 |

The first September 8-October 7 attempts produce **+$1,260.56 baseline** and
**+$533.00 stress**, below the $3,000 target in both families. Later disjoint
attempts likewise have no pass. The incomplete tenth attempt is not a failure.
These replay outcomes also assume no trading on unrepresented dates. See
[V63 details](v63-account-types-20260928.md).

### Other Recent Models

The first saved V92 Evaluation window has no trades and $0 PnL. V97/V102 NQ
and the inherited V122 Evaluation prefix show $1,043.80 baseline and $1,253.00
stress through the first 30-calendar-day window, also below target. Their later
Legacy numerical passes cannot simply transfer because those balances were
accumulated over longer periods. These are saved-path screens; alternative
account sizing may change the path and has not been replayed for all policies.

## Verification And Artifacts

The final related suite passed **360 tests**, exit zero, including the new
screen, source publication, V63 replay, coverage annotation and existing V78,
V85 and V87 account tests. No whole-repository suite was run for this isolated
diagnostic. V63 seals, source pins, 181 dates, four books and attempt arithmetic
were independently rechecked without replaying market data.

Adversarial synthetic review found product-identity deduplication, nested
calendar, empty-execution reconciliation and truncated-lifecycle peak defects.
All were repaired and regression tested. The earlier screen drafts are retained
as superseded diagnostics, not extra economic model trials. The final count is
337 schedules, not the preliminary 333 that omitted effective product identity.

Authoritative derived artifacts:

- `reports/nq_apex_account_type_screen_v1/final_status.json`
  SHA256 `68f67ea72067515baa096ad4c50c674233f2ff90f0ffa35f9a084a9b3ed10c0b`.
- `reports/nq_apex_account_type_screen_v1/final_v85_sizing_proof.json`
  SHA256 `b67e9fe60cf3612276043b2ce8f19fa9f65faecbec89512ae952711ca3c3a20b`.
- `reports/nq_apex_v63_account_types_v1/coverage_status.json`
  SHA256 `a3886656208e392f5cef601b5c665d943107f1db2f9764ea2b084147c3c3147f`.
- Original V63 replay `status.json` SHA256
  `f45da9c7d4592519839b1d36ba3172c96e2d199a5e7ede940947cf7397a3abdb`.

Remaining work is exact new-rule replay for account-adaptive policies, especially
V85 NQ, and reconstruction of older daily-return-only models before any claim
that the entire historical catalog was evaluated tick-by-tick. Missing market
dates and independent validation remain separate limitations. No robust,
complete-calendar, verified live model pass is established here.
