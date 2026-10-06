# V130 Results: Earlier PA Exposure, But No Robust Whole-Route Pass

## Completed Execution

The sole supervised replay completed at 2026-10-06T06:50:05.287580 UTC after
181 complete raw contract pairs and 126 scored dates. Supervisor and child
exited 0; no source changed. Four original conformance accounts and both raw
unit journals reconciled. Eight new books use the two frozen V129 recipes for
BOTH NQ Evaluation and MNQ PA; each owns its phase transition. No fit or inference
was rerun. Three comparisons remain charged, historical total 13,240.

The separate saved-result audit exited 0, verified three sealed output files,
revalidated source/runtime/forecast bindings and recomputed account summaries.
A direct daily-row sum check also matched PnL and trade counts for all 24
account-phase combinations. All required processes are terminal. This verifies
saved evidence and arithmetic, not an independent raw or model replication.

## Account Results

All PnL below is simulated trading USD after modeled execution costs, BEFORE
unpriced program purchase, renewal and activation fees. Evaluation and PA are
separate capital accounts: their profits are not one spendable account balance.
PA dashes mean no PA entry, not a measured zero-profit PA performance.

| Recipe / Mode | Evaluation PnL | Evaluation Trades | PA PnL | PA Trades | Final State |
| --- | ---: | ---: | ---: | ---: | --- |
| HGB / baseline | +4,540.40 | 16 | +2,338.78 | 198 | PA survives observed calendar; hypothetical payout eligible |
| HGB / cost-only | +4,113.00 | 16 | +178.00 | 162 | PA profit-qualified activity closure; no payout |
| HGB / latency-only | +3,259.20 | 18 | +1,626.68 | 175 | PA survives observed calendar; hypothetical payout eligible |
| HGB / combined stress | +927.00 | 24 | - | 0 | Evaluation unfinished at end of calendar |
| Two-part logistic / baseline | -1,360.60 | 26 | - | 0 | Evaluation unfinished |
| Two-part logistic / cost-only | -1,496.00 | 18 | - | 0 | Evaluation unfinished |
| Two-part logistic / latency-only | -1,400.80 | 18 | - | 0 | Evaluation unfinished |
| Two-part logistic / combined stress | -1,476.00 | 18 | - | 0 | Evaluation unfinished |

HGB passes Evaluation on December 17, 2025 in baseline, cost-only and
latency-only; PA begins December 18. Baseline and latency-only each process
115 PA sessions, versus 102 before the cost-only closure. Their first modeled
payout-eligible dates are February 23 and February 12 respectively, with a
hypothetical $500 withdrawal in each. No actual payout occurred. Cost-only's
positive PA total does not prevent the rolling profit-qualified activity closure.

The primary gate requires baseline AND combined stress. Both recipes fail it;
the two-part-minus-HGB benefit gate also fails. Every PA contrast is null because
the two-part recipe never reached PA. Never call its absent PA loss an advantage.
All eight new books have zero hard-threshold/MAE violations; avoiding a breach
alone is not enough. The five unfinished Evaluation books each incur six modeled
renewal units, in addition to one purchase; monetary program fees are unpriced.

## Failure Attribution And Limits

- HGB has a real baseline execution result, not just positive overlapping labels.
  But combined cost and delayed-entry effects change the entire account path.
  That book last fills on December 30, 2025, then ends with only $210.50 above
  its trailing floor and records 250 `RISK_CAP_FLAT` attempts. This is constrained
  capacity after the path evolves, not absent source data, a daily trade cap,
  or a failed Python test. Its total +$927 does not satisfy the Evaluation goal.
- The two-part recipe is negative in every mode and never reaches PA. Its
  baseline has 26 fills and 82 risk-cap skips; combined stress has 18 fills and
  64 skips. Smaller aggregate forecast error from V129 did not produce adequate
  executable selection or account growth. No claim that one architectural
  component alone caused this failure is justified by this whole-recipe contrast.
- Unlike V128's inherited late-April Evaluation transition, HGB here enters PA
  in December under its own NQ forecasts. The different exposure and capital path
  mean the improved PA result is NOT an isolated MNQ model improvement. Do not
  pool different PA calendars as matched observations or declare a stress pass
  from favorable baseline or latency-only outcomes.

The unchanged modeled Legacy rules apply across the historical research dates;
current official cohort/rule/fee compliance was not reverified. Last-tick replay
is not bid/ask liquidity or actual-fill evidence. The 126 development dates have
been repeatedly reused, so no independence or live profitability is established.
The 48 sealed holdout dates remain closed. Do not deploy, increase risk, relax
costs, invert or retune these completed recipes to rescue their result.

A bounded [longer-minute feasibility review](research-long-minute-training-feasibility-20261006.md)
found 436 complete older paired minute sessions and direct longer-history
precedents in V78-V84. The next useful study needs a distinct, preregistered
supervision/history hypothesis and a genuine return-score decision contract,
not another unqualified more-data refit. No follow-on fit was launched here.

## Qualification And Durable Evidence

- Focused tests: 293 passed; affected regression: 445 passed; 738 unique cases.
- Real-source preflight, replay, supervisor and postrun audit: actual exit 0.
- A full repository regression was not rerun or claimed green.
- Fixed local implementation: `8831519`.
- Public pre-execution design: `ec1e5d1b5db496b8385dcc72c6b95a1f05006ddb`.
- Claim: `59376c77c859dfb5797f6b41253bc6bd9d881a6de8a432c36c33484700b31bbf`.
- Accounts: `160e4b0d951acfb73a2a5b90b7f94793c166074de13b7737f9a53e070974fe8a`.
- Status: `7951507ccfc720a2c95fb5cf97713ea229a1e01c3e4b4c11a1c1c63ede2a9f28`.
- Seal: `c6eb9796c455511310c695b9677e33e18df827a4fd1cc062b0947eb46ef8ea93`.
- Terminal: `c3bb24b9150293059cb0bdb5c0279e499f7097f7e7d614149135c877679ab210`.

Local evidence is under reports/nq_apex_whole_route_v130 and its execution
directory, with a separate audit receipt. No raw market rows, fitted artifacts,
private code ancestry, credentials, Windows changes, orders or schedules are
part of the public documentation. The broader research/operation goal remains
active; this completed experiment is not completion of that goal.
