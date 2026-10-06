# V125 Results: Activity Recovered, Profitability Not Confirmed

Market computation ended October1 at16:30:47UTC with exit0. The user paused
research before postrun review. Explicit research resumption on October6
authorized the original no-fit verification, completion and separate saved
decision/account audit. All exited0; there was no second market run or refit.

## Outcome

The local joint-distribution model generated PA trades instead of V124's
complete abstention. All four paths remained alive through the observed period,
with zero recorded hard-threshold or MAE violations. None became payout-eligible.

| Mode | Inherited Evaluation Net | PA Net | PA Trades | PA Active Days |
| --- | ---: | ---: | ---: | ---: |
| Baseline | $3,254.00 | -$220.58 | 60 | 30 |
| Cost only | $3,292.00 | -$832.00 | 51 | 25 |
| Latency only | $3,130.20 | $912.50 | 59 | 33 |
| Combined stress | $3,429.00 | $689.00 | 54 | 30 |

Trading commissions/slippage are included; subscription/activation fees remain
unpriced. Evaluation prefixes are inherited unchanged and are not learning
gains from V125. Scenario books have different entries, sizes and paths, so a
positive stress result does not imply that costs improve the same trades.

The baseline PA loss, absence of payout eligibility, and failed baseline-plus-
stress benefit gate mean **no verified50K/full-route pass**. Right-censored PA
survival is not permanent survival. The four scenarios are not independent
samples. The sealed48-date holdout remains closed.

## Interpretation

The earlier inactivity obstacle was not an unavoidable consequence of the
account engine: the unchanged rules accepted positive local expectations and
executed60baseline PA trades. That does not prove local estimates are reliable.
Baseline stop exits lost $3,240.38 while targets earned $2,979.34 and the single
time exit earned $40.46. Trading more alone did not create positive net edge.
No neighborhood retuning, adverse-head removal, threshold rescue or deployment
was performed after seeing this result.

The already-declared V126 screen compares three direct mean-estimation families
on the same causal inputs before any subsequent account-path work. Its design
was declared before V125 economics were opened. It is not a V125 retry.

## Evidence

- Original single pass:181raw pairs,126scored chronological dates, three analog
  banks and four new continuous books; four V124 controls retained unchanged.
- Completion: `reports/nq_apex_local_distribution_v125_execution/execution-verification.json`,
  SHA `ecc7375544a5c9a2ab53b5182da77d53e568b1b55f539be1b7cc8440d21466ca`.
- Status SHA `dffe64f20b7270e33abd516394dd04774df79975ac50c2d5f704d0217276952f`.
- Seal SHA `e46f7c0eace75cbe4c7a6899780eeb19189345d8e7bfa2be2561c1c7ac455332`.
- Separate audit SHA `ebb4f16696edf442b853239cc4355ce5dc5b4b835357c1735c590b802a64bbb4`.

The verifier checked complete saved neighborhoods by an alternate selection
method. The separate audit checked saved CE decisions and recorded ledger/
lifecycle consistency. Shared numerical utilities and inherited source labels
are not independent raw-first-crossing reconstruction or independent validation.
Historical charges remain13221 for this result. Software checks do not change
the economic verdict; the earlier full-repository suite remains non-green.
