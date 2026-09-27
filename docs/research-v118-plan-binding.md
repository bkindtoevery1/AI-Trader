# V118 Pure Plan And Population Binding

`tools/nq_apex_distribution_plan_v118.py` adds no admission, claim, raw-data
loading, account replay, publication or comparison charge. External byte and
native original-model authentication remain the caller's responsibility.
Synthetic fits exercise software only, not the research hypothesis.

## Interface

- `plans(fits, full_calendar)` returns three detached MNQ plans. Accept exactly
  three MNQ or six NQ/MNQ original fit references, with folds ordered within
  each product. Each original reference retains its entire hashed model.
- `prepare(source, plan, full_calendar)` returns `PreparedPopulation`, with
  `.plan`, `.population` (the V118 `UnitPopulation`), `.source_fit` and
  `.metadata`. `validate_prepared(data, plan)` performs validation without a fit.
- `fit_prepared(data, plan, *, on_stage)` returns a JSON-native fitted wrapper.
  Its fields are `schema_version`, `plan`, `population_metadata`, `forest`,
  `source_fit_sha256`, `source_model_sha256`, `source_identity_sha256`,
  `source_binding` and `fitted_sha256`.
- `validate_fitted(record, plan)` validates without refitting;
  `restore_fitted(record, plan)` additionally returns a detached copy.
- `prepare_day(source, plan, day, full_calendar)` returns original nine-feature
  coordinates, event IDs, decision clocks and identity metadata for every event.
- `day_distribution(prepared_model, source, day, full_calendar)` returns the
  account adapter's exact JSON envelope: `model_sha256`, `population_sha256`,
  `unit_net_cents`, `events`. Each event contains only `event_id`,
  `decision_end_ns` and `probabilities`.

`model_sha256` in that envelope is the exported forest's hash, not the fitted
wrapper's hash. `population_sha256` is the V118 population metadata's
`inputs_sha256`. Forest outcomes are validated as exact integral cents before
conversion to native JSON integers. Negative original MNQ forecast values do
not suppress forest queries. A probability vector is absent exactly for
stop>140, initial NQ capacity zero, or original MNQ null support. All other
source events receive normalized leaf-outcome masses, with the unchanged full
event census. The complete daily row-count times training-row-count must not
exceed the existing two-million-cell bound. Empty dates retain the training
outcome table and return an empty event list.

## Causal And Identity Checks

Plans carry the complete 181-date calendar and its hash so restore validation
can verify the exact 45/87/129 training prefixes, ten full-calendar purge dates
and 42 scoring dates without an external calendar lookup. Label maturity is
strictly before purge-start 09:00 ET in all modes, including subsequently
filtered rows. Exact original source-fit and embedded model digests are both
bound. First-fold embedded chronology and later scaler/bundle date membership
are checked without rerunning original learners or runtime byte admission.

Preparation verifies the original `prepared_identity(source)` over the entire
provided source. This includes hashing future supplied records for identity;
it does not interpret them as targets. Only the exact training prefix is
passed to original population validation and the V118 unit-label adapter.
Original scaled features, reference-quantity dollar targets, date weights and
available complete-label receipts must match the original fitted-model
receipts. Those original targets are used only for reconciliation: the new
forest receives actual one-MNQ net cents, with post-filter date-equal weights.

The forest's `source_binding` hashes the plan, V118 population identity, whole
source identity, original fit digest and original model digest. All these are
identity checks, not a declaration of external source authenticity. Restored
wrappers validate their exported forest and reconstruct the population hashes,
closed static flags, integral targets and causal calendar without fitting.
Day queries additionally bind the wrapper back to the supplied source and
validate the complete original MNQ forecast row identity, finite heads and
null-support contract. No NQ Evaluation prediction, current-day label, account
state, headroom, quantity or future execution tick is a query feature.

## Fit Callbacks

The stage observer receives exactly these strings in order:
`estimator_started`, `estimator_completed`, `model_completed`. The caller owns
durable storage and authorization. Callback failure propagates without a
partial returned model. Plans, source-fit references, arrays and metadata are
detached before the first callback, so mutations to caller objects cannot
change the fit or its binding. No original scaler or estimator is refitted.

The focused test file uses invented source receipts and synthetic sklearn
training only. It checks exact fold boundaries, source/population/model
closure, per-mode maturity before filtering, callback isolation, stage failure,
restore without fit, original feature/event preservation and compatibility
with the parent account's distribution validator. There is no claim of
independent raw-fill or market-outcome validation.
