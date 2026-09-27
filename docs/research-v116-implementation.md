# V116 Component And Source Verification

Completed 2026-09-22. This is implementation progress, not a fitted market model
or a trading-performance result. The economic runner is not implemented yet.

## Implemented Model

V116 learns a constrained combination of original prior-outer-OOS MNQ and NQ
forecasts. It keeps original MNQ reference-dollar targets, date-equal weights,
ten full-session purge and label-maturity checks. It does not refit original
HGBs, add raw features, invert signals or select a penalty from a grid.

Missing NQ forecasts contribute no foreign-score correction, while retaining the
MNQ row and its original target weight. Original model vintages, event identity,
availability and independent convex KKT checks are enforced. The first fold is
unchanged original MNQ; only the two later folds may learn calibrations after a
separate actual-market claim. See `research-v116-design.md` for the fixed design.

## Actual Source Admission

The source admission process completed with exit 0 and unchanged component
bytes. It authenticated 3,067 original source dependencies, restored six original
source models/forecasts and both saved V113 controls without refitting them.

| Calibration Fold | Dates | MNQ Events | Available NQ Forecasts | Missing NQ |
| --- | ---: | ---: | ---: | ---: |
| 2 | 32 | 932 | 932 | 0 |
| 3 | 74 | 2,161 | 2,155 | 6 |

These expanding calibration populations overlap; their sum is not a count of
independent observations. All four added forecast columns vary in both folds,
so the candidate is not structurally redundant due to constant inputs. This is
not evidence of conditional predictive value or improved trading economics.

## Software Verification

- Focused: 400 passed, including all 103 new V116 cases; actual exit 0.
- Full: 18,130 passed, 2 failed, 1 skipped; actual exit 1, not a green suite.
- The 103 new cases also passed in the full run. Source and parent-runtime
  fingerprints remained unchanged throughout all three observed checks.
- The two failures match the preceding full-run failure identities and causes:
  historical candidate-count versus comparison-charge assertion (4 versus 6),
  and the missing V88 `<TMP>/ai-trader-replay-wait-regression.xml` artifact.
  Neither old evidence nor old tests were rewritten to conceal these failures.
- Static independent design/implementation review found no remaining actionable
  issues. Independently authored tests caught the single-observation foreign
  variance validation defect, which was fixed before the final qualification.

The machine-readable authority is
`reports/nq_apex_cross_product_stack_v116_implementation/component-evidence.json`.
It binds the actual child exits, logs, JUnit cases, source admission, component
hashes and review. JUnit's suite counter includes extra reporting events;
passed/failed/skipped counts here come from individual testcase outcomes.

## Remaining Work And Boundaries

Implement and qualify the separate economic runner, make one exclusive claim,
fit the two later-fold calibrators and replay the declared three arms. Verify
eight exact original/V113 controls and four unchanged candidate Evaluation
prefixes. Compare PA net in both baseline and combined stress, with no added
breach or earlier inactivity; absolute PA/full-route/payout success is separate.

Actual V116 market fits, candidate forecasts, account replays and new charged
comparisons are all zero. The ledger remains 13,196; three additional comparisons
are planned only on a genuine claim. No V116 market-output directory or claim
exists. Historical reuse remains development research, not independent evidence.
All 48 sealed holdout dates remain closed. No Windows, Telegram, orders,
credentials, purchases, schedules or frozen operational model were changed.
