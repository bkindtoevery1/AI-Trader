# V118 Complete Pure Pipeline

`tools/nq_apex_distribution_pipeline_v118.py` coordinates the already qualified
plan, population, forest and distribution-envelope components. It does not
admit external bytes, claim a run, perform raw execution, replay accounts,
publish files or calculate economics. Market-fit authorization and durable
callback persistence remain the caller's responsibility.

## API

```python
run(source, full_calendar, plans, populations, *, on_stage, on_model)
```

`source` is the original admitted source dictionary, not a nested prepared
object. `plans` and `populations` are native lists of exactly three ordered
plans and `PreparedPopulation` objects. `full_calendar` is a list or tuple of
the same 181 dates. Both callbacks must be callable.

The native-JSON return record contains:

- `fits`: three complete fitted wrappers in fold order.
- `distributions`: all 126 scoring dates in chronological order, including
  empty dates, with the account adapter's exact distribution envelope.
- `model_fits=3`, `tree_count=192`, `scaler_fits=0`, `source_model_fits=0`.
- `fit_stage_count=9`, `distribution_days=126`.
- `source_identity_sha256` and the ordered three-item `plan_sha256` list.
- `distribution_sha256_by_date`, `distributions_sha256`, `pipeline_sha256`.

`pipeline_sha256` hashes the complete record excluding that field itself.
There is one distribution calendar, shared by both new policies; the pipeline
never constructs arm-specific fits, labels, headroom or quantities. JSON-native
output containers remain ordinary dictionaries/lists. Their recorded hashes
pin their contents, and the replay performs its own detached snapshot.

## Validation Boundary

All supplied inputs are detached before callbacks. Every plan must exactly
match the original source fit. Every prepared population must pass the plan
validator and bind the same complete source identity. The pipeline additionally
reconstructs all three training prefixes with the qualified `prepare` function
and compares their population/binding metadata before the first fit. Rehashed
but substituted training arrays therefore cannot establish source membership.

Every scoring-day event, causal nine-feature vector, original MNQ forecast
identity, four finite heads and null-support contract is checked before fitting.
The complete daily event-count times training-row-count must satisfy the
existing two-million-cell bound. No future current-day label becomes a query
feature. Initial support is unchanged; negative original heads do not block
the forest, and stop-limit or original support exclusions retain null masses.

The training-prefix checks intentionally retain the qualified preparation
function, including its full source-identity validation. Inference avoids 126
whole-source copies: it uses the privately cached, prevalidated day inputs and
the unchanged forest `distribution` function. Every resulting daily envelope
passes the unchanged account `validate_distribution` contract. Synthetic
boundary/empty-day tests compare these envelopes with the qualified standalone
`day_distribution` builder. Private source identity is checked again after
fitting and after inference; fitted wrappers are revalidated before return.

## Callback Order And Failure

For each fold, `on_stage(fold, stage)` receives these strings in order:
`estimator_started`, `estimator_completed`, `model_completed`.
After all three stages and full fitted-wrapper validation,
`on_model(fold, deepcopy(wrapper))` runs before the next fold starts.

The pipeline holds no profiler or no-fit guard around either callback. The
parent may enter its own `_no_fit_calls()` guard inside `on_model`. Mutating the
callback wrapper or the caller's original source/plans/populations cannot
change private inputs, fitted records or later folds. Callback exceptions
propagate immediately: no retry, fallback, later fit or partial return occurs.
Durably published model callbacks may exist on failure; they are not a
complete returned pipeline result and contain no account economics.

Only synthetic source fixtures and synthetic sklearn fits are used in the
focused pipeline tests. Neither this implementation nor those tests claim
source admission, market performance, independent observations or independent
raw-fill verification.
