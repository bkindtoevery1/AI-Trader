# V121 Results And Retrospective

Completed2026-09-27. Verdict: **FAILED_ALL_PA_ABSTENTION**. Both pressure
candidates failed the preregistered economic benefit and full account-route
gates. This is a completed development result, not an independent validation,
confirmed50K pass, official account approval or deployment instruction.

## Why This Version Exists

V120 fitted six forests with384trees but aborted before account replay because
equivalent float/integer cent targets were compared as different JSON bytes.
V121 repaired only that exact-value integrity comparison and restored the same
models without fitting, retuning or changing the study. The two candidates
compare equally weighted tick direction with actual trade-size-weighted pressure
over a causal predecision minute. Original V120 failure evidence stays unchanged.

The sole replay ran12:09:03Z-13:28:09Z, actual exit0. The postrun verifier also
exited0; completion verified517971 recorded-account arithmetic checks. Source
and parent/selected-child runtimes remained unchanged. All181 explicit-contract
pairs were scanned and126 dates scored. There are8new books and8unchanged
controls. No new fit or comparison was charged; four original comparisons remain
reserved and the historical effective total stays13213. The sealed48-date holdout
was not opened. No partial economic results were exposed before completion.

## Economic Result

The following outcomes are identical for both new candidates. Evaluation is the
retained original policy's exact prefix, not a pressure-feature improvement.

| Scenario | Evaluation Trading PnL USD | Evaluation Fills | PA Trading PnL USD | PA Fills | Final Status |
| --- | ---: | ---: | ---: | ---: | --- |
| Baseline | 3254.00 | 10 | 0.00 | 0 | PA inactivity closure |
| Cost only | 3292.00 | 14 | 0.00 | 0 | PA inactivity closure |
| Latency only | 3130.20 | 8 | 0.00 | 0 | PA inactivity closure |
| Combined stress | 3429.00 | 8 | 0.00 | 0 | PA inactivity closure |

These are trading results after modeled execution costs, before unpriced program
fees. All8new books had numerical Evaluation passes, no hard-threshold breach
and no PA MAE violation, but none traded in PA, survived the modeled inactivity
rule or became payout eligible. Avoid treating zero PA loss from zero activity
as successful risk management or a full-route pass.

Each candidate made2210 PA quantity decisions across four scenarios:2210 chose
flat despite positive permitted capacity, and zero were zero-capacity cases.
Thus no new fills were lost to execution after a positive choice. Those repeated
decisions are not2210 independent observations. Actual trade-size weighting did
not improve PA PnL over equal weighting in any scenario. Relative to V119 it was
worse by135.96USD baseline and72.00USD cost-only, better by65.54USD latency-only
and68.50USD stress only because it stayed flat. Neither primary contrast passed.

## Failure Attribution And Next Research Boundary

The observed failure is continued flat selection under the unchanged quantity/
payoff utility, not missing source rows, unfilled positive nominations or a
position-capacity ceiling. This experiment does not establish that volume is
universally useless: it rejects this specific pressure representation and learner
under the declared account objective. Numerical Evaluation success cannot be
credited to the new features because those prefixes are inherited unchanged.

No contract increase can rescue an already-flat choice without changing the
decision rule. Do not force minimum activity, delete the stress head or repeatedly
tune thresholds on these now-observed dates. Before another model trial, audit
whether the existing payoff target/support and candidate geometry systematically
make every feasible PA quantity unattractive, using preserved evidence rather
than reopening the holdout or running another superficially different feature
model. That is a proposed diagnostic, not a new approved experiment or result.

## Software And Evidence

Pre-execution focused qualification:1138 unique passes,0failures,0skips,exit0.
Full regression:20844 unique passes,2predeclared inherited failures,1skip,
actual exit1. The full suite was not green. These are V121 qualification counts,
not the later V102 runtime tests. Passing tests alone did not establish economic
success or independent replay reconstruction.

- Status SHA256:061778cf444b0dab52b9d4c7e3ae3bbabcc64fb306ef144d08c0dd7bb30a3194
- Result seal SHA256:8861bf9c849339e7b7aab0594d7665653ea873646ba3ef99f575591517917a26
- Completion SHA256:6d6cbc7bccf8d62648d7cfa1bfeba98b2eea75dcb991a811323aa9f7ba8092c5
- Local completion:reports/nq_apex_tick_pressure_v121_execution/execution-verification.json

These hashes locate local private evidence; publishing this document does not
publish or back up raw prices, fitted artifacts or detailed account records.
The arithmetic audit is not independent raw-tape reconstruction, statistical
validation or verification of the user's exact account cohort/fee schedule.

See [design](research-v121-design.md), [frozen execution policy](research-v121-execution.md)
and [preserved V120 technical failure](research-v120-results.md).
