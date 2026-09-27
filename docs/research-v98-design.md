# v98 Shared-Account Product Router

This protocol becomes executable authority only when bound by its separate
preoutcome lock after verification. At this design checkpoint the latest
completed study is v97; no v98 market replay, claim, fit, scored outcome or
holdout access has occurred. Later user authority is Apex Legacy50K Tradovate
Evaluation, not the stale25K goal text. Continue separate PA/payout assessment.

## Motivation And Prior Work

v97's NQ baseline account reached numerical Evaluation but skipped38 PA intents
for zero risk capacity and subsequently closed for inactivity. On those original
account snapshots, all38 had nominal MNQ reserve capacity and27 also had a
positive MNQ forecast in all four modes. Cost-only counts were36/26 and
latency-only23/17. These are posthoc descriptive intersections, not replayed MNQ
trades, executable entry geometry, changed-account PnL or independent evidence.
The changed route must be evaluated afresh. Its future balance, trailing floor,
available opportunities and cooldown diverge after the first changed decision.

The read-only v78-v96 review found MNQ stop-based capacity recovery in v83 and
separate NQ/MNQ accounts from v85 onward, not a shared causal product router.
Capacity recovery alone did not make v83 successful. This candidate does not
claim that missing capacity is the only failure or that MNQ must be profitable.

## One Policy, Not A Parameter Search

Reuse the exact six product/fold v97 fitted bundles and their four heads. No
training, scaler fitting, feature additions, threshold fitting or mode selection
is part of this candidate. Preserve the three42-session scoring folds, full
chronological training prefixes and ten full-calendar purge sessions in the
authenticated source. The same126 previously observed dates are development.

At each completed decision, while the shared account is available:

1. Obtain each product's own frozen forecast and known stop. Validate the event,
   clock, explicit same maturity, features and initial reference exposure.
2. Compute current affordable integer quantities using unchanged v85 account
   headroom, plan limits, MAE/DLL and conservative per-contract reserves. Caps
   remain NQ<=1 and MNQ<=6, including any stricter current plan limit.
3. An option is eligible only if its current quantity and original reference
   quantity are positive and all four own forecasts are strictly positive.
4. Rank eligible products by `min(four dollar forecasts) * current_q / q_ref`.
   This is a myopic predicted-dollar score, not a calibrated uncertainty bound
   or an optimized lifecycle value. Use exact rational comparisons of the saved
   finite floating-point values, with NQ breaking exact ties. Maximum feasible
   quantity follows the positive linear score; quantities are not searched.
5. Commit to one product and quantity before asking for its future entry tick.
   Execute only that product's actual tape. If the subsequent entry has invalid
   target geometry, skip; never inspect the other quote to rescue the decision.

If neither model proposes a positive trade, abstain without a future entry-window
request. If a positive intent has no affordable product, record a zero-quantity
skip using the first positive product in NQ/MNQ order solely for the unchanged
first-quote/cooldown clock. That quote probe cannot lead to product reselection.

Both products share exactly one account balance, equity peak, trailing floor,
phase clock, drawdown state and cooldown. At most one product is held at a time;
no hedge, concurrent independent books, or stitching of profitable account
segments is allowed. Product-specific raw fills, commissions and slippage are
used. Existing stops, targets, exit deadlines, uncapped fill count and300-second
cooldown remain. The unchanged v78 lifecycle owns Evaluation, PA, inactivity,
resets and hypothetical payout accounting. Any reset and fees remain visible.
No live or simulated broker orders are implemented.

## Economic Evaluation Contract

The primary development comparison is the shared router versus unchanged v97
NQ-only execution on the identical calendar, under baseline and combined stress.
Unchanged MNQ-only results are a descriptive comparison, not another selectable
candidate. Cost-only and latency-only decompose sensitivity; they cannot replace
a poor baseline or combined-stress outcome. Every policy owns its full continuous
account after paths diverge. Do not splice the original account's PA-only trades.

Report absolute and paired daily trading PnL in integer cents across all126
scheduled dates. Include inactive dates and mechanical zero trading PnL after
terminal closure, without treating missing data as zero or forgetting program
charges. Report Evaluation results, resets, billing units, PA outcome, payout
eligibility and any hypothetical withdrawal separately. Program fees are still
unpriced: no after-program-fee or withdrawable-profit claim is permitted.

Numerical Evaluation success remains distinct from sustained PA success and a
verified model. The economic development screen requires numerical Evaluation
success in both baseline and combined stress, a single Evaluation attempt per
route, and no hard breach or PA MAE violation. Separate full-route screening
additionally requires both PA paths to survive their observed calendar and reach
hypothetical payout eligibility. This remains development screening, not a
confidence statement about future success. Always disclose observed PA duration
and right censoring. A relative gain over a losing benchmark is not absolute
profitability. Forecast MSE, Sharpe, coverage and inference diagnostics are not
additional compulsory gates for an unrelated economic claim.

Paired differences describe this observed simulated path, not randomized causal
effects or unbiased expected profit. Preserve13,131 historical charged
comparisons. Before any v98 claim, freeze separate counts for the one new policy,
reused benchmarks, new economic contrasts and any bookkeeping reservation. A
reused benchmark is not automatically a new selectable or independent hypothesis.
The reservation is three conservative bookkeeping charges: one new policy and
two explicit economic contrasts. The primary NQ contrast and descriptive MNQ
contrast are not two more selectable policies. A successful claim therefore
moves the ledger to13,134, not before. No new count is reserved by this design
document or synthetic implementation.

## Independent Validation Remains Separate

The48 sealed dates stay closed. Before external assessment, fix the selected
candidate or learning algorithm, economic benchmark, meaningful margin, horizon,
dependence assumptions and endpoint decision rule. These choices and adequate
power remain unresolved; this document does not authorize opening the holdout.
No historical p-value or software test can certify the adaptive candidate.
Bootstrap samples do not create independent account trajectories, and resampling
realized daily PnL does not automatically estimate account pass probabilities.

v97 remains closed under its original gates. This is a new outcome-informed
execution policy, not a repaired prediction model or retrospective v97 pass.

## Implementation Ownership

- `tools/nq_apex_account_router_v98.py`: pure forecast/capacity proposal selection.
- `tools/nq_apex_routed_account_v98.py`: shared in-memory chronological account.
- Matching synthetic tests verify behavior, not market efficacy.
- `tools/nq_apex_routed_economics_v98.py`: phase-separated and paired economics.
- `tools/run_nq_apex_account_router_v98.py`: separate `--freeze` and `--run`,
  authenticated v97 closure, exact252-row restored forecasts before raw tape,
  eight independently replayed unchanged control accounts, full181-pair receipt
  equality and exclusive result publication. It never refits the source models.
- Frozen v97 code and evidence remain unchanged. Focused/full regression and
  independent review must complete before freeze; technical failures do not
  imply a strategy-performance result. No partial new policy metrics are shown.
