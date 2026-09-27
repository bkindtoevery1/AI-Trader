# v87 Progress

## Current Status

The frozen eight-policy raw replay completed at 2026-09-07T09:39:13Z; exec 54198
exited zero. All 181 raw pairs and 402,041,614 events were verified; all four
original-control/source checks passed. There were zero development passes and
zero numeric Evaluation passes in every mode, with no PA entries or payouts.
The independent postresult internal-consistency audit passed. It did not
independently replay raw ticks or certify first-fill selection. Do not restart,
retune or claim a verified model. Cumulative counted comparisons are 13,069.

Implementation commit: `9502be8`, local only. Prefreeze regression passed 5,643
tests in 194.51 seconds; 360 focused tests passed separately. Freeze completed
at 2026-09-07T09:25:31Z with 426 dependencies. The structural preflight completed
at 09:26:07Z: 109 of 181 raw dates have any causal event, with 246 opportunities.
These are only structural upper bounds, not profitable fills or active-day
performance. Outcome replay started at 09:26:39Z after reserving eight policies.

Lock SHA256: `eb06546d8de1d5c8333f3c7fe9f80ff8f912a4dd441e2df6b1cb5c713ed4885c`.
Preflight SHA256: `6d93572d95d56e92319d57725094f93edf1bdc6d6d74c310e2b9a792329f753c`.
Run marker SHA256: `de6fb3c048b1a3990f696c53ba8f8a3b8909e619a4efe1f799f85a2e2032f6ea`.
Status SHA256: `10ec2a859cfc41e3069717468ae295baa54544ae5d5f20aa5d83114cc307930b`.
Result seal SHA256: `aa20c358034d269a2dc83ba19c64a468955344d538e1120181ba4747a2ef18ae`.
Failure attribution SHA256: `1e28d3eb50e3727984320939b167c96cba66da884db9dac579d87aefeb344b65`.
Report consistency audit SHA256: `0772ad80b0368fef8f618ca9879f1de0500ac939353330e0eb84473c51dabd5e`.
Completion audit SHA256: `7ea486da8422a0445ee1db41f04af983731b7e17f264b788fb7eaa32b82b2dc3`.

## Completed Frequency Contrast

NQ baseline direct policy, after trading costs but without account guards or
external program fees: one-fill cap 101 fills / -2,783.10 USD; three-fill cap
161 / -3,804.10 USD; six-fill cap and uncapped both 168 / -4,390.80 USD.
Every cap traded the same 101 dates. Six and uncapped were identical; at most
five baseline NQ fills occurred in a day. Extra fills increased losses in this
experiment rather than adding independent dates. This does not prove a daily
cap is universally needed or that all repeated-entry strategies are unprofitable.

Actual account paths differ because risk skips and account state change entries.
Their baseline NQ trading PnL was -1,441.10 / -22.20 / -34.80 / -34.80 USD for
the same four caps. None reached Evaluation qualification; do not confuse
guard-free policy losses with simulated account losses or omission of external
program fees with positive real economics. Positive latency-only diagnostics
do not authorize selecting that clock after observing outcomes.

## User-Directed Change

Before any observations, the user asked to remove the daily count limit, then
to relax it gradually. The final planned comparison is actual filled-trade
caps 1, 3, 6 and uncapped. Identical opportunities, skip handling and five-minute
post-resolution cooldowns apply throughout. Cost/risk skips consume no fill
quota, even in the one-fill diagnostic. There is no daily count stop in uncapped.

Separate NQ1 and MNQ-up-to6 execution gives eight counted policies: six main
and two one-fill diagnostic comparators. Daily count limits do not change
concurrent-contract limits, stop-loss/risk budgets or account rules. Four
mandatory cost/entry-latency modes retain the same absolute time exit. Repeated
fills are aggregated once per trade date; mixed long/short days are not flat.

## Verification And Retrospective

- Final postresult/LAN regression: 5,828 passed in 197.33 seconds, zero failures
  or skips. Combined focused tests passed 197; updated central-state tests
  passed 15. An initial full run had 5,827 passes and one unfrozen account-state
  assertion still expecting v86. Updating that completed-version/count binding
  fixed the failure without changing frozen code, model design or gates.
- All 426 frozen dependencies, source metadata and environment still match.
  Completion audit binds the final JUnit XML and sealed result/audit hashes.
- Postresult auditor: 71 synthetic tests passed, then all 32 direct journals
  and 32 account reports passed the completed-report arithmetic, chronology,
  cost, quota and aggregation checks. Caller separately checked sealed bytes;
  the pure auditor itself makes no source-first-tick or independent-replay claim.
- Extractor: 116 synthetic tests; causal minute prefixes and volume references.
- Account adapter: 169 synthetic tests; quotas, skips, costs, cooldowns, one daily
  lifecycle settlement, PA scaling/MAE, payout-day aggregation and breach stops.
- Independent adapter review found no concrete defects; global first-tick
  selection is caller-owned and covered by separate orchestration tests.
- Independent runner review found equal-byte concurrent stage claims and a
  lock-byte mutation gap. Both are fixed before observations and have regressions.
- Preliminary full regression had 5,639 passes and one stale central-state
  assertion expecting v86 as active work. It was corrected to distinguish v86
  completed evidence from v87 unreserved implementation. Final regression passed
  with zero failures/skips; this supersedes that preliminary software failure.

These are software tests using synthetic fixtures, not market-performance
evidence. Earlier frozen code, research outputs and operating deployments were
not modified. Holdout, orders, credentials, network routes and schedules remain
unchanged. Detailed local reports are not automatically backed up by GitHub.

## Execution Gates

The frozen JSON policy, design, code, tests, environment and source metadata
preceded the structural causal-opportunity preflight on 617 development minute
sessions. Fewer than 30 opportunity dates among the 181 raw dates would have
aborted the entire batch without outcome replay; this gate passed with 109.

Eight comparisons were reserved, taking the ledger to 13,069. Replay all
181 explicit-contract raw pairs exactly once. Do not expose incomplete returns
or retune after seeing results. Preserve the exact old control and independent
final holdout. Report frequency contrasts, costs, account outcomes and failures
even when no policy passes.
