# V118 Independent Adversarial Component Review

Parent resolution: the original review and failed runs below are preserved.
The final resolution section records the subsequent type check and passing
regressions; the original HOLD applies to the reviewed pre-fix revision.

## Recommendation

**HOLD pure-component qualification at the reviewed forest revision until the
native leaf-container validation defect below is fixed and these 33 adversarial
cases pass.** No change to the learner, economic gates or account kernel is
recommended. The current memory repair passes its bounded regression.
No additional concrete blocker was found in the updated source-population
adapter. This review does not qualify a runner, source admission or market claim.

The reviewed design correctly calls this a distributional payoff model with
state-adaptive risk tolerance, not a true PA account-value model. Fixed-H uses
250000 cents but still has own-state quantity. Its all-four-positive rule,
three arms, two primary contrasts, one diagnostic contrast and planned five
charges agree with the supplied config. No charges were created here.

## Open Finding

### P2: Canonical JSON equality admits non-native leaf containers

At `tools/nq_apex_distribution_forest_v118.py:160`, validation compares the
canonical digest of `tree["leaves"]` with reconstructed membership without
checking native leaf-key and row-container types.

Two independent counterexamples retain the exact original model hash:

1. Replace a constant tree's string key `"0"` with integer key `0`.
2. Replace its row-index list with a tuple containing the same integers.

Python JSON encodes both changes exactly like the original. Both pass
`validate_model()`, contrary to the native exported-container contract.
The tuple form subsequently breaks `weights[rows]` indexing in
`distribution()` at line181: NumPy treats the tuple as multidimensional
indices. The integer-key form is accepted through inference.

The preserved failing cases are:
- `test_non_native_leaf_containers_cannot_hide_behind_equal_json_hashes[leaf_key_int]`
- `test_non_native_leaf_containers_cannot_hide_behind_equal_json_hashes[leaf_rows_tuple]`

Suggested parent-only fix: require exact string keys, exact list containers and
exact native-int row indices before membership equality. Do not change graph
ordering or normalize invalid containers into valid ones. This is a validation
defect for direct Python inputs, not a demonstrated corruption of JSON-loaded
market artifacts or economic arithmetic.

## Resolved Observation

The first read found `distribution(record, x) @ y` inside fit verification,
which requested an N-by-N float64 matrix. The admitted 200000-row ceiling implied
320000000000 bytes for that matrix alone. No such allocation was attempted.

The parent changed verification to original-weight leaf means plus an N-by-4
accumulator and native predictions. The current
`test_fit_mean_verification_does_not_allocate_a_training_squared_matrix`
passes while rejecting any N-by-N allocation request on 600 invented rows.
The separate distribution API now caps output mass cells at 2000000 and requires
caller batching. The obsolete quadratic-fit concern is not an open finding.

The current graph validator correctly permits best-first, nonpreorder node
numbering while enforcing bounded depth, unique visitation and complete support.
The adversarial graph permutation preserves the complete query distribution.

## Added Coverage

Only `tests/test_nq_apex_distribution_adversarial_v118.py` and this note were
created/edited by this reviewer. Parent tests, pure components, config, design
and all ancestor modules were read only.

The 33 cases add:
- Native float32 routing at a double-precision threshold that is not itself
  representable in float32. A query equal to that double threshold rounds to
  the right native leaf; casting the threshold to float32 or routing the query
  in float64 would give incorrect membership.
- Finite float64 query overflow rejection before native float32 routing.
- Complete nonpreorder graph relabeling without imposing preorder numbering.
- Native leaf containers, float matrices and node scalar types despite valid
  rebound hashes or canonical JSON equivalence.
- Unsupported sklearn runtime rejection before fit-stage callbacks.
- A large leaf with only four distinct dates rejected despite adequate event
  counts and overall date support.
- Within-date replication without manufactured date/outcome probability mass.
- Identical tree means with a positive mean payoff but negative utility from
  the retained empirical downside; tree count does not supply independent data.
- Read-only strided queries and detached validator/distribution result arrays.
- Bounded regression against quadratic training verification.
- Exact frozen allocator non-equivalence and exact scale cancellation.
- Zero-capacity utility rejection, without claiming to test the missing timing
  adapter's cooldown behavior.
- Prepared-input array/list/metadata isolation across all fit callbacks.
- Rebound fractional or out-of-domain unit-cent arrays rejected before fitting.

All learned test artifacts use invented coordinates, dates, identities and
outcomes. No parent test fixture, actual source population or market outcome was
used. The independent native forest reference fit is also synthetic.

## Exact Allocator Demonstrations

The tests call the unchanged
`nq_apex_product_bracket_replay_v85.ProductBracketAccount.size_limit` and the
unchanged day-start MAE/DLL methods on invented PA states. No account kernel is
patched, and no tick window or account replay is performed.

**Contract-cap non-equivalence:** H=50000 cents, stop20, reserve1650,
half-headroom budget24999. The fresh-PA contract cap binds at q=5.
For equal-probability one-contract outcomes +10000/-8000 cents in each of the
four heads, CE is positive at fixed H=250000 and negative at own H=50000.
An independent 80-digit Decimal calculation confirms both signs. Both arms use
the same current q, not a fixed-H quantity recomputed from imaginary capital.

**Exact cancellation:** stop140 gives reserve7650. At H=35000 and H=70000,
the unchanged allocator permits q=2 and q=4 respectively, below the contract
ceiling and below the MAE cap. Exact fractions satisfy
2/35000 = 4/70000. The four output CEs scale by exactly two and preserve every
nomination sign. This is equality across proportionally scaled own-state
queries, not a claim that own-H always equals fixed-H.

**Zero capacity:** H=2000, stop140 yields q=0, which pure utility rejects.
The future timing adapter must still preserve the existing capacity-skip
attempt, actual resolution and cooldown; converting it into free model
abstention would change the design. These tests do not certify that unimplemented
adapter behavior.

## Population Adapter Review

The current `nq_apex_distribution_inputs_v118.py`:
- Delegates complete original label, identity and all-mode maturity validation
  to V100 before the known stop<=140 filter.
- Extracts the actual one-contract journal net cents, not V100's
  reference-quantity-multiplied dollar matrix; genuine zero outcomes remain.
- Recomputes date-equal weights after retained support.
- Requires the closed metadata field set, exact static flag types, consistent
  support counts/calendar, typed source identity and bounded integer-valued
  cent targets before forwarding to the estimator.
- Deep-copies prepared arrays, dates, identities and metadata before any external
  fit callback. The adversarial callback mutation case passes.

Supplied hashes still establish only supplied identity. The caller owns source
authentication, complete causal fold/purge binding, permitted fit counts and
claims; the component does not independently prove those facts. No further
metadata hardening is requested by this bounded review.

## Verification And Preserved Failure History

Runtime: Python3.14.3, NumPy2.5.2, sklearn1.9.0, original v102 runtime.

Command:
```sh
env PYTHONPATH=src:tools PYTHONDONTWRITEBYTECODE=1 <HOME>/.local/share/ai-trader/runtime/v102-20260912/bin/python -B -m pytest -o addopts='' -q tests/test_nq_apex_distribution_adversarial_v118.py
```

- Initial 30-case run, exec73764: **28 passed, 2 failed**, exit1, 1.42s.
  Test source SHA256:
  `8ddc1588c69760959a91b83fa7f19c443abfd1da18f8a27b183aaea925b45635`.
- Expanded 33-case run, exec9108: **31 passed, 2 failed**, exit1, 1.47s.
  Both failures remain the exact leaf-container cases above. They were not
  removed, skipped, xfailed or weakened. The assertion was
  `Failed: DID NOT RAISE ValueError` at test line132.

The second run includes the three adapter cases, all passing. No full suite,
market fit, account replay, real source admission, outcome recomputation, new
claim, ledger/central edit, git, network, Windows or order action occurred.

## Reviewed SHA256 Pins

- Forest after parent memory fix:
  `d5984d077ab74b8d27e07ce87191bce889a92c6a1402bf996a280227148865a5`
- Updated input adapter:
  `85356463922d83985a9d188920a98f31719d5b97d5acf4918d23828b25acafcb`
- Utility component:
  `e501dc30d2e9c40296b482e6aba47057ddf852bb149fd9667bcc176363cbf667`
- Adversarial test file at the 33-case run:
  `6d3c1420383f6cafd67e754983e98c59a52a7538c14708035679c2297d3df1c7`
- Design:
  `3d66a01a84865110ed2af74db082e810288d0205092f7aef1c4776ecc6401974`
- Config:
  `224c6bf4cdcb14cb39fabc0e427a2d3fe7c4c577af955446dc53558725227e99`

## Parent Resolution

Added exact string-key, list-container and native-int-index checks before leaf
membership comparison. No normalization or learner/decision-rule change was
made. Forest SHA256 after the fix:
`4aa97f5cde758070fdd3baf5246c8bdd0e4fa3a38e6942a523b007615ef3eaee`.

The parent ran the four V118 test modules plus unchanged V100 population and
V85 bracket regressions under the original v102 runtime: **398 passed**, exit0,
3.80seconds, execsession46564. This includes all33 unchanged adversarial cases;
the two failing regressions now pass. JUnit evidence is
`reports/nq_apex_state_distribution_v118_implementation/focused-v1.xml`.
The resulting scope is pure-component verification only. No unrestricted full
suite, actual source admission, market model fit or account runner is certified.
