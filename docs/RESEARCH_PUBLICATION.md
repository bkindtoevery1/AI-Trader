# Research Publication Record

Prepared: 2026-09-27. Branch: `codex/research-records-v119`.

## Why A Curated Branch

The GitHub repository is public. The existing local research history contains
private detailed evidence and is not published wholesale. This branch starts
from the previously published `origin/main` commit `bfe61a8` and adds reviewed
documentation only. It does not merge the unpublished local main history.

## Included And Excluded

Included: V75-V119 design/result/review notes, the version index, record/PR
templates, and explicitly curated public current/historical summaries. Aggregate
research results are not broker statements or evidence of realized personal profit.

Excluded: raw/licensed prices, detailed trades/account ledgers, fitted models,
local report JSON/XML/logs, credentials, account identifiers, sealed holdout
contents, collector/runtime bundles, operational configuration and deployment.
Research implementation remains in the local Git history at this checkpoint;
this documentation branch does not claim to be a standalone runnable research tree.

## Correspondence

- Local documentation source commit: `bc1d855`.
- Local initial V119 implementation commit: `f8e7eaf`.
- Local completed V119 results/evidence commit: `da3618d`. Only its reviewed
  documentation is copied here; its detailed reports and ancestry remain local.
- Historical version notes are backfilled in version-specific publication commits
  dated now. They are not falsely backdated to their original experiments.
- Public notes replace personal repository/home/temporary-directory prefixes
  with `<REPO>`, `<HOME>` and `<TMP>`. These are display placeholders, not paths.
- V119 source/model/policy hashes in historical notes refer to original local
  evidence, not these path-redacted publication copies.
- Public `RESEARCH_CURRENT.md` and `NQ_APEX_RESEARCH.md` are curated summaries,
  not byte-for-byte copies of private central authority documents.
- Links to omitted local reports/source are historical evidence references;
  GitHub publication does not make those private artifacts available or backed up.

## Result And Publication Honesty

V118 and V119 are closed failures. V119's sole historical replay and postrun
verification completed with exit 0, but PA activity and stress economics failed.
The new policy made only 1/2/1/1 PA trades across four scenarios. Baseline PA
trading PnL was +135.96 USD and stress PnL was -68.50 USD before unpriced program
fees. All PA books closed for inactivity; neither economic contrast passed.
No partial economics were published. Passing checks is not an account pass.
See [V119 results](research-v119-results.md) and [status](research-v119-status.md).

This file records preparation, not a successful push. A remote commit SHA and
verification timestamp will be recorded locally only after the push is checked
against the remote branch. A local SHA alone does not prove GitHub publication.

Future versions should add a frozen rationale/design commit, an implementation
checkpoint, and a separate results/retrospective commit, using the
[record template](research-record-template.md). Document technical failures,
economic failures, deferred work and unknown historical facts explicitly.
