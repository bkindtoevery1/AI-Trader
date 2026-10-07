# Continuation Learner And Causal Support

October 7, 2026 UTC. Outcome-informed research implementation, not a market
fitted strategy, independent validation, new Apex pass or live signal service.

## Actual Chronology And Support

A read-only audit verified the closed V137 fast result seal, claim, status,
account and model metadata, plus both first-fold model-file bytes. It did not
deserialize a model, make an inference, regenerate a label or open raw ticks.
The exact audit and hashes are in
`reports/nq_apex_continuation_support_20261007/audit.json`. This is selected-byte
verification, not a fresh full source-restoration qualification.

Those predictors trained on45 dates, September8 through November14,2025, with
cutoff1763388000000000000. Their first recorded scored queries start December3.
They cannot causally generate a roll-in on their earlier training dates. In
the32-date December3,2025 through January23,2026 prefix, every audited decision
matches its actual product model, population identity and native earlier cutoff.

The cash-only roll-in supplies11 NQ and21 MNQ nonempty dates in every mode;
the cash-plus-headroom roll-in supplies32 NQ dates and no MNQ dates. Neither
alone supports a20-date learner for both products. Their union supplies32 NQ
and21 MNQ dates, before exact state deduplication and new pair admission:

| Mode | NQ Events | NQ State Rows | MNQ Events/Rows |
| --- | ---: | ---: | ---: |
| Baseline | 928 | 1,204 | 540 |
| Cost only | 928 | 1,205 | 544 |
| Latency only | 927 | 1,203 | 528 |
| Stress | 928 | 1,203 | 532 |

These are old reachable-query counts with positive planned capacity, not new
counterfactual labels, guaranteed fills or independent samples. Later teacher
chronology and a complete new paired population are not yet qualified. The
original45/87/129-date fits each have ten purge dates and42 scored dates; this
audit does not silently move those dates or register a new student split.

## Fixed Continuation Adapter

`tools/nq_apex_action_forks_v2.py` separates the original roll-in arm from an
explicit continuation arm. Both actions retain the original pre-decision state
and forecasts, then use the same chosen nomination arm after the single forced
action. This permits different causal origins without giving them different
continuation objectives. It changes neither the bound forecasting model nor
direction, quantity, fills, costs, risk guards or lifecycle.

The exact V1 functions are privately rebound per call; V1 source bytes and
module globals remain unchanged. V2 has a distinct scope/schema and explicit
roll-in/continuation fields. Same-arm use remains economically identical to V1.
Cash-only is the supported active-continuation design option, not a promoted
winner: the predecessor still failed full-route economics. No market run or
post-result choice of continuation arm is made here.

## Implemented Learner

`tools/nq_apex_continuation_model_v1.py` implements four separate HGB response
heads per product. Each head receives its own mode's actual state-dependent
rows. It does not falsely align different account states into one common
four-target row. At prediction, all heads evaluate the same supplied current
state and return four raw expected advantages in cents.

The31 inputs are the original15 market features; six causal EntryState fields;
known prior phase trading days and current-day trade count; and the original
eight behavior-model forecasts at that state. The response is the paired
finite-horizon net trading return of ATTEMPT minus ABSTAIN, not an isolated
trade, account reset, withdrawal or optimal Q value. The caller must supply
authentic known counters and forecasts; a numerical matrix is not their proof.

Every head requires at least20 nonempty dates and100 distinct original events.
Each date receives unit weight, split equally among its events and then among
at most two distinct causal states per event. All four populations are validated
before any native fit. Events must retain the same market features, date and
clock across states/modes; behavior artifacts retain one causal cutoff. Labels
and the full declared calendar must mature strictly before fitting.

Use the established fixed HGB recipe:100 iterations, learning rate.05, seven
leaves, L2=10, random state126, no early stopping and one native thread. Minimum
leaf rows are100, preserving a lower bound of50 original events with at most
two state rows each. Each head has its own date-weighted feature/target scalers;
one product therefore performs four estimator and eight scaler fits. No
hyperparameter search, horizon selection or adaptive threshold is implemented.
Metadata retains exact feature order, parameters, native warnings, population
counts, training-only means and scaler states.

## Remaining Market Work

This is a usable learner API, not a completed experiment. Remaining work includes
the authenticated source/state-to-pair adapter, complete causal counter/census
reconciliation, deduplication and group weighting, explicit student chronology
and horizon, numerical/runtime pinning, comparison reservation, supervised
market fitting, policy integration and full account-path evaluation. Changing
several future actions changes the distribution; paired labels do not certify
the learned policy. Do not choose a horizon, split, arm or product after seeing
its economic result, or train only the terminal subset of a censored horizon.

All48 sealed dates remain closed. Historical effective trials remain13,293.
There is no Windows restart, new signal, Telegram request, order or account-fee
verification from this research work. Synthetic test fits are software evidence
only and must never be reported as model performance on market data.

## Verification

Final parent qualification passed 1,116 distinct affected cases, exit 0, in
14.16 seconds. It includes 54 V2 fork cases and 76 learner cases, plus the
unchanged fork, target, trace and account suites. Independent author results
overlap these cases and are not added. The learner tests perform real sklearn
training on synthetic rows, verify per-head weights/scalers, warning handling,
chronology, aliases, invalid populations and raw predictions. Metadata now uses
the same complete-model validation as prediction, including invalid product,
head count and head type rejection. The final run includes that regression.

Final JUnit: `reports/nq_apex_continuation_support_20261007/affected-metadata-qualified.xml`.
Its SHA-256 is
`a5dd5be268425feb24c7a1dbcd75b2ef58ead288d467d42d97b9113576501664`.
The earlier 1,116-case run remains separately preserved; it preceded the shared
metadata-validation improvement and is not the final-source qualification.
Full repository regression was not run. No market model was fitted or evaluated.
