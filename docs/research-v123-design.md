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

Current implementation is only the causal feature component and pure learner
with invented-data software tests. Still required: authenticated minute-volume
joins, full population/label bindings and maturity checks, exact retained
control integration, continuous account adapter, a finite source-scoped runner,
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
