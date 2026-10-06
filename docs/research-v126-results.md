# V126 Results And Retrospective

Completed October 6, 2026. This is an exploratory forecast comparison on reused
development dates, not independent validation or an Apex account pass.

## Execution

The [fixed design](research-v126-design.md) was reserved before the sole market
run. All nine candidate/fold pipelines fitted and published complete forecasts
before scoring. The process exited 0; a subsequent read-only audit exited 0,
verified all 32 sealed output files, and reproduced the stored summaries and
screen decisions without another fit. Runtime/source identities were unchanged.

Three families were evaluated: ridge, histogram gradient boosting and a small
two-hidden-layer MLP. There were 18 response-estimator fits and 18 scaler fits.
The three chronological scoring blocks contain 126 scheduled dates, 124 with
supported opportunities, and 3,236 supported events in total. Training prefixes
contain 45/87/129 dates and 1,335/2,372/3,391 supported examples respectively,
with ten purged sessions before each 42-date scoring block. The complete
calendar, including empty dates, was retained. The 48 sealed dates stay closed.

## Forecast Results

Percentage change in date-equal mean squared error relative to each fold's
training-weighted constant mean; positive values mean worse predictions.
Labels retain original one-MNQ commissions, slippage and execution scenarios.

| Candidate | Baseline | Cost only | Latency only | Combined stress | Screen |
| --- | ---: | ---: | ---: | ---: | --- |
| Ridge | +1.3443% | +1.4415% | +0.7748% | +0.8550% | Failed |
| Histogram boosting | +2.8682% | +3.3650% | +3.8908% | +4.0918% | Failed |
| Small MLP | +14.3078% | +14.2972% | +15.2236% | +14.5076% | Failed |

All three fail even the pooled-error condition, before requiring improvement
in every chronological block. MLP fold 1 additionally reports L-BFGS abnormal
termination after 46 iterations. That warning and its forecasts are retained;
there was no retry, solver change, hyperparameter search or replacement fit.

Descriptive means among opportunities whose four predictions were positive:

| Candidate | Opportunities | Baseline USD per label | Stress USD per label |
| --- | ---: | ---: | ---: |
| Ridge | 253 | -5.39 | -3.78 |
| Histogram boosting | 364 | +4.26 | -1.75 |
| Small MLP | 567 | -3.50 | -5.98 |

These are overlapping event labels, not executed trades or additive account
profits. No V126 account replay, account PnL or drawdown was computed. In
particular, boosting's positive baseline average is not a trading strategy
success: its third-block selected mean was -15.92 USD baseline and -21.13 USD
stress, unlike positive selected means in the first two blocks. This is
descriptive instability, not a proven causal explanation or a new selection rule.

## Interpretation

The same causal price/minute-volume representation does not show a stable
forecast advantage under these fixed learners. Switching learner complexity
alone did not solve the problem. Ridge is closest to the constant control but
still worse; this does not justify deployment. The small neural network has
both worse generalization and one numerical warning, so the evidence does not
support scaling it into a larger network on this representation.

The [V125 account result](research-v125-results.md) separately establishes that
restoring trading activity is insufficient: its baseline PA book made 60 trades
and lost 220.58 USD before unpriced program fees. Future research should test a
distinct information or economic hypothesis, not force more trades, relabel
these diagnostics as account profits, or relax costs to rescue a failed result.
No operational V63/V92 policy, signal route or order permission changed.

## Verification And Limits

Affected regression: 326 passed, 24 recorded synthetic-fixture warnings, exit 0.
Three orchestration review findings were fixed before market execution: parent
comparison reservation, durable fit-attempt accounting, and precise disclosure
of prepared-label access. The prior repository-wide suite remains nongreen;
it was not rerun or represented as passing for this change.

The postrun audit uses shared summary code and retained V123 source evidence.
It is not an independent numerical implementation or a new full raw-tick scan.
The prepared labels were authenticated; each fit saw only its own mature
training prefix. Previously scored dates can legitimately enter later training
prefixes. None of this makes the reused development period an independent test.

Six comparisons remain charged: cumulative total 13,227. There is no account
promotion, verified 50K pass, holdout opening or automatic repeat of this attempt.

Evidence SHA-256:

- Claim: `7dfdc97b78dd24e30786c1c8dac5b075c458fc9bfcffedd55cb86bcda1ee4e3c`
- Status: `3e01c850d73db8843ffc5a141da254c883d0dcf9fc584fe684c133d9c8f54269`
- Result seal: `7572595de007bdc8f51aba3077bedb9459895bb6071eda76b8e9bd4fab3a137b`
- Affected JUnit: `092d8783e2819462585467f13663fa9deefbb2b4671d053bce70a0c05497fc74`

Detailed local artifacts remain under `reports/nq_apex_payoff_screen_v126/`;
fitted models, raw data and private source ancestry are not public attachments.
