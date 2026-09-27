# V113 Adversarial Design Review

2026-09-14. Bounded design review of the main agent's proposed policy, not approval of
Main's in-progress numerical implementation or permission to execute it. V112's
terminal audit and ledger 13,187 are taken from its completion record [S1], not
independently re-audited here. Only this document was written. No models were
loaded, fitted or replayed; no trials reserved, holdout outcomes inspected,
broker data browsed, Windows state changed or commits made.

## Findings

1. **[P1] Distinct extension, but not new information or a new ranking model.**
   V113 adds one residual slope per mode/later fold to V112. For original signed
   dollar forecast x, center c, scale s, intercept a and slope correction b,
   the corrected forecast is `g(x) = c + a + B*(x-c)`, where `B = 1+b/s >= 0`.
   When B>0, positivity is exactly `x > c-(c+a)/B`: a learned original-score
   threshold, preserving within-mode rankings. When B=0, the mode accepts every
   available forecast or none according to `c+a > 0`; equality rejects. The
   four-mode intersection can change its membership/bottleneck, but cannot add
   information absent from the original score vector. The defensible hypothesis
   is transfer of a score-dependent residual relationship, not independent
   confidence, calibrated probability, improved ranking or a threshold-free
   mechanism. Use the signed original forecast, not absolute magnitude or the
   minimum across modes. This conclusion follows algebraically from the proposal.

2. **[P1] Centering DOES match V112's penalized intercept, conditionally.**
   Let `w_i=1/n_d` for the same retained original opportunities on date d,
   `D=sum(w)=number of nonempty retained dates`, `r=y-x`, and
   `c=sum(w*x)/D`, `s^2=sum(w*(x-c)^2)/D`. For nonconstant x, `z=(x-c)/s` gives
   `sum(w*z)=0` and `sum(w*z^2)=D`. The declared objective is
   `sum(w*(r-a-b*z)^2) + 20*(a^2+b^2)`, subject only to `b >= -s`.
   Consequently `a=sum(w*r)/(D+20)`, exactly V112's date-mean residual correction
   in real arithmetic, even when the slope bound is active [S2,S3]. Also,
   `b=max(-s, sum(w*z*r)/(sum(w*z^2)+20))`. These are verification oracles, not
   a request to replace Main's solver. For constant training x, use s=1 and
   training z=0; the unique slope optimum is b=0 and the correction is V112.
   "Unconstrained intercept" must mean unbounded, NOT unpenalized. An ordinary
   unpenalized regression intercept, weights normalized to sum one, different
   rows, or scoring-fold centering breaks the V112 identity. The raw-coordinate
   intercept is `a-b*c/s`, which generally does NOT equal V112's bias.

3. **[P1] Leakage boundary is necessary but not current-vintage independence.**
   Reuse the authenticated six original V102 product/fold bundles and ORIGINAL
   prior outer predictions, not current-model re-predictions, V112-corrected
   history or V113-corrected fold-two history. V102's later models/settings used
   eligible historical prefixes, so those earlier outcomes are not an independent
   calibration sample for the current model [S3,S7]. Freeze each mode's c/s/a/b
   before the entire current fold. Derive the ten-session purge from the complete
   exchange calendar and require all four original label resolutions strictly
   before its cutoff, including rows later excluded for unavailable forecasts.
   Preserve true zero skips; null forecasts and empty dates are not observed
   zero residuals. Keep V112's population and minimum support, not just selected
   trades, PA survivors, stop<=140 rows or future-geometry survivors [S3,S5,S12].

4. **[P1] A slope or account gain does not identify conditional PA payoff.**
   Pooled score/residual covariance can come from between-date or between-vintage
   mean shifts rather than within-date opportunity quality. Training covariance
   and training loss improvement are mechanically favored by adding a regressor;
   neither is confirming evidence. Squared loss can be driven by a few extreme
   dates despite date-equal weights. The labels remain fresh-Evaluation-reference
   dollar outcomes, not current PA quantity, affordability, cooldown, guard or
   survival utility [S5,S13]. V112 lost gross PA money in all four modes and
   depleted later risk budgets [S1]. A change in fills/risk-cap-flat counts cannot
   establish why the learner succeeded or failed. Monotonicity within a mode
   imposes neither cross-mode cost ordering nor monotone account profit.

5. **[P2] Numerical equivalence and boundary behavior need explicit rejection tests.**
   The Ridge-equivalent augmented system uses `sqrt(w)*[1,z]`, target
   `sqrt(w)*r`, and penalty rows `sqrt(20)*I_2` with zero targets. Bounds are
   `[-inf,-s]` to `[inf,inf]`, not b>=0 or b>=-1. SciPy minimizes half the
   augmented squared norm; its common factor changes no minimizer [S14]. Using
   `20*I` as appended rows silently makes the penalty 400. Twenty zero-residual
   pseudodates at z=0 would penalize only the intercept, not both coefficients.
   Preserve event-level weighted covariance: regressing day-mean residuals on
   day-mean scores loses within-day terms and is a different estimator.
   Freeze runtime, solver, tolerances, iteration cap, variance convention and
   failure policy. Reject nonfinite intermediates, nonconvergence, bound/KKT or
   oracle mismatches; a solver success flag alone is insufficient [S14].
   Test constant/nearly constant and extreme scales, cancellation near B=0,
   extrapolation beyond historical score support, and strict-zero decisions.
   Near-zero positive B is not an exactly flat gate. Do not silently round it
   flat, clip forecasts, add a selection epsilon or change the variance floor.

## Precedents

No exact earlier bounded affine calibration of original HGB prior-OOS residuals
was found in the targeted search below. This is a repository-bounded finding,
not exhaustive method novelty. These inspected precedents are materially related:

- **V89:** target-hit logistic probability plus geometry-conditioned hit/other
  payoff regressions, recombined into expected net R. New source-feature models,
  not residual-on-original-forecast post-calibration [S8].
- **V90:** one shared six-feature Ridge effect plus four unpenalized training
  means, fitted on original training labels. It pools modes and constrains their
  slopes to agree; V113 independently calibrates four existing score heads [S9].
- **V93:** three family-regime interactions added to nine causal features, with
  date-weighted multioutput Ridge and exact-source/training-mean controls. Its
  residualization is a feature-rank check, not forecast-error calibration [S10].
- **V112:** exact nested b=0 policy, same prior-vintage history and alpha20
  penalized constant correction. V113 is an additional-degree-of-freedom
  calibration hypothesis, not a new HGB architecture [S2,S3].
- **Other hits:** V10 adapts signal orientation from matured OOS payoff signs;
  V82/V84 use fitted-score quantiles for sizing; V28 checks affine feature-scale
  invariance. None is the proposed monotone residual regression. V98 explicitly
  suggested later calibration research but did not implement it [S11].

## Required Disqualifying Controls

- **Exact nested and source controls:** retain both V112's completed constant-
  calibrated MNQ-PA accounts and V107 repair's original MNQ-phase accounts, not
  V107's NQ-only arm and not approximate reconstructed totals [S4,S6]. Independently
  check a against the authenticated V112 bias within frozen numerical tolerance.
  The slope-zero forecast path must reproduce V112's masks and accounts exactly;
  floating-point algebraic equality alone does not certify strict-positive masks.
  First-fold forecasts and every NQ Evaluation prefix must remain exact. Changed
  controls, row membership, costs, stops, sizing or account semantics disqualify
  slope attribution. This is conformance, not another selectable policy.
- **Synthetic identity and provenance controls:** require zero-residual identity,
  constant-score V112 reduction, positive/negative covariance cases, active and
  inactive slope bounds, unequal daily event counts, and mode permutation
  equivariance. Perturb forbidden current/future labels and assert the fit cannot
  consume them; reject corrected-history substitution, missing/duplicate rows,
  maturity violations and altered callbacks/restoration receipts. Freeze means
  and scales from precisely the same admitted prefix. Existing V112 tests are
  precedent requirements, not evidence that V113 already passes them [S12].
- **Mechanism falsification, without another fitted policy:** predeclare paired,
  date-equal all-opportunity forecast losses versus BOTH controls for each later
  fold/mode; report first-fold identity separately and full-horizon results too.
  Include residual bias/covariance, within-date versus between-date/vintage
  covariance contributions, original score support, extrapolation and largest
  date contributions. Describe threshold-equivalent masks, mode bottlenecks,
  added/removed nominations, fills and account skips. An equivalent original-score
  threshold mask must agree exactly away from documented numerical boundaries;
  it needs no extra market replay. No incremental later-fold prediction evidence
  defeats a general conditional-payoff claim, even if one account path improves.
  Conversely, MSE improvement cannot rescue failed economic gates. Do not turn
  diagnostic bins, days or modes into post-result selection rules.
- **Economic gate:** predeclare positive candidate-minus-control PA trading net
  in baseline AND combined stress for EACH of the two controls, with no added
  hard/MAE breach or earlier inactivity in those primary contrasts. Report all
  four modes, absolute PA profitability and full-route/payout gates separately.
  Beating failed V112 while remaining below V107 is not incremental success.
  Preserve all 126 scheduled dates, including unchanged first-fold and terminal
  tails; no account resets at fold boundaries or survivor-only comparison.
  Three arms x four modes represents 12 continuous paths and 1,512 scheduled
  account-day slots, including authenticated archived comparators, not independent
  samples. Event overlap, correlated modes and only two calibrated scoring folds
  limit inference; any uncertainty calculation must preserve temporal pairing.
- **Prospective accounting:** one new policy plus two primary contrasts would
  charge 3, moving 13,187 to 13,190 only at a separate authenticated preoutcome
  claim. Nothing is reserved by this review. Record eight scalar-target constrained
  solves and 16 correction coefficients, plus eight learned center/scale pairs;
  zero HGB/source-scaler refits is not "no learned normalization." No extra
  ablation fits, market control refits, window/alpha/threshold searches or retries
  are authorized. Positive results remain reused-development evidence with
  unpriced program fees and unverified cohort, not independent validation [S1].

## Exact Inspected Sources

Links identify the read files or the starting locations of inspected excerpts.
Search-only hits were not treated as completed implementations. No report payload,
market-data file or sealed holdout artifact was opened.

- **S1:** [V112 completion](research-v112-completion.md); [V112 policy](../config/nq-apex-prequential-bias-v112.json).
- **S2:** [V112 design](research-v112-design.md); [V112 runner design](research-v112-runner.md).
- **S3:** [V112 component, full file](../tools/nq_apex_prequential_bias_v112.py).
- **S4:** [V112 replay and economics, full file](../tools/nq_apex_prequential_bias_replay_v112.py).
- **S5:** [Population maturity/weights/targets excerpts](../tools/nq_apex_inner_population_v100.py); [V107 phase account, full file](../tools/nq_apex_phase_micro_v107.py); [PA support-mask excerpts](../tools/nq_apex_pa_support_v105.py).
- **S6:** [V107 completion](research-v107-completion.md); [V107 integrity repair](research-v107-integrity-repair-v1.md).
- **S7:** [V102 design](research-v102-design.md).
- **S8:** [V89 design](research-v89-design.md); [V89 catalog/prediction/fit excerpts](../tools/nq_apex_opportunity_model_v89.py).
- **S9:** [V90 design](research-v90-design.md); [V90 component, full file](../tools/nq_apex_shared_effect_v90.py).
- **S10:** [V93 design, estimator/chronology/rank sections](research-v93-design.md); [V93 rank/prediction/fit excerpts](../tools/nq_apex_family_regime_v93.py).
- **S11:** [V10 orientation function](../src/aitrader/nq_apex_multiresolution_research_v10.py); [V82 sizing calibration](../tools/nq_apex_lagged_kernel_v82.py); [V84 sizing calibration](../tools/nq_apex_risk_aligned_models_v84.py); [V28 affine feature transform](../src/aitrader/nq_apex_v28_numerical_preflight.py); [V98 interpretation](research-v98.md).
- **S12:** [V112 synthetic test excerpt, read not run](../tests/test_nq_apex_prequential_bias_v112.py).
- **S13:** [V109 target/PA mismatch design](research-v109-design.md).
- **S14:** [SciPy lsq_linear official API documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.lsq_linear.html), retrieved 2026-09-14; objective, bounds and termination semantics only. The served manual was v1.18.0, not verification of the project's installed runtime.

Targeted `rg -n -i` searches used `affine|calibrat|residual|lsq_linear|isotonic|platt`
and residual/slope combinations over research documents, versioned NQ research
JSON policies, NQ research components/runners/tests, and application source.
Repository-root prefixes were `<REPO>/` with
scopes `docs/research*`, `config/nq-apex-*v*.json`, `tools/nq_apex*.py`,
`tools/run_nq_apex*.py`, `tests/test_nq_apex*`, and `src/aitrader`.
Holdout-named files were excluded; the application-source pass also excluded
broker/Toss/KIS-named files. Search hits about statistical calibration, archived
protocol calibration and cross-mode affine costs were not outcome inspection
or an exhaustive precedent audit. A narrow `13187|v112|v113` search of
`config/nq-apex-research-ledger.yaml` returned no matches; S1, not that search,
supports the stated completion count. Main's V113 learner was not reviewed.
