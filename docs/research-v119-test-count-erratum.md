# V119 Test-Census Documentation Erratum

Recorded 2026-09-27 before any V119 market outcome was opened.

The preceding status/publication note incorrectly described the difference
between the JUnit suite header and concrete test cases as repeated case IDs.
That explanation was inferred, not measured, and is withdrawn.

Direct XML inspection establishes:

| Evidence | Header Declares | Actual Test Cases | Unique Case IDs | Duplicate IDs |
| --- | ---: | ---: | ---: | ---: |
| V118 full regression | 19494 | 19405 | 19405 | 0 |
| V119 full regression | 19781 | 19692 | 19692 | 0 |

Both suite headers exceed the concrete case census by89. The reason for the
inherited header discrepancy has not been established here. It is not evidence
of extra executions or duplicated case IDs. The qualification parser requires
unique actual case IDs and retained predecessor/focused membership; it does not
use the inflated header as proof of coverage.

The measured V119 verdict stays19689 actual passes,2failures and1skip, exit1.
No source, test, XML, qualification receipt, market policy or trial count changes.
The earlier public statement remains visible in commit `ebe6d8b`; this additive
erratum corrects its explanation, not its measured pass/failure census.
