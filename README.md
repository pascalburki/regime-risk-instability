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
- Volatility is not constant — ranges from 15% to 93% annualized for the 
  same asset depending on market regime
- Correlation between assets spikes during crises — JPM/XOM ranged from 
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
