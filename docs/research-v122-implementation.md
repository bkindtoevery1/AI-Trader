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
