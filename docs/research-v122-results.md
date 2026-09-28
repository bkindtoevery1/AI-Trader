# V122 Audited Development Result

Completed 2026-09-28 UTC using existing admitted Mac data. Actual market and
postrun processes both exited 0 with unchanged source/runtime. The final
completion command also exited 0. Status: `COMPLETED_AUDITED_DEVELOPMENT_ONLY`.
Economic verdict: **failed, all PA decisions abstained**. This is not a verified
50K pass, independent validation, deployable signal or a three-day pass promise.

## Intervention And Counts

V122 tested one frozen quarter-stop pullback-market attempt policy, with new
attempt labels and three chronological forests. It included original nonfills
and expiries, maintained causal/purged folds, and changed no Evaluation policy.
Entry delay, costs, account lifecycle and contract constraints remained frozen.
This combines entry-policy and label-relearning changes; it does not isolate
estimator superiority. No post-outcome threshold, model or quantity was changed.

The completed run generated 129 label dates, fitted 3 models / 192 trees, read
181 explicit-contract pairs and scored 126 dates. It created 4 new account books
and retained 4 V119 control books. Exactly 2 comparison charges moved the ledger
from 13213 to 13215. The sealed holdout stayed closed; no orders were enabled.

## Results

All four candidate books ended in modeled `PA_INACTIVITY_CLOSURE` with zero PA
trades and zero PA trading PnL. The unchanged Evaluation leg reached its numeric
target; that inherited result is not evidence that the new PA policy succeeded.

| Mode | Evaluation Trading PnL | PA Trades | PA PnL | Positive-Capacity Abstentions |
| --- | ---: | ---: | ---: | ---: |
| Baseline | $3254.00 | 0 | $0.00 | 561 |
| Cost only | $3292.00 | 0 | $0.00 | 510 |
| Latency only | $3130.20 | 0 | $0.00 | 578 |
| Stress | $3429.00 | 0 | $0.00 | 561 |

Stop-support exclusions were respectively 103, 99, 97 and 103. Eligible quantity
decisions all had positive capacity, but selected no position. No trigger attempt
was placed. Thus the failed route is not explained by zero contract capacity,
missing Windows data, or an attempted entry waiting indefinitely for a fill.
It is a repeated failure of the learned decision rule to select any PA entry
under the frozen utility/risk conditions. Counts are not independent samples.

Compared with V119, PA PnL differences were -$135.96, -$72.00, +$65.54 and +$68.50.
Avoiding the control's stressed losses did not create positive PA economics or
survival. Neither contrast benefit nor the full-route gate passed. Program fees
remain unpriced; the user's actual account cohort and broker fills are unverified.

## Verification And Retrospective

Saved-model postrun verification used zero new fits and zero account replays. It
completed 495900 recorded-account checks and 7896 lifecycle checks. This verifies
recorded arithmetic, bindings and lifecycle, not an independent raw-tape rebuild
or statistical generalization. Historical development outcomes were reused.

Software qualification remains explicitly non-green: focused 1871 passed/exit 0;
full 22682 passed, 2 inherited failures, 1 skipped/exit 1. See the separate runner
qualification record for exact failure identities. No failure was waived away.

Do not repeat this claim or retune it in place. The useful next research step is
to attribute abstention using the completed saved distributions and utility
components before proposing another separately charged candidate. Repeating a
new entry policy without explaining the repeated zero-selection behavior would
not address the observed failure. Live-source recovery is a separate operation.

Immutable local evidence:

- Status SHA256: `8c0b3220f7fbda71b5480352ceae091fbab080a1501e0e2d037a2cde3177de3f`
- Result seal SHA256: `bc67823c78c93f45207fc04b83b4339291b0b78e8f96d70d9d00382ef6531808`
- Completion SHA256: `1177eb294c914632f1d5b59bdde4e4d908f1e106b7dabfbef0fda74be8c61f68`
- Market terminal SHA256: `b1c480de1ca7d17c1577a137f53eff6b6dcab88fb1de5770a22c217d261557f3`
- Postrun terminal SHA256: `c841266109879bf218d454d6f3aab49a2f0096f223001d880dd44f8dfee052e3`

No raw market files, private runtime snapshots or credential values belong in
the public record. Both ongoing user goals remain incomplete.
