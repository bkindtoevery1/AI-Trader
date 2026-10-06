# V126: Direct Net-Payoff Forecast Screen

Declared October 6, 2026 before any V126 market fit or forecast. The user has
explicitly resumed local model research, independently of Windows login.

## Reason

V121 through V124 repeatedly rejected PA opportunities because estimated net
means under costs were negative, not because contract capacity was absent.
Changing forest split objectives did not resolve that failure. V125's existing
completed computation is being verified separately; its economics were not
used to choose this experiment.

Compare three deliberately different direct conditional-mean learners: ridge,
histogram gradient boosting, and a small two-hidden-layer neural network. This
is a development forecast screen, not a change to an existing strategy's CE,
account, sizing, stop, cost or time rules. Better regression loss alone cannot
establish a tradable edge or an Apex pass. No genetic algorithm is used.

## Fixed Design

- Reuse the authenticated V123 twelve causal price/minute-volume coordinates
  and complete four-mode one-MNQ integer-cent outcomes, including losses/zeros.
- Preserve original 181 development dates, 45/87/129-date training prefixes,
  ten-session purges, and three chronological 42-date scoring blocks.
- The 48 sealed dates from June 29 through September 2 stay closed. The 126
  scoring dates have been reused in prior research; they are not a new holdout.
- Fit weighted feature/target StandardScalers only on the original mature
  training prefix. Use original equal-date weights for scaling; normalize
  weights to mean one for the estimators, fixing regularization semantics.
- Ridge: alpha10, SVD. HGB: four squared-error heads,100 iterations, rate0.05,
  seven leaves, minimum50 events per leaf, L2=10, no early stopping, seed126.
- MLP: tanh(16,8), L-BFGS, alpha10, max_iter300, max_fun30000, tol1e-6,
  no early stopping, seed126. Record nonconvergence without tuning or retry.
- One training-weighted constant mean per fold is the explicit control. There
  is no parameter search, shuffled split, scoring-data scaler fit or winner refit.
- Nine candidate/fold pipelines:18 scaler fits and18 response-estimator fits.
  Three candidate and three control comparisons reserve six charges,13221 to
  13227. A failed attempt retains its charge and original evidence.

## Evaluation

Retain the original supported-query mask and all126 scheduled dates, including
empty dates. Publish predictions before attaching scoring labels or computing
diagnostics. Authentication loads the complete prepared labels; later training
prefixes legitimately include earlier scoring dates. Each fit receives only
its own mature prefix, never its own scoring outcomes. Compute MSE and MAE
within each supported nonempty date, then average
dates equally, for every mode and fold. Also describe the realized unit-label
mean among opportunities whose four predicted means are strictly positive.
These opportunities can overlap: do not add their labels into an account PnL,
call them executed trades, or invent an equity curve. No strategy/account replay
occurs in this stage. Costs/latency are inherited in the original four labels.

A candidate qualifies only for further account-path investigation if all four
pooled date-equal MSEs improve on the constant and both baseline/stress improve
in every fold, with no convergence warning. This is a predeclared screening
rule, not a statistical significance gate or an authorization to deploy.
All candidates and failures are reported, not only the best outcome. Subsequent
account work must retain actual overlap/capacity, costs, trailing loss, activity,
PA and payout rules. Operational V63/V92 stay unchanged.

## Evidence Boundary

Use the existing prepared-source authenticator and its explicit nonexecutable
application-drift guard. Record source/code/runtime identity, one exclusive
claim, every fit start/completion, complete predictions, immutable result and
actual exit. The parent reserves all six comparisons centrally before dispatch;
the runner requires that reservation and its exact source/design pins. Failed
fits retain their reservation and durable arm/fold attempt records.
Do not rerun402million raw rows merely for this forecast-only comparison; the
saved label/source boundary is inherited, not freshly independently verified.
Affected software tests scale with the change. The prior repository-wide suite
is not green and is not relabeled as passing here.
