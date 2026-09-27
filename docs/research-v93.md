# v93: Family-Regime Interaction Failure

## Outcome

Completed once at 2026-09-07T18:38:36Z, exec86629 exit0. Neither new product
model passed the frozen development screens or the numeric Legacy50K
Evaluation. There was no PA entry or payout-eligible path in any of the24
account scenarios. Do not deploy, invert, refit or relax this completed version.
Independent terminal consistency auditing is complete with one preserved
nondecisional numerical discrepancy. This is not an all-checks-pass audit.

Implementation: `2d55fb8`; execution checkpoint: `c2a5efb`. Both are local
commits, not pushes. Read `research-v93-design.md` for the immutable design.
Model creation/evaluation remains primary; operational paper is separate.

## What Ran

- Two new NQ/MNQ models with three fixed family-by-regime interactions.
- Exact v92 predictions and causal training-mean controls for each product.
- Six counted policy/product comparisons; cumulative count13,097.
- Six new fold/product Ridge fits, six scalers and24 learned output heads.
- Six existing v92 fits reused without refitting;24 mean outputs derived.
- 181 explicit-contract NQ/MNQ raw pairs,402,041,614 verified raw events.
- 55 warmup dates and126 scored dates in three42-session chronological folds.
- 10,970 complete unit counterfactual labels, not executable portfolio trades.
- 525 frozen dependencies and36 outcome-free fitting-stage receipts.
- All21 predecessor conformance checks passed inside the completed run.

All folds passed the predictor-only family-support and added-rank3 gates.
Both products had126 scored dates with initially affordable opportunities.
Thus this was not an ingestion failure, zero-fit abort or empty evaluation.
Structural feasibility does not prove statistical power or informative features.

## Account Results

USD, modeled commissions and slippage included; unverified program fees excluded.
Guard-free diagnostics are not account returns or evidence that removing risk
protection would pass the challenge. NQ quantity is at most1, MNQ at most6.

| Policy | Guard-Free Base | Account Base | Account Stress | Base Fills / Dates |
| --- | ---: | ---: | ---: | ---: |
| v93 NQ | +6,592.70 | -631.70 | -1,270.00 | 7 / 6 |
| v93 MNQ | -1,457.40 | -1,288.96 | -2,054.00 | 10 / 6 |
| Exact v92 NQ | +3,243.70 | -1,415.50 | -1,153.00 | 5 / 3 |
| Exact v92 MNQ | +2,107.80 | +2,107.80 | +762.00 | 5 / 3 |

Both training-mean controls remained flat under the unchanged all-four-positive
gate. Their zero-action outcomes are valid controls, not missing market data.
Each book has126 daily records; that must not be reported as126 executed trades.

NQ baseline selected49 opportunities on15 dates, compared with v92's35 on8.
It executed33 guard-free trades but only7 risk-managed trades. The account
recorded30 `RISK_CAP_FLAT` attempts. The one-half-headroom reserve is an internal
strategy sizing rule, not an Apex-mandated one-half fraction. Its interaction
with indivisible NQ size and prior account history remains a real execution
constraint of this frozen design. The paths differ in subsequent opportunities,
so subtracting their profits is not an isolated causal effect of one rule.

MNQ selected12 opportunities on6 dates, compared with7 on3 for v92. It lost
under both guard-free and account execution. More selected events did not
improve this product. Cost-only/latency-only scenarios are retained in the
sealed report; they were not discarded in favor of a better-looking mode.

## Predictive Failure

Every policy was scored on the same3,747 opportunities across126 nonempty
event dates for each product, including rejected events. MSE first averages
within date, then weights dates equally. The new model beat both controls on
the prescribed four-mode average in zero of three folds for each product.
All eight pooled product/mode MSEs were higher than exact v92; seven of eight
were higher than the corresponding causal training means. These are observed
paired differences, not a claim of statistically proven inferiority.

NQ's guard-free baseline Sharpe1.403 and stress Sharpe0.316 did not overcome
15 active baseline dates, family-adjusted p0.2354 and negative account PnL.
MNQ failed predictive, profit, coverage and account screens. Dropping MSE,
coverage or p-value requirements would still not create a numeric Evaluation
pass from any of these completed account paths.

## Research Consequences

1. Do not carry the three interactions forward merely because unconstrained
   NQ profit increased. Their stated predictive hypothesis was not supported.
2. Examine the mismatch between unit-R prediction and ex-ante affordable
   executable exposure. Any successor needs a distinct, preregistered objective
   and paired controls, not retrospective removal of v93's losing restrictions.
3. Global MSE is the stated v93 hypothesis gate, not a universal theorem about
   profitable trading policies. A different policy objective may be reasonable
   in a new design, but account feasibility and independent confirmation remain.
4. Reused development is not an independent test. Keep the June29-September2
   48-session holdout closed; do not open it to rescue this failed experiment.

No successor is fitted or reserved by this retrospective. No genetic algorithm,
broker order, data purchase or v93 operational signal is authorized by it.
The separate `research-v94-proposal.md` is a draft, not a frozen experiment.

## Independent Audit

The independent checker verified the source/predictor lineage, paired MSE,
account cash/risk arithmetic, counts, all21 exact reference objects and parent
failure attribution. All525 dependencies and36 fit-stage receipts were rehashed.
Two failed numerical checks describe one shared finding: v92 NQ control's
family-bootstrap p-value is0.29735132433783107 in the frozen result, whereas
exact integer-cent inclusive-tie counting gives0.2978510744627686. Draw102 was
an exact tie excluded by floating-point rounding. The primary v93 probability,
every screen and the no-pass conclusion are unchanged. Preserve both values;
do not edit or replay the frozen result. Future numerical tie handling requires
its own preregistered implementation change, not retrospective rescue.

This internal audit did not independently regenerate raw first crossings or
tickwise equity extrema. Liquidity, exact program fees, operational compliance
and a successful PA lifecycle remain unverified. Its snapshot preceded parent
confirmation of the full regression result; the completion packet now separately
binds the final8259-test XML and observed exit0. Software tests are not strategy
validation.

## Evidence

- Result: `reports/nq_apex_family_regime_v93/status.json`, SHA256
  `7160d99c089bea69ee6a434be876db48ad97266f05ecc16852178674f302265c`.
- Seal: `result_seal.json`, SHA256
  `0862d3b06bdcbe17255bd1319749b0623421da1f1d0bb61a091cb065be862bb4`.
- Attribution: `failure_attribution.json`, SHA256
  `23e01bee2a161f6189694cd8c2800bd04a2d0230553511df891c3ce3b3542778`.
- Independent consistency audit: `report_consistency_audit.json`, SHA256
  `d13abbc5e577fbc73d71b37c57482a107aaa6512c2643a5d882613828cde26f0`.
- Completion: `completion_audit.json`, SHA256
  `70e8786be8e432ef1e50e45b4fc307c22f79aabdb65f3c4dc9c4a9c5b98ee8b6`.
- Focused351, prefreeze full8,259 and postresult full8,259 tests passed.
  Postresult exec19096 exited0; its XML SHA256 is
  `fcc12a2e064025dfc435d312640cf01e21b268916abd4981db5a84e1458cb934`.
- No model replay or research test process remains active. The overall goal
  stays active; there is still no verified Legacy50K pass.

Later v94 prefreeze full regression exposed two omissions in the mutable
central v93 summary: stale account-path totals and a missing versioned progress
entry. They were corrected from sealed v93 evidence, without changing its
result, completion packet or trial count. The unfrozen central evidence test
now derives total new heads from the available schema instead of requiring
v92's redundant field alias. This is a bookkeeping correction, not a new
backtest or a repaired numerical finding.
