# V140r1 Results And Failure Attribution

October 7, 2026. The completed technical continuation succeeded; the economic
experiment failed. This interpretation reads the complete immutable result,
not partial outcomes or a new trial. It supplements the preserved
[completion record](research-v140r1-progress.md).

## Account Outcomes

USD trading PnL includes modeled commissions and adverse fills. Evaluation and
PA are separate phases/accounts, not one summed ending balance. Program fees
remain unpriced. A dash means PA was not reached, not zero observed PA profit.

| Mode | Eval Trades | Eval PnL | PA Trades | PA PnL | Ending State |
| --- | ---: | ---: | ---: | ---: | --- |
| Baseline | 17 | +3,537.30 | 122 | +660.62 | Modeled PA inactivity closure |
| Cost only | 17 | +3,071.00 | 102 | -1,633.50 | Modeled PA inactivity closure |
| Latency only | 32 | +3,250.80 | 106 | +1,894.26 | PA survives observed calendar |
| Combined stress | 34 | -78.00 | - | - | Evaluation incomplete |

Baseline PA is $6.92 below the exact saved V139 control. The latency-only result
does not rescue failed baseline/stress gates. Modeled withdrawals are not real
payouts. No confirmed 50K pass, independent validation or live promotion.

## Not Simply Too Few Trades

The frozen `legacy_post20260301` engine tests at least two daily net profits of
$50 in a rolling 30-calendar-day window. Merely placing a trade does not satisfy
that rule. This explains its modeled closure; it is not verification of the
user's current official cohort terms.

- Baseline first fails on May 23, 2026, during the gap after its last processed
  May 22 session. April 24-May 23 contains **nine days with trades**, but only
  April 24 earns at least $50 (+$248.76). The other positive date earns $44.52.
- Cost-only first fails on May 9. April 10-May 9 contains **seven days with
  trades**, but only April 13 qualifies (+$220).
- The candidate's longest trade-free processed runs are 6/9/5/103 sessions in
  baseline/cost/latency/stress order. These counts are not the rolling calendar
  activity rule. Dates after terminal closure are not filled with zero returns.

Therefore, saying "PA failed because it did not trade" is incomplete. Increasing
frequency or placing token trades would not by itself resolve the modeled rule
or the underlying losing days. The analysis does not relax it retrospectively.

## Minimum Contract Bottleneck

All zero-capacity attempts reconcile with the frozen allocator and conservative
one-contract reserve. Raising the maximum permitted contracts cannot make the
minimum executable position smaller. The reserve is not a guaranteed loss cap.

| Mode | Zero-Capacity Attempts | Unit Reserve Exceeds Entire Headroom | Fits Entire Headroom But Not Allocated Budget |
| --- | ---: | ---: | ---: |
| Baseline | 12 | 6 | 6 |
| Cost only | 11 | 1 | 10 |
| Latency only | 0 | 0 | 0 |
| Combined stress | 200 | 179 | 21 |

Stress last trades on January 9, then has 103 inactive processed sessions. Its
final recorded opportunity has $348.50 headroom, $174.24 allocated risk budget
and $647 one-NQ reserve. This is a mechanical skip explanation, not proof that
skipped trades would have won. No discarded event's return was reconstructed.

The new read-only attribution reconciles each executed attempt to daily PnL,
commission, slippage and quantities, and each daily total to saved phase totals
for all eight candidate/control books. It partitions skip reasons, preserves
unattempted events and reconstructs only the frozen activity calendar. The
Evaluation unattempted log is not a complete full-calendar nomination census.
This does not replace independent raw-tick first-crossing verification.

## Next Hypothesis

V140's both-product MSE still loses to the training mean in all four modes;
fold 3 nominated returns are negative throughout. Its 24 training-only means
are themselves negative, so a new mean-policy replay would just abstain under
unchanged nomination. Prior V93/V94 mean-policy failures already document this
problem. A mean's lower MSE is not a tradable positive edge.

The separate [V141 design](research-v141-design.md) asks whether a fixed,
sample-size-normalized ridge extracts useful conditional information from the
same targets and features with less flexibility. This is a matched learner
comparison, not a claim that ridge is new or that regularization fixes capacity.
No new market fits or trials were made for this interpretation. Seven V141
comparisons are only planned; current effective trials remain 13,277 and all
48 holdout dates stay closed.

Complete result SHA256:
`18fcc2ed06d2ff4930903e2835ce68ee56c7f5b7ded813e79f8112d6fbb2a751`.
The local read-only analysis is `tools/nq_apex_capacity_attribution_v140.py`.
Detailed source/model/financial artifacts are not part of public documentation.

