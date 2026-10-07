# V140 Matched Unit Target Execution

October 7, 2026. V140 now has an integrated source, label cache, training,
diagnostic, account-replay and supervised-result path. The frozen design and
V139 remain unchanged. This is outcome-informed historical development, not
independent validation. Complete software qualification is finished and five
comparisons were reserved before a single supervised market attempt started
at 2026-10-07T05:42:41Z. Effective trials are now 13,277. The attempt stopped
at 05:50:23Z with a technical source-order error before any raw labels, fits
or account replay. Both child and supervisor exited1; the failed attempt and
five charges are preserved. No economic result, strategy failure/pass or
Windows model start is inferred. See the [failure analysis](research-v140-failure.md).

## Source And Storage

The new source adapter restores the unchanged V139 envelope and authenticates
its sealed candidate forecasts and four candidate account books separately.
The original V134/V136 route supplies support and execution mechanics, not the
primary comparator. A read-only restoration verified 181 original dates,
5,485 events, 97 sealed evidence files, 45/87/129-date training prefixes and
126 scoring dates. It made no raw-tick scans or numerical model calls.

Each new label day must bind both explicit-contract products, every original
event including unsupported rows, old journals, complete normal/delayed windows,
source receipts and conservative maturity. New one-contract targets never
replace old provenance or guarded account outcomes. The training reader may
decode only its exact original prefix; diagnostics use the same new targets
for candidate, original V139 and training-only mean forecasts.

The storage adapter creates a new private directory exclusively. It publishes
181 canonical day files before their complete manifest, using the established
fsync/create-if-absent publisher. Reopening authenticates an externally pinned
manifest and all file hashes. Missing, extra, changed, linked, partial or failed
evidence blocks use. A failed directory is retained and cannot restart.

## Accounts And Audit

The account adapter uses four unchanged V136 GivebackAccount engines and the
exact four saved V139 candidate books. It checks every one of the 181 raw-pair
receipts before use, scores all 126 scheduled dates, and retains the original
nomination, sizing, commissions, adverse fills and lifecycle rules. Missing PA
exposure is null, not a zero-profit comparison or a relative win. The absolute
full-route and relative primary-mode economic gates are unchanged.

A production integration defect was found before market execution: ordinary
NumPy deepcopy turns immutable inputs writable. The adapter now validates the
original source first, then copies each array into independent immutable bytes
while detaching mutable metadata. Tests exercise the real source-memory checks
and require originally writable inputs to fail, not be silently repaired.

The supervisor checks qualification and requires a preexisting five-comparison
reservation before any new labels. One attempt must complete labels, six pipelines/36 native fits,
durable complete forecasts, same-target diagnostics and four new account books.
It keeps all 276 non-result payloads bound in a single final result seal, which
publishes accounts, diagnostics and status together. Failure preserves the
attempt, actual child exit and comparison charge without automatic retries.

The saved-result audit authenticates six serialized models, reconstructs their
prefix-only target bindings and training means, reproduces all 252 candidate
product/date forecasts and reconciles diagnostic/account summaries. It neither
refits nor relabels nor replays account tapes. This is reproducibility and
consistency evidence, not a new independent financial sample or raw first-touch
audit.

## Qualification Status

Focused orchestration tests passed 37 cases, storage tests passed 25, and the
account adapter passed 178. Real sklearn learners on invented source/cache
data passed the two-case integration test, including authenticated restoration
and a no-fit saved-result audit. The initial native integration failure was a
test isolation fixture blocking StandardScaler, not a market failure; only the
synthetic test's explicit numerical entry points were restored.

The combined affected regression passed 1,322 unique cases with zero failures,
errors or skips in 591.437 seconds. This includes 567 V140 and 755 predecessor
cases. Eleven warnings are retained V139 numerical-edge tests, not market fits.
The full-runner read-only preflight exited zero after 482.485 seconds, restoring
181 dates and 5,485 events without labels, fits or account execution. All 19
V140 source/test/design pins and 271 loaded source pins remained unchanged.
The original 16 V139 pins and 261 loaded predecessor pins also remained exact.

The separate static review found no concrete defect but did not claim to prove
production market execution or crash-time durability. The native integration
test exercises real learners and storage but substitutes its account result;
the 178-case replay suite separately exercises the unchanged account engines.

Qualification: `reports/nq_apex_v140_integration_qualification_20261007/qualification.json`,
SHA256 `4cb495af8c0ff820fe09fa72b4043e1cf28ee9a3b8d640f141dc8671f28523ea`.
Combined JUnit SHA256:
`db98a8540d65052a0b293990f72a3341ba71f5a00a00c2b94b5caed5a7899afa`.
Source preflight SHA256:
`cb2655528a2dd2de09e5b1a32dcd4dbc5cda11ed5cc1689fda98d0e034a9dc75`.
The earlier repository-wide run still has 13 unresolved case identities after
runtime attribution; no whole-repository-green claim is made.

## Next Step

Qualify the separate integrity-only envelope-order adapter without modifying
the original source pins or failed evidence. Its real-source preflight must
reach the previously missed snapshot check without extracting labels or
fitting. Any later market attempt needs explicit new output ownership and
qualification; the original attempt cannot restart. All48 sealed holdout dates
remain closed. V139's economic failure remains the latest complete verdict.

Windows model startup remains a separate integration task. The bounded catch-up
helper is implemented and tested but not installed or wired into a service.
No order, signal, schedule, login, spending or Windows configuration changed in
this implementation.
