# v94 Proposal: Ex-Ante Feasible Exposure

Status: SUPERSEDED_BY_PREFREEZE_DESIGN. See `research-v94-design.md` for the
implemented matched target-space experiment. The account risk rule is unchanged;
the initial-capacity proxy is not a new budget or dynamic-account guarantee.
No actual model fit, trial reservation or new outcome inspection has occurred.
Cumulative comparisons remain13,097 until the gated one-shot claim. This
proposal is retained as design history, not executable authority.

## Failure Evidence

v93 added three family interactions but improved none of the eight pooled
product/mode MSE comparisons against v92. NQ guard-free baseline profit was
6,592.70 USD, while its continuous guarded account lost631.70 USD and recorded
30 risk-cap skips. MNQ lost in both paths. This does not show that removing
guards or adding leverage would succeed.

Older v89 did fit its target-hit/conditional-payoff decomposition:96 new fits,
not a zero-fit support abort. It improved some errors against v88 but lost to
training means in all eight product/mode comparisons and produced only four
selected NQ events, zero MNQ. v90 increased forecast agreement and activity,
but imposed negative transfer on delayed modes and still failed account
Evaluation. Do not repeat either version while misattributing its failure
to missing data or an arbitrary daily trading cap.

## Proposed Question

Does learning payoff in ex-ante affordable dollar exposure, instead of unit
stop-normalized R on every event, improve an executable small-buffer policy?
This changes the learning objective and its feasible population deliberately;
it is not another family-feature expansion or a rescued v93 threshold.

Use the unchanged broad v92 causal event definitions and nine predictors as
the starting reference, without v93's rejected interactions. A risk-budget
rule must be tied to an independently stated account-risk rationale, not
chosen by searching the observed stops, returns or v93 losing dates. Fix the
rule, product limits, whole-contract rounding and handling of unaffordable
events before looking at new feasibility statistics. Do not treat absent
labels or untradable trades as fabricated market returns.

The comparison must separate two effects: changing the learning objective
and changing execution/risk policy. The unchanged fitted reference must run
under the same proposed risk policy as the new learner; unchanged historical
account paths may remain contextual references, not falsely exact controls
for a different executor. Include a causal simple-mean or no-information
control on the same feasible population. Do not count derived outputs as fits.

## Admission Questions

- Is there adequate chronological training and scoring support per product
  under the fixed whole-contract risk rule, without inspecting future labels?
- What is the truthful estimand for unaffordable events, and which paired
  denominators prevent an apparent error improvement from trivial zero exposure?
- Can the target be constructed from authenticated existing unit journals
  without assuming overlapping counterfactual trades form a portfolio?
- Can identical, already authenticated unit labels be reused with exact source,
  cost, horizon and hash bindings, while new account decisions still receive
  the required ordered raw-price execution evidence? This is an efficiency
  opportunity, not permission to weaken provenance or substitute labels for
  account-path replay.
- Which out-of-sample policy/utility checks match the new objective? Do not
  retroactively replace v93's global-MSE hypothesis gate. Do not infer genuine
  alpha from a few selected profitable dates or a better guard-free curve.

Keep the chronological folds, purging, fees/slippage, separate Evaluation/PA
assessment, closed48-session holdout and no-order boundary. No genetic
algorithm, risk-budget grid search, source-admission weakening or postoutcome
threshold change is proposed. Reject or redesign this draft before observation
if it cannot isolate its hypothesis; the version number is not a reason to run.
