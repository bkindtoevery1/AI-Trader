# V139 Paired Minute Results And Retrospective

Completed October 7, 2026. The [frozen design](research-v139-design.md) ran once
through the [qualified execution path](research-v139-execution.md). Execution
and saved-result audit succeeded; the economic experiment FAILED. Neither the
new paired-minute arm nor its exact V136 control passed the full route.

## Complete Evidence

Six pipelines completed 24 response and 12 scaler fits, with no market-fit
warnings. All 252 product/date forecasts preceded scoring. Replay scanned all
181 original paired raw-tick dates and retained all 126 scored dates from
December 3, 2025 through June 12, 2026. Four new books and four exact saved
controls completed; controls were neither refitted nor replayed.

Child exit0 and supervisor/audit exit0 were verified, with both processes gone.
The saved audit verified 94 payloads, six models and all three result sections,
recomputing predictions and summaries without new fitting or account replay.
A subsequent read-only interpretation rehashed all94 payloads and16 own source
pins, and independently summed every executed attempt's PnL, commission and
slippage to its day and phase totals. This is arithmetic reconciliation, not
independent strategy validation or a second raw first-crossing audit.

## Economic Results

USD trading PnL includes the modeled commissions and adverse fills, but excludes
unverified program fee prices. Evaluation and PA are different accounts/phases:
their PnL must not be added and called a final account balance. A dash means
PA was never reached, not a zero-profit PA observation.

| Arm / Mode | Eval Trades | Eval PnL | Eval Pass Date | PA Trades | PA PnL | Ending State |
| --- | ---: | ---: | --- | ---: | ---: | --- |
| V139 baseline | 19 | +3,981.10 | 2025-12-15 | 153 | +667.54 | PA inactivity closure |
| Control baseline | 20 | +3,273.00 | 2025-12-16 | 167 | +686.62 | PA inactivity closure |
| V139 cost only | 16 | +813.00 | No | - | - | Evaluation incomplete |
| Control cost only | 21 | +3,483.00 | 2025-12-17 | 56 | -1,129.50 | PA inactivity closure |
| V139 latency only | 16 | -1,199.60 | No | - | - | Evaluation incomplete |
| Control latency only | 38 | +942.20 | No | - | - | Evaluation incomplete |
| V139 combined stress | 15 | -1,405.00 | No | - | - | Evaluation incomplete |
| Control combined stress | 19 | +582.00 | No | - | - | Evaluation incomplete |

All books have zero recorded hard-threshold breaches and PA MAE violations.
That does not imply success: both full-route gates and the candidate economic
benefit gate are false. Baseline PA contrast is -19.08USD; the other three PA
contrasts remain null with PA_NOT_REACHED. Phase exposure dates differ, so this
is a whole-route comparison, not an isolated matched MNQ treatment effect.

Baseline V139 reaches hypothetical payout eligibility on March13, compared with
February27 for the control. Each models a500USD withdrawal; neither is an actual
payout. V139 finishes with balance50,167.54USD against floor50,100USD, then closes
for inactivity. Its153 PA trades span77 active dates; the control's167 span80.
The three incomplete candidate Evaluations each record one purchase and six
renewal units. These unpriced costs cannot be ignored by calling inactivity free.

## Failure Attribution

This is not V138's zero-nomination failure. Across the full scored support,
V139 nominates446 of3,708 NQ opportunities and300 of3,236 MNQ opportunities;
the control nominates488 and328. Candidate baseline executes172 trades across
both phases, including21 giveback exits. New paired features did not translate
into a robust executable advantage.

| Candidate Mode | Risk-Cap Rejections | Last Filled Date | Longest Inactive Processed Sessions |
| --- | ---: | --- | ---: |
| Baseline | 20 | 2026-05-13 | 11 |
| Cost only | 283 | 2025-12-22 | 112 |
| Latency only | 242 | 2025-12-22 | 112 |
| Combined stress | 236 | 2025-12-22 | 112 |

The three stressed paths stall after early fills: their remaining headroom and
the unchanged risk allocator cannot fund many nominated one-NQ trades. For
example, the final stress-day attempt records309.50USD headroom,154.74USD risk
budget and907USD one-contract reserve, hence quantity0. Raising a maximum
contract limit cannot make the minimum executable contract smaller. Existing
MNQ allocation studies, including V98 and V133, already failed their full
routes; switching product is not an untested automatic cure.

These recorded skip reasons identify a mechanical bottleneck, not the unique
causal explanation for the early losses. No data shortage, software crash or
threshold breach explains away the failed economics. No rule is relaxed to
turn these results into a pass.

## Forecast Diagnostics

Date-equal MSE percent change relative to the saved control; negative is better.
All four heads and all three folds are shown, without selecting a favorable one.

| Product / Fold | Baseline | Cost Only | Latency Only | Combined Stress |
| --- | ---: | ---: | ---: | ---: |
| NQ overall | -0.582% | -0.650% | -0.144% | -0.608% |
| NQ fold1 | +0.724% | +0.356% | -0.951% | -0.312% |
| NQ fold2 | -0.789% | -0.120% | +0.581% | -0.895% |
| NQ fold3 | -1.267% | -1.929% | -0.346% | -0.508% |
| MNQ overall | +0.548% | -0.351% | +0.336% | +0.512% |
| MNQ fold1 | +1.223% | -0.229% | -0.490% | +0.203% |
| MNQ fold2 | +0.308% | -1.230% | +1.587% | +2.014% |
| MNQ fold3 | +0.249% | +0.677% | -0.478% | -1.159% |

MNQ retains two empty scored dates,124 nonempty of126; NQ has126 nonempty dates.
Small NQ forecast-error improvements did not improve the complete account
route. Overall selected ORIGINAL-exit one-contract label means in the same
four-head order are58.83/24.55/28.01/-2.71USD for NQ and
-1.14/-4.88/-0.64/-5.13USD for MNQ. In fold3, both products' selected means are
negative in every mode. Opportunities may overlap; these are not account PnL.

Both arms were explicitly designed to learn original-exit cash labels while
executing the later giveback exit. That disclosed mismatch is not an integrity
defect justifying a rerun. A separate matched target-alignment experiment can
test it, but cannot assume alignment will fix headroom, costs or PA survival.

## Retained Boundaries

Five comparisons remain charged, total13,272. Reused historical development is
not independent confirmation. All48 sealed dates stay closed. No actual50K
pass, current-cohort compliance, live promotion or order is claimed. The2,280
affected software cases passed before execution; the previously disclosed
full-repository suite is still not claimed green.

The earlier completion audit intentionally records the pre-interpretation
checkpoint. It is preserved unchanged, not rewritten after reading outcomes.
The new interpretation receipt is
`reports/nq_apex_paired_minute_v139_interpretation.json`.

- Result seal SHA256: `b9c51eb66aaad5d34e6625da5fe453ce6783e74b903bbb2ecea8c607ff5c26f3`.
- Child terminal SHA256: `a727b08f1f28b4327128d78620f8d3735d0b067b162be76a47748c18df2f187d`.
- Completion audit SHA256: `dac7e1a4c93e479da8530ba76ce5dfdc947528cc7b8f67f0e481bd3832b4db20`.

The full research and Windows operation goal remains active. Daily archival
success is separate from fresh collection/model/Telegram operation. The latest
Windows diagnosis and unperformed recovery prerequisites remain in
[the archive/recovery record](windows-daily-archive-20261006.md).
