# V110 Selector Transfer: Completed Development Failure

The single frozen attempt completed at2026-09-13T09:43:05Z, actual process exit0.
This is successful execution, not a successful strategy. Independent terminal
review found no integrity or accounting discrepancy:400 attempts,294fills,
1040contracts,1004represented days plus4terminal-padding days reconcile.
It verified all3157dependencies twice without rereading raw market payloads or
rerunning predictions. This audit is not independent statistical validation.
Read reports/nq_apex_selector_transfer_v110_runner_implementation/execution-verification.json.

## Result

The treatment kept the original NQ forecast nomination in PA, then executed
MNQ at its own prices, point value, commission and slippage. It did not rescale
forecast dollars, refit, change stops or sizing, or relax the account rules.

| Mode | Control PA Net | V110 PA Net | Difference | Control/V110 PA Trades |
| --- | ---: | ---: | ---: | ---: |
| Baseline | -$1,271.14 | -$1,332.92 | -$61.78 | 22/35 |
| Cost Only | -$1,588.50 | -$2,079.00 | -$490.50 | 15/19 |
| Latency Only | +$1,470.00 | +$1,754.90 | +$284.90 | 25/38 |
| Combined Stress | +$742.50 | +$182.50 | -$560.00 | 24/36 |

Both primary deltas, baseline and combined stress, are negative. The frozen
economic-benefit gate therefore fails. The positive latency-only difference
cannot rescue it. More executed trades did not improve the primary account
results. These whole-path differences include feedback through sizing and
eligibility; they are not isolated PnL of only the additional trades.

The four unchanged Evaluation prefixes numerically passed, as did their four
controls. This is not new Evaluation improvement. Neither arm reached a first
hypothetical payout or the full-route gate. Baseline PA remains loss-making;
combined-stress PA is positive but below its control. Cost-only accounts close
under the modeled activity rule on2026-06-10. Baseline, latency-only and combined
stress survive only the observed PA calendar. All paths report zero hard-floor
breaches and zero PA MAE violations.

## Evidence And Limits

The runner restored six original model records and252 forecast envelopes with
zero new estimator or scaler fits. It fully checked181 explicit same-maturity
NQ/MNQ raw pairs, retained55 context dates and126 scored development dates,
and executed eight account paths with1008 scheduled account-days. It verifies
four exact completed V107 controls, unchanged NQ Evaluation prefixes and all
original raw/window receipts. All3157 dependencies were bound before the claim.

The original source preflight exposed a real schema-integration defect missed
by invented fixtures: V109 projection belongs to its preoutcome lock, not its
status. The code and fixtures were corrected before any claim or economic
replay. Original failure receipts remain intact. Corrected78focused tests pass;
the full suite records15662pass/2exact unchanged baseline failures/23skip,
including all78new cases and unchanged hashes of all10 scope files. This is
not an all-green suite. Real source preflight and freeze subsequently exit0.

The one policy plus one contrast retain exactly two comparison charges,
total13181. There is no restart, integrity successor, post-result retuning,
favorable-mode selection or operational replacement. The48 historical holdout
dates remain closed. Reusing outcome-informed development dates does not
establish independent validation or a verified50K pass.

Trading net includes modeled commissions/slippage but excludes unpriced
program fees. The modeled post2026-03-01 PA activity cohort is unchanged;
the user's personal Legacy purchase cohort and official account compliance
remain unverified. No live orders or Telegram messages were sent.

## Immutable Bindings

- Lock:3100673d091da176dca49d58fd35dd7ba93a26b1ef75011e127441fad494ffaa
- Claim:de92768f4360fec48b8f7db2002ba554205d039cd991515e4204594edae075ba
- Status:46173d4e984c74a21f57e322c984e3d6cd79ffc4db32e8dfb11975b34643b9df
- Seal:d679323b22bd69f875d3ef8883ffed203de229cd53a7e54bfa1d8091a96004ac

Original output is reports/nq_apex_selector_transfer_v110. Raw process receipts
and software verification are in
reports/nq_apex_selector_transfer_v110_runner_implementation.
Both full user goals remain active and incomplete.
