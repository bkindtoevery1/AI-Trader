# v92 Soft Regime Opportunity Model

## Changed Failure Hypothesis

v88-v91 learned only on an already severely filtered quiet-late event stream.
v91's185 scored forecasts per product yielded8/7 actual trading dates, and all
eight forecast modes lost to their training-only mean comparator. More model
variants on the same restricted sample did not establish better predictions.

This outcome-informed, fixed experiment replaces HARD narrow-band, low-volume
and quiet-slope gates with causal payoff covariates. It is a coupled opportunity
breadth and representation change, not an isolated feature ablation. It does
not claim that more trades or relaxed regime gates improve profitability.

Keep the v87 late-session10:30-14:00 reentry/wick union, exact completed-minute
anchors,20 strictly earlier same-clock volume dates, positive finite ATR and
volume, and explicit contracts. Do not expand the clock to the volatile open.
All eligible events are emitted, not just the first. Previous-band width and its
preceding20-minute20th percentile must be positive; degenerate inputs are
reported, not imputed. Every original v87 event must remain byte-for-byte present
or the batch aborts. A broadened event is not mislabeled as passing old gates.

The feature vector is exactv91's seven coordinates plus log(previous bandwidth
/ preceding20-width q20) and absolute SMA slope/ATR. Log relative volume is
already present. No future volume, postentry state, clipping, threshold search,
probability interpretation, or score-based size is added. Four separate actual
unit-contract net-R targets remain correlated execution conditions, not four
independent samples. Learn every candidate event, including zero-payoff skips.

Use weighted training-only StandardScaler and Ridge(alpha10, SVD, intercept).
The parent enforces one thread in supported BLAS/OpenMP pools during the entire
runner using the existing locked threadpoolctl runtime, reapplies the limit at
fits, and binds actual supported pool/version/count records in the new lock.
The environment label alone is not proof, unsupported pools or general Python
threads are not covered, and historicalv91 pool settings remain unverified.
Exact control equality is still required; no thread or tolerance rescue is allowed.
Each training event date contributes total weight1 regardless of event count.
More events within a date do not create independent days or increase that
date's weight. The first55 of181 raw dates warm up training;126 scored dates form
three contiguous42-date folds. Purge ten dates from the FULL617-session calendar.
Old models continue across the between-fit purge dates. Never reset account
state at a fold boundary. Require40 training events/20dates per fold and30
structurally possible scored dates before any new raw labels or fits.

## Controls And Costs

Two main product policies and two exact narrowv91 controls reserve four
comparisons,13087 to13091. Six main and six control estimator fits produce48
learned output heads and no derived heads. Each control trains on its original
narrow events and original fold counts, NOT the broadened training population.
Verify original control fits, forecasts, all labels, journals, account paths,
full raw receipts and window receipts against the completedv91 seal. The broad
and narrow loss denominators differ; do not call their aggregate MSEs paired.

Trade only when all four mode forecasts are positive. Actual own-product NQ1
or MNQ up to6, nonoverlap,300-second cooldown, costs, risk guards, ATR stop,
immutable mean target, entry+60/+240s and common exit+5460s remain fixed. This
experiment's NQ1 is not a new global user authorization restriction. Preserve
all four execution modes and the complete Evaluation-to-PA account journey.
Program fees remain unpriced; simulated net trading PnL is not external cashflow.

Keep existing development screens: baseline Sharpe>=0.5, stress Sharpe>0,
positive net all modes,30 active baseline dates, HAC effective samples>=84,
four-policy bootstrap p<=0.20, and numeric Evaluation pass in baseline/stress.
Use2000 bootstrap samples,10-date blocks, seed20260992. PA and payout remain
separate. Software correctness, structural coverage or a historical shortlist
does not prove independent strategy success. The final48-date holdout remains
closed; global historical DSR is still unavailable. No orders or signal routing.

## One-Shot Evidence

Freeze source metadata, environment, policy, code, tests and this design before
extracting new opportunity prefixes or labels. An immutable preflight records
full617-date source hashes, legacy subset equality and broad/narrow fold support.
Recompute and compare it before reserving four policies. Predict both products
and all policies before opening that date's raw tape. Then process accounts and
append complete counterfactual labels. Scan each actual pair once and verify all
file hashes; do not reuse observed dates as a new independent holdout.

Within one product/date, a lazy four-entry LRU cache reuses identical immutable
TickWindows for the paired cost modes. It is populated only after predictions,
cleared before the next product, and never caches geometry, skips or trade
results. Four retained windows is not a total process-memory bound. Receipt and
control equality remain exact; no raw integrity check or outcome is omitted.

Publish no performance until all181pairs/126scoreddates and exact control checks
finish. Create immutable run/result evidence with no-overwrite operations. A
terminal error is a failed one-shot run, not permission to rerun, retune or omit
unfavorable dates. Keep all failures and scoped local commits.
