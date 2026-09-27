# V110 NQ Selection, MNQ PA Execution

This implements one outcome-informed development candidate, not an economic
pass or a deployed operational replacement. The component is
`tools/nq_apex_selector_transfer_v110.py`; V102/V107 bytes remain unchanged.

## Hypothesis And Implemented Change

V107 changed both forecast source and execution product on entering PA. V110
holds the original causal V102 NQ selection fixed while preserving V107's MNQ
execution. Both original forecast sets must still validate before any quote is
read. Only NQ's original all-four-positive nomination mask is consumed. There is
no fallback, OR combination, mode selection, sign inversion, forecast rescaling,
new target or confidence-based sizing rule.

The separate pre-observation screen completed once at2026-09-13T05:52:23Z.
Source SHA606e5d9270b4e0a590d1b29ea27c67f59383687e3e838020244d537196241afd
and its frozen policy remained unchanged. Of3747 matched events,3236 are within
the unchanged140-tick PA stop support:42 selected by both,65 NQ-only,2 MNQ-only,
3127 neither. The67 disagreements span28 development dates, with2/3/23 dates
across the three folds. Parent independently reconciled these counts without
reexecuting the screen or reading account outcomes. The preselected heuristic
passes; concentration in the third fold remains a limitation, not independent
replication or proof of actual PA trades. Do not retune the informational gate.

## Preserved Mechanics

Evaluation remains original NQ execution. PA retains actual MNQ quotes, tick
value, commissions, slippage, positive-entry-net/5:1 geometry guards, target,
stop support, busy/cooldown logic, half-headroom reserve, MAE, trailing floor,
fresh-PA five-contract limit and existing prior-day six-contract unlock.
The inherited account alone owns cash, quantity and phase transitions. NQ
forecast dollar magnitudes are not MNQ expected PnL and do not determine size.

The subclass copies only the strict phase dispatcher necessary because V107
rejects subclasses in its process_day method. The only dispatch treatment is
forecasts[NQ] instead of forecasts[execution_product]. Existing day routing,
trade kernel and lifecycle are inherited. Complete-day mutation remains atomic;
invalid unused MNQ forecasts and late wrong-product quotes still roll back.

## Required Economic Replay

A separate source-admitted runner is now implemented and under synthetic
regression; it has not entered an economic claim or replay. Before any replay,
freeze one candidate plus one contrast against all four exact
completed V107 phase-micro controls. Preserve the original181 paired dates,
55 context dates,126 scored development dates, three causal folds and purges.
Authenticate original six model records and252 forecast envelopes. The eight
paths must reconcile all four unchanged Evaluation prefixes and own-product
raw unit-label evidence; no partial results may choose a policy or stopping time.

Relative benefit requires positive candidate-minus-control PA net in BOTH
baseline and combined stress, no additional hard/MAE breaches and no earlier
activity closure. Absolute positive PA net and full-route/payout gates are
separate requirements; favorable cost-only/latency-only results cannot rescue a
failure. Program fees remain unpriced, so trading net is not fee-adjusted success.
Frozen account rules are modeling assumptions, not newly certified compliance.

Only a unique, separate performance claim would reserve two comparisons,
13179 to13181 if the ledger has not otherwise changed. No such claim, fitting,
raw replay, new prediction or outcome exists for V110 now. The screen and
synthetic tests do not change the ledger or open the48 sealed holdout dates.
No Windows, order, Telegram, schedule or credential action is part of this study.

## Component Verification

The support screen tests passed60 cases, including40 new cases. The final account
integration selection passed176, including41 new component cases. Independent
static reviews found no substantive actionable defects. Synthetic cash/trade
fixtures test mechanics, not profitability. See
`reports/nq_apex_selector_transfer_v110_support/component_checkpoint.json`.

The earlier support-only full suite was deliberately interrupted after scope
expanded to account implementation. Its exit2/XML is retained as incomplete,
not a failed strategy or a complete regression result. Final-code full suite
session1448/PID84901 completed its XML and is no longer present. The original
raw tool exit could not be recovered; do not report the inferred exit1 as an
observed exit. XML contains15584 passes, two exact previously known failures,
23 skips and all81 new support/component cases passing. All3100 V109 dependency
hashes, six support-freeze pins and two component pins remain exact. Read
reports/nq_apex_selector_transfer_v110_support/verification.json and full.xml.gz.
This is not an all-green suite or an economic result. Do not rerun that completed
scope; the separate new economic runner requires its own final-scope regression.
