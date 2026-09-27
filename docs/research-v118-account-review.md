# V118 Distribution Account Review

## Findings

- Confirmed and fixed by the implementation owner: duplicate event IDs were
  accepted and the PA `by_id` lookup could substitute a later probability row
  for an earlier decision. The first focused run had one failure and 16 passes.
  The retained regression now passes with the new unique, chronological event
  validation before callbacks. No implementation or frozen ancestor was edited
  by this reviewer.
- The legacy `pa_support_nomination.nominated` counter counts distribution
  support before dynamic utility decisions, including busy events. It is not
  the number of CE-positive candidates or executed trades. The owner's new
  `support_nomination_count_is_pre_utility_not_trade_count=True` policy field
  explicitly distinguishes this. Tests retain original accounting and verify
  examples with two supported rows but one CE nomination, and four supported
  rows but only two CE decisions. Use `state_utility_decisions` for actual
  decision evidence; quantity-zero rows have null CE and nomination fields.
- No additional behavioral defect was confirmed by this bounded review.

## Synthetic Coverage

- All four modes and both directions: exact V107 Evaluation and PA reports
  after removing only `distribution_policy` and `state_utility_decisions`.
- Independent fixed/own headroom decisions, realized state after the latest
  completed trade, current quantity changes, unlocked six-MNQ capacity, and
  fresh original PA state after Evaluation transition.
- No entry read on CE abstention, no CE for busy/day-stop/terminal events,
  all-four-head strict positivity, and no new cooldown for model abstention.
- Zero capacity retains original entry resolution, nominal-guard precedence,
  capacity attempt, and five-minute cooldown in all four modes.
- Complete envelope validation before callbacks, source detachment, callback
  exceptions including KeyboardInterrupt, late wrong-product/CE failures,
  original-account mutation, reentrancy, and full rollback with clean reuse.

## Final Focused Receipt

Original Python runtime, execution session `7798`, exit code `0`:

```text
84 passed in 1.17s
```

```sh
PYTHONPATH=src:tools PYTHONDONTWRITEBYTECODE=1 \
<HOME>/.local/share/ai-trader/runtime/v102-20260912/bin/python -B \
-m pytest -o addopts='' -q --tb=short tests/test_nq_apex_distribution_account_v118.py
```

These file hashes were identical before and after the final run:

- `tools/nq_apex_distribution_account_v118.py`:
  `73fdaccf3d27d4c41848e156ba3ae512bc2b82c9717dc8452052416d7e558408`
- `tests/test_nq_apex_distribution_account_v118.py`:
  `c7e9fba5d21dbe4a09e27d36631de5edff933a75398f3004b56890f77761de03`

## Boundary

Invented distributions, forecasts, and tick fixtures only. No market fits,
trials, historical account replay, source admission, central writes, or full
regression were performed here. Model/population/source authentication remains
the caller's responsibility. Unit-outcome CE is a decision proxy, not an exact
account outcome or financial-performance claim. Parent owns combined and full
qualification.
