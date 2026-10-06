# Longer Minute Training: Bounded Feasibility Review

October 6, 2026. **Feasible as a distinct supervision/history comparison,
not novel merely because it uses older minutes. No experiment run or reserved
by this review.**

## Scope

Read existing research documentation, configuration, loader/source contracts,
SQLite `snapshots` metadata through June 12, 2026, and 518 pre-September 8, 2025
minute manifests. SQLite was opened with `sqlite3 -readonly`; no `bars` rows
were queried. No raw/normalized price payload, report/output directory, V130
outcome or holdout content was inspected. No imports/runners, fits, new candidate
metrics, replay, tests, code/pin/dependency changes, Windows interaction, orders,
schedules, commits or publication. This document is the only write.

Counts below are metadata reconciliation against existing admission evidence,
not a fresh full-grid, OHLCV, payload-hash or independent-provider audit.
Repository-relative evidence paths below are rooted at
`/Users/bkindtoevery1/workspace/AI-Trader`.

## Prior Versions

| Precedent | What was already tried; what differs |
| --- | --- |
| Multiresolution V3/V4 | Configured a 617-session long-minute track; V4 explicitly learns same-session entry-open to exit-open points. Terminal-return supervision is therefore not a new general idea. These configurations do not establish the proposed close-to-close/126-date experiment. See `config/nq-apex-multiresolution-research-v3.yaml` and `-v4.yaml`. |
| V63, V75, V76, V77 | Already use the older minute cohort, not only the raw year. V76 has 617 source dates, 597 after 20-session warmup, and 305/378/451/524 training dates; it includes a sign-probability/constant-conditional-payoff model. V77 trains opening TCN/GRU representations on the longer history. These use the older minute action-label/account framework, not the present 126-date intraday tick test. |
| V78 | Replays the already longer-minute-trained V63/V77 signals on all 181 explicit raw pairs, without new fits. This establishes the broad train-on-minutes/evaluate-on-ticks path. |
| V80 | Strong direct precedent: 617 minute sessions, four long chronological fits, approximate minute stopped-payoff labels, then actual ordered-tick evaluation on all 181 pairs. The three new payoff recipes failed the documented objective. |
| V81 | Most explicit history-expansion precedent: extends V57's unnecessarily 181-date-restricted minute training to the older cohort. After 60-session warmup, 557 dates and 265/338/411/484 training prefixes; exact tick evaluation remains on 181 pairs. The learned wick policies did not establish a pass. |
| V82-V84 | Continue the older-minute training/raw-tick evaluation path. V84 specifically realigns approximate minute payoff labels to changed stops. More history and label alignment alone did not establish the objective. |
| V89 / V129 | Not older-minute outcome training. V89 learns actual tick-derived target-hit/conditional-payoff labels from raw training dates; its 617-date calendar supplies purge/context, not pre-raw tick labels. V129 uses own-product tick net-cent labels on 45/87/129-date prefixes. Its completed forecast-only result does not establish better selection or an account verdict. |

Evidence: `docs/research-v76.md`, `research-v77.md`, `research-v78.md`,
`research-v80.md` through `research-v84.md`, `research-v89-design.md`,
`research-v89.md`, `research-v129-design.md`, `research-v129-results.md`;
`config/nq-apex-multiresolution-research-v63.yaml` and
`config/nq-apex-regime-research-v76.json`.

**No exact fixed close-to-close target + matched long/recent training arms +
current 126-date tick-scoring experiment was identified in this bounded review.**
That is not an exhaustive novelty claim. V80/V81 already answer whether the
broad longer-minute path has been attempted: yes.

## Usable Older Sessions

The declared development split is September 5, 2023 through June 12, 2026;
raw history starts September 8, 2025. The roughly three-year inventory includes
excluded embargo/holdout dates and is not three years of permissible training
in every fold. Authority: `config/nq-apex-multiresolution-research-v2.yaml`,
`docs/data-inventory-20261006.md`.

Pre-raw metadata contains **518 paired dates; 436 have 1,380 minutes per product,
82 do not**. The 436 contribute 601,680 bars per product, 1,203,360 combined.
They have unique session dates and the expected 23-hour first/last-end span.
Together with the 181 complete raw-overlap dates, this reconciles the documented
617 admitted complete development sessions. No incomplete date is silently
filled or admitted because its RTH window might suffice.

| Explicit NQ/MNQ maturity | Complete paired dates | Incomplete dates | First / Last complete date |
| --- | ---: | ---: | --- |
| U23 | 4 | 0 | 2023-09-05 / 2023-09-08 |
| Z23 | 58 | 7 | 2023-09-11 / 2023-12-08 |
| H24 | 55 | 8 | 2023-12-12 / 2024-03-08 |
| M24 | 56 | 13 | 2024-03-11 / 2024-06-14 |
| U24 | 46 | 19 | 2024-06-18 / 2024-09-12 |
| Z24 | 55 | 10 | 2024-09-17 / 2024-12-13 |
| H25 | 52 | 11 | 2024-12-18 / 2025-03-14 |
| M25 | 59 | 5 | 2025-03-17 / 2025-06-13 |
| U25 | 51 | 9 | 2025-06-17 / 2025-09-05 |

Ranges are bounds, not assertions that every weekday inside is complete.
The exact older metadata set is `snapshots` with
`last_interval_end_utc >= '2023-09-05' AND last_interval_end_utc < '2025-09-08'
AND observations = 2760`, reconciled to manifests with both product counts
equal to 1,380. Its ordered LF-terminated, pipe-delimited vector of
`session_date|snapshot_id|manifest_sha256|normalized_sha256|batch_identity`
(ordered by last interval end, then snapshot ID) hashes to
`9c85304883f42df9d4cc479dc59beebd70fe1f98e0a335bc3930bd3cde06341d`.
This binds metadata, not newly verified payload bytes.

All 518 manifests declare explicit quarterly contracts, Tradovate via historical
NinjaTrader export, interval-end timestamps, no filled minutes and no
repository-generated source; all carry ready-receipt paths. Their
`historical_model_selection_eligible` remains false at quarantine level.
Research permission comes from V2's explicit historical-quarantine authorization,
not from changing those flags. Source locations:
`data/nq/ninjatrader_minutes.sqlite3` and
`data/nq/ninjatrader_quarantine/snapshots/<snapshot-prefix>/manifest.json`.

Actual row admission remains stricter than counts: `_load_complete_snapshot`
requires the exact expected timestamp set for BOTH products and the scheduled
explicit maturity, validates observation hashes, and requires aligned pairs.
The roll rule switches on the Monday of quarterly third-Friday week. Historical
receipt/hash lineage supports reproducibility, not independently certified
exchange prices or proof of what was available in real time. No historical
revision/as-of guarantee was established here. This is development-only source
evidence, not live-feed or promotion qualification.

## Source APIs And Target

- `src/aitrader/nq_apex_multiresolution.py::load_minute_development_inputs`
  already constructs the full development cohort using
  `src/aitrader/nq_apex_ninjatrader_25k.py::_load_complete_snapshot`.
  It excludes out-of-split prices before per-snapshot loading, but first queries
  global timestamp metadata and opens SQLite without enforced read-only mode.
  Do not invoke it during this review. A later isolated reader should retain
  its admission rules with explicit snapshot allowlists and a read-only URI.
- `src/aitrader/nq_minute_store.py::query_bars` preserves snapshot/batch identity,
  explicit symbol and integer ticks; bounds are inclusive INTERVAL ENDS. It
  rejects ambiguous sources, but is not itself split/full-session admission,
  and its connection helper also lacks enforced read-only mode. Query per
  admitted snapshot; the default 10,000-row limit is not a full-history extract.
- `src/aitrader/nq_apex_tradovate_qualification.py` supplies
  `contract_pair_for_trade_date` and `expected_tradovate_session_epochs`.
  `MinuteBar.epoch` is the interval START; its close/volume become available
  only at `epoch + 60`. Never turn a start-stamped close into a pre-close input.
- `tools/nq_apex_intraday_opportunities_v87.py::extract_opportunities` can
  reconstruct causal minute opportunities on the full admitted calendar;
  `tools/nq_apex_minute_volume_join_v123.py::build_contexts` supplies matched
  NQ-anchor features. Neither fabricates older tick outcomes. V123's prepared
  wrapper is deliberately fixed to 181 dates/5,485 original events. V129's
  `unit_cents`/population bindings require original own-product tick journals;
  older minute returns cannot be appended as if they satisfied that schema.

**Yes: a fixed-horizon close-to-close return is valid forecast supervision.**
For example, at completed-minute decision D, define an own-product signed
return `s * (C[D+h] / C[D] - 1)`, with direction s known at D and one fixed h.
Keep both endpoints within the same explicit contract and complete session.
This asks about subsequent price displacement. It does NOT label target-before-
stop, executable entry, net cents, fill probability or account profit. A model
of this return cannot be substituted into four cost-mode net-payoff heads or
interpreted as expected account utility without a separately declared adapter.
Minute OHLC cannot recover intrabar ordering, stop gaps or delayed tick fills.

## Leakage And Evaluation Boundaries

1. Preserve the exact 181 admitted raw pairs and all 126 scored dates, including
   empty/untradeable dates, in three 42-date blocks. Use existing 45/87/129 raw
   prefixes and ten-session purges on the FULL admitted minute calendar, not
   ten sparse event dates. The older set adds at most 436 dates to each prefix:
   481/523/565 before feature warmup or target eligibility exclusions.
2. Every training label must end strictly before its fold's maturity cutoff
   (the current contract uses 09:00 ET on the first purge date). Validate this
   before any support filter. Features use only completed bars/prior sessions;
   scalers, target normalization and any fitted transfer/calibration use the
   training prefix only. No random event splits or full-development pretraining
   followed by retrospective scoring. Earlier scored dates enter later fits
   only when the declared expanding prefix and maturity rules permit them.
3. Preserve explicit maturity per product. Never compute returns across rolled
   price levels; reset maturity-specific activity context or use documented
   within-contract summaries. Pair NQ/MNQ by time and maturity, never synthesize
   one product's prices or execution labels from the other's multiplier.
4. Historical minute opportunity labels may overlap. Weight/assess by session;
   more bars are not more independent sessions. Freeze feature/event support,
   horizon, learner and decision mapping before outcomes; do not select only
   old filled/profitable trades. Keep scoring outcomes outside fitting inputs.
5. June 15-26 outer embargo and June 29-September 2 sealed holdout remain excluded
   from learning, normalization and selection. Repeatedly reused development
   dates cannot establish independent generalization. Actual tick replay retains
   own-product contracts, provider sequence, delays, stops/targets, costs,
   integer sizing and continuous account state. Last-tick simulation itself is
   not proof of bid/ask liquidity or actual fills.

## Decision And Minimum Next Experiment

**Conditional go for one matched history ablation; no-go for an unqualified
"more data" refit or another V76/V89/V129 hurdle recipe.** There is no missing
older-minute acquisition problem to solve, and no reason to build a new storage
platform. V76 already had long history; V89/V129 already explored decomposition.

After the sole V130 run is terminal and a separate design is preregistered under
the user's existing research authorization, the smallest
informative study is two matched arms: the same fixed causal minute features,
own-product return target and modest regularized learner, trained on (a) mature
raw-era minute sessions and (b) those sessions plus the admitted older minutes.
One horizon only; the existing event terminal boundary of D+91 minutes is a
defensible alignment to review, not a parameter frozen by this note. Keep
direction/event support unchanged so the contrast tests added history rather
than a new event catalog. This is not a matched comparison against V129's
different net-cent task.

Hard prerequisites are a separately bound minute-return schema with feature and
label-end clocks, old-session opportunity/support admission, and a declared
return-score-to-decision adapter. Keep the execution/account engine unchanged;
do not treat a positive gross return prediction as positive net payoff or feed
it into the old net-cent utility calculation. A synthetic alignment check and
development-only structural support check must precede any fit. Existing
writers/recovery wrappers are not read-only review utilities and must not be
launched against frozen dependencies.

If these contracts can be specified without outcome-driven horizon/gate search,
freeze that finite comparison separately and evaluate on the unchanged
126-date actual tick/account path, with no partial-outcome tuning or blind
repeats. Return prediction diagnostics and executable economic results remain
different claims; lower MSE alone is neither a pass nor an economic veto.
If a credible decision adapter or sufficient matched support cannot be declared,
stop: the available minutes do not overcome that blocker, and repeating the
already-failed broad longer-history path is not worth another fit. No trial,
reservation, candidate implementation or follow-on run was created here.
