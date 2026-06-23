#!/bin/zsh
set -euo pipefail

cd /Users/bkindtoevery1/workspace/AI-Trader

START_DATE="$(date -v-5y +%Y-%m-%d)"
END_DATE="$(date +%Y-%m-%d)"

for SYMBOL in SOXL SOXS; do
  SYMBOL_LOWER="$(echo "${SYMBOL}" | tr '[:upper:]' '[:lower:]')"
  .venv/bin/python service/server/scripts/fetch_toss_candles.py \
    --symbol "${SYMBOL}" \
    --interval 1d \
    --count 200 \
    --max-pages 1 \
    --sleep-seconds 0.2 \
    --start-date "${START_DATE}" \
    --end-date "${END_DATE}" \
    --csv-path "service/server/data/exports/${SYMBOL_LOWER}_1d_adjusted_5y.csv"
done
