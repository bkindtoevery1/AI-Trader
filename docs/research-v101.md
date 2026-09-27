# v101 Retained HGB Account-Utility Tuning

Completed 2026-09-08T08:21:42Z, sole exec49656 exit0. Economic development
and full-route screens failed; this was not a technical abort. The MNQ
derivative improved baseline and combined-stress trading PnL versus v97,
but no model achieved verified Legacy 50K success. Preserve v97 and v100.

## Actual Work

Two product-level HGB learning procedures, using the original nine-feature
representation and nine learning-rate/L2 settings. Selection reused 108
authenticated v100 inner prediction matrices; no inner model was refitted.
Across six chronological product/fold searches, 54 configuration comparisons
and 108 split evaluations replayed 432 fresh five-date account episodes
(2,160 scheduled account-days). Each setting was scored by the worst of
four execution modes' combined two-block net trading cents. Account balances
carried within each block, with independent fresh capital between blocks.

Then 24 new native outer fits, 24 validated heads and six scalers completed,
with 84 durable fit-stage receipts. These are not 24 distinct strategies.
The sole full raw scan covered 181 explicit NQ/MNQ pairs, 402,041,614 events
and 126 scored development dates. Eight new outer paths and eight exact v97
controls completed. Four outer bookkeeping charges take 13,142 to 13,146;
the 54 inner comparisons are recorded separately, not independent trials.

Chronological training prefixes, inner-only preprocessing, ten full-calendar
purge sessions, actual integer sizing NQ<=1/MNQ<=6, costs, execution and
separate Evaluation/PA lifecycle were unchanged. The 48 sealed dates remain
closed. Reused outer dates are outcome-informed development, not a fresh test.

## Economic Result

USD after modeled commissions/slippage, before unpriced program fees.
Evaluation and PA are separate simulated phases, not withdrawable cash.

| Product / Version | Baseline Eval | Cost-only Eval | Latency-only Eval | Combined-stress Eval |
| --- | ---: | ---: | ---: | ---: |
| NQ v101 | -818.60 | -957.00 | 3559.00 | 3053.00 |
| NQ original v97 | 3157.80 | 3143.00 | 3130.20 | 1693.00 |
| MNQ v101 | 533.88 | 240.00 | 1236.12 | 966.00 |
| MNQ original v97 | -739.00 | -952.00 | 2020.98 | 69.00 |

NQ v101 baseline/cost paths did not pass Evaluation. Its latency/stress
paths passed the modeled numerical Evaluation gate, then lost 847.90/566.00
in PA and closed for inactivity. Whole-path sums were -818.60/-957/2711.10/
2487 USD; these are not single-account balances or payouts. Executed trades
were 6/6/19/19. Neither mode-specific success qualifies the baseline-AND-stress
economic screen, and neither PA path survived.

MNQ executed 13/13/12/11 trades and remained in Evaluation in every mode.
Baseline/stress improved by 1272.88/897 USD versus v97, but neither reached
the account target. All MNQ paths and the two nonpassing NQ paths accrued
six modeled monthly renewal units. Fee amounts remain unpriced. Original
NQ control baseline/cost/latency passed numerical Evaluation then closed
in PA; these three control passes are not new-model successes.

## Attribution

Selected (learning_rate, L2) by chronological fold:
NQ (0.05,10), (0.05,1), (0.025,100);
MNQ (0.1,10), (0.05,10), (0.025,1).

Four of six selected worst-mode inner utilities were zero. Three selected
settings made no inner trades in any mode. The two strictly positive
searches were supported by only one or two fills per mode over ten dates.
NQ outer nominated events were 8/60/0; MNQ 24/0/1. Nominations are not fills.

The objective recovered some MNQ activity versus v100's zero trades, but
short-block utility selection still provided sparse and unstable evidence.
This describes observed limitations, not proof of a causal market mechanism
or overfitting. A lower prediction error and a higher short validation PnL
are both insufficient guarantees of sustained account performance.

NQ latency paths are not the baseline trade list minus a cost. For example,
on 2026-02-03 baseline lost 823.10 USD while latency took no trade due to its
then-current risk cap. Earlier fills changed balance and trailing floor.
A favorable delayed path must not be selected retrospectively as the strategy.

Retain the HGB family and tuning infrastructure. A subsequent study may
preregister stronger temporal support for utility selection or tune another
retained family; do not rewrite v101, fish modes/seeds, force trades to rescue
its result, relax actual account rules, or open sealed outcomes here.

## Evidence

- Lock: 10a147f84bcac6651926c40acb8ef0bc21fa54f5ab34bc69cdce9f557dc0a867.
- Claim: b3ad78f9ed934f216ecf1c518c91a511b8a72b487edfc546c555b1b7e618aa48.
- Status: 63942dde8675a588ae128a7bdf024cce7a3fed69902d4b08acfeb6c30753f654.
- Seal: 4244d1932fe041eb64a962570d23e05aa0df406be412851b7e56f1fd5258920c.

Before freeze, 127 focused and 11,206 full software cases passed. Both
independent code reviews closed. Parent postrun audit45440 exit0 reverified
2,313 dependencies, 13 installed runtime files, 45 captured core hashes,
84 receipts, six utility choices, 29,820 restored forecast mode values,
252 exact control envelopes and eight exact control accounts. No fitting
or raw replay occurred in that audit; summary reproduction alone is not
independent economic proof.

The independent standard-library saved-account audit reproduced on the parent
(exit0, chunkc8454e): zero mismatches across 432 inner episodes/2,160 days,
16 outer paths/1,886 processed days plus 130 terminal-padding days, 1,307 event
attempts, 765 fills and 1,008 paired daily differences. All six selections
matched; 292 inner episodes had no fills. This validates saved arithmetic,
not raw executable quotes, unseen-market performance or unobserved branches.
No actual breach/reset/payout occurred in these paths. The exact reproducer
and coverage limits are retained in independent_account_audit.json.
Terminal metadata checks passed 54 cases after correcting one stale v100
key-finding summary alias; the initial failing XML is preserved. No model or
economic-result byte changed to repair that reporting-only failure.

See reports/nq_apex_utility_tuning_v101/selection_attribution.json,
postrun_integrity_audit.json and terminal_evidence.json. No frozen code,
policy or result changed after observation. No orders, Windows deployment,
Telegram messages, purchases or broker activity occurred.
