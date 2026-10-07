# V142 Component Checkpoint

October 7, 2026 UTC. This is an implementation checkpoint, not a completed
market experiment, economic pass or operational deployment. The fixed
[design](research-v142-design.md) follows the complete failed V141 result and
explicitly retains earlier failed risk-normalized Ridge precedents.

## Implemented

The pure learner reuses V141's fixed lambda-one SVD Ridge, eighteen inputs,
original date weights and native fit journal. It validates integer-cent cash
targets before converting them to own-product initial-stop risk units. Training
scalers see only the supplied mature prefix. Prediction multiplies the R
forecast by that query's known original stop risk and returns unrounded cents.
It does not clip losses, reprice costs, select quantity or refit at prediction.

The separate geometry binder authenticates every original completed anchor and
joins its stop to the exact training population and query support. It verifies
caller-supplied event/context content pins, complete calendar and ordered event
identities. Outcome cash, delayed fills, account capacity and realized loss do
not determine the denominator. Source admission is inherited, not recreated.

These components do not modify V141 or any other frozen implementation. The
old journal cannot directly persist the new fitted wrapper; complete model
persistence, saved V141 comparators, forecast diagnostics and the account
runner still need V142-specific integration and qualification before fitting.

## Verification

The combined five-file affected suite exited zero: 365 passed, no failures,
errors or skips, in 30.07 seconds. It includes the two V142 components and
V141 learner, V139 pipeline and V140 population regressions. JUnit:
`reports/nq_apex_v142_component_qualification_20261007/affected-v1.xml`, SHA-256
`8707739041a543f6fb547da20151484f2a80e1a8f6d699b620cd5e7edbbd6b2e`.
The 56 retained scaler warnings arise from invented constant-column fixtures.
This is an affected-component pass, not a green whole-repository test run.

Checks include independent weighted normal equations, constant-risk equivalence
to V141, variable-risk differences, exact product conversion, unclipped gap
losses, empty queries, input isolation, invalid types/numerics, fit/warning
journaling and fail-closed causal support joins. A read-only peer review of the
geometry/model interface found no concrete defect. Synthetic results are not
strategy evidence.

The actual-source no-fit probe (session16308) terminated with exit1 at final
report publication: the inline harness supplied a relative output path to the
existing journal, which requires an absolute native path. Its source/binding
checks had reached publication, but no qualification JSON was written. The empty
attempt directory is retained. This is a harness publication failure, not an
economic failure or an admissible durable geometry qualification. It performed
no candidate fit, new label extraction, raw replay or saved V141 model restoration.
Do not count it as a completed source-only preflight. Before another probe, bind
the destination to the existing absolute project root and test that publication
path; rerunning the expensive source chain without that fix is not useful.

## Remaining Work

Repair and qualify the probe publication, then qualify the integrated pipeline
and restoration against exact existing V141
forecast/model evidence and V140 cash labels. Publish all 252 product/date
forecast sets before scoring, retain the unchanged four account books and full
economic gates, and reserve the nine declared comparisons before any market
fit. No V142 comparisons are reserved now; the total remains 13,284. The 48
sealed holdout dates stay closed. V63/V92 operation, Windows restrictions,
Telegram delivery and order prohibition are unchanged by this research.
