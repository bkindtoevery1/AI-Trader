# Poll-Budget Candidate: Offline Timing Evidence

October 7, 2026. Software performance probe only; Windows signal operation is
still unverified/stopped at its latest observation. No deployment occurred.

## Question And Method

The candidate yields before a new transaction once its original source receipt
is4s old, but an in-flight transaction still fails at the unchanged5s limit.
Fixed-clock correctness fixtures cannot establish processing latency. Extend the
existing isolated schema6 package harness with translated monotonic elapsed time
and one separately instrumented cProfile run, leaving all runtime bytes and
resource/type/source/transaction guards unchanged.

Use synthetic preopen NQ/MNQ records and temporary SQLite only. The selected
package is the exact07034 candidate with9e8c controller and446c wrapper. The
fixture clock equals its synthetic origin plus actual perf_counter_ns elapsed;
it is not a Windows clock or historical/live observation. Socket/subprocess
access inside the isolated fixture is rejected. No trading data or account
secrets are read, no signals are published, and no model prediction is exercised.
The original model files are loaded and verified, not refitted or replaced.

## Measured Result

Values below are the final complete package-suite observations on this Mac.
Each row is one sample, not a latency percentile or throughput guarantee.

| Invented Ticks | Source Records | Instrumentation | Cycle Seconds | Committed Records |
| --- | --- | --- | ---: | ---: |
| 2 | 1 | Timer only | 0.276931166 | 1 |
| 128 | 64 | Timer only | 0.288556500 | 64 |
| 4,096 | 64 | Timer only | 0.596709791 | 64 |
| 4,096 | 64 | cProfile plus timer | 1.404270334 | 64 |

All four completed without poisoning or an outbox event. The profiled row
includes substantial instrumentation overhead and is not comparable as a pure
latency estimate. Within that row, native-value recursion `_plain` ran1,027,352
calls (including recursive calls), with0.5690s self time. `verify_lineage` ran
once and consumed0.5323s cumulative; `canonical` ran3,268 times and consumed
0.6372s cumulative. Cumulative times overlap and must not be added.

This identifies repeated state serialization and initialization-history
verification as concrete optimization candidates, not proof of the original
Windows failure cause. A later optimization must preserve external-database
mutation detection, canonical values, lineage identity and commit deadlines;
removing validation or blindly caching mutable state is not justified.

## Evidence And Limits

- `tests/test_nq_v4_poll_budget_package_v1.py` adds four timed modes using the
  actual immutable package loader, native source reader and schema6 store.
- Focused timing run:4passed. Complete package regression:54passed,0skipped,
  exit0,48.24s. The four are included in54, not additive. The entire repository
  suite was not run. The initial invocation failed before running a cycle
  because tools/windows was missing from PYTHONPATH; that invocation is retained.
- Final captured stdout and case results:
  `reports/nq_v4_poll_budget_timing_20261007/package-full.xml`, SHA256
  `bac6a6214d4c6f58878ff381094810080860af39599d9f19897c1f1e8087e29f`.
- Harness SHA256:
  `6c3645685105e7ceccd4322b87f5301dc0c8c083a7f3c07507bfe025e4202afc`.
- Runtime and packaged archive hashes were independently rechecked unchanged.
  No candidate version, Windows file, schedule, restart, credential, order or
  Telegram request changed. Historical research remains13,293effective trials.

The timed tests validate committed-state or fail-closed reporting, not a CI
speed threshold: a genuine freshness failure is recorded as a failure status
in their output, not mislabeled operational readiness. The final run had none.
Preopen synthetic state omits mature minute history, inference, open-position
work, Windows filesystem/antivirus/OneDrive cost and live producer contention.
Do not use these measurements to promise Windows readiness or a signal time.

Reproduce with the qualified Python runtime, PYTHONPATH=src:tools:tools/windows:tests,
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1, python -B -m pytest -q -x --tb=short
-o addopts= -o junit_logging=system-out -p no:cacheprovider
 tests/test_nq_v4_poll_budget_package_v1.py --junitxml=<new-report-path>.
Do not overwrite the retained final evidence file.

