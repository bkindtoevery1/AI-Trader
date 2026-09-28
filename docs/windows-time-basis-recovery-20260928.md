# Native Time-Basis Recovery

At 2026-09-28 01:12:03 and 01:12:38 UTC the Windows agent observed the existing
NQ December chart's last-price label change across 34.712 seconds. This verifies
display movement, not event timestamps, MNQ reception, collector recovery or a
model signal. Mac authenticated the 7936-byte metadata receipt
`windows-data.v3-time-basis-readonly.40c3ea6da9569488196ebf7fb3bb6927c4afca0250975ca019fef9575d8b03ac.json`
as stable regular bytes with exact hash and strict JSON. No screenshots, full
logs, source bodies, accounts or secrets were included.

Windows reports Korea Standard Time. The verified terminal epoch also recorded
Korea Standard Time and confirmation=false. Current native options/provider
remain unverified: an overlapping idle prior-volume window obscured the menus.
Only existing chart/Control Center windows were activated. No settings, login,
compile, restart, order, Telegram or schedule changes occurred.

## Specific Missing Evidence

The exact retained V3 source SHA is
`cf07ffadcdcc6282fed0e499559f987392d9c4d7671e3fbd26b7bc447a702eb5`.
Its timestamp check occurs before the tick is queued. Rejected callbacks preserve
the failure reason, but not the raw callback wall-clock Time or directly observed
Kind. Successful ticks retain normalized time/receive time/Kind, not raw Time.
Repeating the same terminal read cannot reveal the missing raw value.

The official [MarketDataEventArgs reference](https://ninjatrader.com/support/helpGuides/nt8/marketdataeventargs.htm)
describes Time as a DateTime, without establishing this provider's Kind/timezone.
The [application timezone reference](https://ninjatrader.com/es/support/helpGuides/nt8/application_timezoneinfo.htm)
describes the configured application timezone, not proof of raw callback semantics.
Neither the matching timezone names nor a moving chart authorizes setting the
confirmation flag. Display-capture UTC must not be substituted for event time.

The missing step is a bounded native observation of raw callback Time, Kind,
receipt UTC, configured timezone/rules and the instrument's actual provider.
A diagnostic must keep unconfirmed values separate from normalized model input,
retain original values and not silently use arrival time as exchange time. The
existing user-only physical-path diagnostic is a separate pending prerequisite.
No new diagnostic has been installed, compiled or activated in this turn.

## Same-Instance Recovery

The source's PollLocked path can recover without a full NinjaTrader restart only
after safe owner retirement. A fault latches; editing confirmation while enabled
does not clear it. Valid disabled settings must first be observed with no owner,
then corrected enabled settings may clear the latch and start a fresh epoch.
Missing/malformed settings are not that acknowledgment. Unproven retirement
continues to hold the producer lock and must not be bypassed.

The source matches the retained installed-source pin. Its existing static test
module passed all 42 cases on Mac, actual exit0. The existing C# harness includes
`unknown_time_basis_requires_correction`, including refusal of an enabled-only
flag edit. The harness was inspected, not executed natively in this turn. Static
tests are not proof of current loaded assembly, safe retirement or recovery.

After genuine time-basis evidence: review current physical settings and source
binding, preserve the old terminal epoch, use the observed disable/correct/enable
path if native retirement is proven, then verify fresh NQ and MNQ callbacks and
completed-minute input. Only afterward may normal source/context admission and
the unchanged model consumer start. A fresh heartbeat alone is insufficient.
