# V142 Results And Retrospective

October 7, 2026. **Completed and audited; FAILED the economic gate.** The
[fixed design](research-v142-design.md) changed only target coordinates to
original stop-risk units, inverted using decision-time query risk. This is
outcome-informed development evidence, not independent validation, official
50K account compliance or a recommendation to deploy.

## Execution Evidence

Nine comparisons were reserved, committed and publicly recorded before the
sole supervised attempt started at 19:20:23 UTC. Child 80475 exited zero at
19:46:28 UTC. Supervisor 80465 then completed its no-fit saved-result audit;
tool session 20569 returned exit zero, observed by 20:03:02 UTC. Both processes
are gone. No retry, retuning or partial-outcome selection followed.

Six fixed Ridge pipelines, comprising six joint estimators and twelve scalers,
published all 252 product/date forecasts before scoring. All 181 raw contract
pairs were replayed across four candidate account modes and 126 scored dates.
Four exact saved V141 books were reused without control refitting or replay.
The 181-day label cache was reused; no new raw labels were extracted. Native
fits recorded no warnings. All 48 sealed holdout dates remain closed.

The complete audit restored six models without fitting, regenerated forecasts
and diagnostics, and checked 504 candidate account days and 84 attempts against
original event lineage. It authenticated all three result sections and 59
payloads. The completion record rehashed those payloads, 290 bound source files
and 19 own pins. This is not a second independent raw-entry/first-touch replay.

## Account Results

Modeled trading PnL includes frozen execution costs, but not unpriced program
fees. All four modes remain `EVALUATION_RIGHT_CENSORED`: the observed calendar
ended without a pass. None reached PA or breached the hard trailing threshold.
No breach is not a pass. Each incurred six modeled renewal units.

| Mode | Trades | Active Dates / 126 | Evaluation Trading PnL | PA |
| --- | ---: | ---: | ---: | --- |
| Baseline | 9 | 8 | -$1,602.90 | Not reached |
| Cost only | 6 | 6 | -$1,557.00 | Not reached |
| Latency only | 5 | 5 | -$590.50 | Not reached |
| Combined stress | 5 | 5 | -$1,120.00 | Not reached |

Both primary full-route gates, relative PA benefit and categorical full-route
improvement are false. PA profit differences are unavailable, not zero.
Scenario books are not independent samples and their executed paths differ.

## Failure Attribution

The subsequent [event-matched partition](research-v142-executability-attribution.md)
locates the discrepancy: all filled events match their stored unit-label PnL,
while the positive V142 aggregate is concentrated in unfilled events. It does
not simulate a changed risk policy or rescue this failed result.

Each mode has 21 nominated attempts. In baseline, ten could not fit one contract
inside the existing risk budget and two found the target already reached.
The remaining nine fills produced four target exits totaling +$437.60 and five
stop exits totaling -$2,040.50. This is not a zero-trade software loop. Fewer
trades and no hard breach did not produce positive expectancy in this sample.

Positive-all-four-head opportunities fell from V141's 75 to 24 for NQ and
43 to 6 for MNQ, on unchanged supported populations of 3,708 and 3,236 events.
The 24 NQ guard-free selected unit labels averaged +$73.54, +$20.17, +$86.84
and +$52.25 in baseline/cost/latency/stress order. These potentially overlapping
opportunities are not the feasible chronological account trades. Their positive
average must not substitute for the actual negative account result.

Cash forecast MSE still exceeds the training-only cash mean in every mode for
both products. Candidate error relative to that mean is:

| Product | Baseline | Cost | Latency | Stress |
| --- | ---: | ---: | ---: | ---: |
| NQ | +0.370% | +0.561% | +0.490% | +0.740% |
| MNQ | +0.739% | +1.089% | +0.424% | +0.269% |

Against saved V141, cash MSE improves only for NQ baseline (-0.123%); the other
seven comparisons worsen. Risk-unit error is mixed and does not overturn the
preregistered account gate. Neither response normalization nor sparsity has
established a deployable edge. The matched experiment does not isolate the
effects of feature information, the nomination rule, contract feasibility and
execution. PA routing cannot explain these losses because PA was never reached.

A future hypothesis may distinguish profitable guard-free opportunities from
actually affordable, chronologically executable opportunities. It would require
a new preregistered study, not retrospective relaxation of this run's risk cap,
thresholds or stops. No new study, inversion or larger sizing followed here.

## Evidence And Limits

- Result seal: `1b73f5ece12cacfb8221760f25e8e5fb5cda690ed0464ad6a956b0e40537b37e`.
- Child terminal: `f95336b461386dd624e8d566094a6bd4165484d27f4ce9d30e3c10931078ad89`.
- Completion record: `reports/nq_apex_v142_completion_20261007/completion.json`,
  SHA-256 `a2d396b80610bd3e2b00daf7c91f07216478c9732ba949e6a67d295bc238082a`.
- Pre-market software qualification passed 1,517 distinct affected cases,
  including 246 focused cases; not a full-repository all-green claim.

All nine comparisons remain charged, total 13,293. Current official account
cohort compliance and program fees are not established by these frozen modeled
rules. No live model, order, schedule, credential or Windows process was changed.
V63/V92 signal recovery remains a separate unresolved operational issue; this
research completion is not evidence of model judgment or Telegram delivery.
Private models, source data and detailed ledgers are not publicly published.
