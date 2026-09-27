# V118 Existing-Data Result

Status: completed and audited development experiment; not a successful model
or verified personal Apex account pass. Windows and new collection were not
prerequisites. No order, deployment, holdout access or data purchase occurred.

## Experiment

Used 181 admitted explicit-contract NQ/MNQ session pairs from 2025-09-08 through
2026-06-12, with 126 chronological scored dates starting 2025-12-03. Three
training prefixes of 45/87/129 sessions each precede 10 purged sessions and 42 scored
sessions. Fitted three 64-tree conditional-outcome forests once, shared by two
policies: fixed risk tolerance and current own-account headroom. The original
strategy was the control. Four execution modes produced 12 account books and
1,512 scheduled account-days, including terminal zero padding.

One claim charged five comparisons, increasing the ledger from 13,201 to 13,206.
The historical development dates had been used before; chronological separation
does not make this an independent holdout or justify a statistical promotion.

## Outcome

PA trading PnL in USD, after modeled trading costs:

| Policy | Baseline | Cost Only | Latency Only | Stress | PA Trades |
| --- | ---: | ---: | ---: | ---: | --- |
| Original control | -1271.14 | -1588.50 | 1470.00 | 742.50 | 22/15/25/24 |
| Fixed tolerance | 0.00 | 0.00 | 0.00 | 0.00 | 0/0/0/0 |
| Own headroom | 0.00 | 0.00 | 0.00 | 0.00 | 0/0/0/0 |

Both new policies abstained on all 4,420 recorded utility decisions across their
eight books and closed for PA inactivity. These repeated book observations are
not 4,420 independent trading opportunities. In each baseline/stress candidate
book, 561 decisions all had capacity for 5 MNQ and risk tolerance of 250,000 cents.
The cost-only certainty equivalent was never positive, so none satisfied the
four-positive-CE entry rule. Zero capacity and absent data were not the cause.

With no PA fill, headroom never changed; fixed-H and own-H stayed identical.
Consequently this experiment provides no realized contrast that demonstrates
a dynamic-headroom benefit. Avoid interpreting zero losses as a successful
strategy: both failed activity/survival and payout requirements. All three
relative-benefit contrasts and every modeled full-route gate failed.

The unchanged Evaluation path passed numerically in every mode. Baseline
Evaluation PnL was 3,254 USD; this is inherited control behavior, not an improvement
from the new learned policies. Evaluation pass and PA success remain separate.
Program fees are unpriced and the user's exact account cohort is unverified.

## Verification And Reflection

The actual market child 44401 exited 0 at 2026-09-23T03:13:38Z. Source audit 59378
exited 0, restored all 126 daily distributions and verified 4,420 utility records,
four controls and eight exact Evaluation prefixes without refitting or replay.
Independent recorded-account audit 67205 exited 0 after 429,720 checks. This is
ledger reconciliation, not a second independent intratick simulator.

Qualification: 706 focused passes; 19,402 full passes, two documented pre-existing
failures and one Windows-only skip. Counts use unique testcase nodes. A first
qualification rejected two timestamp-bearing ZIP test IDs; original evidence
was preserved and a narrow timestamp-only correction was fully requalified.

The first account auditor had two schema mistakes: population metadata was
compared with binding metadata, and the false risk-reserve-guarantee flag was
omitted from its expected allocator record. The v2 auditor verifies the exact
binding digest/mappings and the false flag; 205 synthetic tests passed. Original
audit failure files, market results and fitted models remain unchanged.

Do not retune or rerun this closed V118 attempt. A subsequent research design
should examine cost-aware action/quantity selection using training data only,
with explicit trial accounting. This is a proposed next hypothesis, not an
already evaluated alternative or permission to drop costs. Merely waiting for
Windows data would not address the demonstrated all-abstention failure.

Authoritative evidence:
- `reports/nq_apex_state_distribution_v118_execution/execution-verification.json`
- `reports/nq_apex_state_distribution_v118_execution/failure-attribution.json`
- `reports/nq_apex_state_distribution_v118/status.json`
- `reports/nq_apex_state_distribution_v118/result_seal.json`
