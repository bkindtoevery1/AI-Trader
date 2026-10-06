# V132 Results: Terminal Confirmation Does Not Improve The Account Route

## Completed Execution

The sole supervised replay completed at 2026-10-06T08:30:26.669310 UTC.
All 181 explicit-contract raw pairs (402,041,614 ticks) and 126 scored dates
were processed. Sixteen books reconciled: eight new confirmation books and
eight exact original/HGB controls. The two fixed V131 history forecasts only
vetoed V130 HGB nominations; no fit, inference, threshold search or new label
generation occurred. Existing unit journals remained hash-bound, not recomputed.
Five comparisons remain charged, bringing the historical total to 13,248.

Child and supervisor exited 0 with source unchanged. The supervisor's audit
and a separate saved-result audit both passed. Three sealed output files,
complete saved forecasts, decisions, receipts and summaries were verified.
A separate direct sum of daily PnL and trade counts matched all 32 account-phase
combinations. All required processes are terminal. This is evidence consistency
and arithmetic checking, not independent model or raw-replay replication.

## Account Results

Amounts are simulated trading USD after modeled commissions, slippage and
execution effects, before unpriced purchase, renewal and activation fees.
Evaluation and PA are separate capital accounts, not additive spendable equity.
An absent PA is shown as a dash, not measured zero-return PA performance.

| Route / Mode | Evaluation PnL | Evaluation Trades | PA PnL | PA Trades | Final State |
| --- | ---: | ---: | ---: | ---: | --- |
| Recent confirmation / baseline | +77.20 | 38 | - | 0 | Evaluation unfinished |
| Recent confirmation / cost-only | -164.00 | 32 | - | 0 | Evaluation unfinished |
| Recent confirmation / latency-only | -965.10 | 21 | - | 0 | Evaluation unfinished |
| Recent confirmation / combined stress | -1,110.00 | 15 | - | 0 | Evaluation unfinished |
| Long confirmation / baseline | +3,300.90 | 11 | -1,399.82 | 45 | PA activity closure; no payout |
| Long confirmation / cost-only | +982.00 | 19 | - | 0 | Evaluation unfinished |
| Long confirmation / latency-only | -146.50 | 15 | - | 0 | Evaluation unfinished |
| Long confirmation / combined stress | -360.00 | 10 | - | 0 | Evaluation unfinished |
| HGB control / baseline | +4,540.40 | 16 | +2,338.78 | 198 | PA survives observed calendar; hypothetical payout eligible |
| HGB control / cost-only | +4,113.00 | 16 | +178.00 | 162 | PA activity closure; no payout |
| HGB control / latency-only | +3,259.20 | 18 | +1,626.68 | 175 | PA survives observed calendar; hypothetical payout eligible |
| HGB control / combined stress | +927.00 | 24 | - | 0 | Evaluation unfinished |
| Original conformance / baseline | +3,254.00 | 10 | -1,271.14 | 22 | PA survives observed calendar; no payout |
| Original conformance / cost-only | +3,292.00 | 14 | -1,588.50 | 15 | PA activity closure; no payout |
| Original conformance / latency-only | +3,130.20 | 8 | +1,470.00 | 25 | PA survives observed calendar; no payout |
| Original conformance / combined stress | +3,429.00 | 8 | +742.50 | 24 | PA survives observed calendar; no payout |

The original route is a conformance control, not another selection comparator.
Both new candidates fail the baseline-plus-stress full-route gate, both HGB
benefit comparisons and the history-benefit contrast. All 16 books have zero
hard-threshold/MAE violations; that alone is not success. Each new route has one
Evaluation attempt and no resets. The seven unfinished new Evaluation books
each incur six modeled monthly renewals; fee amounts remain unpriced.

Long confirmation passes Evaluation on December 30, 2025, then enters MNQ PA
on December 31. It processes 61 PA dates, makes 45 trades, loses $1,399.82 and
closes for the modeled profit-qualified activity rule on April 1, 2026. Its
last fill is March 25. No payout eligibility occurs. Its baseline PA total is
$3,738.60 below HGB, but those routes have different PA start dates and exposure
lengths (61 versus 115 processed dates). This is a whole-route comparison, not
an isolated MNQ forecasting effect. Every other preregistered PA-dollar contrast
is null because at least one account never enters PA.

## Nomination And Failure Attribution

Each product has 3,747 chronological predecision queries over the 126 dates.
These are overlapping opportunities, not independent samples or filled trades.

| Confirmation | Product | HGB Nominees | Retained | Vetoed |
| --- | --- | ---: | ---: | ---: |
| Recent | NQ | 489 | 281 | 208 |
| Recent | MNQ | 364 | 187 | 177 |
| Long | NQ | 489 | 183 | 306 |
| Long | MNQ | 364 | 117 | 247 |

- Confirmation removes many nominations but does not establish better account
  outcomes. The recent route fails every Evaluation mode; long history passes
  only baseline Evaluation and then loses money in PA. An additional agreeing
  model is not automatically a useful ensemble component.
- Fewer predecision nominees need not imply fewer Evaluation fills: the recent
  baseline makes 38 Evaluation trades versus HGB's 16 because it never exits
  that phase. Exposure and account state change after the first altered trade.
  Do not attribute the result solely to a trade-count cap or unavailable data.
- Capital path remains material. Recent baseline ends with $290.05 above its
  trailing floor and 153 risk-cap skips; recent stress has $281.50 and 152 skips.
  Long stress has $217.50 and 105 skips. The recent baseline's last fill is
  February 2; recent stress stops filling December 22, 2025. These are observed
  capacity restrictions after prior outcomes, not a failed software test.
- Long baseline PA has 25 stop exits and 20 target exits. Its activity closure
  is not a hard liquidation breach, and zero hard breaches cannot rescue the
  negative PA economics. Its 91-minute gross-return confirmation is not the
  stop/target net-payoff objective; V132 shows no benefit from this particular
  fixed conjunction, not that all multi-model combinations must fail.

No inversion, threshold rescue, favorable-mode selection, refit or retry follows
this observation. Future work requires a distinct predeclared information or
economic-objective hypothesis. Reused development dates are not independent
validation. The 48 sealed holdout dates stay closed. Last-tick replay does not
prove bid/ask liquidity or real fills. Current official account/cohort compliance,
after-program-fee profit, actual payout and a verified 50K pass are not claimed.
No operational model, Windows installation, order or schedule was changed.

## Qualification And Evidence

- Focused: 325 passed. Affected regression: 563 passed. Total: 888 unique cases.
- Real-source/adapter preflight, child, supervisor and separate audit: exit 0.
- No full-repository green claim; no new fit or inference.
- Fixed implementation: `a5e3ae4`.
- Public pre-execution design: `bcf6d2dbaa2db36a1e765bfc8edbbf10b5091642`.
- Claim: `cdbb5c34f65640b7ff3d320dae0d85430447ee454256d6d2515bc4122e7746d4`.
- Accounts: `c04ce7cab81aad3da826cee6f6ee09ee1abe1e26c515f8f2a41701b8c379726e`.
- Status: `8955d6b7392cae4b393ca2945500710a04366de2b06a72b9e1c0545eff57d692`.
- Seal: `f5644b14e753b474e8c3581ee7b79804e21b4f5b0f6c14c57d4a0565034ca8a9`.
- Terminal: `170ddf26d98adc0df1b6e2aa70ca3d23203862f360b5e7e380cde6ab16d7bf22`.

Local evidence is in reports/nq_apex_terminal_confirmation_v132 and its execution
directory, with a separate audit receipt. Public documentation excludes market
rows, fitted artifacts, credentials and private source ancestry. The overall
research/Windows goal remains active; this experiment does not complete it.
