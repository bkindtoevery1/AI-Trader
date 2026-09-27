# v103 Retained-Model PA Capacity Result

Completed 2026-09-08T12:11:25Z, sole market exec90619 exit0.
The unchanged v102 NQ model improves PA results under one fixed allocation
change. It does not pass the complete Legacy 50K PA/payout/compliance objective.
No new estimator fits, deployment, orders or independent validation occurred.

## Actual Experiment

Retained six exact v102 product/fold model records and their 24 heads. Restored
252 source forecast envelopes, then replayed eight new PA-capacity paths and
eight exact v102 controls. Only PA entry headroom allocation changes from one
half to two thirds; MAE/DLL, product caps, signals, stops, targets and execution
rules remain unchanged. Every candidate owns its subsequent account state.

All 181 explicit NQ/MNQ pairs and 402,041,614 events were verified in one raw
pass. The 126 scored dates are reused development, not fresh out-of-sample
evidence. All 48 sealed dates remain closed. Four bookkeeping charges move the
ledger from 13,152 to 13,156; these are not independent-trial estimates.

## Economic Results

USD after modeled commissions/slippage, before unpriced program fees.
Evaluation PnL and PA PnL are separate simulated phases, not withdrawable cash.

| Product / Mode | Evaluation PnL | PA PnL | PA Fills | Result |
| --- | ---: | ---: | ---: | --- |
| NQ baseline | 3,254.00 | 781.30 | 27 | Alive through 34 observed PA sessions; no payout |
| NQ cost-only | 3,292.00 | -1,366.00 | 8 | PA inactivity closure after 20 sessions |
| NQ latency-only | 3,130.20 | 3,839.10 | 39 | Alive through 37 sessions; hypothetical withdrawal 500 |
| NQ combined stress | 3,429.00 | 891.00 | 32 | Alive through 34 sessions; no payout |
| MNQ baseline | -210.68 | 0 | 0 | Evaluation incomplete |
| MNQ cost-only | -446.50 | 0 | 0 | Evaluation incomplete |
| MNQ latency-only | 3,367.92 | 30.70 | 9 | PA still observed; no payout |
| MNQ combined stress | 3,009.00 | -437.50 | 7 | PA still observed; no payout |

All Evaluation rows and pass dates exactly match v102. NQ baseline/stress PA
improves by 955.40/2,070 USD from -174.10/-1,179 USD. PA fills rise from 11/2
to 27/32; risk-cap skips fall from 36/26 to 22/5. Old NQ controls close for
inactivity while these two new paths remain alive to the calendar end.
This identifies allocation as a material bottleneck within this simulation,
but not the only problem: cost-only PA loses another 552 USD and still closes.

All MNQ economic paths are unchanged. The latency-only NQ hypothetical payout
date is 2026-05-11; no actual payout was received. Never substitute this mode
for the preregistered baseline-and-stress requirement. Neither product passes
the full-route gate. PA paths alive at the data boundary are right-censored,
not proof of indefinite survival. NQ still incurs four Evaluation renewals and
a PA activation per mode; exact prices and PA fee plans remain unverified.

## Compliance And Learning

The new NQ paths contain 3/1/2/1 nominal stop/target ratios above five across
baseline/cost/latency/stress. The controls contain two more, nine in total.
These were reported, not silently filtered. No hard-threshold or MAE breach
appeared in the 16 journals, but that does not certify the complete rulebook.
Planned risk/reward and system-influenced PA signal operations remain unverified.

Retain the improved NQ family. Do not rerun v103 with another fraction, rewrite
v102, or turn increased trade count into a success definition. The user's new
complementary-ensemble direction is recorded separately in
docs/research-ensemble-reuse-plan.md; no ensemble has been fitted by this study.

## Verification

Freeze25446 and integrity5478 exited0: 2,963 dependencies, 13 runtime files and
60 captured source/evidence hashes match. Parent postrun audit11875 exited0,
restoring six models and all 252 forecasts again, verifying 252 candidate copies,
eight exact controls and eight exact Evaluation prefixes. Independent audit77894
exited0: 16 paths, 1,960 processed days plus 56 terminal pads, 684 attempts,
403 fills and 1,008 paired daily differences reconcile with zero mismatches.
The hypothetical payout branch was exercised in one saved journal; the audit
does not certify raw quotes or unexercised breach/reset branches.

Prefreeze focused188 cases pass. Unrestricted full regression95070 has 11,528
passes and one preserved frozen legacy metadata incompatibility (4 records
versus 6 v102 charges), not a new execution failure. Separate audit adapters
pass 23 synthetic cases. The unrestricted suite is not claimed green.

Status62dd2b43e4a1056ae41850ebbcf6ffccaaa2e60da2c1deeb5901ffb9cc2e1742;
seal452417db7a63e3246327ce3a11816b980667d526100cdfb399267b8498392e22.
Lock4b08c1db26dc4ed62f7ff1e95f20a61e7e1d247c6b3dea33770a4ef2fa140d79;
claim9f6f159c72181a99f12db2ea9b8df11a5c2b95b8fe279bf16497793899337c5e.
Implementatione643673/5a6bb52 and checkpoint3fa74f5 are local, not pushed.
