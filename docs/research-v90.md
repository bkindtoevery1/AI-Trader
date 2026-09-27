# v90 Implementation State

Status: completed without a main Legacy50K development or numeric Evaluation pass.
Exec72218 finished exit0 at2026-09-07T13:43:20Z. Never restart or rerun it.
No partial performance or holdout observation was exposed.

Previous goal turn classification: progress. It closed v89 internal evidence,
completed the user-requested Replay Lab causal history/panning release and
verified actual LAN assets without changing original human decision records.

## Scope

Read `docs/research-v90-design.md` and `config/nq-apex-shared-effect-v90.json`.
Two product policies test a shared conditional payoff slope with mode-specific
training means. Two counted exact v88 controls retain separate slopes.
Four comparisons are reserved; the current ledger is 13,083.
Actual fits: six new one-output estimators and six four-output controls,
12 estimators and 30 learned heads; 24 derived mode outputs are not new heads.

An adversarial mathematical review confirmed the narrow interpretation:
average-mode predictions are exactly those of v88 under identical weights and
alpha. Only mode-contrast prediction is restricted. There is no fourfold sample
increase or claim of a new nonlinear architecture. Tests must expose negative
transfer when true mode slopes disagree, not merely prove smoother agreement.

The independent source/cost-path review found no consequential defect within
its scope. Non-affine admission, stop and latency effects remain explicit model
limitations. The pure model's 115 synthetic tests passed, including independent
normal-equation/KKT checks, projection identity, negative transfer, strict
training journals, causal prefixes and metadata isolation. No market fits were
used for these checks. The runner's 120 synthetic tests also passed, including
whole-calendar purge, predictions before current tape, once-only accounts,
shared masks, exact source conformance, fatal algebra checks and one-shot claims.
Independent static runner review found no consequential defect in that scope.

Combined focused verification passed 254 tests, including 19 current-state
checks; `<TMP>/ai-trader-v90-focused.xml`. Full regression passed 7,190
tests with no errors, failures or skips; exec87564 is finished exit0. Evidence:
`<TMP>/ai-trader-v90-prefreeze-full.xml`. Closed policy validation and all
477 dependency paths and 181 raw source envelopes were checked without new
labels. At that prefreeze check, no actual-data fit or raw replay had started
and no comparisons were reserved. Software tests are not trading-performance evidence.

Implementation commit: `292ceef`. Frozen at2026-09-07T13:35:43Z, lock SHA256
`ff723baa54d735cdae11f503c48fd9da942acba68a149bc569818a9559e0ccd1`.
Structural preflight passed at13:36:27Z with an80-date opportunity upper bound,
not80 executed dates or a power guarantee. Preflight SHA256:
`4ea7558ce527652df4101b72fa4409fe3eaf4c6c0fe00695b56b24fd621c105d`.
Run claimed at13:36:42Z, marker SHA256:
`9ce7a293211674629ac963d06d429349fbb2f4eb5ddc6ff0c447d5e73a1e7e93`.
Do not start a second execution or modify the477 locked dependencies.
The terminal report now verifies every scheduled fit and source-control check.
Prefreeze full regression XML SHA256:
`4b8caec57d0819eb5e5f57d577f9e10198333cf095113e3472a932b25e3e31bf`.

Parent owns pure model, policy, design and integration. Separate workers own
adversarial synthetic model tests and one-shot runner/synthetic orchestration.
Neither worker may fit actual data, reserve trials, replay ticks or touch live
Replay services, account connections, credentials, orders or frozen evidence.

The completed lifecycle froze only after focused/full regression and design
review, then ran one structural preflight, reserved the entire fixed batch and
evaluated once. Partial performance stayed withheld. This note is not
execution authority; only the frozen lock and stage evidence authorize a run.

## Terminal Result

All181 raw pairs/402,041,614 events completed;126 dates were scored. All21 exact
v88 source/control checks passed. The algebra check compared36 coefficients and
370 predictions: maximum mean prediction deviation2.776e-16 and coefficient
deviation8.327e-17. These identities do not demonstrate predictive improvement.

| Main product | Signal baseline | Signal stress | Account baseline | Account stress | Baseline signal dates/fills |
| --- | ---: | ---: | ---: | ---: | ---: |
| NQ1 | +2374.90 USD | +69.00 USD | +1066.10 USD | -1012.00 USD | 17/21 |
| MNQ-up-to6 | +915.48 USD | -381.00 USD | +915.48 USD | -381.00 USD | 19/23 |

Signal PnL bypasses account risk guards; account PnL includes them. Both include
modeled trading commission/slippage but exclude unverified program fees. NQ
had two risk-cap skips in each mode and executed19 baseline/16 stressed trades.
All eight main account paths remained Evaluation-right-censored, with no PA or
payout and six modeled monthly renewal units each. Never call this a pass simply
because no hard breach occurred. Removing the30-active-date research screen
would not satisfy the missing numeric Evaluation pass or repair negative
stressed account returns.

Every product had185 scored predictions across80 event dates. Shared slopes
selected26 NQ and28 MNQ events. Against exact v88,17/16 selections were added
and one removed per product; path-dependent portfolio differences are not an
independent extra-trade strategy. NQ direct baseline/stress fell754.10/1783USD
versus the control; MNQ baseline rose231.60USD but stress fell1458USD.

All12 mode-contrast MSE comparisons improved against v88. Baseline/cost-only
payoff MSE improved7.0-8.2%, but latency/stress MSE worsened0.8-1.6%; against
prefix means those delayed-mode errors were3.7-4.4% worse. Common-mean prediction
is unchanged, and contrast MSE equals the constant-mean comparator by design.
This supports reduced contrast overfit, not a robust trading or account edge.
The next hypothesis needs genuine predictive information or a defensible
execution-sensitive contrast, not more activity or a rescued cutoff.

Status SHA256 `12a90623cff7c49b15f5988bc96335ca17a803afe6785c9e8353ff86b528307a`.
Result seal SHA256 `8e4483fbb14d5a89a5ca722bccc8c18bd5bf60e7ebe41c027334e4208a289b0a`.
Failure attribution SHA256 `a1144f2502f7d4b8a7cfcdcc4ebcd4f41a4c72fc0fd251f8604a8adadeb266bc`.
Both read-only agent reviews found no discrepancy. The numerical review
independently reconstructed weighted scalers and normal-equation coefficients
for six shared and six control models, checking740 event forecasts/2,960 mode
values. The account review checked2,016 direct and2,016 account days,554 attempts,
480 fills and74 skips. These are internal consistency checks on sealed labels
and persisted journals, not independent raw-tick or strategy validation. No
standalone v90 auditor was persisted; no estimator.fit call or bootstrap
regeneration occurred during closure.

Postresult focused verification passed255 tests. The first full regression
had7,190 passes and one stale v89 prose assertion failure. Correcting that
unfrozen central-ledger assertion did not change the model or result. The final
full regression passed7,191 tests with zero failures/errors/skips in282.472s:
`<TMP>/ai-trader-v90-final-full.xml`, SHA256
`a7517ba9e4087fbd60c7e964e168aaf1555fff3b92ea1a0b8e4e921c608247b0`.
All477 frozen dependencies, source envelopes, environment and sealed result
bytes were reverified before atomic completion publication at14:02:08Z.
Report-consistency audit SHA256:
`5e79d864d052a4a882e4dda6674d4d3b21ec14e7437cbf991f3eaa6d61d39c11`.
Completion audit SHA256:
`77ca2c26c426e1a13761aff20fb156ed72ac46073a62da664b1e1ea53e32c833`.
No backtest or regression execution remains running.
No frozen model edits, new fits, holdout opening, orders or promotion are allowed.
