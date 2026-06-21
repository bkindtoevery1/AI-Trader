# Architecture

```text
config/strategy.yaml
        |
        v
aitrader.config -> aitrader.strategy -> aitrader.backtest
        |                  |                  |
        |                  v                  v
        |            aitrader.broker    aitrader.reporting
        |                  |                  |
        v                  v                  v
aitrader.toss_client   Toss Open API     web/public/dashboard-data.json
```

## Modules

- `aitrader.toss_client`: Toss Invest REST API wrapper.
- `aitrader.strategy`: rule-based signal generation.
- `aitrader.backtest`: long-only simulator and parameter search.
- `aitrader.broker`: order intent creation and risk checks.
- `aitrader.reporting`: Markdown and dashboard JSON writers.
- `web`: React dashboard deployed as static assets.

## Data Contract

`data/sample_candles.csv` uses:

```csv
symbol,timestamp,open,high,low,close,volume,currency
```

Toss candle payloads are normalized into the same internal `Candle` model.

