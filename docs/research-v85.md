# v85: Bollinger Entries On NQ

## Status

Frozen2026-09-07T06:46:04Z; started06:46:28Z after184 focused and4549 full
regression tests passed. Completed07:00:49Z with181 raw pairs/402041614 events,
395 locked dependencies and all four exact v84 conformance checks.
18 comparisons reserved, cumulative13057; zero fits. No complete development
pass. All38 sealed direct vectors and the18-candidate bootstrap family passed
independent numerical recalculation. Post-run focused tests:346 passed.
Final full regression: 4,923 passed in 171.93 seconds. All 395 frozen
dependencies, source metadata and environment were rechecked. See the additive
`reports/nq_apex_bollinger_product_research_v85/completion_audit.json`.
This includes the parallel manual replay and v86 mechanics software tests;
neither is additional v85 market evidence. No model passed full development.
The previous completed research made concrete progress: v84 completed181 raw
dates,16 multioutput fits and all4365 regression tests, but no verified model.
Inherited ledger13039. The user's latest request makes Bollinger research
primary, emphasizing1NQ and observable signal confirmation. NQ's cost advantage
motivates the product comparison; a1000USD winning day is not strategy evidence
or a daily target to fit. Preserve the latest Legacy50K goal and older frozen
EOD25K/MNQ runtime evidence without conflating them.

## Design

Nine causal rule policies: five band-reentry variants, plus band breakout and
trend pullback with base and confirmed variants. Signals use completed NQ1minute bars only,
20-period SMA/population standard deviation and2sigma bands. Decisions occur
at minute closes09:50-11:30 ET. Each variant takes only its first eligible
decision, entering60 seconds later to allow manual signal consumption.

The latest user observation was incorporated BEFORE any freeze or outcome:
reentry may work better with narrow bands, LOW volume and after the opening.
Compare reentry base, narrow-band-only, low-volume-only, quiet combined, and
quiet combined after10:30ET. Narrow means preceding band width in the bottom
20% of its previous20 minute-width readings; low volume is at most0.8 times
the previous20 complete sessions' same-clock median. Quiet additionally
requires absolute MA slope at most0.25ATR. The late variant skips the first
hour after09:30, not a later window chosen after seeing performance.
Breakout/pullback confirmations retain high volume (at least1.5 times median)
as contrasting continuation hypotheses, together with narrow prior bandwidth
or aligned MA slope respectively. No future day volume, labels or fitted success probability.
These variants can choose different first entry times, so the comparison is
not a same-event isolated volume ablation. The volume-only auxiliary research
already completed separately and is not a prerequisite here.

Both products execute the same NQ-derived intent on their OWN ordered Last
ticks. NQ requests1 actual contract; the MNQ matched-budget comparison requests
up to6. Half-headroom, DLL, MAE and conservative plan limits determine actual
size. Same budget rule is not equal exposure or identical future budgets.
Record unused budget and integer capacity, not just gross return.

A common initial stop is1.5 times completed20-minute ATR, rounded up to ticks;
target is2R, both anchored to the slipped entry. This isolates entry families;
it is not the full dynamic-middle-band mean-reversion exit recipe. Hold at
most90 minutes, with no bracket widening or trailing. Stress adds180 seconds
to entry, subtracts180 from exit and uses the unchanged more adverse v78
product costs. Stops and targets use first crossing of actual ticks with
adverse exit slippage, not invented within-bar ordering or optimistic limits.

Nine signals times two products gives18 counted candidates; no estimator fits
or parameter search. Reserve18 before any new outcomes for total13057. Repeat
the first v84 model/stop/fixed1 control, with its original MNQ stop-only route,
dates and Legacy journals, to verify the wrapper and source windows. Control
reproduction is not another candidate or a choice of the best prior result.

Directional coverage changes BEFORE outcomes: at least30 active dates total,
not25 in each direction, because support for both directions is not a forced
long/short quota. Other baseline/stress, Sharpe, HAC, family-bootstrap,
Evaluation, PA survival, payout and MAE gates remain unchanged. Sparse models
cannot be promoted from a few impressive days. All development dates are
already observed exploratory history;48 sealed holdout dates stay closed.

John Bollinger explicitly distinguishes a band touch from a complete buy/sell
signal, recognizes continuation outside bands, and discusses confirmation and
bandwidth. The rules here are research hypotheses, not claims endorsed or
validated by the source: [Bollinger's rules](https://www.bollingerbands.com/bollinger-band-rules).

## Completed Outcomes

Guard-free signal PnL AFTER trading costs, not funded-account cashflow.
NQ is1 contract; MNQ is6 contracts, not equivalent exposure.

| Rule | Active dates | NQ baseline USD | NQ stress USD | MNQ baseline USD | MNQ stress USD |
| --- | ---: | ---: | ---: | ---: | ---: |
| Reentry base |181|238.90|2503.00|460.56|-426.00|
| Reentry narrow |125|-14962.50|-19360.00|-10320.00|-12954.00|
| Reentry low volume |79|-6204.90|-12353.00|-4305.96|-8250.00|
| Reentry quiet |19|-1448.90|-3083.00|-949.56|-2061.00|
| Reentry quiet late |9|1197.10|-238.00|690.84|-243.00|
| Breakout base |181|2028.90|-29247.00|-2944.44|-20406.00|
| Breakout confirmed |99|-3206.90|-12408.00|-3752.76|-9228.00|
| Pullback base |180|-1253.00|-20905.00|-2548.20|-15474.00|
| Pullback confirmed |26|-12610.60|-14957.00|-7668.24|-9249.00|

Quiet-late is not a validated winner: only9 signals and stress reverses its
positive baseline. Its actual Legacy NQ baseline path executed5 trades,
skipped4 for the risk cap and lost1150.50USD, instead of the guard-free
1197.10USD gain. Its MNQ path took all9 and gained690.84USD baseline,
but lost243USD stress and did not complete Evaluation.

Basic reentry numerically passed only the baseline Evaluation: NQ2025-09-26,
MNQ2025-10-01. Both subsequent PA paths closed for inactivity without payout;
neither stress path passed Evaluation. Across36 new account paths there were
6239 journal rows,479 executed trades and2840 risk-cap skips. No hard threshold
breach is not proof of success when the policy largely stops trading.
Family bootstrap p=0.9845077461269365; all global HAC Bonferroni pvalues=1.
No rule met all development gates or qualified to open the sealed holdout.

The result does not disprove the user's full discretionary strategy. This
study is first-event-only and fixed2R, not middle-band profit taking or
multiple reentries. A new mean-reversion exit model is a separately designed
and counted exploratory hypothesis, not a retuned or reclassified v85 pass.

## Boundaries

New tools/config/tests only. No edits to frozen source, src/aitrader modules,
historical results or operational runtimes. No live orders, Telegram messages,
secrets, network setup, purchases, account conversion or schedule changes.
Exact program fees, PA plan and signal-service compliance still need evidence.
