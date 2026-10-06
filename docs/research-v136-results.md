# V136: Causal Giveback Exit Results

Completed October 6, 2026. [Frozen design](research-v136-design.md).
Verdict: FAILED the development full-route and benefit gates. The fixed exit
improves realized Evaluation progress in baseline and cost-only conditions,
but neither resulting PA survives the observed calendar. Latency-only and
combined stress never pass Evaluation. This is not a verified 50K pass.

## Complete Results

One fixed trade-local exit arms when causal liquidatable net profit first
reaches the original conservative 1R reserve and exits on half-peak retracement.
Both commissions and adverse exit slippage are included; original account,
initial-stop and fixed-target guards retain priority. There is no promised
half-peak fill in a gap. V134 forecasts, sizing and lifecycle rules are unchanged.
Evaluation uses at most one actual NQ; PA at most six actual MNQ.

All 181 raw pairs / 402,041,614 ticks and 126 scored development dates were
processed. Eight account books comprise four new books and four exact V135
controls. No fit, inference call or retained training-label rebuild was added.
Trading PnL below includes the frozen trading costs, not unpriced program fees.

| Candidate Mode | Evaluation USD | Evaluation Pass | PA USD | Final State |
| --- | ---: | --- | ---: | --- |
| Baseline | +3,273.00 | 2025-12-16 | +686.62 | PA inactivity closure |
| Cost only | +3,483.00 | 2025-12-17 | -1,129.50 | PA inactivity closure |
| Latency only | +942.20 | No | Not entered | Evaluation right-censored |
| Combined stress | +582.00 | No | Not entered | Evaluation right-censored |

The controls reproduce V135 exactly: Evaluation +1,254.90 / +749.00 /
+398.60 / -48.00 USD in the same mode order; none enters PA. PA differences
therefore remain null, not zero. This is a whole-route comparison, not an
isolated MNQ effect or exposure-matched PA comparison.

Baseline executes 20 Evaluation fills over 10 processed dates, then 167 PA
fills / 872 total contracts over 110 processed dates. It becomes hypothetically
payout-eligible on February 27 with a modeled 500 USD withdrawal, but later
closes for inactivity; last processed PA date is June 3. No actual payout is
claimed. Cost-only executes 21 Evaluation and 56 PA fills / 250 PA contracts;
its last processed PA date is February 11, with no hypothetical payout.

Baseline/cost each use one purchase and one PA activation unit, with zero
Evaluation renewal units. Latency/stress each use one purchase and six monthly
renewal units. These are frozen Legacy lifecycle simulations, not verification
of the user's current cohort or the October promotional one-day-pass rules.

## Failure Attribution

| Mode | Armed Trades | Giveback Exits | Risk-Cap Rejections | Final Headroom USD |
| --- | ---: | ---: | ---: | ---: |
| Baseline | 55 | 25 | 21 | 86.62 |
| Cost only | 19 | 10 | 4 | 49.25 |
| Latency only | 12 | 3 | 238 | 292.85 |
| Combined stress | 7 | 1 | 253 | 262.50 |

The change can realize some formerly surrendered excursions and alter the
account path enough to reach PA. That is useful development evidence, but not
robustness: stressed paths still stall and PA headroom becomes very small.
There are no hard-threshold or PA MAE breaches in these four candidate books;
absence of breach is not a full-route pass. No outcome-driven threshold change,
automatic retry or successor selection was made in this run.

## Verification

Local frozen implementation `7c5b217`; public pre-execution design
`c2df324cae0a3449a72f3ea58c4d6d3a19549557` on
`codex/research-records-v136`, independently remote-head verified before replay.
Two comparisons remain charged, increasing the total from 13,256 to 13,258.

Focused tests: 502 unique passes, comprising parent account/runner 336 and
delegated source/replay 166 across two invocations. Affected regression:
1,093 passes, for 1,595 unique focused/affected cases. This is not one combined
focused invocation or a full-repository green claim. Real-source CLI preflight
exec16242 exited 0 without replay. A synthetic full-pipeline test exercises the
real account implementation in all four modes; fixtures are not market evidence.

Sole supervisor exec48940, parent94744, child94766 started 11:27:38 UTC.
Replay completed 11:53:38.585274 UTC; child terminal 11:53:39.002195 UTC is exit0,
source unchanged. Supervisor saved-result audit exit0 was observed at 11:56:17.
Both processes are gone; no separate third CLI audit or market rerun occurred.
Three sealed outputs and exact controls were verified. A separate read-only
arithmetic pass reconciled 16 phase records / 80 numeric totals and all 921
daily cash/attempt sums; all nine frozen source/design/test pins are unchanged.
This is consistency evidence, not independent numerical validation. In
particular, saved giveback metadata was not independently replayed to prove
raw first-crossing correctness.

| Artifact | SHA-256 |
| --- | --- |
| claim.json | `be4450c19c1c67144561896403ce115d26cb301da2b4ce3f2337984d992c3027` |
| accounts.json | `f7ac9aebb1c18ec850fcf1a29af56be963d0a9749830f08c5ec3c71bc235ef7c` |
| status.json | `28839f610fb6957227b1d6cd2b718ff6adf79d643613a7abc51cb16a399bcdde` |
| result_seal.json | `c7df2ef662653d0c14709c57af07e35334d0d2dd0b40aa702074ca8b482ce629` |
| execution terminal.json | `d4ac600b2c0f53fc37abfd47d59902294f901e60906d1e43119f2b247ece2525` |

All 48 sealed holdout dates stay closed. This is reused, outcome-informed
historical development, not prospective proof. No model deployment, order,
Telegram signal or purchase follows from this result. Separately, the user
requested Windows daily archival; that operational work is not model evidence.
The overall research/Windows goal remains active.
