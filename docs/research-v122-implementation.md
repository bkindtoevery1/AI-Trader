# V122 Implementation Checkpoint

Checkpoint2026-09-27UTC. This is a curated development record, not a completed
experiment, market-performance result or deployment instruction.

## What Changed

The fixed quarter-stop pullback policy now has three additional implemented
components beyond the pure trigger clock:

- Complete four-mode, guard-free one-MNQ attempt labels. Genuine expiry and
  entry-geometry skips remain zero-payoff observations; missing or invalid tape
  evidence is an error. Every original event remains represented.
- A pending PA account adapter. It freezes the unchanged V119 quantity choice
  before reading future trigger prices, occupies the account through resolution,
  applies cooldown after expiry/rejection/execution, and cancels rather than
  resizing when release eligibility fails. Original NQ Evaluation, zero-capacity
  handling, fees and actual guarded account execution are preserved.
- An explicit new-target training adapter. Original nine-feature membership,
  initial-capacity support, stop support and date-equal weights are unchanged.
  All labels, including excluded events, must mature before the causal cutoff.
  The fixed64-tree empirical forest receives exact one-contract net cents, not
  reference-quantity-multiplied outcomes or a triggered-only subset.

The label metadata and fitted wrapper distinguish this attempt policy from old
fixed-entry targets. Caller-supplied hashes bind bytes but do not establish
external feed completeness, source authenticity or broker fills.

## Software Evidence

The integrated invented-fixture run passed631 unique cases, with no failures or
skips and actual process exit0. The three new component modules contribute
152 label,119 account and41 input tests; the run also covers the pure trigger
core and relevant predecessor components. Separate static reviewers found no
concrete account or input-binding defects in their requested scopes.

One invented forest fit checks the estimator wrapper. It is not a market fit,
strategy trial or profitability observation. The earlier full regression was
collected before these additions and remains pending at this checkpoint; its
eventual result cannot be represented as full qualification of these files.

Local implementation commit:54a731a. This identifier is a private-worktree
checkpoint, not an ancestor published by this documentation branch. No research
source, price rows, fitted artifact, detailed account ledger or credentials are
included here.

## Remaining Work And Lessons

Repeated full-session validation and hashing currently cost O(N+4EN), for N
prints and E events. Tiny passing tests do not prove acceptable real-tape
throughput. A separately verified batch implementation may remove redundant
validation without skipping source records or changing execution behavior.

The complete authenticated reader, three-fold fit/scoring pipeline, V122-specific
account auditor, immutable runner and pre-outcome comparison reservation remain
unfinished. No actual-market labels, model fits, account replay or comparison
charges have run. Proposed charges remain two; historical total remains13213
and the sealed48-date holdout is closed. V121 remains the latest completed
economic study and failed. More complete software is not evidence of a better
trading policy.

## Batch Follow-Up

Later on the same UTC date, the core and label path gained a locally generated
event-major batch. It performs one full-tape validation and hash per batch,
including empty input; the complete label path has three validations and two
hashes independent of event count. Per-event execution scans can remain O(EN).
There is no persistent trusted cache or caller-supplied validation bypass.

The final integration run passed927 unique software tests, exit0, covering all
V122 components and all six retained V119 quantity test modules. Eight complete
pre-change envelopes and32 entry receipts remained bit-exact across both sides
and four modes. Scalar API error precedence is unchanged; day-level entries now
all resolve before any geometry/replay, a documented and tested failure-order
difference that returns no partial results. A separate read-only review found
no actionable correctness or policy regression.

Four bounded invented expiry benchmarks retained exact output hashes; one-run
timings under different host load do not establish real-market throughput.
The older full suite completed with21450 passes, two inherited failures and one
skip; its actual exit was not recovered, and it does not cover these additions.
No post-batch full-suite claim is made. A complete frozen runner still requires
full qualification before market execution. Model fits, replays and new charges
remain zero; the research result and holdout boundaries above are unchanged.

## Source And Three-Fit Follow-Up

The next additive checkpoint connects original stored-export verification to
complete129-day attempt labels and three fixed causal fits. Each original raw
scan, window receipt and old own-product label must reconcile before new labels.
All original feature memberships and the complete scoring queries are checked
before the first fit. The fixed45/87/129-date prefixes, ten-date purges and three
42-date scoring blocks yield192 trees and126 daily distributions. Detached model
callbacks and private accepted-model hashes prevent later record substitution.

Receipt schema2 corrects one distinction before any real V122 market outcome:
historical event-time maturity is not the later administrative verification time.
The final supplied tick is the historical replay watermark; actual source
verification is recorded separately and may occur after a historical cutoff.
This does not establish historical feed arrival or backdate intake evidence.
Legacy receipts are rejected instead of silently upgraded. Trading rules,
features, costs, quantities and model hyperparameters are unchanged.

Eight complete old invented envelopes remain preserved. A narrowly defined
availability/hash projection verifies unchanged business results; new schema2
envelopes are not called byte-identical to schema1. All32 unchanged core receipt
goldens remain exact when supplied their original opaque coverage identity.

The first source-focused test found a text-versus-bytes receipt interface error
(six failures, sixteen passes). Explicit UTF-8 encoding corrected it; the next
run passed22, exit0. A separate connected invented-data test generated labels,
performed all three fits and produced the full scoring calendar; its two tests
passed. Static review found no actionable source or pipeline issue. Additional
tests cover last-day inference failure and a self-consistently rehashed model
mutation. None of these software tests uses real market outcomes as evidence.

Four-account guarded replay, a trigger-aware independent auditor, the complete
frozen runner and its full qualification still remain. No market label run,
market fit, new economic result or comparison charge is claimed. This research
path is separate from the existing Windows signal deployment; its progress does
not mean that live judgments or Telegram trade messages are being produced.

Final focused integration passed1342 distinct cases across20 modules in289.33
seconds, actual exit0, with no failures/errors/skips. Earlier focused counts
overlap this run. The full retained suite was not repeated for this additive
checkpoint; it remains mandatory after the complete runner closure is frozen.

Local source/evidence checkpoint:10c8aab. This private-worktree commit is not
published ancestry on this documentation-only branch. The initial failed test
and corrected evidence are preserved locally. Only this sanitized account of
scope, tests, failure attribution and remaining work is published here.
