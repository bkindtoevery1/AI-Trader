# V135: Opportunity-History Whole-Route Results

Completed October6,2026. [Pre-execution design](research-v135-design.md).
Verdict: FAILED development full-route and relative-benefit gates. All four
candidate modes finish Evaluation without a numeric pass; none enters PA.
This is not a hard-breach failure, independent validation or a verified50Kpass.

## Complete Account Results

The candidate uses exact frozen V134 own NQ Evaluation/MNQ PA forecasts, with
no new fits, inference or execution-policy change. The control is exact V130
own-product HGB. Both preserve the original costs, stops, caps, cooldown and
own account transitions. Original conformance controls are not alternatives
selected by outcome. All181raw pairs/402,041,614ticks and126scored dates were
processed;12books include four new and eight exact replayed controls.

Values below are simulated trading PnL after the retained trading costs.
Program purchase/renewal/activation fee prices remain unverified and excluded.

| Candidate Mode | Evaluation USD | Filled Trades | Active Dates | Evaluation Pass | PA Entry |
| --- | ---: | ---: | ---: | --- | --- |
| Baseline | +1254.90 | 21 | 9 | No | No |
| Cost only | +749.00 | 23 | 10 | No | No |
| Latency only | +398.60 | 44 | 24 | No | No |
| Combined stress | -48.00 | 19 | 9 | No | No |

All candidate fills are one actual NQ; total contracts equal filled-trade
counts. Each account has one right-censored Evaluation attempt, one purchase,
six monthly renewal units and no reset or PA activation. All126scored dates
are retained, including inactive dates. There is no hypothetical payout.

| Retained HGB Mode | Evaluation USD | Evaluation Pass | PA USD | PA State |
| --- | ---: | --- | ---: | --- |
| Baseline | +4540.40 | 2025-12-17 | +2338.78 | Survives observed calendar; hypothetical payout eligible |
| Cost only | +4113.00 | 2025-12-17 | +178.00 | Does not survive observed calendar; no payout |
| Latency only | +3259.20 | 2025-12-17 | +1626.68 | Survives observed calendar; hypothetical payout eligible |
| Combined stress | +927.00 | No | Not entered | No PA |

Candidate and HGB both fail the full-route gate, which requires baseline AND
combined-stress success. Candidate-minus-HGB PA differences remain null in
every mode, not zero or negative PA returns: candidate PA exposure is absent.
The candidate's MNQ forecasts were authenticated but never executed in PA.
This run therefore cannot identify an isolated realized MNQ model effect.

## Why Forecast Improvement Did Not Transfer

V134's overlapping selected-opportunity label means are not a feasible sequence
of positions. Here the early executed path raises the trailing floor and then
leaves little headroom for another indivisible NQ. The unchanged half-headroom
risk policy rejects further entries. Positive nominal account PnL does not imply
sufficient distance from the ratcheted floor or achievement of the profit target.

| Mode | Final Headroom USD | RISK_CAP_FLAT Attempts | Last Filled Date | Longest Inactive Scored Run |
| --- | ---: | ---: | --- | ---: |
| Baseline | 331.05 | 295 | 2025-12-29 | 110 |
| Cost only | 254.50 | 290 | 2026-01-12 | 102 |
| Latency only | 240.55 | 232 | 2026-01-27 | 92 |
| Combined stress | 262.50 | 253 | 2025-12-29 | 110 |

There are no hard-threshold breaches or PA MAE violations. This is insufficient
feasible progress while preserving the risk boundary, not a daily fill-count
cap: the unchanged policy already has uncapped daily fills plus exit cooldown.
Simply allowing more maximum contracts cannot resolve zero feasible quantity.
Removing the risk guard would change the question rather than establish an edge.

Baseline reaches a maximum recorded intraday equity of53423.85USD but never
the modeled numeric Evaluation pass; final equity is51254.90USD and floor
50923.85USD. Unrealized excursions, realized profit and account pass are not
interchangeable. These are descriptive path mechanics, not proof that any
particular alternative exit or position policy would succeed.

V133 already showed that switching to smaller MNQ from Evaluation start alone
did not repair robustness. Preserve that negative evidence. A subsequent
preregistered question should address executable risk/exit-path consequences,
not reuse the pooled forecast gain as proof of profitability or silently swap
back the unfavorable component. No successor was selected or tested here.

## Completion And Verification

Frozen local implementation `e79c6dc`. Public design
`4e6622c98dc1ec0ca017f16116537383f234bdb4` on
`codex/research-records-v135` was remotely verified before the sole replay.
Two comparisons were reserved before execution,total13,254 to13,256. Both
remain charged despite failure; no automatic retry or threshold rescue.

720 focused tests passed in three isolated delegated suites: source213,
replay249 and runner258. Parent affected regression655passed,1375unique cases
in total. This is not one combined focused invocation or a full-repository
green claim. Actual runner preflight exec61708 exited0 with no replay/fits.
An earlier source-only diagnostic returned admitted data but its print wrapper
incorrectly called decode on a string; that wrapper exited1. It was not a market
attempt or a scientific change; do not misreport it as a successful CLI run.

Sole exec88512,parent79550,child79566 started10:27:24UTC. The replay completed
10:54:25.109467UTC; observed child terminal10:54:25.523634UTC is exit0 with
source unchanged. Supervisor saved-result audit exited0, observed10:56:26UTC.
Both processes are gone. Three sealed outputs, exact controls, adapted
forecasts and account summaries were verified without refit/inference/raw replay.
No third separate CLI audit was run or claimed.

An additional read-only arithmetic check reconciled24phase records and120
numeric values directly from daily rows: PnL, trades, quantities, processed
days and active days. All1497stored daily rows also satisfy starting balance
plus net PnL equals closing balance and sum of attempt PnL equals daily PnL.
All seven frozen design/code/test pins remain unchanged. This is consistency
evidence, not independent numerical or statistical validation. Retained unit
journal hashes stayed bound; unused training labels were not rebuilt.

| Artifact | SHA-256 |
| --- | --- |
| claim.json | `c53c3e860b2cc60432f328c698117f19659c0b71e9e62449300ad7bdba309def` |
| accounts.json | `65d864e8e63774feab13aa16441e951c9bb098b009cb217832db5875f197317e` |
| status.json | `c072c3e4926ff7c9ba92515508c0d5c2f6f3d95b1e651c8c15c23d8d7141dbec` |
| result_seal.json | `4bb4da455206b9ac2d5ce78554cdce592ffd27300c922a95f2f0080613363668` |
| execution terminal.json | `53a655308dde0016e718e24937f92cc6e7268e3b875d00d5b20cdf6d3468140c` |

All48sealed holdout dates remain closed. No partial outcome release, new
collection, Windows, login, schedule, order, Telegram, purchase or operating
model change. Windows remains an unchangedidle revision615 snapshot, not new
operating proof. Last-tick replay is not bid/ask liquidity or actual fills;
cohort compliance, actual payouts and personal50Kqualification are unverified.
The full research/Windows goal remains active; this account experiment is done.
