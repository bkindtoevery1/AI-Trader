# V111 Component And Source Qualification

2026-09-13 UTC. Components and actual source-array integration are implemented;
the full market runner, preoutcome lock, claim, fits and account replay are not.
Latest completed historical experiment remains V110 and the ledger is13181.
Neither a profitable model nor a verified50K route is claimed.

## Implemented

Read docs/research-v111-design.md and config/nq-apex-event-order-v111.json.
tools/nq_apex_event_path_v111.py authenticates the existing completed21-bar NQ
anchor and produces signed OHLC coordinates in original stop units. Whole-row
canonical sorting provides a matched order-erased predictor without changing
event identity, source execution geometry, existing volume coordinate or labels.

tools/nq_apex_event_order_v111.py fits two176-parameter GRU/readout models with
the same initialization, training-only transforms and128fixed epochs. It accepts
already authenticated/scaled original context; it does not claim to authenticate
source data, own purge decisions or run an account. It returns a complete paired
artifact only after both fits and their stage notifications succeed. No outcome,
checkpoint, seed, architecture or runtime selection occurs inside this module.

The separate CPU environment is
<HOME>/.local/share/ai-trader/runtime/v111-20260913.
It uses CPython3.14.3 and exact Torch2.14.0, with requirements recorded in
config/nq-apex-event-order-v111-requirements.txt. Native model size176 and
`pip check` passed. Use PYTHONPATH=src:tools; no editable project distribution
was installed here. Existing V102 and default runtimes were not modified.

## Verification

Final focused exec95474 completed actualexit0:148passed, no failures or skips.
The source-path worker's109cases are included, not added a second time. Tests
exercise invented fixtures only; their neural fits are not market trials.
Final-focused XML is in reports/nq_apex_event_order_v111_implementation.
The full regression exec66358/PID43879 completed11:12:34Z, actualexit1:
15834passed,2failed,1skipped across15837distinct testcase nodes. All148 V111 cases
passed. Compared with the V110 corrected full run, two Windows state checks
from the preceding commit also passed and22 prior neural-test skips now passed
in the new runtime. Raw case-ID comparison additionally shows two old and two
new names for passing KIS ZIP fixture checks: their parameter IDs include ZIP
bytes generated without a fixed timestamp. Do not claim all raw IDs are stable
or rewrite the XML to make that true. The raw suite header says15926,
89more than actual testcase nodes, the same header/node difference as the prior
full XML. Count actual nodes and retain the original XML without rewriting it.
Read verification.json and regression-delta.json in the implementation reports.

Both failure IDs AND messages are unchanged: the historical account-transition
test compares four candidate objects with six charged comparisons, and the
V88 completion test references a missing older temporary XML. The suite is not
all green. Do not fabricate that temporary report or treat these software
failures as negative strategy returns. No required process remains running.
After updating central state, its17-case suite completed actualexit1 with16pass
and the same V88 missing-XML failure. checkpoint.json preserves the current
V111 progress, unchanged Windows installation boundary and seven source pins.

An independent component reviewer found two numerical/runtime defects. Both
were fixed before the final148-case run and before full regression started:
exact constant decimal channels with unequal date weights now use original
means, zero variance and unit scale; model construction and state restoration
explicitly request CPU even when a different default device is ambient.
All seven implementation scope files remain fixed during the full run.

Actual source preflight v2 completed10:57:11Z against3067 admitted dependencies,
the completed V107 repair comparator and the original V102 source preparation.
Three populations contain1430/2670/3899 events across45/87/129 training dates.
Every event's new21-by4 array aligned with the original retained row ID and
unchanged original scaler, nine coordinates, four dollar targets and date weights.
No new market estimator/scaler fit, scored candidate prediction, raw replay or
account replay occurred. The source preflight's separate raw command exit was
not retained; successful report publication is not fabricated into an exit code.
Report SHA256:
eccac8734311f179264baec1dba253ba955a916ab6fda1accaecfea22c8310cb.

The first preclaim harness attempt failed at10:48:08Z because the caller nested
the non-reentrant no-fit guard already owned by `admit()`. Preserve its failure
receipt. The corrected harness calls unchanged `admit()` directly, guards the
subsequent population construction separately and forbids learner.fit_pair.
This caller-integration mistake had appeared in earlier research too; component
fixtures alone did not catch it. Reuse the actual admitted source interface in
the next runner instead of copying a nested-guard pattern. This was not a model
loss or permission to rerun a claimed economic experiment.

## Remaining Work

Implement and test the caller-owned source/coordinate bindings, paired fit-stage
receipts, per-fold forecast artifacts and12 continuous account books. Authenticate
actual source semantics and the completed reference before a separate immutable
claim. On that claim, charge the frozen two policies plus two primary contrasts,
13181to13185; do not charge component tests or this input-only preflight.

All four unchanged controls and NQ Evaluation prefixes must reproduce. Reveal
new economic results only after the complete terminal experiment. Do not rerun,
retune or select a diagnostic cost/latency mode to rescue primary results. Keep
48 historical holdout dates closed, actual fee/cohort uncertainties disclosed,
and the fixed Windows V102 artifact unchanged. The new learner does not repair
or replace the still-uninstalled Windows collector. No source install, F5,
activation, service, schedule, order or Telegram action occurred in this work.
