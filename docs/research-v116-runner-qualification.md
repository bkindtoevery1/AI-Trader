# V116 Runner Qualification

Completed 2026-09-22 UTC before a market claim. This is software and input
qualification, not trained-candidate performance. The original component
qualification and all predecessor results remain unchanged.

## Verification

- Independent scoped collection: 466 cases, exit 0.
- Focused: all 466 passed, no skips, exit 0.
- Actual-source admission and saved V113 restoration: exit 0, no new fit.
- Full regression: 18,493 passed, 2 failed, 1 skipped, actual exit 1.
- All 363 newly added runner/replay cases passed in focused and full runs.
  Together with the 103 frozen component cases, all 466 V116 cases passed.
- Source and numeric runtime fingerprints were unchanged across each observed
  process. Full-case identities and outcomes were reconciled to the component
  baseline, including the exact two preexisting failure identities and causes.

The two existing failures remain the historical candidate-count versus charged
comparison assertion (4 versus 6), and the missing V88 temporary XML artifact.
The full suite is not green. No test or old result was rewritten to hide them.

Independent tests found an inventory defect: consistently repinning a changed
pytest node ID could pass without matching the corresponding JUnit identity.
The runner now requires exact ordered pytest-to-JUnit identity mapping and
binds the mapper version and module hashes. The six targeted checks and the
final complete runs passed after this correction. No market attempt was made
before the correction or qualification.

Actual admission restored the two saved V113 models and 126 forecast envelopes
without fitting or scanning raw execution pairs. The prepared input identity is
`628f4aa5898aa027f87c25b5d3d58d0bd836e720285f05fa3c32d1e33822c733`.
The original source identity remains
`bb5040a283e9149f6daa3450f2aa5b420313bea468e6891549ea60b5c804b20a`.

Machine-readable qualification:
`reports/nq_apex_cross_product_stack_v116_runner/qualification.json`, SHA256
`c0be121e8ec5046215324a04b2f2266606fe5d944315ff9d8f7fd25e4f29b4c1`.
It binds collection, raw logs, actual PIDs/exits, JUnit, source restoration and
the source-bound review. Passed counts use distinct testcase outcomes, not
JUnit's aggregate counter with additional reporting events.

## Next Execution

The user's latest instruction is to validate with existing Mac data without
waiting for Windows collectors or new market data. The fixed experiment uses
the already admitted historical population, chronological calibration/scoring,
181 raw explicit-contract pairs and 126 scored dates. The 48 sealed holdout
dates stay closed. Historical adaptive reuse is development evidence only.

One exclusive claim will reserve three comparisons, 13,196 to 13,199; eight
scalar fits may learn at most 24 coefficients. The first fold passes through
unchanged. Twelve account books retain costs, slippage, sizing and lifecycle
rules. Partial candidate metrics cannot be opened. Successful process exit,
source/model restoration and independent recorded-account arithmetic are
required before final interpretation. No automatic market retry or rescue tune.

At qualification there are zero new market fits, candidate forecasts, account
replays or charged comparisons. This does not qualify V116 for Windows or live
signals. Windows operations, Telegram, orders, credentials, spending and
schedules are outside this experiment.
