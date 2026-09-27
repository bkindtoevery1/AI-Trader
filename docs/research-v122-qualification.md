# V122 Runner Qualification

Checkpoint: 2026-09-27T20:23:44Z. Private source commit:
`6df5c95145ca22d13eed4cc526abfdeb9558d930`.

The frozen runner qualification is complete with the explicitly inherited
non-green suite boundary. It is not a market result, strategy approval or live
signal activation. The user's existing-model signal path remains the immediate
priority; it does not depend on training or evaluating V122.

## Observed Results

- Focused: 1871 passed, no failures or skips, actual exit 0, 444.30 seconds.
- Full: 22682 passed, 2 failed, 1 skipped, actual exit 1, 3608.10 seconds.
- The full suite contains every current focused case and retained predecessor
  case required by the runner. Both observed processes preserved their source,
  parent runtime and selected child runtime snapshots.
- The actual qualification command exited 0 and published the immutable status
  `QUALIFIED_WITH_KNOWN_PREEXISTING_SUITE_FAILURES`. No test failure was removed,
  normalized or relabeled as a pass. Earlier failed receipts remain intact.

The two exact inherited failure IDs are:

1. `tests.test_nq_apex_account_transition_v1_evidence::test_active_state_uses_latest_user_legacy_50k_authorization`:
   an older report-count assertion expects six entries where four are recorded.
2. `tests.test_nq_apex_research_current::test_v88_completion_packet_closes_evidence_not_strategy_success`:
   the old completion packet references a temporary regression XML that is no
   longer present. A replacement XML was not fabricated.

This is not an all-green repository claim. These failures were declared before
this run; their exact identities, exits and retained case census were checked.

## Immutable Evidence

Local evidence directory: `reports/nq_apex_triggered_entry_v122_execution/`.
The raw XML, streams and process receipts remain local, not public market data.

- `qualification.json`: `2240983f8707219ab30458d438a911427f8375c03fb643d3f98f833509dae495`
- `focused-v1.xml`: `73618908a877a98c80672a3d546823b7edd80f6f57d1638fa3835bb7dd9e8f4e`
- `focused-v1.terminal.json`: `c7665a432ce2dd29ef90c8530d9ab3c7eba4da5da8e4d685534a2faaf0a88ce3`
- `full-v1.xml`: `3a276e66e9c446829437f68ba6a018aaab35e589155c283161bc03f97b2b3f2b`
- `full-v1.terminal.json`: `739adad8b02d4b7b49b0c492ebd3d97ecbbae05755b63a31a8d23fed6df4caf1`

## Remaining Boundary

No V122 real-market labels, fits, replay, exclusive claim or comparison charge
has occurred at this checkpoint. The ledger remains V121 / 13213 effective
historical trials. The next research action is the already fixed one-shot run,
then observed postrun verification and immutable completion, not another design
or parameter search. Its two comparison charges apply only after an actual
exclusive claim. Keep the sealed holdout closed and all order flags false.

The frozen runner and its pinned documentation were not edited to report these
results. This separate checkpoint is additive. Software qualification does not
prove live price availability, Telegram delivery, account survival or a pass
before renewal. Both ongoing goals remain active.
