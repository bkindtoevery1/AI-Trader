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

type BacktestResult = {
  symbol: string;
  totalReturnPct: string;
  maxDrawdownPct: string;
  sharpe: string;
  tradeCount: number;
  equityCurve: EquityPoint[];
  parameters: Record<string, string | number>;
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
  parameters: Record<string, string | number>;
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

type DashboardData = {
  generatedAt: string;
  mode: string;
  status: string;
  summary: {
    symbols: string[];
    bestSymbol: string;
    bestReturnPct: string;
    tradeCount: number;
    maxDrawdownPct: string;
  };
  results: BacktestResult[];
  signals: Signal[];
  improvements: Improvement[];
  decisions?: TradeDecision[];
  risk?: RiskData;
  strategy?: StrategyData;
  execution?: ExecutionData;
};

type ViewMode = "overview" | "risk" | "reports";

const fallbackData: DashboardData = {
  generatedAt: "2026-06-22T00:00:00+09:00",
  mode: "dry-run",
  status: "ready",
  summary: {
    symbols: ["005930", "AAPL"],
    bestSymbol: "AAPL",
    bestReturnPct: "4.2",
    tradeCount: 3,
    maxDrawdownPct: "2.1",
  },
  results: [
    {
      symbol: "005930",
      totalReturnPct: "2.8",
      maxDrawdownPct: "1.9",
      sharpe: "1.21",
      tradeCount: 2,
      equityCurve: [
        { date: "2026-04-01", equity: "10000000" },
        { date: "2026-04-15", equity: "10082000" },
        { date: "2026-04-30", equity: "10154000" },
        { date: "2026-05-22", equity: "10280000" },
      ],
      parameters: { shortWindow: 5, longWindow: 20, rsiPeriod: 14 },
    },
    {
      symbol: "AAPL",
      totalReturnPct: "4.2",
      maxDrawdownPct: "2.1",
      sharpe: "1.46",
      tradeCount: 1,
      equityCurve: [
        { date: "2026-04-01", equity: "10000000" },
        { date: "2026-04-15", equity: "10110000" },
        { date: "2026-04-30", equity: "10290000" },
        { date: "2026-05-22", equity: "10420000" },
      ],
      parameters: { shortWindow: 5, longWindow: 20, rsiPeriod: 14 },
    },
  ],
  signals: [
    {
      symbol: "005930",
      side: "HOLD",
      score: 0.32,
      price: "77900",
      timestamp: "2026-05-22T00:00:00+09:00",
      reason: "no crossover; RSI=66.42",
    },
    {
      symbol: "AAPL",
      side: "HOLD",
      score: 0.41,
      price: "216.2",
      timestamp: "2026-05-22T00:00:00+09:00",
      reason: "no crossover; RSI=68.10",
    },
  ],
  improvements: [
    {
      title: "AAPL: SMA 8/30 검증",
      rationale: "최근 데이터에서 기준 전략 대비 낙폭 대비 수익률이 개선되었습니다.",
      expectedDeltaPct: "1.4",
      parameters: { shortWindow: 8, longWindow: 30, rsiPeriod: 14 },
    },
  ],
  decisions: [
    {
      symbol: "005930",
      signal: "HOLD",
      action: "SKIP",
      score: 0.32,
      price: "77900",
      quantity: "0",
      notional: "0",
      orderType: null,
      limitPrice: null,
      clientOrderId: null,
      accepted: true,
      reason: "hold signal",
      dryRun: true,
    },
    {
      symbol: "AAPL",
      signal: "HOLD",
      action: "SKIP",
      score: 0.41,
      price: "216.2",
      quantity: "0",
      notional: "0",
      orderType: null,
      limitPrice: null,
      clientOrderId: null,
      accepted: true,
      reason: "hold signal",
      dryRun: true,
    },
  ],
  risk: {
    initialCash: "10000000",
    currency: "KRW",
    maxPositionPct: "30",
    reserveCashPct: "15",
    maxOrderValue: "1000000",
    maxDailyOrders: 3,
    feeBps: "1.5",
    slippageBps: "5",
    allowLiveTrading: false,
  },
  strategy: {
    name: "ma-rsi-core",
    symbols: ["005930", "AAPL"],
    interval: "1d",
    candleCount: 120,
    shortWindow: 5,
    longWindow: 20,
    rsiPeriod: 14,
    rsiBuyBelow: "62",
    rsiSellAbove: "72",
  },
  execution: {
    mode: "dry-run",
    orderType: "LIMIT",
    priceOffsetBps: "10",
  },
};

function App() {
  const [data, setData] = useState<DashboardData>(fallbackData);
  const [activeView, setActiveView] = useState<ViewMode>("overview");
  const [selectedSymbol, setSelectedSymbol] = useState("PORTFOLIO");
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
      selectedSymbol === "PORTFOLIO"
        ? portfolio
        : data.results.find((item) => item.symbol === selectedSymbol) ?? portfolio,
    [data.results, portfolio, selectedSymbol],
  );
  const portfolioReturn = useMemo(
    () => num(portfolio.totalReturnPct).toFixed(2),
    [portfolio.totalReturnPct],
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

  const selectChart = (symbol: string) => {
    setSelectedSymbol(symbol);
    setStatusMessage(`${displaySymbol(symbol)} chart selected`);
  };

  const selectedSignal = useMemo(
    () => data.signals.find((signal) => signal.symbol === selectedSymbol),
    [data.signals, selectedSymbol],
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
          <strong>{data.summary.symbols.join(" / ")}</strong>
        </div>

        <section className="metricGrid" aria-label="summary">
          <Metric icon={<Gauge />} label="Universe" value={data.summary.symbols.join(" / ")} note="tracked symbols" />
          <Metric icon={<TrendingUp />} label="Portfolio" value={`${portfolioReturn}%`} note="combined backtest" />
          <Metric icon={<ShieldCheck />} label="Max DD" value={`${num(data.summary.maxDrawdownPct).toFixed(2)}%`} note="risk budget" />
          <Metric icon={<GitBranch />} label="Trades" value={String(data.summary.tradeCount)} note="daily review set" />
        </section>

        {activeView === "overview" ? (
          <section className="mainGrid">
          <section className="panel chartPanel">
            <div className="panelHeader">
              <div>
                <p className="eyebrow">Equity Curve</p>
                <h2>{displaySymbol(selectedChart.symbol)}</h2>
              </div>
              <span className="timestamp">{formatDate(data.generatedAt)}</span>
            </div>
            <div className="segmented" aria-label="chart symbol selector">
              {chartOptions.map((result) => (
                <button
                  key={result.symbol}
                  className={result.symbol === selectedChart.symbol ? "selected" : ""}
                  onClick={() => selectChart(result.symbol)}
                >
                  {result.symbol === "PORTFOLIO" ? "Portfolio" : result.symbol}
                </button>
              ))}
            </div>
            <Sparkline points={selectedChart.equityCurve} />
            {selectedSignal ? (
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
                <p className="eyebrow">Order Preview</p>
                <h2>Trade Plan</h2>
              </div>
              <span className="badge safe">Guarded</span>
            </div>
            <div className="signalList">
              {decisions.map((decision) => (
                <article className="signalRow" key={decision.symbol}>
                  <div>
                    <strong>{decision.symbol}</strong>
                    <span>{decision.reason} · {formatMoney(decision.notional)}</span>
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
                  <th>Return</th>
                  <th>Max DD</th>
                  <th>Sharpe</th>
                  <th>Trades</th>
                  <th>Parameters</th>
                </tr>
              </thead>
              <tbody>
                {data.results.map((result) => (
                  <tr key={result.symbol}>
                    <td>
                      <button className="tableButton" onClick={() => selectChart(result.symbol)}>
                        {result.symbol}
                      </button>
                    </td>
                    <td className={num(result.totalReturnPct) >= 0 ? "positive" : "negative"}>
                      {num(result.totalReturnPct).toFixed(2)}%
                    </td>
                    <td>{num(result.maxDrawdownPct).toFixed(2)}%</td>
                    <td>{num(result.sharpe).toFixed(2)}</td>
                    <td>{result.tradeCount}</td>
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
                  <strong>Strategy</strong>
                  <span>
                    {data.strategy?.name ?? "strategy"} · SMA {data.strategy?.shortWindow ?? "-"}
                    /{data.strategy?.longWindow ?? "-"} · RSI {data.strategy?.rsiPeriod ?? "-"}
                  </span>
                </article>
              </div>
            </section>
            <section className="panel">
              <div className="panelHeader">
                <div>
                  <p className="eyebrow">Order Preview</p>
                  <h2>Current Signals</h2>
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
                    <th>Return</th>
                    <th>Max DD</th>
                    <th>Sharpe</th>
                    <th>Trades</th>
                    <th>Parameters</th>
                  </tr>
                </thead>
                <tbody>
                  {data.results.map((result) => (
                    <tr key={result.symbol}>
                      <td>{result.symbol}</td>
                      <td className={num(result.totalReturnPct) >= 0 ? "positive" : "negative"}>
                        {num(result.totalReturnPct).toFixed(2)}%
                      </td>
                      <td>{num(result.maxDrawdownPct).toFixed(2)}%</td>
                      <td>{num(result.sharpe).toFixed(2)}</td>
                      <td>{result.tradeCount}</td>
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
      symbol: "PORTFOLIO",
      totalReturnPct: "0",
      maxDrawdownPct: "0",
      sharpe: "0",
      tradeCount: 0,
      equityCurve: [],
      parameters: {},
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
  return {
    symbol: "PORTFOLIO",
    totalReturnPct: String(totalReturnPct),
    maxDrawdownPct: String(maxDrawdown(equityCurve)),
    sharpe: String(average(results.map((result) => num(result.sharpe)))),
    tradeCount: results.reduce((sum, result) => sum + result.tradeCount, 0),
    equityCurve,
    parameters: {},
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

function parameterText(parameters: Record<string, string | number>) {
  const shortWindow = parameters.shortWindow ?? "-";
  const longWindow = parameters.longWindow ?? "-";
  const rsiPeriod = parameters.rsiPeriod ?? "-";
  return `SMA ${shortWindow}/${longWindow}, RSI ${rsiPeriod}`;
}

function formatDate(value: string) {
  return new Intl.DateTimeFormat("ko-KR", {
    month: "short",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  }).format(new Date(value));
}

function formatMoney(value: string | number, currency = "") {
  const amount = num(value);
  const suffix = currency ? ` ${currency}` : "";
  if (amount === 0) {
    return `0${suffix}`;
  }
  return `${Math.round(amount).toLocaleString()}${suffix}`;
}

function num(value: string | number) {
  const parsed = Number(value);
  return Number.isFinite(parsed) ? parsed : 0;
}

function displaySymbol(symbol: string) {
  return symbol === "PORTFOLIO" ? "Portfolio" : symbol;
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
