# v96 Proposal: Integrity-Only Continuation Of The v95 Candidate

Status: COMPLETED_NO_DEVELOPMENT_PASS. See `research-v96.md` for execution
evidence; the proposal below is the pre-outcome design. This is a correction, NOT
a new scientific strategy, new evidence of efficacy or a rescue rerun of v95.
The original v95 attempt remains closed with2actual fits and8comparisons.
Independent proposal review found no substantive design blocker; its wording
clarification is incorporated. v95 terminal audit, focused1,008/full9,245
regression and completion evidence are now complete, not strategy validation.

## Defect And Scope

v95 reconstructed authenticated v94 coefficient lists as C-contiguous arrays.
Their floating-point accumulation differed from the original estimator. The
strict control guard stopped the run before its first scored outcome. Parent
reconstruction of already-observed v94 controls found explicit F-contiguous
restoration reproduces all22,365 feasible control vectors exactly. No new v95
candidate parameters or performance were inspected to identify this defect;
the saved, already-observed v94 coefficients were inspected.

The successor should use an explicit F-contiguous float64 array for the saved
8-by-9 v94 coefficients, preserving the original single-thread operation order
and all row keys, types, model hashes, masks, quantities and canonical bytes.
Do not try multiple layouts dynamically and select whichever works. Do not
replace exact checks with a tolerance, clamp predictions, change selection
signs or silently refit a missing reference. Add deterministic nontrivial-float
matrix, serialization round-trip and near-zero sign tests. Simple integer
coefficient tests were insufficient and must remain disclosed as a coverage gap.

Independently review the proposed restoration and verify every authenticated,
already-observed v94 control prediction before any new fit. This is a software
conformance preflight of the old comparator, not inspection of new candidate
performance or permission to train on scoring rows. Reject any mismatch.

## Unchanged Scientific Design

Reuse the exact locked v95 pure model, nine predictors,16 date-ranked RBF
centers, gamma1/9, Ridge alpha10, center seed20260995 and bootstrap seed20261995.
Keep its feasible populations, mature targets, date weights, authenticated
scalers,45initial training dates,10full-calendar purge and three42-date folds.
No source universe, parameter, centering, rank, label, selection, loss or gate
change is authorized by this proposal. Preserve the duplicate/singular-center
abort without replacement and the regularization-geometry limitation.

Keep NQ<=1/MNQ<=6 continuous Legacy 50K account execution, costs, slippage,
stops, targets, cooldown, same126 scoring dates and all53 exact-v94 conformance
checks. Require the same all-three-control prediction gates, practical
Evaluation screens and separate PA/payout assessment. No campaign resets.

## Before Any New Run

1. Finish the v95 typed terminal/layout audit, full regression, completion
   evidence and scoped retrospective commit. Preserve its lock, claim,
   terminal failure,12fit receipts,2actual fits and8counted comparisons.
2. Independently review this integrity-only continuation before implementation.
   Use a new runner/policy/lock; never patch or reexecute frozen v95 in place.
3. Bind the same scientific model and corrected reference restoration in a new
   hash closure. Validate synthetic nontrivial-float and exact-reference cases,
   focused/full regressions and source metadata before a new one-shot claim.
4. Conservatively count all8 policy comparisons again at that claim, increasing
   13,113 to13,121. Schedule6new map fits,6Ridge fits and24heads, zero new scalers
   or control fits. Do not erase the prior2fits or call them completed6foldfits.
5. Keep all partial candidate outcomes private and report actual acknowledged
   work. If this new claimed attempt aborts, preserve it rather than retrying.

Repeated development remains observed, outcome-informed development. This
proposal supplies no independent validation, global historical DSR, economic
liquidity/fee proof or verified50K pass. Keep the final48sessions2026-06-29
through2026-09-02 closed. No genetic algorithms, orders, purchases, secrets,
Windows deployment or paper-model promotion.
