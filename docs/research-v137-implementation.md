# V137 Training Components And Remaining Integration

October 6, 2026. Status: IMPLEMENTED_COMPONENTS_NOT_MARKET_FITTED. The
[design](research-v137-design.md) specifies the proposed complete experiment;
this record does not authorize or imply that its remaining stages ran.

## Implemented

- `tools/nq_apex_transition_population_v137.py`: fixed six NQ / 26 MNQ state
  anchors, four causal state coordinates and complete event-grid validation.
  Each date has equal mass; replicas split their event's mass.
- `tools/nq_apex_transition_model_v137.py`: 19-input, eight-response HGB;
  date-weighted training-only scalers, original-event regularization mass,
  replica-adjusted leaf size, warning journals and no early stopping. Native
  synthetic fits and joblib restore/prediction roundtrips were tested.
- `tools/nq_apex_transition_labels_v137.py`: complete ordered prefix/census
  checks before support selection or tick callbacks, both first-entry windows,
  same-contract/provider-order suffix verification, full-window maturity and
  counterfactual state/mode labels through the unchanged V136 kernel. Source
  authenticity and independent original-census admission remain caller-owned.

The label adapter retains empty dates, explicit support-exclusion records and
genuine zero transitions. It does not count rejected/missing data as flat
trades. It prevents dropping one event or state while calling the result a
complete supplied census. A caller supplying two identically incomplete maps
still needs independent source authentication; hashes are not provenance.

## Review Corrections Before Market Execution

The test agent's initial 259 passes / two failures exposed a missing prediction
row-count check. A malformed estimator could return a different batch length;
this now fails before scores are produced.

Independent design review identified impossible PA floor penalties and overly
strong state-reachability wording. Decision scores now require current states
and bound predicted PA floor increase to its known remaining capacity, exactly
zero at the cap. Raw forecasts remain unchanged for error measurement. Training
labels exceeding that cap are rejected, not clipped. Capped peak representatives
now allow exit friction, and the design explicitly identifies idealized numerical
boundary states rather than claiming observed/reachable account histories.

These corrections preceded market labels or fits; they are not changes made
after seeing a candidate's performance. Uniform state anchors do not estimate
the historical distribution of account states. Only the later continuous
actual-state account replay can establish executable economics.

## Verification

Final combined run: 861 passed, zero failures/errors/skips, 16.426 seconds,
actual exit 0. This comprises 295 new population/model/label cases, 172 unchanged
transition-target cases and 394 existing V134/V136/V87 cases. Earlier runs
overlap and are not added again. This is focused/affected regression, not a
full-repository green claim. The previous stage's 929-pass count is separate
and overlapping. All nine frozen V136 pins and original V137 target bytes remain
unchanged. Tests use invented prices/states, not strategy evidence.

JUnit SHA256: `da7bc929027bcd8f5a43acf072b39883ea7956220319044d9be40c2a7969288d`.
Population SHA256: `6cdf5b48b8bbf63881b4125ae3008296380b402aec84528748c05e4ae576da49`.
Model SHA256: `2b687794f5c79f812a26c74c19bcf7d1cd033a53330d83f0719fe4091d1c0692`.
Label adapter SHA256: `d03a7f169957e754daebda4c3e015e7e8199581f7dd506e7645a68b2bbce215f`.

## Next Required Work

1. Connect the source/fold/account components below into a day-scoped raw-label
   cache, six saved fitted pipelines and twelve-book replay. Reuse identical
   event labels across nested folds, not duplicate market observations. Keep
   raw-window receipts, maturity and original-event census bound throughout.
2. Add V137-aware full-route account summaries, the two declared contrasts,
   date-balanced forecast diagnostics and saved-model/result audit. Do not
   relabel V137 books as old V136 policies to pass their identity validators.
3. Finish the immutable supervised runner; preflight the full path, pin and
   publish its dependencies, reserve the four planned comparisons, then fit
   and replay once. Publish only complete results and retain failures rather
   than tuning against them. The source-only preflight below is not this gate.

Verified existing metadata contains 5,485 original opportunities / 181 dates,
training-prefix counts 1,430 / 2,670 / 3,899 and 3,747 scored opportunities.
Those are not trade counts or independent observations. Before support, a full
label construction would have at most 702,080 state/mode transitions; the nested
training union has at most 499,072. Repeated full-window validation and original
Python tick loops may be expensive. Profile bounded synthetic inputs and ensure
streaming/day-scoped caches before any supervised market job; do not silently
replace the execution kernel or drop samples for speed.

New market labels, market fits, account replays and trial charges remain zero.
The historical total remains 13,258 and all 48 sealed dates stay closed. No
Windows collector/model, schedule, Telegram credential or order change occurred.
The full model-development and Windows-operation goal remains active.

## Source And Account Integration

Completed October 6, 2026, observed by 14:41 UTC. Three additional components
are implemented, still WITHOUT market transition labels, fits or account replay:

- `prepare_nq_apex_transition_v137.py` restores the pinned V123 source and
  V134 contexts, complete broad census and three plans. It binds the four
  sealed V136 giveback books, not the older V135 control. Admission remains
  current-content restoration, not renewed provider authentication.
- `nq_apex_transition_pipeline_v137.py` joins all original prefix events with
  mature labels and exact 15+4 features before known-support filtering. It
  validates complete state/mode evidence, cash/floor/peak arithmetic, zero-label
  skip reasons, independent census hashes and irreversible byte-backed arrays.
  Unsupported events and empty dates remain in the census; future labels are
  rejected. Future V123 context bytes are hash-bound, not used as training rows.
- `nq_apex_transition_account_v137.py` supports both declared arms in both
  phases. It queries only its own causal state after busy/day-stop checks and
  before entry-window reads. It journals raw eight-head predictions, projected
  floor, scores, quantities, bindings and out-of-grid queries. Known zero
  capacity bypasses model nomination. Callback failure rolls back the entire
  day; original source inputs and global execution namespaces are unchanged.

Parent verification passed 1,844 integration/affected cases plus 125 disjoint
source cases: 1,969 unique tests, zero failures/errors/skips, actual exits 0.
The suites took 240.190 and 30.479 seconds. The 346 new cases are 151 account,
70 pipeline and 125 source tests. Earlier 799/365/574-case runs overlap and
are NOT added to the total. This is not a full-repository green claim or
economic evidence. The nine V136 frozen pins and initial V137 target hash are
unchanged. Review caught and fixed omission of NONPOSITIVE_NET_TARGET from
accepted zero-label reasons and hardened prepared array/state revalidation.

The one real source-only preflight exited 0 after 175.029 seconds, observed at
14:39:35 UTC. It reconciled 181 dates / 5,485 opportunities, 1,430/2,670/3,899
training-prefix opportunities, 126 scoring dates / 3,747 opportunities, exact
V134 contexts and four V136 controls. No raw-tick payloads, sealed dates, new
labels, fits or account replays were accessed/executed by this preflight.
Its source bytes were unchanged throughout and its binding SHA256 is
`333f16a9d173fbd4747f94f1f16b8fdd2769088d27967e38f04331ceccb8fc5d`.

A bounded synthetic performance check built 104 MNQ state/mode labels from
20,000 normal-window ticks (19,333 delayed) in 1.2677 seconds. It is neither
market evidence nor a production runtime forecast. Large raw-label jobs still
need day-scoped caches and the immutable supervised runner before execution.

Private receipts and JUnit files are under
`reports/nq_apex_v137_integration_20261006/`. Integration JUnit SHA256:
`27d2d9db18c0384500d23bd73e4a2c33a5d8e87a5deb716f29799f9f2930d2e8`.
Source JUnit SHA256:
`fe38d5e7cbd2e022ba5c66e8e80898bf5c13636aec3301814adb56f9bf95ef8a`.
Source-wrapper SHA256:
`d5ab18842b9c482a4a0ad46a675ebb3d617ca01b21e6de513f93de656e5cb9d5`.
Pipeline SHA256:
`2b583d0cae290dd3d174c16412ccd2492f7250353b91fa458ecbef19c06712ff`.
Account SHA256:
`38a980d81f2b49ec3c24dc507ec5f54519616114f7591de0e8544280affd3bc7`.

No model result or live signal was manufactured. Four comparisons remain
unreserved, historical trials remain 13,258 and all 48 sealed dates are closed.
The Windows archive's automatic 23:00 KST run succeeded with no failed/pending
backups; seven current-date metadata/invalid-marker files were deferred, not
fresh prices. The Mac relay process was alive with zero signal-inbox files.
Cancelled Windows UI recovery was not retried. The complete goal stays active.
