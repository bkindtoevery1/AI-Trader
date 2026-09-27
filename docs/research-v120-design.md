# V120: Does Trade Size Add To Tick-Direction Information?

Declared 2026-09-27 before V120 source extraction, fitting or account replay.
This is an outcome-informed development design, not a market claim or a pass.
V119 is closed: small quantities occasionally recovered entries, but 2,195 of
2,200 PA decisions stayed flat, and all four PA books closed inactive. More
activity alone is not the objective; baseline and stressed economics must improve.

## Distinct Question

V79 tested opening minute-volume removal/seasonality. V88/V92 already contain
relative minute volume. V99 added five-minute price efficiency; V111 tested
21-bar OHLC ordering. V114 added paired Last price gap, age and print counts,
explicitly not volume or signed flow; V115 used those same paired features.
None of those documented treatments compares equal-print and trade-size-weighted
tick-direction pressure at the original decision. This is a bounded precedent
review, not a claim that no earlier financial research used the technique.

Test whether source-reported trade sizes add information beyond price-change
signs from the same predecision prints. The two new arms add two coordinates
(NQ and MNQ) to the original nine V118 features. One weights every print equally;
the other weights by its actual positive integer volume. Both retain the same
events and learner capacity. A gain over V119 alone cannot identify a trade-size
effect; the volume arm must also beat the equal-print arm.

## Fixed Representation

For every original NQ event at D, use its same-expiry NQ/MNQ raw records in
[D-60 seconds, D), including the left boundary and excluding every print at D.
Keep original sequence order, including equal timestamps. Missing product data
aborts admission; do not delete the event or impute volume. Aggregate the original
four-field records (sequence, UTC nanoseconds, integer price ticks, volume).
The older execution TickWindow omits volume and must not supply fabricated ones.

Reset inferred direction to zero at the beginning of each minute. Its first
print and subsequent unchanged-price prints remain unclassified until the first
nonzero price change. A positive/negative change sets direction to +1/-1; an
unchanged price then carries the last nonzero direction within this minute only.
No earlier-minute seed, later tick, quote proxy or future correction is used.

For each product, equal-print pressure is sum(direction)/number_of_prints.
Volume pressure is sum(direction*volume)/sum(volume). Unknown prints contribute
zero numerator but stay in both denominators. Multiply both by the original
event direction. All integer arithmetic precedes the final ratio; normalize
signed zero. A constant-price minute legitimately gives zero, unlike absent data.
Record positive/negative/unknown counts and volumes, ordered-prefix hashes and
timestamp/sequence bounds so later audits can reproduce both alternatives.

These are minute-level features derived from ticks, not an n-tick-bar strategy.
Last prices do not identify the actual aggressor. This bounded, reset variant
is not the complete Lee-Ready quote algorithm. Historical event timestamps do
not prove that all prints arrived before a live decision. No synthetic bid/ask
or exchange-certified order-flow interpretation is allowed.

## Fixed Learning And Decision Plan

Use the V118 joint empirical four-mode one-MNQ outcome forest: same 64 trees,
squared-error splits, depth 2, at most four leaves, minimum 100 events and five
distinct training dates per leaf, no bootstrap, max_features 3, seed 202609118,
one thread, and equal total mass per nonempty training date. Input width becomes
11 for both arms, not a feature/seed/parameter search. Fit six forests total,
two per original 45/87/129-date training prefix. Preserve the ten-session calendar
purge, mature original labels, original stop/capacity population and 42 scored
dates per fold. No standardization or extra transform is fitted.

Both candidates use the unchanged V119 integer-quantity choice, including flat,
strictly positive worst-four-mode certainty equivalent, and their own current
headroom. Preserve the original NQ Evaluation and MNQ PA routing, NQ <= 1 and
MNQ <= 6 in this study, actual-entry guard, costs, delays, stops, uncapped daily
fills, cooldown, trailing/MAE/activity and payout rules. The user's wider maximum
remains a ceiling, not a reason to change this isolated feature comparison.

Retain exact V119 and original all-head controls: eight existing account books.
Two new arms create eight new books across all 126 scored dates. Scan the same
181 admitted pairs; all 48 sealed holdout dates remain closed. Primary contrasts
are volume-minus-equal-print and volume-minus-V119. Both must strictly improve
PA trading PnL in baseline AND combined stress, without added hard/MAE violations
or earlier inactivity. Absolute PA profit, survival, payout and full-route gates
remain separate. Do not pick the equal-print arm as an uncharged rescue result.

Two new policies and two primary contrasts budget four comparison charges,
13,209 to 13,213, only upon a genuine later exclusive market claim. No charge,
fit or economic verdict follows from implementing or admitting input features.
Source admission, the 11-input learner/export, causal plan bindings, complete
account runner, regression qualification and immutable claim are all required
before fitting. This component stage does not yet supply that full pipeline.

No partial economics, optional stopping, rescue threshold changes, model refit
after outcomes, sealed-holdout access or independent-validation claim. Program
fees and the personal account cohort remain unverified. Existing Mac data are
enough; Windows deployment, live orders, secrets and schedules are outside this
study. The fixed operational models remain unchanged.

## Primary Sources

[Lee and Ready (1991), Inferring Trade Direction from Intraday Data](https://onlinelibrary.wiley.com/doi/full/10.1111/j.1540-6261.1991.tb02683.x)
describes price-change-based classification and its limitations. It does not
establish this NQ/MNQ feature's accuracy or trading profitability.

[NinjaTrader historical import formats](https://ninjatrader.com/support/helpguides/nt8/importing.htm)
distinguishes price-and-volume Last ticks from the separate bid/ask-enriched
format. The existing admitted Parquet source carries volume; this does not
certify its upstream completeness or turn Last-only ticks into aggressor labels.
