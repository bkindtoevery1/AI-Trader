# V113 Completion

The sole monotone-confidence calibration experiment completed at
2026-09-13T21:35:03Z; launcher exec55026/PID64020 exited0 at21:35:04Z.
All twelve qualified source files and the numeric runtime stayed unchanged.
The run completed181raw contract pairs,126scored dates,12account books and
1512scheduled account-days. Eight scalar fits learned16coefficients using
two forecast transforms; no original HGB, feature scaler or control refit.
Three declared comparisons remain charged, bringing the ledger to13,190.

Terminal result/lock/claim/seal and all20ordered stage receipts are verified.
Original-source/forecast restoration audit exec86558/PID78911 exited0 at21:42:46Z,
verifying3,294dependencies and126forecast envelopes/3,747events without fitting
or account replay. All24market outputs remained unchanged; frozen economic and
predictive summaries reproduced exactly. The separate recorded-account audit
found no discrepancies across79,053checks and597attempts/333executions. Its
1,439represented days plus73mechanical terminal-zero days reconcile to1,512.
The accounting reproducer is saved separately; this is not independent raw-tick
replay or statistical validation. Both actual market/source processes and the
independent auditor are terminal. Final bindings are in
reports/nq_apex_confidence_calibration_v113_execution/execution-verification.json.

## Economic Result

The new model makes **zero PA trades in every execution mode**. Its PA trading
PnL is0USD, but this is abstention, not a profitable strategy or successful PA.
Both frozen primary contrasts fail, as do absolute-positive PA, payout and
modeled full-route gates. All arms reproduce the same NQ Evaluation prefixes.

| Mode | Original PA USD | V112 PA USD | V113 PA USD | V113 inactivity closure |
| --- | ---: | ---: | ---: | --- |
| Baseline | -1,271.14 | -2,086.40 | 0.00 | 2026-05-23 |
| Cost only | -1,588.50 | -2,368.00 | 0.00 | 2026-05-30 |
| Latency only | 1,470.00 | -2,230.48 | 0.00 | 2026-05-19 |
| Combined stress | 742.50 | -1,713.00 | 0.00 | 2026-05-23 |

Against V112, baseline/stress cash differences improve only by avoiding its
losses, while inactivity occurs earlier. Against the original, baseline improves
by1,271.14USD, stress worsens by742.50USD, and both primary modes close earlier.
No added hard-threshold or PA MAE breach rescues those failures. Evaluation
net remains3,254.00/3,292.00/3,130.20/3,429.00USD; those unchanged Evaluation
passes are not evidence that the new MNQ PA mapping helped.

## Failure Attribution

This is not missing-data or failed-solver abstention. The complete84later dates
contain2,504feasible source forecast events. Their fitted stress mapping has
zero total slope and a negative intercept in both later folds:

| Fold | Stress total slope | Stress predicted USD | Feasible scored events |
| --- | ---: | ---: | ---: |
| 2 | 0 | -18.9213136797 | 1,241 |
| 3 | 0 | -13.3194891712 | 1,263 |

The unchanged selector requires all four forecasts to be strictly positive.
Therefore no later event can be nominated. Across all126source dates the
candidate has0joint nominations, versus45original and250V112 nominations.
These are before PA stop, busy, cooldown and account-sizing exclusions, not
executed-trade counts. The first42dates are unchanged original passthrough.
Unlike V112, V113's PA failure cannot be attributed to depleted headroom or
commissions on its own fills: there are no PA attempts or fills.

Prior score/residual covariance is negative in all eight fitted mode/fold
combinations. The declared nonnegative total-slope constraint binds for both
stress mappings and fold3baseline. This is observed calibration behavior, not
proof of an optimizer defect or a causal diagnosis of market predictability.
No slope inversion, threshold relaxation or retrospective rescue was performed.

## Prediction Versus Trading

All eight later-fold/mode mean-squared forecast errors decrease versus both
references. Equal-date/equal-mode pooled loss falls from135,414.0681(original)
and135,308.5796(V112) to132,504.0830(V113): reductions2.149% and2.073%.
These are squared fresh-Evaluation-reference-exposure USD, not realized dynamic
PA cash. Mean-squared-error improvement can coexist with complete abstention
and inactivity failure. Diagnostics are descriptive, not an alternate pass gate,
causal estimate, significance test or independent validation.

## Verification And Boundaries

Preclaim focused qualification:964passes/exit0. Full regression:17,137passes,
two exact existing failures and one skip/exit1; all371new cases pass. The full
suite is not green. The old comparison-count assertion and missing V88 temporary
XML remain recorded. The terminal audit helper passed18synthetic parent smoke
tests; those are code checks, not extra strategy trials or a new full-suite run.

This is historically reused development, not an independent holdout pass.
All48sealed holdout dates remain closed. Trading costs/stresses remain modeled;
program fees, the user's personal Legacy purchase cohort and official compliance
remain unverified. Zero PA trading PnL is not zero after-fee personal cashflow.
No actual payout, live promotion, Windows configuration, order or Telegram change
occurred. Both full user goals remain active. Preserve the failed experiment;
future research needs a separately declared conditional PA-payoff hypothesis,
not another post-hoc adjustment of this already observed calibration.
