# V131 Results: More History Did Not Establish Forecast Value

Completed October6,2026,07:33:09UTC; terminal07:33:10UTC. The sole supervised
attempt and a separate read-only audit exited0. Twelve fixed pipelines completed
without native market warnings. No restart, refit, account replay or holdout read.

## Why And What Changed

[The design](research-v131-design.md) was published before execution at
`f511e97974ef4ca48749660c16a1a84e7c2015bb`, branch
`codex/research-records-v131`. Private implementation commit: `475db18`.
Following V130's stress-account failure, change the learning target to own-product
91-minute signed close-to-close gross returns and compare recent versus longer
history. This is not another net-payoff decomposition or first use of long minutes.

The same twelve causal features, fixed Ridge(alpha10,SVD), equal total training
weight per nonempty date and chronological folds apply to both history arms.
617complete paired development sessions and19,142broad events authenticated.
The older436sessions add13,657events;20of those dates contain no broad events.
Empty dates remain in the calendar. NQ/MNQ use their own prices and identical
event/query identities, not independent underlying markets.

| Fold | Recent Scheduled / Nonempty Dates | Long Scheduled / Nonempty Dates | Recent / Long Training Events |
| --- | ---: | ---: | ---: |
| 1 | 45 / 45 | 481 / 461 | 1430 / 15087 |
| 2 | 87 / 87 | 523 / 503 | 2670 / 16327 |
| 3 | 129 / 129 | 565 / 545 | 3899 / 17556 |

Both products share these counts. Each training prefix precedes ten purged
sessions and42scored dates. All126scored dates remain, each with events;
3,747matched scored events per product. Twelve Ridge and twelve X-scaler fits;
no Y-scaler, tuning, orientation inversion or new trade policy.

## Complete Forecast Results

MSE is in basis-points squared; MAE and selected gross labels are basis points.
Errors and sign accuracy weight each nonempty date equally. Selected labels
weight opportunities equally, overlap in time and are NOT executable trades.

| Product / History | MSE | Training-Mean MSE | MAE | Mean-Anchor MAE | Sign Accuracy | Positive Predictions | Selected Gross Label Mean |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| NQ recent | 1181.5486 | 1174.9187 | 24.8266 | 24.6850 | 51.57% | 1912 | +2.0223 |
| NQ long | 1181.4267 | 1174.5972 | 24.7472 | 24.6784 | 49.74% | 1321 | +1.1187 |
| MNQ recent | 1181.2711 | 1174.6598 | 24.8237 | 24.6819 | 51.43% | 1912 | +1.9796 |
| MNQ long | 1181.1253 | 1174.3384 | 24.7428 | 24.6758 | 49.55% | 1322 | +1.0759 |

Long history reduces aggregate MSE only0.0103% for NQ and0.0123% for MNQ;
MAE decreases0.3200% and0.3259%. All four models have worse overall MSE AND MAE
than their own training-mean anchors. MSE is0.56%-0.58% above those anchors.
Direction accuracy and selected-label means decrease with the extra history.
No statistical-significance or economic-benefit claim follows these descriptions.

| Product / History | Fold1 MSE | Fold2 MSE | Fold3 MSE |
| --- | ---: | ---: | ---: |
| NQ recent | 888.1968 | 1350.9607 | 1305.4882 |
| NQ long | 878.5673 | 1338.2632 | 1327.4495 |
| MNQ recent | 888.2825 | 1349.6421 | 1305.8889 |
| MNQ long | 878.5146 | 1337.0372 | 1327.8240 |

Long history improves folds1/2 but worsens fold3, almost cancelling in aggregate.
Do not select favorable folds/products or invert the completed predictions.

## Interpretation And Limits

The admitted data volume is sufficient to fit this small learner; this particular
fixed feature/linear-target recipe has not demonstrated added forecast value.
That does not establish that older data, nonlinear models or all other targets
are useless. Adding history also changes effective regularization relative to
the total mean1-weighted loss; the design disclosed this confound in advance.

Economic verdict remains **NOT_EVALUATED**. Positive gross endpoint labels omit
execution timing, stops, costs, account headroom, overlapping exposure and fees.
They must not be presented as dollar profit, strategy wins, or an Apex pass.
The reused126development dates are not independent validation;48sealed dates
remain closed. This stage neither passes nor fails a newly invented economic gate.

No operational replacement is justified. A future preregistered account stage
would need an explicit confirmation/veto interface over retained nominations,
unchanged costs/sizing and whole-route state; no such follow-up is launched here.
Alternatively a distinct hypothesis must be fixed before new outcomes, not a
rescue tuning of this completed run. Three comparisons remain charged,total13,243.

## Verification And Completion

546focused tests and724affected tests passed (1,270unique);24warnings belong to
retained V126 synthetic fixtures, not the V131 market run. Full-repository suite
was not run/claimed green. Integrated review repaired constant-coordinate native
roundoff admission, missing mean-anchor MAE, input-bound fit diagnostics and
dependency-pin completeness before freezing and fitting. No xfails remain.

Final source preflight verified617allowlisted original/normalized/SQLite pairs,
same-maturity contracts and original broad-event/feature conformance. Supervisor
exec65640/PID31917 and child31939 exited0; both are absent. Separate audit
exec56056 exited0: three sealed files, twelve restored models, exact predictions
and complete summaries verified without fits. This shares the implementation;
it is not an independent numerical replication. All required processes terminal.

| Evidence | SHA-256 |
| --- | --- |
| Claim | `3f021f028f2ef22029c62d94691b554925f9c5667e30f8bc2bb325071d61113a` |
| Result | `cdc80f210b6a4b1ab12be441f30373bab88d7e2d6bdf1283a44d10af98d136e9` |
| Status | `4be283b279a27e204f2162648d68a3dfb9ea844635fb5bd51223a277fa4fc4a3` |
| Seal | `e9086daf09529c3d133b077c993a884beacaea4834fb45d7905d5a6fe58ccf1f` |
| Terminal | `11227837c2949c6d1ed4fbc1f277a377084ed2286200ef96279a220e9b031bbd` |

The central ledger retains the original reservation and observed terminal/audit.
The overall research/Windows goal stays active. Windows remained idle revision615;
no new login, collector, live-model or Telegram delivery evidence was obtained.
No Windows settings, schedules, secrets, live orders or purchases changed.
