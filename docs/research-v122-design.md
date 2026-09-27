# V122: Quarter-Stop Pullback Market Entry

Design date: 2026-09-28. Partial implementation only: a pure trigger and
modeled-entry-clock core with invented unit tests. No market labels, fits,
inference, account replay, trial reservation, outcome or deployment exists.
Frozen predecessors remain unchanged. This document fixes one proposed policy,
not an authorization to start a market experiment.

## Distinct Question

V121 rejected every supported PA decision; its retained CE diagnostic identifies
cost_only as the uniquely limiting head at the best positive quantity. That does
not distinguish negative conditional mean from a downside-risk penalty or prove
that costs should be reduced. V85's pullback was a completed-bar signal followed
by a fixed delay, not a pending post-decision price trigger. Reviewed V105-121
designs preserve that fixed entry-clock family. This bounded precedent review
does not claim universal novelty.

Test whether a price-triggered MARKET entry changes the execution payoff enough
to improve unchanged cost-sensitive decisions. There is no resting limit order,
queue position, maker discount, threshold-price fill or guaranteed improvement.
Actual delayed modeled fills may be worse than both the trigger and reference.

[Nevmyvaka, Feng and Kearns (ICML 2006)](https://www.cis.upenn.edu/~mkearns/papers/rlexec.pdf)
study execution as a distinct learning problem using millisecond limit-order data.
V122 is not a replication, RL method or order-book fill proof; its quarter-stop,
five-minute Last-market proxy constants are our hypothesis, not paper-backed optima.

## Fixed Mechanics

Keep original source events, externally selected direction s in {-1,+1},
explicit same-maturity NQ/MNQ contracts and completed decision time D. The NQ
anchor supplies its unchanged ATR stop S and immutable mean target. Use the last
MNQ Last print in [D-60 seconds,D), preserving original sequence for timestamp
ties, as P0. Missing reference evidence aborts, never changes event membership.

Set delta=ceil(S/4) integer quarter-point ticks and level=P0-s*delta. Search the
original ordered MNQ tape for the FIRST print satisfying s*(price-P0)<=-delta
in [D,D+300 seconds). The right boundary is excluded. Earlier reference prints
are not triggers. No later better price can replace the first qualifying print.
Five minutes bounds staleness; a quarter stop scales the threshold to the known
risk unit. These are preregistered engineering constants, not optimized values.

No trigger resolves at D+300 seconds with no position or trading costs. Once a
trigger occurs at tau, its expiry no longer cancels its scheduled market entry:
baseline/cost_only use tau+60 seconds; latency_only/stress use tau+240 seconds.
Take the globally first Last at or after that due time, strictly before due+60
seconds. A missing timely tick is an evidence error. Use unchanged adverse
slippage of 1 tick or 4 ticks for cost stress, in the trade direction. Never fill
at the threshold or trigger print. The absolute exit remains D+5460 seconds;
delaying entry does not extend it. Long and short mechanics are exact mirrors.

Later execution retains the actual slipped-entry stop, original immutable mean
target, positive-net geometry/PA nominal guard, unchanged per-side commissions,
adverse exit fills and first-crossing trailing/MAE/DLL precedence. The core
does not execute those exits, apply guards, choose quantity, calculate PnL or
construct training labels. Its absolute-exit index is evidence for a later
adapter, not a claim that the eventual trade exits at that tick.

## Pure API And Evidence

`prepare_intent(anchor, reference_window, source_symbol=..., signal=...)` freezes
the supplied original selection and strict pre-D reference. It neither selects
features nor consumes future price payloads. The caller owns authenticating the
NQ anchor, MNQ reference time index, original event identity and causal selection.
The returned TriggerIntent and nested anchor/reference values are immutable.

`resolve_entry(intent, tape, mode=..., coverage=...)` requires an original MNQ
TickWindow spanning the reference minute through the absolute exit, with native
integer ticks and contiguous sequences. Indices in its result are zero-based
within this supplied tape, not provider-global indices; sequences are original.
The coverage dictionary has exactly trade_date, symbol, start_ns, end_ns,
tape_sha256 and admission_receipt_sha256. Its bounds must equal the supplied
tape bounds and its hash must equal tape_sha256(tape). The caller must first
authenticate the referenced external admission/coverage evidence. This core
checks only content/boundary consistency, not the existence or truth of that
external receipt. Hashes and consecutive sequences do not prove complete feed
coverage, absent missing timestamps, live arrival or broker execution. Full-tape
admission must establish that selected entry/exit prints are globally first.

The resolver revalidates native tape structure and the frozen reference, rejects
missing trigger-window or timely entry/exit evidence, and requires known policy
and mode values. There are no tunable thresholds, delays or costs. Positive
integer prices are quarter-point tick counts, not floating dollar prices.
Do not label absent/rejected coverage as a zero payoff or genuine expiry.
No interprint-gap threshold can certify continuity of an externally incomplete
feed; that remains an explicit caller-owned admission limitation.

Results distinguish EXPIRED_NO_TRIGGER from TRIGGERED_MARKET_ENTRY. A modeled
entry is not a broker fill. Receipts bind the intent, caller coverage claim,
trigger and entry clocks/sequences/indices, adverse slippage and fixed deadline.
They contain no PnL, contracts, performance metrics or production approval.

## Proposed Labels And Model

Future separately authorized work must label every original eligible training
event under this complete fixed attempt policy in all four modes. Use exact
one-MNQ net cents, including genuine expiry and geometry/cost skips as zero.
Do not condition training membership on triggering, filling or winning. Keep
V118's guard-free unit-label convention otherwise; actual account trailing/MAE,
nominal PA guard and lifecycle remain downstream. This residual account-target
mismatch is disclosed, not silently fixed as a second treatment.

Use the original nine features and date-equal weights; preserve the V118 initial
MNQ-capacity training population and stop<=140 filter, and its scoring support
requiring stop<=140, positive initial NQ reference capacity and a non-null original
MNQ forecast. No support or event selection may depend on a future trigger.
Retain the fixed V118 empirical forest: 64 trees, depth 2,
max_leaf_nodes 4, min_samples_leaf 100, at least five dates per leaf,
max_features 3, no bootstrap, seed 202609118 and one thread. Three chronological
fits, no scaler, classifier, pressure-feature alternative or parameter search.
At D apply unchanged V119 integer quantity/strict positive worst-four-mode CE
selection to the new conditional attempt-outcome distribution. No trigger or
entry observation may leak into these pre-D features or quantity decisions.

## Causality And Pending Occupation

Use the existing 181 admitted pairs with 45/87/129-date training prefixes,
10-session purges and three 42-date scored blocks. Every new label in every mode
must resolve strictly before its purge cutoff. Historical development is reused,
not independent validation. Keep all 48 sealed holdout dates closed.

Evaluation remains original NQ; only PA MNQ changes. A positive nomination
occupies the account from D until expiry, entry rejection or completed exit.
Skip intervening events; never retroactively recover them. Apply the existing
300-second cooldown after every attempt resolution, including expiry. Positive-
capacity model abstention remains immediate and reads no future trigger tape;
zero capacity retains original skip/cooldown semantics, not new pending time.
At market release recheck eligibility and chosen quantity; cancel rather than
resize, increase or reselect. Retain sizing caps, fees, safety gates, activity,
payout and continuous account state. This core does not implement that adapter.

One new candidate plus one primary contrast against retained V119 proposes TWO
comparison charges, not reserved or charged. Planned work is three forest fits
(192 trees), four new account books and exact retained controls. Comparing this
combined entry/learning intervention does not isolate estimator superiority.
Unchanged Evaluation timing also means existing PA experience is late-vintage,
not three independent PA replications. No new claims follow from unit tests.

## Failure And Remaining Work

Adding zero expiries alone cannot reverse a nonpositive CE: the exponential
moment becomes (1-p)+p*M and remains >=1 when M>=1. The triggered outcomes must
actually improve. Delays can erase price improvement, adverse selection can
worsen losses and waiting can accelerate inactivity. More activity is no pass.

Before any market claim: implement authenticated first-trigger/entry readers,
complete four-mode labels and maturity/schema bindings; add the pending account
adapter and its rollback/clock tests; bind the unchanged learner and CE selector
to new labels; preserve complete conditional masses for mean/risk attribution;
then qualify a separately frozen full runner with immutable complete evidence.
Focused synthetic tests are owned here; the parent runs full regressions only
after all components are finalized. No frozen label/clock lock may be weakened
or a new target disguised as an old V118 target.

Any eventual result must report trigger/expiry/admission reasons, delayed fill
prices, pending-time skips and PA terminal causes. Negative cost-head CE, erased
price improvement, worse inactivity, or failure of unchanged absolute PA profit,
risk, survival and payout gates is failure evidence, not reason to tune this
attempt. No partial outcome selection, alternate favorable mode or forced-trade
quota. Last-only market fills still omit verified spreads/liquidity; this design
removes passive-queue assumptions, not all execution uncertainty.
