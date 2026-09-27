# V117 Completion: More PA Trades Did Not Improve Returns

## Decision

Completed on 2026-09-22 UTC using existing Mac data only. Windows collectors,
new sessions and new credentials were not dependencies. The candidate failed
the preregistered relative benefit gate and the modeled full-route gate. Do not
deploy it or call it a verified personal Legacy 50K pass.

This was one PA nomination-policy ablation, not a newly fitted model. It retained
the six causal V102 model records and all original forecasts. Evaluation kept
the original four-positive-head rule; PA required only a positive baseline
head. All execution, sizing, costs and account constraints were unchanged.

## Data And Design

- 181 existing explicit-contract NQ/MNQ raw pairs, 2025-09-08 to 2026-06-12.
- 55 context dates and 126 scored dates, 2025-12-03 to 2026-06-12.
- Original chronological three-fold vintages and ten-session purges preserved.
- Two arms, four execution modes, eight complete account paths and 1,008
  scheduled account-days. These are not eight independent market samples.
- No new estimator/scaler fits. Two comparisons were charged once: 13,199 to
  13,201. Audit repairs did not rerun the market or charge additional trials.
- The 48 sealed historical holdout dates remained closed. This repeated,
  outcome-informed historical comparison is development, not independent
  statistical validation.

## Results

PA trading PnL in USD, after the modeled trading fees and execution effects:

| Execution mode | Original control | V117 candidate | Difference | PA trades, control / candidate |
| --- | ---: | ---: | ---: | ---: |
| Baseline | -1,271.14 | -1,400.52 | -129.38 | 22 / 57 |
| Cost only | -1,588.50 | -2,404.50 | -816.00 | 15 / 39 |
| Latency only | +1,470.00 | -1,953.36 | -3,423.36 | 25 / 53 |
| Combined stress | +742.50 | -1,020.50 | -1,763.00 | 24 / 33 |

The required baseline AND combined-stress improvement failed. Cost-only and
latency-only were diagnostics and did not rescue the result. Candidate PA was
negative in all four modes. Hypothetical payout and modeled full-route passes
were zero for both arms. No hard-threshold breach or PA MAE violation occurred.

Candidate baseline PA remained open at the observation boundary; this is
right-censoring, not indefinite survival. Candidate cost-only, latency-only and
stress paths closed for inactivity. The stress closure was 2026-05-30; the
control did not close in the observed calendar. These are modeled lifecycle
dates, not an assertion that May 30 was a scored exchange session.

Evaluation paths exactly matched the control in every mode, with numeric
passes and PnL of $3,254.00, $3,292.00, $3,130.20 and $3,429.00 respectively.
Those Evaluation profits are NOT PA cash and do not offset PA losses.
Subscription and activation fee dollars remain unpriced; personal account
cohort and official compliance are unverified. No actual payout was received.

## Failure Attribution And Reflection

Relaxing the head filter solved the zero/low-trade symptom, not profitability.
Baseline PA fills increased from 22 to 57 while losses increased. Candidate
baseline had 33 model-stop exits versus 24 model-target exits, and 62
`RISK_CAP_FLAT` attempts versus 3 for the control. More nominated opportunities
did not ensure positive executable value or available risk capacity.

This is a path-level comparison: different fills alter later risk capacity and
eligibility. The PnL difference is not the isolated return of extra trades and
does not establish a causal effect for all future markets. The observed data
reject this specific relaxed policy; they do not justify forcing activity,
raising size to recover losses or weakening the pass gate after observation.
Any next experiment needs a distinct declared hypothesis on the same admitted
data, with forecast quality and account feasibility considered separately.

## Verification And Repair History

The sole market process (PID 68119) exited 0 at 21:29:23Z. Source audit v1
(PID 82927) exited 0 and restored all six original models, 252 forecast
envelopes, four exact controls and four exact Evaluation prefixes. Independent
account audit v3 (PID 92396) exited 0 with 209,291 arithmetic/consistency checks
and no findings. Completion verification exited 0. All four market files
remained byte-identical through finalization.

Account audit v1 failed because native Evaluation records can omit event IDs;
v2 repaired exact decision-clock identity but still expected excluded forecasts
in Evaluation records. V3 reconciles the original nominated Evaluation subset,
as required by the frozen source contract. PA still requires the full forecast
population. Financial arithmetic, model, market results and gates did not
change. Both failed audits and their process receipts are preserved. These
auditor defects are separate from the candidate's economic failure.

Qualification: 358 focused tests passed; full regression had 18,851 passed,
2 exact preexisting failures and 1 skipped. This is NOT a globally green suite.
The known failures are the old account-transition candidate-count assertion
and a missing V88 temporary XML artifact; see runner qualification. Subsequent
v3 synthetic checks passed: JS auditor 60, observer 47, completion 64. Synthetic
tests are software evidence only, not trading evidence. Full-suite qualification
preceded the standalone v3 auditor repairs; their checks are reported separately.
After updating central state, its focused regression had 19 passes and the same
two known failures, with no new failures. Evidence is
`reports/nq_apex_baseline_nomination_v117_execution/completed-state-v1.xml`.

Authoritative completion:
`reports/nq_apex_baseline_nomination_v117_execution/execution-verification-v3.json`

SHA-256:
`e8090c2b622b0ecd05d12e425974f22585b20bc80e5662d46138016f67b86420`

The completion binds market outputs, original-source verification, both failed
accounting attempts and the successful independent recorded-account audit.
It is not an independent raw-tick fill-engine replication or a statistical
validation claim. Windows readiness was not established by these Mac results.
No orders, Telegram messages, purchases, secret transfers, schedule changes or
holdout observations were made. Both broader research/Windows goals remain
active; this experiment is closed and must not be silently rerun or retuned.
