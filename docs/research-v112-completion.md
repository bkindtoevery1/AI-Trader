# V112 Completion

The sole prequential-bias experiment completed at 2026-09-13T17:55:34Z;
its launcher exited 0 one second later (exec90948, PID18384). All ten frozen
source files stayed unchanged. It processed 181 raw contract pairs, 126 scored
dates and eight account books / 1,008 scheduled account-days. Two multioutput
calibration fits learned eight scalars, with no HGB or scaler refit. Two actual
comparisons bring the historical development ledger to 13,187.

## Economic Result

Original NQ Evaluation and four exact original MNQ controls reproduced. The
candidate changed only later-fold MNQ PA forecast bias. It increased filled PA
trades, but worsened PA net trading PnL in every execution mode:

| Mode | Reference PA USD | Candidate PA USD | Difference USD | Candidate fills |
| --- | ---: | ---: | ---: | ---: |
| Baseline | -1,271.14 | -2,086.40 | -815.26 | 31 |
| Cost only | -1,588.50 | -2,368.00 | -779.50 | 20 |
| Latency only | 1,470.00 | -2,230.48 | -3,700.48 | 33 |
| Combined stress | 742.50 | -1,713.00 | -2,455.50 | 43 |

The frozen primary economic gate fails: baseline and stress improvements are
both negative. Baseline and cost-only candidate accounts close for modeled
inactivity on May30; latency-only closes on June10. These are earlier than the
respective controls. Stress is right-censored without inactivity closure, not
a demonstrated PA pass. No new hard-threshold or PA MAE breach occurred.
Absolute-positive PA, full-route and payout gates all fail. Passing unchanged
NQ Evaluation is not evidence that this MNQ calibration helped.

More executions did not resolve profitability. Candidate RISK_CAP_FLAT attempts
number 39/41/42/26 in baseline/cost/latency/stress, compared with 3/6/0/0 for the
reference. These are recorded execution outcomes, not proof of a causal model
or optimizer defect. Aggregate signed forecast correction does not establish
an improved conditional, dynamically sized PA payoff. Do not rescue this result
by changing thresholds, reversing trades, dropping a mode or refitting.

## Verification

The source/restored-forecast audit exited 0 at18:02:44Z (exec39525, PID32963).
It verified 3,242 dependencies, all ten immutable outputs, six fit-stage
receipts and 126 restored forecast envelopes / 3,747 events. It performed no
new fitting or account replay. Separate recorded-account arithmetic findings
and their exact scope are bound in the completion execution-verification report;
they are not independent market replay or independent statistical validation.

Final focused qualification: 957 distinct passes, exit0. Full regression:
16,715 passes, two exact pre-existing failures and one skip, exit1. All593
genuinely new cases pass. The known failures are the old V102 comparison-count
assertion and the missing V88 temporary regression XML. This is not a green
full suite. The two timestamp-bearing KIS testcase aliases are not new tests;
original XML and failure text remain preserved.

Separate accounting independently reconciled 52,757 checks, 541 attempts and
293 executions: 986 represented account-days plus 22 terminal-zero days equal
1,008. No accounting discrepancies were found. Candidate gross PA results are
negative even before commissions and slippage in all four modes; costs are not
the sole explanation. After losses, continuing nominations often cannot fit
inside the depleted account risk budget.

## Boundaries

This is reused historical development, not an independent holdout result or
verified 50K success. The 48 sealed holdout dates remain closed. Trading costs
and execution stresses are included; program fees are unpriced and the user's
Legacy purchase cohort is unverified. Windows operational model, collector
settings, subscriptions, tasks, credentials, orders and Telegram were unchanged.
The research and Windows-operation goals remain active. Any later hypothesis
needs a distinct prior declaration and honest comparison charges.
