# V129 Results: Lower Error Is Not Better Trade Selection

## Execution

The sole supervised development run completed on October 6, 2026 at
04:50:48.095216 UTC. Child 93472 and supervisor 93446 exited 0, source unchanged;
the separate read-only audit also exited 0. It verified 128 sealed files and
recomputed all saved descriptive summaries without refitting. Both run processes
are terminal. This is a forecast comparison, NOT an account backtest or pass.

Nine new pipelines completed: NQ two-part logistic and direct HGB, plus MNQ
two-part logistic, each over three causal training prefixes. There were 36 native
response fits and 12 scalers, no constant heads and no native market warnings.
The exact sealed V126 MNQ HGB comparator was reused without fitting. Five
comparisons remain charged, bringing the historical count to 13,237.

NQ training populations were 1,429 / 2,638 / 3,861 events; MNQ populations were
1,335 / 2,372 / 3,391. All 126 scheduled scoring dates were kept. NQ had 3,708
supported opportunities on 126 dates; MNQ had 3,236 on 124 nonempty dates.
The same twelve causal NQ-derived features were used for both products with
genuine own-product one-contract net-cent targets. The 48 holdout dates remain
closed. Reused development dates do not become independent validation.

## Descriptive Results

Negative percentages mean lower date-equal MSE than the comparator.

| Product | Versus HGB: Baseline | Versus HGB: Stress | Versus Training Mean: Baseline | Versus Training Mean: Stress |
| --- | ---: | ---: | ---: | ---: |
| NQ two-part | -3.70% | -2.67% | +1.90% | +0.31% |
| MNQ two-part | -0.98% | -3.28% | +1.86% | +0.68% |

Two-part MSE improved against HGB in all four modes for both products, but was
worse than the descriptive training-mean anchor in all four. Aggregate error
reduction did not translate into better selected opportunity labels:

| Product / Recipe | All-Four-Positive Opportunities | Dates With Such Opportunities | Baseline Mean USD | Stress Mean USD |
| --- | ---: | ---: | ---: | ---: |
| NQ two-part | 152 | 59 / 126 | -112.78 | -81.45 |
| NQ HGB | 489 | 112 / 126 | +25.88 | -18.37 |
| MNQ two-part | 139 | 65 / 126 | -13.15 | -9.28 |
| MNQ retained HGB | 364 | 105 / 126 | +4.26 | -1.75 |

These are average ONE-contract outcome labels at potentially overlapping
opportunities, including valid unfilled/zero labels. Counts are not account
trades; means are not executable portfolio profit, expected live returns or an
equity curve. Modeled execution costs are in the labels. Dynamic sizing, busy
time, drawdown, Evaluation transitions, PA survival and program fees were not
replayed in this stage. The candidate's selected averages are negative in all
four modes for both products; no profitability improvement is demonstrated.

## Interpretation And Next Boundary

The observed failure signature is poor positive-opportunity selection despite
slightly smaller aggregate error. It is not a missing-data or failed-training
execution. Both baseline selected means are negative in each of the three
folds. The constant conditional payoff magnitudes and linear probability heads
are plausible limitations, not causally established explanations: the complete
recipe differs from HGB in several respects. V76/V89 already explored related
decompositions; do not present this as the first such model.

No formal economic gate was evaluated or relaxed. The economic verdict remains
NOT_EVALUATED, not an invented account failure or success. A later whole-route
replay must use each recipe's own NQ AND MNQ forecasts, allow its own Evaluation
transition, preserve actual costs and integer sizing, and reserve its policies
and contrast separately. It must not use V128's identical-Evaluation assertion
or select only favorable folds. Do not tune, invert or refit these completed
models after seeing this result. No deployment or operational signal change.

## Qualification And Evidence

Final tests: 278 focused passes and 533 affected passes, with 58 overlapping
cases (753 unique). They retain 32 and 24 synthetic/native fixture warnings;
the actual market fits emitted none. Earlier fault-injection tests exposed
missing terminal receipts after setup/log-sync errors, child-reaping races and
non-integer retained folds; these were fixed before market fitting. A later
three-case fixture mismatch omitted the new runtime field; corrected fixtures
pass. No green full-repository regression is claimed.

- Fixed local implementation: `7a45aba`.
- Public pre-execution design: `0351f6c40330d7e44bb086b609f654dba48c8184`.
- Claim SHA-256: `0d7e7394b912756e3904ba34bb1c17c49cda23fc37d08952dfc337f6650a7f51`.
- Status SHA-256: `4798ac8e6190979685d68c69a25611b2eb0ac5323178fe1ad11e6379e3ab7653`.
- Result seal SHA-256: `d38021d73907ef4263fca973a172343f75c431a1b24578c491b09aa8b308ddfe`.
- Supervisor terminal SHA-256: `978e5b452135cfb34cfa946a6afbe39be5f66115432a6b9a550b20c47e5e0527`.

The initial reservation's manually minute-rounded 04:48:00Z was not an exact
clock observation. The actual reservation is bounded by the observed 04:47:43Z
clock and 04:48:33.352918Z parent-start receipt. Preserve the original claim;
this metadata erratum does not change fits, charges, chronology or outcomes.

Local evidence: reports/nq_apex_two_part_v129 and its execution directory.
The audit authenticates saved lineage and recomputes arithmetic; it is not an
independent raw-tick or numerical-model replication. No raw data, fitted model,
private code ancestry or secrets are included in the public documentation.
