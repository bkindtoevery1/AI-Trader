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
};

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
};

function App() {
  const [data, setData] = useState<DashboardData>(fallbackData);

  useEffect(() => {
    fetch(`${import.meta.env.BASE_URL}dashboard-data.json`)
      .then((response) => (response.ok ? response.json() : fallbackData))
      .then((payload: DashboardData) => setData(payload))
      .catch(() => setData(fallbackData));
  }, []);

  const best = useMemo(
    () => data.results.find((item) => item.symbol === data.summary.bestSymbol) ?? data.results[0],
    [data],
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
          <button className="navItem active" title="Overview">
            <BarChart3 size={18} />
            <span>Overview</span>
          </button>
          <button className="navItem" title="Risk">
            <ShieldCheck size={18} />
            <span>Risk</span>
          </button>
          <button className="navItem" title="Reports">
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
            <button className="iconButton" title="Refresh report" aria-label="Refresh report">
              <RefreshCw size={18} />
            </button>
            <button className="iconButton" title="Risk guard" aria-label="Risk guard">
              <ShieldCheck size={18} />
            </button>
            <button className="runButton" title="Dry-run mode">
              <Activity size={18} />
              <span>Dry Run</span>
            </button>
          </div>
        </header>

        <section className="metricGrid" aria-label="summary">
          <Metric icon={<Gauge />} label="Best Symbol" value={data.summary.bestSymbol} note="walk-forward target" />
          <Metric icon={<TrendingUp />} label="Return" value={`${num(data.summary.bestReturnPct).toFixed(2)}%`} note="sample backtest" />
          <Metric icon={<ShieldCheck />} label="Max DD" value={`${num(data.summary.maxDrawdownPct).toFixed(2)}%`} note="risk budget" />
          <Metric icon={<GitBranch />} label="Trades" value={String(data.summary.tradeCount)} note="daily review set" />
        </section>

        <section className="mainGrid">
          <section className="panel chartPanel">
            <div className="panelHeader">
              <div>
                <p className="eyebrow">Equity Curve</p>
                <h2>{best?.symbol ?? "Portfolio"}</h2>
              </div>
              <span className="timestamp">{formatDate(data.generatedAt)}</span>
            </div>
            {best ? <Sparkline points={best.equityCurve} /> : null}
          </section>

          <section className="panel">
            <div className="panelHeader">
              <div>
                <p className="eyebrow">Latest Signals</p>
                <h2>Orders</h2>
              </div>
              <span className="badge safe">Guarded</span>
            </div>
            <div className="signalList">
              {data.signals.map((signal) => (
                <article className="signalRow" key={signal.symbol}>
                  <div>
                    <strong>{signal.symbol}</strong>
                    <span>{signal.reason}</span>
                  </div>
                  <SideBadge side={signal.side} />
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
      </section>
    </main>
  );
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

function num(value: string | number) {
  const parsed = Number(value);
  return Number.isFinite(parsed) ? parsed : 0;
}

export default App;

