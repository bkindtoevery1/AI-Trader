# V121 Abstention Attribution

Descriptive post-outcome audit, 2026-09-27. This supplements, and does not
replace, the completed [V121 result](research-v121-results.md). It neither
changes the frozen selector nor evaluates another trading policy.

## Evidence

The audit authenticates the completed V121 receipt and all immutable outputs,
then reruns 517,971 recorded-account arithmetic checks before aggregating the
stored quantity-choice tables. It checks input and source hashes again before
exclusive publication. No raw-market read, fit, inference, account replay,
alternative return or additional comparison charge occurs. Effective historical
trials remain 13,213; the independent holdout remains closed.

- Completion receipt SHA-256:
  `6d6cbc7bccf8d62648d7cfa1bfeba98b2eea75dcb991a811323aa9f7ba8092c5`.
- Audit: `reports/nq_apex_pressure_abstention_v121/audit-v1.json`, SHA-256
  `81a8ec2d4bb6466be6dcd957535b31e676235e7a55de1e9f0f98d01375445afb`.
- Focused qualification: 27 passed, exit 0. XML SHA-256
  `f818cc05c681b8de8e4955f8a616f7f8677d9ac54b9844b970e2ff2705aaa262`.
- Full regression for this additive diagnostic is not yet completed.

## Findings

Both pressure candidates made 2,210 quantity decisions across four correlated
scenario books. Every decision had positive capacity, selected flat, and had
one contract as the best *recorded positive* quantity. That diagnostic quantity
is not a trade recommendation: its utility was still below flat at zero.
The cost-only head was uniquely limiting at every such choice, with no ties.

| Baseline book | Equal-print | Volume-weighted |
| --- | ---: | ---: |
| PA quantity decisions | 561 | 561 |
| All four heads nonpositive | 155 | 161 |
| Mixed positive/negative heads | 406 | 400 |
| Best positive-quantity CE median, cents | -444.1140 | -448.7470 |
| Best positive-quantity CE maximum, cents | -68.0240 | -67.2168 |

These are stored certainty equivalents, **not realized or expected trading
PnL**. Counts across books are not independent samples. The margins exclude
a zero-rounding explanation. The inherited V119 control had five positive
quantity choices across its four books despite the same limiting head, so the
selector does not structurally ban all trading.

For the frozen utility, CE(q) = -H log(sum_i p_i exp(-q U_i/H)), with H > 0.
CE is concave and CE(0) = 0; therefore CE(q)/q cannot increase for q > 0.
If a scenario's one-contract CE is negative, increasing the integer quantity
cannot make that scenario's CE positive. This explains why merely increasing
the contract cap cannot rescue these recorded nominations under this selector.
It is not a claim about every strategy or an altered account objective.

Cost-only changes both commissions and slipped-entry geometry. Stress also
changes entry timing, so stress need not be worse on each individual price
path. The observed head ordering is not, by itself, a software defect.

## Limits And Next Hypothesis

Stored CEs do not separate expected-payoff effects from downside-risk penalties.
They do not establish that costs are unrealistic, tick pressure is useless,
or dropping the cost gate would improve PA outcomes. Some decisions have no
positive head at all. No relaxed-gate or alternative-PnL calculation was made.

A distinct research direction is execution-aware, price-constrained entry,
including expiry, nonexecution, adverse selection and occupied time in training
targets. V85's `bb_pullback` is a completed-bar recross followed by delayed
entry, not evidence of a resting limit order's fill. Last-only ticks cannot
prove bid/ask availability or queue priority. A successor must therefore use an
explicit market-entry rule after a causal trigger, or clearly label passive
fills as unverified assumptions. A touch must never be presented as proof of
an executable limit fill. Candidate policy and comparisons must be fixed before
new labels or outcomes are observed; this audit grants no model pass.
