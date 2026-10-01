# V121 Payoff Attribution

As of 2026-10-01, the descriptive analysis code is implemented and tested,
but historical decomposition is **not complete**. No new model, account replay,
alternative policy or independent performance result was produced.

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
Before any attribution, all 252 reconstructed arm-date distribution hashes,
the whole restored-result hash and each recorded probability identity must
match the completed V121 evidence. No source or model admission is inferred
from a passing synthetic test.

## Verification

Final related tests: 242 passed in 15.59 seconds, exit 0, using the original
V102 numeric interpreter. This is not a full-repository pass. Independent review
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

Next work is an isolated, reproducible source reconstruction or an explicitly
reviewed reconstruction method authenticating the necessary historical inputs
and exact original predictions. Do not silently weaken existing admission,
pretend newly inferred probabilities were stored, or infer an economic cause
from the incomplete attempt. The 13,213-trial total and sealed holdout are
unchanged. V18 signal delivery is independent of this analysis.
