# v87 Intraday Opportunity Design

This is an outcome-informed Legacy50K development experiment, not independent
confirmation. No fitting, genetic algorithm, holdout opening or operational
change is authorized by this design. Earlier models and their outcomes remain
unchanged. The closed JSON policy is the executable authority.

## Question And Comparators

Following the user's pre-observation request, daily fill caps are one, three,
six and uncapped, separately on one NQ or up to six MNQ. The one-fill policies
are counted diagnostic comparators; the six remaining policies are eligible
for development nomination. All eight consume the same causal opportunity
stream. Every profile permits later signals after a cost/risk skip and the
same cooldown, including up_to1. Only actual filled-trade caps differ. Unlike
the superseded pre-observation first_attempt draft, a skipped first attempt
does not end up_to1. Limits are ceilings, never quotas. Uncapped has no daily
count stop, but retains time, cooldown, no-overlap and account-risk controls.
More fills do not imply more independent trading days.

The stream is the disjoint union of outside-close band reentry and inside-origin
wick rejection with unchanged quiet-volume, narrow-bandwidth and flat-slope
conditions. Decisions are completed minutes from 10:30 through 14:00 ET.
Features use 09:00 through 13:59 minute starts and only prior admitted days for
same-clock volume history. The target is the immutable completed NQ mean; ATR
defines the stop before entry. Actual explicit same-maturity NQ/MNQ ticks,
product commissions and adverse slippage remain separate.

The extended hours and family union mean comparisons with v86 are descriptive,
not an isolated frequency experiment. Only comparisons among the four fill
caps within v87 isolate the daily cap on a common opportunity stream. No rule is
selected after observing which frequency or cost mode performed best.

## Execution And Accounting

Four mandatory modes independently vary costs and entry latency. Entry occurs
at decision+60 seconds or decision+240 seconds. Every mode retains the same
absolute decision+5460-second exit. The original v86 stress control keeps its
original clock; its outcome is not relabeled. Cost/latency effects include any
changes in admissible entries and account paths, not merely a fee subtraction
on constant fills.

Each new decision must occur at least 300 seconds after the previous attempt
resolves: actual exit for a fill, first due entry tick for a skip. Signals
observed while busy are not queued for retroactive execution. Entry requires
a strictly positive planned target net of adverse exit slippage and both fees.
There is no additional profit threshold, learned strength score or bracket
update. Risk budgets are recalculated per attempt; PA MAE limits and scaling
permissions remain based on prior EOD. Hard/MAE breaches stop the day. Closed
Evaluation qualification stops further entries. Account lifecycle settlement
occurs once per unique trade date; payout and activity use aggregate daily PnL.

## Admission And Statistics

Freeze policy, implementation, synthetic tests, design, environment and source
metadata before new feature extraction. Then count only structural opportunity
dates among the 181 admitted raw dates. If fewer than 30 distinct dates have any
causal event, abort the whole catalog without outcome replay or retuning. This
is only an upper bound: future fills, costs and risk skips can reduce coverage.
Completed-bar profitability cannot establish an executable-coverage upper bound
because a later entry price can differ. Do not use that invalid shortcut.

A passing structural preflight reserves eight counted policies before any new
raw outcome replay: 13,061 inherited comparisons become 13,069. The four cost
modes are mandatory diagnostics, not selectable candidates. Failed or aborted
outcome runs retain their reservation. All results remain withheld until every
one of the 181 explicit-contract pairs is scanned and integrity checks finish.
617 minute sessions are development inputs; the final 48 dates remain sealed.

Daily return vectors count executed dates using trade_count > 0. Mixed long and
short days are active once, not flat and not two independent observations.
Nomination requires the main profile, at least 30 executed baseline dates,
baseline Sharpe >= 0.5, joint-stress Sharpe > 0, positive direct PnL in all four
modes, baseline HAC effective samples >= 84, family block-bootstrap p <= 0.2,
and baseline and joint-stress numeric Evaluation passes. Family bootstrap
includes all eight policies. Global HAC multiplicity uses 13,069; global DSR
remains unavailable. No historical screen is a verified model claim.

PA is reported separately, not removed: baseline and joint stress must each
survive PA, reach payout eligibility and have zero PA MAE violations for the
full-route development screen. Program fees, actual signal-service compliance,
final independent evidence and real liquidity remain unresolved. Passing code
tests or a structural gate is not a trading-performance pass.
