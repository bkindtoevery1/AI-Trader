# V140 Training And Matched Diagnostics

October 7, 2026. Implementation and synthetic qualification, not a market result.
The [frozen design](research-v140-design.md) and original V139 files are unchanged.
There are no new market labels, fits, account replays or reserved comparisons.
Effective historical trials remain 13,272; the 48 sealed dates stay closed.

## Training Boundary

`nq_apex_giveback_unit_pipeline_v140.py` validates all six separately bound V140
target populations before its first native fit. External manifest pins bind
the new targets; separate sealed V139 pins bind all eighteen feature floats
and original-target control predictions. Self-generated content hashes do not
replace those authenticated source artifacts.

The original Prepared y and provenance remain untouched. IDs, date-equal
weights, train/purge/scoring calendars, query masks and model recipe stay exact.
Only new training-prefix y reaches the same V139 HGB/scaler implementation.
Actual fit arrays are byte-backed and irreversibly read-only. Mutable callbacks
receive detached records; mutations of original inputs or publication payloads
are detected. Failures propagate without retries or a partial forecast result.

Six pipelines mean 24 response fits and 12 scalers. A training-only weighted
mean is a diagnostic arm, not another fitted or traded candidate. All 252
candidate product/date forecasts, exact V139 controls and mean diagnostics must
be published together before scoring. The fit API has no scoring-label input.
The caller still owns exclusive reservation and durable publication authority.

## Same-Target Scoring

`nq_apex_giveback_unit_diagnostics_v140.py` consumes only the 126 scored dates
after authenticating the complete published forecast content. Its day reader
must verify the real extraction-manifest/file pins. The diagnostic separately
checks the whole original census, new unit-label role, policy, product, modes,
integer cents and journal arithmetic, including unsupported opportunities.

Candidate, sealed V139 and training-mean forecasts are scored against the SAME
new giveback unit targets and support. No scoring outcome recomputes a training
mean or fits any model. Date-equal MSE/MAE use the existing arithmetic, preserve
empty dates and folds, and reject overflow/nonfinite results. Selected labels
can overlap and remain explicitly not account PnL. A failed late day returns no
partial result; the module has no publisher, market reader or order interface.

## Verification

The 820-case affected regression completed with exit zero, no failures, errors
or skips. This includes 62 new pipeline/native/diagnostic cases, the prior 186
V140 label/population cases and 572 predecessor feature, learner, journal,
source, population and giveback-account/audit cases. The eleven warnings come
from retained V139 synthetic numerical-edge tests, not a market fit.

The actual-native synthetic integration runs all 36 scaler/estimator fits
through the existing immutable V139 journal, writes six real model artifacts,
verifies all 84 journal events and restores every model from authenticated
bytes. It reproduces all 252 candidate predictions without refitting. Scaler
means are checked against new prefix-only targets with the original weights.
No real market data, account outcome or production source was used in this test.

JUnit: `reports/nq_apex_v140_integration_qualification_20261007/parent-regression-v1.xml`.
SHA256: `e4c365d029adb9f92fc07fbe7f4e3ba1ce599525994d1ae820a5f3d7e5f0d5ec`.
All 16 V139 own pins and 261 loaded dependency pins were checked unchanged.
This is a full affected-component regression, not a new all-repository pass.
The prior repository-wide audit's 13 remaining case identities are unresolved.

## Completion Boundary

The later [execution integration](research-v140-execution.md) implements the
authenticated source/label cache, four-book replay against exact V139 controls,
supervisor, atomic result and no-fit saved-result audit. Its own complete-path
qualification must finish before reservation or real execution. This earlier
820-case component checkpoint alone is not execution authority. A successful
test suite is software evidence, not profitability or an Apex pass.
