# v97 Threshold-Interaction Results

Completed 2026-09-08T02:10:44Z, exec68407exit0. This is completed exploratory
development, not independent validation or a verified50K model. The unchanged
frozen development gates failed. Numerical Evaluation success is reported
separately below rather than hidden behind that aggregate verdict.

## Actual Model Evaluation

Two threshold policies, NQ<=1 and MNQ<=6, used24single-output HGB fits in six
product/fold bundles. All1,536trees,181explicit pairs,402,041,614raw events,
10,970unit labels and126scored dates completed. Ten comparisons include eight
reused controls; the conservative ledger is13,131. No control, scaler or kernel
map was refitted. The48-session holdout remains sealed.

Account trading PnL in USD, after modeled commissions/slippage but before
unpriced program fees. Evaluation and PA are different phases and balances.

| Product / Mode | Evaluation PnL | Numeric Eval | PA PnL | Final Route |
| --- | ---: | --- | ---: | --- |
| NQ baseline | 3157.80 | 2026-04-23 | -174.10 | PA inactivity closure |
| NQ cost-only | 3143.00 | 2026-04-30 | -814.00 | PA inactivity closure |
| NQ latency-only | 3130.20 | 2026-04-17 | -1102.40 | PA inactivity closure |
| NQ combined stress | 1693.00 | Not reached | Not entered | Evaluation censored |
| MNQ baseline | -739.00 | Not reached | Not entered | Evaluation censored |
| MNQ cost-only | -952.00 | Not reached | Not entered | Evaluation censored |
| MNQ latency-only | 2020.98 | Not reached | Not entered | Evaluation censored |
| MNQ combined stress | 69.00 | Not reached | Not entered | Evaluation censored |

NQ baseline Evaluation took92processed dates,12fills on11active dates, starting
2025-12-03. Four monthly renewal units were modeled, but their prices are not
verified. Its PA phase had11fills on6active dates. Combined trade-book profit
2983.70USD is not a withdrawable payout or the final PA balance gain. Across all
40paths, there are3numerical Evaluation passes,3PA entries and0payout paths.

## Failure Attribution

The tree representation increased NQ selected coverage to123events on37dates,
versus30events on13dates for the exact nonlinear control. It did not produce
reliable success across execution modes or the complete account lifecycle.

NQ baseline has39risk-cap skips: only1during Evaluation but38inPA. This is a
new phase-specific capacity bottleneck; closedv96's zero-cap-skip finding must
not be generalized to v97. Stops, sizing and activity rules were not relaxed.
Combined stress remains below the Evaluation target, and the three PA routes
close for inactivity, not a recorded hard-threshold breach. Fees, compliance
and exact raw breach timing are not independently established by this summary.

The guard-free NQ baseline journal has228.50USD profit and0.063Sharpe; cost-only
is-1503USD, with baseline family p=0.882. Those fixed-size diagnostics are not
guarded account balances. MNQ baseline account profit is negative. Both products
lose the frozen all-control MSE hypothesis in all three folds and pooled means.
Removing only the MSE gate would not solve combined-stress or PA failures.

Before v97 results were inspected, a separate review established that global
forecast-MSE dominance is not necessary or sufficient for executable utility.
See `research-execution-vs-forecast-review.md`. That is a future design issue,
not a retrospective exemption or a passed label for v97. No new feature,
threshold, timing, sizing or account-phase route is tested by this report.

## Verification And Limits

Prefreeze full regression passed, with11core hashes unchanged. Independent
source/publication review findings were repaired before freeze; source preflight
reproduced all1,008old rows from reconstructed causal coordinates. Parent
postrun verification rechecked726dependencies,13runtime files, source metadata,
84individual fit receipts and the final seal/claim bindings. No replay was rerun.

The independent saved-tree auditor traversed252new rows and checked29,820mode
values bitwise,39null vectors,218selected vectors,1,008old control rows and64
saved control account/journal comparisons, with no mismatch. This does not
independently reconstruct features, training support, native fitting, raw
account breaches, program fees, statistical confidence or strategy efficacy.

Result status SHA256:
`08eaeef7f4687c1c35f0ab2faa454d37492abdf69daccaa5364c25e4f13e43ad`.
Result seal SHA256:
`399430922dc69ae78cdf666fb0f0ec4fbe970d7833213dea97886def99c3e872`.
Attribution SHA256:
`673d5b30ef5ad17ad4825b7d24f0be5b5b3b1348482d79c8b06ad25b31ddbff8`.
Independent saved prediction audit SHA256:
`fb4584efdf8d758c71e59b88e58da5152d9889cb1e57ecf4293162be571914eb`.

Completion audit SHA256:
`8c81369873fa1fcebb7cfb48c8c38a6fd89b54ea157d06562147db5af0575c84`.
The prefreeze suite passed10,365 cases in428 modules. After result publication,
only derived reports and central metadata changed; all38 affected-module tests
passed. Three earlier metadata failures and their XML reports are retained:
missing run-marker alias, missing terminal-status alias, and a summary prefix.
These are bookkeeping defects, not model-performance failures. No full suite
was rerun solely for these metadata repairs, and frozen code remains unchanged.

The study is closed to retuning or rescue. No orders, purchases, Windows
deployment, Telegram sends or operational model promotion occurred. The broader
research goal remains active; a verified50K pass and operational route are not
achieved by this numerical development result.
