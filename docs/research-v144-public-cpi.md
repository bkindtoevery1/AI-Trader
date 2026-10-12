# V144 Public CPI Ablation

## Scope Frozen Before Fitting

October 12, 2026 user scope: Mac research only, no Windows connection work.
Hypothesis: inflation level and the age of the last known release can improve
own-product conditional payoff forecasts beyond V134 price, minute-volume and
prior-event features. This is an outcome-informed development experiment, not
independent validation, a deployable strategy, or an Apex pass.

Use US BLS archived CPI-U all-items 12-month unadjusted percent only. Original
release excerpts are retained with source URLs in config/nq-apex-public-cpi-v144.json.
They are web-tool extracted text retrieved now, NOT original HTML/PDF bytes,
contemporaneous feed receipts, or proof of intraday live availability. Excerpt
hashes bind retained content, not remote provenance. BLS material is public
domain: https://www.bls.gov/opub/copyright-information.htm.

Ten releases cover July 2025-May 2026 reference months excluding October 2025,
which was not published due to the government shutdown. Actual embargo clocks
are parsed as America/New_York, including DST. The fixed simulated availability
is release time plus 60 seconds. Latest known CPI and elapsed days since its
release are appended to the original 15 features. No backward fill, revised
values, interpolation, consensus surprise, or inferred monthly release dates.
No prior release or an age over 90 days is an error, not zero inflation.
GMD is excluded due to its research-use license; unemployment is deferred due
to incomplete primary-source release retrieval, not performance selection.

Reuse the original 181-session, 5,485-event development population ending
2026-06-12. Three expanding folds: initial 45 training sessions, 10-session
purge, 42 scored sessions each (126 total). Keep original support, product
labels, cost/latency/stress modes and date-equal weights. No sealed holdout.

Fixed V134 HGB recipe, 17 instead of 15 features. Two product candidates,
NQ and MNQ; six pipelines, 24 response estimators, 12 scalers. Reuse and
reproduce the original V134 forecast control rather than refitting it. Four
counted comparisons (two product candidates plus two paired contrasts), from
13,294 to 13,298, reserved before any market fit. No threshold, window,
hyperparameter or policy search, retry after partial fitting, account replay,
position sizing change or economic pass claim. V143's reservation is retained.

Primary descriptive diagnostic: date-equal MSE of net own-product cents for
each of four modes; secondary MAE. Report all products, folds and modes, not
only favorable slices. Forecasts must be persisted before scoring labels are
attached. Results do not imply profitable trade selection or PA survival.
Only ten macro releases exist; thousands of intraday rows do not supply
thousands of independent inflation observations. No significance or causal
claim; no automatic promotion based on this ablation.

## Execution

Pending. Run focused regression before reserving and fitting. Preserve source,
design, dependency, control, model and forecast hashes in the run artifacts.
