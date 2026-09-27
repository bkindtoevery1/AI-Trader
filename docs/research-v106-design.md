# V106: PA Headroom-Log Learning

## Mechanism And Scope

V105 completed but failed. Its support-only learner increased nominations
while PA baseline fell to -$1,457.40 and combined stress stayed at -$1,179.
PA-only journal attribution shows that B and C share their first two baseline
losses, -$583.10 and -$558.10, on April 24. C then has 39 zero-capacity skips
among 45 PA attempts; B has 34 among 48. These histories end at different
dates. This does not isolate a causal contribution of any individual skip.

The new hypothesis changes the fitted objective, not the stop-support cutoff,
features, contract quantity or account rules. A conditional mean dollar target
does not penalize a large loss symmetrically with a large gain's effect on
remaining risk capital. Fit a concave headroom-log target on the exact V105
training population instead. No claim is made that this necessarily improves
PA survival, activity, or profitability.

[Kelly (1956)](https://onlinelibrary.wiley.com/doi/abs/10.1002/j.1538-7305.1956.tb03809.x)
motivates expected-log growth. [Busseti, Ryu and Boyd (2016)](https://web.stanford.edu/~boyd/papers/kelly.html)
separately constrain drawdown; log growth alone is not such a guarantee.
This experiment is neither their allocation optimizer nor Kelly sizing. Its
fixed reference headroom is a training proxy, not dynamic account wealth,
an IID-market assumption, a calibrated uncertainty bound or a ruin guarantee.

## One Target-Only Candidate

Keep the complete matured NQ event/label validation, stop <=140 support,
date-equal weights, training-only scaler, nine features, three chronological
folds, ten full-calendar purge sessions, and the original causal settings.
Reference H is $2,500, the unchanged initial Legacy50K trailing-distance
scale, fixed before new outcomes rather than fitted to this losing path.

For each of the four original guard-free unit-net-dollar labels U, learn
`H * log1p(U / H)`. Zero labels remain zero. Reject the whole study for a
nonfinite label or U <= -H; do not clip, delete, tune H, or change support.
Weights and the newly fitted scaler must reproduce the original V105 scaler
exactly. At most 12 native estimator fits and three scalers are admitted;
the 42 ordered fit stages and any technical abort remain durable.

Convert each forecast z to `H * expm1(z / H)`. These are reference-headroom
certainty-equivalent dollars, NOT expected PnL. Conversion preserves the
strictly-positive sign criterion in all four modes and is checked for finite
values. No certainty-equivalent value enters the operational V102 artifact
or wire. There is no grid, new threshold, forecast clipping, fallback or retry.

## Matched Accounts And Decision

Replay three own-state arms: unchanged V105 gate-only B, unchanged V105
support learner C, and the new log specialist D. All use untouched original
V102 Evaluation predictions; each switches only after its own next-date PA
start. All have the original 1 NQ limit, half-headroom allocation, actual-entry
nominal stop <=5*target guard, costs, latency, brackets and five-minute cooldown.
Do not remove risk-capacity checks or force trades to satisfy activity.

The 181 same-maturity raw pairs are scanned; all NQ four-mode unit labels and
original raw/window receipts are reverified. All 126 scoring dates remain
reused development, not new independent evidence. Require eight exact V105
control accounts and twelve unchanged Evaluation prefixes. There are twelve
account paths and 1,512 scheduled day slots, not independent observations.

D minus C isolates the loss-objective change. D minus B is the primary
economic benchmark: PA trading-PnL improvement must be positive in BOTH
baseline and combined stress, with no added hard/MAE breach and no earlier
inactivity closure. Cost-only and latency-only are diagnostic, not alternate
passing routes. A separate full-route gate still requires numeric Evaluation,
PA survival, modeled payout eligibility and no hard/MAE breach in both primary
modes. Relative benefit over a losing control is not absolute profitability.
The complete own-account calendar includes inactivity gaps and terminal tails.
Program fees remain unpriced; official compliance and actual payout are unverified.

## Admission And Evidence

Closed V105 status/lock/claim/seal, all 42 fit receipts, postrun audit and
dependency hashes bind the source. Restore all 126 C forecast envelopes before
new training, without invoking an old claim. Reuse V105's explicit original-HGB
byte/runtime readmission; do not recreate obsolete temporary runtime files or
weaken prior locks. Source populations and new transformed-target hashes are
bound before a new immutable claim. New outcomes stay hidden until all work
and postrun integrity checks complete and the result is exclusively sealed.

One new policy plus two contrasts reserves three charges: 13,172 to 13,175,
only when its new run claim exists. A technical abort retains its charge but
is not a profitability verdict. An existing claim prohibits every retry.
The 48 sealed historical holdout price/outcome dates stay closed. No new
Windows installation, source admission, Telegram message, order, operational
model replacement or verified50K success is authorized by this study.
