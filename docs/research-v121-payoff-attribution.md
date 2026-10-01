# V121 Payoff Attribution

As of 2026-10-01, exact committed-envelope recovery and descriptive payoff
decomposition are **complete**. All 252 original distribution hashes matched;
517971 recorded-account checks passed. This is not restored source admission,
a new model, an account replay or an independent performance result.

## Finding

Across both pressure arms and four scenario books, all 4420 PA decisions had
positive contract capacity. One MNQ was the best recorded positive quantity in
every decision, but the cost-stress head's model-implied mean was already
negative in every case. Risk aversion worsened that value; it was not necessary
to explain the frozen minimum-across-heads rejection. These are overlapping,
correlated decision records, not 4420 independent or executed trades.

For the baseline book's 561 PA decisions in each arm:

| One-MNQ Quantity | Equal Print | Volume Weighted |
| --- | ---: | ---: |
| Cost-head modeled mean, median | -$4.0646 | -$4.0913 |
| Cost-head risk penalty, median | $0.3582 | $0.3583 |
| Cost-head CE, median | -$4.4411 | -$4.4875 |
| Highest cost-head modeled mean | -$0.1471 | -$0.1390 |

Medians are separate summaries, not an additive decomposition of one median
trade. These are conditional learned-support expectations, not realized PnL or
known future expectancy. The cost-only scenario stresses commission/slippage;
baseline already includes costs. This analysis does not isolate fee versus
slippage effects or judge whether the original stress assumptions are realistic.

Removing only the risk premium or multiplying this same negative MNQ unit mean
by more positive contracts cannot fix it. The finding agrees with the later
[V122 abstention audit](research-v122-abstention-audit.md), whose cost/label
arithmetic has its own separate audit. A next candidate needs a distinct,
declared cost-adjusted edge hypothesis, not another unexamined entry trigger or
post-outcome deletion of the losing head. No replacement is selected here.

## Purpose

The completed V121 audit found that the cost-only certainty equivalent was
limiting every positive-capacity PA choice. That alone cannot distinguish a
negative model-implied mean from a positive mean outweighed by risk aversion.
The new helper reproduces the recorded four-head CE before computing the mean
and the difference between mean and CE. These quantities describe a learned
distribution over training outcomes, not realized trading profit.

The runner explains the best already-recorded positive quantity, retaining
ties, zero-capacity cases and all four scenario books. It does not change
headroom, contract caps, stress assumptions, thresholds or trade selection.
The original runner still requires both all 252 distribution hashes and the
whole restored-result hash. The new explicit recovery route requires every
complete distribution envelope and recorded probability identity to match,
without claiming that the larger historical source/population object was
restored. Neither route infers source/model admission from synthetic tests.

## Exact Recovery

`tools/recover_nq_apex_payoff_v121.py --run` authenticates the completed receipt,
six exported forests, pressure contexts, original loader inputs, numerical
runtime and research code. It regenerates development-only broad opportunities
through the original read-only minute loader and requires their complete hash
and source snapshot to match. Exact retained event IDs/order supply nine causal
coordinates; retained pressure adds two. Original support, three 42-date folds,
integer outcome support, population bindings and unsupported nulls are retained.
Only after all 252 envelope hashes match does attribution inspect recorded CEs.

The six changed application dependencies are reported and prohibited from
executing during recovery. Fitting is also prohibited. Old admission and full
restore guards remain unchanged. This is explicitly post-outcome content
recovery, not full historical runtime equality, raw-tape reverification or
authority to deploy a model.

Both actual recovery processes exited 0. Independent review found one report
field mislabeled current code hashes as historical hashes. V2 names it
`current_code_sha256`; V1 remains preserved. Repeating the exact no-fit recovery
after this metadata-only correction produced identical envelopes, models,
account-check count and all attribution numbers. There was no model selection.

Final private report: `reports/nq_apex_pressure_payoff_attribution_v121/recovered-audit-v2.json`
SHA256: `5218a87e6f95b9bce5ec754121aed2afb9824f4dafbf3a2e8a6b0d57fa7e4ab6`.

## Verification

Final related tests: 265 passed in 17.47 seconds, exit 0, using the original
V102 numeric interpreter. The broader repository attempt was intentionally
interrupted after 841.05 seconds: 3696 passed, 3 failed, exit 2. It did not finish
the full test census and is **not** a full-repository pass. Two observed failures
are V78/V85 frozen dependencies versus the already-changed `broker.py`; the third
is an existing assertion that current operational-goal wording contains
`Legacy 50K`. Those files/conditions were not repaired or waived by this work.
Independent review
found a quantity-scaling cancellation defect in the new helper: a nonzero mean
could round to zero when very large support values were scaled first. The fix
sums before scaling and uses an exact rational mean only near cancellation;
the reported 1.5-cent synthetic counterexample is now covered. No old model or
utility implementation was changed. Revised runner review found no further
concrete issue; it was a code review, not execution evidence.

## Historical Attempts

Both actual attempts exited 1 before source reconstruction or attribution:

1. Session 80281 stopped at the old V120 failed-attempt runtime comparison.
   Eight unrelated editable-install application files changed since that run.
   The new diagnostic now authenticates the six exports directly against the
   completed V121 inference receipt instead. It does not assert that the full
   historical editable installation is unchanged.
2. Session 83166 stopped at the unchanged original input-admission guard,
   first reporting `src/aitrader/broker.py`. Six declared source dependencies
   differ: broker, CLI, market schedule, reporting, Telegram and Toss client.
   This guard was not bypassed; no audit result file was published.

Read-only Git lookup found the required market-schedule blob at current HEAD.
The five other exact hashes were absent from all available per-path revisions
examined: respectively 4, 12, 6, 2 and 3 revisions, plus HEAD, without rename
following. This is not proof that no external backup exists. Current files and
all unrelated changes remain untouched.

Those failures remain part of the record, but the separate exact-envelope route
above now completes the descriptive question. Do not describe recovered
probabilities as originally stored or as new forecasts. The historical V121
receipt records 13213 trials at that run; the current ledger already includes
V122 and remains **13215**, with zero new charges from this analysis. The sealed
holdout stays closed. V18 signal delivery is independent and unchanged.
