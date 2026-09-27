# V116 Initial-Geometry Audit Correction

The market attempt remains the single successful execution recorded at
2026-09-22T17:23:17Z. Auditor v1 failed because it rebound frozen methods;
auditor v2 preserved identity but was too broad about constructor calls.
Both failures and their scripts are retained, not silently replaced.

At 17:35:38Z, v2 exited 1 while restoring an existing ancestor forecast.
`nq_apex_feasible_exposure_v94.reference_exposure` legitimately constructs
a fresh initial account and reads its initial sizing limit. This computes an
input to an already fitted predictor; it does not advance a day, fill a trade,
change a fitted model, replay raw data or create a new economic comparison.

The additive v3 auditor permits only the original initial-geometry constructor
chain and sizing function needed by that helper. All fitting, tape replay,
phase/account advancement and trading entrypoints remain prohibited. Original
method identities and all model, cost, risk and economic gates are unchanged.
Tests must exercise the real reference helper and confirm that trade/calendar
advancement remains blocked. Successful source and independent account audits
are still required; this correction is not a performance exemption.

## Preserved V2 Evidence

- Auditor: `ee3abfaebec61b90071a7a92e5d53547c94371a62222a1e227516621d9736fd3`.
- Terminal: `a5347f1a345ff48e511e06078a5070a3cd6fea6f972ba36fbec7471e40bff1c3`.
- Stderr: `77c321db55f28dd4568c6b792b0d0e9d3a2a3b8a2196f4892cee3977cbe14f43`.
- Failure receipt: `6d74b5b0999c2d179325facdbdbd450808bd755f8314c63fc124f84d43163c8f`.
- Pre-dispatch review: `8013fee524a928f95c2f2e40de20ae82e1615f715bd2d443b1605ac71c8ea973`.

V3 receipts use `terminal-audit-v3.*`, `source-audit-v3.*` and
`account-audit-v3.*`. The independent JavaScript accounting is unchanged.
No new market run, fit, replay or comparison charge is authorized here.
V1 rationale is retained in `docs/research-v116-audit-repair.md`.
