# V139: Paired Minute Context Under The Fixed Giveback Route

Declared October 7, 2026 before new paired-context extraction or market fits.
Outcome-informed development, not independent validation or an approved signal.

## Reason And Precedents

V138 rejected every executable query under the all-four-positive rule; direct
utility forecasts also lost to the state-only mean anchor. More activity alone
is not a solution: V117 baseline-only nomination and V137 cash-only allocation
already failed their complete economic routes. Preserve these failures.

This study returns explicitly to V134 own-product cash forecasts and the V136
fixed giveback route. Its sole change is a fixed paired information bundle for
BOTH NQ and MNQ heads. It is not a V138 threshold relaxation or a new claim that
V136 passed. V136 failed the full route and never entered PA under combined
stress. Its cash labels retain the original exit, not the giveback exit: both
comparison arms share that known mismatch. Scores are entry rankings, not
calibrated giveback expected profits.

Paired information is not new to this research. V41 learned an opening
one-second lead/lag orientation; V52 tested zero-fit opening basis convergence;
V114/V115 used signed Last gap, Last age and print-count ratio in the preceding
minute; V120/V121 used tick-sign quantity pressure. V116 stacked forecast
scores. V123 used NQ local minute-volume shape and V134 prior opportunity
history. This increment is specifically a 21-minute centered-basis dispersion
and contract-size-equivalent relative-volume bundle, not the first paired model.

## Frozen Information

Preserve the exact fifteen V134 input floats, including the original NQ anchor,
local volume and prior broad-opportunity history. For each decision D, append
three features from the same explicit quarterly NQ/MNQ maturity and exactly the
21 contiguous completed one-minute intervals ending at D. Each minute uses its
recorded Last OHLC and traded contract quantity. Define b[i] as NQ close ticks
minus MNQ close ticks, m as the arithmetic mean of the 21 b values, s as the
unchanged event side (+1 long, -1 short), and stop as the original stop in ticks:

1. s * (b[last] - m) / stop.
2. mean(abs(b[i] - m)) / stop, unsigned.
3. Recent five-minute share minus full 21-minute share, where each share is
   sum(MNQ quantity) / (10 * sum(NQ quantity) + sum(MNQ quantity)).

The share is a ratio of sums, not a mean of minute ratios. The tenfold multiplier
normalizes contract-size exposure, not signed flow, quote liquidity or actual
dollar notional at differing prices. Differences and ratios use integer/Fraction
arithmetic until one finite float conversion. No clipping or winsorization.

Require complete native clocks, exact same-maturity symbols, consistent OHLC,
and integral nonnegative quantities below 2**53. Missing/duplicate/misaligned
bars or malformed records abort the readiness/run; never drop an opportunity.
Zero-quantity minutes keep their supplied source prices and contribute zero
quantity, with their counts recorded. Do not synthesize or forward-fill prices.
Each product must have positive total 21-minute quantity; the combined last-five
denominator must be positive, otherwise the feature is undefined and aborts.
Recorded zero-quantity closes may be stale; they are not asserted to be fresh
trades. No last-print age, quote synchronization or arbitrage guarantee is inferred.

The join reads clocks before payloads outside each decision's window. No
postdecision price/volume, scoring label, account state or fill enters context.
The current completed minute can enter its own backward mean without leakage.
Keep all original events and empty dates. NQ rows must match the original anchor
and local-volume receipt; the first fifteen feature bits must remain identical
to the exact V134 context. Feature hashes bind supplied bytes, not provenance,
calendar completeness or live arrival; the authenticated source adapter owns
those duties.

## Fixed Experiment

Use exact V129 own-product one-contract net-cent labels, date-equal weights,
NQ original support and MNQ original <=140-tick support. Preserve all losses,
zeros, unsupported-event history and the complete original query masks.
Use V134's HGB recipe: squared error, 100 iterations, learning rate .05,
seven leaves, minimum 50 rows per leaf, L2=10, no early stopping, seed126.
Only training prefixes fit the weighted X/Y scalers; estimator weights have
mean one. Six product/fold pipelines mean 24 response fits plus 12 scaler fits.
No grid, genetic algorithm, seed search or scoring-dependent fit.

Retain the 181-date original development calendar through 2026-06-12,
45/87/129-date mature training prefixes, ten-session purges and three 42-date
scored blocks. Keep every one of the 126 scored dates. All 48 sealed dates
remain closed. Controls are exact saved V134 forecasts and V136 account books,
not refitted or replayed alternatives chosen after seeing the new result.

The intended end-to-end evaluation comprises complete predictions followed by
four new fixed V136 giveback account books and four saved controls. Preserve
all-four-positive nomination, long/short support, integer NQ/MNQ quantities,
stops, sizing, headroom, fees, slippage and the whole Evaluation-to-PA lifecycle.
The purpose is economic evaluation, not declaring success from lower MSE.

Plan five counted comparisons: the two product forecast candidates, their two
fixed forecast contrasts, and one whole-account paired route comparison.
These are planned, NOT yet reserved: effective trials remain 13,267. Before any
new market feature extraction/fitting, complete source/runner qualification,
publish the design and freeze a five-comparison reservation (13,267 to 13,272).
No market execution is authorized merely by this design or component tests.
Do not alter the frozen spec after results. Record every native fit attempt
and warning; use one supervised attempt and an authenticated no-fit saved-result
audit. Save all forecasts before scoring; publish outcomes only after complete
forecast and account results, with actual terminal exits and immutable bindings.

Report all products, modes and folds: date-equal MSE/MAE, nominations, executed
trades, trading and separately priced program costs, Evaluation pass, PA
survival, breach/inactivity and payout conditions. Forecast scores or overlapping
labels are not executed PnL. Apply the unchanged V136 full-route gate absolutely.
Compare PA PnL only when both arms reached PA; otherwise report null with
PA_NOT_REACHED rather than substituting zero. A missing relative PA contrast
does not become a relative win. No favorable mode substitutes for failed stress.
Any bundled benefit cannot be attributed to one coordinate or information alone:
adding features also increases available split choices at the same tree budget.

No new Windows install, operational V63/V92 change, schedule, Telegram message,
order, spending, provider admission or holdout opening belongs to this study.

## Primary Sources And Limits

CME specifies NQ at $20 per index point and MNQ at $2, both with 0.25-point
minimum ticks. These contract sizes motivate the fixed tenfold quantity ratio,
not an asserted predictive edge. See the official
[NQ specification](https://www.cmegroup.com/markets/equities/nasdaq/e-mini-nasdaq-100.contractSpecs.html)
and [MNQ specification](https://www.cmegroup.com/markets/equities/nasdaq/micro-e-mini-nasdaq-100.contractSpecs.html).

Hayashi and Yoshida (2005), *On covariance estimation of non-synchronously
observed diffusion processes*, Bernoulli 11(2), 359-379,
[author-hosted paper](https://www.ms.u-tokyo.ac.jp/~nakahiro/mypapers_for_personal_use/hayyos03.pdf),
explains why nonsynchronous observations require care. V139 does not implement
their estimator or inherit its guarantees. Minute-close basis can reflect
asynchrony or stale Last prices rather than an executable economic discrepancy.
