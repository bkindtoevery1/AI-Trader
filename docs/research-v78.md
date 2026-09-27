# Legacy 50K / EOD 50K ordered-tick replay v78

## Authority and fixed design

The user confirmed their actual account is Legacy 50K Evaluation. Legacy is
primary; EOD is a separately labelled counterfactual, not a selected substitute.
The old prerequisite 25K pass is superseded for new research. The hypothetical
six-contract question did not change the two-actual-contract control.

Before new execution outcomes, the study fixed the original v77 walk-forward
v63 signals on all 181 admitted raw-tick development dates, 2025-09-08 through
2026-06-12. It did not refit, invert, retune, select another date cohort, or alter
the frozen v63 runtime. Both accounts use two MNQ in Evaluation and one in PA,
the 187-tick stop from the slipped entry, baseline 10:02-12:00 ET, and mandatory
stress 10:05-11:57 ET. MNQ commission per side is $0.52 baseline/$1.25 stress;
adverse slippage is one/four ticks per side. Each side's commission and slippage
is counted once. Last ticks are an execution proxy, not bid/ask queue evidence.

The runner fully verified 362 files and 402,041,614 raw events, including both
NQ and MNQ and all rows outside the selected trade window. Trigger order follows
provider sequence, including equal timestamps. Stop gaps execute at the first
triggering observed price plus adverse slippage, never a fabricated stop fill.
Both baseline and stress complete for each account family, even if one account
fails earlier. The 48-session historical holdout remains closed.

This is a two-comparison exploratory account replay on previously observed
dates, bringing the ledger from 12,949 to 12,951. It is not an independent test,
two newly trained models, or evidence of successful live operation.

## Results

| Path | Evaluation attempts | Numerical Evaluation pass | PA / payout outcome |
|---|---:|---|---|
| Legacy baseline | 3 | 2026-03-16 | PA starts March 17; later inactivity closure; no payout eligibility |
| Legacy stress | 3 | None | Final Evaluation unfinished at June 12 |
| EOD baseline | 10 | None | Eight expiries, one threshold breach, one unfinished Evaluation |
| EOD stress | 10 | None | Nine expiries, one unfinished Evaluation |

Legacy baseline first failed two Evaluation attempts on intraday trailing
thresholds. Its third attempt met the numerical target and traded-day rule, but
the resulting PA later lacked two $50 net-profit days in a rolling 30-calendar-day
window. A numeric Evaluation pass is therefore not a surviving PA, first payout,
or a validated 50K model. Last PA journal date is May 22; closure can occur on
an intervening calendar day, so do not label May 22 itself the closure date.
The last five qualifying PA dates were April 16/20/22/24 and May 8.

An independent reports-only reconstruction places the policy's inactivity
closure on May 24: the April 24 qualifying day has left the inclusive 30-day
window, leaving only May 8. It also reconciled all 711 journal days and 572
trades across the four paths. Net trade PnL summed across all attempts was
-$501.28/-$1,054.00 for Legacy baseline/stress and -$774.68/-$1,256.00 for EOD.
These amounts include commission/slippage but exclude unpriced program fees;
the final reset account balance is not cumulative earnings or external cashflow.

The first-payout event was absent in all four paths. Neither account family is
recommended for conversion based on these results. This same-period ordered-tick
study must not replace or be directly subtracted from v77's different 282-date
minute-based results.

## Cost and compliance boundaries

An independent prefrozen review found two billing defects: treating each Legacy
reset as a new subscription and stopping billing at numeric pass. Both were
fixed before freezing or loading new tick execution outcomes. A reset preserves
the original monthly billing anchor, and evaluation fees continue until PA
conversion. A renewal during a failed interval includes the reset; otherwise
the declared next-session restart counts a manual reset fee unit.

Legacy baseline used one original subscription, six renewals, two manual resets
and one PA activation. Stress used one subscription, nine renewals, two manual
resets and no PA activation. Each EOD path used ten Evaluation purchase units.
These are modeled events, not purchases executed by the agent. Exact dollar
amounts, the PA fee plan and net external cashflow are unknown, not zero.
Conversion-day charges are conservatively included; no conditional refund is
silently applied without exact timing and approval evidence.

Legacy per-trade MAE uses the fixed conservative 30% research guard. Its failure
label does not claim an automatic official penalty. Planned risk/reward and
third-party signal-service compliance remain unverified. No actual order,
payout, account conversion, Telegram send, credential or schedule change occurred.

Sources: [Legacy billing](https://apextraderfunding.com/help-center/evaluation-accounts-ea/legacy-evaluation-subscription-billing/),
[Legacy refund conditions](https://apextraderfunding.com/help-center/everything-billing-subscriptions-cancellations-resets/legacy-refund-policies/),
[PA activity rules](https://apextraderfunding.com/help-center/billing/inactivity-policy-on-performance-accounts-pa/).

## Evidence and next research

Immutable policy: `config/nq-apex-50k-tick-replay-v78.json`.
Evidence: `reports/nq_apex_50k_tick_replay_v78/` contains the preoutcome lock,
start marker, complete report, failure attribution and result seal. The lock
binds 322 dependencies and every selected raw-pair identity.

Sixty focused mechanics tests and 3,438 full regression tests passed before the
market replay. Four additional result tests reconcile the completed source
scans, immutable lineage, original signals, journal fills, costs and fee units.
Synthetic fixtures test mechanics only, never strategy profitability.

Future model research must address predictive robustness and account-time
constraints, not simply relabel this numerical Evaluation pass. Do not shorten
the dataset, change v78 restart/stop/sizing rules, or retune after these results.
Minute-volume semantics were independently audited. Original v63 and v77
neural inputs already contain basic minute-volume channels; a causal relative-
volume feature or price-only ablation is a distinct counted experiment, not
the first use of volume. Preserve the existing frozen prospective lineage.

The fixed September 8, 2025 opening-window volume audit now matches every minute
to the raw quantity sum for both products. NQ totals 70,592 versus 66,143 raw
events; MNQ totals 187,588 versus 168,506 events. Raw quantities are not all one.
Original export, normalized CSV and readonly SQLite preserve these volumes.
This supports use as source-reported minute-volume features, not independent
exchange-volume certification or a whole-history quality claim.

The additive v54 attribution audit resolves the contradiction without changing
the frozen old report. Its 181-day metadata identity equals the old cache. On
the actual hash-matched first-day window, 63,948 of 66,143 NQ events and 156,348 of
168,506 MNQ events have unit quantity. Nonunit quantities reach 93 and 50.
Because at least 75% are one, the nearest-rank q75 is one, and the old `>=q75`
large-group definition captures every positive integer quantity. An empty small
group does not imply every quantity is one or any normalization occurred.
The old all-unit-normalization explanation is withdrawn; the feature-degeneracy
abort and its zero-trial disposition remain correct. Actual distributions were
recomputed only for the first day, not all 181 sessions.

Correction evidence is
`reports/nq_v54_volume_attribution_v1/audit-94e75642eb9be1d9581423776e6f6ce07408adabd19b385fd817a7724b9f72e7.json`.
Twenty additional tests cover the tied-quantile counterexample, frozen-rule
conformance, source identity and no-holdout boundary. Neither audit adds a
model trial or independently establishes exchange-level provenance.

Before a successor design, note that v76 already used total opening activity
relative to the median of the preceding 20 opening windows, as well as an
activity-weighted price displacement. Rebranding that aggregate as a new RVOL
feature would repeat an existing information set. A matched price-only ablation
or per-minute historical time-of-day normalization would be a distinct question,
but neither successor experiment has been frozen or run in this cycle.

Final integration: 140 focused mechanics/result/provenance/current-state tests
and 3,506 full regression tests passed. All 322 frozen dependencies reverified
after bookkeeping. The heartbeat prompt reflects the completed v78 comparison,
corrected volume attribution and active Legacy 50K target; its schedule and
target task did not change. These tests prove implementation checks, not a
successful trading model. The research goal remains active.
