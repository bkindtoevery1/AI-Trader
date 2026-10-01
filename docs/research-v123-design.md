# V123: Minute Volume And Price Alignment

Declared 2026-10-01 before V123 market feature extraction, fitting or replay.
This is an outcome-informed development candidate, not an independent test,
market-run authorization or live signal model. V63/V92 operation is unchanged.

## Why This Candidate

Exact V121 recovery found negative cost-stress conditional unit means in all
4420 recorded PA decisions despite positive contract capacity. V122's changed
entry trigger also failed; its separate audit found the same sufficient
negative-mean rejection mechanism. Reducing only risk aversion or increasing
quantity does not repair these modeled unit means. We do not remove a losing
head, relax costs or retune either completed model.

This candidate tests whether a new causal predictor helps distinguish
cost-adjusted opportunities: how reported minute volume evolves across the
21 completed bars and aligns with their candle bodies and closing locations.
It is motivated by the user's low-volume/quiet-band observation, not proof of
an edge. V91 added inverse stop size; V92 has current relative volume; V111
encoded price-only OHLC order; V114 added a one-minute pair context; V120 used
one-minute tick-sign pressure. This bounded design review does not establish
universal novelty. No indicators or constants were chosen from new V123 results.

## Fixed Inputs

Preserve the original nine NQ event coordinates and exact event population.
Add precisely three coordinates from the original anchor's 21 completed NQ
minute bars. Each supplied row has explicit contract, interval start/end,
integer-tick OHLC and nonnegative integer traded volume. Match every OHLC and
clock to the original event anchor, not just its last bar. Every interval ends
by decision D; no post-D, partial, missing or duplicate minute is accepted.
Zero-volume bars are allowed as supplied observations, but zero total volume
cannot define this context. Such invalid input is an evidence error, not a
zero feature or a discarded losing event. A source adapter must establish that
these are authentic reported volumes; a hash alone cannot do that.

For 21 bars, volume v_i, total V, OHLC o_i/h_i/l_i/c_i, direction s:

1. Recent-volume concentration: sum(last five volumes)/V - 5/21.
2. Signed volume-body pressure: s*sum(v_i*(c_i-o_i))/sum(v_i*(h_i-l_i)).
   An exactly zero denominator maps to positive zero.
3. Volume-close alignment: s*(sum(v_i*CLV_i)/V - sum(CLV_i)/21)/2,
   with CLV_i=(2*c_i-h_i-l_i)/(h_i-l_i), or zero for a flat bar.

Use exact integer/rational arithmetic before one float conversion. Normalize
negative zero; no epsilon, clipping, tunable threshold or fitted scaling.
All added values are bounded in [-1,1]. Multiplying every volume by the same
positive integer does not change them. Equal volume makes coordinates 1 and 3
zero; coordinate 2 then still contains a price-body summary. Consequently this
is a bundled price/volume representation test, not proof that all benefit would
come uniquely from volume. Volume is traded quantity, not trade count, signed
aggressor flow, quotes or available order-book liquidity.

## Learner And Decision

The separate V123 learner has twelve inputs and four aligned one-MNQ integer
net-cent outcomes. It uses the existing sklearn empirical-forest construction:
64 trees, depth two, at most four leaves, minimum 100 rows per nonroot leaf,
at least five distinct dates per leaf, max_features three, no bootstrap,
seed 202609118, one thread and original date-equal event weights. Preserve joint
outcome vectors; average date-weighted training-event masses inside routed
leaves, not dispersion of tree means. Exported routing and implied means must
match native sklearn. Increasing input dimension changes available splits;
holding tree budget constant does not prove unchanged model capacity.

Use the complete original 181-date source, 45/87/129-date training prefixes,
ten full-calendar-session purges and three 42-date scored blocks. Validate
complete mature labels before original feasibility/stop-support filtering.
No score labels, later fit, volume-dependent row filtering, checkpoint search,
new execution target, seed search or genetic algorithm is part of the design.
The pure learner cannot enforce source/calendar admission on its own.

Proposed integration retains V119's joint positive-integer quantity choice and
all four cost/latency CEs. Evaluation remains original NQ, PA remains MNQ under
the existing study caps, stops, mean targets, half-headroom allocator, MAE,
trailing floor, inactivity, payout, uncapped fill count and cooldown. No forced
trade is added to escape inactivity. Study-specific NQ<=1/MNQ<=6 is not a
redefinition of the user's broader six-contract authorization.

## Finite Comparison And Remaining Work

Propose one candidate and one primary contrast against exact retained V119:
two comparison charges, 13215 to 13217 only on a later explicit one-shot claim.
Three fitted forests would produce 192 trees and four new continuous account
books. These are proposed counts, not completed or reserved work. Cost-only and
latency-only are scenarios, not extra independent trials or fallback winners.

Require positive candidate-minus-control PA net in baseline and combined stress,
with no added hard/MAE breach or earlier inactivity; report absolute Evaluation,
PA net, survival and hypothetical payout separately. Relative improvement alone
does not pass the whole route. Historical dates were repeatedly observed, so
even a favorable development result would not demonstrate generalization.
The sealed 48-date holdout remains closed. Program fees and personal account
cohort/compliance remain unverified.

Current implementation includes the causal feature component, pure learner,
development minute-volume joins and mature population bindings described below.
Still required: exact retained control integration, continuous account adapter,
a finite source-scoped market runner,
trial claim, actual market fitting/replay and independent completed-result audit.
Retain complete conditional masses for future mean/risk attribution rather than
stripping the evidence and reconstructing it later.

Final component and affected-regression run: **929 passed in 6.57 seconds**,
exit 0, under the existing V102 numeric interpreter. It covers the two V123
components, original event-path validation, V118/V120 forests, state utility and
V119 integer quantity choice. Synthetic fits verify software only. No V123
market features, market fits, account replay or comparison charge occurred.
The full repository suite was not rerun for this component stage.

Test scope follows changes: focused feature/forest causality, native parity,
mutation and regression tests now; broader account/source integration tests
when those adapters actually change. Do not require an unrelated 20,000-case
suite on every pure helper iteration or label an interrupted suite complete.
Prior broker-source and central-goal assertion failures remain disclosed.

No market outcome, verified pass, rollout, order, Telegram test, purchase,
Windows restart, schedule change or secret transfer follows from this document.

## Completed Source Join

On 2026-10-01 the separate source-only runner completed with actual exit 0.
All **5485 original events across 181 dates**, 2025-09-08 through 2026-06-12,
received twelve coordinates without event filtering or imputation. Original
nine-coordinate values are unchanged. The adapter validates the original
300-minute source window, then matches each event's exact 21 completed anchor
minutes by explicit NQ contract, OHLC ticks and interval-end nanoseconds.
Source volumes must be native int/float, finite, nonnegative, integral and
strictly below 2^53 before the frozen window validator converts them to float.
Fractional or missing volume is rejected, not rounded or replaced.

The complete original broad-opportunity hash and development snapshot match
their retained structural receipt. Retained event/context identities, frozen
research files, loader cache/policy and original numeric runtime are checked
before/after the operation. Six unrelated application modules differ from old
hashes; an execution guard forbids their use as well as fitting. The old
all-application admission is not bypassed or declared restored. This artifact
establishes only historical development feature content, not mature target
admission, source closure for training, live arrival timing or generalization.
Full-window validation is an offline integrity check, not future input to a
decision or proof that all rows were available live.

The private content receipt is `source-v1.json`, SHA-256
`31be8d88d61115a0c1b5a378990d156c861454d049092f240e005c919eb30023`.
Its full contexts hash is
`48effdad02f2bfc13a99df9b9fe76e821957b1f02b6481e66bc63eec385a5b5a`.
The parent rechecked all 5485 context self-hashes, count, date order and current
runner/helper hashes after publication. The market-derived feature artifact
is kept private and is not included in public documentation commits.

Focused source/adapter tests: **59 passed in 1.61 seconds**. Final combined
component/source/affected regression: **1011 passed in 9.23 seconds**, exit 0,
including the V121 recovery guard. The parsed JUnit has no failures, errors or
skips. This stage did not rerun the full repository suite; the earlier
interrupted full-run failures remain disclosed. No market fit, account replay,
comparison charge, label selection or live deployment occurred. Historical
ledger remains 13215 and the sealed holdout remains closed. That source stage
left mature-label/population binding as the next task, completed below.

## Completed Training Binding

The source-only training runner completed at 2026-10-01T06:17:50Z, actual exit
0. The three original plans exactly match their retained hashes: 45/87/129
scheduled training dates, ten full-calendar purge sessions and 42 scoring dates
per fold. Training populations contain **1335/2372/3391 events**, respectively,
on 45/85/127 represented dates after the original support filters. Dates with
no retained rows still remain in the scheduled calendar and purge calculation.

Pinned V97 four-mode MNQ unit journals and pinned V102 plans were reused, not
recomputed or retuned. The complete source journal file contains already-known
development outcomes; only exact training-prefix labels enter each population.
All original training event journals, including later-excluded events, pass
strict resolution-before-cutoff checks before initial MNQ capacity and stop
support filters. No scoring-specific NQ capacity filter enters training.
The original V118 population hashes match all three retained admissions; both
old pressure-arm exports in each fold match original nine coordinates, one-MNQ
integer-cent targets, event/date order and date-equal weights exactly. Only the
three fixed new feature coordinates differ from the original nine-input data.

The runner reconstructs the original event source and checks full source,
context, code, loader and numeric-runtime bindings before/after work. Each
prepared numeric array has immutable byte backing. Caller-bound context/source
hashes remain content authentication, not proof of live availability. No old
all-application admission is declared restored, and raw ticks were not rescanned
in this stage. The historical journal bytes and prior receipts remain the
provenance evidence; account replay must still verify its own execution input.

Private `populations-v1.json` SHA-256:
`9a626d55bc6dffbdadf00859df99095f782b037017a298d5d47b57484fa21e0e`.
Its complete populations hash is
`88ade59c7f2cba3031104a7f02d0568c56a53d95431b8275de9330b51e78b798`.
The parent reopened the artifact, reconstructed all three typed populations,
validated their bindings/arrays and reconciled the original input hashes.
Feature/target arrays remain private, not part of a public documentation push.

Adapter checks: **34 passed in 5.23 seconds**. Runner binding checks initially
passed 29 tests; final combined source/population/component/affected regression
passed **837 tests in 23.01 seconds**, exit 0, with no failures/errors/skips.
The full repository suite was not rerun. No market learner fit, account replay,
new comparison charge, holdout access, signal-policy change or order occurred.
Ledger remains 13215. Next is the three-forest/four-account integration and its
finite claim, not additional data collection or a new feature-selection search.

## Account Source And Pipeline

The retained account source was published at 2026-10-01T06:37:32Z. Independent
readback verified its full file SHA-256
`ba96345185f523d776c549caa3e2a56dbfe24b9d1e023f6ae67afa1b29cdd358`,
original prepared-source identity, six original models, 252 forecast envelopes,
181-date projection and eight retained control books. Both control arms match
the completed V119 status byte-for-byte under the original canonical encoder.
Raw-pair metadata matches the original V102 lock; no raw tick payload was read
by this restoration. The producer process's final exit was not retained after
context transition; successful immutable publication and independent readback
are the evidence, not an invented process exit code.

The new pipeline validates all three original causal prefixes and all 126
scoring-date query populations before fitting. It preserves original coordinates,
unit targets, weighting, support rules and integer-cent distribution envelopes.
It exposes exactly nine ordered fit-stage callbacks for three 64-tree forests.
The replay adapter runs four unchanged V119 quantity-account variants against
one authentic raw-pair pass, with a single declared V119 contrast and unchanged
cost, breach and payout distinctions. These are implemented components, not
completed market fits or replay results.

Real-data no-fit integration exited 0 in session 74769: **181 source dates,
three folds, 1335/2372/3391 training events, 126 query dates and 3747 queries**.
The original prepared-source identity and exact control bytes matched; source,
artifact and runtime pins were checked. Fitting and execution of the six
drifted application modules were forbidden throughout the causal preflight.

Combined source/pipeline/replay and affected component tests: **254 passed in
274.69 seconds**, exit 0, with zero failures/errors/skips in the parsed JUnit.
The full repository suite was not rerun. No new market fit, account replay,
comparison charge, holdout opening, Windows deployment or order occurred.
The historical ledger remains 13215. A finite claim and qualified execution
runner are still required before the planned two-charge market experiment.
