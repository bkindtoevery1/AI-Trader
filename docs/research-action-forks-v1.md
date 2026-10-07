# Same-State Action Forks

October 7, 2026 UTC. Pure research implementation. No admitted market pair,
fitted strategy, profitable result, Windows recovery or deployment permission.

## Question And Mechanism

The [observed continuation targets](research-sequential-targets-v1.md) cannot
identify the action not taken. This component instead simulates two paths from
the same original V137 account, forcing exactly one eligible decision to
`ABSTAIN` or `ATTEMPT`, then returning to the same behavior predictor. An attempt
is not a guaranteed fill: original geometry, risk limits and cooldown still
apply. Unsupported, busy, day-stopped and zero-capacity targets fail explicitly;
they do not receive invented flat labels.

`tools/nq_apex_action_forks_v1.py` privately rebinds only the original nomination
hook and exact-account class guard. The original daily execution, V136 giveback
kernel, costs, adverse fills, phase routing, sizing, five-minute cooldown,
Evaluation resets, PA activation, payout bookkeeping and terminal rules remain
the actual execution path. Predecessor modules/classes are not patched.

The original eight predictions, projected floors and behavior nomination are
retained truthfully. The applied nomination is separately marked as an explicit
intervention at one event. No positive or negative fake cash/floor prediction
is used to coerce the legacy interface. Later decisions query the predictor
with that branch's own evolving state, not scaled PnL or the other branch's
balance. This is a single-deviation return under a fixed continuation policy,
not an optimal Q function or full reinforcement learning.

## Inputs And Atomicity

The caller supplies an idle original account, one through63 ordered `DayFrame`
objects, the entire declared calendar, a target event on its first date, one
behavior callback, product-specific model/population bindings and a training
cutoff. All declared dates must be on or before June12,2026, preserving the
current development fence. Every full17:00ET endpoint must mature strictly
before the training cutoff. The target cannot be chosen from future dates in
the same call. Caller-owned source admission and a frozen study must additionally
define the event/state census; this API does not prevent outcome-informed
selection across calls.

Frames, static event/session inputs, calendar and bindings are detached. The
starting account is held in the existing in-flight dispatch state during the
operation and restored afterward. A callback mutation, reentrant invocation,
unavailable target or second-branch failure returns no partial pair and restores
the original account. The two branches must reach exactly matching causal
pre-action snapshots, completed market anchors, behavior predictions and prefix
journals. Future entry prices are not part of that fork input.

Identical product/event/state queries must give identical behavior predictions.
Identical requested source windows must hash identically across branches. These
checks expose inconsistent callbacks but do not authenticate model artifacts
or prove that branch-only windows came from one immutable market tape. The
research runner must still authenticate those exact dependencies; the output
explicitly retains `source_admitted=false`.

## Responses

Each branch contains its complete original account report and subsequent
decision observations. Return starts at the intervention, excluding earlier
same-day or historical profits. Immediate and continuation trading PnL sum to
the finite-horizon return after modeled trading costs. Account cash changes and
hypothetical withdrawals are separate, so resetting Evaluation or entering PA
cannot fabricate a trading gain or loss.

The paired advantage is `ATTEMPT return - ABSTAIN return`, not the immediate
attempt's PnL. The label is available only when both paths have matured. An
absorbing terminal can finish a branch early; the entire declared calendar is
still required and checked, avoiding terminal-only availability selection.
Purchase/renewal/activation charges are still unpriced. Overlapping pairs are
not independent observations and must not be summed as an executable strategy.

## Remaining Study Design

A usable model still requires causal feature projection, an authenticated
complete training census, date-balanced fitting, a frozen learner/nomination
rule and whole-account out-of-sample execution of that learned rule. Applying
several learned deviations changes the state distribution; success of isolated
fork labels is not proof of that new policy's performance.

Behavior-policy chronology is a separate limitation: a saved predictor trained
on a45-date prefix cannot generate causally admitted behavior on those same
earlier dates. The binding cutoff check rejects that shortcut. A concrete study
must supply an earlier admissible behavior policy or explicitly preregister a
different nested chronology. Neither a new horizon nor a new split is selected
by this component. Existing failed studies and all48 sealed dates remain closed;
no market trial, fit or comparison reservation is created here.

## Verification

Final parent result: **986passed**, exit0,11.42s. This includes206new independently
authored fork cases and780existing target/trace/account cases. JUnit independently
contains986unique cases with no failures, errors or skips. Actual parent tool
session60510 is terminal; overlapping earlier invocations are not added.

Coverage includes both phases/arms/sides and all cost/latency modes; exact
matched-action comparison with the original account; real own-state continuation;
giveback exits; busy/support/day-stop/zero-capacity rejection; geometry cooldown;
prior-reward exclusion; actual Evaluation-to-PA and hypothetical payout paths;
Evaluation reset versus PA breach/inactivity; causal model/label cutoffs; source
and same-state forecast consistency; first-day target and complete-calendar
admission; detached future inputs; callback mutation/reentrancy and second-branch
rollback; truthful original predictions and exact predecessor namespace identity.

Initial independent and parent runs each had205passed/1failed because the
namespace audit captured Python's lazy `__slotnames__` cache too early. A
standalone reproduction, without importing the fork module, confirmed that
ordinary deepcopy creates only that empty cache and changes no existing member.
Warming only the original control first exposed the same issue on the traced
control. Both controls are now warmed before capture; every namespace member
still receives the exact identity check. No implementation guard was removed.
The failed parent session38353 JUnit remains at
`reports/nq_apex_action_forks_20261007/affected-final.xml`, SHA256
`d9b38c1463ffcaca47da53e11f24f71db73be7229917e130347c728f677fabdd`.
Despite its filename, that is failed evidence, not the final qualification.

- Source SHA256: `0489899cb93793fc7e39c86e8df685f1157998baec2e239a95dbe283388d1425`.
- Test SHA256: `084ae075d2d4a667a2270f0a1a14e5c13319de1df4ca6d13cb6507b4bc9fb8a1`.
- Qualified JUnit: `reports/nq_apex_action_forks_20261007/affected-qualified.xml`.
- Qualified JUnit SHA256: `094ecd34cb9bb7dd82f7bad78248ca463ff7e0ca790ee7cc179cc95cc8bfe83a`.

The full repository regression was not run. Original trace/target/V137/V136/V87
account and Windows files have no task edits. No real market pair, new fit,
market replay, comparison charge or holdout access occurred; total remains13,293.
Windows still has no new execution or authorization evidence from this work.
