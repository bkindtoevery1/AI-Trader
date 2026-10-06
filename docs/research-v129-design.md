# V129: Own-Product Two-Part Payoff Forecasts

## Reason

V128 completed the matched PA replay: both V126 direct HGB and V127 session
context forecasts lost money in every PA cost mode and produced no payout.
The inherited NQ Evaluation model also delayed use of the new MNQ forecasts
until late April. V129 therefore prepares separate NQ and MNQ forecasts so a
later whole-route study can replace BOTH Evaluation and PA predictions.

This is one outcome-informed extension of V76's sign-probability/constant-payoff
recipe and V89's intraday probability/payoff decomposition, not a new invention
or an independent validation. It compares complete forecasting recipes, not
classification versus regression with everything else held constant.

## Frozen Experiment

- Products: genuine own-product one-contract net cents for NQ and MNQ.
- Features: exact V123 twelve coordinates, nine price/risk coordinates plus
  three local minute-volume coordinates. BOTH products use NQ-anchor features;
  MNQ labels do not imply MNQ-derived feature prices or volume.
- Calendar: existing 181 development dates, ending June12,2026. Three training
  prefixes of45/87/129 sessions, each followed by ten purge sessions and42 scored
  dates. All126 scored dates remain, including empty/no-supported-event dates.
- All original training journals resolve strictly before09:00 ET on the first
  purge date, including rows later excluded by capacity or stop support.
- NQ training/query support is its own initial reference capacity greater than
  zero, reconciled against original NQ nulls. NO140-tick PA stop restriction.
- MNQ retains exact V126 populations and queries: own-capacity-positive then
  stop<=140 for training; original MNQ nonnull, stop<=140 and original initial
  NQ capacity-positive for querying. The query gate never migrates into fitting.
- Equal retained-date weights; zeros and losses retained. No filtering by old
  forecast positivity, selected account trades or observed profitability.
- V100 validates NQ populations and original fit receipts, but its reference
  exposure USD target is NOT used. Extract original journal unit cents by ID.
- Prepared source already contains development scoring labels. Isolation means
  fit receives only mature prefix arrays, not that outcomes were never loaded.

## Learners

Candidate `hurdle_logit` uses four separate LogisticRegression heads for raw
`net_cents > 0`. Fixed C=1, lbfgs, max_iter=1000, tol=1e-6, intercept=true,
class_weight=None; all remaining installed sklearn defaults are recorded.
One weighted X StandardScaler is fitted per product/fold; no Y scaler.
Estimator weights are original date weights divided by their training mean.

Per mode, recombine p with the original-weighted positive and nonpositive
training means: `p*mu_positive + (1-p)*mu_nonpositive`. Do not rebalance classes
or re-equalize dates separately inside branches. Zero belongs to nonpositive.
Branch magnitudes are constants within each prefix, a material restriction
despite varying stop sizes. Probabilities are not independently calibrated.
Single-class prefixes use the predeclared constant0/1 probability, with the
absent branch mean0 unused; record this as a constant head, not a native fit.
Native errors are fatal, never a reason to switch to a constant or retry.
Warnings/nonconvergence remain in the evidence without tuning or refitting.

Comparator `hist_gradient` uses the EXACT V126 recipe: weighted X/Y scalers,
mean-one native weights, squared error,100 iterations,.05 learning rate,
7 leaves,50 minimum leaf samples,L2=10,early_stopping=false,random_state126.
Fit three NEW NQ pipelines. MNQ comparator is the exact sealed V126 forecast,
not a refit, with exact population/query/parameter/runtime/source reconciliation.
Training means are descriptive anchors only. No MSE-based economic pass gate.

## Accounting And Evidence

Reserve five comparisons before any market fit: three new product/recipe cells
(NQ hurdle,NQ HGB,MNQ hurdle) and two within-product hurdle-versus-HGB contrasts.
Effective historical count13232 becomes13237. Conditional means, retained MNQ
forecasts and descriptive mean anchors are not separately selected policies.
There are nine new pipelines, at most36 native response fits (24 logistic,
12 HGB) and exactly12 native scaler fits. Record constant heads separately.
Later account policies/comparisons need their own explicit reservation.

Freeze design, implementation and tests; one supervised attempt with durable
native fit and pipeline journals, immutable files, actual child exit receipt
and no automatic retry. Save all forecasts before attaching scoring outcomes.
Recheck source, loaded code, runtime and retained comparator after fitting.
Audit saved hashes and recompute saved descriptive summaries, without refits.

Date-equal errors and all-four-positive overlapping label averages describe
forecasts; they are NOT executable account PnL or independent significance.
No account replay, economic verdict, verified50K pass or promotion occurs in
this stage. A later account test must replace both product routes, allow each
arm its own Evaluation transition, preserve costs and real contract sizing,
and not reuse V128's inherited-Evaluation equality assertion.

June29-September2 sealed holdout remains closed. No new raw-tick scan, order,
Windows change, Telegram message, purchase, model rollout or genetic algorithm.
