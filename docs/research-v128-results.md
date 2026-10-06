# V128 Results And Retrospective

Completed October 6, 2026 at 04:17:22 UTC. This is outcome-informed development,
not independent validation, live performance or a verified current Apex pass.
The [fixed design](research-v128-design.md) was publicly committed before replay.

## Complete Execution

One supervised child ran from 02:42:25 to 04:17:23 UTC, exit 0, without retry.
Its immutable claim was published at 02:43:52 after source authentication.
The 181 paired development raw-tick dates span September 8, 2025 through June 12,
2026. Both products' unit journals and original execution receipts reconciled.
The 126-date scoring calendar spans December 3 through June 12, including zero
activity and terminal tails. There are twelve complete books: eight new matched
V126/V127 books and four exact original conformance books, or 1,512 scheduled
account-days (1,008 new). All four controls and eight Evaluation projections
matched exactly. No fit, inference rerun or parameter change occurred.

The separate read-only audit exited 0, required the successful bound terminal,
verified all three sealed output files and recomputed complete account summaries.
An additional direct sum of saved PA daily net cents agreed for all eight new
books. These are saved-book arithmetic checks, not independent raw/numerical
implementations. All research subprocesses are now terminal.

## PA Results

USD after modeled commissions and slippage, before unpriced program fees.
These are actual simulated fills, not overlapping event-label sums.

| Scenario | V126 HGB PA net | Trades / active days | V127 session PA net | Trades / active days |
| --- | ---: | ---: | ---: | ---: |
| Baseline | -2,303.14 | 22 / 11 | -2,323.26 | 16 / 7 |
| Cost only | -2,417.00 | 19 / 10 | -2,296.50 | 15 / 7 |
| Latency only | -1,790.72 | 31 / 15 | -1,696.86 | 41 / 23 |
| Combined stress | -1,908.50 | 21 / 10 | -1,892.50 | 25 / 12 |

Every new PA book lost money. Seven ended in modeled activity closure. V127's
latency-only book remained alive through June 12 but was right-censored and
unprofitable; survival is not payout success. No new book reached hypothetical
payout eligibility. There were zero hard-threshold breaches and zero PA MAE
violations in all eight, which did not make the accounts profitable or viable.

The single preregistered V127-minus-V126 contrast is -20.12 USD baseline,
+120.50 cost-only, +93.86 latency-only and +16.00 combined stress. It fails the
required improvement in both baseline and stress. Neither candidate passes the
absolute profitability, payout or modeled full-route gate. Diagnostic cost and
latency scenarios cannot rescue a failed primary contrast. Different modes have
different fills, phase dates and account states, not the same trades with only
an extra fee deducted.

## Evaluation Is Not New Candidate Success

Every new book inherits the unchanged original NQ Evaluation policy. Its modeled
profits are 3,254.00 / 3,292.00 / 3,130.20 / 3,429.00 USD in mode order, with
8-14 trades and April 17-30 pass dates. This identical result demonstrates route
conformance, not a newly learned Evaluation advantage. It also took months, not
a short renewal-window pass. Four monthly renewal units are recorded but their
amounts, activation fees and actual account cohort are not verified or priced.

PA starts with fresh account capital. Evaluation gains are not cash that can
offset PA losses. A positive sum of Evaluation and PA trading PnL must not be
presented as payout or as a healthy PA balance.

The new forecasts only act after each inherited Evaluation pass, so executable
PA evidence is concentrated in late April-June, not 126 PA trading sessions or
three independent PA replications. All 126 dates were processed by the continuous
route, but the first two forecast blocks mostly did not control actual positions.
This is an important limitation of this matched routing experiment.

## Failure Attribution

1. Selection quality, not zero-trade abstention, was the immediate economic
   problem. Baseline V126 had sixteen stop exits and six targets; V127 had
   thirteen stops and three targets. Session context did not improve baseline
   selection in this account period. This is a descriptive failure, not proof
   that the indicators can never work or a causal separation of each feature.
2. Losses depleted usable headroom. Baseline ending headroom was 69.66 USD for
   V126 and 81.84 USD for V127. There were thirteen and sixteen `RISK_CAP_FLAT`
   attempts respectively. Actual PA sizing was one to five MNQ, often five
   early on; no six-contract unlock occurred. Increasing contracts is not a
   demonstrated remedy for negative expected payoffs and reduced headroom.
3. The frozen modeled activity gate is profit-based: at least two days earning
   50 USD in its rolling 30-calendar-day window, not merely two trading days.
   Each baseline candidate had only one qualifying PA day. Both closed on
   May 23 even though they had made trades more recently. The exact current
   broker/account rule has not been reverified; this describes the frozen
   `legacy_post20260301` model, not a universal official rule assertion.
4. Overlapping forecast-label averages did not translate into a sustainable
   account. Cooldown, actual-entry geometry, support and own cash constrained
   execution. Removing these rules after this result would not validate the
   original model. The test count was not a financial pass/fail criterion.

Do not promote either candidate, refit this completed attempt, drop costly heads
or inflate size to rescue it. A next model should address own-product executable
net-payoff quality and the inherited Evaluation/PA coverage limitation. Any new
NQ/MNQ learner or action policy needs a separate outcome-informed declaration,
chronological training and comparison charge, not synthetic scaling of MNQ
forecasts into NQ or opening the sealed holdout. No such next model ran here.

## Qualification And Evidence

Final qualification: 138 focused tests plus 548 affected account/source tests,
all passed, exit 0, unchanged frozen code. An earlier overly broad test attempt
was interrupted after 772 passes and 25 failures from two synthetic-fixture
defects; the corrected 138-case suite includes all of those cases. It is not
represented as a green or completed full-repository suite. The inherited
repository-wide nongreen status remains disclosed. An integration alias error
was fixed at preflight before any market claim. Review also hardened sealed
reads against replacement races and recorded process spawn failures.

Three comparisons remain charged, cumulative 13,232. Historical outcomes are
reused; the 48 sealed dates remain closed. No operational V63/V92 replacement,
Windows change, credential transfer, Telegram test, purchase or order occurred.

SHA-256 evidence:

- Claim: `9de5e840ec9df00daa372c8f04a9b9e5c3999c45f7ea537fb93ee1fcb8767cba`.
- Status: `e80991d62401277073a4c1858fdef6d2f56170643ab96b29115b2d7d5f57257b`.
- Complete accounts: `ad6f680b7a82547a0b5889ac3b34794cfd9987ce1efda61c044aac724afbaa5c`.
- Result seal: `56f1a56dc5b24651fd270bed1a75cc88a26ff48ce06d71664a803e3537d4b87d`.
- Observed terminal: `faf6ab7d2ecf1fcaada1bdce071cc99a17532f718f934ac5dc6803a2cd800e66`.
- Focused JUnit: `0f2cbe95dbcadef532578f17cff1c2720c18abe1dc40ec670e5f78bcdc70245b`.
- Affected-core JUnit: `9e09f72100851c4364fa172475c12c72e27be0acab1dc9c50a1ea801fc7cc337`.

Local detailed artifacts: `reports/nq_apex_point_accounts_v128/` and its separate
execution directory. Raw data, fitted artifacts and private source ancestry are
not public attachments. See [data inventory](data-inventory-20261006.md).
