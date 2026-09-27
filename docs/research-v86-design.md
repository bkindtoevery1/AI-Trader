# v86: Frozen-Midline Mean Reversion

This is the initial design snapshot. Current integration/run status is recorded
in `docs/research-v86.md`; the original no-run scope below describes that snapshot.

## Status And Boundary

DESIGN AND PURE MECHANICS ONLY. No v86 backtest is running or completed. No
raw data, market outcome rerun, fitting, preregistration freeze, trial
reservation, account connection, order, Telegram message, purchase, schedule,
commit or push is part of this work. Synthetic tests are software checks, not
development evidence, independent validation, a 50K pass or promotion evidence.
Only this document and the new v86 helper/test files are changed. Existing
frozen files, all `src/aitrader` modules and operational runtimes stay untouched.

v85's completed result seal binds the status and preoutcome lock hashes. Those
bindings were checked before parsing status. It completed at
`2026-09-07T07:00:49Z`: 9 signal rules, 18 executable candidates, 181 raw dates,
402,041,614 events, zero fits and no development pass. Its status also contains
one historical control, not a nineteenth new candidate.
`docs/research-v85.md` now records the completed run; parent owns final
full-suite evidence and research-state updates.
No candidate returns or rankings were used to select new thresholds.

The inherited cumulative comparison count remains **13,057**. All prior
development dates are outcome-informed. A future authorized four-comparison
run would require separate admission/reservation to reach 13,061; nothing is
reserved now. No genetic algorithm, model fitting, threshold sweep, optional
fifth candidate, selective retries or result-dependent rule revision.

## Bounded Hypothesis

v85 attached an entry-relative 2R target to a 1.5ATR stop. That tests its entry
families under a shared bracket, not a return to the completed Bollinger mean.
The next hypothesis changes the target to the **fixed mean known at decision**.
It does not follow a future moving average or retrospectively move the goal.
The change may shorten rewards, worsen costs relative to gross reward and
reduce executable coverage after manual delay. No profit claim follows.

Use exactly two complete-minute entry families, each on NQ1 and MNQ up to6:

| Proposed Candidate | Entry Family | Product Request | Target |
| --- | --- | --- | --- |
| `bb_reentry_quiet_late_midline__NQ` | Outside-close reentry | 1 NQ | Frozen mean |
| `bb_reentry_quiet_late_midline__MNQ` | Outside-close reentry | At most 6 MNQ | Frozen mean |
| `bb_wick_rejection_quiet_late_midline__NQ` | Inside-origin wick rejection | 1 NQ | Frozen mean |
| `bb_wick_rejection_quiet_late_midline__MNQ` | Inside-origin wick rejection | At most 6 MNQ | Frozen mean |

The first entry family is inherited from v85's `bb_reentry_quiet_late`, not a
new discovery. Its changed target is a new counted, outcome-informed follow-up,
not independent confirmation or an unexposed retuning. The second family is a
new deterministic entry hypothesis: an excursion rejected within a completed
minute rather than a previous close outside the bands. It adds a genuine
entry change, so this four-cell design is **not** a factorial target ablation.
There is no new 2R arm. Existing sealed v85 summaries are descriptive context
only, not a causal estimate of the exit's effect or a control selected by profit.

No machine-learned confidence score is needed to make this bounded question
executable. Adding one now would introduce fits and extra model choices before
the payoff mechanics are even defined. Neither rule is implemented as a signal
extractor in this change; only the exit and sizing mechanics below are coded.

## Proposed Signal Rules

Use NQ completed 1-minute bars with 20-close SMA, population standard deviation,
2-sigma bands, simple 20-minute true-range ATR and 5-minute SMA difference.
Let `p` be the previous close, `c` the current completed close, `L/U/M` the
current lower/upper/mean, and `Lprev/Uprev` the previous completed bands.

- Outside-close reentry long: `p < Lprev` and `L <= c < M`.
- Outside-close reentry short: `p > Uprev` and `M < c <= U`.
- Wick rejection requires `Lprev <= p <= Uprev` for either direction.
- Wick rejection long: current completed low `< L` and `L <= c < M`.
- Wick rejection short: current completed high `> U` and `M < c <= U`.

The prior-close conditions separate the two entry families. Equality at the
mean is no signal. Wicks are observed only after the whole minute completes;
there is no claimed within-bar fill or inferred high/low ordering.

Both families use the exact inherited quiet-late confirmation values, not
new values selected from v85 outcomes:

- Decision close is between 10:30 and 11:30 America/New_York, inclusive.
  This excludes the 09:30 opening hour, not a new post-result optimal window.
- Previous bandwidth `(Uprev-Lprev)/Mprev` is at most the linear 20th percentile
  of its preceding 20 bandwidth readings, excluding itself and the current bar.
- Current volume is positive and at most 0.8 times the positive median of the
  previous 20 admitted complete sessions' same-clock NQ minute volumes.
- Absolute 5-minute SMA change is at most 0.25 times completed ATR20.
- Missing references, nonfinite features or nonpositive ATR mean no eligible
  signal. Never substitute future-day volume or a different reference window.

Select only the first eligible decision per family per day. Both products and
both cost modes share that intent and the same frozen NQ anchor. A later entry
that fails geometry or risk sizing stays flat for the day; do not hunt for a
replacement signal or choose a product using later outcomes. Timing/direction
coverage and all no-trade causes must be reported, including reference warmup.

## Implemented Mechanics

`tools/nq_apex_mean_reversion_exit_v86.py` uses only the Python standard library
and does no I/O. Its immutable values require positive native integer
quarter-point ticks, nanosecond times, consistent OHLC and a contiguous prefix.
Booleans, floats, NaN/infinity, strings and noninteger prices are rejected.

`CompletedBandAnchor` accepts exactly 21 completed minute bars ending at the
decision. The last 20 closes produce an exact rational mean; the extra prior
close supplies the first of 20 true ranges. Stop distance is the integer ceiling
of 1.5 times ATR in ticks, bounded to 1..1,000,000 as in the existing engine.
Zero ATR is invalid. Missing, duplicated, reversed, stale or future minute
prefixes are rejected. End-time equality admits the just-completed bar; an
interval starting at the decision is NOT complete. Source admission still has
to prove timestamps, NQ product, maturity and predecision availability.

`ExitGeometry` binds that snapshot to a product, direction and cost mode:

- Baseline entry due: decision +60 seconds; stress: decision +240 seconds.
- Accept an actual first Last tick from due time inclusive to due +60 seconds
  exclusive, matching v78's timely window. The caller must prove it is first.
- Baseline time exit: decision +5460 seconds (planned entry +90 minutes).
  Stress exit: decision +5280 seconds (baseline exit -180 seconds). A late
  first actual tick does not extend the deadline.
- Proposed entry fill is Last plus adverse directional slippage, 1 tick in
  baseline or 4 in stress. Stop remains that slipped entry minus directional
  stop distance. Positive executable price levels are required.
- Absolute target is `ceil(mean_ticks)` long, `floor(mean_ticks)` short.
  Thus target crossing cannot precede reaching the unrounded mean. The mean
  remains fixed for the entire trade, including stress and delayed entries.
- Signed target distance is measured from the proposed slipped entry. If zero
  or negative, `skip_reason = TARGET_ALREADY_REACHED`: size is zero and the
  diagnostic refuses execution. Never clamp this to a one-tick target or book
  a guaranteed winner. These are proposed fills, not fills charged on a skip.
- A positive target distance is not a profitability filter: a small target can
  still yield negative net PnL after costs. No hidden minimum-R or net-edge gate.

`model_exit_at_tick` is a guard-free, single-tick diagnostic. Stop crossing is
inclusive, then target crossing inclusive, then time expiry inclusive. It uses
the observed Last tick plus adverse exit slippage, including a stop gap beyond
the planned level. Targets are not optimistic limit fills. Net cents deduct
two commissions and use the slipped entry/exit once; the slippage diagnostic
is not deducted again. The function does not scan ticks, certify first crossing,
maintain account state, enforce order or prove stop-loss bounds.

## Local Budget And Costs

These are the existing repository's Legacy50K research assumptions, not newly
verified official account terms. Keep `legacy_post20260301`, starting balance
5,000,000 cents, target 5,300,000 cents and initial trailing distance 250,000
cents. Legacy Evaluation has no DLL in the current engine. Do not import a
different EOD25K account, relax PA rules or assert unpriced fees are zero.

| Product | Tick Value | Baseline Commission/Side | Stress Commission/Side | Unit Risk Reserve |
| --- | --- | --- | --- | --- |
| NQ | 500 cents | 155 cents | 350 cents | `500*stop_ticks + 4700` cents |
| MNQ | 50 cents | 52 cents | 125 cents | `50*stop_ticks + 650` cents |

`size_for_budget` uses `max(0, (headroom_cents-1)//2)` and, when supplied, caps it
by `max(0, DLL-1)` and `max(0, MAE-1)`. Integer capacity is the minimum of product
maximum, supplied conservative plan ceiling and budget divided by unit reserve.
Actual quantity also respects the requested quantity; any crossed-target skip
has zero actual quantity regardless of capacity. It records unused budget and
explicitly says the reserve is not a loss guarantee. Stop gaps, adverse fills
and trailing peak updates can violate a modeled reserve.

The account adapter must supply actual state: Evaluation plan ceiling10;
Legacy PA ceiling5 until the existing strict prior-EOD unlock above 5,260,000
cents, then10. MNQ product ceiling remains6 and NQ1. Current conservative PA
MAE and any applicable DLL are supplied, never inferred from the final day.
The helper cannot enforce account rules from a price prefix. Matched budget
rules do not mean equal exposure, equal quantities or equal later headroom.
Each product needs its own ordered Last ticks and independent account path;
NQ PnL cannot be divided by10 to manufacture MNQ results. A shared NQ absolute
target on same-maturity MNQ is an explicit cross-product assumption, not a
fitted basis correction or a guarantee that either product reaches it.

## Future Admission And Integration

Only the **181 actual development dates, 2025-09-08 through 2026-06-12**, may be
scored or raw-replayed in a future proposed run, using the exact admitted
calendar rather than every weekday in the range. Do not expand it to the 617
minute-source sessions referenced in v85. Prior same-clock predictor references
require separate source admission and explicit predecision cutoffs; no new
warmup payload is authorized here. Missing admitted history remains flat.
The **48 holdout dates, 2026-06-29 through 2026-09-02**, remain closed. No
holdout manifest or payload was opened for this design. Reusing development
dates never restores independence or makes global DSR available.

The following work is explicitly NOT implemented or authorized to run here:

1. Add a separately owned additive v86 signal extractor for the two families,
   prefix receipts and exact inherited filters. v85 selected intents do not
   carry a numeric midline; their feature hashes cannot recover one. Do not
   turn a whole-session or future MA into a decision anchor. Bind symbol,
   maturity, session date, minute-end semantics and provenance outside this
   scalar helper. Audit deterministic reference warmup before any outcomes.
2. Add an admitted ordered-tick adapter. Resolve each product/mode's first
   timely entry, form geometry there, gate skips before costs or execution,
   and process every subsequent sequence, including tied timestamps and the
   entry mark. Preserve first eligible intent even if the delayed entry skips.
   Bind target distance to the identical slipped fill used by the engine.
3. Integrate with an additive account wrapper without editing any v85/frozen
   dependency. Preserve live precedence: trailing breach, strict MAE, inclusive
   DLL, model stop, model target, time. Preserve final fill/commission marks,
   PA violation checks, phase transitions, resets, billing, inactivity, payout
   and strict prior-EOD sizing. Flat days must still advance account lifecycle.
   The diagnostic is not a replacement for these account journals.
4. Add synthetic wrapper and replay-page integration tests: sequence/timestamp
   ties, missing first ticks, guard precedence, final-cost threshold breaches,
   zero-size days, rollover rejection and product/mode-specific skip receipts.
   Expose decision time, frozen mean and rounded target, proposed versus actual
   fills, stop, quantity, unused budget, skip reason and observed crossing.
   Manual replay must be labelled historical/exploratory, never a live order
   route or a demonstrated model. Do not connect this helper as a runnable
   strategy merely because its local mechanics tests pass.
5. Parent-owned review/full tests, source/dependency preflight and separate
   explicit authorization are needed before any future freeze/reservation/run.
   Preserve the inherited at-least30-active-dates requirement and the existing
   baseline/stress, Sharpe, HAC, family-bootstrap, Evaluation, PA survival,
   payout and MAE gates. Use the cumulative ledger, not only four trials, and
   do not loosen gates to rescue sparse results. Fix all report/statistical
   settings before outcomes. A development shortlist still is not validation.

The focused test file is `tests/test_nq_apex_mean_reversion_exit_v86.py`. It
uses only invented scalar/minute fixtures and an independent arithmetic oracle,
not frozen replay imports or sealed strategy returns. Run only:

```sh
<TMP>/ai-trader-v77-venv/bin/python -m pytest -q -o addopts='' tests/test_nq_apex_mean_reversion_exit_v86.py
```

Parent owns final full-suite tests and research-state updates. Neither the
test count nor the existence of this design implies a running model backtest.
