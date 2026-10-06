# V133 Results: Smaller Contracts Do Not Repair The Stressed Route

## Completed Execution

The sole supervised replay completed at 2026-10-06T09:25:48.613872 UTC.
All 181 explicit-contract raw pairs (402,041,614 ticks), 126 scored dates and
12 books finished: four new all-MNQ books and eight exact original/HGB controls.
This is one new execution policy using unchanged fitted HGB own-product
forecasts, not a newly fitted estimator. No fit, inference, label reconstruction,
terminal confirmation, product reselection or support expansion occurred.
Retained unit journals remained hash-bound, not recomputed. Two comparisons
remain charged, bringing the historical total to 13,250.

Child and supervisor exited 0 with source unchanged. The supervisor audit and
separate saved-result audit passed. Three sealed outputs, saved forecasts,
receipts and all account summaries were verified. Direct execution-level sums
matched PnL, trade counts and contract totals for all 24 account-phase
combinations. All required processes are terminal. These checks establish
evidence consistency and arithmetic, not independent numerical/model validation.

## Account Results

All amounts are simulated trading USD after modeled commissions, slippage and
execution effects, before unpriced purchase, renewal and activation fees.
Evaluation and PA start with separate capital: their PnL is not additive
spendable equity. A dash means PA was never entered, not measured zero return.

| Route / Mode | Evaluation PnL | Evaluation Trades | PA PnL | PA Trades | Final State |
| --- | ---: | ---: | ---: | ---: | --- |
| All-MNQ / baseline | +3,059.64 | 39 | +1,461.32 | 179 | PA survives observed calendar; hypothetical payout eligible |
| All-MNQ / cost-only | +618.50 | 58 | - | 0 | Evaluation unfinished |
| All-MNQ / latency-only | +3,294.48 | 48 | +668.00 | 138 | PA activity closure after hypothetical payout eligibility |
| All-MNQ / combined stress | -1,436.00 | 38 | - | 0 | Evaluation unfinished |
| HGB control / baseline | +4,540.40 | 16 | +2,338.78 | 198 | PA survives observed calendar; hypothetical payout eligible |
| HGB control / cost-only | +4,113.00 | 16 | +178.00 | 162 | PA activity closure; no payout |
| HGB control / latency-only | +3,259.20 | 18 | +1,626.68 | 175 | PA survives observed calendar; hypothetical payout eligible |
| HGB control / combined stress | +927.00 | 24 | - | 0 | Evaluation unfinished |
| Original conformance / baseline | +3,254.00 | 10 | -1,271.14 | 22 | PA survives observed calendar; no payout |
| Original conformance / cost-only | +3,292.00 | 14 | -1,588.50 | 15 | PA activity closure; no payout |
| Original conformance / latency-only | +3,130.20 | 8 | +1,470.00 | 25 | PA survives observed calendar; no payout |
| Original conformance / combined stress | +3,429.00 | 8 | +742.50 | 24 | PA survives observed calendar; no payout |

Original is conformance only, not another selection comparator. No route passes
the joint baseline-plus-stress full-route gate. The new policy fails both its
relative PA benefit and categorical full-route improvement gates. All 12 books
have zero hard-threshold/MAE breaches; this alone is not an economic pass.

New baseline passes Evaluation on January 8, 2026 after 22 processed dates,
then enters PA on January 9. It processes 104 PA dates, first qualifies for the
modeled payout on February 24 and deducts a hypothetical $500 withdrawal. This
is not an actual payout. Latency-only passes January 20, enters PA January 21,
processes 95 PA dates and reaches hypothetical $500 payout eligibility February
23, but closes under the activity rule on June 10; its last fill is June 3.
Each new book has one Evaluation attempt and no resets. Baseline/latency each
count one monthly renewal; cost/stress each count six. Fee amounts are unpriced.

Baseline PA is $877.46 below HGB; latency PA is $958.68 below HGB. Their PA
exposures differ (104/95 versus 115 processed dates). Cost/stress PA contrasts
are null because at least one book never enters PA. Product, own forecasts,
support, costs and account trajectory all differ: this is a whole-route policy
comparison, not an isolated contract-size effect or independent samples.

## Failure Attribution

- Smaller granularity does not preserve sufficient stressed capacity. Combined
  stress ends with only $33.50 above its trailing floor, after 38 Evaluation
  fills and 172 risk-cap skips; its last fill is January 27. Cost-only ends
  $45 above its floor after 58 fills and 176 risk-cap skips; last fill February
  10. The account can remain technically alive while unable to fund another
  admissible stop. No missing-data or software-test failure explains this.
- Sizing did adjust: stress used one, two, three and six actual MNQ contracts;
  cost-only used every quantity from one to six. Baseline Evaluation filled
  39 trades at six MNQ each; latency filled 48 at six. Fresh-PA five-contract
  limits and the existing prior-day unlock were preserved. Smaller units do
  not guarantee smaller aggregate risk or create positive net expectancy.
- Baseline had 218 total fills, with 109 stop exits, 108 target exits and one
  time exit. Stress had 23 stops and 15 targets. Do not infer a causal cost
  deduction from final PnL differences: changed fills, capital and phase dates
  create different paths. These descriptive counts are not new selection gates.
- Baseline and latency reach modeled payout eligibility, yet latency later
  loses sufficient capacity/activity to close. Payout eligibility, observed
  survival and robust profitability are separate requirements. A favorable
  diagnostic mode cannot replace failed combined stress.

No quantity increase, threshold rescue, favorable-mode selection, inversion,
refit or retry follows this result. A successor needs a distinct predeclared
information/economic hypothesis rather than relabeling this policy as a pass.
Repeated historical development is not independent validation. The 48 sealed
holdout dates stay closed. Last-tick replay does not establish bid/ask liquidity
or real fills. No current-cohort compliance, after-program-fee profit, actual
payout or verified personal 50K pass is claimed. No operational model, Windows
installation, order, purchase or schedule was changed.

## Qualification And Evidence

- Focused: 492 passed. Affected regression: 624 passed. Total: 1,116 unique cases.
- Final real-source preflight, child, supervisor and separate audit: exit 0.
- An initial read-only preflight found an unrestricted-versus-retained MNQ
  support-check mismatch. It was repaired before market replay with seven
  support tests, preserving the exact previously narrowed forecast support.
  No fit, account outcome or support expansion preceded the fix.
- No full-repository green claim; no new fit or inference.
- Fixed implementation: `61275b6`.
- Public pre-execution design: `313848923f6bc6642476a1695fbc050e6130d951`.
- Claim: `a8d795e91a470fae5b8b43f843b19e6ccbd0940d83f9ccf438892e5f62e0611a`.
- Accounts: `adf571b3e8bb725e6404aacb79d56e33e5ec2e9935cc1937b5223c4aad0110f7`.
- Status: `8f2e47f4c48a6c45bdaa5eefa5565a856c98e177b8cba4bd51698099b60ca21d`.
- Seal: `07d7deba83bd59bc682a9320605bb96968d8d98200269b3c786acb47e54b45a8`.
- Terminal: `0a29893be80e34fe7f9ac902a06984bd0bc929018b41333b08d381ac9658e2cf`.

Local evidence is in reports/nq_apex_micro_whole_route_v133 and its execution
directory, with a separate saved-result audit receipt. Public documentation
excludes market rows, fitted artifacts, credentials and private source ancestry.
The overall research/Windows goal remains active, not completed by this study.
