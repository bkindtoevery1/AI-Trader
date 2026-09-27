# V109 Completion

Completed2026-09-13T04:08:26Z, independently audited after terminal publication.
This was a real development training/replay, not a software-test-only cycle:
12 estimator fits, zero scaler fits,181 explicit-contract NQ/MNQ pairs,
126 scored dates and eight account paths. Two charged comparisons remain in
the cumulative13179 ledger. No integrity or cash-accounting discrepancy found.

## Economics

PA trading net USD includes modeled commissions and fill slippage. Program,
subscription and activation fees remain unpriced; Evaluation profit is not PA cash.

| Mode | V107 Control | V109 Guarded Target | Difference | Control/New Fills |
| --- | ---: | ---: | ---: | ---: |
| Baseline | -1271.14 | -1299.82 | -28.68 | 22/22 |
| Cost only | -1588.50 | -1620.00 | -31.50 | 15/14 |
| Latency only | 1470.00 | 1320.40 | -149.60 | 25/23 |
| Combined stress | 742.50 | 630.00 | -112.50 | 24/22 |

The frozen relative-benefit gate fails. Neither arm has positive PA net in both
primary modes or passes the full-route gate. No payout eligibility or withdrawal
occurs. Hard breaches and PA MAE violations are zero. Numerical Evaluation
passes are unchanged from the control, in April after four monthly renewals;
this is not a quick pass or fee-adjusted success.

## Failure Attribution

Zeroing guard-inadmissible training payoffs did not improve executable selection.
Baseline shares20 fills with the control, removes two and adds two. Five shared
fills have changed quantities, but their entry/exit prices and exit reasons are
unchanged. Different nominations change account cash and later permitted sizing;
do not attribute quantities directly to prediction magnitude. Its cents delta is
-8038(shared)-4714(removed control)+9884(added candidate)=-2868.
Stress removes four and adds two fills; shared executions and quantities do not
change, yielding-11250cents. This is not a missing-data or zero-trade failure.

Baseline and cost-only candidate PA paths close June3 under the frozen modeled
activity rule: at least two PA days with net >=$50 in30 calendar days. The failed
May5..June3 window has just one such candidate day, May18. Baseline control has
three and cost control two. Baseline candidate and control both last filled May26;
the difference is qualifying-profit days, not merely days since last fill.
This describes the frozen model, not newly verified official Apex rules. Other
surviving paths are right-censored by the observed calendar, not permanent survival.

## Boundaries

The48 sealed historical holdout dates remain closed. This outcome-informed
development experiment is not independent validation or a confirmed50K pass.
Do not select the positive stress mode, invert, retune, restart or promote this
attempt. A future substantive hypothesis needs its own explicit freeze and
comparison accounting; no successor is created by this closure.

The unchanged fixed V102 model remains the operational candidate, not V109.
Its receipt-owner software passed291 focused cases; full regression has15368
passes, two exactly unchanged failures and23 skips. All125 new cases pass.
The Windows launcher, authentic source bootstrap, installation and complete
paper-to-Mac signal remain unfinished. Both full user goals stay active.

Evidence: reports/nq_apex_guarded_target_v109_execution/verification.json,
diagnostic.json and activity_diagnostic.json. The immutable status/seal remain
under reports/nq_apex_guarded_target_v109/; full market results are not added to git.

Final metadata checks:20 passes and the same two known failures across22 cases;
latest V109 status/seal/attribution and auxiliary ledger bindings pass. All3100
frozen dependencies match after documentation edits. The automation was updated
through the app and read back exactly, preserving cadence, target and preferences.
Its old live-process instructions were replaced by this terminal checkpoint.
See reports/nq_apex_guarded_target_v109_execution/closeout.json and archived XML.
