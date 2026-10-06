# V136 Execution Audit And Failure Attribution

Supplemental October 6, 2026 audit of the already completed failed study.
The [original design](research-v136-design.md) and
[results](research-v136-results.md) remain unchanged. This is not V137, a
second account replay, a threshold search or a new model-selection trial.

## Independent Execution Check

`tools/audit_nq_apex_giveback_ticks_v136.py` uses a separate NumPy vector
calculation, with no production strategy/account/forecast imports. It binds
the exact saved claim, result seal, accounts, status and archival source index.
Only the 126 scored development dates can be considered; all 48 sealed dates
remain closed. Each actually executed candidate trade is enumerated from both
the saved attempts and executions; missing/duplicate enumeration cannot pass.

The audit rehashes source manifests, conversion receipts and each accessed
Parquet file. It checks explicit contract/product/date/source identities,
contiguous provider sequences, nondecreasing timestamps, and the earliest
provider-order entry tick at the saved entry-due time. Equal timestamps do not
erase provider ordering. It then examines every tick from recorded entry
through recorded exit, not future extrema or alternative trades.

Independent masks establish the first triggering index and exit priority:
account floor, MAE, daily loss, initial stop, target, giveback, time. It checks
both commissions, adverse fills, integer quantity, net liquidation peaks,
first 1R arming, exact rational half-peak crossing, final cash and adverse loss.
No rounded guaranteed-floor fill or end-of-trade maximum can rescue a mismatch.

Completed at 12:57:28 UTC, actual process exit 0:

| Mode | Recorded Trades Checked |
| --- | ---: |
| Baseline | 187 |
| Cost only | 77 |
| Latency only | 38 |
| Combined stress | 19 |
| Total | 321 |

All 39 giveback exits matched. The 102 accessed Parquet files were hashed and
decoded; 4,120,068 execution-prefix tick visits were checked, including overlap
between modes. This is not a count of additional or independent market events.
All nine frozen V136 source/design/test hashes were subsequently unchanged.

Private result: `reports/nq_apex_giveback_v136_tick_audit_v1.json`, SHA256
`f51c324096ea88c1734471fab68c28dfbcf02fef6c01f76375f410fd683e541d`.
Audit implementation SHA256
`53e4a1ae01544e482a285ada7ee9add1389f3e2a42faef2fc4e1b48d38aa0378`.

Verification: 71 new focused cases plus 502 unchanged V136 account, source,
replay and runner cases passed in one combined run: 573 passed, no failures,
errors or skips, actual exit 0, 187.520 seconds. JUnit SHA256
`3631c09daece746046a9ebd29b803e42d8ca1d1bd92906160ec0bca708b13e87`.
An initial new-test collection failed because PYTHONPATH omitted tools; rerunning
with the repository's tools:src import path passed. No market retry followed.
This is focused/affected regression, not a full-repository green claim.

The check is conditional on saved nomination, sizing, starting account state
and bracket geometry. It does NOT independently reconstruct the whole account
lifecycle, prove signal causality/calibration, establish provider authenticity,
or supply independent strategy validation. Its success does not change V136's
failed full-route verdict or authorize deployment.

## Failure Attribution

A separate read-only agent examined the saved ledger; parent calculations
reconciled phase counts, costs, final 30-calendar-day windows and risk-cap tails.
No rejected opportunity's hypothetical profit was inferred.

| Mode / Phase | Fills | Active / Processed Dates | Final Headroom USD | Risk-Cap Rejections |
| --- | ---: | ---: | ---: | ---: |
| Baseline PA | 167 | 80 / 110 | 86.62 | 20 |
| Cost-only PA | 56 | 27 / 34 | 49.25 | 3 |
| Latency Evaluation | 38 | 20 / 126 | 292.85 | 238 |
| Stress Evaluation | 19 | 9 / 126 | 262.50 | 253 |

Baseline PA's final nine processed dates contain no fills; 17 risk-cap
rejections occur in that tail. Its last 30-calendar-day window loses 2,660.04
USD across 20 fills and has only one day reaching the modeled 50 USD activity
threshold. Cost-only PA still trades 33 times in its last such window and loses
2,137 USD; it also has only one qualifying day. Thus its activity closure is
not equivalent to simply having stopped trading.

Latency/stress Evaluation have 102/110 fill-free scored dates after their last
fills, with 223/236 risk-cap rejections in those tails. Smaller available budgets
cannot support the attempted stop reserves. Merely raising contract caps does
not solve zero feasible capacity. These are frozen research-rule calculations,
not verification of the user's current Apex cohort or current official rules.

Baseline PA stored commission plus slippage totals 1,778.88 USD, versus
1,625 USD cost-only. Adding them back gives 2,465.50 / 495.50 USD before those
recorded costs, not a zero-cost strategy counterfactual. The two paths have
different trades, quantities and phase calendars. Fees or latency alone cannot
be isolated by subtracting their final outcomes.

## Next Hypothesis, Not Yet An Experiment

Investigate a joint forecast of net trade PnL and trailing-floor increase to
estimate post-trade usable headroom, while keeping the V136 exit rule fixed.
V106 transformed terminal payoff; V118 explicitly did not learn account-state
transitions; V119 optimized quantity over those terminal-payoff distributions.
A bounded review found no exact prior joint-transition study, not exhaustive
novelty or evidence that this proposal will work.

The 321 selected executions are not an unbiased training set. A real successor
needs all eligible opportunities, causal state/label construction, explicit
account-guard semantics, fixed chronological folds and a frozen control before
any fit or replay. No successor is selected, fitted, reserved or deployed here.
Trial count remains 13,258, and model research plus Windows operation stay active.
