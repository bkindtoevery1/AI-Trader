# Apex 25K research batch v75

Completed 2026-09-07 KST following explicit user authorization to implement more
models and consider justified development-screen revisions.

## Result

Eight new models and one v63-style reference were evaluated on four chronological
63-session development folds. All nine failed both the original and revised
screen. No confirmed 25K pass, holdout test, live signal, or promotion occurred.

| New model | Net USD | Stress USD | Sharpe | PA survival folds | Payout folds |
|---|---:|---:|---:|---:|---:|
| Bayesian ridge | 520.12 | 573.50 | 0.275 | 50% | 0% |
| Nearest analogs | 1284.34 | 603.00 | 0.546 | 25% | 0% |
| Fixed blend | 601.40 | 526.50 | 0.322 | 25% | 0% |
| Extra trees | -1455.16 | -1105.50 | -0.715 | 0% | 0% |
| Shallow boosting | -2767.02 | -2533.50 | -1.401 | 25% | 0% |
| RBF kernel | -72.18 | -593.50 | -0.080 | 0% | 0% |
| Recency ridge | -1016.22 | -505.50 | -0.459 | 25% | 0% |
| Huber linear | -1743.78 | -1069.50 | -0.783 | 25% | 0% |

Direct PnL is a one-MNQ development return series after commission and slippage.
It excludes Evaluation purchases and activation fees; it is not payout cashflow
or account profit. Separate account journeys use two MNQ in Evaluation and one
MNQ in PA, the existing Apex EOD rule snapshot, and a 46.75-point protective stop.
Stress includes timing changes as well as higher fees/slippage and can sometimes
outperform baseline. An ongoing PA at a fold boundary is right-censored, not an
observed eventual failure.

Bayesian ridge is the first **research lead**, based on the frozen safety/gate
ordering. Nearest analogs has the best new-model direct profit but weaker account
progress. Neither merits replacing the frozen v63 shadow deployment.

## Experimental Boundaries

- Development inputs: 616 aligned sessions, 2023-09-06 through 2026-06-12.
- Expanding training prefixes: 324, 397, 470, 543 sessions; ten-session gaps.
- Validation: four blocks of 63 sessions, 252 scored observations per candidate.
- Existing dates have already informed earlier research. This is not independent
  confirmation, despite correct time-ordered fitting within this batch.
- All transformations are training-only. Model parameters, ensemble weights,
  decisions, account rules and execution times were frozen before this run.
- The only relaxed statistical shortlist cutoff is single-model bootstrap
  p <= 0.20 rather than p <= 0.10. This does not imply statistical significance.
  Economic gates stay unchanged; stress PA EOD breaches are also disqualifying.
- Nine comparisons are counted, including the reference and fixed blend:
  inherited 12,929; total 12,938. Family bootstrap and global HAC-Bonferroni
  diagnostics are retained. Global historical DSR is still unavailable.
- The sealed 2026-06-29 through 2026-09-02 holdout and v63 prospective protocol
  are untouched. No model parameters were changed after this comparison.
- The reference uses one fewer initial training session than the original v63
  study. Its different result must not overwrite the original v63 evidence.

### Reference Sensitivity

The already-counted reference comparison also exposed sensitivity to the initial
training sample. The original v63 used training prefixes 325/398/471/544; this
common-data replay uses 324/397/470/543 with the same validation dates and selected
alpha 100. Three daily PnL observations differ. Original direct net PnL was
2579.66 USD versus 1877.12 USD in the replay; observed payout folds change from
25% to 0%, and baseline PA EOD breaches from zero to one. This is an additional
reason not to describe the historical v63 result as a robust verified pass.
It does not modify the original result or the frozen deployed model.

## Reproducibility

Code: `src/aitrader/nq_apex_model_batch_v75.py` and
`tools/run_nq_apex_model_batch_v75.py`.
Policy: `config/nq-apex-model-batch-v75.json`.
Optional isolated dependencies: `config/nq-apex-model-batch-v75-requirements.txt`.

The run used `<TMP>/ai-trader-v75-venv/bin/python` with system NumPy and explicitly
installed, version-pinned scikit-learn dependencies. No trading environment was
reconfigured. The temporary environment can be recreated from the requirements.

The runner requires `--freeze` before loading outcomes and refuses to overwrite
an existing completed comparison. Evidence lives in
`reports/nq_apex_model_batch_v75/`: preoutcome lock, run receipt, complete status,
result seal and failure attribution. Both feature caches were recomputed from
the current real development data and verified before model fitting.

## Next Research Question

Verification completed: 38 focused model/evidence/central-state tests and the
full 3,295-test regression suite passed in the isolated research environment.

The main failure is not merely an overly strict p-value: the new models did not
build the required payout buffer in any observed fold and suffered regime
instability. Any next experiment should preregister a different economic
hypothesis, count every trial, preserve the sealed data and account rules, and
not silently tune these failed models until the same development dates pass.

## Primary References

- [scikit-learn histogram gradient boosting](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html): early stopping is explicitly disabled to avoid random internal validation splitting.
- [scikit-learn extremely randomized trees](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html): the implementation uses fixed shallow trees and large minimum leaf sizes.
