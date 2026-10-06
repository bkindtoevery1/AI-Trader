# V138 Component Qualification

Record date: October 7, 2026 KST / October 6 UTC.
Stage: COMPONENTS_QUALIFIED_NOT_MARKET_FITTED.
Economic verdict: NOT_EVALUATED. Market-run authorization: NOT_GRANTED.
See the [unreserved design](research-v138-design.md) and the completed
[V137 failure record](research-v137-performance-audit.md#completed-market-run).

## What Changed

The learner directly predicts four fixed `2*cash-floor` scores instead of
combining eight separately fitted response heads. The objective, input features,
state replicas, train-only weights, purged folds, support and execution costs
are unchanged. This is an estimation comparison, not continuation value or a
claim of new market information. The state-only arithmetic anchor separates
market-feature value from known account-state mechanics.

The own-account dispatcher accepts and journals four actual scores. It keeps
the frozen daily execution/rollback bytecode in a private namespace, without
changing the predecessor or fabricating cash/floor predictions. Busy periods,
day stops, zero-capacity bypass, risk sizing, fees, latency, giveback exits and
Evaluation-to-PA routing remain unchanged. All four scores must be positive.

The forecast protocol publishes 252 product/fold/date records and then a
complete manifest. It authenticates and recomputes the entire prediction census
before opening the first scoring-label payload. Even corruption in the last
record prevents any scoring-label read. Empty dates retain null loss, not zero
loss. The state-only reference is diagnostic, not an interpolated account policy.

The source adapter rejects duplicate/out-of-order prefix reads before decoding,
permits exactly one authenticated scoring-day read per request, checks the full
six-model census and all model hashes before deserialization, and rejects
symlinks, path traversal and root escapes. Original V137 bytes remain unchanged.

## Verified Evidence

| Layer | Observed Result |
| --- | --- |
| Revised actual source-only preflight | Exit 0 at 21:36:12 UTC; 181 dates, 5,485 original events, six model records; no fitting, deserialization, raw-label generation or account replay. |
| Native synthetic training/forecast integration | 22 passed; six direct pipelines / 36 native fits on invented data; saved forecast audit performs no additional fits. |
| V137/V138 transition regression | Actual exit 0; 2,264 passed in 607.14 seconds. |
| Supplemental empty/exposure cases | Actual exit 0; six passed in 21.05 seconds. |
| Unique qualification scope | 2,270 distinct case identities: 541 V138 and 1,729 V137. Integration and agent-reported subsets are not added again. |
| Predecessor source preservation | All 257 frozen source pins verified; both V137 reservations and total 13,262 unchanged. |
| Whole repository regression | NOT_RERUN for this component checkpoint; the prior broad suite remains not green with its disclosed historical/schema failures. |
| V138 market training, whole-account replay, result audit | NOT_RUN. |

The supplemental cases cover an entirely empty 252-record scoring census with
actual temporary-file publication/readback, null per-state losses, unequal PA
exposure, both signs of the relative-benefit comparison and cross-book identity
conflicts. Synthetic positive gate cases test arithmetic only; they are not a
successful strategy, actual account or payout.

Private evidence is retained under
`reports/nq_apex_v138_component_qualification_20261007/`:

- `qualification.json`: SHA256
  `740bc1c7ad6884cae9f5b6f783b76cc4ad85179a36143339ec77ab9de5e24ea6`.
- `source-preflight.json`: SHA256
  `8e7f143aec33774d2f4c078d60425e838d873d0cb97cb53ffb705bd5b1f47fb9`.
- `transition-regression.xml`: SHA256
  `3c1411bdd7df7064f4a8757aacf6f19f09531b7580359fd12ff541c585022dc7`.
- `edge-regression-v2.xml`: SHA256
  `7809ffbe550bd57a838e7792d256b0275e5caa4145c19e626e6a1d431a6ac709`.

The qualification record binds the exact component/test/design bytes. It is
not the still-unfinished market execution lock. Raw data, models and detailed
local evidence are not included in the public documentation snapshot.

## Corrections And Limits

An initial integration fixture addressed the predecessor's production output
instead of the pytest temporary output. The I/O guard rejected it before a
market-artifact read. The fixture was corrected; it did not create a market
fit or consume a new trial.

The initial test also incorrectly expected no sklearn warnings. Weighted
constant columns in the invented data produce tiny negative roundoff variances
and a square-root warning before sklearn's constant-feature mask applies unit
scaling. The revised test requires all warnings to match the retained native-fit
journal, finite scaler state, positive scale and unit scale for negative
roundoff variance. No warning was suppressed and no learner recipe changed.
The standalone integration retained six warnings, including its reused V137
synthetic setup; the combined regression retained nine. Prediction checks remain
finite. This does not waive a future market-run numerical defect.

A separate read-only review found no concrete component bug and identified
the empty-fold and unequal-PA-exposure gaps covered by the supplemental tests.
Neither software tests nor internal review provide independent trading evidence.

## Next Required Work

Complete the raw-tick four-book replay driver and saved own-state query audit,
then the immutable native-fit journal/supervisor, dependency lock and publication.
Reserve the five planned comparisons before any market fit. Run the complete
forecast and account assessment once, regardless of the forecast-loss result,
and verify the terminal saved result before releasing economics. No retry,
threshold rescue, selected cash-only fallback or sealed-date access is allowed.

The full research/Windows goal remains active and incomplete. The existing daily
Mac backup is verified, but current live collection and model signals remain
unverified. Previously cancelled Windows UI work was not resumed. No orders,
credentials, spending, Windows settings or schedules changed in this work.
