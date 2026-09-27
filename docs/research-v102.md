# v102 Deferred Continuous-Utility HGB Tuning

Completed2026-09-08T10:13:37Z, sole market exec72659 exit0. NQ passes the
baseline-AND-stress first-attempt numerical Evaluation development screen.
Neither product passes the full PA/payout route; no verified Legacy50K success.
This is a retained-family tuning result, not independent market confirmation.
Preserve the originalv97 and the separately closedv100/v101 studies.

## Actual Work

Nine fixed learning-rate/L2 settings, unchanged original nine features and
execution rules. The first outer fold reuses the exact untunedv97 anchor.
Subsequent choices use immutable42/84-date continuous inner account snapshots.
Later account state cannot revise the earlier choice. Inner training prefixes
contain35/77dates; all purges use ten full-calendar sessions. Original outer
training prefixes and all126scored dates remain unchanged.

144new inner native fits plus16outer fits, eightscalers and496durable stage
receipts completed. These are two product-level learning procedures, not160
independent strategies. Retain36inner four-head bundles, four new outer bundles
and two reused first-fold bundles/eight heads. There are72continuous inner
books/6048scheduled days. Their144prefix reports represent9072overlapping day
slots; do not count them as144new accounts or add42-day and84-day profits.

The sole raw pass verified181explicit NQ/MNQ pairs and402041614events. Eight
new outer account paths and eight exactv97 controls completed. Savedv101
comparisons required no additional account replay. Six bookkeeping charges
take13146to13152;36inner configuration comparisons and54overlapping block
contributions are separately recorded, not estimates of independent trials.

## Economic Result

USD after modeled commissions/slippage, before unpriced program fees.
Evaluation and PA are separate simulated phases, not withdrawable cash.

| Product / Mode | Evaluation PnL | PA PnL | Whole-Path Sum | Outcome |
| --- | ---: | ---: | ---: | --- |
| NQ baseline | 3254.00 | -174.10 | 3079.90 | Eval pass; PA inactivity closure |
| NQ cost-only | 3292.00 | -814.00 | 2478.00 | Eval pass; PA inactivity closure |
| NQ latency-only | 3130.20 | -564.30 | 2565.90 | Eval pass; PA inactivity closure |
| NQ combined stress | 3429.00 | -1179.00 | 2250.00 | Eval pass; PA inactivity closure |
| MNQ baseline | -210.68 | 0 | -210.68 | Evaluation incomplete |
| MNQ cost-only | -446.50 | 0 | -446.50 | Evaluation incomplete |
| MNQ latency-only | 3367.92 | 30.70 | 3398.62 | PA still observed; no payout |
| MNQ combined stress | 3009.00 | -437.50 | 2571.50 | PA still observed; no payout |

NQ baseline/stress executed21/10trades. All four NQ modes reached numerical
Evaluation on the first attempt, without hard breach or MAE violation, then
closed for inactivity. MNQ executed23/22/26/26trades; only delayed modes passed
Evaluation and their PA observations remain right-censored. No path qualified
for a hypothetical payout or received actual cash. Do not select a favorable
execution mode retrospectively.

Versus originalv97, NQ baseline/stress whole-path sums improved96.20/557USD;
MNQ improved528.32/2502.50USD but still lost under baseline. Versusv101, NQ
baseline improved3898.50USD while stress declined237USD; MNQ baseline declined
744.56USD while stress improved1605.50USD. Longer utility history is not a
uniform improvement. NQ accrued four modeled Evaluation renewal units and a
PA activation per path; MNQ baseline/cost accrued six renewal units, delayed
paths five plus PA activation. Do not invent fee prices or net external cashflow.

## Selection And Limits

Selected(learning_rate,L2): NQ checkpoint1(0.05,10), checkpoint2(0.025,10);
MNQ checkpoint1(0.05,10), checkpoint2(0.05,1). The first outer fold was never
tuned. Chosen worst-mode internal utilities were203/0/0/279USD in
NQ42/MNQ42/NQ84/MNQ84order. Two chosen settings had no inner fills in any mode.
The final MNQ choice had nine fills per mode over84dates. Outer nominations
byfold: NQ8/3/99; MNQ0/0/45. Nominations are not actual fills.

Longer history did not remove sparse evidence or guarantee PA activity.
Forty of72unique inner books had zero fills. The independent audit found1218
inner risk-cap skips; these are a capacity limitation, not proof that skipped
trades should be forced. Keep the improved NQ family as a lead, while treating
PA survival and signal continuity as unresolved. Do not force uneconomic
trades to evade inactivity or silently loosen actual account rules.

PA failure alone does not establish overfitting. This study jointly changes
delayed tuning, account continuity, untuned first-fold anchoring and terminal
eligibility. It is not isolated causal evidence about horizon length. Reused
development remains outcome-informed; the48sealed2026-06-29through2026-09-02
dates stayed closed. No orders, Windows deployment, Telegram messages, broker
activity, purchases or schedule changes occurred.

## Verification

Implementation7d4df50 and frozen checkpoint50c6463 are local commits. Before
freeze,135focused and11341full software cases passed. Source-only41373 and
freezeaudit37650 passed. Lock binds2423dependencies/13runtimefiles; all51
captured core hashes remained unchanged. Initial fixture-date and draft-policy
failures, plus three mutable reporting failures, are preserved separately.

Parent audit18612 exit0 reauthenticated the source/lock and496receipts, four
immutable snapshots,36inner bundles and six outer records. It restored176436
inner mode values,19880new outer mode values and29820original control values;
252control envelopes,84anchor envelopes and eight control accounts matched.

Independent standard-library audit40210 exit0 reconciled144prefix reports,
72unique continuous books,16outer paths and eight savedv101 paths;2016paired
differences matched. Unique inner coverage:6040processed days plus8terminal
pads,1952attempts/581fills. Outer coverage:1935days plus81pads,772attempts/
369fills. No mismatch. Snapshot overlap is counted separately, not as new
trading. No actual breach/reset/payout branch occurred in these journals;
the audit does not prove unexercised branches or raw quote completeness.

Initial audit39054 failed because the new auditor looked for mode on the
head wrapper instead of its nested predictor. The initial script is preserved.
Only the unpinned audit adapter changed; repaired90723 and tightened40210 both
passed with byte-identical reports. No frozen study/result was repaired.

Postrun reporting has a preserved compatibility limitation. The hash-bound
legacy account-transition test assumes candidate count equals ledger charges;
v102 has four candidate records but six charges, including two saved-v101
contrasts. It also expects an obsolete derived-output alias. Do not falsify
the sealed report or edit the frozen test to satisfy those assumptions.
Terminal metadata9665 produced37passes/one incompatible legacy failure.
The explicit postrun successor contract27297 passed4cases and verifies the
actual model, comparison and alias units. It was added after observation, not
used for model selection. The unrestricted legacy suite is not claimed green.

Status606e5d9270b4e0a590d1b29ea27c67f59383687e3e838020244d537196241afd;
seal caa0fbb500756913a3007b316c4f382c2a7a575f37e0f28780515d027ac248b5.
Lockc24aa2581b2252e447fc0de3aba67dfb1ed4a0543448f3f527d79d2b9c5eac31;
claim147ba8a6a22565e7f68ec62b6b2d3535f8c9a250bf1632b4a32415205fc76ba6.
See the result directory's selection_attribution.json,
postrun_integrity_audit.json and independent_account_audit.json.
