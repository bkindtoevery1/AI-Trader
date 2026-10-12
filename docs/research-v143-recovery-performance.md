# V143 Recovery Performance Observation

October 12, 2026. This is outcome-blind runtime attribution, not another model
trial, a completed label population, or permission to change the running job.
The sole recovery was session20785/PID27410, started04:38:29UTC; the first cell
started04:41:51UTC. At05:19UTC it remained live with no completed cell or failure.
At05:27:07UTC it published completion for one cell. At05:29:58UTC the process
was absent and its live exec session was unavailable after a context transition.
The app's retained commandExecution record subsequently established actual
exit0 and2920505ms duration for that exact invocation. This terminal evidence
is separate from the producer's self-reported completion and PID absence.

## Measured Versus Inferred

A one-second native process sample at04:45:07UTC found82/82 main-thread samples
inside JSON encoding, including nested dictionaries and float formatting.
It cannot identify the Python caller or establish the whole-run time share.
No labels, account outcomes or process variables were read by the sampler.
Private sample SHA256:
612183beda05a93e6f790e5fc3a1b37ed0e895798982c5c72de556fe754a3e56.

At that observation, ps RSS was about3.0GiB; the sampler reported physical
footprint7.3G and peak8.7G. These are distinct metrics. The frozen8GiB guard
uses resource.getrusage().ru_maxrss, not physical footprint. The sample alone
does not prove a guard violation or compliance of total physical footprint.
A later system memory-pressure query reported46% free memory.

The saved complete first cell records2714.562703 seconds (45.24minutes),
27 complete action pairs and13,968 original-teacher NQ queries. It has27 NQ
training rows and zero MNQ rows; this single anchor does not establish either
product's full training support. Process high-water RSS is4,898,029,568 bytes
(4.56GiB), within the unchanged8GiB guard. This is not a claim about peak total
physical footprint. The stored cell is1,319,611 bytes. No advantage targets or
account results are exposed here. One cell is not a precise full-run forecast.

Independent read-only code review identified bounded redundant work, not an
apparent infinite recursive call. The sampled floats are more consistent with
event/account-history serialization than integer-only tick-window records.

## Concrete Repeated Work

- mixed_account_v104._copy_window materializes lists, reconstructs tuples and
  invokes the full TickWindow validator. Population, each pair and each branch
  day repeat this. For27 pairs across all10 nonterminal horizon dates, the
  structure schedules1620 session copies inside forks plus22 outer copies;
  early absorbing terminals can reduce executed branch-day copies. This is a
  static count, not measured calls, and excludes event-window copies.
- Population and fork readers each copy and hash the complete returned window;
  transition dispatch copies it again. The repeatability maps compare hashes
  after recomputation, not cache computation. The underlying four-window LRU
  does not eliminate outer copies or validation.
- Every fork decision makes two public-account JSON round trips. Those snapshots
  contain prior trades and phase days, while later dispatches deepcopy accumulated
  private observations. Snapshots exclude private observations themselves, so
  this is history amplification rather than a self-embedding cycle.
- V1 hashes the full pair. V2 discards that hash, adds policy metadata, hashes
  the full pair again and deepcopies it. Population ultimately retains mostly
  outcomes and the pair hash. This duplication is real, but its runtime share
  is not established by the one-second sample.

## Next Qualified Experiment

Status: NOT_IMPLEMENTED and NOT_ADOPTED. With the original first cell retained,
the narrowest proposed prototype is a cell-scoped immutable-window copy and
validation memo through private adapters. Keep mutable histories, predictions,
execution, callback order, digests and all economic conditions unchanged.

On a miss, execute the original complete copy/validation. A reusable proof must
bind exact native metadata, recursively immutable integer tick tuples, strong
references and unchanged validator/runtime bindings. Return detached new window
shells sharing only proven immutable rows. Mutation, rebinding, subclasses or
unproved contents must invalidate/fall back. Release the bounded memo per cell.
The existing V137 label accelerator demonstrates a proof pattern, but targets
build_event_grid and is not a drop-in continuation implementation.

Require complete canonical pair/population byte and hash equality, successor
state equality, both actions/origins and all modes, PA transitions, terminals,
zero capacity, malformed inputs, mutation, detached outputs and full horizons.
Measure actual timing and memory separately. Fewer validation calls do not
prove a speedup, and window memoization may leave the history-JSON cost intact.
Do not delete checks, shorten horizons or change the research question to make
the benchmark faster. The producer is no longer running; the original cell and
frozen implementation remain unchanged. No additional batch is started here.
