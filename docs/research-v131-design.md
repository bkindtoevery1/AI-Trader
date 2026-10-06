# V131: Matched History For Intraday Terminal-Return Forecasts

## Reason And Boundary

V130's own-product HGB route has a positive baseline PA outcome but fails the
combined-stress Evaluation. Two-part net-payoff learning also fails. A bounded
review confirms that longer minute history was already used in V78-V84; this is
not a first attempt to use three years of minutes or a new claim of independence.

Test one different supervision/history hypothesis: does adding the 436 complete
older minute sessions improve the same regularized forecast of subsequent
price displacement, on the same current intraday opportunities? Use two matched
history arms, not another payoff decomposition or hyperparameter grid. This
stage is forecast-only. It does not assert economic viability from smaller MSE
and does not put a gross-return number into a net-dollar account API.

## Fixed Source, Target And Split

- Preserve the 617 complete paired development sessions ending June12,2026,
  the exact V92 broad completed-minute event extractor, and the twelve V123
  NQ-derived features for both products. Reproduce all 5485 original raw-era
  events and original joined features, not the narrower V87 hard-filter subset.
- Source minute admission is read-only and allowlisted by snapshot/date;
  authenticate manifests, normalized receipts and original observation hashes,
  full1380-minute grids, aligned explicit NQ/MNQ maturities, and unchanged bytes.
  No incomplete session is filled, no rolled prices are spliced, and no sealed
  or outer-embargo bar is loaded. Keep empty dates in the chronological census.
- Target for each own product is the signed simple close-to-close return in
  basis points: 10000 * event_direction * (C[D+5460]-C[D]) / C[D]. D is the
  event's completed-minute END. Both closes are minute ends, within the same
  complete session and explicit contract. D+5460 is the unchanged91-minute
  event terminal boundary, not a searched horizon or executable fill.
- Features use only rows completed at D. Targets are separate records carrying
  product, contract, event identity, decision end and label end. Training labels
  must mature strictly before09:00ET on the first purged date, checked before
  any support filtering. No tick stop/target outcome is inferred from OHLC.
- Preserve three45/87/129 raw-era training prefixes, ten full-session purges and
  three42-date scored blocks, totaling126dates. The long-history arm adds the
  same436older complete dates, yielding481/523/565 scheduled training dates
  before event eligibility. Both arms share identical query features/events.
  Earlier scored dates enter later training only under the expanding schedule.
- All admitted broad events are eligible for terminal-return forecasts; no
  initial account-capacity, PA-stop, later-fill or profitability filter is used.
  This differs from V129 net-payoff support and is not a matched V129 comparison.
  The48sealed dates and ten outer embargo dates remain excluded.

## Fixed Learner And Reporting

For each NQ/MNQ product and each fold fit both recent-only and long-history
arms: twelve pipelines total. Weighted StandardScaler uses training X only;
one sklearn Ridge(alpha=10,solver="svd",fit_intercept=True) predicts unscaled
signed-return basis points. No target scaler, clipping, tuning, orientation
inversion or recency decay. Each nonempty training date has equal total weight;
native estimator weights are normalized to mean1, matching the existing local
recipe convention. Thus more training rows also changes effective regularization
relative to total data loss; this is a fixed-algorithm history comparison, not
an isolated constant-effective-penalty experiment.

Record every estimator/scaler, training census, mature-label/feature hashes,
native warnings and all predictions. Twelve Ridge fits plus twelve X scalers;
training-mean anchors are arithmetic diagnostics, not extra fitted strategies.
Preserve native constant-coordinate scaler roundoff without clipping: a negative
variance is accepted only with scale1 and magnitude within the float64 bound
(weighted sample count * coordinate mean * machine epsilon)^2. Other negative
variances fail. Bind saved training means and weight diagnostics to actual inputs.
Report date-equal MSE/MAE versus each arm's training mean, long-minus-recent
errors, sign diagnostics, and signed realized terminal returns among strictly
positive predictions, retaining empty-date accounting. These overlapping
gross-return labels are not trade counts, net profit or an equity curve. No
economic screen is passed or failed at this stage; report NOT_EVALUATED.

Reserve three comparisons before constructing target outcomes or fitting: two
history recipes plus one matched history contrast.13240 becomes13243. Do not
refund failed attempts, restart on an observation timeout, or use partial metrics
to choose products, dates, horizons, features, thresholds or the next run.

## Execution And Next Economic Contract

Qualify causal close/end alignment, explicit own-product targets, chronology,
weights, finite numerics, identical query support, source allowlists and terminal
evidence with synthetic tests before market execution. Freeze source/runner/tests
and design; use one supervised process and immutable completed outputs. Observe
actual exit and audit saved predictions, models and descriptive arithmetic without
refitting. Disclose focused/affected versus full-repository test scope precisely.

A later preregistered economic follow-up may use this as an explicit directional
confirmation/veto of retained HGB nominations, not as replacement net-dollar
means or a promise of profitable brackets. Its gate interface and account lineage
must be implemented and tested before replay; no such policy is selected by
this forecast stage. Retain costs, integer contract limits, own-state sizing and
continuous Evaluation/PA rules. No live deployment, Windows change, orders,
purchase, schedule, genetic algorithm, secret access or holdout opening here.
