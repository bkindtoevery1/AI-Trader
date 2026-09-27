# V116 Completed Existing-Data Evaluation

## Decision

V116 fails both preregistered relative-improvement comparisons and the separate
PA profitability, payout and full-route gates. Do not deploy it or call the
absence of trading losses a success. Windows collection and new data were not
dependencies of this evaluation.

The candidate combines prior out-of-fold original MNQ and NQ dollar forecasts
with a constrained residual ridge calibration. It does not refit the original
HGB models or scalers. Eight scalar fits learned 24 coefficients across two
later folds and four cost/latency modes; the first fold is exact original
passthrough. Three comparisons were charged once, 13,196 to 13,199.

## Data And Results

Already admitted explicit-contract NQ/MNQ tick pairs cover 181 dates from
2025-09-08 through 2026-06-12. There are 126 scored dates from 2025-12-03 through
2026-06-12, in three chronological 42-session folds. Prefix-only calibration,
ten-session purge and label maturity remain unchanged. This is reused historical
development data, not a fresh independent test; the 48 sealed holdout dates
were not opened.

| Mode | Evaluation Trading Net USD | Evaluation Trades | V116 PA Trading Net USD | PA Trades | Modeled Inactivity Date |
| --- | ---: | ---: | ---: | ---: | --- |
| Baseline | 3254.00 | 10 | 0.00 | 0 | 2026-05-23 |
| Cost Only | 3292.00 | 14 | 0.00 | 0 | 2026-05-30 |
| Latency Only | 3130.20 | 8 | 0.00 | 0 | 2026-05-19 |
| Combined Stress | 3429.00 | 8 | 0.00 | 0 | 2026-05-23 |

The NQ Evaluation policy is unchanged, so these simulated Evaluation successes
are reproduced controls, not an improvement attributable to V116. They cannot
be summed with the fresh PA balance or interpreted as cash withdrawn.

V116's independently recomputed account fields equal the saved V113 monotone
control in all four modes. Compared with the original MNQ control, baseline PA
net improves by USD1271.14 only by not trading, while combined-stress PA net
deteriorates by USD742.50. Earlier inactivity also fails the comparison. There
are no hard-threshold or PA-MAE breaches, but zero PA profit and no payout.

## Failure Attribution

This is a model nomination failure, not missing data or an absent backtest.
All 3,747 saved forecast events are present across 1,243 / 1,241 / 1,263 events
in the three folds. None satisfies the unchanged all-four-predictions-positive
rule. The first-fold stress forecast is always negative; the second-fold
stress forecast is constant at approximately -18.9213 reference-exposure USD.
In fold 3, baseline is constant at +7.0028, but cost-only forecasts range from
-17.0859 to -16.0406 and stress from -25.4432 to -5.9509.

The fitted NQ coefficient is zero in all fold-2 modes and fold-3 baseline/cost;
it is positive only in fold-3 latency/stress. The own-forecast total slope hits
zero in fold-2 stress and fold-3 baseline/stress. Adding an NQ score therefore
does not repair the zero-nomination behavior already seen in V113. A positive
baseline score alone cannot satisfy the existing joint rule. On baseline PA's
represented interval, 664 events divide into 561 model abstentions and 103
stop-support exclusions; none reaches execution sizing.

The next hypothesis should address the mismatch between fresh-Evaluation
reference-exposure dollar prediction and PA account utility, rather than repeat
another score-only calibration or force trades by lowering a threshold after
seeing this result. This is a proposed direction, not a new model, trial,
performance claim or authorized change to this completed experiment.

## Verification

The sole market process, PID12410 / exec36674, exited 0 at
2026-09-22T17:23:17Z. Source audit v3, PID33053 / exec56272, exited 0 at
17:52:52Z. Independent JavaScript accounting, PID34972 / exec26889, exited 0
at 17:53:03Z with 153,992 arithmetic checks and no discrepancies. All 24 market
outputs remain unchanged. Source restoration verified 3,570 dependencies,
126 forecast envelopes, eight exact control books and four exact candidate
Evaluation prefixes without new fitting or raw replay.

The twelve books contain 1,512 scheduled account-days, 1,408 represented days
and 104 terminal zero days. They include 206 executed trades across controls,
not 206 V116 PA trades. They are overlapping comparative books, not independent
statistical samples. The independent audit checks recorded-ledger arithmetic;
it is not a second independent raw-tick fill engine or statistical validation.

Source auditors v1 and v2 each exited 1 because of overbroad auditor guards.
Their files and failures are preserved. V3 corrects method-identity interference
and permits only initial geometry under the exact reference-exposure helper;
fit, replay, account advancement and trading calls stay blocked. See
`docs/research-v116-audit-repair.md` and
`docs/research-v116-audit-repair-v3.md`. The market attempt was never restarted.

Qualification passed 466 focused cases. The completed full suite had 18,493
passes, two verified preexisting failures and one skip; it is not fully green.
The known failures are the old account-transition trial-count assertion and a
missing legacy V88 temporary evidence file. V3 audit preparation passed the
43 inherited cases, eight guard checks, three geometry checks, 18 launcher
checks and 18 finalization checks. These software checks are not profit gates.

Trading commissions and slippage are priced. Evaluation subscription/renewal
and PA activation fee units are recorded, but program-fee dollar prices and
the user's actual account cohort remain unverified. Zero PA trading net is
therefore not zero all-in expense. There is no verified personal Legacy50K
pass, independent validation or live deployment. Orders, Telegram tests,
purchases, Windows changes and schedule changes were not part of this run.
