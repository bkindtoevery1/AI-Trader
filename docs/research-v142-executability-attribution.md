# V142: Selected Labels Versus Actual Fills

October 7, 2026. Post-result attribution on the closed V142/V141 development
books. No new model, fit, parameter selection, raw replay or charged comparison.
The failed account results and total 13,293 trials are unchanged.

## Question And Method

V142's 24 positive-all-head NQ opportunities had positive average guard-free
labels, while every actual account mode lost money. The unresolved question was
whether the same filled events earned different payoffs, or the positive label
values belonged to events that did not fill.

The new tool joins original event IDs and native decision clocks across the
published forecasts, all 126 scored label days and recorded account attempts.
It requires a complete partition into fills, recorded skips and recorded
busy/cooldown omissions, retaining both V142 and its exact saved V141 comparator
in all four modes. Only NQ Evaluation is analyzed: neither arm reached PA.
The existing capacity auditor independently reconciles saved cash and quantities.
Per-filled-event differences are checked, not just a sum that could cancel.

## Matched Results

Amounts are USD sums of the already stored one-contract labels, except the
explicit account-PnL column. Labels may overlap and are not portfolio returns.

| V142 Mode | Selected / Filled Events | All Selected Labels | Filled Labels | Unfilled Labels | Actual Account PnL |
| --- | ---: | ---: | ---: | ---: | ---: |
| Baseline | 24 / 9 | +1,764.90 | -1,602.90 | +3,367.80 | -1,602.90 |
| Cost only | 24 / 6 | +484.00 | -1,557.00 | +2,041.00 | -1,557.00 |
| Latency only | 24 / 5 | +2,084.20 | -590.50 | +2,674.70 | -590.50 |
| Combined stress | 24 / 5 | +1,254.00 | -1,120.00 | +2,374.00 | -1,120.00 |

Every filled event's label equals its recorded net PnL in all eight V142/V141
books. There are no offsetting per-event mismatches hidden by a zero sum. Thus
the positive V142 selected-label aggregate did not describe the events actually
filled. It is not an unexplained same-fill cash discrepancy.

In baseline, ten risk-cap skips account for +$3,419.00 of stored unit labels;
three busy/cooldown omissions account for -$51.20. Two target-already-reached
skips have zero labels. The ten capacity skips divide equally: five reserves
exceed the entire recorded headroom, and five fit the headroom but exceed its
allocated risk budget. The analogous full-headroom/budget-only split is 5/5
for cost-only, 2/8 for latency-only and 3/7 for combined stress.

These are descriptive partitions on the original account path. They do NOT mean
that relaxing a limit earns the skipped-label sum. A changed fill alters later
headroom, exposure, cooldown and lifecycle. Some labels overlap, and the reserve
is not a guaranteed maximum loss. No rejected event was traded in this audit.

The comparator is important counterevidence: V141 risk-cap-skipped label sums
are +$1,266.80 / -$610.00 / -$1,009.60 / -$1,703.00 in mode order. Capacity
rejections are not consistently excluding winners even within this closely
matched comparison. No universal risk-limit relaxation follows.

## Previously Tested Ideas

- [V103](research-v103.md) increased PA risk allocation. Some paths improved,
  but neither product passed the full route.
- [V109](research-v109-completion.md) zeroed guard-inadmissible training payoffs;
  executable economics did not improve. This is not an untried target idea.
- [V133](research-v133-results.md) used MNQ from Evaluation start; smaller
  contracts did not repair stressed economics or depleted capacity.
- [V118](research-v118-results.md) and [V119](research-v119-results.md) used
  headroom-aware utility and integer quantity selection; they did not pass.
- [V137](research-v137-performance-audit.md) learned cash/floor transitions.
  The primary combined score scarcely traded and never completed Evaluation.

[V135](research-v135-results.md) had already demonstrated the gap between
positive overlapping labels and a feasible account path. This diagnostic makes
that distinction exact for V142; it is not a new affordability strategy. A later
model must have a genuinely distinct declared hypothesis and preserve this
counterevidence. No automatic successor or retuned version was created here.

## Verification

The focused/helper suite passed 80 cases. The final affected regression passed
380 distinct cases, including those 80, with actual exit zero in session 57017.
It covers the new partition, existing capacity checks, V142 diagnostics, runner
and saved-result audit. Full-repository regression was not run. Peer review
found a duplicate-date acceptance gap; the final suite rejects 126 calendar
entries masking only 125 distinct sessions. Invented test fixtures are not
market-performance evidence.

The final real-evidence invocation exited zero in session 96805, authenticated
131 input artifacts, and rehashed all 290 frozen V142 source files unchanged.
Report: `reports/nq_apex_v142_executability_attribution_20261007/attribution.json`.
SHA-256: `cc3ec38da70959f55e6addfcf95ebf65286561e108cda9af8fa829aa2a44306e`.
The report retains all event partitions privately; it does not re-admit source
data or independently reconstruct raw fills. All 48 holdout dates remain closed.
Windows recovery and actual Telegram delivery remain separate and unverified.
