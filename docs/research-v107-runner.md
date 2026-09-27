# V107 Replay Runner

The account component was committed as `fb5a37a`. The separate runner is
`tools/run_nq_apex_phase_micro_v107.py`, with the closed policy at
`config/nq-apex-phase-micro-v107.json`. The hypothesis and unchanged research
constraints are in `research-v107-design.md`.

## Source Admission

Read the original V102 and V105 closures through the existing current-runtime
readmission path, then bind the completed V106 predecessor and its 42 fit-stage
receipts. Rehash the merged dependency closure at current paths. Do not recreate
obsolete temporary runtimes or modify ancestor files.

Reuse V103's original dual-product population, grid, scaler, snapshot, causal
outer-model and full-envelope validators. Their input is the authenticated V97
source and the unchanged development snapshot ending 2026-06-12. Restore all
six original V102 product/fold records and 252 original continuous-utility
envelopes. Do not select the similarly named threshold-control envelopes for
later MNQ folds. The preflight reads already observed development data, performs
no fit, opens no sealed holdout and requests no execution tape.

## Complete Replay

Capture forecasts, label identities, raw envelopes and expected controls before
calling a tape provider. Validate and scan every explicit pair across all 181
dates, including the 55 warmup dates and dates after any account becomes terminal.
Recompute both products' original four-mode unit journals, with original first
touch and adverse-path behavior. Candidate PA uses actual MNQ quotes and costs.

Maintain eight independent state objects: gate-only NQ and phase-micro, each in
four modes. Independence here means no shared mutable account state, not
independent market observations. Require four exact V105 control reports and
four exact candidate Evaluation projections. Replay candidate PA continuously;
never splice or multiply historical NQ PA returns.

The mixed-phase accounting adapter validates each row and execution against its
actual phase/product, uses the original lifecycle checks, and reconciles daily
counts, cash changes, hypothetical withdrawals and final balances. It does not
rename executions into a single-product account. Economic improvement, absolute
PA profitability, modeled full-route screening and verified live operation are
separate conclusions. Program fees remain unpriced.

## One-Shot Execution

Use the existing pinned runtime:

```sh
<HOME>/.local/share/ai-trader/runtime/v102-20260912/bin/python tools/run_nq_apex_phase_micro_v107.py --preflight
<HOME>/.local/share/ai-trader/runtime/v102-20260912/bin/python tools/run_nq_apex_phase_micro_v107.py --freeze
<HOME>/.local/share/ai-trader/runtime/v102-20260912/bin/python tools/run_nq_apex_phase_micro_v107.py --run
```

Run only after the runner's focused and full regression review. A preflight or
freeze does not reserve comparisons. A unique immutable run claim reserves two
comparisons, moving 13,175 to 13,177. Fit calls are prohibited. Failures after
the claim retain its charge and forbid retries; a competing claim is not owned
by the losing process. Technical aborts are not performance verdicts.

Progress output reports completed pair scans only. No partial performance is
printed or serialized. Final publication follows all replay checks, summary
reconciliation and postrun dependency/runtime/claim checks. `status.json` alone
is insufficient: require the matching immutable `result_seal.json` and absence
of a terminal conflict before consuming results.

## Verification Scope

Synthetic tests cover one-shot ownership, lock mutations, fail-closed stage
errors, no-fit enforcement, source receipt linkage, original control equality,
dual-product label checks through the last date, callback mutation isolation,
phase-specific economics and separate benefit/profitability gates. They are not
strategy evidence. Current test receipts and actual execution evidence belong
in `reports/nq_apex_phase_micro_v107_runner_implementation/`; never overwrite the
earlier component checkpoint under `nq_apex_phase_micro_v107_implementation/`.

This runner does not install or activate Windows collectors, generate live
signals, access Telegram credentials, purchase data or place broker orders.
