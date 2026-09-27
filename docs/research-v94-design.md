# v94: Matched Initial-Capacity Objectives

Pre-outcome design. No v94 fit, outcome scan or comparison reservation has yet
occurred. Freeze this design, code, tests, policy and sources before running.
The current target is Apex Legacy50K Tradovate Evaluation, not the historical
25K goal string. This is outcome-informed development, not an independent test.

## Question And Controls

On the identical broad v92 events and nine causal features, does predicting
initial-capacity dollar exposure improve paired dollar forecasts versus a
matched unit-stop-risk learner and a causal dollar mean? This is a target-space
parameterization and loss-weighting experiment, not a pure loss-only ablation
or proof of optimizing account utility. v93's rejected interactions are absent.

Keep the exact v87 account implementation and its risk reserve, whole-contract
rounding, costs, clocks, stops, mean targets,300-second cooldown and uncapped
daily fills. Do not remove the half-headroom rule or choose a new budget after
observing losses. NQ<=1 and MNQ<=6; no quantity is chosen from model confidence.

For each event and product, use a fresh baseline Legacy50K account's initial
size_limit at the known completed-anchor stop. Initial balance5,000,000 cents,
floor4,750,000, budget124,999. The inherited reserve is already cost-stressed:
NQ500*stop+4700, MNQ50*stop+650 cents. The resulting q_ref is the same across
execution modes. This is an INITIAL-state support/target proxy, not later-path
affordability or a loss guarantee. The real account continues using its own
path-dependent size_limit; do not reset it at an event or fold.

The three matched policies retain only q_ref>0 events. q_ref=0 events receive
null predictions, remain counted as unavailable and are not zero-return data.
Validate the COMPLETE original training event/journal prefix before this
deterministic filter. Bind both full-prefix and retained IDs, and reapply40
events/20 event-dates of minimum support to each retained product/fold prefix.
Never hide invalid or missing labels by filtering them out.

For each mature retained unit journal, D=q_ref*net_cents/100, directly from
native integer cents, not reconstructed from rounded R. Preserve its original
unit-R label as the matched control. A valid geometry/cost skip's zero unit
journal remains a valid zero target; missing or infeasible data does not.
Reweight each retained date to total1, shared by its events. Use the same
StandardScaler and alpha10 SVD Ridge with intercept for both objectives.

One eight-output fit has ordered heads D_baseline,D_cost_only,D_latency_only,
D_stress,R_baseline,R_cost_only,R_latency_only,R_stress. All coefficients are
independent, so the solve is mathematically separable into two four-output
fits. Test this algebra and output independence synthetically. Each policy
selects using ONLY its own four strictly-positive outputs and the common
feasibility mask, never positivity of all eight outputs. There is no clipping,
seed search, calibration, epoch selection, inversion or mode reselection.

Four policy kinds per product are counted: new feasible_dollar, matched_R,
derived dollar training_mean, exact old all-universe v92_control. The last is
a contextual whole-policy control, not the matched target-objective comparator.
It preserves exact old predictions and account paths. Eight comparisons add
to13,097, giving13,105 ONLY when the one-shot run is claimed. Schedule6 joint
estimator fits,6 scalers,48 learned heads (24 primary/24 matched),6 reused v92
fits with no refit and24 derived mean outputs with no extra fit. Log actual
invocation/completion stages rather than treating the schedule as evidence.

## Chronology And Evaluation

Retain the181 admitted raw pairs,55 warmup dates, three42-session scoring folds
and ten full-calendar purge dates. Every original training label in every
mode must resolve strictly before the first purge session's09:00 ET predictor
window, including labels later excluded by q_ref. Validate both product
prefixes before fitting either. Every current-date decision precedes opening
its raw outcome tape. Rebuild complete unit journals during ordered raw replay
and require exact v92 source/journal/control conformance; no cached label
shortcut is used in this version.

Before loading new labels, verify at least30 feasible scored dates per product
and every fold's feasible training support. Feasibility counts are structural
upper bounds, not executed coverage, forecast power or profit evidence.

Compare D predictions, matched R predictions multiplied by known
q_ref*stop_ticks*tick_value_cents/100, and the same-prefix date-weighted meanD.
Use exactly the same feasible event IDs and equal-weight nonempty event dates
for every paired dollar MSE. Report excluded events and empty-feasible dates
separately; do not invent zero loss for them. Require lower mean-four-mode MSE
than BOTH controls in the same two of three folds and lower pooled average,
baseline and stress MSE than both. These are preregistered development screens,
not proof of statistically significant forecast superiority.

Keep the previous practical screens: positive net in all four modes, baseline
Sharpe>=0.5, positive stress Sharpe,30 active baseline dates, baseline HAC
effective samples>=84, family block-bootstrap p<=0.2 and numeric Evaluation
in baseline AND stress. PA survival/payout remain separately assessed. MSE
improvement alone is not a main-model pass. Exact program fees, liquidity and
operational compliance remain unresolved; no verified50K pass is claimed.

The eight-policy circular bootstrap retains2000 draws, blocks10 sessions and
new fixed seed20260994. Compare centered sums using integer cents and exact
inclusive ties, correcting v93's documented rounding weakness only in this
new version. With n equal-length observations and total T_k, a draw's centered
numerator is n*sum(resampled_cents)-n*T_k, compared to n*T_candidate. This
avoids float tie tolerance choices. Test against a rational arithmetic oracle;
equal observed means name the lexicographically first candidate regardless of
mapping insertion order. Do not alter frozen earlier probabilities. HAC remains
the inherited method.

Keep all126 scored dates in account/performance calendars, even when no event
is feasible. Multiple counterfactual unit labels are not an executable
portfolio. Guard-free fixed1NQ/6MNQ diagnostics differ from actual account
quantity and must not be called account profit or target-dollar performance.

The final48-session June29-September2,2026 holdout remains closed. No prospective
data, operational paper outputs, human decisions, orders, purchases, Telegram
secrets or genetic algorithms are part of this experiment. Preserve every
frozen predecessor byte, failure, count and residual audit limitation.
