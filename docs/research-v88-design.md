# v88 Conditional Opportunity Quality

## Changed Failure Hypothesis

v87's uncapped baseline had negative recorded pre-cost PnL as well as negative
net PnL. More entries added no active dates. This experiment changes opportunity
selection, not caps, clock, direction, stops or contract sizing. It is selected
after observing prior development results and is explicitly outcome-informed.

Two main policies fit a small multioutput ridge, separately for NQ and MNQ.
Two counted diagnostic controls keep every original uncapped v87 event on the
same new scoring calendar. Four comparisons add to 13,069, reaching 13,073 only
when execution is reserved. Exact full-calendar conformance repeats add none.
Do not select controls as a newly discovered main model or claim independence.

## Information And Targets

Six features use the already completed decision prefix: mean-target distance
over ATR stop, directional SMA slope over ATR, log same-clock relative volume,
directional candle body over ATR, wick-family indicator, and normalized session
time. The frozen v87 union, source events and explicit same-maturity pair remain
unchanged. Relative volume uses the earlier 20 admitted same-clock sessions,
including cross-maturity history exactly as frozen v87 did; it does not reset
at rollover. This preserves a known interpretation limit, not a new volume
normalization claim or a rollover-filter change.

Generate unit-contract labels for EVERY original opportunity separately in all
four baseline/cost-only/latency-only/joint-stress modes. A cost/target admission
skip has zero payoff and stays in training. These counterfactual labels can
overlap and are not portfolio returns; do not learn only from historically
filled or model-selected trades. Each target is net cents divided by the
decision-known ATR-stop risk in cents. No clipping or label inversion.

Fit four conditional expected payoffs, not the minimum of realized outcomes
across modes. The latter would introduce an unnecessary hindsight worst-path
target. Trade only if all four predicted expectations are strictly positive,
using exactly the same decision selection in every execution mode. This is an
expected-value filter, not a confidence probability or proof of robustness.

## Chronological Training

From 181 admitted raw dates, the first 55 are training warmup. Score the last
126 in three contiguous blocks of 42. Before each block, exclude the previous
10 dates of the FULL 617-session admitted minute calendar from training; this
is not ten sparse raw dates. The previous model continues through scoring
dates that a later fit excludes, so no between-fold trading blackout is added.
Initialize each scored account once at the first scored date and preserve its
state across all blocks; do not reset after losses.

Use every available raw training opportunity strictly before the purge. Each
event date has total weight one, divided across its opportunities. Weighted
StandardScaler and multioutput sklearn Ridge(alpha=10, solver="svd") fit only
that prefix. No hyperparameter, feature, seed, threshold or fold search. Six
multioutput fits contain 24 output heads. Training-mean predictions are loss
diagnostics only, not additional tried trading policies.

Before any new raw labels, freeze code, tests, policy, environment and source
metadata. The structural preflight requires at least 40 events on 20 distinct
training dates for EACH fold and at least 30 possible active scored dates.
Abort the entire batch if insufficient, with no labels, fits or reserved
comparisons. No threshold rescue after this design is frozen. These minima
are feasibility screens, not statistical-power or profitability evidence.

## Execution And Evidence

Make each scored decision before loading that day's raw outcomes. Append all
counterfactual labels only after its predictions and account processing. Read
each admitted raw pair once and preserve full-scan hash/receipt checks. Reproduce
the entire original v87 uncapped direct and guarded paths in all four modes.
Separately initialize common-calendar controls and filtered accounts at score
start. New 126-date accounts cannot be relabelled as the original 181-date test.

Reuse the frozen uncapped adapter: no overlaps, five-minute post-resolution
cooldown, entry at decision+60 or +240 seconds, common exit at +5460 seconds,
ATR stop and immutable mean target. Actual NQ1 or MNQ-up-to6 contracts and all
account guards remain. Model rejection emits no trade intent and consumes no
execution cooldown; actual admission skips retain existing cooldown semantics.

Use daily returns, never count overlapping labels as independent observations.
Retain v87's practical screen on the 126 scored dates: baseline Sharpe >=0.5,
stress Sharpe >0, net positive in every mode, 30 active baseline dates, HAC
effective samples >=84, four-policy block-bootstrap family p<=0.20, and numeric
Evaluation passes in baseline and stress. Bootstrap uses 2,000 samples, blocks
of 10 dates, seed 20260988. PA survival, payout and MAE are assessed separately.
No partial metrics, optional stopping, retuning or holdout opening. A historical
screen pass is a development shortlist only; the final 48 dates stay sealed.
Global historical DSR, exact program fees and operational compliance remain
unresolved. Never enable orders, Telegram messages or modify operating bundles.

## Implementation References

Use the existing installed scikit-learn version recorded by the environment
lock. [Ridge documentation](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html)
defines the regularized estimator and sample weights.
[TimeSeriesSplit documentation](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html)
documents forward splits; here it splits ordered raw DATE groups, while the
purge is separately derived from the full exchange calendar. Equal raw-date
counts do not imply equal elapsed calendar durations or independent samples.
