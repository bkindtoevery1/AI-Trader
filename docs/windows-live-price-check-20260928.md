# Windows Live Price Check

The user confirmed that Windows and Codex were open. The desktop wait tool's
no-match error was not evidence that Windows was powered off: direct task reads
and the existing Windows-to-Mac metadata transfer continued to work.

## Verified Finding

Windows performed a read-only inspection at 2026-09-28 00:44:25 and 00:44:55 UTC
(09:44 KST). The verified physical V3 root contained only the known epoch. Its
durable sequence stayed at 43443 and it was terminal, with no successor in the
first inventory. The directory inventory was not repeated for the second sample.

The terminal timestamp is 2026-09-27 22:00:00 UTC (September 28, 07:00 KST).
The final complete record's hash matches the durable anchor. Its reason is
`unspecified_time_basis_unconfirmed`. The retained source maps this reason to
an Unspecified callback time whose interpretation has not been confirmed.
That mapping is a source-based inference; no tick record separately established
the actual callback Time.Kind in this diagnostic.

NinjaTrader and the known sender processes were present. No known model consumer
or publisher appeared in the process snapshot. Neither process presence nor the
earlier green connection indicator proves current price collection. The inspected
V3 pipeline must not be reported as receiving prices normally or generating signals.
Displayed NinjaTrader quotes were not inspected; this is not a login failure.

## Evidence And Limits

The 8555-byte Windows receipt is named
`windows-data.v102-live-prices-readonly.d631b055333c40e3a0b5251485aecfefccbe7b70aa0ec6065ca1651c4c6d290a.json`.
Mac verified a stable regular file, no symlink ancestry, exact whole-byte SHA,
strict UTF-8, no BOM, no duplicate JSON keys and no nonfinite constants.
The local review is
`reports/nq_v102_signal_activation_20260928/windows-live-price-audit-v1.json`.

Only 66396 native content bytes were read, within the existing 8 MiB bound.
This was a small diagnostic, not full-prefix hash-chain or source admission.
Current tick counts, last prices and actual tick growth remain unknown; zero
ticks in a terminal record must not be presented as zero ticks for the session.
The earlier incomplete and size-limited reports remain preserved.

No settings, source, login, schedule, order, Telegram message or restart changed.
The next repair must establish the native time basis and physical inputs first;
blindly setting the confirmation flag would conceal the unresolved assumption.
The user-only native diagnostic remains a separate pending input. Model research
on existing admitted Mac data does not depend on this live-source repair.
