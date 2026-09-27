# V119: Joint Cost-Aware Integer Quantity Choice

Outcome-informed successor to the closed V118 experiment, declared before any
V119 historical policy execution. Existing admitted Mac data suffice. Windows,
new sessions and new fitting are not prerequisites.

## Hypothesis

V118 tested the allocator's maximum permitted quantity and then either entered
or abstained. Both policies abstained throughout PA. This experiment asks
whether jointly choosing quantity and entry avoids excessive risk aversion at
maximum size. It is a decision-policy extension, not a new predictive fit.
V94 used an initial-capacity target, V102 tuned forecast hyperparameters, and
V118 varied utility risk tolerance; none of these jointly optimized the
integer quantity over the same conditional outcome distribution.

Reuse the exact three fitted V118 forests and all original nine features,
181 admitted explicit-contract NQ/MNQ pairs, 45/87/129 training prefixes,
ten-session purges and three 42-session scoring blocks. Restore and authenticate
all models and daily distribution hashes. No refit, seed search, changed
training population, feature, calibration or risk-tolerance coefficient.

## Single New Policy

At each otherwise eligible PA decision, after any prior trade resolves and
before reading its future entry, obtain capacity Q from the unchanged account
allocator and H from this account's current balance minus trailing floor.
For every integer q in 1..Q evaluate the unchanged four-mode exponential
certainty equivalent CE_m(q,H). Choose the q maximizing min_m CE_m(q,H), with
flat q=0 assigned utility zero. Strictly positive utility is required to enter;
exact ties choose the smaller quantity. There is no admission epsilon, minimum
trade quota, clipping, mode removal or replacement of costs by gross returns.
All numerical errors abort rather than silently choosing flat.

Q=0 keeps the original capacity-skip attempt and cooldown semantics. Choosing
flat with Q>0 is model abstention and reads no future entry. A positive choice
does not guarantee execution: the unchanged actual-entry geometry and PA 5:1
guard still apply. Store the full ascending quantity/CE table and chosen q in
the causal decision journal; preserve size_decision as capacity, not an invented
smaller cap. The actual trade must use the chosen quantity, bounded by Q.

Evaluation remains the exact original NQ path; only PA MNQ quantity choice
changes. Keep half-headroom sizing, the original NQ<=1/MNQ<=6 study caps,
fresh-PA ceiling5, stop<=140, costs, adverse slippage, latency, 300-second
cooldown, uncapped daily fills, trailing/MAE/activity/payout rules unchanged.
This experiment's tighter NQ limit does not redefine the user's general cap.

## Complete Evaluation

Replay one new policy's four full 126-session books. Compare against the exact
audited V118 original-all-heads and own-headroom reports, not newly refitted or
modified controls. Verify all four Evaluation prefixes and input hashes. Raw
ticks drive any new execution; guard-free unit outcomes remain prediction
proxies, not actual account profit. No sampled/synthetic data are economic
evidence. Do not inspect or publish partial economics.

Primary contrasts are joint quantity minus original and joint quantity minus
V118 own-headroom. Both must strictly improve PA trading PnL in baseline AND
combined stress, without extra hard/MAE breaches or earlier inactivity. Report
absolute PA profit, activity, numerical Evaluation, survival, hypothetical
payout and full-route gates separately. Trade count is descriptive, not a
new success gate. Zero-trade zero PnL is not a pass.

One new policy plus two declared contrasts charge three comparisons once,
13206 to13209, on an exclusive claim. There are zero new fits and four new
account books (504 scheduled account-days); eight controls are reused evidence,
not fresh independent samples. Maximum quantity checks are actions within one
fixed policy, not independently selected model trials. Retain the complete
failed attempt on any error; no restart, integrity retry, retuning or fallback.

## Interpretation And Safety

Historical dates were observed in earlier development. Chronological fitting
and purges control within-model leakage but do not restore an independent
holdout or prove generalization after 13,000-plus comparisons. Keep the sealed
48-date holdout closed. No verified personal account pass, priced program
fees, received payout, model promotion, orders, purchase, Windows deployment,
Telegram test, secret transfer or schedule change is part of this study.

Use focused causal/quantity tests and the full software suite before execution.
Known predecessor failures must be disclosed, not relabeled as a passing suite.
Hash-bind code, policy, runtime, original completion and input model receipts.
