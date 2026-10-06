# V137: Account-State Transition Targets

October 6, 2026. Development milestone, not a fitted model, registered market
experiment, new account replay or deployment. The ongoing model-development
objective remains incomplete. V136 and all earlier outcomes stay unchanged.

## Reason

The [V136 execution audit and retrospective](research-v136-tick-audit.md)
confirmed recorded exits but found that higher realized PnL can coexist with
the same depleted trading headroom. Net terminal payoff alone omits the
unrealized peak that moves the account's trailing floor. The proposed successor
will learn cash and floor transitions conditional on causal account state,
rather than assuming an old one-contract PnL scales into the actual account.

V106 transformed terminal payoffs, V118 used current headroom as risk tolerance,
and V119 optimized integer quantity over terminal-payoff distributions. These
are relevant precedents, not failed models to erase. A joint state-transition
learner must be compared against unchanged V136, not called better from its
architecture or software tests.

## Avoid A Structural No-Trade Rule

With cash C, floor F and usable headroom H = C - F:

    delta_H = delta_C - delta_F

Before the Legacy floor cap binds, F = running_peak - 250000 cents. At a fresh
account's starting peak, H is already the maximum 250000 cents. A profitable
trade can raise the floor as much as or more than its realized profit, including
the difference between interim marks and adverse liquidation costs. Requiring
strictly positive expected headroom change alone can therefore prevent the
first trade. V137 does NOT introduce that gate or claim that more contracts
solve an exhausted feasible risk budget.

One synthetic NQ example with the frozen execution costs realizes +48690 cents
but raises the floor 49345 cents, leaving headroom 655 cents smaller. This is
an arithmetic example, not a measured strategy return. Cash progress and
capacity consumption both need to remain visible to the future decision rule.

## Implemented Component

`tools/nq_apex_transition_targets_v137.py` is pure and performs no I/O, fitting,
source admission, order or population selection. It provides:

- An immutable flat-account EntryState containing phase, cash, prior running
  peak, day-start cash, known-at timestamp and prior full-size latch.
- Six causal state coordinates, with no future entry quote or outcome access.
- One guarded counterfactual transition using original CostGeometry, original
  integer sizing and the unchanged V136 GivebackAccount execution kernel.
- Separate cash, floor, peak and headroom deltas, actual contracts, resolution
  and conservative full-window label maturity. Every genuine geometry/risk skip
  remains a zero transition, not an omitted or successful trade.

Preserved mechanics: NQ Evaluation/MNQ PA, at most 1 NQ / 6 MNQ, fresh PA sizing cap,
day-start MAE, positive actual-entry target, PA nominal stop/target guard,
same four fee/latency modes, initial stop/target, causal 1R half-peak protection,
account trailing breach precedence, actual gap fills and costs. No global module
monkeypatch, new exit threshold or copied trade-PnL rescaling is introduced.

All input clocks use the declared development date, original 10:30-14:00 ET
decision range, exact 60/240-second entry delay and 91-minute scheduled endpoint.
State must be known by the decision. Geometry is label evidence, not a predictor.
Provider-first entry, source authenticity and complete raw-window coverage still
belong to source admission. Dataclass/type validation alone cannot prove them.

This is a single eligible flat-decision transition. It does not independently
simulate position overlap/cooldown, monthly fees, PA activation, payout history,
profit-qualified activity or whole-account survival. A later account evaluation
must retain those original lifecycle rules; labels alone are not PA evidence.

## Work Still Required

Before any market fit, fix an outcome-independent training-state population and
the learner/decision objective. The 321 selected V136 executions must not become
the training population. Enumerate all original eligible opportunities and
validate their full census before known support filtering; do not remove rows
because future quotes, costs, capacity or guards produce a zero transition.

State replicas for one event share one outcome path and are not independent
observations. Per-date and per-event weights must not inflate with replica
count. Keep exact chronological folds, full-calendar purges and conservative
label-maturity cutoffs. Query only causal own-account state, not a comparator's
balance or future termination. Off-grid state handling must be fixed before
scoring, not tuned after failures. Preserve all 48 sealed holdout dates.

Then freeze and publish the full experimental design, source/model/test pins
and comparison reservation before creating any market labels or fits. Fit and
restore the learner, publish complete forecasts before outcome scoring, and
run the full guarded account comparison. Software correctness, label validity,
predictive benefit and complete Evaluation-to-PA economics are separate gates.

Current new market fits, counterfactual market labels, account replays and trial
charges are all zero. The total remains 13,258. This milestone does not replace
or activate Windows V63/V92. Their operational connection recovery is separate.

## Verification

A separate test agent authored 172 synthetic cases, including hand-calculated
cash, commission, slippage, running-peak and floor transitions. The initial run
had 170 passes and two failures: nested completed-minute values were not
revalidated when an otherwise frozen input had been malformed. The component
now checks the exact anchor and every completed minute before execution. The
same 172 cases pass after that repair. No market data was used in these tests.

Coverage includes both products/sides, all four execution modes, capacity and
PA MAE boundaries, gap/guard precedence, genuine skip labels, future-state
rejection, immutable inputs, no I/O/fitting and full-window label maturity.
The tests explicitly demonstrate positive cash with negative headroom change.
All nine frozen V136 source/design/test hashes remain unchanged.

The combined focused/affected regression completed with actual process exit 0:
929 passed, no failures, errors or skips, in 182.537 seconds. That includes
172 new cases plus 757 unchanged V136 account/source/replay/runner and V86/V87
execution/account cases. The initial standalone 172-pass run overlaps this
count; it is not added again. No full-repository green claim is made.

Source SHA256: `da2db584d5efe75eb6bfbdb19c2c099c4d544b8a7c63d5fe3e9d729b66150bca`.
Test SHA256: `8a87ad09501c07976280899cef04790bf94097e3e6f8b896060f96bceea77958`.
Combined JUnit SHA256: `274550231af534b6fd9ca2230df4fdfbe15d40e9e8a7fef9cf1a53bb03537916`.
