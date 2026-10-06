# V127 Results: Mixed Forecast Change, Account Economics Pending

Completed October 6, 2026 at 02:17:22 UTC. The sole supervised market process
exited 0 with unchanged source pins and no observer error. A subsequent audit
exited 0, required that exact terminal evidence, verified all 51 sealed output
files, and recomputed the saved diagnostics without another fit.

## Scope

The [fixed design](research-v127-design.md) adds three session-context inputs to
the original twelve local price/volume inputs. All 5,485 original events across
181 development dates received causal prefixes of 60 to 270 completed minutes.
The original local21 context hashes and original twelve features matched.

Three fifteen-input HGB pipelines fitted on the original 45/87/129-date mature
prefixes, with ten-session purges and three 42-date scoring blocks. This means
six scaler fits and twelve response-head fits, all individually journaled.
No market-fit warning was recorded. The exact V126 twelve-input HGB forecasts
were the control: no control refit or parameter change occurred.

Scoring retained 126 scheduled dates, 124 nonempty supported dates and 3,236
supported opportunities. The other 48 sealed dates remain closed. These are
reused historical development dates, not independent validation.

## Complete Forecast Comparison

Date-equal MSE change relative to retained V126 HGB; positive means worse:

| Scenario | Change |
| --- | ---: |
| Baseline | +1.1704% |
| Cost only | +1.4033% |
| Latency only | -0.1131% |
| Combined stress | -0.5715% |

Session context did not improve all four predictive scenarios. The third
chronological block had worse MSE in all four modes. The small pooled stress
improvement is not evidence of stable generalization or an economic pass.
No post-result feature removal, new threshold or alternate training was tried.

Descriptive event-weighted mean of original one-MNQ net labels among events
with all four predicted means strictly positive:

| Model | Selected opportunities | Selected dates / scheduled | Baseline USD | Cost-only USD | Latency-only USD | Stress USD |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Retained V126 HGB | 364 | 105 / 126 | 4.26 | 0.13 | 3.96 | -1.75 |
| V127 session context | 388 | 104 / 126 | 0.75 | -3.52 | 4.97 | -0.05 |

These values include the original execution-cost scenarios but are overlapping
counterfactual labels, not executed trades, additive profits or account PnL.
Empty/no-selection dates remain in the coverage denominator, not as fabricated
zero-return trades. Candidate selection does not establish calibration: its
realized cost-only and combined-stress means remained negative.

Candidate baseline/stress selected means by chronological block, USD per label:
3.51/1.31, 12.94/12.34, and -21.25/-19.77. The last-block deterioration remains
visible; no favorable block or execution mode is selected as the final result.

## Interpretation And Next Boundary

The context bundle changes forecasts but has not established a reliable
cost-adjusted advantage. This is not proof that all session context is useless,
nor does lower global MSE by itself establish tradability. This stage had no
preregistered economic pass cutoff; its economic verdict remains NOT_EVALUATED.

The next required economic step is a matched continuous account replay with a
declared identical point-forecast-to-action adapter for candidate and control.
V126 has no existing account book; do not pretend its forecasts are the V119
joint empirical distribution. Original commissions, latency, stops, contract
capacity, carried account state, cooldown, drawdown, PA activity and payout
rules must remain explicit. The existing V107/V115 point-forecast account route
is a code precedent to inspect, not automatic authorization to relabel units
or reuse an unmatched control. This note does not define a new selected policy.

V125 remains the latest completed continuous account study. No V127 account
replay, verified 50K pass, operational replacement, Windows deployment, order
or Telegram delivery occurred. No same-attempt retry or fit remains running.

## Verification And Evidence

Final affected qualification: 1,104 passed, 24 retained V126 synthetic-fixture
warnings, exit 0 in 62.06 seconds; source hashes match before and after. The
full repository suite was not rerun and is not claimed green. Five reviewed
defects were fixed before market execution: fit-guard scope, reused-dependency
binding, per-native-fit failure evidence, observed-terminal requirements and
supervisor exception cleanup. Synthetic tests are not performance evidence.

The audit shares summary code; it is not independent numerical or raw-tape
validation. The development minute source was reloaded and bound, while raw
tick target evidence was inherited from authenticated prepared labels. All
two reserved comparisons remain charged; cumulative total is 13,229.

SHA-256 identities:

- Claim: `19c8e05b5588e1eef2bcbbd7093947ba5ec8501714aac8c5720836ca412b19d5`
- Status: `0edd37033134dfc95b1cad8f73043f57d99dd7d9b8fb0874e6ced08bce1205ff`
- Result seal: `c58c873cd7cc0377f7b16dcd042fd27939c65349df8162879383f19d71e7b3af`
- Observed terminal: `9827898ea3575bbcabb0185ec9db5e78b236c96996239ca33dba43dbe951bf37`
- Qualified JUnit: `76635e237249a42ffe536cbb2b6a9852df617e63573be71ba5182aa82c54318e`

Detailed evidence is local under `reports/nq_apex_session_context_v127/` and
its sibling execution directory. Raw data and fitted artifacts are not public.
