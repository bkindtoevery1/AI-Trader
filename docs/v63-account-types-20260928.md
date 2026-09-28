# V63 50K EOD and Intraday Evaluation Reevaluation

## Scope

User-authorized 2026-09-28 development reevaluation only. This is a new ordered-tick account calculation using the existing V63 signals saved by v78. It does not fit, infer, tune, trade live, access Windows, use the network, change the central research ledger, or open the sealed 2026-06-29 through 2026-09-02 holdout.

The official-rule inputs were supplied by the coordinating task after its same-day verification. This task did not duplicate that web research. This is not independent validation, verified broker execution, account purchase advice, or a compliance certification.

## Inputs and Integrity

- Signal authority: `reports/nq_apex_50k_tick_replay_v78/status.json`, `original_signal_dates` and `original_signals`, SHA-256 `7d88678e6f48ed7a2937bf8ec99c6ac1a9c9040e3271bf3aecf47b57f1fa55b5`.
- The v78 result seal and preoutcome lock are pinned, and all 181 signals are cross-checked against the sealed v77 `v63_nested_reference.continuous_account` schedule.
- Exactly 181 admitted paired development dates, 2025-09-08 through 2026-06-12. Only the explicit snapshot identities in the v78 lock are loaded. There is no raw-root discovery, holdout-envelope enumeration, or holdout payload access.
- Each NQ/MNQ pair is scanned once by the existing strict Parquet validator. The MNQ baseline and stress windows are shared by both account families. Full scan receipts must match v78 exactly.
- Parquet SHA-256 is checked before and after each scan, source metadata is rechecked, and all selected Parquet hashes are checked again after the completed replay. Source reports, implementation, tests, rules and runtime versions are pinned in the new preoutcome lock.
- Each daily scan receipt also records SHA-256 of the complete baseline/stress execution-window tuple stream, encoded as big-endian signed int64 sequence, timestamp and price ticks.

## Account Convention

Both books start at $50,000, target $53,000 realized flat balance, and allow $2,000 trailing drawdown. The access period ends on start date plus 29 days, inclusive. There is no minimum trading-day count. The supplied maximum is 6 NQ / 60 MNQ; this frozen strategy always uses 2 MNQ, never a tuned size.

EOD trails the highest flat session closing balance, including the initial balance. Its floor is enforced intraday at every ordered Last-tick mark and at the modeled exit fill. Intraday trails the highest equity including unrealized PnL. Neither trailing floor is capped under the supplied Tradovate convention. Equity touching the floor fails the attempt.

EOD has a $1,000 session net realized-plus-unrealized DLL. A touch liquidates with modeled adverse exit slippage and exit commission and stops the day, but is not itself an account failure. The actual modeled fill can additionally touch drawdown and fail. Intraday has no DLL. Because V63 makes at most one trade per day, there is no subsequent intraday entry after any exit. A cost-only DLL crossing at a normal exit is also marked as stopping the day.

The unchanged V63 stop is 187 ticks from the slipped entry fill. Baseline enters at the first observed tick at/after 10:02 ET and exits at/after 12:00 ET, with 1 tick adverse slippage per side and 52 cents commission per MNQ per side. Stress uses 10:05/11:57 ET, 4 ticks and 125 cents. The original first-tick-within-60-seconds boundary checks and source sequence order are preserved. Costs are deducted exactly once, in integer cents.

Live marks deduct entry commission; the executable exit additionally deducts exit commission and adverse slippage. Exit priority is drawdown touch, DLL, model stop, then fixed time exit. Gap fills occur at the first observed triggering tick plus adverse slippage, not an assumed stop-price fill. Unrealized target touches do not introduce a new liquidation policy: a pass requires realized flat balance after the frozen exit.

## Attempts and Coverage

Each book begins on the first admitted date. After pass, drawdown failure or expiry, the next disjoint attempt begins on the next admitted date. There is no PA transition and no same-day restart. All attempts are reported chronologically, including the initial attempt; there is no rolling best-start search.

Flat signals consume calendar time without a trade or cost. Unadmitted dates are not fabricated as market observations or additional signals. All numeric outcomes are conditional on no trading on unrepresented dates; missing weekdays are potential market-data gaps, not zero-return evidence. Calendar expiry still advances across weekends and gaps. An unfinished final attempt is explicitly right-censored, not counted as failure or pass. Trading PnL summed across attempts is not one continuous account balance and excludes program fees.

The coverage-annotated report lists `unrepresented_weekdays` for each full 30-calendar-day attempt window. It separately identifies missing weekdays through the actual outcome, after that outcome, and beyond the available data end. The existing conservative full-session calendar is an auxiliary classification only: holidays/non-full days remain in the weekday list and are not silently removed. This does not establish complete contiguous market-calendar coverage or official holiday verification.

## Artifacts

- Runner: `tools/run_nq_apex_v63_account_types_v1.py`
- Focused tests: `tests/test_nq_apex_v63_account_types_v1.py`
- Evidence directory: `reports/nq_apex_v63_account_types_v1/`
- Before replay: `preoutcome.lock.json`, `run_started.json`, `tests.xml`
- During replay: `progress.json`, `scan_receipt.001.json` through `scan_receipt.181.json`
- Terminal: `status.json`, `result_seal.json`; failures instead produce `terminal_failure.json`
- Primary integration result: `coverage_status.json`, authenticated by `coverage_result_seal.json`. These preserve all original numeric results and add the per-attempt coverage conditions. The original replay status and seal remain unchanged.
- Coverage postprocessor and tests: `reports/nq_apex_v63_account_types_v1/annotate_coverage.py` and `test_coverage_annotation.py`. These are narrow report-only enrichment, added after the coverage caveat arrived during the sealed replay; they do not replay market data or modify the frozen implementation.
- Results schema: `books.{eod,intraday}.{baseline,stress}.{initial_attempt,attempts,trades,summary}`. Each attempt has a deadline, terminal/censored status, balances and a half-open trade-index range. Daily rows preserve fills, trigger equity, floors, running peak, adverse excursion, exact drawdown diagnostics, DLL flags, and checked-mark counts.

## Commands

```sh
.venv/bin/python -B -m pytest -p no:cacheprovider tests/test_nq_apex_v63_account_types_v1.py --junitxml=reports/nq_apex_v63_account_types_v1/tests.xml
.venv/bin/python -B tools/run_nq_apex_v63_account_types_v1.py --freeze
.venv/bin/python -B tools/run_nq_apex_v63_account_types_v1.py --run
.venv/bin/python -B tools/run_nq_apex_v63_account_types_v1.py --verify
.venv/bin/python -B -m pytest -p no:cacheprovider reports/nq_apex_v63_account_types_v1/test_coverage_annotation.py --junitxml=reports/nq_apex_v63_account_types_v1/coverage_tests.xml
.venv/bin/python -B reports/nq_apex_v63_account_types_v1/annotate_coverage.py
```

Freeze and run are exclusive one-shot publications and refuse to overwrite an existing attempt. Do not rerun a claimed economic scan. The verify command checks saved evidence without replaying market data. `-B` and disabled pytest caching keep generated files out of the original source directories.

## Verification and Results

The 29 focused prefreeze tests passed. They cover floor touch, uncapped trailing, EOD/intraday differences, tied-timestamp order, fixed costs/quantity, actual-fill stop geometry, DLL versus drawdown behavior, exit-cost DLL crossing, inclusive deadline and gap expiry, next-attempt reset/no PA, right censoring, source pin failure, holdout rejection before raw scanning, and one scan per product shared between windows.

Four additional coverage tests passed, including explicit ordinary-weekday gaps, holidays retained in the list, post-data-end censoring, and immutability of original results. Saved-result verification checked source pins, both original seals, all 181 scan receipts, the four-book date coverage and attempt arithmetic. A separate Node.js arithmetic check validated all 724 daily rows and 40 disjoint attempts, exact fixed-quantity fill/cost PnL, the coverage seal, and unchanged economic results after annotation. No broad repository regression was run.

Execution session 64798, PID 69653, exited successfully with code 0. Runtime was 171.748 seconds. All 181 pairs / 362 files were scanned once, validating 402,041,614 ordered raw events. Every original v78 scan receipt was reproduced exactly. Final pinned-source and Parquet hash verification passed. No process remains running for this replay.

All outcomes below are conditional on no trading on unrepresented dates.

| Book | Attempts | Numeric passes | Drawdown failures | Expired | Right-censored |
| --- | ---: | ---: | ---: | ---: | ---: |
| EOD baseline | 10 | 0 | 1 | 8 | 1 |
| EOD stress | 10 | 0 | 0 | 9 | 1 |
| Intraday baseline | 10 | 0 | 2 | 7 | 1 |
| Intraday stress | 10 | 0 | 0 | 9 | 1 |

There were no modeled DLL-triggered liquidations in these recorded schedules. This does not remove the missing-session caveat.

The initial attempt in every book runs from 2025-09-08 through 2025-10-07 and expires without reaching the target. Baseline closes at $51,260.56 (+$1,260.56); stress closes at $50,533.00 (+$533.00). Both families have the same initial values. Its unrepresented weekdays are 2025-09-11, 2025-09-15 and 2025-09-22.

Across the complete admitted development span, 19 weekdays are unrepresented, including possible holidays/non-full sessions: 2025-09-11, 2025-09-15, 2025-09-22, 2025-10-10, 2025-10-31, 2025-11-27, 2025-11-28, 2025-12-24, 2025-12-25, 2025-12-26, 2026-01-01, 2026-01-06, 2026-01-19, 2026-02-16, 2026-03-03, 2026-04-03, 2026-04-21, 2026-05-25 and 2026-06-09.
