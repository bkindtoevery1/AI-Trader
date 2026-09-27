# v79 Auxiliary Volume Ablation

This is auxiliary work. Parent v80 owns the new-model objective and architecture.
v79 changes neither root modules, prior frozen artifacts, central state, ledger,
runtime, nor prospective operation. It reserves exactly 12 comparisons beyond
12951: two new feature variants times three nested ridge alphas times two account
families. The parent owns joint v79/v80 accounting; 12963 is only the isolated v79
conceptual subtotal, not a new shared ledger value.
Parent v80 reserves six additional comparisons independently. The joint
conservative diagnostic bound is 12969 = 12951 + 12 + 6, recorded before freeze.

## Frozen Design

- Recompute unchanged v63 from the exact 617-session cohort and require exact
  readouts and v77 sequences, 282 continuous signals and selected alphas.
- Zero both volume sequence columns and both volume context entries, retaining
  all price inputs, reservoir weights, readout and nested training-only ridge.
- Seasonal minute residual: log1p current volume minus the median log1p volume
  at that minute over strictly preceding up to 20 admitted sessions, per product.
  Empty history gives zeros. Append current volume only after constructing its
  features. Do not reset at contract rolls. Center/std-normalize within the 30
  completed minutes; std <= 1e-12 gives zeros. Context is signed mean residual.
- Reuse 4 outer folds (325/10/63) and inner selection (180/10/42), alphas 1/10/100,
  the original stopped action-value target and 6.5-point direction dead zone.
  The previous fit continues across the 30 bridge sessions, as in v77.
- Scan exactly the v78 181 raw pairs once, sharing each baseline/stress execution
  window across all variants. Reproduce reference accounts and receipts exactly.
- Report Legacy 50K and EOD 50K as distinct account families under frozen v78
  rules. Also report fixed one-MNQ daily diagnostics across all 181 dates to avoid
  confusing feature quality with early PA termination. These reuse `_trade` and
  a subclass `_mark` with no account barrier, DLL or MAE policy termination;
  model stop, adverse gap fills, commissions and slippage remain unchanged.

## Evidence Boundaries

Use the v77 Python environment, CPU float64 and one BLAS thread. Bind code,
policy, this document, focused tests, environment, dependencies and selected
source metadata before outcomes. Publish `run_started.json` before target or new
outcome loading. No restart, retune, partial family metrics, holdout reading or
new account selection. Full result is published only after every replay and
reference check completes; a failure exposes no partial outcomes.
An all-flat candidate explicitly fails activity coverage rather than being
treated as success or an unknown statistical result.

v63 minute volume and v76 aggregate relative activity already exist. The earlier
unit-volume claim was corrected; none of these experiments authenticate actual
exchange volume. Paired changes are descriptive reused-history diagnostics,
not independent confirmation, verified account compliance, actual payout or
promotion evidence. Program fees remain unpriced as in v78.

## Artifacts

Run `tools/run_nq_apex_volume_ablation_v79.py --freeze`, then run without flags.
All generated artifacts live in `reports/nq_apex_volume_ablation_v79/`:
`preoutcome.lock.json`, `run_started.json`, `status.json`, `result_seal.json`, or
`terminal_failure.json`. Focused fixtures are plumbing tests only.
