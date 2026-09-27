# v86: Actual-Product Frozen-Midline Replay

## Current Status

One-shot actual-product replay completed at 2026-09-07T08:24:29Z:
**NO_MIDLINE_MEAN_REVERSION_50K_DEVELOPMENT_PASS**. All 181 actual raw pairs
and 402,041,614 events were checked. Four new comparisons, zero estimator fits,
cumulative 13,061; no Evaluation pass, PA entry or payout for any new candidate.
The run started at 08:16:00Z after the 08:15:23Z freeze, source metadata
preflight, 357 focused tests and 5,194 full regression tests (175.15 seconds).
Lock SHA-256 is
`7343bf557ee419e6d6e32a176db716b3f94d5f7b1f7ad994b5f11ab9d8568447`,
binding 410 dependencies including the unchanged 273 source modules. Four
comparisons were reserved before outcome access. Exec session 52799 exited 0;
the completed experiment must not be restarted. Independent numerical and
reports-only reconciliation passed. Post-result full regression passed all
5,295 tests in 176.99 seconds, with zero failures or skips. Completion evidence
is `reports/nq_apex_mean_reversion_research_v86/completion_audit.json`.
This goal turn is **progress**, not goal completion: both signal families and
actual-product account execution were implemented and evaluated, not merely
planned. The result does not validate a profitable 50K model.

The current user-authorized target is their actual **Legacy 50K Tradovate
Evaluation** account. The persisted old 25K/max-two-contract goal banner is
superseded for new research by the user's later account and sizing changes.
Original 25K results and operational bytes remain preserved, not relabeled as
50K evidence. This bounded cycle requests NQ1 or MNQ up to6 separately; no orders,
account purchase, conversion, credential changes or Telegram transmission.

## Completed Results

Amounts below are USD after modeled commission and adverse slippage, before
unpriced program/subscription/PA fees. Direct diagnostics ignore account risk
guards. Account results include actual quantity caps and skipped opportunities.
Baseline and stress are mandatory views of the same four candidates, not eight
new strategies or an opportunity to choose a better execution delay afterward.

| Family / Product | Direct Baseline / Stress | Account Baseline / Stress | Account Trades Baseline / Stress |
| --- | ---: | ---: | ---: |
| Reentry NQ1 | +362.10 / -1,379.00 | +362.10 / -1,760.00 | 9 / 5 |
| Reentry MNQ up to6 | +186.84 / -900.00 | +186.84 / -900.00 | 9 / 7 |
| Wick rejection NQ1 | -2,915.60 / +282.00 | -967.70 / -1,648.00 | 17 / 9 |
| Wick rejection MNQ up to6 | -2,052.24 / -105.00 | -1,839.62 / -105.00 | 24 / 24 |

Eight new account paths contain 1,448 daily journal rows: 104 executed trades,
28 risk-cap skips, 36 crossed-target skips and 1,280 no-intent flat days.
There were no hard breaches or MAE violations. All eight paths end
`EVALUATION_RIGHT_CENSORED`: reaching the end of observed data without passing
is not successful Evaluation or evidence of indefinitely safe operation.

Reentry produced nine raw signal dates; wick rejection produced 33. Target
geometry reduced baseline direct executions to nine and 26, both below the
unchanged 30-active-date gate. However, low frequency is not the only failure:
reentry loses under stress, while wick rejection loses in the baseline.
Family block-bootstrap p-value is 0.67616, and all global HAC Bonferroni values
are 1. Global DSR remains unavailable; the final holdout remains unopened.

## Failure Attribution

- Moving the old reentry exit to the fixed mean improved NQ baseline account
  PnL from v85's -1,150.50 to +362.10, with nine trades instead of five plus
  four risk skips. But direct PnL fell from +1,197.10 to +362.10. This is an
  account-path change, not proof that the mean target adds predictive edge.
- Reentry stress losses reject a simple "lower the activity gate" solution.
  Entry delay can consume the remaining distance to the mean; crossed targets
  are skipped rather than recorded as wins or replaced with later signals.
- Wick NQ's +282 stress direct result is not an account success. Its actual
  stress account loses 1,648, with 15 risk-cap skips. Selecting that delay only
  after seeing this result would be retrospective selection.
- A target hit can still lose after costs. Completed reports include NQ
  baseline direct -3.10 and MNQ stress -3.00 target exits. No minimum-profit
  filter is inserted retrospectively to remove these observations.
- This first-event-only, quiet-late design is not the user's full repeated
  discretionary Bollinger approach. A bounded repeated-opportunity experiment
  is a possible next hypothesis, requiring a separate freeze and trial count.
  No such successor has been implemented or reserved by this completion.

An independent agent reconciled all ten direct and account paths, including
the unchanged control, in 33 completed-evidence tests. Another independently
recomputed returns, Sharpe, HAC and family-bootstrap values using different
numerical algorithms; 68 synthetic tests passed and the actual sealed-vector
audit passed. All six prior-reference checks match exactly. The combined
post-result focused run passed 473 tests in 9.15 seconds. These are software
and report-consistency checks, not independent strategy validation.

## Frozen Question

The initial design is preserved in `docs/research-v86-design.md`. Its four
proposed comparisons are now implemented without adding a fifth candidate:

| Entry Family | Products | Fixed Target |
| --- | --- | --- |
| Outside-close Bollinger reentry, quiet late | NQ1 / MNQ up to6 | Completed NQ mean |
| Inside-origin wick rejection, quiet late | NQ1 / MNQ up to6 | Completed NQ mean |

The previous reentry arm had only nine active raw dates. With unchanged entry
selection, a new exit cannot increase that coverage and cannot satisfy the
existing 30-active-date gate. It remains a counted, outcome-informed payoff
mechanics extension, not a likely validation pass. The wick-rejection family
is a new entry hypothesis. Neither its frequency nor outcomes are used to
adjust thresholds or decide which arms get reported. All four are reported,
including zero activity and delayed-entry target skips.

Same causal thresholds as v85: 20-minute population Bollinger bands at 2 sigma,
previous bandwidth at or below its preceding 20 widths' linear 20th percentile,
positive current minute volume at most 0.8 times the previous 20 admitted
sessions' same-clock median, and absolute 5-minute SMA slope at most 0.25 ATR.
Only completed 10:30 through 11:30 ET decisions count. The first qualifying
event per family/day is never replaced, even if later execution is skipped.

Each intent carries exactly 21 contiguous completed NQ minutes. The last 20
closes give the fixed mean; their true ranges use the additional prior close.
ATR stops use exact rational ceiling of 1.5 ATR in native quarter-point ticks.
The absolute target rounds upward for LONG and downward for SHORT. It never
updates with later means. There is no minimum-profit filter. A slipped entry
already at or beyond the target means zero contracts, fees and PnL, not a win.

## Execution And Admission

Use the same 617 admitted minute-source sessions for prior causal references,
but score only the exact 181 raw development pairs from 2025-09-08 to 2026-06-12.
The 48 sealed final holdout dates remain closed. This is not a new train/test
split claiming independence: deterministic rules have no fitted labels, their
prior references are chronological, and reused development is outcome-informed.

Baseline entry is decision +60 seconds and exit deadline +5460 seconds. Stress
entry is +240 and exit deadline +5280. Source admission proves actual first
timely Last events. Each NQ and MNQ source is integrity scanned independently;
price paths are never manufactured by dividing one product's PnL.

The v85 window scanner and original risk-aligned fixed1 MNQ control remain
unchanged. The v86 adapter changes only absolute target geometry and explicit
skip attribution. It delegates to frozen v85/v78 risk sizing and lifecycle:
trailing threshold, strict MAE, inclusive DLL, stop, target, time, then final
adverse-fill/commission checks. Flat and skipped days still advance Evaluation,
subscription/reset accounting, PA inactivity and payout requirements. Prior-EOD
PA sizing unlock remains strict. Risk reserve is not a guaranteed loss bound.

NQ commission is 155/350 cents per side baseline/stress; MNQ is 52/125 cents.
Slippage is 1/4 ticks per side. Targets use first crossing Last plus adverse
exit slippage, not optimistic limit fills. Same half-headroom budget is not
equal exposure. Program fees, PA plan, planned risk/reward and signal-service
compliance still need evidence before a genuine completed operational route.

## Preoutcome Controls

`config/nq-apex-mean-reversion-research-v86.json` binds the exact catalog and
four-comparison count. The following records the already-completed invocation;
do not rerun it. Freeze and run were separate commands:

```sh
<TMP>/ai-trader-v77-venv/bin/python -B tools/run_nq_apex_mean_reversion_research_v86.py --freeze
<TMP>/ai-trader-v77-venv/bin/python -B tools/run_nq_apex_mean_reversion_research_v86.py
```

Only the run marker reserves four comparisons, moving 13,057 to 13,061 before
outcome access. A failed run retains its reservation and cannot restart. Full
results are published only after all 181 paired scans, reference conformance,
and final dependency/source/environment checks. Partial metrics stay hidden.

Practical baseline/stress PnL, Sharpe, HAC effective samples, family-bootstrap,
Evaluation, PA survival, payout and no-MAE gates remain unchanged from v85.
Direct `signal=0` for geometry skips ensures they do not count as active coverage.
Global HAC Bonferroni uses all 13,061 comparisons; global DSR remains unavailable.
Bootstrap has 2,000 samples, 10-session blocks and fixed seed 20260986.
There is no tuning, inversion, new seed, genetic algorithm or model fit.
Even a development shortlist would not itself be independent final validation.

## Implementation Review

- Signal module binds prefix/anchor/identity hashes and previous-session volume
  references, with exact inherited active reentry timing/direction/stop/prefix.
- Account adapter records proposed versus actual entry/target, zero-size reasons,
  first crossing, fees and unused risk budget; direct diagnostics are separate.
- Parent runner checks exact product/maturity/date pairs before price scans,
  all signal plans before replay, and the frozen original MNQ control afterward.
- An independent reviewer found a catalog could outgrow its reservation. Exact
  model keys, product/mode pairs, executable catalog and ledger are now checked
  together before metadata loading or freeze. Six synthetic mutations cover it.
- Independent final code review found no further substantive defect. Its
  47 focused synthetic checks are software evidence only. Parent owns full
  regression, actual source preflight, freeze and completed result review.

The manual page and human-action imitation trainer are not inputs to v86.
No automated QA label or screenshot is used as a model candidate observation.
