# AI Trader

Toss Invest Open API 기반 룰 베이스 자동매매 프로젝트입니다. 기본 실행은 항상 `dry-run`이며, 실거래는 `config/strategy.yaml`의 `risk.allow_live_trading: true`와 CLI의 `--execute`가 동시에 필요합니다.

## What It Does

- Toss Invest Open API 형식에 맞춘 인증, 시세, 캔들, 계좌, 주문 클라이언트
- 이동평균 교차 + RSI 필터 기반 룰 베이스 전략
- 백테스트, 개선 후보 탐색, Markdown/JSON 리포트 생성
- React 대시보드와 GitHub Pages 배포 워크플로
- 유닛테스트와 GitHub Actions CI

공식 문서 기준:

- 문서 진입점: https://developers.tossinvest.com/docs
- LLM용 안내: https://developers.tossinvest.com/llms.txt
- OpenAPI JSON: https://openapi.tossinvest.com/openapi-docs/latest/openapi.json

## Quick Start

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e ".[dev]"
pytest
ai-trader daily --data data/sample_candles.csv --report-dir reports --dashboard web/public/dashboard-data.json
```

웹 대시보드:

```bash
cd web
npm install
npm run dev
```

## Trading Flow

1. `ai-trader daily`가 최신 캔들 데이터로 백테스트를 수행합니다.
2. `find_improvements`가 SMA 윈도우 조합을 비교해 개선 후보를 리포트합니다.
3. 대시보드는 `web/public/dashboard-data.json`을 읽어 결과를 표시합니다.
4. `ai-trader trade`는 주문 의도만 출력합니다.
5. 실주문은 `ai-trader trade --execute`와 `risk.allow_live_trading: true`가 모두 설정된 경우에만 Toss 주문 API를 호출합니다.

Toss API에서 최신 캔들을 내려받으려면:

```bash
ai-trader fetch-candles --out data/live_candles.csv
ai-trader daily --data data/live_candles.csv --report-dir reports --dashboard web/public/dashboard-data.json
ai-trader trade --live-data
```

실제 계좌 기준으로 buying power, holdings, sellable quantity를 반영하려면:

```bash
ai-trader account
ai-trader daily --live-data --account-snapshot --save-data data/live_candles.csv
ai-trader trade --live-data --account-snapshot
```

실주문은 여전히 아래 두 조건이 동시에 필요합니다.

- `config/strategy.yaml`의 `risk.allow_live_trading: true`
- CLI의 `ai-trader trade --execute`

## Environment

```bash
cp .env.example .env
export TOSSINVEST_CLIENT_ID=...
export TOSSINVEST_CLIENT_SECRET=...
export TOSSINVEST_ACCOUNT_SEQ=...
```

계좌, 자산, 주문 관련 Toss API는 `Authorization: Bearer ...` 외에 `X-Tossinvest-Account` 헤더가 필요합니다.

## Deployment

`.github/workflows/deploy-pages.yml`가 GitHub Pages 배포를 담당합니다. `main` 브랜치에 push되면 Python 리포트 데이터를 생성하고 Vite 대시보드를 빌드한 뒤 Pages에 배포합니다.

## Safety Defaults

- 기본 모드: `dry-run`
- 실거래 기본 차단: `risk.allow_live_trading: false`
- 일일 주문 수 제한: `risk.max_daily_orders`
- 주문 금액 제한: `risk.max_order_value`
- 현금 보존 비율: `risk.reserve_cash_pct`
