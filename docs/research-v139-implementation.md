# V139 Component Qualification

October 7, 2026. Status: COMPONENTS_QUALIFIED_NOT_MARKET_FITTED.
Read the [frozen experiment design](research-v139-design.md).
V138 remains the latest completed market study and remains a failure.

## Implemented

- `nq_apex_paired_minute_context_v139.py`: exact same-expiry 21-minute NQ/MNQ
  join, centered Last-close basis and quantity-share features, original V134
  fifteen-feature preservation, no event filtering or price imputation.
- `nq_apex_paired_minute_model_v139.py`: fixed eighteen-input own-product HGB,
  unchanged numerical recipe and weighted scalers, four unit-net-cent heads,
  native fit journaling/warning capture, finite predictions and serialization.
- `nq_apex_paired_minute_pipeline_v139.py`: complete feature-to-prefix/support
  mapping, six training-only pipelines, exact retained-control copies and
  mandatory complete-forecast publication callback. No scoring-label argument,
  market reader, CLI, account replay or source-admission authority.

The numerical integration uses invented arrays only. It fits six test models,
records 36 native fit completions and produces the complete 252 product/date
forecast dictionaries. None is a real-market fitted candidate or strategy result.

## Verification

Final affected regression: 1,517 unique cases passed, zero failures, errors or
skips; actual exit zero in 51.69 seconds. V139 contributes 247 cases: context107,
model107, pure pipeline32 and native integration1. The other 1,270 cases cover
the reused V123/V126/V127/V129/V134 feature, population and numerical paths.
Sixty-seven synthetic warnings remain visible: 64 scaler arithmetic warnings
and three prior MLP convergence warnings. No market warning count is inferred.

Runtime: Python3.14.3, NumPy2.5.2, scikit-learn1.9.0, the existing qualified
research environment. JUnit evidence is
`reports/nq_apex_v139_component_qualification_20261007/affected-regression-v3.xml`,
SHA256 `1b9b62bb9c90bee2b45bd26f513f02af8884b97485440987c7e4659f9c724105`.
The qualification JSON binds all eight new design/source/test files. All 259
previous V138 loaded dependency hashes were independently rechecked unchanged.
No old frozen source, test, model, reservation or completed outcome was edited.

Independent review found and confirmed fixes before market work:

1. A single-event test did not prove nonempty V134 history preservation. Three
   alternating-side events now retain unsupported/unfilled predecessors, exact
   fifteen-feature bits and event order; later MNQ changes cannot affect earlier
   decisions.
2. Rehashed population metadata could declare incompatible target units or
   support. Exact one-contract cents, no quantity scaling and original NQ/MNQ
   stop support are now required before the first fit.
3. Positive weights alone did not prove date equality. The adapter now checks
   the exact original 1/count-per-date weights.
4. Array lengths could agree despite contradicting declared population counts.
   Exact native retained-event/date counts are now reconciled before fitting.

The first affected run had 1,506 passes and one test-harness failure: a native
integration test inherited the pure-adapter ban on estimator fitting. Native
testing moved into a separate invented-data test module; the pure guard was not
weakened. The next 1,507-case pass preceded the three additional population
checks; the final 1,517-case run above supersedes it. Two earlier collection-only
attempts used the repository's unrelated `.venv`, which lacked the tools import
path and then scikit-learn; neither executed market work or justified changing
the qualified runtime.

This is the complete affected component regression, not the full repository
suite. The previously documented broad-suite failures are not waived or claimed
fixed. No full-repository green status is asserted.

## Required Next Work

The goal is still a full economic comparison, not merely a tested feature.
Before any market feature extraction or fit:

1. Authenticate exact saved V134 fifteen-feature contexts/forecasts, original
   V129 own-product populations and four saved V136 giveback account controls.
2. Restore the existing paired minute inputs under unchanged source/config and
   development-calendar bindings. Reconcile every original event and same-expiry
   NQ/MNQ window, without opening the 48 sealed dates or filtering failures.
3. Implement and qualify the complete prediction, four-new-account replay and
   no-fit saved-result audit runner. Publish outcomes atomically only after all
   forecast and account results exist; never expose partial economics.
4. Publish/freeze the executable plan and reserve its five comparisons before
   the one supervised market attempt. Planned count13,267 to13,272 is NOT charged
   yet; current effective count remains13,267.

No market feature extraction, fits, new account replay or economic result has
occurred for V139. No threshold was relaxed. No Windows, schedule, Telegram,
order, spending, source admission or holdout permission was changed. Research
and Windows/model-operation goals remain active and incomplete.
