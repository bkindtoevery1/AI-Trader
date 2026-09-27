# v88 Completed Research

## Current State

The frozen run completed at 2026-09-07T10:44:58Z, exit 0. All 181 dual-product
raw pairs and 402,041,614 events were processed, with 126 scored dates, six
multioutput fits/24 heads and four counted comparisons; cumulative trials are
13,073. Never restart or retune this completed run. Internal report/algebra
audit passed; its 94 focused tests passed. Postresult full regression passed
6,415 tests, with no failures or skips (JUnit duration 254.010 seconds).
JUnit SHA256: `e52994666e56a108e31dc2c7e1875eeea826c88fd71d1562aca7d013d4475b39`.
The completion packet was published at 2026-09-07T11:47:39Z after rechecking all
444 dependencies, source metadata, environment, sealed bytes and the independent
internal-consistency audit. A later full regression passed 6,492 tests with no
failures or skips, including all 493 v88 model/label/orchestration tests and
94 audit tests. This is software/evidence verification, not a strategy pass.
Completion audit SHA256:
`a38545240e621cee070762dc45daf242dde711b2301bd0e865696d54a76e3f07`.

NQ conditional baseline net PnL was +3,129.00 USD on nine active dates/ten fills,
reaching numeric Evaluation pass only on the final scored date, 2026-06-12.
Stress net was +1,852.00 USD, without Evaluation pass. Coverage, family-adjusted
p=0.287856 and stress Evaluation gates failed. PA never started; it was not an
observed PA survival failure. MNQ baseline +683.88 USD and stress +1,077.00 USD
did not pass Evaluation. No verified Legacy50K model is claimed. The six
monthly renewal units are tracked but exact program fee amounts remain unpriced.
All-mode prediction MSE exceeded the training-mean forecast by 2.6-7.0%; selected
tail profit alone does not establish broad predictive skill. No rescue tuning.

Sealed status SHA256: `4d10e24e0bd8ec94fa8ceecb9369a335aa3930f13dfaf37a8257efaa215efb9f`.
Result seal SHA256: `6de006dbfb4993f18011b67eccbfd8dce319ad90f5a84b4803d86c551c119455`.
Failure attribution SHA256: `0318f2453eeedf8ebd923640647c9f7b855c5857b1f20187c9f0786a4c62c0e9`.

Implementation commit: `1dc3192`, local only. Freeze at 10:35:29Z bound 444
dependencies. Structural preflight passed at 10:35:42Z with 80 possible active
dates and 185 events on the 126-date scored suffix, not performance evidence.

Lock SHA256: `6df2696f9ab3978a4e7804e517328baabe013657b4718e0b4923861d398350d0`.
Preflight SHA256: `914359885a94928750b07fb9329ea4eecd61ef69166e30ed6cc0db0575363992`.
Run marker SHA256: `bc19713fdbe9bfa2ac52b218e6a6e45af9074486ec6eda7d4430fc67e0c46ec2`.

Prior goal turn classification: progress. v87 completed and its reports passed
an independent internal-consistency audit; the user-requested trusted-LAN
manual evaluator was implemented with 5,828 passing regression tests. The
current goal turn returns to main model creation/evaluation, not LAN maintenance.

## Software Verification

The combined focused run passed 508 tests in 8.22 seconds: 289 model tests,
124 label tests, 80 orchestration tests and 15 mutable central-state tests.
Full regression passed 6,321 tests in 238.21 seconds, with no failures or skips.
Synthetic tests do not count as strategy evidence.
The planned immutable closure has 444 dependencies; metadata admission still
contains 181 raw dates and all 426 frozen v87 dependencies remain unchanged.

Independent review corrections before observations: source preflight now binds
to the authenticated completed v87 status as well as its own sidecar; prediction
requires exact scoring-date membership, not just an enclosing date range; fold
IDs and training counts require native integers. Eight initial model rejection
tests exposed the scalar-type gap and now pass without weakened assertions.
The design's volume-history wording was corrected to preserve v87's actual
cross-maturity history rather than claim a nonexistent same-contract reset.

## Evidence Behind The Change

An independent completed-report audit found uncapped v87 direct baseline NQ
recorded gross PnL -2,190.00 USD, commission 520.80, slippage 1,680.00, net
-4,390.80 across 168 fills. Six-MNQ direct baseline gross was -2,103.00,
commission 1,042.08, slippage 1,002.00, net -4,147.08 across 167 fills.
The gross add-back is an accounting identity on the recorded execution path,
not a separately replayed zero-cost strategy or isolated entry-quality effect.

Guarded account results differed because risk admission rejected many entries:
uncapped baseline NQ had 111 risk-cap skips; MNQ had 92. Smaller account losses
are not proof of profitable entry forecasts. Further cap changes do not address
the demonstrated lack of net expectancy. Original sealed v87 evidence stays
unchanged; this additive diagnosis adds no model trials.
Its immutable accounting report is
`reports/nq_apex_intraday_opportunities_v87/cost_path_attribution.json`, SHA256
`e3023607dca95422b4fa75e32a10f56687b97fada1d0efb8989933fecad446b8`.

## Planned Training Geometry

The read-only structural design audit found three 42-date scoring blocks:

| Fold | Scoring | Training Raw Dates | Training Events / Event Dates |
| --- | --- | --- | --- |
| 1 | 2025-12-03 through 2026-02-06 | 45 | 48 / 24 |
| 2 | 2026-02-09 through 2026-04-10 | 87 | 118 / 53 |
| 3 | 2026-04-13 through 2026-06-12 | 129 | 190 / 81 |

The last 126 scored dates contain 185 original opportunities on 80 dates.
This is only a coverage upper bound before model rejection, costs and account
admission. Every fit excludes ten full-calendar sessions before its block.
The first 55 raw dates are warmup, not silently omitted OOS returns. The small
first training group does not establish statistical power.

Read `docs/research-v88-design.md` for the exact information, weighting,
multioutput target, unchanged uncapped execution and development gates.
Source/execution conformance, synthetic tests and historical screen passes
must never be called independent confirmation. The 48-date holdout stays closed.

## Next Hypothesis

v89 will separately predict target-hit probability and the signed conditional
net-R for target-hit and other outcomes, retaining skips and losses. It is an
outcome-informed change to the forecast objective, not a retuned v88 threshold,
contract count, clock or risk gate. Two product models, geometry-only controls
and exact v88 controls are planned as six counted policies; none is reserved
until its own immutable preflight passes. Previous goal turn: progress, including
completed v88 evidence and the user-requested Replay Lab deployment correction.
