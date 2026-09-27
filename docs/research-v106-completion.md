# V106: Completed, No Usable PA Policy

## Outcome

V106 is a completed development experiment, not a technical abort or a
verified live/account pass. The fixed headroom-log target made PA selection
entirely inactive. Zero trading loss was achieved by zero PA nominations,
attempts and fills in all four modes, not profitable risk management.

| PA trading PnL, USD | Gate-only B | Support learner C | Log learner D |
| --- | ---: | ---: | ---: |
| Baseline | -256.00 | -1,457.40 | 0.00 |
| Cost-only | -862.00 | -784.00 | 0.00 |
| Latency-only | -564.30 | -1,112.40 | 0.00 |
| Combined stress | -1,179.00 | -1,179.00 | 0.00 |

All 12 account paths retain the exact original numeric Evaluation result,
then close for PA inactivity. No modeled payout eligibility or full-route
pass exists. The new target changes only PA, not the Evaluation learner.
D improves relative PnL over losing B, but baseline inactivity is eight
calendar days earlier, failing the frozen economic-benefit gate too.
Program fees remain unpriced; actual payout/compliance are unverified.

## Failure Attribution

On the common 21 baseline PA dates, all three arms saw 664 source events.
Stop support excluded the same 103. B nominated 68, C 80, and D zero.
D abstained on the remaining 561; no capacity/order filter was reached.
Cost-only and latency-only common-prefix nominations were also zero.
The different full own-account horizons must not be treated as matched rates.

Across all 126 stored development forecast dates, D had no all-four-positive
forecast. Fold 1/2 had no positive cost-only forecast; fold 3 had no positive
combined-stress forecast. Counts exclude, and separately preserve, 1/8/30
null forecast rows. These are saved prediction diagnostics, not new trials.
An initial postrun counting command did not handle nulls; the corrected
read-only aggregation changed no model, claim or immutable result.

The changed objective therefore did not solve the PA problem. Do not tune H,
relax positivity, force activity or retry this completed study after seeing
the outcome. A future candidate requires a distinct justified mechanism;
none is reserved by this closeout. Relative improvement over a losing
benchmark is not evidence of an executable profitable policy.

## Execution And Tests

Implementation commit: `f1cf81f`. One immutable claim charged three comparisons,
moving the ledger from 13,172 to 13,175. Twelve native head fits, three scalers,
42 ordered fit receipts, 181 dual-product raw pairs and 126 scoring dates
completed in 12 own-account paths, or 1,512 scheduled account-day slots.
The market process 34502 and postrun audit 59591 both exited zero.

The postrun audit verified 3,020 dependency hashes, 13 runtime files, eight
exact V105 control accounts, twelve exact Evaluation prefixes and all 126
stored control forecast envelopes. It recomputed saved-account summaries;
it is not independent implementation or independent market validation.
The 48 holdout price/outcome dates stayed closed. No operational model changed.

Focused software tests: 628 passed, including 50 V106 cases. Full suite 60023:
14,402 distinct passed, 3 failed, 23 skipped; all focused/V106 cases passed.
One V105 central metadata omission was repaired and focused-rechecked.
Final central metadata check 2858: 16 passed, two known historical failures.
They concern V102 four policies versus six comparison charges and a missing
V88 temporary JUnit file. The full suite was not rerun or declared green.

Terminal evidence and compressed test logs are under
`reports/nq_apex_pa_log_utility_v106_implementation/`. Read
`execution_verification.json` and `terminal_metadata_verification.json`.
The sealed study is `reports/nq_apex_pa_log_utility_v106/`; all pins are recorded
in the audit and central state. Do not reopen its claim or replace its files.

## Windows Boundary

Windows reply `91ed982d...` confirms PaperLastFeedV2 is the matching native
source; the binary/Parquet raw platform is separate. No V102 launcher/real
receipt owner or new PaperLastFeedV2 install/activation was demonstrated.
Installation/compile/activation approval was asked once and remains unanswered.
This is not a new runtime health snapshot. The last diagnosis showed V63
processes with zero packages/signals, V92 absent, and full-session bridge
stopped with last result 1. Login was not the identified blocker.

Both goals remain active. No order, Telegram message, credential transfer,
installation, restart, login, provider request or schedule change occurred.
