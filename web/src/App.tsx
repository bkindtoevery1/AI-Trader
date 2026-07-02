import {
  Activity,
  BarChart3,
  CalendarClock,
  FileText,
  Gauge,
  GitBranch,
  RefreshCw,
  ShieldCheck,
  TrendingUp,
} from "lucide-react";
import { useEffect, useMemo, useState } from "react";

type EquityPoint = {
  date: string;
  equity: string;
};

type DrawdownPoint = {
  date: string;
  drawdownPct: string;
};

type ReturnPoint = {
  date: string;
  returnPct: string;
};

type PricePoint = {
  date: string;
  close: string;
};

type ParameterValue = string | number | string[];

type BacktestMetrics = {
  cagrPct?: string;
  volatilityPct?: string;
  sortino?: string;
  calmar?: string;
  winRatePct?: string;
  avgTradeReturnPct?: string;
  bestTradePct?: string;
  worstTradePct?: string;
  profitFactor?: string;
  exposurePct?: string;
  buyHoldReturnPct?: string;
  closedTrades?: number;
};

type BacktestResult = {
  id?: string;
  symbol: string;
  strategyName?: string;
  totalReturnPct: string;
  maxDrawdownPct: string;
  sharpe: string;
  tradeCount: number;
  equityCurve: EquityPoint[];
  drawdownCurve?: DrawdownPoint[];
  returnCurve?: ReturnPoint[];
  priceCurve?: PricePoint[];
  parameters: Record<string, ParameterValue>;
  metrics?: BacktestMetrics;
};

type Signal = {
  symbol: string;
  side: "BUY" | "SELL" | "HOLD";
  score: number;
  price: string;
  timestamp: string;
  reason: string;
};

type Improvement = {
  title: string;
  rationale: string;
  expectedDeltaPct: string;
  parameters: Record<string, ParameterValue>;
};

type TradeDecision = {
  symbol: string;
  signal: "BUY" | "SELL" | "HOLD";
  action: "BUY" | "SELL" | "SKIP";
  score: number;
  price: string;
  quantity: string;
  notional: string;
  orderType: string | null;
  limitPrice: string | null;
  clientOrderId: string | null;
  accepted: boolean;
  reason: string;
  dryRun: boolean;
};

type RiskData = {
  initialCash: string;
  currency: string;
  maxPositionPct: string;
  symbolPositionCaps?: Record<string, string>;
  reserveCashPct: string;
  maxOrderValue: string;
  maxDailyOrders: number;
  feeBps: string;
  slippageBps: string;
  allowLiveTrading: boolean;
};

type StrategyData = {
  name: string;
  symbols: string[];
  interval: string;
  candleCount: number;
  shortWindow: number;
  longWindow: number;
  rsiPeriod: number;
  rsiBuyBelow: string;
  rsiSellAbove: string;
};

type ExecutionData = {
  mode: string;
  orderType: string;
  priceOffsetBps: string;
};

type AccountData = {
  generatedAt: string;
  source: string;
  buyingPower: Record<string, string>;
  holdings: Record<string, string>;
  sellableQuantities: Record<string, string>;
  errors: string[];
};

type DashboardData = {
  generatedAt: string;
  mode: string;
  status: string;
  summary: {
    symbols: string[];
    bestSymbol: string;
    bestStrategy?: string;
    bestResultId?: string;
    bestReturnPct: string;
    tradeCount: number;
    maxDrawdownPct: string;
    strategyResultCount?: number;
  };
  results: BacktestResult[];
  signals: Signal[];
  improvements: Improvement[];
  decisions?: TradeDecision[];
  strategyPlans?: StrategyPlan[];
  risk?: RiskData;
  strategy?: StrategyData;
  execution?: ExecutionData;
  account?: AccountData;
};

type ViewMode = "overview" | "risk" | "reports";

type StrategyPlan = {
  symbol: string;
  strategyName: string;
  pro: string;
  action: "BUY" | "SELL" | "HOLD";
  actionReason: string;
  previousDate: string;
  previousClose: string;
  currentDate: string;
  currentClose: string;
  buyThresholdPct: string;
  buyLimit: string;
  sellThresholdPct: string;
  sellTrigger: string;
  tierPct: string;
  tierBudget: string;
  tierQuantity: string;
  sellTargetAfterBuy: string;
  stopLossDays: number;
};

function sampleResult(
  symbol: string,
  strategyName: string,
  pro: string,
  totalReturnPct: string,
  maxDrawdownPct: string,
  sharpe: string,
  buyThresholdPct: string,
  sellThresholdPct: string,
): BacktestResult {
  const initialEquity = 10000;
  const finalEquity = initialEquity * (1 + Number(totalReturnPct) / 100);
  const previousClose = symbol === "SOXL" ? "212.40" : "3.94";
  const currentClose = symbol === "SOXL" ? "217.55" : "3.86";
  return {
    id: `${symbol}:${strategyName}`,
    symbol,
    strategyName,
    totalReturnPct,
    maxDrawdownPct,
    sharpe,
    tradeCount: 4,
    equityCurve: [
      { date: "2026-04-01", equity: String(initialEquity) },
      { date: "2026-05-01", equity: String(Math.round((initialEquity + finalEquity) / 2)) },
      { date: "2026-06-22", equity: String(Math.round(finalEquity)) },
    ],
    drawdownCurve: [
      { date: "2026-04-01", drawdownPct: "0" },
      { date: "2026-05-01", drawdownPct: `-${maxDrawdownPct}` },
      { date: "2026-06-22", drawdownPct: "-2.20" },
    ],
    priceCurve: [
      { date: "2026-06-19", close: previousClose },
      { date: "2026-06-22", close: currentClose },
    ],
    parameters: {
      sourceLogic: "buy-dip-sell-peak",
      strategy: strategyName,
      pro,
      buyThresholdPct,
      sellThresholdPct,
      tierRatios: ["0.33", "0.33", "0.34"],
      stopLossDays: "3",
    },
    metrics: {
      cagrPct: totalReturnPct,
      volatilityPct: symbol === "SOXL" ? "68.20" : "52.40",
      sortino: "1.20",
      calmar: "1.10",
      winRatePct: "54.00",
      profitFactor: "1.35",
      exposurePct: "36.00",
      buyHoldReturnPct: "0.00",
      closedTrades: 4,
    },
  };
}

const fallbackRisk: RiskData = {
  initialCash: "10000",
  currency: "USD",
  maxPositionPct: "30",
  symbolPositionCaps: { SOXS: "20" },
  reserveCashPct: "15",
  maxOrderValue: "1000",
  maxDailyOrders: 2,
  feeBps: "1.5",
  slippageBps: "5",
  allowLiveTrading: false,
};

const fallbackResults: BacktestResult[] = [
  sampleResult("SOXL", "bdsp-pro1", "Pro 1", "18.40", "14.20", "1.18", "-2.50", "4.00"),
  sampleResult("SOXL", "bdsp-pro2", "Pro 2", "16.10", "12.80", "1.05", "-3.00", "5.00"),
  sampleResult("SOXL", "bdsp-pro3", "Pro 3", "13.75", "11.40", "0.94", "-3.50", "6.00"),
  sampleResult("SOXS", "bdsp-pro1", "Pro 1", "5.80", "8.90", "0.72", "-2.50", "4.00"),
  sampleResult("SOXS", "bdsp-pro2", "Pro 2", "4.90", "8.20", "0.68", "-3.00", "5.00"),
  sampleResult("SOXS", "bdsp-pro3", "Pro 3", "3.60", "7.70", "0.61", "-3.50", "6.00"),
];

const fallbackData: DashboardData = {
  generatedAt: "2026-06-22T00:00:00+09:00",
  mode: "dry-run",
  status: "ready",
  summary: {
    symbols: ["SOXL", "SOXS"],
    bestSymbol: "SOXL",
    bestStrategy: "bdsp-pro1",
    bestResultId: "SOXL:bdsp-pro1",
    bestReturnPct: "18.40",
    tradeCount: 24,
    maxDrawdownPct: "14.20",
    strategyResultCount: fallbackResults.length,
  },
  results: fallbackResults,
  signals: [
    {
      symbol: "SOXL",
      side: "HOLD",
      score: 0.5,
      price: "217.55",
      timestamp: "2026-06-22T00:00:00+09:00",
      reason: "sample snapshot; run local daily report for live Toss data",
    },
    {
      symbol: "SOXS",
      side: "HOLD",
      score: 0.5,
      price: "3.86",
      timestamp: "2026-06-22T00:00:00+09:00",
      reason: "sample snapshot; run local daily report for live Toss data",
    },
  ],
  improvements: [
    {
      title: "SOXL/SOXS: 종가 확정 후 threshold 재검증",
      rationale: "장 시작 전에는 stale snapshot 여부를 먼저 확인하고, 종가 확정 데이터로 다음날 기준선을 갱신합니다.",
      expectedDeltaPct: "0.8",
      parameters: { sourceLogic: "buy-dip-sell-peak" },
    },
  ],
  decisions: [
    {
      symbol: "SOXL",
      signal: "HOLD",
      action: "SKIP",
      score: 0.5,
      price: "217.55",
      quantity: "0",
      notional: "0",
      orderType: null,
      limitPrice: null,
      clientOrderId: null,
      accepted: true,
      reason: "fallback sample; no live order preview loaded",
      dryRun: true,
    },
    {
      symbol: "SOXS",
      signal: "HOLD",
      action: "SKIP",
      score: 0.5,
      price: "3.86",
      quantity: "0",
      notional: "0",
      orderType: null,
      limitPrice: null,
      clientOrderId: null,
      accepted: true,
      reason: "fallback sample; no live order preview loaded",
      dryRun: true,
    },
  ],
  strategyPlans: buildStrategyPlans(fallbackResults, fallbackRisk),
  risk: fallbackRisk,
  strategy: {
    name: "buy-dip-sell-peak",
    symbols: ["SOXL", "SOXS"],
    interval: "1d",
    candleCount: 120,
    shortWindow: 0,
    longWindow: 0,
    rsiPeriod: 0,
    rsiBuyBelow: "0",
    rsiSellAbove: "0",
  },
  execution: {
    mode: "dry-run",
    orderType: "LIMIT",
    priceOffsetBps: "10",
  },
  account: {
    generatedAt: "2026-06-22T00:00:00+09:00",
    source: "simulated",
    buyingPower: { USD: "10000" },
    holdings: {},
    sellableQuantities: {},
    errors: [],
  },
};

function App() {
  const [data, setData] = useState<DashboardData>(fallbackData);
  const [activeView, setActiveView] = useState<ViewMode>("overview");
  const [selectedResultId, setSelectedResultId] = useState("PORTFOLIO");
  const [statusMessage, setStatusMessage] = useState("Report loaded");
  const [refreshing, setRefreshing] = useState(false);

  useEffect(() => {
    loadDashboardData().then((payload) => {
      setData(payload);
      setStatusMessage(`Updated ${formatDate(payload.generatedAt)}`);
    });
  }, []);

  const portfolio = useMemo(() => buildPortfolioResult(data.results), [data.results]);
  const chartOptions = useMemo(() => [portfolio, ...data.results], [portfolio, data.results]);
  const selectedChart = useMemo(
    () =>
      selectedResultId === "PORTFOLIO"
        ? portfolio
        : data.results.find((item) => resultKey(item) === selectedResultId) ?? portfolio,
    [data.results, portfolio, selectedResultId],
  );
  const portfolioReturn = useMemo(
    () => num(portfolio.totalReturnPct).toFixed(2),
    [portfolio.totalReturnPct],
  );
  const strategyPlans = useMemo(
    () => data.strategyPlans?.length ? data.strategyPlans : buildStrategyPlans(data.results, data.risk),
    [data.results, data.risk, data.strategyPlans],
  );
  const decisions = useMemo(() => {
    if (data.decisions?.length) {
      return data.decisions;
    }
    return data.signals.map<TradeDecision>((signal) => ({
      symbol: signal.symbol,
      signal: signal.side,
      action: "SKIP",
      score: signal.score,
      price: signal.price,
      quantity: "0",
      notional: "0",
      orderType: null,
      limitPrice: null,
      clientOrderId: null,
      accepted: signal.side === "HOLD",
      reason: signal.reason,
      dryRun: true,
    }));
  }, [data.decisions, data.signals]);
  const isStaleSnapshot = useMemo(() => snapshotIsStale(data.generatedAt), [data.generatedAt]);
  const snapshotAge = useMemo(() => snapshotAgeLabel(data.generatedAt), [data.generatedAt]);
  const primaryStrategyName = strategyPlans[0]?.strategyName ?? data.strategy?.name ?? "primary strategy";
  const previewMode = decisions.every((decision) => decision.dryRun) ? "Dry Run" : "Live";

  const refreshReport = async () => {
    setRefreshing(true);
    try {
      const payload = await loadDashboardData(true);
      setData(payload);
      setStatusMessage(`Refreshed ${formatTime(new Date())}`);
    } finally {
      setRefreshing(false);
    }
  };

  const switchView = (view: ViewMode) => {
    setActiveView(view);
    setStatusMessage(`${view[0].toUpperCase()}${view.slice(1)} view selected`);
  };

  const openRiskGuard = () => {
    setActiveView("risk");
    setStatusMessage("Live orders remain blocked unless config and CLI both allow execution");
  };

  const inspectDryRun = () => {
    setActiveView("risk");
    setStatusMessage("Dry-run mode previews orders without submitting them");
  };

  const selectChart = (resultId: string) => {
    setSelectedResultId(resultId);
    const result = chartOptions.find((item) => resultKey(item) === resultId);
    setStatusMessage(`${displayResult(result ?? selectedChart)} chart selected`);
  };

  const selectedSignal = useMemo(
    () => data.signals.find((signal) => signal.symbol === selectedChart.symbol),
    [data.signals, selectedChart.symbol],
  );

  return (
    <main className="shell">
      <aside className="sidebar" aria-label="workspace">
        <div className="brand">
          <div className="brandMark">
            <TrendingUp size={22} />
          </div>
          <div>
            <strong>AI Trader</strong>
            <span>Toss Invest</span>
          </div>
        </div>
        <nav className="nav">
          <button
            className={`navItem ${activeView === "overview" ? "active" : ""}`}
            title="Overview"
            onClick={() => switchView("overview")}
          >
            <BarChart3 size={18} />
            <span>Overview</span>
          </button>
          <button
            className={`navItem ${activeView === "risk" ? "active" : ""}`}
            title="Risk"
            onClick={() => switchView("risk")}
          >
            <ShieldCheck size={18} />
            <span>Risk</span>
          </button>
          <button
            className={`navItem ${activeView === "reports" ? "active" : ""}`}
            title="Reports"
            onClick={() => switchView("reports")}
          >
            <FileText size={18} />
            <span>Reports</span>
          </button>
        </nav>
        <div className="sidebarStatus">
          <span className="pulse" />
          <span>{data.mode}</span>
        </div>
      </aside>

      <section className="workspace">
        <header className="topbar">
          <div>
            <p className="eyebrow">Rule-Based Automation</p>
            <h1>Daily Strategy Desk</h1>
          </div>
          <div className="toolbar">
            <button className="iconButton" title="Refresh report" aria-label="Refresh report" onClick={refreshReport}>
              <RefreshCw className={refreshing ? "spin" : ""} size={18} />
            </button>
            <button className="iconButton" title="Risk guard" aria-label="Risk guard" onClick={openRiskGuard}>
              <ShieldCheck size={18} />
            </button>
            <button className="runButton" title="Dry-run mode" onClick={inspectDryRun}>
              <Activity size={18} />
              <span>Dry Run</span>
            </button>
          </div>
        </header>

        <div className="statusStrip" role="status">
          <span>{statusMessage}</span>
          <strong className={isStaleSnapshot ? "staleText" : ""}>
            {snapshotAge} · {data.summary.symbols.join(" / ")}
          </strong>
        </div>
        {isStaleSnapshot ? (
          <div className="warningBanner" role="note">
            정적 스냅샷이 오래됐습니다. 화면의 전략별 조건표보다 실제 주문 후보와 로컬 dry-run 결과를 우선 확인하세요.
          </div>
        ) : null}

        <section className="metricGrid" aria-label="summary">
          <Metric icon={<Gauge />} label="Universe" value={data.summary.symbols.join(" / ")} note="tracked symbols" />
          <Metric icon={<TrendingUp />} label="Portfolio" value={`${portfolioReturn}%`} note="combined backtest" />
          <Metric icon={<ShieldCheck />} label="Max DD" value={`${num(data.summary.maxDrawdownPct).toFixed(2)}%`} note="risk budget" />
          <Metric icon={<GitBranch />} label="Strategies" value={String(data.summary.strategyResultCount ?? data.results.length)} note={`${data.summary.bestSymbol} · ${data.summary.bestStrategy ?? "best"}`} />
        </section>

        {activeView === "overview" ? (
          <>
          <section className="panel planPanel" aria-label="strategy buy sell plans">
            <div className="panelHeader">
              <div>
                <p className="eyebrow">Strategy Conditions</p>
                <h2>전략별 조건표</h2>
              </div>
              <span className="badge amber">정보용</span>
            </div>
            <p className="basisNote">
              이 표는 모든 전략 변형의 dip/peak 조건을 비교합니다. 실제 주문 후보는 {primaryStrategyName}
              신호에 계좌 잔액, SOXS 20% 제한, 일일 2건 제한을 적용한 아래 카드 기준입니다.
            </p>
            <div className="planTableWrap">
              <table className="dataTable planTable">
                <thead>
                  <tr>
                    <th>Symbol</th>
                    <th>Strategy</th>
                    <th>Plan</th>
                    <th>Basis</th>
                    <th>Buy Dip</th>
                    <th>Sell Peak</th>
                    <th>Tier 1</th>
                    <th>After Buy</th>
                    <th>Risk</th>
                  </tr>
                </thead>
                <tbody>
                  {strategyPlans.map((plan) => (
                    <tr key={`${plan.symbol}:${plan.strategyName}`}>
                      <td>{plan.symbol}</td>
                      <td>
                        <strong>{plan.strategyName}</strong>
                        <span className="cellSub">{plan.pro}</span>
                      </td>
                      <td>
                        <SideBadge side={plan.action} />
                        <span className="cellSub">{plan.actionReason}</span>
                      </td>
                      <td>
                        {plan.previousDate} → {plan.currentDate}
                        <span className="cellSub">
                          {formatPrice(plan.previousClose)} → {formatPrice(plan.currentClose)}
                        </span>
                      </td>
                      <td>
                        <strong className="positive">≤ {formatPrice(plan.buyLimit)}</strong>
                        <span className="cellSub">{formatPct(plan.buyThresholdPct)}</span>
                      </td>
                      <td>
                        <strong className="negative">≥ {formatPrice(plan.sellTrigger)}</strong>
                        <span className="cellSub">{formatPct(plan.sellThresholdPct)}</span>
                      </td>
                      <td>
                        {formatMoney(plan.tierBudget, data.risk?.currency)}
                        <span className="cellSub">{formatPct(plan.tierPct)} · {plan.tierQuantity}주</span>
                      </td>
                      <td>
                        {formatPrice(plan.sellTargetAfterBuy)}
                        <span className="cellSub">filled buy 기준 목표</span>
                      </td>
                      <td>
                        {plan.stopLossDays}d stop
                        <span className="cellSub">{plan.symbol === "SOXS" ? "max 20% cap" : "position cap"}</span>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </section>
          <section className="mainGrid">
          <section className="panel chartPanel">
            <div className="panelHeader">
              <div>
                <p className="eyebrow">Equity Curve</p>
                <h2>{displayResult(selectedChart)}</h2>
              </div>
              <span className="timestamp">{formatDate(data.generatedAt)}</span>
            </div>
            <div className="segmented" aria-label="chart symbol selector">
              {chartOptions.map((result) => (
                <button
                  key={resultKey(result)}
                  className={resultKey(result) === resultKey(selectedChart) ? "selected" : ""}
                  onClick={() => selectChart(resultKey(result))}
                >
                  {displayResult(result)}
                </button>
              ))}
            </div>
            <Sparkline points={selectedChart.equityCurve} />
            <DrawdownChart points={selectedChart.drawdownCurve ?? drawdownFromEquity(selectedChart.equityCurve)} />
            <div className="statStrip">
              <span>CAGR <strong>{formatPct(selectedChart.metrics?.cagrPct)}</strong></span>
              <span>Vol <strong>{formatPct(selectedChart.metrics?.volatilityPct)}</strong></span>
              <span>Win <strong>{formatPct(selectedChart.metrics?.winRatePct)}</strong></span>
              <span>PF <strong>{formatNumber(selectedChart.metrics?.profitFactor)}</strong></span>
              <span>Exposure <strong>{formatPct(selectedChart.metrics?.exposurePct)}</strong></span>
            </div>
            {selectedSignal && selectedChart.symbol !== "PORTFOLIO" ? (
              <div className="chartNote">
                <SideBadge side={selectedSignal.side} />
                <span>{selectedSignal.reason}</span>
              </div>
            ) : (
              <div className="chartNote">
                <span className="badge safe">Portfolio</span>
                <span>Combined curve across tracked symbols</span>
              </div>
            )}
          </section>

          <section className="panel">
            <div className="panelHeader">
              <div>
                <p className="eyebrow">Executable Preview</p>
                <h2>실제 주문 후보</h2>
              </div>
              <span className={previewMode === "Dry Run" ? "badge amber" : "badge safe"}>{previewMode}</span>
            </div>
            <p className="basisNote compact">
              이 카드의 행만 주문 엔진 결과입니다. 대시보드 버튼은 토스 주문을 제출하지 않습니다.
            </p>
            <div className="signalList">
              {decisions.map((decision) => (
                <article className="signalRow" key={decision.symbol}>
                  <div>
                    <strong>{decision.symbol}</strong>
                    <span>
                      {decision.reason} · {decision.quantity}주 · {formatMoney(decision.notional)}
                      {decision.limitPrice ? ` · ${decision.orderType ?? "LIMIT"} ${formatPrice(decision.limitPrice)}` : ""}
                    </span>
                  </div>
                  <DecisionBadge decision={decision} />
                </article>
              ))}
            </div>
          </section>

          <section className="panel wide">
            <div className="panelHeader">
              <div>
                <p className="eyebrow">Backtest Matrix</p>
                <h2>Strategy Results</h2>
              </div>
              <CalendarClock size={18} />
            </div>
            <table className="dataTable">
              <thead>
                <tr>
                  <th>Symbol</th>
                  <th>Strategy</th>
                  <th>Return</th>
                  <th>Max DD</th>
                  <th>CAGR</th>
                  <th>Vol</th>
                  <th>Sharpe</th>
                  <th>Sortino</th>
                  <th>Calmar</th>
                  <th>Win</th>
                  <th>Trades</th>
                  <th>PF</th>
                  <th>Exposure</th>
                  <th>Parameters</th>
                </tr>
              </thead>
              <tbody>
                {data.results.map((result) => (
                  <tr key={resultKey(result)}>
                    <td>
                      <button className="tableButton" onClick={() => selectChart(resultKey(result))}>
                        {result.symbol}
                      </button>
                    </td>
                    <td>{result.strategyName ?? result.parameters.strategy ?? "strategy"}</td>
                    <td className={num(result.totalReturnPct) >= 0 ? "positive" : "negative"}>
                      {num(result.totalReturnPct).toFixed(2)}%
                    </td>
                    <td>{num(result.maxDrawdownPct).toFixed(2)}%</td>
                    <td className={num(result.metrics?.cagrPct) >= 0 ? "positive" : "negative"}>
                      {formatPct(result.metrics?.cagrPct)}
                    </td>
                    <td>{formatPct(result.metrics?.volatilityPct)}</td>
                    <td>{num(result.sharpe).toFixed(2)}</td>
                    <td>{formatNumber(result.metrics?.sortino)}</td>
                    <td>{formatNumber(result.metrics?.calmar)}</td>
                    <td>{formatPct(result.metrics?.winRatePct)}</td>
                    <td>{result.tradeCount}</td>
                    <td>{formatNumber(result.metrics?.profitFactor)}</td>
                    <td>{formatPct(result.metrics?.exposurePct)}</td>
                    <td>{parameterText(result.parameters)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </section>

          <section className="panel">
            <div className="panelHeader">
              <div>
                <p className="eyebrow">Daily Improve</p>
                <h2>Next Tests</h2>
              </div>
              <span className="badge amber">Review</span>
            </div>
            <div className="improvementList">
              {data.improvements.map((item) => (
                <article className="improvement" key={item.title}>
                  <strong>{item.title}</strong>
                  <p>{item.rationale}</p>
                  <span>+{num(item.expectedDeltaPct).toFixed(2)}%p</span>
                </article>
              ))}
            </div>
          </section>
        </section>
        </>
        ) : null}

        {activeView === "risk" ? (
          <section className="mainGrid">
            <section className="panel wide">
              <div className="panelHeader">
                <div>
                  <p className="eyebrow">Risk Guard</p>
                  <h2>Execution Controls</h2>
                </div>
                <span className="badge safe">Live Blocked</span>
              </div>
              <div className="ruleList">
                <article>
                  <strong>Dry-run first</strong>
                  <span>Execution mode is `{data.execution?.mode ?? data.mode}`. Dashboard actions do not submit Toss orders.</span>
                </article>
                <article>
                  <strong>Two-key live trading</strong>
                  <span>
                    Config is {data.risk?.allowLiveTrading ? "live-enabled" : "live-blocked"}; CLI `--execute`
                    is still required for real orders.
                  </span>
                </article>
                <article>
                  <strong>Order caps</strong>
                  <span>
                    {data.risk?.maxDailyOrders ?? 0} orders/day · max {formatMoney(data.risk?.maxOrderValue ?? "0", data.risk?.currency ?? "KRW")} · reserve {data.risk?.reserveCashPct ?? "0"}%
                  </span>
                </article>
                <article>
                  <strong>Execution source</strong>
                  <span>
                    실제 주문 후보는 {primaryStrategyName} 신호와 계좌/리스크 가드로 생성합니다. 전략별 조건표는 비교용입니다.
                  </span>
                </article>
                <article>
                  <strong>Strategy</strong>
                  <span>
                    {data.strategy?.name ?? "strategy"} · SMA {data.strategy?.shortWindow ?? "-"}
                    /{data.strategy?.longWindow ?? "-"} · RSI {data.strategy?.rsiPeriod ?? "-"}
                  </span>
                </article>
                <article>
                  <strong>Account</strong>
                  <span>
                    {data.account?.source ?? "simulated"} · buying power {formatEntries(data.account?.buyingPower)}
                  </span>
                </article>
                <article>
                  <strong>Dashboard access</strong>
                  <span>
                    Local Vite scripts bind to 127.0.0.1. It is local-only unless you deploy it, bind to 0.0.0.0,
                    or expose it through a tunnel.
                  </span>
                </article>
                <article>
                  <strong>Holdings</strong>
                  <span>{formatEntries(data.account?.holdings) || "none"}</span>
                </article>
              </div>
            </section>
            <section className="panel">
              <div className="panelHeader">
                <div>
                  <p className="eyebrow">Executable Preview</p>
                  <h2>실제 주문 후보</h2>
                </div>
              </div>
              <div className="signalList">
                {decisions.map((decision) => (
                  <article className="signalRow" key={decision.symbol}>
                    <div>
                      <strong>{decision.symbol}</strong>
                      <span>
                        {decision.quantity} shares · {formatMoney(decision.notional)}
                      </span>
                    </div>
                    <DecisionBadge decision={decision} />
                  </article>
                ))}
              </div>
            </section>
          </section>
        ) : null}

        {activeView === "reports" ? (
          <section className="mainGrid">
            <section className="panel wide">
              <div className="panelHeader">
                <div>
                  <p className="eyebrow">Backtest Matrix</p>
                  <h2>All Symbols</h2>
                </div>
                <CalendarClock size={18} />
              </div>
              <table className="dataTable">
                <thead>
                  <tr>
                    <th>Symbol</th>
                    <th>Strategy</th>
                    <th>Return</th>
                    <th>Max DD</th>
                    <th>CAGR</th>
                    <th>Vol</th>
                    <th>Sharpe</th>
                    <th>Sortino</th>
                    <th>Calmar</th>
                    <th>Win</th>
                    <th>Trades</th>
                    <th>PF</th>
                    <th>Exposure</th>
                    <th>Parameters</th>
                  </tr>
                </thead>
                <tbody>
                  {data.results.map((result) => (
                    <tr key={resultKey(result)}>
                      <td>{result.symbol}</td>
                      <td>{result.strategyName ?? result.parameters.strategy ?? "strategy"}</td>
                      <td className={num(result.totalReturnPct) >= 0 ? "positive" : "negative"}>
                        {num(result.totalReturnPct).toFixed(2)}%
                      </td>
                      <td>{num(result.maxDrawdownPct).toFixed(2)}%</td>
                      <td className={num(result.metrics?.cagrPct) >= 0 ? "positive" : "negative"}>
                        {formatPct(result.metrics?.cagrPct)}
                      </td>
                      <td>{formatPct(result.metrics?.volatilityPct)}</td>
                      <td>{num(result.sharpe).toFixed(2)}</td>
                      <td>{formatNumber(result.metrics?.sortino)}</td>
                      <td>{formatNumber(result.metrics?.calmar)}</td>
                      <td>{formatPct(result.metrics?.winRatePct)}</td>
                      <td>{result.tradeCount}</td>
                      <td>{formatNumber(result.metrics?.profitFactor)}</td>
                      <td>{formatPct(result.metrics?.exposurePct)}</td>
                      <td>{parameterText(result.parameters)}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </section>
            <section className="panel">
              <div className="panelHeader">
                <div>
                  <p className="eyebrow">Daily Improve</p>
                  <h2>Next Tests</h2>
                </div>
                <span className="badge amber">Review</span>
              </div>
              <div className="improvementList">
                {data.improvements.map((item) => (
                  <article className="improvement" key={item.title}>
                    <strong>{item.title}</strong>
                    <p>{item.rationale}</p>
                    <span>+{num(item.expectedDeltaPct).toFixed(2)}%p</span>
                  </article>
                ))}
              </div>
            </section>
          </section>
        ) : null}
      </section>
    </main>
  );
}

async function loadDashboardData(cacheBust = false): Promise<DashboardData> {
  const suffix = cacheBust ? `?t=${Date.now()}` : "";
  try {
    const response = await fetch(`${import.meta.env.BASE_URL}dashboard-data.json${suffix}`);
    return response.ok ? await response.json() : fallbackData;
  } catch {
    return fallbackData;
  }
}

function buildPortfolioResult(results: BacktestResult[]): BacktestResult {
  if (!results.length) {
    return {
      id: "PORTFOLIO",
      symbol: "PORTFOLIO",
      strategyName: "Combined",
      totalReturnPct: "0",
      maxDrawdownPct: "0",
      sharpe: "0",
      tradeCount: 0,
      equityCurve: [],
      drawdownCurve: [],
      parameters: {},
      metrics: {},
    };
  }
  const baseCurve = results.reduce((longest, result) =>
    result.equityCurve.length > longest.length ? result.equityCurve : longest,
  results[0].equityCurve);
  const equityCurve = baseCurve.map((point, index) => {
    const total = results.reduce((sum, result) => sum + num(result.equityCurve[index]?.equity ?? 0), 0);
    return { date: point.date, equity: String(total) };
  });
  const initial = num(equityCurve[0]?.equity ?? 0);
  const final = num(equityCurve[equityCurve.length - 1]?.equity ?? 0);
  const totalReturnPct = initial ? ((final - initial) / initial) * 100 : 0;
  const drawdownCurve = drawdownFromEquity(equityCurve);
  const mdd = maxDrawdown(equityCurve);
  return {
    id: "PORTFOLIO",
    symbol: "PORTFOLIO",
    strategyName: "Combined",
    totalReturnPct: String(totalReturnPct),
    maxDrawdownPct: String(mdd),
    sharpe: String(average(results.map((result) => num(result.sharpe)))),
    tradeCount: results.reduce((sum, result) => sum + result.tradeCount, 0),
    equityCurve,
    drawdownCurve,
    parameters: {},
    metrics: {
      cagrPct: String(average(results.map((result) => num(result.metrics?.cagrPct)))),
      volatilityPct: String(average(results.map((result) => num(result.metrics?.volatilityPct)))),
      sortino: String(average(results.map((result) => num(result.metrics?.sortino)))),
      calmar: String(average(results.map((result) => num(result.metrics?.calmar)))),
      winRatePct: String(average(results.map((result) => num(result.metrics?.winRatePct)))),
      profitFactor: String(average(results.map((result) => num(result.metrics?.profitFactor)).filter((value) => value < 999))),
      exposurePct: String(average(results.map((result) => num(result.metrics?.exposurePct)))),
    },
  };
}

function Metric({
  icon,
  label,
  value,
  note,
}: {
  icon: React.ReactNode;
  label: string;
  value: string;
  note: string;
}) {
  return (
    <article className="metric">
      <div className="metricIcon">{icon}</div>
      <span>{label}</span>
      <strong>{value}</strong>
      <small>{note}</small>
    </article>
  );
}

function Sparkline({ points }: { points: EquityPoint[] }) {
  const values = points.map((point) => num(point.equity));
  if (!values.length) {
    return <div className="emptyChart">No equity data</div>;
  }
  const min = Math.min(...values);
  const max = Math.max(...values);
  const range = max - min || 1;
  const path = values
    .map((value, index) => {
      const x = (index / Math.max(1, values.length - 1)) * 100;
      const y = 86 - ((value - min) / range) * 72;
      return `${x.toFixed(2)},${y.toFixed(2)}`;
    })
    .join(" ");

  return (
    <div className="chartWrap">
      <svg viewBox="0 0 100 100" preserveAspectRatio="none" role="img" aria-label="equity curve">
        <defs>
          <linearGradient id="equityFill" x1="0" x2="0" y1="0" y2="1">
            <stop offset="0%" stopColor="#2f855a" stopOpacity="0.28" />
            <stop offset="100%" stopColor="#2f855a" stopOpacity="0" />
          </linearGradient>
        </defs>
        <polyline className="area" points={`0,100 ${path} 100,100`} />
        <polyline className="line" points={path} />
      </svg>
      <div className="chartLabels">
        <span>{points[0]?.date}</span>
        <strong>{Math.round(values[values.length - 1]).toLocaleString()}</strong>
        <span>{points[points.length - 1]?.date}</span>
      </div>
    </div>
  );
}

function DrawdownChart({ points }: { points: DrawdownPoint[] }) {
  const values = points.map((point) => num(point.drawdownPct));
  if (!values.length) {
    return <div className="emptyChart compact">No drawdown data</div>;
  }
  const min = Math.min(...values, -1);
  const range = Math.abs(min) || 1;
  const path = values
    .map((value, index) => {
      const x = (index / Math.max(1, values.length - 1)) * 100;
      const y = 12 + (Math.abs(value) / range) * 72;
      return `${x.toFixed(2)},${y.toFixed(2)}`;
    })
    .join(" ");
  return (
    <div className="drawdownWrap">
      <div className="miniChartHeader">
        <span>Drawdown</span>
        <strong>{Math.min(...values).toFixed(2)}%</strong>
      </div>
      <svg viewBox="0 0 100 100" preserveAspectRatio="none" role="img" aria-label="drawdown curve">
        <line className="zeroLine" x1="0" x2="100" y1="12" y2="12" />
        <polyline className="drawdownArea" points={`0,12 ${path} 100,12`} />
        <polyline className="drawdownLine" points={path} />
      </svg>
    </div>
  );
}

function SideBadge({ side }: { side: Signal["side"] }) {
  return <span className={`sideBadge ${side.toLowerCase()}`}>{side}</span>;
}

function DecisionBadge({ decision }: { decision: TradeDecision }) {
  const label = decision.action === "SKIP" ? decision.signal : decision.action;
  const state = decision.action === "SKIP" ? "hold" : decision.action.toLowerCase();
  return (
    <span className={`sideBadge ${state}`} title={decision.accepted ? "accepted" : "blocked"}>
      {label}
    </span>
  );
}

function buildStrategyPlans(results: BacktestResult[], risk?: RiskData): StrategyPlan[] {
  const initialCash = num(risk?.initialCash ?? 0);
  return results
    .filter((result) => result.parameters.sourceLogic === "buy-dip-sell-peak")
    .map((result) => {
      const prices = result.priceCurve ?? [];
      const latest = prices[prices.length - 1];
      const previous = prices[prices.length - 2] ?? latest;
      const currentClose = num(latest?.close ?? 0);
      const previousClose = num(previous?.close ?? 0);
      const tierRatios = Array.isArray(result.parameters.tierRatios)
        ? result.parameters.tierRatios.map((item) => num(item))
        : [];
      const tierPct = tierRatios[0] ?? 0;
      const buyThresholdPct = numParam(result.parameters.buyThresholdPct);
      const sellThresholdPct = numParam(result.parameters.sellThresholdPct);
      const buyLimit = floorPrice(previousClose * (1 + buyThresholdPct / 100));
      const sellTrigger = floorPrice(previousClose * (1 + sellThresholdPct / 100));
      const sellTargetAfterBuy = floorPrice(buyLimit * (1 + sellThresholdPct / 100));
      const tierBudget = initialCash * tierPct;
      const tierQuantity = buyLimit > 0 ? Math.floor(tierBudget / buyLimit) : 0;
      let action: StrategyPlan["action"] = "HOLD";
      let actionReason = "current close is between buy dip and sell peak triggers";
      if (currentClose <= buyLimit) {
        action = "BUY";
        actionReason = "current close is at or below the buy-dip trigger";
      } else if (currentClose >= sellTrigger) {
        action = "SELL";
        actionReason = "current close is at or above the sell-peak trigger";
      }
      return {
        symbol: result.symbol,
        strategyName: result.strategyName ?? String(result.parameters.strategy ?? "strategy"),
        pro: String(result.parameters.pro ?? ""),
        action,
        actionReason,
        previousDate: previous?.date ?? "-",
        previousClose: String(previousClose),
        currentDate: latest?.date ?? "-",
        currentClose: String(currentClose),
        buyThresholdPct: String(buyThresholdPct),
        buyLimit: String(buyLimit),
        sellThresholdPct: String(sellThresholdPct),
        sellTrigger: String(sellTrigger),
        tierPct: String(tierPct * 100),
        tierBudget: String(tierBudget),
        tierQuantity: String(tierQuantity),
        sellTargetAfterBuy: String(sellTargetAfterBuy),
        stopLossDays: Math.trunc(numParam(result.parameters.stopLossDays)),
      };
    });
}

function numParam(value?: ParameterValue) {
  return Array.isArray(value) ? 0 : num(value);
}

function floorPrice(value: number) {
  return Math.floor(value * 100) / 100;
}

function parameterText(parameters: Record<string, ParameterValue>) {
  if (parameters.sourceLogic === "buy-dip-sell-peak") {
    return `${parameters.pro ?? ""} · buy ${parameters.buyThresholdPct ?? "-"}% · sell ${
      parameters.sellThresholdPct ?? "-"
    }% · stop ${parameters.stopLossDays ?? "-"}d`;
  }
  const shortWindow = parameters.shortWindow ?? "-";
  const longWindow = parameters.longWindow ?? "-";
  const rsiPeriod = parameters.rsiPeriod ?? "-";
  return `SMA ${shortWindow}/${longWindow}, RSI ${rsiPeriod}`;
}

function resultKey(result: BacktestResult) {
  return result.id ?? `${result.symbol}:${result.strategyName ?? result.parameters.strategy ?? "strategy"}`;
}

function formatDate(value: string) {
  return new Intl.DateTimeFormat("ko-KR", {
    month: "short",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  }).format(new Date(value));
}

function snapshotAgeLabel(value: string) {
  const hours = snapshotAgeHours(value);
  if (hours === null) {
    return "snapshot unknown";
  }
  if (hours < 1) {
    return "updated now";
  }
  if (hours < 48) {
    return `updated ${Math.round(hours)}h ago`;
  }
  return `updated ${Math.round(hours / 24)}d ago`;
}

function snapshotIsStale(value: string) {
  const hours = snapshotAgeHours(value);
  return hours === null || hours > 36;
}

function snapshotAgeHours(value: string) {
  const generatedAt = new Date(value).getTime();
  if (!Number.isFinite(generatedAt)) {
    return null;
  }
  return Math.max(0, (Date.now() - generatedAt) / 3_600_000);
}

function formatMoney(value: string | number, currency = "") {
  const amount = num(value);
  const suffix = currency ? ` ${currency}` : "";
  if (amount === 0) {
    return `0${suffix}`;
  }
  return `${Math.round(amount).toLocaleString()}${suffix}`;
}

function formatPrice(value: string | number) {
  const amount = num(value);
  if (amount >= 100) {
    return amount.toFixed(2);
  }
  return amount.toFixed(4).replace(/0+$/, "").replace(/\.$/, "");
}

function formatEntries(entries?: Record<string, string>) {
  if (!entries || Object.keys(entries).length === 0) {
    return "";
  }
  return Object.entries(entries)
    .map(([key, value]) => `${key} ${value}`)
    .join(", ");
}

function num(value?: string | number | null) {
  if (value === undefined || value === null) {
    return 0;
  }
  const parsed = Number(value);
  return Number.isFinite(parsed) ? parsed : 0;
}

function displayResult(result: BacktestResult) {
  if (result.symbol === "PORTFOLIO") {
    return "Portfolio";
  }
  return `${result.symbol} · ${result.strategyName ?? result.parameters.strategy ?? "strategy"}`;
}

function formatPct(value?: string | number) {
  return `${num(value ?? 0).toFixed(2)}%`;
}

function formatNumber(value?: string | number) {
  const parsed = num(value ?? 0);
  if (parsed >= 999) {
    return "∞";
  }
  return parsed.toFixed(2);
}

function maxDrawdown(points: EquityPoint[]) {
  let peak = num(points[0]?.equity ?? 0);
  let worst = 0;
  points.forEach((point) => {
    const equity = num(point.equity);
    peak = Math.max(peak, equity);
    if (peak > 0) {
      worst = Math.min(worst, (equity - peak) / peak);
    }
  });
  return Math.abs(worst) * 100;
}

function drawdownFromEquity(points: EquityPoint[]): DrawdownPoint[] {
  let peak = num(points[0]?.equity ?? 0);
  return points.map((point) => {
    const equity = num(point.equity);
    peak = Math.max(peak, equity);
    const drawdownPct = peak > 0 ? ((equity - peak) / peak) * 100 : 0;
    return { date: point.date, drawdownPct: String(drawdownPct) };
  });
}

function average(values: number[]) {
  if (!values.length) {
    return 0;
  }
  return values.reduce((sum, value) => sum + value, 0) / values.length;
}

function formatTime(value: Date) {
  return new Intl.DateTimeFormat("ko-KR", {
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
  }).format(value);
}

export default App;
