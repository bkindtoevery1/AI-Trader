# v97 Proposal: Bounded Threshold-Interaction Dollar Models

Status: COMPLETED_FAILED_DEVELOPMENT_WITH_NUMERIC_EVALUATION_PASSES. Pure model,
comparator, paired diagnostics, policy and chronological runner are implemented.
Independent runner review and parent integration verification are complete;
the execution lock75059431... freezes726dependencies and13installed HGB files.
Fresh-feature preflight verified1008old rows before new fitting. Claim914e7095...
reserved10comparisons at2026-09-08T01:46:08Z, cumulative13131. Exec68407 exited0
at02:10:44Z. Only completed, authenticated outcomes were inspected. NQ reaches
numerical Evaluation in three modes but fails combinedstress and the PA route;
MNQ does not reachEvaluation. See `research-v97.md`; no verified pass exists.
v96 remains closed, with its failed
result, six fits and eight comparisons preserved. This is outcome-informed
development planning, not an independently validated finding.

## Question

v94 linear and v95/v96 smooth RBF dollar forecasts did not beat causal means.
v96 changes against linear forecasts were tiny and left baseline executed
coverage sparse. Test whether a bounded piecewise-threshold model can capture
regime interactions missed by those representations, on the SAME nine causal
features, feasible-dollar labels, scalers, date weights and event population.
This changes representation and regularization jointly; it is not a clean
capacity-matched isolation of thresholds. Failure may instead reflect absent
information, so no improved outcome is promised.

Boosting is NOT new to this research: v75 shallow boosting failed on the old
opening/EOD25K setup, and v80's35th-percentile boosting on30opening echo-state
features stayed flat on all181days. See `research-v75.md` and `research-v80.md`.
The new question is its application to the nine-feature intraday feasible-dollar
population with four cost/timing objectives, not a claim that a previously
untried learner will solve the problem. Those failures remain counted; their
models and thresholds are not retuned or renamed as v97.

## Proposed Single Configuration

Use installed scikit-learn1.9.0 `HistGradientBoostingRegressor`, independently
per product and execution mode, with exactly one fixed configuration:

- loss squared_error, learning_rate0.05, max_iter64, max_depth2,
  max_leaf_nodes4, min_samples_leaf100, l2_regularization10.0, max_bins64.
- max_features1.0, categorical_features=None, monotonic_cst=None,
  interaction_cst=None, quantile=None, warm_start=False, random_state20260997.
- early_stopping=False, validation_fraction=None; no validation arrays,
  random holdout, score callback, trial grid or training-progress selection.
- Retain exact authenticated v94 standardization and native finite inputs.
  All nine coordinates remain numeric; no learned missing-value fallback.
- Retain every original per-date sample weight after feasibility filtering,
  without renormalization: changing its scale changes the effective L2 penalty.
  Record and verify its sum, target hashes and complete matured prefix.
- Require each product/mode fitted population to have at most200,000rows;
  abort before any fit if exceeded. This avoids the installed estimator's
  larger-population weighted bin subsampling, not an outcome validation split.

The small depth, leaf count and fixed iteration budget constrain capacity;
they are heuristics, not optimized choices or a statistical power guarantee.
Overlapping events are not independent samples. After each fit, require every
occupied terminal leaf in every tree to include at least five distinct
training dates. Route only that product/mode's exact feasible positive-weight
fitted rows, excluding all infeasible, purged, immature and scoring rows.
Record each leaf's row count, distinct dates and original weight mass. Five
dates are a support heuristic, not five independent or equally weighted samples.
Root-only trees must satisfy the same support requirement. Fail the entire
claimed attempt if unsupported; no leaf replacement, pruning, parameter
relaxation or fallback fit. Synthetic tests must establish routing correctness
and account for valid constant/no-split trees before any real-data fit.

Six product/fold fitted objects contain24single-output estimator fits and
24learned output heads, exactly1,536trees on successful completion. Each
estimator must report64iterations with one tree per iteration, including any
constant trees; preserve acknowledged partial counts if an attempt aborts.
Do not report this as only six
underlying estimator fits. No new scaler, kernel map or control fit. Reuse
exact v96 nonlinear, v94 linear-dollar, matched-R and causal-mean policies:
two new main policies plus eight counted controls, ten comparisons. A future
one-shot claim would raise13,121 to13,131; nothing is reserved by this proposal.

## Chronology, Evidence And Gates

Preserve181raw pairs,55warmup/126scored dates, three42-session folds, ten
full-calendar purge sessions, full matured training prefixes and causal
prediction-before-current-tape order. Preserve continuous NQ<=1/MNQ<=6 Legacy
50K account execution, stops, mean targets, cooldown, four execution modes,
costs and separate Evaluation/PA/payout criteria. No reset or risk relaxation.

For prediction loss, exclude events with q_ref=0 separately per product/mode,
average errors within each nonempty date, and weight those date means equally.
Keep the executable rule requiring all four own forecasts strictly positive.
Require same-date paired dollar-error superiority over ALL four exact controls
in the same two of three folds, plus pooled average/baseline/stress superiority,
in addition to unchanged practical/account screens. All ten policies enter the
fixed family bootstrap,2,000samples/10date blocks/seed20261997, with exact-cent
arithmetic and inclusive ties inherited from the corrected v94 design. Global historical
DSR remains unavailable. Controls cannot be promoted as new discoveries.

Before new fitting, reproduce all1,008old v96 prediction rows, routes and
masks exactly. After replay, verify the unchanged control journals, labels,
prediction identities and fit receipts. Preserve old canonical float layouts and operation shapes;
never use tolerance to decide executable signals. Before freezing, synthetic
nontrivial-float, threshold-equality and serialization tests must show how new
tree state can be recorded/restored without a semantic change. Any private
scikit-learn node representation used for audit needs a pinned runtime and
closed node schema; do not assume shrinkage must be applied twice.

Independent read-only review by Pascal found no fundamental design blocker
and required the explicit population, weight, binning, iteration, count and
reference-parity clarifications above. The review is not a scientific pass.
Finish v96 completion evidence/full regression first, then implement and test
a separate policy/model/runner/lock before
source support or actual fitting. Preserve the sealed48sessions2026-06-29
through2026-09-02, no partial outcome inspection or optional stopping, and
no rescue rerun. No genetic algorithms, orders, purchases, secrets, Windows
deployment or paper-model promotion.

API scope checked against installed1.9.0 and the official
[HistGradientBoostingRegressor documentation](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html).
Its early-stopping defaults can enable an internal validation split; the
explicit disabled setting above prevents that workflow. Depth/leaf/bins and
L2 settings constrain the estimator but do not establish predictive validity.

## Pure Implementation Checkpoint

The pure module is `tools/nq_apex_threshold_exposure_v97.py`; comparator
restoration is `tools/nq_apex_threshold_reference_v97.py`. Pascal implemented
the model and231 synthetic tests. Poincare added92 adversarial comparator
tests to the parent's57 tests, with no concrete comparator defect identified.
Parent combined focused verification passed388 tests, including eight existing
account/closed-v96 evidence checks. Full regression passed9,893 tests, zero
failures/errors/skips,425.236seconds (exec32799exit0). Ten captured hashes
remained unchanged during the test run. Separate model review found no
substantive defect within its pure-code scope. These are software tests, not
new market trials, validation sessions or evidence of investment performance.

An authenticated, read-only check using OLD v96 saved coordinates reproduced
all1,008prediction rows,29,820feasible vectors and156null vectors with zero
exact prediction or selection mismatches. It did not reconstruct features
from source inputs, fit a candidate, replay accounts or inspect the holdout.
See `reports/nq_apex_threshold_exposure_v97/reference_coordinate_precheck.json`.
The future runner must repeat exact old-row comparison on reconstructed causal
features; this narrower check cannot replace that prefit requirement.

The callback `on_stage(stage, mode)` emits estimator_started,
estimator_completed and model_completed for each of four modes. Thus72
mode-stage receipts acknowledge24validated heads, not six completed bundles.
The runner must separately persist each bundle's start and successful return,
record partial acknowledgments on failure, and never retry a claimed attempt.
It must also freshly rehash installed library dependencies instead of trusting
the pure module's once-per-process runtime cache. External reference-container
authentication and immutable result publication remain runner responsibilities.

At the pure checkpoint, the next task was the policy/runner and five-kind paired-loss
aggregation. Require eight unchanged control policies across four account and
direct execution modes, exact saved labels/receipts/windows, and all-four-control
superiority before any development shortlist. That checkpoint had no actual-data
fit, source-support inspection, claim, promotion or performance result. The header
records the newer execution state without rewriting the pure checkpoint evidence.

The pure checkpoint report is
`reports/nq_apex_threshold_exposure_v97/pure_implementation_verification.json`,
SHA256 `586986620486c92b510b966f28267e8c3c20c0c25efd0f5877a1c5cd2b48b7b9`.
It predates the subsequent runner/policy and five-kind diagnostics work
dispatched separately to Pascal and Poincare. Their future code requires its
own focused/full integration verification and review; the9,893-test result
does not cover those additions. No actual-data work is authorized by a test pass.
