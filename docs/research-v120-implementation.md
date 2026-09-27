# V120 Implementation Checkpoint

This is development work, not a completed market comparison or an account pass.
The two full thread goals remain active: model research and Windows model
operation. The user's latest operational priority does not require waiting for
Windows data to continue historical model development.

## Rationale And Scope

V119's joint quantity policy failed through sparse PA activity and weak stressed
economics. V120 asks whether direction-aligned, minute-aggregated trade size adds
information beyond equally weighted tick directions. Both candidates retain the
original nine features plus NQ/MNQ pressure, the same fixed learner capacity,
causal training prefixes and execution rules. Read `research-v120-design.md`.

Initial implementation is committed as `559e6a2`: causal feature extraction,
source-input admission and an eleven-coordinate forest. Its435 focused software
cases passed with actual exit0 and unchanged sources. These include248 synthetic
forest cases, not248 additional market fits or strategy trials.

The new pure pipeline validates the complete original source, all training
prefixes and both candidates' scoring coordinates before any fit. It produces
six fixed forests through18 ordered fit stages and detached model callbacks.
The new account adapter processes181 raw pairs once for eight new accounts while
retaining the exact original and V119 control books. Both comparisons must improve
baseline and stressed PA economics without added breaches or earlier inactivity.
The fixed operational models, costs, risk rules and sealed holdout are unchanged.

The pipeline's31 and account adapter's7 targeted synthetic cases passed with
observed exit0; a combined rerun retained38 distinct cases and exit0. Independent
read-only code review found no concrete defect within the caller-authenticated
pure-component contract. Three additional isolation cases passed: two rebuild
later synthetic labels/populations while proving earlier-fold probabilities stay
unchanged, and one mutates caller-owned inputs from a stage observer while the
private result remains identical. They were added after full-suite collection,
so their separate focused exit0 is not full-suite coverage.

Synthetic prices, forecasts and fitted trees in these tests are software evidence
only. The full regression is in progress; do not claim it is green or that the
implementation is qualified for market execution yet. The future integrated runner
must authenticate each arm's model bindings and exact retained V119 control bytes;
self-consistent hashes in pure-component inputs do not establish provenance.

## Source Attempt History

`source-v1` failed before the actual raw scan because the new caller nested the
inherited non-reentrant no-fit profiler. Its failed terminal and stderr remain
unchanged. The repair lets inherited admission own its profiler and guards the
new extraction separately; a focused test checks that entry boundary.

`source-v2` ran from2026-09-27T07:19:23Z to07:39:11Z,
with actual exit0 and unchanged source/runtime hashes. It is the corrected
implementation's first actual source admission, not an economic retry. All181
paired raw files and5485 original events were admitted. Output SHA256 is
`84f9acf2af99129acb9b66b3a8c0a2c35a11d4ca4a27c862e84732120160a8cc`;
context SHA256 is
`29f96dda87ea02393f6669a27f156c120015eb2b387015710db05ccc66909de9`.
These are historical causal price-direction features, not verified aggressor
labels or proof of live arrival timing. Original start, intent, stdout/stderr
and terminal records live under
`reports/nq_apex_tick_pressure_v120_implementation`.

## Remaining Work

Complete full regression and independent code review, bind the integrated
pipeline/account comparison to a frozen execution policy and exclusive claim,
then execute all candidates without exposing partial outcomes. Independently
reconcile account decisions against the fitted distributions and original ticks.
Only a later genuine claim reserves the four planned comparison charges.

At this checkpoint new market fits, economic replays and comparison charges are
zero; the historical total remains13209. No market verdict, live-model change,
Telegram message, broker order, fee purchase or independent-validation claim
is implied by implementation progress.
