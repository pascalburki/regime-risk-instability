# Regime-Based Risk Instability in Financial Markets

## What this project is
A system that analyzes how financial relationships (returns, volatility, 
and correlation) change across market regimes, and when diversification 
breaks under stress.

## Current status
Foundation complete (April–May 2026). Multi-asset system starting June 2026.

## Assets analyzed so far
JPM, XOM, GS, AAPL, MSFT, NVDA, TSLA, SPY

## Key findings so far
- Volatility is not constant, it ranges from 15% to 93% annualized for the 
  same asset depending on market regime
- Correlation between assets spikes during crises, JPM/XOM ranged from 
  -0.57 to 0.93 across 2018-2023
- Diversification benefit collapses from 4.31% to 1.19% when correlation 
  hits 0.95 and volatility triples simultaneously
- Static parameters describe no individual subperiod accurately

## Project structure
- Layer 1: Data foundation (June 2026)
- Layer 2: Core metrics engine (June 2026)
- Layer 3: Regime system (June 2026)
- Layer 4: Failure and instability analysis (July 2026)
- Layer 5: Final write-up and visualization (August 2026)

## findings so far (week 1)
SPY's mean daily return went from 0.0007 in low vol periods to -0.0001 in high vol periods. High vol doesn't just mean more risk, it also means lower or negative returns on average.
QQQ and XOM had a correlation of 0.1363 in low vol and jumped to 0.5187 in high vol. Assets that look unrelated in calm markets become correlated during stress, which means diversification breaks down exactly when you need it most.
QQQ and TLT correlation went from -0.0236 in low vol to -0.2450 in high vol. During a crisis investors sell stocks and move into bonds so the two assets move more strongly in opposite directions. This is called flight to safety.

## Core Finding
This system shows that diversification in a 5 asset portfolio is regime dependent. Under normal conditions the equal weight portfolio reduces risk by 44.6% compared to holding individual assets. Under stress conditions this drops to 33.0%. The primary driver of this reduction is not volatility but correlation. Diversification fails when uniform correlation exceeds 0.879. The portfolio's stress resilience depends almost entirely on TLT maintaining negative correlation with equities. Removing TLT drops high vol benefit from 33.0% to 19.5%. This conclusion holds as long as bonds continue to act as a flight to safety asset during equity stress.

## june 24 core finding
Diversification fails when correlation spikes towards 1. For example QQQ/XOM went from 0.1363 in calm periods to 0.5187 under stress and SPY/QQQ went from 0.8526 to 0.9508. This happens because one macro factor aligns equity assets while defensive assets like TLT sometimes still move in different directions. It is limited because this conclusion depends on TLT maintaining negative correlation with equities. Removing TLT dropped the high vol diversification benefit from 33% to 19.5%, showing that if bonds stop acting as a hedge the entire system breaks down. This happened in 2022 when rate hikes caused both equities and bonds to fall together.

## Failure Conditions
Diversification benefit drops below 20% when uniform correlation exceeds 0.545. Diversification collapses below 5% when correlation exceeds 0.879. Portfolio requires 3.83x volatility spike to breach 50% annualized vol threshold. Removing TLT nearly halves high vol diversification benefit from 33% to 19.5%.

## Contradictions and Limitations

The regime based finding is probabilistic, not deterministic. Individual 
days can contradict the regime average in both directions.

On April 16 2020, classified as high vol, diversification still worked 
extremely well. QQQ rose 1.81% while XOM fell 3.34% that day, and the 
opposite moves nearly cancelled each other out in the portfolio.

On May 22 2018, classified as low vol, diversification completely failed. 
All five assets including TLT moved down together that day. Since nothing 
diverged, nothing cancelled, and the portfolio moved just as much as the 
individual assets did.

This shows that regime labels describe a tendency across many days, not 
a guarantee for any single day. A portfolio manager that relies on the regime 
average alone could still get caught off guard on a specific low vol day 
where all assets happen to move together.

## Theory vs Reality

Theory assumes correlation stays stable, meaning one fixed number can describe the relationship between two assets. In reality, SPY/QQQ 20 day rolling correlation changed significantly, ranging from 0.41 to 0.99 between 2018 and 2023, a spread of 0.58 on a scale from negative 1 to 1.

Theory suggests diversification consistently reduces risk. In practice, diversification benefits fell from 44.6% during calm market conditions to 33.0% during stressed periods. TLT alone contributed 24% of the low volatility benefit and 41% of the high volatility benefit.

Theory treats volatility as the main source of risk. However, the results show diversification breaks down when correlation rises to 0.879 rather than because volatility itself increases. The failure point appears at a volatility multiplier of 1.0 once correlation becomes high enough.

Theory often assumes market returns follow a normal distribution. The data shows otherwise: SPY experienced events beyond 3 standard deviations on 1.53% of trading days compared to the normal prediction of 0.27%, making extreme outcomes almost six times more common than expected.

