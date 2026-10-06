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

1. Bind the exact V123 source and V134 contexts, all original event identities,
   paired raw receipts and three plans. Derive rows from source stream, not
   V129/V134 already-filtered training arrays or V136 selected executions.
2. Integrate mature labels with the exact training prefixes (45/87/129 sessions,
   ten full-calendar purge sessions, cutoff 09:00 ET on the first purge date).
   Join all 15 causal feature bits and four state coordinates. Reuse identical
   training-event labels across nested folds without treating them as new data.
3. Implement both-phase actual-own-state inference after busy/day-stop checks
   and before entry quote reads, retaining the original full account lifecycle.
   Add the two declared decision arms and four exact V136 mode controls.
4. Finish the immutable source/model/result runner and saved-model audit; run
   source preflight, pin and publish the complete design/dependencies, reserve
   the four planned comparisons, then fit and replay once. Publish only complete
   results and retain failures rather than tuning against them.

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
