# V144 Results: Public CPI Ablation

Completed October 12, 2026 on existing Mac data. No Windows connection,
collector change, Telegram message, account order, purchase or schedule change.

## What Was Tested

One frozen feature-set ablation: V134's 15 price, minute-volume and prior-event
features versus those same 15 plus last-known CPI-U headline 12-month NSA
inflation and release age. Public BLS archived release text supplies actual
8:30 ET release dates; simulated availability starts 60 seconds later.
Ten releases were retrieved for July 2025-May 2026 reference months, with
October 2025 absent due to the shutdown. No revised-series backward filling.
Unemployment is deferred because two original primary-source releases were
not recovered. This is a retrieval limitation, not evidence against unemployment.

The original 181-session / 5,485-event development cohort was reused with its
three expanding folds and ten-session purge. Scoring covers 126 scheduled
sessions: NQ has 3,708 supported events on 126 days; MNQ has 3,236 on 124 days.
The two empty MNQ dates remain in the scheduled calendar; they are not losses
or new data exclusions. Date-equal error summaries average nonempty dates as
in the unchanged control. Original support, labels, product units and costs
are unchanged. The sealed June 29-September 2, 2026 holdout remains closed.

Six new product/fold pipelines completed: 24 HGB response estimators and 12
training-only scalers. Six original V134 models/forecasts were authenticated
and reproduced, not refitted. Complete forecasts were durably published before
scoring. Four pre-reserved comparisons remain charged: 13,294 -> 13,298.
The interrupted V143 reservation remains intact; no V143 work was restarted.

## Forecast Errors

Percent change relative to retained V134. Negative is better. These are errors
of predicted one-contract net payoff, NOT account returns or increased profit.

| Product / Fold | Baseline MSE | Cost-Only MSE | Latency-Only MSE | Stress MSE |
| --- | ---: | ---: | ---: | ---: |
| NQ overall | -1.2480% | -1.1567% | -0.6764% | -0.4811% |
| NQ fold 1 | -0.1396% | -0.7145% | -1.1144% | -0.8299% |
| NQ fold 2 | -2.5016% | -2.1362% | -0.0170% | +0.3035% |
| NQ fold 3 | -0.6694% | -0.4080% | -1.0737% | -1.0825% |
| MNQ overall | -0.6158% | +0.0223% | -0.2099% | +0.2699% |
| MNQ fold 1 | +1.0953% | -0.2885% | +0.0309% | +0.4209% |
| MNQ fold 2 | -1.8460% | -0.2202% | +0.2675% | +0.9905% |
| MNQ fold 3 | -0.5732% | +0.6233% | -1.0738% | -0.8298% |

| Product / Fold | Baseline MAE | Cost-Only MAE | Latency-Only MAE | Stress MAE |
| --- | ---: | ---: | ---: | ---: |
| NQ overall | -0.4662% | -0.3212% | -0.2687% | -0.1217% |
| NQ fold 1 | -0.2116% | -0.1297% | -0.0734% | -0.3102% |
| NQ fold 2 | -1.2270% | -0.9880% | -0.3932% | +0.1452% |
| NQ fold 3 | +0.1296% | +0.2288% | -0.2973% | -0.2509% |
| MNQ overall | -0.3742% | -0.3849% | +0.0781% | +0.1659% |
| MNQ fold 1 | +0.8647% | -0.1942% | +0.0407% | +0.0470% |
| MNQ fold 2 | -1.2526% | -0.7205% | +0.4683% | +0.4246% |
| MNQ fold 3 | -0.5038% | -0.1738% | -0.3391% | -0.0183% |

## Interpretation And Next Decision

NQ has a small overall error improvement, but not uniform fold/stress
improvement. MNQ is mixed and its overall stress error worsens. Neither result
establishes profitable selection, statistical significance, an Apex Evaluation
pass or PA survival. No execution policy or account replay was part of this
experiment; no model is promoted or sent to Windows.

Training folds expose only 3, 5 and 7 distinct releases, respectively. Intraday
rows do not increase the number of independent macro observations. CPI can
also act as a time/regime proxy, so these outcome-informed historical changes
are weak evidence, not causal proof. The relatively larger baseline NQ gain
does not justify increasing size or ignoring unfavorable stress results.

The next model-research step is a separately frozen matched account replay
using unchanged incumbent entry/execution rules, keeping both product results
and all four modes. It must charge any new comparisons before execution and
cannot select a new threshold after viewing these errors. No new run is queued
by this document. Do not resume Windows work under the current user scope.

## Verification And Limitations

- Initial focused tests: 58 passed. Broader affected regression: 757 passed,
  zero failures/errors/skips. Older numerical fixtures emitted 67 warnings;
  these are not a claim of clean full-repository regression.
- Full-suite attempt was interrupted after discovering three failures:
  1,615 passed, 3 failed, 1 skipped in the executed portion. Failures are the
  existing isolated deployment-loader manifest digest, frozen V78 broker-file
  digest, and missing v123_counted_comparisons in the old historical ledger.
  The missing ledger key is also absent in pre-change HEAD. Do not weaken
  those checks, repair Windows code here, or label the full suite green.
- Read-only audit verified all 95 sealed payloads, reproduced all six saved
  models across 252 product/date forecasts, and independently recomputed MSE
  and MAE with scalar fsum across 13,888 candidate-plus-control vectors.
  No new fits, trials or account replays occurred in that audit.
- BLS excerpts were retrieved through web extraction, not original PDF/HTML
  bytes or a historical live feed. Content hashes do not establish historical
  receipt times. Source: https://www.bls.gov/bls/news-release/cpi.htm.

Local result: reports/nq_apex_public_cpi_v144/result.json

Result SHA-256: ce7a603caf379ff5e5d3f56f2a83223f62b85291f7473131fa6452ff9233e311

Seal SHA-256: 9b896b6363c744eefa1cc29462f60af9a4e82b807ab2baf7ec9543d339d4cf31
