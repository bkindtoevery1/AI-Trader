# V138 Direct Utility Results

Completed October 7, 2026 KST. The [frozen design](research-v138-design.md) and
[qualified execution](research-v138-execution.md) ran once. Software execution
and saved-result verification succeeded; the model's economic gates FAILED.

## Complete Experiment

Six product/fold pipelines completed 24 response and 12 scaler fits without
market-fit warnings. All 252 forecasts were published before scoring outcomes.
The replay scanned 181 original paired raw-tick dates and processed all 126
scored development dates, December 3, 2025 through June 12, 2026. Four new mode
books were compared with four exact saved V137 projected-joint books. There
was no control refit/replay, new raw-label generation or holdout opening.

Child exit was zero at 01:06:13 UTC; supervisor saved-result audit exit zero
was observed at 02:13:31 UTC. Both processes are gone. The audit authenticated
345 payloads and all three complete result sections, six fitted models,
181 receipts, 14,832 own-state queries and four exact controls. It recomputed
forecast diagnostics and account arithmetic without refitting or replaying.
This shared-code audit is not independent strategy validation or a separate
raw first-crossing audit. All 48 sealed holdout dates remain closed.

## Economic Failure

| Mode | V138 Trades | V138 Trading PnL | V137 Control Trades / PnL |
| --- | ---: | ---: | ---: |
| Baseline | 0 | $0 | 1 / -$148.10 |
| Cost Only | 0 | $0 | 1 / -$167.00 |
| Latency Only | 0 | $0 | 1 / +$116.90 |
| Combined Stress | 0 | $0 | 1 / -$167.00 |

Neither arm passes Evaluation or reaches PA in any mode. Both full-route
gates and the candidate economic-benefit gate are false. Zero trading loss is
not success: each candidate book remains inactive for all 126 dates. The
modeled lifecycle records an initial purchase and six monthly renewal units;
their dollar prices are unverified, so $0 is NOT after-program-fee PnL.

Each candidate book made 3,708 nonzero-capacity queries, all with planned size
one NQ and zero out-of-grid states. None satisfied all four positive scores.
Individual baseline/cost/latency/stress heads were positive 25/1/5/1 times;
their joint intersection was empty. Four identical inactive books do not turn
these into 14,832 independent opportunities. No candidate account queried MNQ
because Evaluation never passed; MNQ account economics were not exercised.

This repeats V137's nomination starvation rather than a missing-data or
zero-contract-capacity failure. Direct estimation of the same one-step utility
did not solve it. The unchanged rule, learned scores and objective together
produced abstention; these observations alone do not prove a relaxed threshold
would be profitable. No threshold rescue, fallback winner or new trial was run.

## Forecast Diagnostics

Equal supported-date MSE, then an equal average of the four predefined heads:

| Product | Nonempty Dates | Direct MSE vs Separate Raw | Direct MSE vs State Mean |
| --- | ---: | ---: | ---: |
| NQ | 126 | 0.464% lower | 0.701% higher |
| MNQ | 124 | 0.056% higher | 2.860% higher |

Two empty MNQ dates remain explicitly retained in the complete diagnostics.
The small NQ improvement over separate regression does not beat the simpler
state mean and did not create executable nominations. These descriptive
aggregates are not a significance test, independent evidence or a selection
gate. All folds/heads remain in the sealed result; none was picked as a winner.

## Evidence And Retrospective

The one attempt took about 3 hours 44 minutes including the supervisor audit.
Source inspection shows repeated whole-source/population validation; a limited
runtime sample also observed Python computation and JSON serialization. This
supports investigating redundant verification cost, not an exact phase-level
profile. A future performance change must preserve evidence and results, not
remove checks or rerun this closed study as another model-selection attempt.

The five preregistered comparisons remain charged, total 13,267. The 2,519
affected software tests passed before execution; the previously disclosed full
repository suite remains not green. No new software-suite pass is inferred
from successful market execution. Source, sizing, costs and all gates stayed
unchanged. No model promotion, Windows change or order was performed.

Private evidence (not published raw data or models):

- Result seal: `reports/nq_apex_transition_utility_v138/result_seal.json`, SHA256
  `26dbf76c68e2da32bc6b289043d3e2f97e50d28b09d18fcd66fd43d6ffeeefbc`.
- Child terminal: SHA256
  `3e745780fb4bd0aeacc6c7ccea1b4be20e188468bc4e8ea4014c2c7c6ab7c70e`.
- Supervisor audit receipt: `reports/nq_apex_transition_utility_v138_audit.json`,
  SHA256 `e11d1831f0d54ffc3169eb09f2ddb902bfd554c24a267cc49bc21f46bcb22c41`.

The full research and Windows operation goal remains active and incomplete.
No verified current-cohort 50K pass or working fresh live signal is claimed.
