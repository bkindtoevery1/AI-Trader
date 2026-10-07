# Continuation Training And Account Execution

October 7, 2026 UTC. Implementation of the proposed continuation experiment's
training and execution connections, not a registered or completed market study.
The [population adapter](research-continuation-population-v1.md) and
[learner](research-continuation-learner-v1.md) remain the preceding components.

## Complete Training Population

`tools/nq_apex_continuation_training_v1.py` reads every declared anchor date,
both original roll-in arms and all four execution modes exactly once. For the
proposed 32-anchor schedule this is 256 day records. It consumes one record at a
time and retains learner rows, compact references and the eight current account
snapshots, rather than holding every historical day trace simultaneously.

Each record must bind the same source contexts, frozen teachers, cutoff and
inclusive horizon. The first account is fresh; each subsequent day must start
from the preceding original roll-in's exact ending snapshot. Reachable and
zero-capacity decisions are reconciled to original opportunities. The adapter
reconstructs all 31 features from the known state and prior-only counters,
reconciles the two finite-horizon outcomes to their target difference, and
checks the row, state, trace-node and day identities.

Repeated source-window or teacher-query identities must have identical content
across dates, origins and modes. Each product/head retains its own state rows.
Both products and all four heads must meet the learner's existing minimum of
20 nonempty dates and 100 original events before this API returns. Sorting is
by original decision clock and state ID. Date/event/state weights and the
maximum of two origin states remain unchanged; replicas are not independent
trading observations and semantic state deduplication is not claimed.

Context mappings are JSON objects, not an order-bearing list. The assembler
validates their exact contents, then derives event order from native decision
clocks and date order from the declared calendar. Canonical JSON serialization
must not turn valid context into a different event sequence. Duplicate clocks,
missing dates and incorrect event content remain errors.

This is a content and chronology check, not a raw-tape replay or authentication
of the teacher/day artifact bytes. The caller still authenticates those bytes.
The retained pair digests and compact branch outcomes do not independently
re-execute future ticks or prove a profitable counterfactual trading policy.

## Learner-Driven Account

`tools/nq_apex_continuation_account_v1.py` adds one fixed policy,
`continuation_all_positive`, using private clones of the original V137/V136
engine. At a reachable positive-capacity decision, the original teacher makes
its eight forecasts and the learner makes four continuation-advantage forecasts
at the same immutable EntryState. The learner also receives only previously
completed phase trading days, completed fills earlier today and the original
eight forecasts. The caller attaches the authenticated 15 market features.

Nominate only when all four raw, finite continuation advantages are strictly
positive. There is no epsilon, projection, artificial teacher forecast,
quantity override or direction override. The original teacher's complete
decision is retained separately; its cash-only diagnostic nomination is not
presented as the learner's strategy. Teacher and learner each have separate
two-product model/population/cutoff bindings checked before prediction.

Original support, zero-capacity bypass, entry geometry, long/short direction,
sizing, costs, slippage, giveback exit, risk guards, cooldown and Evaluation-to-PA
lifecycle remain unchanged. Intraday fill count is updated only after a real
positive-quantity simulator fill, not after a geometry skip, and reconciles to
the original daily count. Failed callbacks or reads restore the complete account;
arbitrary external callback side effects remain outside that rollback boundary.

## Integration And Remaining Work

The end-to-end test connects invented ticks, original roll-ins, paired labels,
complete population assembly, actual sklearn HGB fitting, serialization and
restoration, raw predictions and account nomination. Synthetic software evidence
must not be reported as strategy performance or a live signal.

The proposed market design remains 32 anchors with a ten-source-date inclusive
label horizon, a full post-maturity ten-date embargo and 75 development scoring
dates. No horizon, threshold, fit recipe or scoring date is tuned here. A new
registered experiment, authenticated tape integration, bounded execution cost,
market fits and complete account/result auditing are still required. The two
first-fold teachers and current-content source restoration were verified in
the preceding checkpoint, not refitted here.

Mac has 16 GiB of physical memory. A read-only projection of the exact closed
V137 `accounts.json` receipt metadata finds 14,564,425 to 24,393,004 full-session
NQ/MNQ rows in the 32 proposed ten-date windows; the first has 18,406,746 rows.
These are full 23-hour input counts, not measured regular-session memory or a
runtime estimate. They justify a bounded tape/residency qualification before a
full raw-tick job, not shortening the research horizon after observing outcomes.

No market pair, market fit, new trial reservation, holdout access, Windows
installation/restart, signal or order was produced in this implementation step.
Historical effective trials remain 13,293; all 48 sealed dates remain closed.

## Verification

The final parent invocation passed 1,642 distinct cases in 1,550.09 seconds,
exit0, without failures, errors or skips. The 397 new cases comprise 147 training
assembly cases, 232 account cases and 18 end-to-end cases; they are included
in that total, not additional passes. The remaining 1,245 exercise the preceding
population, learner, fork, target, trace and original account components.
Independent account results overlap the parent invocation. Full repository
regression was not run and is not claimed.

The end-to-end fixture fits two genuine sklearn product models with four native
HGB heads each, using invented data only. It serializes/restores them in memory
and exercises their unchanged raw forecasts through both phases, directions and
all four account modes. A valid abstention is not forced into a trade merely to
make this integration test look active. No saved market model is produced.

The earlier parent run was deliberately interrupted after 1,066.51 seconds,
before any test completed, because it had imported the pre-final source and
global fitting-entry profiler. Its exit2 and zero-test JUnit are retained as
incomplete evidence, not a passing run. The final test guard uses local Python
monitoring where available, verifies that forbidden fitting is detected, and
retains the profiling fallback for older interpreters.

The two fixture-heavy test cases took 669.057 and 660.948 seconds respectively,
including setup. They generated the complete 32-date population independently.
These times do not isolate HGB fit cost. Repeated full population validation
took about50 seconds per case. This establishes a substantial component/runtime
cost on tiny invented ticks; production tape execution still needs bounded
performance qualification without changing chronology or outcome definitions.

Final JUnit: `reports/nq_apex_continuation_execution_20261007/affected-final.xml`.
SHA256: `f7f75eacb631d09f1747677f60e91e237e5f6364d32ac219f9a72e7b35dd2e8f`.
Initial incomplete JUnit:
`reports/nq_apex_continuation_execution_20261007/end-to-end-initial.xml`.
