# V122 Saved Cost And Label Alignment Audit

This is post-completion attribution of pinned saved evidence, not a new model
trial. All money below and in `audit.json` is integer cents. Label PnL is NOT
executable account PnL: these guard-free one-MNQ attempts overlap, ignore account
occupation/quantity/lifecycle, and include genuine zero outcomes. Counts are not
independent samples. No candidate, alternative label, filtered-policy result,
forecast, conditional mean, ranking or account outcome is generated here.

## Evidence And Reproduction

- Reproducer: `reports/nq_apex_v122_cost_label_audit_v1/reproduce.py`.
- Deterministic output: `reports/nq_apex_v122_cost_label_audit_v1/audit.json`.
- Synthetic tests: `tests/test_nq_v122_cost_label_audit.py`.
- Saved labels: `reports/nq_apex_triggered_entry_v122/status.json`, at
  `label_generation.attempt_labels_by_date`.
- Saved forest membership/outcomes: the same status, at
  `learned_evidence.fits[*].attempt_fit.forest`.
- Completion: `reports/nq_apex_triggered_entry_v122_execution/execution-verification.json`.
- Frozen manifest: `reports/nq_apex_triggered_entry_v122/preoutcome.lock.json`.

Pinned report SHA256 values:

```text
status     8c0b3220f7fbda71b5480352ceae091fbab080a1501e0e2d037a2cde3177de3f
completion 1177eb294c914632f1d5b59bdde4e4d908f1e106b7dabfbef0fda74be8c61f68
lock       e3eda3068d9345f17ea4437f35b85f0f946cdb793f1241af411361e2c4c2d12c
```

The script verifies these byte pins, their cross-bindings, the eight explicitly
listed relevant source files against the frozen manifest, qualified-source pins
where present, all 129 envelope digests, label/intent/entry receipt digests, all
15,596 mode journals, and the three forests' exact saved-label membership and
outcomes. It checks original/retained stop-support partitions and saved date-equal
training weights without querying any tree. It verifies that the 2,210 saved PA
decisions bind forest three and select zero, without rerunning selection.

The source allowlist covers V78 lifecycle, V85 execution, V87 geometry, V118
forest weighting, and V122 trigger/labels/inputs/account. It does NOT reverify
the entire dependency manifest, raw tape, model runtime or operating system.
No raw-market or Windows file is read. No model module is imported.

Default invocation writes JSON only to stdout after every check succeeds.
`--check` compares its deterministic bytes with the saved `audit.json`; it never
writes. Failed pins, malformed input, inconsistent arithmetic or changed output
return nonzero with no partial JSON. Explicit exception guards remain active
under Python `-O`. The output includes the reproducer's own SHA256, so code changes
also invalidate the saved-output check. There is no execution timestamp to mask.

Actual successful commands:

```sh
python3 -B reports/nq_apex_v122_cost_label_audit_v1/reproduce.py
python3 -B reports/nq_apex_v122_cost_label_audit_v1/reproduce.py --check
env PYTHONDONTWRITEBYTECODE=1 PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 /Users/bkindtoevery1/.local/share/ai-trader/runtime/v111-20260913/bin/python -B -m pytest -o addopts= -p no:cacheprovider -q tests/test_nq_v122_cost_label_audit.py
```

Reproduction: exit 0, 15,596 journals including 11,139 filled unit journals,
zero arithmetic mismatches. Focused synthetic tests: 42 passed, exit 0.
No full repository suite was run. The initial reproducer exited 1 without JSON
because its new checker incorrectly required the same status string in status
and completion; the corrected checker explicitly verifies their distinct pinned
values. No frozen input or economic result was changed.

## Cost And Execution Semantics

Frozen costs, not newly verified broker prices or official account rules:

| Product / mode | Tick value | Commission/side | Slippage/side ticks | RT commission | RT slippage | RT total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| MNQ baseline | 50 | 52 | 1 | 104 | 100 | 204 |
| MNQ cost-only | 50 | 125 | 4 | 250 | 400 | 650 |
| NQ baseline | 500 | 155 | 1 | 310 | 1000 | 1310 |
| NQ cost-only | 500 | 350 | 4 | 700 | 4000 | 4700 |

Costs: `tools/nq_apex_intraday_account_v87.py:78`; actual net arithmetic:
`tools/nq_apex_product_bracket_replay_v85.py:39`. There is no separately observed
bid/ask spread or separate spread charge. Adverse Last-based slippage is embedded
in both fills; `slippage_cents` is not subtracted again from slipped-fill net.

Baseline and cost-only share the first quarter-stop pullback in `[D,D+300s)`,
trigger+60s due time, first entry Last strictly before due+60s, and absolute
`D+5460s` exit deadline. Cost-only adds no latency. Source:
`tools/nq_apex_triggered_entry_v122.py:264`. Cost-only entry is three ticks worse;
the stop follows slipped entry, while the absolute completed mean target stays
fixed. Admission and exit timing therefore can change. Sources:
`tools/nq_apex_intraday_account_v87.py:98` and
`tools/nq_apex_triggered_labels_v122.py:194`.

## Population And Cost Decomposition

| Population / mode | Positive labels | Negative labels | Nonfill/zero |
| --- | ---: | ---: | ---: |
| All 3899 / baseline | 1405 | 1556 | 938 |
| All 3899 / cost-only | 1326 | 1574 | 999 |
| Forest-three 3391 / baseline | 1235 | 1335 | 821 |
| Forest-three 3391 / cost-only | 1158 | 1351 | 882 |

All-population trigger clocks and entry prints agree. There are 861 shared
expiries, 77 baseline geometry rejections versus 138 cost-only, 2900 common fills,
61 baseline-only fills and no cost-only-only fills. All 61 extra rejections are
nonpositive-net-target skips: 49 existing baseline winners and 12 losers.

For every common fill:

```text
cost net - baseline net = delta Last-to-Last gross - 146 commission - 300 slippage
```

| Cost minus baseline group | Count | Net delta | Commission delta | Slippage delta | Last-to-Last gross delta |
| --- | ---: | ---: | ---: | ---: | ---: |
| Common fills | 2900 | -1276000 | 423400 | 870000 | 17400 |
| Baseline-only fills | 61 | 16044 | -6344 | -6100 | 3600 |
| Neither filled | 938 | 0 | 0 | 0 | 0 |
| Complete label population | 3899 | -1259956 | 417056 | 863900 | 21000 |

Only 1329 common fills share an exit print and lose exactly 446 cents. All 1571
others exit earlier in cost-only: 1542 stop-to-stop and 29 target-to-stop. The
positive aggregate gross-path delta is an arithmetic attribution, not evidence
that slippage improves edge. `audit.json` retains each exit-transition component
and the separate forest-three decomposition.

The saved forests contain 1335/2372/3391 labels over 45/85/127 represented dates
from 45/87/129 scheduled training dates. Forest three excludes 508 stop-support
events. No future trigger or winning outcome selects training membership.
Date-equal training weights are not raw label proportions, and neither equals
event-conditional forest probabilities. Exact scored probabilities/means were
not retained. The separate `research-v122-abstention-audit.md` bounds scored
cost-head means below zero; this audit neither reruns nor replaces those bounds.

## Nominal Guard Alignment

For filled labels ONLY, flag `stop_ticks > 5 * target_ticks` using saved slipped
entry geometry. Equality passes. Expiries and geometry nonfills are not assigned
a fabricated target. The actual account guard is at
`tools/nq_apex_triggered_account_v122.py:128`; the labels deliberately omit it.

| Population / mode | Mismatches | Positive / negative | Positive PnL support | Negative PnL support | Signed PnL support |
| --- | ---: | ---: | ---: | ---: | ---: |
| All / baseline | 51 | 47 / 4 | 18862 | -19716 | -854 |
| All / cost-only | 30 | 26 / 4 | 6800 | -25450 | -18650 |
| All / latency-only | 98 | 89 / 9 | 35844 | -48636 | -12792 |
| All / stress | 41 | 36 / 5 | 13150 | -27000 | -13850 |
| Forest three / baseline | 43 | 40 / 3 | 13540 | -12362 | 1178 |
| Forest three / cost-only | 20 | 18 / 2 | 3550 | -9700 | -6150 |
| Forest three / latency-only | 77 | 70 / 7 | 19770 | -33828 | -14058 |
| Forest three / stress | 26 | 22 / 4 | 4600 | -19250 | -14650 |

Zero-PnL mismatch counts are zero throughout. These are unweighted signed sums
of EXISTING label support, not removal gains, revised targets, conditional means,
account eligibility or new-model performance. All-label rows also include
stop-support-excluded events; forest-three rows do not. Actual PA additionally
depends on capacity, release checks, MAE, trailing limits, occupation and lifecycle.
No current PA trade encountered this guard because all decisions abstained.
The diagnostic confirms a disclosed label/account mismatch, not an implementation
defect, a cause of abstention, or proof that guard-aligned relearning would help.

## NQ Context And Limits

Frozen NQ round-trip friction is 0.655/2.350 index points versus MNQ
1.020/3.250. At equal exposure the commission advantage is real in the model;
assumed slippage in points is identical. One NQ nevertheless has ten times
one-MNQ dollar exposure and cannot reproduce smaller micro positions.
At stop 140, NQ reserve is 74700 cents versus 7650 per MNQ, under the fresh-PA
74999-cent effective budget. Five MNQ reserve 38250. Caps, shrinking headroom,
the nominal guard and gap risk remain; reserve is not a guaranteed loss limit.
Sources: `tools/nq_apex_product_bracket_replay_v85.py:24` and `:103`,
`tools/nq_apex_50k_tick_replay_v78.py:155`. No NQ V122 labels are synthesized.

The broad product/cost idea is not new: V85-87 compared actual NQ/MNQ execution;
V98 tested routing; V102 tested separate product learners; V107 compared NQ PA
with an MNQ phase switch. None established a successful full PA route. V110
transferred NQ nominations and V116 used NQ forecasts, also without passing their
primary comparisons. See those versions' existing results/completion documents.
These are precedents, not the exact V122 triggered-policy comparison.

No raw tape, replay, fit, threshold change, strategy selection, holdout access,
trial charge, central-state edit, commit or push belongs to this audit. The failed
original completion and ledger are unchanged. New evidence here is limited to
saved-record reconciliation and descriptive nominal-guard mismatch support.
