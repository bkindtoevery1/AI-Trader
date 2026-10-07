# V141 Results And Retrospective

October 7, 2026. **Completed and audited; FAILED the economic gate.** The fixed
[design](research-v141-design.md) and [execution](research-v141-execution.md)
are unchanged. This is reused-development evidence, not independent validation,
an official 50K account pass or a deployment recommendation.

## Complete Execution

One supervised attempt started at 12:05:29 UTC. Child PID 72646 exited zero at
12:26:34 UTC; its parent and complete no-fit audit subsequently exited zero in
tool session 79027, observed by 12:38:37 UTC. Neither process remains present.
No retry, refit, threshold change or partial-result selection followed.

Six fixed Ridge pipelines contain six joint four-response estimators and twelve
training-only scalers. All 252 candidate product/date forecasts were published
before scoring. All 181 raw contract pairs and 126 scored dates completed. Four new
account books were compared with four exact saved V140r1 books, without refitting
or replaying controls. The original 181-file label cache was reused read-only;
no labels were regenerated. Actual model fitting produced no recorded warnings.

The supervisor authenticated 59 payloads and all three result sections, restored
six saved models, regenerated their predictions, and recomputed diagnostics and
account summaries. The later completion record rehashed all 59 payloads and 281
bound source files. It records the observed supervisor exit rather than claiming
a second independent raw-tick replay or renewed root-data admission.

## Account Results

All results below are modeled trading PnL after the frozen execution costs,
before unpriced program fees. None reached PA or passed Evaluation.

| Mode | Trades | Active Dates / 126 | Evaluation Trading PnL | PA |
| --- | ---: | ---: | ---: | --- |
| Baseline | 31 | 21 | -$1,646.10 | Not reached |
| Cost only | 22 | 15 | -$1,939.00 | Not reached |
| Latency only | 27 | 20 | -$373.70 | Not reached |
| Combined stress | 23 | 19 | -$826.00 | Not reached |

Each remains `EVALUATION_RIGHT_CENSORED`: the observed calendar ended before a
pass, not an asserted future failure date. There were no hard trailing-threshold
breaches. Avoiding a breach is not economic success. All four paths incurred six
modeled Evaluation renewal units; fees remain unpriced. There is no PA profit,
survival or payout evidence. All PA profit contrasts are null, not zero.

Both primary full-route gates, relative PA benefit and categorical full-route
improvement are false. Scenario books are not independent samples and do not
trade identical realized paths, so a less-negative stressed result does not
establish that worse execution improves the strategy.

## Forecast Findings

The date-equal MSE is lower than the saved HGB comparator in every mode, but
higher than the training-only mean in every mode for both products. The table
shows candidate MSE relative to each comparator; negative is lower error.

| Product / Comparator | Baseline | Cost | Latency | Stress |
| --- | ---: | ---: | ---: | ---: |
| NQ / saved HGB | -4.224% | -4.614% | -3.601% | -3.196% |
| NQ / training mean | +0.494% | +0.402% | +0.107% | +0.115% |
| MNQ / saved HGB | -3.464% | -3.546% | -2.315% | -2.406% |
| MNQ / training mean | +0.681% | +0.608% | +0.176% | +0.054% |

Positive-all-four-head opportunities fell from 418 to 75 for NQ, and from 255
to 43 for MNQ, on the same supported-event sets (3,708 and 3,236 respectively).
This was a more selective forecast, not a zero-trade technical loop. Its selected
NQ unit-label averages were negative in all modes: -$6.09, -$39.15, -$47.78 and
-$72.60. These potentially overlapping, guard-free opportunity labels are
diagnostics, not executable portfolio PnL or independent observations.

## Lessons

Reducing model complexity improved forecast error against the prior complex
model without establishing an edge over the mean or profitable selected trades.
Sparse nominations alone do not explain away the losses in actual accepted
trades. The experiment does not isolate whether the fixed penalty, feature
information, regime variation or nomination rule is the dominant cause; it
does not prove that all Ridge models fail. More contracts, inversion or a new
threshold are not validated remedies and were not applied after seeing results.

PA instrument routing cannot explain this candidate's losses: it never left NQ
Evaluation. Further research should distinguish weak conditional payoff
information from the selection rule before attributing failure to PA sizing.
No new trial or revised parameter search is authorized by this retrospective.
The current operational priority remains the unchanged V63/V92 signal route.

## Evidence And Limits

- Result seal: `89af4c3e9f23105865395946443f67f7f01652c3c8babaa5e4cb2083a566eaef`.
- Child terminal: `686243d5ff9f08a3ba4e41c59afe42e18addf2b7453dfcde9c51c291d11884fa`.
- Completion record: `reports/nq_apex_v141_completion_20261007/completion.json`, SHA-256 `6848f3ffdf2a1ce2cdc861f9adee9406ea83657493f2331fb8c652656d8135a2`.
- Software qualification: 2,134 distinct affected cases, including 119 focused
  cases, all passed; not a whole-repository all-green claim.

All seven comparisons remain charged, total 13,284. The 48 sealed holdout dates
remain closed. Current official account-cohort compliance and program fees are
not established by these frozen modeled rules. There was no live-model change,
order, data purchase or schedule change. Referenced private detailed evidence,
model files and raw data are not part of the curated public documentation.
