# V124 Results: Cost-Directed Splits Did Not Resolve PA Abstention

Completed October 1, 2026. Verdict: **FAILED_ALL_PA_ABSTENTION**.
The sole market run, observed no-fit verification and separate completed-result
audit finished successfully. That is execution integrity, not model success.

## Design And Scope

V124 changed only the forest split target from joint four-mode squared error
to cost-only payoff. It retained V123's twelve inputs, date weights, three causal
training prefixes, ten-session purges, fixed shallow forests, full joint outcome
masses, four-mode quantity decision and original V119 account/risk rules.
The exact four completed V123 books were retained controls, not new independent
samples. Three fits, 192 trees and four new account books completed.

All 181 explicit-contract raw pairs and 402,041,614 recorded events were scanned;
126 chronological dates were scored. The 48-date sealed holdout stayed closed.
Two comparisons remain charged, cumulative 13,219, regardless of failure.
No retry, refit, threshold rescue, mode removal or live deployment followed.

## Economics

Simulated USD after modeled trading commissions/slippage, before unpriced
subscription/activation fees. Evaluation and PA are separate account phases.

| Mode | Inherited Evaluation PnL | PA PnL | PA Trades | PA Choices | Outcome |
| --- | ---: | ---: | ---: | ---: | --- |
| Baseline | 3,254.00 | 0.00 | 0 | 561 | Inactivity closure |
| Cost only | 3,292.00 | 0.00 | 0 | 510 | Inactivity closure |
| Latency only | 3,130.20 | 0.00 | 0 | 578 | Inactivity closure |
| Combined stress | 3,429.00 | 0.00 | 0 | 561 | Inactivity closure |

All 2,210 PA decisions had positive capacity but selected flat. There were no
hard breaches, MAE violations or payout eligibility. The inherited Evaluation
prefixes pass numerically but are not V124 learning gains; each journey includes
four modeled renewal units. PA PnL differences from V123 are zero in all modes.
Relative benefit, absolute positive PA and modeled full-route gates all fail.

## Failure Attribution

The 2,210 scenario decisions represent 769 distinct market opportunities, not
2,210 independent samples. All have 250,000 cents of headroom and capacity for
five MNQ. One contract is always best among positive quantities but still worse
than flat under the unchanged worst-head criterion.

Unlike V123, cost-only is no longer the sole limiting head: it limits 2,154
decisions, while combined stress limits 56. Every limiting head already has a
negative model-implied mean, before its risk penalty. Some cost-only CEs become
positive, but another head still rejects the trade. Raising capacity or reducing
the risk penalty alone does not address the observed negative-mean obstacle.
This is a description of this fitted model, not proof of actual negative edge
or authorization to remove an adverse head after seeing results.

Completed-only forecast diagnostics use original one-MNQ net-cent labels and
saved probability masses. They average events within each nonempty date, then
weight dates equally. All 126 scheduled dates remain visible; 124 are nonempty,
with 3,236 supported and 511 unsupported queries. Empty dates are null, not zero.

| Head | V123 MSE | V124 MSE | Relative Change |
| --- | ---: | ---: | ---: |
| Baseline | 23,626,311.03 | 23,661,524.07 | +0.1490% |
| Cost only | 22,987,199.14 | 23,018,333.24 | +0.1354% |
| Latency only | 24,265,499.58 | 24,248,037.42 | -0.0720% |
| Combined stress | 23,546,647.84 | 23,524,295.55 | -0.0949% |

MSE units are squared cents per one-contract payoff; lower is better. Cost-only
error improves in folds one/two but worsens in fold three and overall. These
small descriptive differences are not significance tests or a new selection
rule. Cost-directed partitioning did not fix either the target error or PA
economics. Repeating this objective-only change is not justified by this result.

## Verification And Limits

Market exit zero: 13:19:52 UTC. No-fit verifier exit zero: 13:22:58 UTC.
Process completion: 13:23:12 UTC. Separate saved-result audit completed at
13:26:50 UTC and its actual process exited zero. It reconciled 126 saved masses,
2,210 decisions, 11,050 feasible quantities, 44,200 scalar CEs, 156,526 recorded
ledger checks and 7,896 frozen lifecycle checks. Completed V123 controls and
original prepared source bindings were rechecked. Frozen process receipts were
not rewritten to clear their historical audit-pending flags.

Named qualification passed 1,203 cases. The later diagnostic parent selection
passed 528 overlapping related cases. Full regression: 30,005 passed, 18 failed,
22 errors and 516 skipped; it is not green. All 194 collected V124 cases passed.
The six direct verification and later audit/diagnostic modules were not collected
in that earlier full run, but have separate focused evidence. See the detailed
[execution checkpoint](research-v124-execution.md) for failure attribution.

The CE audit reuses frozen numeric utilities. Raw first crossings and intratick
paths are not independently reconstructed. Development dates are reused;
independent validation, official compliance, personal account eligibility,
fee-adjusted cashflow, actual payout and a verified 50K pass remain unproved.
V63/V92 operational recovery remains separate; no orders were enabled.

Status SHA: `4e3c150e16611eb3531ed91cd5fa0eeb0b97ea927f6d7d4833223e0288dfc2cb`.
Seal SHA: `caedfd3140f726ecb11eb4a6653fe930f385c20bc58bebc122d30fc39586afc3`.
Completion SHA: `d2c049582e90bea50e75f33075f3c8884a1317ee6e996c09a911f72a7664603c`.
Separate audit SHA: `a51a619d0f5b32e0ffd9a500d92d49b70537b2c05851a255d118a356cc13c7b7`.
