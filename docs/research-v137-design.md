# V137: Cash And Trailing-Floor Transition Learning

October 6, 2026. Outcome-informed development design. This is not independent
validation, a successful model, a live signal or current-cohort certification.
Market execution is NOT_AUTHORIZED_BY_THIS_DOCUMENT: source/census integration,
account inference, immutable runner and their tests must be complete, pinned
and reserved before creating market transition labels or fitting. The existing
[component milestone](research-v137-transition-targets.md) is not a full model.

## Hypothesis And Matched Contrast

V136's profitable interim marks can raise the account floor without preserving
enough capacity for later trades. Learn actual cash gain and floor increase
conditional on known account state, retaining its giveback exit unchanged.
Do not rescale selected trade PnL or learn from only V136's 321 executed trades.

Use one fixed state-conditional HGB recipe, separately for NQ Evaluation and
MNQ PA, in each of the same three chronological folds. Predict cash and floor
increments in each of four original cost/latency modes. Eight response heads
per fit, six fitted pipelines total. There is no tuning grid or early stopping.

Two decision arms share those identical fitted heads:

- cash_only: nominate if all four predicted cash increments are strictly >0.
- cash_plus_headroom: nominate if all four `2*cash - projected_floor` scores are
  strictly >0. This equals predicted cash plus predicted headroom change.

Flat has score zero. The unit weight on headroom is a declared, unoptimized
shadow-price assumption, not a learned optimum or proof of an economic edge.
Floor projection is nonnegative and, in PA, bounded above by the CURRENT
remaining floor-cap capacity. At the cap it is exactly zero. This prevents
both negative increases manufacturing free capacity and impossible increases
penalizing capped accounts. Raw unprojected predictions remain for error scoring.
Do not clip cash, add an epsilon, select a best mode or widen the decision clock.
Pure positive-headroom gating is not used: it can forbid the first profitable
trade at an uncapped starting peak. Before the PA floor cap, cash progress and
capacity retention can conflict. Once capped, the joint score always reduces
to twice cash because additional floor movement is mechanically impossible.

The matched cash-only arm separates the new transition learner/labels from the
additional floor penalty. Both also face the exact frozen V136 policy control.
Plan four retained comparisons before execution: two decision arms and their
two declared contrasts (joint versus cash-only; joint versus V136). Do not add
an unplanned coefficient or a winning fallback after observing results.

## Fixed Counterfactual Population

Authenticate the complete original V92 broad-opportunity census, including empty
dates, before known support filtering. Training preserves each product's own
initial reference-feasibility mask, plus the original MNQ PA stop <=140 mask.
Scoring retains the original NQ-feasibility guard in both phases; do not copy
that scoring-only gate into MNQ training. Count every rejected support row by
identity. Entry-gap, nonpositive actual target, nominal-ratio and
zero-capacity outcomes of supported rows are genuine zero labels, never dropped.
Each mode uses its own first timely actual product tick; NQ/MNQ may not substitute.

State anchors are deterministic account mechanics, not states sampled from
selected/terminated comparator accounts. Known-at time equals the decision.
Headroom cents are `(15625,31250,62500,125000,187500,250000)`, fixed fractions of
the 250000-cent initial drawdown capacity. The ordered grid is:

- NQ: six Evaluation states with cash 5000000 and peak `5250000-headroom`.
- MNQ: remaining PA floor-cap capacity `(260000,130000,0)`, each with the six
  headrooms. Floor is `5010000-remaining`, cash is `floor+headroom`.
- Only capped MNQ states additionally use headroom 500000, and each capped
  state is represented with both prior full-size-latch values. Uncapped states
  use the locked value. Total: 26 MNQ states, not 26 independent observations.

Uncapped PA peak is `max(cash,floor+250000)`. Capped peak is
`max(5260000,cash+1950,5262050 if unlocked else 0)`, allowing at least the
maximum six-MNQ stressed exit friction above cash and a prior close over the
unlock threshold. Capped peak selection does not change cash/floor mechanics.
Day-start cash is current cash
when unlocked, otherwise `min(cash,5260000)`: a locked state cannot assume a
prior end-of-day balance strictly above its unlock threshold. These are numerical
counterfactual anchors, NOT sampled or certified reachable whole-account states.
The grid includes idealized uncapped full-headroom boundaries above the initial
balance; exact flat-account cash would fall below a new marked peak by exit
friction. Cent/tick-lattice reachability is not asserted for every grid point.
Such anchors approximate the transition function, not a historical state
distribution or additional market evidence. Full account evaluation must use
only the actual causally realized states and original fees/guards.

Use original V136 quantity, costs, gap fills, guards, target/stop and 1R-armed
half-peak exit at each state. Record cash, floor, peak and headroom deltas, skips,
quantities and breaches; train only the cash/floor responses. The conservative
label maturity is the latest final raw-window tick across all four modes, not
the earliest state-dependent exit. Unsupported/invalid source evidence aborts;
it does not create zeros or a shortened window.

## Features, Weights And Learner

Retain all 15 V134 causal market features unchanged. Append four known state
coordinates: headroom/250000, remaining floor cap/250000, day-start MAE/75000
and prior full-size latch. The last three are zero for NQ Evaluation. Separate
product models disambiguate an uncapped Evaluation from capped PA. These
coordinates determine the single-trade cash/floor mechanics, not peak deltas,
fees, payout, activity or whole-account lifecycle.

All replicas for an event have identical market-feature bits. State coordinates
must exactly match their fixed grid identities. Native integer-cent targets
must be finite, exactly float64-representable, and have nonnegative floor deltas
not exceeding the known PA remaining cap. Impossible training labels are errors,
not repaired by the prediction projection.
The complete ordered state grid is required for each globally unique event.

Every nonempty training date has total weight one, every original event within
that date equal weight, and its replicas split that event's weight equally.
No statistical count or significance calculation treats replicas as independent.
Both scalers use these original weights. Estimator weights sum to the original
event count, not replica count, preserving regularization mass. Increase native
minimum leaf rows from 50 to `50*replicas`; a leaf cannot obtain 50-event support
merely by duplicating one event's states. Date clustering remains a separate
evaluation issue; this is not proof of independent leaf support.

Use the existing HGB numerical recipe: squared error, 100 iterations, learning
rate .05, seven maximum leaves, L2=10, no early stopping, random_state=126,
single native thread. Record all native constructor defaults, warnings and
training-only scaler states. Require at least 20 dates and 100 original events;
insufficient support is an explicit preflight failure, not a smaller fallback.

At replay, evaluate actual own-account state after busy/cooldown/day-stop checks
and before reading any entry quote. Do not use a comparator's balance. Query
the fixed HGB directly at the actual four coordinates: no nearest-state PnL
rescaling, query refit, input clipping or extrapolated linear multiplier. Record
out-of-grid-range query counts and their identities without changing treatment.
Native tree predictions outside training support are not a guarantee of accuracy.

## Temporal And Economic Evaluation

Preserve all 181 admitted development dates, the original three purged plans,
126 scored dates, full-calendar purge/embargo rules and all 48 sealed dates.
Fit only complete events whose latest label maturity precedes their training
cutoff. Never split a date, an event or its state/mode replicas across folds.
Source-bound models and complete decision-only market features must be frozen
before account replay. Dynamic state queries necessarily depend on prior
executed outcomes; the query journal must prove ordering before future entry
reads, not pretend that all state-dependent forecasts existed before the path.

Replay 12 separate account books: joint, cash-only and exact V136 controls in
all four modes. Retain NQ Evaluation -> MNQ PA, at most 1 NQ / 6 MNQ, PA limits,
original lifecycle, no daily fill-count cap, busy/cooldown behavior and all costs.
Zero capacity keeps its original resolution/cooldown treatment. No real orders.
The known zero-capacity branch must not become MODEL_ABSTAIN because a smoothed
forecast is negative: bypass model nomination for that branch, resolve the
original geometry/zero-size attempt and retain its original reason precedence.

Report date-balanced cash/floor error against training-mean controls separately
from executable PnL. The diagnostic comparator is each product/fold's global
date/event/replica-weighted training target mean, exactly its fitted target
scaler mean; it is not a state-conditional mean. Score the raw eight heads
without floor projection. Empty or unsupported-only scoring dates remain in
the calendar with null error values; averages give equal mass to each nonempty
date. State replicas are never independent observations.
Full-route success still requires baseline AND combined
stress Evaluation pass, PA entry, observed PA survival, positive PA trading PnL,
hypothetical payout eligibility and no hard/MAE breaches. Primary joint relative
benefit requires positive PA dollar differences against both controls in both
primary modes when both books entered PA; otherwise the contrast is unavailable,
not zero or passed. Unequal phase exposure must be reported. Software tests,
forecast error improvement or a baseline-only pass cannot replace this gate.

Before any market execution, finish and test the complete adapter/replay/runner,
pin the design and all dependencies, reserve the four comparisons, publish the
design and issue one immutable supervised claim. Publish only complete results.
No observed outcome permits retuning/retry, sealed-date access, Windows changes,
orders or a declaration that synthetic tests are strategy evidence.

## Immutable Execution

The runner first creates a private claim binding the original source, runtime,
code, complete calendar and four-comparison reservation. It scans the 181 raw
pairs into day-scoped immutable label files, validates the original receipts,
and retains every original event before product support filtering. Those
private intermediates are not published model verdicts. They are shared across
folds, but each fit reads only its own 45/87/129-date training prefix and obeys
the existing purged maturity cutoff. Six saved pipelines contain 48 response
estimators and 12 training-only scalers, with 132 start/completion journal events.

Only after all six models are saved does the twelve-book replay begin. The
second 181-pair scan reconciles the same raw receipts and reproduces all four
V136 control books exactly. The complete result includes all 126 scoring dates,
both primary contrasts and diagnostics, with no interim performance release.
The 325 payload/evidence files receive one create-if-absent final seal. The
unchanged V136 supervisor protocol supplies actual parent/child exit evidence
under new V137 paths; process presence or a claim alone is not completion.

A saved-result audit authenticates model bytes before deserialization,
reconstructs every training prefix without fitting, checks fixed native model
and scaler state, and recomputes every nonzero-capacity decision's raw forecasts
and all diagnostic predictions. It repeats economic and journal arithmetic
without raw-tick or account replay. Prefix reconstruction owns its admission
profiler; it must not be nested inside the replay/audit profiler. This is
reproduction under pinned code, not independent strategy validation or proof
of current Apex cohort terms. Failures retain their artifacts and trial charge;
there is no automatic retry, coefficient tuning or fallback winner selection.
