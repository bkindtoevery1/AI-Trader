# V116 Source Audit Repair

The only market run exited 0 at 2026-09-22T17:23:17Z. The first source audit
exited 1 at 17:24:31Z before source restoration. Its execution guard replaced
account methods with throwing functions, which correctly triggered the inherited
V103 frozen-engine identity check. This is an auditor defect, not evidence of
strategy failure, and not permission to replay, refit, retune or charge a new
comparison.

The failed v1 auditor, launcher, logs and failure receipts remain immutable:

- Auditor SHA256: `e0c80934b6516672561f9a66f8f116acf530eb39b1504d2e871a340ba55027db`.
- Source terminal: `4ac684b46bdcad9e5fbe9dd616cfea15ec2ee1578a84de5da9457295a7aeb5c1`.
- Source stderr: `c3d48be457f505c023ecb666aaaf749106bc0497fc25350715b9cced83889c01`.
- Failure receipt: `9eac32a166b4b07fa2e71ccf9d60bd99be75ec4ab5e593565a3a65864676e1c4`.
- Successful market terminal: `5940866611960e90f758db0bdea807dc616393199c8b051855cec6eb36d0029d`.

An additive v2 auditor will preserve method identity while rejecting entry to
training, raw-replay and account-execution functions. Its own receipt namespace
is `terminal-audit-v2.*`; observed audit processes use `source-audit-v2.*` and
`account-audit-v2.*`. Existing v1 evidence is not overwritten or reclassified as
successful. Market code, gates, all 24 market outputs, the sole claim and three
comparison charges remain unchanged.

The v2 launcher and completion recorder are mechanical namespace adaptations of
their original counterparts, with explicit new code hashes. The independent
JavaScript account arithmetic remains byte-identical. Invented-data tests and
an actual no-data frozen-engine identity check must pass before explicit v2
source-audit dispatch. Both successful terminal audits are still required for a
verified economic interpretation. This document records the repair rationale,
not an audit pass or a strategy result.
