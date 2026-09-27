# V105: PA-support learning did not improve the account route

## Decision

The frozen study completed on 2026-09-12 at 17:30:58 UTC. This was an
executed learning and raw-backtest experiment, not a technical abort.
Do not promote V105, replace the fixed V102 operational lineage, rerun this
claim, or retune its support cutoff after observing these results.

The design is `docs/research-v105-design.md`. Terminal evidence is
`reports/nq_apex_pa_support_v105_implementation/execution_verification.json`;
the earlier `verification.json` remains a pre-performance implementation record.

## Actual Work

- 12 estimator fits, 3 scaler fits, and 42 ordered fit-stage receipts.
- 181 explicit same-maturity NQ/MNQ raw pairs scanned; 126 scored dates.
- Three arms in four execution modes: 12 own-account paths, 1,512 scheduled day slots.
- Four original V102 control accounts and eight new-arm Evaluation prefixes reproduced exactly.
- 2,967 frozen dependency hashes checked after execution; status and seal verified.
- Two new policies and two contrasts charged: ledger 13,168 to 13,172.
- No sealed holdout access, independent success, orders, or operational model replacement.

## PA Results

Amounts are PA-only trading PnL in USD, after modeled trading costs, excluding
Evaluation and unpriced program fees. A is original V102; B adds PA support
and actual-entry nominal reward/risk gates; C additionally learns on PA support.

| Mode | A | B | C | C minus B |
| --- | ---: | ---: | ---: | ---: |
| Baseline | -174.10 | -256.00 | -1,457.40 | -1,201.40 |
| Cost only | -814.00 | -862.00 | -784.00 | +78.00 |
| Latency only | -564.30 | -564.30 | -1,112.40 | -548.10 |
| Combined stress | -1,179.00 | -1,179.00 | -1,179.00 | 0.00 |

All twelve paths passed their inherited numeric Evaluation, then closed for
PA inactivity; none became payout eligible. All had zero hard breaches and
zero PA MAE violations. Those zero counts do not establish PA survival.
C closed eight calendar days earlier than B in baseline and one day earlier
in cost-only. The favorable cost-only difference does not satisfy the
preregistered baseline/combined-stress learning-benefit test.

## Failure Attribution

This is not explained by fewer model nominations. On the same 21 processed
PA dates, baseline nominations increased from 68 for B to 80 for C; latency-only
increased from 52 to 68. Yet C's baseline PA trades fell from 10 to 4 over
their own complete account histories, with fewer qualifying PA activity dates.
The account trajectory and executable risk capacity matter in addition to
the number of predictions. These comparisons are diagnostic, not a new
causal experiment; differing terminal horizons must not be pooled silently.

Support-only retraining did not solve the previously identified
selection/capacity/activity problem. A later proposal must address a distinct
mechanism and preserve an untouched control, not search another cutoff on
the same outcomes. Do not force extra trades to satisfy inactivity or blame
data quantity without evidence. No successor was fitted or reserved here.

## Verification And Remaining Work

Implementation commit: `0ee5ddf`. Focused: 901 passed, including 85 V105 cases.
Full run 8100: 14,353 distinct passed, 2 known failures, 23 skipped; all focused
cases passed in full. The suite's larger aggregate includes 89 subtest
increments, not additional distinct cases. Full regression is not green.
The residuals are the historical four-policy/six-comparison assertion and
a missing historical temporary JUnit artifact. Neither was hidden or altered.
These tests preceded terminal report and central-state bookkeeping.

The separate Windows diagnosis at 2026-09-12 16:48:13 UTC confirmed V63 and
predecision processes but zero packages/signals, V92 absent, and full-session
bridge stopped with last result 1. The latest connection log said Connected
at 14:21:24 UTC; it is not a fresh API snapshot. Login is not the remaining
blocker. Exact bridge exception is unknown. The new raw opt-in host is
offline-tested, not installed or model-admitted. No deployment, restart,
schedule, market request, order, or Telegram message was performed here.

Both user goals remain active and incomplete.
