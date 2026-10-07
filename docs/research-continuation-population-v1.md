# Reachable Continuation Population

October 7, 2026 UTC. Research implementation and a candidate chronology, not a
registered market experiment, independent validation or operational recovery.

## Why This Component

The learner needs decisions from accounts that could actually have reached
them. A Cartesian product of every event and every retrospective account state
would invent opportunities, and using the day's final trade count would leak
later actions. The new day adapter connects the original account trace and
paired action simulation directly to the existing 31-feature learner API.

`tools/nq_apex_continuation_population_v1.py` runs the unchanged roll-in for the
anchor date, finds every reachable positive-capacity decision, then compares
ABSTAIN and ATTEMPT at exactly that state through the declared horizon. Original
abstentions are included. Busy/cooldown and original support exclusions remain
excluded by the original account, not by their future profitability. Zero
capacity is recorded separately and never assigned an invented action pair.

Each pair must reproduce the complete original pre-decision account snapshot,
anchor and eight raw forecasts. The historical phase trading-day count comes
from completed phase days; today's count includes only fills resolved before
the decision. The original source census, reachable census, capacity exclusions,
trace nodes, pair digests, row digests, binding identities and branch outcomes
remain explicit. Shared forecasts and source windows must stay identical
between the roll-in and all subsequent pairs, not just within a single pair.

The caller's account is unchanged even on success or exception. A separate
successor advances exactly one day under the original roll-in, not under a
hypothetical action branch. This prevents label generation from changing the
next day's state distribution. Returned rows use the learner's exact field set;
empty product populations remain empty, never zero-valued training examples.

State IDs conservatively retain full causal account history and roll-in origin.
Feature-identical histories are not asserted to be identical simulator states.
Semantic deduplication is not claimed; date/event weighting and the maximum of
two roll-in states remain required at final population assembly. Matching
hashes and this pure component do not authenticate raw sources or model bytes.

## Candidate Chronology

An independent read-only review confirmed the following single proposed split
against the closed V137 fast claim and model metadata. It is not a parameter
search and has not been reserved or used to produce market labels or fits.
The horizon of ten declared source dates represents a fixed two-trading-week
planning approximation, not a choice based on new continuation returns.

| Role | Zero-Based Slice | Dates | Count |
| --- | --- | --- | ---: |
| Frozen teacher training | `[0,45)` | 2025-09-08 to 2025-11-14 | 45 |
| Original teacher purge | `[45,55)` | 2025-11-17 to 2025-12-02 | 10 |
| Student action anchors | `[55,87)` | 2025-12-03 to 2026-01-23 | 32 |
| Additional label-maturation dates | `[87,96)` | 2026-01-26 to 2026-02-05 | 9 |
| Post-maturity embargo | `[96,106)` | 2026-02-06 to 2026-02-20 | 10 |
| Account scoring | `[106,181)` | 2026-02-23 to 2026-06-12 | 75 |

Ten inclusive dates make each label endpoint `anchor_index + 9`, at 17:00 ET.
The first endpoint is December 16; the final is February 5. The ten-date
embargo starts after that final endpoint. Reusing the old fold-2 purge would
leave only one excluded date after label maturity and is therefore wrong.
These are entries in the frozen source calendar, not independently certified
complete exchange sessions or an assumption of ten consecutive weekdays.

Both first-fold product-specific teacher pipelines remain fixed throughout;
no second/third-fold teacher substitution, scaler refit or calibration. Both
original roll-in arms supply their own states, but both action branches use
cash-only continuation on their own evolving states. The old teacher cutoff
is `1763388000000000000` (November 17, 2025 at 09:00 ET). The independent audit
only verified recorded query lineage in the 32-date anchor prefix. Later
continuation and scoring queries still need authenticated causal reconstruction.

Any student fit needs an explicit simulated market-information cutoff after
February 20 at 17:00 ET and before the first February 23 scored decision.
Its actual offline execution timestamp must remain the true current timestamp;
this is not a claim of having trained or deployed the model in February.
Roll-in starts from the original fresh Evaluation account on December 3.
For the proposed account comparison, each policy starts a separate fresh
Evaluation account on February 23 and carries its own account continuously
through June 12. Embargo paths do not initialize or tune these scored books.
These proposed semantics must be bound in the eventual new experiment plan.

The original three V137 plans remain unchanged ancestor evidence. They cannot
be relabeled as this student schedule while retaining their old hashes. A new
chronology/population contract and comparison reservation remain necessary.

## Limits And Next Integration

The parent then ran the original current-content restoration and complete
context lookup against today's files, plus all six saved model-record checks.
It exited 0 in 183.032 seconds and reconciled 181 dates and 5,485 original
events. Source binding is
`333f16a9d173fbd4747f94f1f16b8fdd2769088d27967e38f04331ceccb8fc5d`;
the exact first-teacher bindings and original first plan are recorded in
`reports/nq_apex_continuation_population_20261007/source-restoration.json`.
This is the existing V123 current-content restoration route, not a renewed
provider admission, raw-pair rescan, deserialization or native-model audit.
No prediction, new label or account replay ran during this check.

A separate subsequent check restored only the two first-fold NQ/MNQ native
models from their exact verified bytes. The numeric runtime matches the closed
claim; each pipeline's eight HGB heads, two native scalers, feature dimensions,
100 iterations, fixed parameters and complete metadata match the saved record.
Hashes were checked again after restoration. That check also exited 0 and made
zero prediction or fit calls. Evidence is in
`reports/nq_apex_continuation_population_20261007/native-teacher-restoration.json`.
No second/third-fold model was deserialized or selected.

The 32 overlapping training anchors are not 32 independent ten-date journeys.
The 75 account dates are one dependent development replay, not a new holdout.
If a complete ten-date forecasting diagnostic is also implemented, only 66
scoring anchors through May 29 mature within the development fence. The nine
June 1-12 tails cannot become zero targets, shortened horizons or a reason to
open sealed data. Account scoring through June 12 is a separate estimand.

Remaining work is authenticated context/tape delivery to the new adapter,
complete four-mode/two-origin population assembly and its census,
bounded replay performance qualification, final experiment registration,
market fitting, learner-driven account execution and complete result audit.
No new market label, fit, replay, comparison reservation or signal was produced
here. Effective trials stay 13,293 and all 48 sealed dates remain closed.

## Verification

The parent synthetic smoke generated one pair, left the caller unchanged and
returned the correct original-day successor. Independent testing added 129
synthetic cases, including direct original-account and standalone-fork
reconstruction, NQ/MNQ and long/short parity, phase transitions, prior-only
counters, excluded/empty/terminal dates, all-mode geometry, a 63-date horizon,
shared-callback consistency, detachment and rollback. A separate subprocess
keeps normal Python control-class cache initialization out of legacy namespace
guards; it does not mock account execution.

The final parent affected suite passed 1,245 distinct cases in 22.00 seconds,
exit 0, with no failures, errors or skips. The 129 new cases are included, not
added to this total; the independent 133-case invocation overlapped four old
guards. Existing learner, fork, trace, target and account regressions are in
the parent run. Full repository regression was not run.

Final JUnit: `reports/nq_apex_continuation_population_20261007/affected-qualified.xml`.
SHA-256: `2c5ad841142d7414aed56d89f601e96daa90e8c0a9d65ba0ee31c246c9b19ed8`.
Software tests, source restoration and native model restoration do not establish
a new market result or live Windows signal. No market performance is implied.
