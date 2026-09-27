# V111 Event Ordering: Completed Development Failure

The single frozen experiment completed on 2026-09-13 at 13:59:17Z with actual
process exit 0. It executed six estimator fits, three shared sequence and three
shared target transforms, then 181 complete NQ/MNQ raw-pair scans and twelve
continuous account books. No retry, refit, retuning or operational replacement.
Exactly four comparisons remain charged, bringing the historical ledger to
13,185. Successful execution is not a successful strategy.

## Result

The original V102 NQ Evaluation path stayed unchanged. Only MNQ PA forecasts
differed: the original reference, a chronological GRU, and its matched
whole-row order-erased GRU. Every candidate PA book had zero nominations,
attempts, trades, commissions, slippage and trading PnL. All eight candidate
books closed under the unchanged modeled inactivity rule.

| Mode | Reference PA Net | Ordered PA Net | Order-Erased PA Net |
| --- | ---: | ---: | ---: |
| Baseline | -$1,271.14 | $0.00 | $0.00 |
| Cost Only | -$1,588.50 | $0.00 | $0.00 |
| Latency Only | +$1,470.00 | $0.00 | $0.00 |
| Combined Stress | +$742.50 | $0.00 | $0.00 |

Ordered-minus-erased is zero, not a positive improvement. Ordered-minus-original
is +$1,271.14 in baseline but -$742.50 in combined stress, with earlier
inactivity in both modes. Both primary contrasts fail. Avoiding baseline losses
by never trading cannot rescue the failed ordering hypothesis or PA survival.
Every arm also fails absolute-positive PA in both primary modes and the full
route/payout gate. There are no hard-floor breaches or PA MAE violations.

All twelve Evaluation books numerically pass, reproducing the same four NQ
prefixes. Their trading net is $3,254.00 / $3,292.00 / $3,130.20 / $3,429.00
for baseline/cost/latency/stress. These are reused Evaluation results, not new
GRU successes. Evaluation profit correctly does not carry into a fresh PA.

## Why There Were No PA Trades

The independent account audit reconciled the following counts separately for
each candidate. This is not missing market data or a downstream fill failure.

| Mode | Represented PA Dates | Source Events | Model Abstentions | Stop-Cap Exclusions |
| --- | ---: | ---: | ---: | ---: |
| Baseline | 21 | 664 | 561 | 103 |
| Cost Only | 20 | 609 | 510 | 99 |
| Latency Only | 21 | 675 | 578 | 97 |
| Combined Stress | 21 | 664 | 561 | 103 |

Exclusions exhaust source events; no other reason or downstream failure was
recorded. The stop>140 mask precedes model selection. A stop-excluded event's
counterfactual model decision cannot be inferred from these reason counts.

Across the full scored calendar, before PA phase/stop/capacity/cooldown gates,
the ordered model has 19 all-four-positive forecasts (folds 2/16/1), versus 24
for the order-erased model (7/17/0), out of 3,747 events per arm. A positive
forecast anywhere in development is not an actionable opportunity in the
account's actual PA calendar. This post-terminal algebra changes no threshold
and creates no new model, replay or comparison. It does not establish whether
training capacity, optimization or target calibration caused the abstention.

The failure does not prove neural models or chronological information are
universally useless. It rejects this fixed implementation and decision policy.
Do not lower the all-four-positive threshold, switch cohorts, choose a favorable
mode or invert a model to rescue this completed attempt. Any distinct future
plan must address the failed actionable PA support and carry its own charge.

## Verification And Limits

The source/model auditor completed at 14:06:16Z, actual exit 0. It reverified
3,178 dependencies, all 27 stage receipts and all 31 immutable output files.
Restoring the saved weights reproduced all 252 forecast envelopes / 7,494
event vectors exactly with zero new fits, scaler fits or account replays.
The separate read-only accounting agent found no discrepancy, reproducing
four V107 controls and eight candidate Evaluation prefixes and recomputing
both primary gates. Its report does not independently replay raw intratick
fills or establish independent statistical validation.

There are 126 scored development dates, 2025-12-03 through 2026-06-12:
1,408 represented book-days plus 104 terminal-padding days = 1,512 scheduled
book-days. These overlapping accounts are not independent samples. The 48
sealed holdout dates remain closed. Modeled commissions and slippage are
included; program fees remain unpriced. The user's personal Legacy purchase
cohort and official compliance are unverified; no actual payout occurred.

Preclaim focused tests: 435 passed. Full regression: 16,122 passed, two exact
unchanged baseline failures and one skip, actual exit 1. All 287 new runner
cases passed. The full suite is not green; preserved failure receipts must not
be replaced with synthetic evidence. No frozen production/model code changed
during the experiment or terminal audits.

## Immutable Evidence

- Lock: c4a9bf0b430879c949c3581d5767a10abf340139f22aa47010be9671df098e82
- Claim: 35194b7a921434abd1be607af9a10e638fd27e1e7d3924733fc9fcb66e090118
- Status: ed4a7538a743132b1279db0fa9e4cb7e2f1a2de9ec4bd7686d9045db466b6d59
- Seal: 98f2be289af203e32c322cc30f4b3c071c0b69e2eaabc8c705b3f77a2bb8cdcc

Original output: reports/nq_apex_event_order_v111. Terminal receipts and audits:
reports/nq_apex_event_order_v111_execution. Both full user goals stay active.
This result does not authorize Windows feed activation, orders or Telegram.
