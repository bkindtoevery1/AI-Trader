# Apex 25K neural and prior-model research v77

## Prefrozen Design

The user requested deep-learning research, excluded genetic algorithms, then
authorized rational validation changes and revalidation of promising previous
models. These requests were incorporated before this experiment's lock and
before loading its market targets. This is a new exploratory experiment, not a
revision of v63, v75 or v76 results.

Two new architectures train their temporal representations end to end:

- A causal residual TCN: four two-convolution blocks, dilations 1/2/4/8,
  eight hidden channels, ReLU, 1,671 trainable parameters.
- A one-layer unidirectional GRU: eight hidden units, 399 trainable parameters.

Both use the same six opening path channels and six scale/context features as
the v63 information set. Each decision sees thirty completed one-minute bars
ending 09:31 through 10:00 ET. Within-window normalization is available only at
the 10:00 decision; it is not a tradable intermediate-minute forecast.
Training scalers and target standardization see only the chronological training
prefix. Models train for exactly 128 full-batch AdamW steps at learning rate
0.003, weight decay 0.01, gradient norm cap 1, MSE loss, and one fixed seed.
No early stopping, best epoch, seed search or architecture grid is allowed.
PyTorch 2.14 runs in a separate deterministic CPU/float64 environment, leaving
the frozen production and earlier research environments unchanged.

Three outcome-informed prior-model references are revalidated:

- Original v63, including the 617-session cohort and unchanged nested
  three-alpha ridge selection inside each training prefix.
- v75 Bayesian ridge with its original 616-session feature cohort.
- v75 nearest-analogs kNN with the same cohort and original 63-neighbor setting.

These are the first revalidation group, not a claim that every older candidate
has been revalidated. v63 had the strongest prior practical evidence, and the
two v75 models had positive baseline and stress aggregates but failed their
screens. Selection of these references is outcome-informed and explicitly
charged. Five reported policies and twenty outer fits add seven comparisons:
two neural policies, three nested v63 alpha choices, and two v75 references.
The resulting ledger is 12,949 comparisons, conditional on completing the run.

## Validation Correction

The previous model continues unchanged for the next ten embargo sessions;
excluding labels from training does not require forbidding trading on those
dates. Every session must have exactly one previously fitted model assigned.
The next fit takes over only at its declared validation boundary. This leaves
the original four 63-session comparison folds unchanged and supplies the
additional thirty between-fold sessions to a 282-session continuous account.
There is no selection between a flat-calendar and a continued-calendar variant.

The fixed 10-session training purge remains. The first neural/v63 fit uses
325 sessions; later fits use 398/471/544. The two v75 references use one fewer
training session in each fold, exactly as in their original runs. Require the
old 252-session results to reproduce before interpreting the new continuous
path. v75 has daily signals and baseline/stress vectors; v63 exposes baseline
daily returns, per-fold direction counts, selected alphas and stress totals.
The conformance gate checks only what the respective records actually contain.

All five policies retain the fixed 46.75-point protective stop, costs and
slippage, baseline 10:02-12:00 ET execution, and joint cost/latency stress.
Account journeys use two actual MNQ contracts in Evaluation and one in PA.
One-MNQ fixed-notional PnL is reported separately from account-path outcomes;
it excludes account purchase/activation fees and is not payout cashflow.

The practical screening gates remain unchanged from v76. Passing them would
still be exploratory: these historical dates have been observed before, global
historical DSR is unavailable, and the sealed 48-session historical test and
frozen v63 prospective confirmation must not be opened or rewritten here.
No candidate is deployed or sent to Telegram by this research tool.

## Sources

- [TCN sequence-modeling study, Bai et al.](https://arxiv.org/abs/1803.01271).
  This motivates a temporal architecture, not a claim of investment profitability.
- [PyTorch GRU implementation](https://docs.pytorch.org/docs/2.14/generated/torch.nn.GRU.html).
- [PyTorch reproducibility guidance](https://docs.pytorch.org/docs/2.14/notes/randomness.html).
  Deterministic local tests do not establish cross-platform bitwise equivalence.
- [Official Apex EOD Evaluation rules](https://apextraderfunding.com/help-center/eod-trailing-drawdown-accounts/eod-evaluations/).
- [Official PA inactivity policy](https://apextraderfunding.com/help-center/billing/inactivity-policy-on-performance-accounts-pa/).
  The published account rules were checked on 2026-09-07 UTC; the experiment
  retains the existing account-rule snapshot rather than relaxing the actual rules.

Implementation: `tools/nq_apex_neural_v77.py` and
`tools/run_nq_apex_neural_research_v77.py`.
Evidence directory: `reports/nq_apex_neural_research_v77/`.

## Completed Results

The five policies completed all twenty outer fits. The prior-reference
conformance gate passed. All five failed the continuous practical screen;
the historical ledger is now 12,949 comparisons. No model was promoted.

| Model | Original 252 dates, USD | Continued 282 dates, USD | Continued stress, USD |
|---|---:|---:|---:|
| Causal TCN | -1580.60 | -2474.26 | -3226.00 |
| Small GRU | 573.72 | -853.66 | -86.00 |
| Original v63 reference | 2579.66 | 1670.70 | 1146.00 |
| v75 Bayesian ridge | 520.12 | -493.18 | -72.50 |
| v75 kNN | 1284.34 | -180.20 | -952.00 |

These are fixed-one-MNQ model-signal vectors with commission/slippage, not
account cashflows or money actually earned. Adding the previously omitted
dates made several superficially positive aggregates negative. This is a
reason to preserve complete calendar evidence, not to restore selective gaps.

The unchanged v63 remains the strongest candidate in this group. Its baseline
account reached simulated payout eligibility on 2025-07-01 but later closed
for inactivity, with its last observed PA session on 2025-11-13. The stress
account closed for inactivity without reaching payout eligibility. The legacy
`PAYOUT_ACHIEVED` summary records a historical event and does not override the
separate failed-survival flag. No actual payout was requested or received.

TCN training MSE fell to 0.014-0.131, but validation error was 1.35-2.25 times
the training-mean predictor's error in every fold. GRU error was approximately
0.993-1.070 times that baseline. These are post-result generalization
diagnostics, not permission to select an earlier epoch or new architecture
using the exposed validation errors.

The five-policy family bootstrap p-value was 0.364. The original v63 return
vectors reproduced, but this experiment's bootstrap seed/family differs;
its p-values must not replace the original statistical report. None of these
reused dates constitute independent confirmation.

An additive diagnostic replay in `postresult_audit.json` verifies the detailed
account closure reasons and neural errors without fitting another model.
The remaining positive-return older leads are documented in
`failure_attribution.json`; only three previous candidates were revalidated
in this group. The first group is not a claim of full legacy-archive coverage.
