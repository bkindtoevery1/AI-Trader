# V118 Pure Learning Components

## Scope

The preceding goal turn made progress: V117 completed a real existing-data
replay, both successful audits and its unsuccessful economic conclusion were
recorded in commit5f13ba2. It was not a data-wait turn or a zero-observation
model failure. V118 is a separately declared successor, not a restarted V117.

Implemented three new, isolated components without changing any frozen ancestor:

- `tools/nq_apex_distribution_inputs_v118.py`: validates complete original MNQ
  journals and strict label maturity before stop filtering; produces exact
  one-contract cent targets rather than fresh-reference-quantity dollar targets.
  Reweights retained events equally within each training date and binds arrays.
- `tools/nq_apex_distribution_forest_v118.py`: fits the fixed sklearn forest,
  exports complete leaf memberships and date-weighted empirical outcomes,
  verifies native float32 routing and conditional means, and rejects malformed
  model/support/runtime records. The fit parity check uses leaf means, not a
  quadratic training-row probability matrix. Query mass matrices are bounded
  at two million cells; callers must batch larger requests.
- `tools/nq_apex_state_utility_v118.py`: evaluates four-mode expected exponential
  certainty equivalents using log-sum-exp, exact deterministic outcomes and
  compensated near-zero arithmetic. Tiny mass-rounding tolerance is not a
  selection threshold. Unresolved sign or unrepresentable arithmetic fails
  explicitly rather than clipping a loss or inventing a positive forecast.

The source-population adapter is not external admission. Its caller still has
to authenticate actual source bytes and bind the exact causal fold calendar
and maturity cutoff. No component opens files, creates a claim, deploys a
model, or executes accounts/orders. Synthetic fitting tests cannot prove
market usefulness or establish a fitted market model.

## Verification Boundary

Focused tests cover native/restored forest parity, date-equal outcome mass,
empirical loss dispersion, float32 split boundaries, source-unit versus
reference-quantity labels, prefilter validation/maturity, input detachment,
closed record types, no retry, finite arithmetic and independent Decimal CE.
Adversarial allocator examples test both a genuine own-H/fixed-H decision
difference and exact q/H cancellation. Zero quantity is rejected by the pure
utility function; the future account adapter must preserve original zero-cap
attempt/cooldown semantics.

The implementation receipt in
`reports/nq_apex_state_distribution_v118_implementation/component-evidence.json`
records the final scoped test result and source hashes. The independent review
is `docs/research-v118-adversarial-review.md`.

Final focused run: 398 passed, zero failures/skips, exit0 in3.80seconds. This
includes142 new V118 cases and256 unchanged population/bracket regressions.
The adversarial review found two canonical-JSON container counterexamples;
explicit native leaf types fixed both, and the failed tests/history remain.

An unrestricted full regression is NOT claimed for this component checkpoint.
The latest completed V117 qualification was 18,851 passes, two known failures
and one skip; it does not qualify new V118 code. Full regression and actual
source admission are required after the account/runner integration and before
a market claim. Isolated component tests are run now instead of repeating a
long full suite for each unfinished integration layer.

## Next Required Work

1. Bind original complete three-fold training plans and prepared source identity
   to these components, with no future labels or control-account state.
2. Implement the own-state account decision adapter after busy/day-stop checks
   and before future entry-tick reads. Preserve zero-cap attempt cooldown,
   later nominal guards, dynamic sizing and unchanged Evaluation projections.
3. Integrate the fixed twelve-book runner, exact controls, three durable forest
   fits, complete raw receipts, exclusive freeze/claim and terminal publication.
4. Qualify focused/full tests and actual admitted data, then charge five
   comparisons once and run the whole development replay. Reconcile economic
   results separately from software success; keep all48holdout dates closed.

At this checkpoint: zero V118 market fits, zero account replays, no claim,
no reservation and no performance result. Ledger remains13201; latest completed
economic experiment remainsV117. Five planned charges would become13206 only
after a genuine claim. No Windows/new-data dependency, orders, Telegram,
credential transfer, purchases, schedules or operational model change.

## Windows Coordination

The bounded read-only coordinator request completed in turn
`01a0cb33-57d2-78f0-acea-f297e741222a`, but the cross-host snapshot/read APIs
returned no message or evidence items and no new Mac intake report arrived.
Message delivery/completion is not proof of current connection, fresh ticks or
running inference. Existing Windows readiness remains unverified; this does
not block Mac model development and did not trigger another connection setup.
