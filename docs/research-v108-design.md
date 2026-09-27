# V108 Product-Correct MNQ PA Support

Status: account component implemented; structural forecast audit completed;
economic replay deferred before any claim. No new market result is available.
The latest completed study remains V107's separately preserved integrity repair.
Its original technical abort and repaired negative economic result stay closed.

## Hypothesis

V107 kept NQ Evaluation and used the original causal MNQ V102 forecasts and MNQ
raw tape in PA. It also deliberately retained the NQ-derived 140-tick PA stop
support. That matched experiment reduced risk-cap exclusions but did not improve
both primary modes or achieve PA payout. Greater activity is not an edge.

V108 is one different execution-support policy, not a newly trained estimator.
It replaces only that inherited support with MNQ initial-PA risk feasibility.
Nomination uses the already completed stop geometry, not future entry quotes,
realized returns, target fills, product ranking or a later account balance.
The fixed reference budget is min(floor((250000-1)/2),75000-1) = 74999 cents.
The frozen MNQ stressed per-contract reserve is 50*stop_ticks+650 cents.
One MNQ is initially feasible through 1486 ticks (74950 cents), not 1487
(75000 cents). This is a frozen engine derivation, not newly verified broker
rules or permission to risk that entire amount on every trade.

The actual execution allocator still applies each account's own current cash,
trailing floor, MAE, stressed reserve and quantity limits. A nominated signal can
remain unfilled because of current capacity, nonpositive net target, the original
5:1 nominal stop/target guard, busy time, cooldown or a terminal account state.
The reference support does not expand when this account later becomes richer.

## Matched Comparison

Before any new market replay, the runner must freeze one candidate and one
contrast against the exact completed V107 phase-micro control. Both use the same
NQ Evaluation, MNQ own-product forecasts, explicit raw pairs, four execution
modes, account lifecycle and source-admission boundary. No additional fitting,
forecast scaling, model choice, stop optimization or early outcome inspection.
The source must authenticate the original six model records and 252 forecast
envelopes; unavailable forecasts stay abstentions, never invented predictions.

The intended replay retains all 181 raw dates, including 55 context dates and
126 previously used scored development dates. It must reconcile the exact four
V107 controls, unchanged candidate Evaluation prefixes and both products' raw
unit-label journals. Reusing these dates is not independent validation. Keep
the 48 sealed holdout dates closed.

One policy plus one contrast would add two charges, 13177 to 13179, only when a
new unique run claim is actually published. This document and synthetic tests
reserve nothing. No repair, retry, reselect, refit or parameter change may be
made after that claim to rescue its result. An integrity abort remains visible.

Economic benefit requires positive candidate-minus-control PA trading PnL in
both baseline and combined stress, no added hard/MAE breaches, and no earlier
inactivity closure. Disclose absolute PA profitability independently of that
relative gate. A full modeled route additionally needs Evaluation numeric pass,
observed PA survival, payout eligibility and no hard/MAE breach in both modes.
Cost-only and latency-only results remain diagnostics, not selection options.
Program fees remain unpriced and official compliance is not certified.

V108 cannot replace the fixed operational model merely by passing software
tests or improving one observed mode. Orders, Telegram, Windows deployment,
schedules and credentials are outside this component's authority.

## Observed Structural Support

After this design was written, a read-only sidecar found sparse incremental
nomination support in the existing V102 forecasts. The parent independently
reproduced the counts with `tools/audit_nq_apex_micro_support_v108.py` against
the pinned saved status SHA
`606e5d9270b4e0a590d1b29ea27c67f59383687e3e838020244d537196241afd`.
There are 126 MNQ envelopes with 3747 events, stops 19 through 405 ticks.
All 511 events beyond the old 140-tick support have available finite forecasts,
but only one additional event passes the original all-four-positive rule:
44 old nominations versus 45 new, with one incremental nomination date.

This is an observed forecast-support diagnostic, not a preregistered minimum
sample gate and not a finding that the candidate would lose money. No entry
quotes, raw replay, account PnL, model restoration or full source readmission
were used by this audit. A difference originating at one nomination could later
propagate through account state and cooldown; those divergent trades would not
provide independent replications of the treatment.

The economic comparison is therefore deferred. Do not change the cutoff,
forecast sign rule, mode or date set to manufacture additional support. Record
one structurally screened hypothesis, zero new performance comparisons and
zero trial claims; the effective performance-comparison ledger stays 13177.
V108 is neither a failed economic backtest nor a promoted model. The useful
product-correct account component remains isolated for an explicitly designed
future study with genuinely informative support. V107 stays the latest
completed economic study.

## Verification

Focused regression passed all 164 cases, including 74 new component/audit cases.
Full pytest completed with 14706 distinct passes, 2 unchanged historical
metadata failures and 23 skips (14731 case nodes). Its aggregate XML test count
is 14820 because of existing subtest accounting; do not use that as independent
case coverage. The complete suite exited1, not a globally green result. All
74 new cases passed and 20 captured source/evidence hashes remained unchanged.

The old failures are the V102 candidate-count-versus-comparison-count assertion
and the unavailable V88 historical temporary XML reference. A separate central
metadata check reports 16 passes and those same two failures. No assertions,
immutable evidence or trial counts were altered to hide these failures.
The exact focused/full/metadata XML bytes are retained as gzip archives under
`reports/nq_apex_micro_support_v108_preflight/`, with hashes, actual case counts,
source bindings and scope limitations in `verification.json`.

## Implementation Boundary

`tools/nq_apex_micro_support_v108.py` leaves frozen V105/V107 bytes unchanged.
It reuses the original risk and mixed-execution kernels and copies only the
strict phase dispatcher required by V107's exact-class guard. Entire days commit
atomically; invalid pairs, forecasts or late quote failures leave prior state
unchanged. Synthetic fixtures test mechanics, never market performance.
