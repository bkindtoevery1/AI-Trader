# V122 Abstention Attribution

This is post-completion analysis of saved V122 evidence, not a new model trial.
No forecasts were regenerated, selectors rerun, fits/replays performed or holdout
opened. The trial ledger remains 13215. The failed original result is unchanged.

## Finding

All 2210 PA decisions had capacity five but selected zero. All 11050 saved
positive-quantity robust certainty equivalents (CEs) were negative; one contract
was best among positive quantities in every decision. These correlated decisions
are not independent samples. Every decision binds the third saved forest.

The sufficient rejection mechanism is a negative expected one-contract payoff
in the cost-only head for every decision. A risk premium worsens that head, but
is not necessary to explain rejection under the frozen four-head minimum.
The observed result does not support a risk-penalty-only explanation.

| Book | Decisions | Own Mean Negative | Own Mean Positive, CE Negative | Own CE Positive, Minimum Negative |
| --- | ---: | ---: | ---: | ---: |
| Baseline | 561 | 408 | 35 | 118 |
| Cost only | 510 | 510 | 0 | 0 |
| Latency only | 578 | 166 | 9 | 403 |
| Stress | 561 | 489 | 63 | 9 |

Each row partitions decisions using that book's own head. Cost was the unique
limiting head in 521/474/527/521 decisions; stress in 40/36/51/40. No head ties.
Some individual-head means were positive in 412/372/429/412 decisions, but none
had all four means positive. V121's negative-CE/cost-head pattern repeats.

## Reproduction And Qualification

Exact conditional means/probabilities were not published: the runner strips
distributions. Do not describe these as directly recorded means. The five saved
CEs per head and retained model outcome support instead bound the mean.

With headroom H, one-contract payoff U and Z=exp(-U/H), the retained CE(k)
determines moment Mk=exp(-CE(k)/H). Let a=min(1,min Z) and r=max(abs(Z-1)) over
the saved forest support. Fifth-order Taylor bounds for -log(Z) give:

```text
P5/H = -5(M1-1) + 5(M2-1) - (10/3)(M3-1) + (5/4)(M4-1) - (M5-1)/5
P5 <= E[U] <= P5 + H*r^4*(M2-2*M1+1)/(6*a^6)
E[U] <= H*(1-M1 + (M2-2*M1+1)/(2*a^2))
```

An independent parent calculation reproduced the agent's sign-count partitions
at 60-digit precision while allowing every recorded CE to vary independently by
plus/minus 0.001 cent. Interval propagation retained every sign. Maximum fifth-
order interval width was 0.035125 cents; the highest cost-head mean upper bound
was -16.739347 cents. The looser second-order upper bound alone was at most
-9.340356 cents for every cost-head decision, also strictly negative.

The numerical allowance is a diagnostic sensitivity assumption, not a formal
bound on all production floating-point errors or a changed selection epsilon.
Bounds describe the model distribution, not true future or realized profit.
Saved evidence does not isolate commissions from slippage or entry geometry.

`reports/nq_apex_v122_abstention_audit_v1/reproduce.py` reads only exact pinned
status/completion files and writes JSON to stdout. `audit.json` retains the
actual parent output. The code asserts model/population identity, headroom,
quantities, stored minimums and complete decision counts. It imports no model
runtime and cannot fit, replay, modify policy or submit orders.

The persisted script reproduced every reported numeric field (apart from its
execution timestamp), actual exit0. Eight synthetic arithmetic cases separately
checked that the known mean lies within the fifth-order interval and below the
second-order upper bound. These are mathematical checks, not trading evidence.
No model/runtime source changed and the full repository suite was not rerun.

Status SHA256: `8c0b3220f7fbda71b5480352ceae091fbab080a1501e0e2d037a2cde3177de3f`.
Completion SHA256: `1177eb294c914632f1d5b59bdde4e4d908f1e106b7dabfbef0fda74be8c61f68`.

## Research Consequence

Increasing quantity cannot reverse a negative modeled unit mean, and dropping
only the risk premium would still leave the cost head negative in this batch.
The next candidate should address cost-adjusted conditional edge or demonstrate
a specific cost/label implementation defect. Do not claim that looser tests,
another entry trigger or more contracts have solved this failure. Any new policy
requires a separate declared comparison; this attribution selects no replacement.
