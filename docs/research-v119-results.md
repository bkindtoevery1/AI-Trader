# V119 Results: Small Quantities Do Not Resolve PA Inactivity

Completed 2026-09-27. Verdict: **FAILED_SPARSE_PA_ACTIVITY_AND_STRESS**.
This is a completed historical development experiment, not missing-data zero
validation and not a verified personal-account pass.

## Reason And Fixed Experiment

[V118](research-v118-results.md) tested distributional utility at maximum allowed
size and abstained throughout PA. [V119](research-v119-design.md) asked whether
jointly choosing flat or a smaller integer quantity could recover worthwhile
trades. It restored the exact three fitted forests without refitting, retained
both the original and V118 own-headroom controls, and changed only the quantity
decision rule. Costs, delays, actual-entry checks and account rules stayed fixed.

All 181 admitted explicit-contract pairs were scanned; 126 chronological dates
were scored. Four new account books were compared with eight retained books.
504 candidate account-days were scheduled;453 were processed before terminal
states, with 51 mechanical terminal-zero slots. These are not 51 missing sessions.
Four original NQ Evaluation prefixes and all 126 distribution hashes matched.
The 48-date sealed holdout stayed closed. The exclusive claim charged three
comparisons once, taking the historical ledger from 13,206 to 13,209.

## Complete Economic Results

All amounts below are simulated trading dollars after the modeled commissions
and adverse fills, **before unpriced program/subscription/activation fees**.
The four execution scenarios are not independent samples.

| Mode | Inherited NQ Evaluation PnL | New MNQ PA PnL | PA Trades | PA Days At Least +$50 | PA Status |
| --- | ---: | ---: | ---: | ---: | --- |
| Baseline | +3254.00 | +135.96 | 1 | 1 | Inactivity closure |
| Cost only | +3292.00 | +72.00 | 2 | 1 | Inactivity closure |
| Latency only | +3130.20 | -65.54 | 1 | 0 | Inactivity closure |
| Combined stress | +3429.00 | -68.50 | 1 | 0 | Inactivity closure |

Numerical Evaluation passes in every scenario are inherited exactly from the
unchanged control, not a new learning benefit. No hypothetical payout, actual
payout, complete PA survival or full-route pass occurred. Hard threshold and
PA MAE violations were zero; that does not turn an inactive strategy into a pass.
Four monthly Evaluation renewal units remained in each inherited journey;
dollar subscription costs and the user's exact legacy cohort remain unverified.

| PA Comparison | Baseline Delta | Stress Delta | Required Joint Benefit |
| --- | ---: | ---: | --- |
| New policy minus original | +1407.10 | -811.00 | Failed; also earlier inactivity |
| New policy minus V118 own-headroom | +135.96 | -68.50 | Failed |

The candidate improves the original baseline loss but loses the original stress
profit and closes earlier. Against V118's zero-trade control, baseline improves
but stress becomes negative. Neither preregistered primary comparison passes.

## Failure Attribution And Lesson

- Across the four scenario books there were 2,200 eligible PA quantity decisions:
  2,195 flat choices and five positive choices, all executed as one MNQ contract.
  These are scenario counts, not 2,200 independent statistical observations or
  five necessarily distinct market opportunities.
- All five positive choices were below maximum capacity and overcame the old
  maximum-size utility veto. Thus the proposed mechanism did sometimes work,
  but it did not produce a viable account strategy.
- Zero decisions had zero allocator capacity. In every flat decision, the
  cost-only head was the limiting one-contract CE. Contract capacity, Windows
  collection and absent historical data did not explain this abstention pattern.
- The fixed simulated activity rule required two days of at least +$50 in its
  rolling 30-calendar-day window. The books achieved only 1/1/0/0 such days and
  closed. This describes the locked simulation, not newly verified current rules
  or proof of the user's account cohort.
- Basic and cost-only outcomes include target exits; delayed scenarios include
  stop exits. Sparse fills and negative stress economics remain material limits.

Do not rescue this closed attempt by removing its stress head, increasing risk
tolerance, forcing activity or tuning quantities against these outcomes. V117
already tested baseline-only nomination without solving PA economics. A next
study should first check whether genuinely new causal information about
cost-adjusted payoff exists, with explicit comparisons to prior volume/event-
order work. No V120 model, claim or new fit is created by this next-step note.

## Execution And Verification

- Sole market process: 05:15:43Z to 06:32:42Z, actual exit 0. Sources and runtime
  unchanged. No partial outcomes were opened, no refit and no rescue rerun.
- Separate observed postrun verification: 06:36:16Z to 06:36:21Z, actual exit 0.
  Rechecked 3,826 dependencies, retained controls, distributions, immutable outputs,
  qualification and the complete economic summary.
- Independent recorded-ledger arithmetic: 156,843 checks, no discrepancies;
  its explicit scope excludes independent raw-tape/first-crossing reconstruction,
  model fitting/provenance and full fee/payout lifecycle reconstruction. Those
  boundaries are not relabeled as independent market validation.
- Focused software tests: 485 passed, exit 0. Full actual unique cases: 19,689 passed,
  two failures, one skip, exit 1. See [status](research-v119-status.md) for the
  corrected metadata spelling and inherited-failure recheck, and the additive
  [JUnit header erratum](research-v119-test-count-erratum.md). The suite is not green.

Local-only immutable evidence hashes:

| Artifact | SHA256 |
| --- | --- |
| Status | `55ad53f9536ccde284d01391746585579f574b0c45635d085af439a983249c80` |
| Result seal | `a3ffc4fdd0afa19f0a90a92025cb1b3f93c9e608d728f8e6af1230a8e10e9d94` |
| Market terminal | `c008d040a5a12655f094a160ea798010257038a393f52b1a908d179e5a01757e` |
| Postrun terminal | `0175375ce0749849d1b75a729e751fd772b273a2759637c401ace2050b23df3f` |
| Postrun summary | `6a8263ae9c748cf5c4f87d4940e6d06fd6da3f93e5cfa257e4627a28d785af38` |
| Completion verification | `eefc627d0b9e3bb7b55182a2d3511cb69b0c1fbe2f809cdd958d9bf9c00f5b18` |

Public documentation contains aggregate results only. Detailed ledgers, raw
data and fitted artifacts remain private/local. This result does not authorize
deployment, Telegram trading signals, orders, new data purchases or holdout access.
