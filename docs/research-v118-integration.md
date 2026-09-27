# V118 Causal Account And Replay Integration

This extends the existing conditional-outcome components without changing the
frozen learner, utility calculation, policy, original accounts or V117 result.
Existing Mac data are the research input. Windows and new sessions are not
prerequisites. This implementation is not a market claim or a performance result.

## Implemented Path

- `nq_apex_distribution_plan_v118.py` binds the three original MNQ source fits
  to exact 45/87/129-date training prefixes, ten full-calendar purge dates and
  42 scored dates each. It reconciles original source populations before
  preparing the one-contract MNQ targets and binds the forest to that source.
- One fit has three ordered observer stages. Restoration never refits. Pure
  daily distributions use the original nine completed-event coordinates and
  are independent of any account's Evaluation outcome or later state.
- `nq_apex_distribution_account_v118.py` keeps NQ Evaluation unchanged and
  evaluates PA certainty equivalents only after busy/day-stop checks, using
  the current candidate account's own quantity and remaining headroom before
  reading its future entry tick. CE abstention does not consume cooldown.
  Zero capacity still resolves the original attempted entry and cooldown.
- The execution loop is a narrow PA-only adaptation of V104. Actual trade
  execution, costs, slippage, geometry guards, sizing and lifecycle remain
  in the original kernels. Callback errors or mutations roll back the whole
  day, including earlier completed trades and decision evidence.
- `nq_apex_distribution_replay_v118.py` scans all181 same-maturity raw pairs,
  reconciles both products' four-mode journals, and returns only twelve
  complete books. Four controls and eight candidate Evaluation projections
  must reproduce exactly. Both primary contrasts must improve baseline and
  stress; the diagnostic fixed-H contrast cannot rescue a failed primary gate.

The replay API deliberately owns neither source authentication nor fitted-model
authentication. Its caller must produce the distributions through the admitted
plan/forest path and bind those bytes before any market claim. A correctly
shaped invented envelope is software-test input, not evidence of a fitted model.

## Review And Limitations

Independent account review caught duplicate event IDs that could rebind an
earlier event to a later probability row. Uniqueness and chronology are now
required before callbacks, with the reproducer retained as a passing regression.
The original support-nomination counter counts pre-utility support, not actual
CE-positive decisions or trades; the new policy explicitly labels that meaning.

See `research-v118-account-review.md` and `research-v118-plan-binding.md` for
bounded reviews and APIs. The full-loop tests use invented tapes, forecasts
and distributions only. No test PnL is strategy evidence. Unit-journal CE
remains a proxy, not expected account PnL or a learned account-value function.

## Completion Boundary

Verification completed on 2026-09-22 UTC:

- Focused:803passed, exit0, source bytes unchanged;351 V118 cases and452
  unchanged neighboring cases. This turn added209 cases.
- Full:19202passed,2known failures,1skipped, exit1; source bytes unchanged.
  All351 V118 cases passed. The suite is not globally green. Existing failures
  are the V102 four-policies/six-charges assertion and the missing temporary
  V88 XML receipt; neither frozen assertion nor evidence was rewritten.
  Counts come from19205 unique testcase nodes, not the aggregate suite header:
  that header reports19294, an89-case excess also present in the prior V117
  full XML. The preliminary header-derived19291pass count was corrected;
  the original XML was not rewritten. No root cause for the aggregate excess
  is asserted by this integration checkpoint.
- Actual existing-source admission: exit0. Source identity remains
  `bb5040a283e9149f6daa3450f2aa5b420313bea468e6891549ea60b5c804b20a`.
  The45/87/129 scheduled training prefixes retain1335/2372/3391 events on
  45/85/127 distinct dates. These prefixes overlap; do not add their counts
  as independent samples. Empty retained dates do not shorten either purge.
  All126 scoring dates remain outside their own fitted training prefix.

The source-admission stdout was normalized from the completed tool response;
its observation receipt explicitly distinguishes that from a child-generated
process receipt. Focused/full runs use the existing child-exit evidence harness.

Focused/full test and input-admission results are recorded separately under
`reports/nq_apex_state_distribution_v118_integration`. The prior component
receipt remains immutable and is not relabeled as completed market evaluation.

The exclusive five-comparison claim, market fit-stage persistence, authenticated
terminal publication and independent recorded-account reconciliation remain
required. Actual V118 market fits and market account replays are still zero.
The trial ledger remains13201; latest completed economics remains V117.
No partial outcome, holdout access, order, operational deployment, Windows
change, secret transfer, purchase or schedule change is authorized by this work.
