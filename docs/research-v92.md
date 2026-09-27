# v92 Research Outcome

Previous goal turn classification: progress. v91 completed failed Legacy50K
Evaluation/development, internal audits and7494 full regression tests; local
closure commit92425d8. Its493 frozen dependencies and result seals are preserved.
The intervening human Replay Lab question was answered without changing research.

The one-shot raw replay exec42296 completed exit0 at2026-09-07T16:17:20Z.
All181 explicit NQ/MNQ pairs and402,041,614 events were verified;126 dates were
scored after55 warmup dates. Actual counts:6 main plus6 control estimator fits,
48 learned output heads,10,970 counterfactual labels, four counted comparisons,
13,091 cumulative comparisons. These are not13,091 distinct fitted models.
All21 exact v91 source/control assertions passed. No restart, refit or holdout
opening occurred. Internal numerical/account closure audits and final7719-test
regression passed. All relevant one-shot/test exec sessions are terminal.

## Completed Result

Status: `NO_SOFT_REGIME_50K_EVALUATION_DEVELOPMENT_PASS`.

| Product | Account Baseline USD | Cost-Only USD | Latency-Only USD | Stress USD |
| --- | ---: | ---: | ---: | ---: |
| NQ x1 | -1415.50 | -1525.00 | -1057.40 | -1153.00 |
| MNQ up to6 | +2107.80 | +1983.00 | +842.04 | +762.00 |

Amounts sum actual risk-guarded daily trade PnL, after modeled trading costs,
before unpriced program fees. Neither product completed numeric Evaluation,
entered PA or reached payout eligibility in any mode. Each path accumulated
six monthly renewal units; these are billing units, not a verified cash amount.
No hard account breach or reset occurred. No verified50K model is claimed.

Broad opportunities increased from185 on80 dates to3747 on126 dates. Nevertheless,
all-four-mode positivity selected only35 NQ events on8 dates and7 MNQ events on3.
Neither product selected anything in the first scoring fold; NQ fold selections
were0/4/31 and MNQ0/1/6. There was no daily fill cap. Baseline account fills were
5 on3 dates for each product; stress fills were4 NQ and3 MNQ on2 dates each.

NQ guard-free baseline signal profit was+3243.70USD on23 fills, not the account
result. Its account had four model-stop fills, one target fill and19 risk-cap
flat attempts. Risk constraints prevented the later guard-free recovery.
Latency-only/stress guard-free NQ PnL was-3132/-1632USD. Higher costs can alter
admissibility and execution paths, so stress is not simple fee subtraction.
MNQ profitability is sparse and below the numeric Evaluation target, not a pass.

Five of eight broad product/mode forecast losses were worse than their own
causal training means. Broad and narrow aggregate MSEs cover different event
populations and are not a paired feature comparison. Breadth and two features
changed together; this run cannot isolate their causal contributions.
Lowering the active-day screen alone cannot repair missing Evaluation passes or
NQ account losses. Do not rescue this frozen result by changing thresholds,
direction, leverage, risk gates or the final holdout. The next separately counted
design must address predictive information and executable risk geometry.

Terminal status SHA256:
`c16fc925db89ee90be2536d103dd5d6ff9252bf96a6edd18c464ce25e05bfa1b`.
Result seal SHA256:
`922afca031c6e1489b0b8e6dad31e9a5d6afa6d519082d196ce204e4fbc7f9c9`.
Failure attribution SHA256:
`0fd4e7015c723fa4d1af773dfc5f80fe19ae29117b8e9b9399ef0733d207c03a`.
All509 dependencies, source metadata, supported runtime pool identity and the23
inherited environment fields matched in the parent's postresult check. This
integrity result is not independent raw-tick or strategy validation.

## Internal Closure Checks

Two read-only agents found no discrepancy. Numerical reconstruction checked all
12 fits,43,880 label-mode journals and31,456 prediction scalars without calling
estimator.fit. Maximum prediction and MSE deviations were3.72e-15 and7.33e-15;
maximum weighted normal-equation residual was2.93e-14. All780 full-calendar
legacy events and21 exact source/control assertions matched.

Account review checked16 direct plus16 account paths,2016 daily rows per scope.
Direct attempts/fills/skips were192/167/25; account counts198/103/95. Account
journals included70 main-NQ risk-cap skips across the four modes. Fees, embedded
slippage, sizing, risk reserves, nonoverlap/cooldowns, cash continuity and frozen
screens reconciled. No raw first crossings or bootstrap probabilities were
regenerated, and no standalone auditor was saved. This is internal consistency,
not independent market, liquidity or strategy validation.

Internal audit SHA256:
`9299aed88fbaabd82cecfa3d278bf1f1eb538402f957a4da1b70c1caca7d700e`.
Postresult focused regression passed239 tests in27.284s, XML SHA256
`dd97cf9ed6c75f9077cb4038af0f4fe59ee62f8cf7fa41007b23bf6e4d817831`.
The unfrozen central-state test now binds the sealed result and checks broad
opportunity counts, first-fold abstention, actual account money/fills, risk-cap
skips, fees-unpriced flags and the absence of Evaluation/PA/payout success.

Full regression exec92371 completed exit0:7719passed, zero failures/errors/skips,
313.429s. XML `<TMP>/ai-trader-v92-postresult-full.xml`, SHA256
`861a568b2193eb84db9faaef19c63728d060a3306f67b35f835aa256452d3771`.
All509 frozen dependencies/source metadata/environment/pool bindings were
reverified afterward. Completion packet published2026-09-07T16:29:59Z, SHA256
`c790940e52b1fc20396a1634e42badf9fbbd96c0e80cb9fe98f2ea8ef43c9be6`.
The packet closes this failed research batch, not the active50K goal. There were
no new closure fits, market comparisons, raw replays or operational changes.

## Implementation And Freeze History

Parent owns runner/policy/docs. One worker owns pure extraction/model/tests,
another performs read-only integration review. Existing live Replay Lab services,
human records, frozen model/runtime bundles and operational routes are untouched.

The initial three workers stopped on account usage errors. The user's explicit
retry resumed the same work, without source extraction, reservations or model
restarts. Core implementation and166 v92 synthetic tests are complete;423
core/prior focused checks passed. Parent core plus central checks passed180.
The initial combined check passed236 tests before the final bounded window-cache
addition. Final focused/full regression and the subsequent freeze are recorded below.

Read-only integration review found no unresolved source, chronology, feature,
narrow-label, account or report integration blocker. This is static internal
review, not independent market verification. Parent fixed diagnostic closure:
every policy/product/date and event population must exactly match the complete
scoring calendar and its own broad/narrow label group, including empty dates.
The runtime enforces supported numerical pool limits and records actual pool
identity/counts, rather than trusting the inherited constant environment label.
The initial493 v91 dependency bytes and all23 environment fields remain exact.
The new dependency closure contains509 paths, frozen after the checks below.

All workers have completed and been closed. Final focused check passed238 tests
in25.754s, including166 pure model,58 runner and14 central tests. This is the
post-cache version; both cached/uncached synthetic journals and separate
product/day cache lifetimes match. XML:
`<TMP>/ai-trader-v92-prefreeze-focused.xml`, SHA256
`84561bb7edf8241c3664f173d10cb4acf4fc7cb1cd9584b02ead15e805d35887`.
Full regression exec42584 finished exit1:7717passed and one failure. An unfrozen
volume-evidence state test assumed that a preparation-stage primary cycle
already had a run marker. It now distinguishes zero-reservation preparation
from a hash-bound executed run, preserving the historical ledger and auxiliary
volume checks. No frozen file or strategy gate changed. The original XML is
preserved at `<TMP>/ai-trader-v92-prefreeze-full.xml`, SHA256
`7acadf3d9d69dbfe419cd7dc097f0c2ae85e914b237653dec97fe9f131a3cf94`.
The repaired state checks passed18 tests. Full regression exec26504 completed
exit0:7718passed, zero errors/failures/skips,304.631s. XML:
`<TMP>/ai-trader-v92-prefreeze-full-final.xml`, SHA256
`3f4f731ad3a3d275809cdad8991d538b67f635a9ed7521008d6fb3ecfc2bcdf9`.
Neither regression handle remains running. No actual model run has been restarted.

Implementation commit234dca9 is local only. Freeze exec31468 completed exit0 at
2026-09-07T15:52:27Z and bound509 dependencies. Lock SHA256:
`4491452db93876cc2b9fc636343440988ab0e114d88c24b8a3ca786e1a7180eb`.
The actual supported pool record is libomp/OpenMP with1thread. This does not
attest to unsupported libraries or historicalv91 pool settings. Never edit the
six new frozen files or any inherited frozen dependency. Structural preflight
exec50110 completed exit0 at2026-09-07T15:53:15Z. Preflight SHA256:
`abdb6d83d42158c13e98c5e2ad20679bfb5a8e204150a3647057215be4b07142`;
seal SHA256 `e9cec4dec3acb5cb4b713ae991366428f9be24793156ec26145a7edea1d1b524`.
The broad scored stream has3747 events on126 possible dates; the exact narrow
control has185 on80. All780 original full-calendar events match byte-for-byte.
Training support is1430events/45dates,2670/87 and3899/129 after the full-calendar
purges. These are opportunity upper bounds, not actual fills or statistical power.
Exec42296 was launched once after that gate and is now terminal. Its
run_started.json SHA256 is
`23cae61822b315f5140240a6d8461ea33828ae35f78c305ee95f5f7424e87335`.
Source/preflight revalidation finished before the four-comparison claim and new
raw labels. The first55 pairs were warmup; no partial performance was exposed.
Never restart the completed run, alter its509 frozen dependencies or open the
final holdout. Live Replay Lab services and human records were untouched.
