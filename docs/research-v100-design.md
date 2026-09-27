# v100 Bounded Chronological HGB Tuning

Proposed2026-09-08 after closedv99, before any new market fit or inner score.
This is outcome-informed development of a selection procedure, not independent
validation. Promising families may be retained without rewriting their failed
frozen configurations. This study reuses originalv97 nine features and its
unchanged unit labels, execution and separate NQ<=1/MNQ<=6 Legacy50K accounts.
It does not include thev99 price-path feature or change trading thresholds.

## Hypothesis And Search

Test whether chronological training-only selection of learning rate and L2
regularization improves the economic robustness of the retained v97 HGB family.
The nine-settings grid is learning_rate0.025/0.05/0.1 crossed with L2=1/10/100.
The exact original setting0.05/10 is first; remaining settings use deterministic
sklearn ParameterGrid order. Capacity,64trees/head, depth2,100row minimum leaf,
five-date leaf support and seed20260997 stay fixed. No GA, seed fishing, random
internal validation, early stopping, feature search or candidate-specific mode
selection. One joint setting selects all four payoff heads for each product.

For each original outer training prefix (45/87/129 admitted dates), validate on
its final two disjoint five-date blocks. Training for each inner block is the
complete allowed prefix before ten FULL admitted-calendar purge sessions.
Every training label must resolve before that inner purge starts. Validation
labels must resolve before the original OUTER purge starts. Full input and
journal integrity validation precede initial-capacity filtering. All six outer
population arrays must exactly match the original v94/v97 arrays.

Source-only preflightexec94208 confirmed train support for all12product/inner
combinations. First inner NQ808/MNQ809 events on25dates; second NQ959/MNQ960 on
30dates. Validation has168then142events onfive dates in both products. Later
inner training covers67/72 and109/114dates. This is support evidence, not a fit
or predictive result. Actual fitted leaf support remains checked after fitting.

The implemented adapter's source-only preflightexec88147 also exited0 at
2026-09-08T06:03:49Z: all six outer arrays exactly match original features,
four dollar targets and weights; all12inner training and12validation populations
pass date/label maturity checks. It restored252old complete control envelopes.
See `reports/nq_apex_nested_tuning_v100_prefreeze/source_support.json`.

StandardScaler is refit only on each inner training population with original
equal-feasible-date weights, shared across the nine settings for that split.
Rank settings by squared dollar forecast error: equal event weight within each
date, equal weight across the four modes, then equal weight across all ten
inner validation dates. Exact ties prefer anchor-first grid index. All settings
and both split results are retained. No score can average over only successful
splits. A well-formed leaf-support failure makes that setting unselectable;
malformed data/arithmetic/export errors abort the owned attempt. No supported
setting means abort. A selected outer-refit failure aborts without next-best
fallback or a new seed. The common five-date validation support is bound before
fits, not selected by candidate outcome.

After selection, fit a new scaler and four heads on the full eligible OUTER
training prefix. Its scaler must reproduce the original outer scaler exactly.
The account then scores the next42dates. It does not reset between model folds.
The source-only preflight may authenticate old cached labels; actual selection
receives only labels recomputed from past raw sessions during the claimed run.
No selected setting, inner score or partial outer outcome is exposed before
the entire replay, integrity check and result seal complete.

## Compute And Accounting

At most9settings x2innerblocks x3outerfolds x2products x4heads =432inner native
fits, then24outer fits;18scalers total. Expected support failures can stop one
bundle before all its heads are fitted. Actual started/completed/validated
counts are durably acknowledged, not inferred from this maximum. Inner full
trees are not retained: store setting, model/head hashes, validation predictions,
daily scores and failure records. Full selected outer models are retained.

There are54product/outerfold/setting comparisons and108split evaluations. Record
these separately from the legacy outer ledger's two new learning procedures and
two matched economic comparisons, whose four charges take13138to13142. Neither
that legacy number nor54or108 estimates independent trials. Tuning effort is not
hidden merely because only two learned procedures receive outer outcomes.
Do not run a global historical DSR from this accounting.

Each of181explicit NQ/MNQ raw pairs is read once for the complete batch, verifying
the original raw/window receipts and unit labels. All new forecasts precede
the date's entry tape. The eight new product/mode paths and eight exactv97
control paths share read-only market input but have separate account states.
Reproduce252complete control envelopes and eight exact control account reports.

## Economic Interpretation

Use the unchanged v99 pure account-summary checks through an explicitly named
key adapter, not its feature/model identity. Baseline AND combined stress within
each product determine economic development viability: numerical first-attempt
Evaluation target and no hard-breach/MAE failure. Report cost-only and latency-only
sensitivities, full-calendar same-product differences, PA survival, activity,
renewal units and hypothetical payout separately. Do not add MSE/Sharpe/pvalue
superiority as mandatory profitability gates. The inner MSE chooses estimator
parameters; it is not proof of executable utility or a sustainable payout.

Program fees remain unpriced. A numerical Evaluation pass, PA survival, eligible
hypothetical payout and actual external cashflow are distinct. Prior observations
of the126outer dates informed the research design, so even correct nested code
does not make them fresh independent evidence. Keep the48sealed dates closed.
No orders, new messages, Windows deployment, purchases or schedule changes.
Review, focused/full software regression, separate freeze and exclusive claim
are required before the actual attempt. Do not restart a claimed study or change
its specification after looking at its inner or outer outcomes.

References: [ParameterGrid](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ParameterGrid.html),
[HGB parameters](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html),
and [nested validation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_nested_cross_validation_iris.html).
The generic sklearn examples do not establish trading profitability or remove
the caller's complete-calendar and label-maturity obligations.
