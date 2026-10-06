# Local NQ/MNQ Data Inventory

Read-only metadata inventory on October6,2026. Counts below exclude duplicate
copies and synthetic fixtures. No sealed prices or holdout outcomes were read.

| Kind | Dates | Rows or Events | First Date | Last Date |
| --- | ---: | ---: | --- | --- |
| One-minute NQ+MNQ | 774 | 2,119,916 | 2023-09-05 | 2026-09-02 |
| NQ Last ticks | 256 | 127,392,138 | 2025-09-08 | 2026-09-02 |
| MNQ Last ticks | 256 | 462,900,801 | 2025-09-08 | 2026-09-02 |
| Combined Last ticks | 256 | 590,292,939 | 2025-09-08 | 2026-09-02 |

The minute count includes incomplete days:671dates have1,380minutes for BOTH
products,103do not. Product rows are1,059,923NQ and1,059,993MNQ. Derived15-tick
bars are39,353,094, not additional observations to add to raw ticks.

## Research Split

- Development through June12:617complete minute sessions (1,702,920rows),
  198tick dates (426,329,294events). The raw/minute complete intersection used
  by the recent experiments is181dates.
- Ten outer embargo dates:June15-26.
- Sealed holdout:48dates,June29-September2. Metadata only was inspected.
- The recent126scored development dates are reused historical research dates,
  not a newly independent holdout or126new collection sessions.

## New Collection

The latest full-session admission report at2026-10-05T23:40:00.456666Z has
joint_receipt_count=0 and ready_manifests=0. No additional complete raw+minute
session after September2 is admitted by that pipeline.

Predecision staging contains1,334raw chunks on13dates,September7-October5,
totaling1,392,777,044bytes. These are partial/unprocessed, with interval variants;
file counts are not extra unique sessions. Event counts are unverified. A
64-chunk predecision sequence is not the required92-chunk23-hour session.

## Storage And Verification

Historical tick Parquet:512files,3,405,562,837logical bytes. Minute originals:
120,708,532bytes, with another identical incoming copy; normalized CSV and
SQLite are derived storage. data/nq totals6,800,978,786logical bytes and
6,832,852,992allocated bytes, including partial data/metadata/state. Reports
consume another5,415,317,504allocated bytes but are not new market history.
The manifest's41,479,113,634original tick-CSV bytes are not locally retained
CSV space: the local history is compressed Parquet.

Read-only inventory verified774minute manifest hashes against SQLite snapshot
pins and ready receipts;256tick manifests/conversion receipts, count sums and
512Parquet sizes; no duplicate market dates/original hash identities. It also
checked the existing development-cache hash and holdout identity metadata.
Entire payload hashes and all590million rows were NOT reread this time.
Counts rely on the linked manifests/receipts, not new provider verification.

Authorities: data/nq/ninjatrader_quarantine/snapshots,
data/nq/ninjatrader_raw_tick_quarantine/snapshots,
config/nq-apex-multiresolution-research-v2.yaml,
config/nq-apex-multiresolution-holdout-v1.json,
reports/nq_apex_multiresolution_v2/development_features_v2.json,
reports/nq_apex_v27_full_session_pipeline/runtime-admission.json.
