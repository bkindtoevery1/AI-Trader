# V145: Public CPI Whole-Account Results

Completed October 12, 2026. [Frozen design](research-v145-design.md).
Verdict: FAILED development full-route and relative-PA-benefit gates. None of
the four CPI candidate modes passes Evaluation or enters PA. This is a completed
economic failure, not a data/runner failure or a verified personal 50K result.

## Question And Complete Results

V144 adds first-release public CPI level and release age to the fixed V134
opportunity-history HGB. Its small pooled forecast-error improvement was not
account evidence. V145 replaces both own-product forecasts as one fixed route:
NQ in Evaluation, MNQ in PA, versus exact V134 forecasts and saved V135 accounts.
No new fit, inference, threshold, exit, cost or risk-policy change was made.

All 181 original explicit-contract raw pairs were scanned. The same 126 scored
sessions, December 3, 2025 through June 12, 2026, remain in the results, including
inactive dates. Twelve distinct books comprise four new candidates, four exact
V134/V135 controls and four original conformance controls. They are not twelve
independent statistical samples. All eight controls reconcile exactly.

Amounts are simulated trading PnL after the retained trading costs. Unverified
program purchase, renewal and activation fee prices are excluded. Evaluation
PnL is not withdrawable cash, and no actual payout is claimed.

| Mode | CPI Evaluation USD | V134 Evaluation USD | CPI Minus V134 USD | CPI Trades | CPI Active Dates |
| --- | ---: | ---: | ---: | ---: | ---: |
| Baseline | -1211.30 | +1254.90 | -2466.20 | 23 | 9 |
| Cost only | -1332.00 | +749.00 | -2081.00 | 16 | 5 |
| Latency only | -1599.40 | +398.60 | -1998.00 | 24 | 11 |
| Combined stress | -1634.00 | -48.00 | -1586.00 | 17 | 6 |

Neither candidate nor matched V134 control enters PA in any mode. PA PnL
comparisons are therefore null, not zero-return PA observations. The candidate
MNQ forecasts were authenticated but never executed; this cannot isolate a
realized MNQ effect. Every candidate fill is one actual NQ. Each candidate has
one right-censored Evaluation attempt, one purchase, six monthly renewal units,
no reset and no PA activation. There are no candidate hard-threshold breaches
or PA MAE violations, but also no hypothetical payout eligibility.

The original conformance controls below are not the V130 HGB comparator used
in the older V135 experiment and are not alternative candidates selected here.

| Original Conformance Mode | Evaluation USD | Evaluation Pass | PA USD | PA Survival | Payout Eligible |
| --- | ---: | --- | ---: | --- | --- |
| Baseline | +3254.00 | 2026-04-23 | -1271.14 | Yes, observed calendar only | No |
| Cost only | +3292.00 | 2026-04-30 | -1588.50 | No | No |
| Latency only | +3130.20 | 2026-04-17 | +1470.00 | Yes, observed calendar only | No |
| Combined stress | +3429.00 | 2026-04-23 | +742.50 | Yes, observed calendar only | No |

All three roles fail the fixed full-route gate. Baseline AND combined stress
must pass Evaluation, enter and survive PA, earn positive PA trading PnL,
qualify for hypothetical payout and avoid hard/MAE breaches. The diagnostic
cost-only and latency-only modes cannot rescue the primary gate.

## Failure Attribution And Retrospective

| CPI Mode | Final Headroom USD | Risk-Cap-Flat Attempts | Last Filled Date | Longest Inactive Scored Run |
| --- | ---: | ---: | --- | ---: |
| Baseline | 338.35 | 302 | 2025-12-30 | 109 |
| Cost only | 268.50 | 306 | 2025-12-09 | 121 |
| Latency only | 315.25 | 252 | 2026-01-09 | 103 |
| Combined stress | 331.50 | 254 | 2025-12-30 | 109 |

The observed path loses money and leaves insufficient headroom under the
unchanged half-headroom reserve for subsequent indivisible NQ entries. The
baseline ends at 48788.70 USD against a 48450.35 USD trailing floor. Risk-cap
rejection is not a daily trade-count limit: daily fills remain uncapped, subject
to the original cooldown, position and risk rules. Raising maximum quantity
cannot fix a zero feasible quantity. These are descriptive path mechanics,
not proof that weakening the risk guard or changing exits would succeed.

V144 baseline NQ MSE improved about 1.25%, yet this complete account route is
worse than V134 in every execution mode. An aggregate regression loss averages
many overlapping opportunities; a sequential account acts on a subset and its
own changing capacity. Those objectives are not interchangeable. The previous
V135 failure already showed that opportunity-level improvements can leave an
account stranded. V145 explicitly tested, rather than assumed, that transfer.

The CPI experiment also has only 3, 5 and 7 distinct macro releases in its
respective training folds. It does not establish that all public macro data
are useless, nor that a macro feature improves live performance. This exact
recipe receives no promotion or post-result threshold rescue. A subsequent
experiment needs a separately declared economic mechanism, not a favorable
subset of these outcomes. Prior failed micro sizing, exit and utility studies
remain evidence; do not repeat them under a new version label without a change
that addresses their documented failure.

## Completion Evidence

Implementation `27277f9d`; reservation `ad149446`. Public design
`99370f7b9dd3ed79acf218ac7adc83ef70215b3f` was remotely verified before replay.
Two comparisons were reserved before execution, 13,298 to 13,300, and remain
charged. The interrupted V143 reservation is preserved, not retried or refunded.

The sole supervised child started at 03:34:14.790452 UTC. Its complete status
was written at 03:59:56.797597 UTC. Actual child exit is 0, source unchanged is
true, and the parent saved-result audit completed at 04:02:05.506389 UTC.
The terminal exec returned 0; no V145 process remains. Counts-only progress
preceded completion; no partial selection or account outcomes were released.

The saved-result audit verifies three sealed files, frozen inputs and models,
eight exact control books and recomputed account summaries without new raw
replay, fitting or inference. This shares account implementation and is not
independent numerical strategy validation. A separate script, importing no
account/model implementation, additionally reconciles all 1510 stored daily
rows, 2799 attempts and 313 executions using integer arithmetic. Starting cash
plus daily PnL equals closing cash, attempt/execution sums match daily cash,
trade counts and quantities match, and all 24 phase records/120 numeric phase
totals match. All five frozen design/code/test pins remain unchanged.

Affected regression: 283 passed, zero failures/errors/skips, 155.567 seconds.
The initial 35-test run is included, not an additional 35 unique passes. No
full-repository green claim is made. The preceding V144 broader run stopped
with three unrelated failures: old loader manifest binding, the pre-existing
V78 broker hash change and a missing old V123 ledger field. These were not
silently repaired or relaxed for V145. Test fixtures are not strategy evidence.

| Artifact | SHA-256 |
| --- | --- |
| claim.json | `362f468d54de99252218c24140257971c9135566e2d2ce466dc0bf4ec9eaae9b` |
| accounts.json | `314c723489c9e2d11219aad7e9a9a6f382b7045b39420e7fbbec23685e423673` |
| status.json | `9959d9d3a51722f2cb175493b5b0bb761bfbeaa96b3e33de8ade8850219daf5a` |
| result_seal.json | `1fa819475791006dbdd633fc43e4beaf042947437592fdad38e5c61baf347344` |
| execution terminal.json | `7d67c86b528636d451054c30f40cbaf449fc1f92fbb6c950cdf63d5cfc32294a` |
| saved-result audit | `9db3f9be51a9749899d1b11dbae62cdd1412d90838b53171a426715e87422cf2` |
| separate arithmetic audit | `b97f876033b2fa2e8b745118387158aef87066f9f9cbe0d91fab6bafb52dc9d1` |

No Windows connection/action, collector/relay/task change, Telegram message,
order, purchase or credential transfer occurred. The sealed June 29 through
September 2, 2026 holdout remains closed. This is repeatedly observed historical
development, not independent validation. Last ticks do not establish bid/ask
liquidity or actual fills; current official cohort compliance and personal 50K
qualification remain unverified. Research continues under the Mac-only scope;
the full persistent goal is active and has not been marked complete or blocked.
