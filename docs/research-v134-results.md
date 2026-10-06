# V134: Prior Opportunity History Results

Completed October 6, 2026. Read the [pre-execution design](research-v134-design.md).
Verdict: forecast comparison completed and audited; economics NOT_EVALUATED.
No Evaluation, PA, payout, independent-validation or verified 50K pass is claimed.

## What Was Learned

Adding prior opportunity clustering and side history modestly improves pooled
NQ prediction error and the descriptive mean of nominated opportunity labels.
The favorable stress mean is concentrated in the middle fold; the last fold
remains negative. MNQ nominations deteriorate versus the retained own-product
control despite lower pooled MSE in three modes. Prediction-error improvement
alone is not executable account profitability. No favorable mode or product
was promoted, retuned or substituted into the operating models.

This addresses a different hypothesis from merely reducing contract size in
V133, adding terminal-return confirmation in V132, or session location in V127.
It does not establish which of the three new coordinates causes any change.

## Fixed Experiment

The first twelve local features, own-product labels, query support and HGB
recipe remain unchanged. Three causal coordinates describe the previous
30 minutes of ALL original broad opportunities: count, same/opposite imbalance,
and time since an opposite opportunity. Current/future outcomes and account
state are excluded. History resets each date, remains within the explicit
contract, and is left-truncated by the original 10:30 ET event universe.
Both product models still use NQ event features, not MNQ-derived features.

181 development dates, training prefixes of 45/87/129 sessions, ten-session
purges and three 42-session scored folds were retained. These 126 dates were
already used in historical research; they are not a fresh independent holdout.
All 48 sealed dates remained closed. NQ has 3,708 supported scored events on
126 dates; MNQ has 3,236 on 124 dates, retaining two empty dates in the calendar.

Six new product/fold pipelines completed: 24 response estimators and 12 scalers.
Exact retained own-product HGB forecasts served as controls, without refitting.
Complete forecasts were published before scoring labels were attached. There
was no fresh raw-tick replay or account simulation in this forecast stage.
Four comparisons were reserved before extraction/fitting; total 13,250 to
13,254. No retry, grid, genetic algorithm or threshold rescue was performed.

## Prediction Error

MSE improvement is `100 * (1 - candidate MSE / control MSE)`, using date-equal
means on matched support. Positive means lower error, not statistical significance.
MAE differences are candidate minus control, in cents; negative is better.

| Product | Mode | MSE Improvement | MAE Difference, Cents |
| --- | --- | ---: | ---: |
| NQ | Baseline | 0.3476% | -76.5968 |
| NQ | Cost only | 0.1680% | +23.6756 |
| NQ | Latency only | 0.0818% | -74.6058 |
| NQ | Combined stress | 0.0525% | -69.0926 |
| MNQ | Baseline | 0.1763% | -1.3676 |
| MNQ | Cost only | -0.2136% | +3.1526 |
| MNQ | Latency only | 0.4394% | -12.4919 |
| MNQ | Combined stress | 0.9340% | -19.8106 |

Improvement is not uniform by fold: NQ stress MSE worsens in fold 2, cost MSE
in fold 1, and latency MSE in folds 1 and 3. MNQ baseline/latency MSE worsen
in fold 1; cost MSE worsens in folds 1 and 2. Full per-fold/per-mode MSE and
MAE contrasts remain in the sealed result and were recomputed by the audit.

## Descriptive Nominations

These are one-contract net-label means for opportunities whose forecasts are
positive in all four modes. Opportunities can overlap and may be unexecutable
together. Counts are NOT actual trades; dollar means are NOT account PnL or
live expected returns. Do not sum these labels into an equity curve.

| Product / Model | Opportunities | Baseline USD | Cost USD | Latency USD | Stress USD |
| --- | ---: | ---: | ---: | ---: | ---: |
| NQ new history | 488 | 37.65 | 2.66 | 35.49 | 8.84 |
| NQ retained HGB | 489 | 25.88 | -9.23 | 10.56 | -18.37 |
| MNQ new history | 328 | 1.43 | -2.84 | 2.69 | -2.75 |
| MNQ retained HGB | 364 | 4.26 | 0.13 | 3.96 | -1.75 |

| Product / Model | Fold 1 Stress USD | Fold 2 Stress USD | Fold 3 Stress USD |
| --- | ---: | ---: | ---: |
| NQ new history | -0.04 | 125.64 | -76.63 |
| NQ retained HGB | -33.82 | 68.56 | -79.68 |
| MNQ new history | -1.25 | 9.23 | -18.97 |
| MNQ retained HGB | 2.58 | 10.81 | -21.13 |

Candidate nominations by fold are 159/146/183 NQ and 122/112/94 MNQ. The NQ
pooled change merits a declared execution test, not a pass claim. The MNQ
forecast-only results do not establish a nomination benefit. Any account test
must preserve all modes, calendar, own account transitions, costs, risk limits,
and missing-PA semantics; it needs a separate declared comparison charge.

## Verification And Completion

- Frozen local implementation: `95e9b5d`.
- Public pre-execution design: `a03c53ca8e6777d30ccd4d84732bb835400a8298`,
  branch `codex/research-records-v134`, remotely verified before execution.
- 204 focused plus 629 affected tests passed, 833 unique cases. The affected
  suite has 32 retained synthetic scaler warnings. This is not a claim that
  the full repository suite ran or passed. Market fitting emitted no warnings.
- Source-only and actual runner preflights exited 0 before any new fits.
- Sole supervisor exec58517, parent70161 and child70181; no replacement launch.
  Child completed at 09:57:40.170167 UTC, terminal exit0/source unchanged at
  09:57:40.446565 UTC. Supervisor audit exit0 was observed at 10:01:09 UTC.
- The supervisor, a separate process from the fitting child, verified 94 sealed
  files, restored all six models, and recomputed predictions and summaries with
  fits forbidden. Native accounting reconciles 36 fits/72 native events and
  12 pipeline events. Both processes are gone. No third audit run is claimed.
- This consistency audit shares implementation with the study. It is NOT
  independent numerical validation or reestablished raw-provider provenance.

| Artifact | SHA-256 |
| --- | --- |
| claim.json | `2d9afcfd2422a8a2c9f1c0af112de480bab7d002f807b27bfefa3e775459bba0` |
| result.json | `bfa74981ad3d68e7e1b7cd78688881a8df3d8be13349732955f9b217787336ce` |
| status.json | `d37ea7ed26d72aa4d36aa8463899cde659f5fec5f02335b8f1078ef4275f4650` |
| result_seal.json | `adfa5d8e03b7cd3b1670f864202e3d8ea978246aa66601d1fea1faecdf7dddcd` |
| persist_forecasts.json | `326e2b3c025e59f8ede1548d99b8d96986a5fe62b4f1c95e44084dde1107303a` |
| execution terminal.json | `29276a848d37d1b5b71936be3f2ae06d3d59e5597d894f12eb7d4518a388fc3a` |

Evidence is retained locally under reports/nq_apex_event_history_v134 and its
execution directory. No market rows, fitted models or credentials accompany
this public summary. Windows was observed unchanged at idle revision615; this
is not new operating evidence. No Windows, schedule, order, login, purchase,
Telegram or operational-model change occurred. The overall research/Windows
goal remains active; this forecast experiment is complete.
