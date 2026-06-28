# Regime Based Risk Instability in Financial Markets

## What This Project Is

A system that analyzes how financial relationships, returns, volatility, 
and correlation, change across market regimes and when diversification 
breaks under stress.

## Assets

SPY, QQQ, GLD, TLT, XOM across 2018 to 2023.

## Core Finding

Diversification only works until correlations start moving together. For 
this 5 asset portfolio the breaking point is correlation 0.879. Above 
this level diversification benefit falls below 5% regardless of 
volatility. During stress periods QQQ/XOM correlation jumped from 0.1363 
to 0.5187 and SPY/QQQ rose from 0.8526 to 0.9508, causing 
diversification benefit to drop from 44.6% to 33.0%, a 26% decline. 
Volatility is not the trigger. The failure threshold occurs at vol 
multiplier 1.0 when correlation is high enough. TLT drives 42% of the 
high vol benefit. Removing it drops protection from 33% to 19.5%. The 
system breaks completely when correlation exceeds 0.879 and TLT stops 
hedging, exactly what happened in 2022 when rate hikes caused stocks and 
bonds to fall together.

## Failure Conditions

Diversification benefit drops below 20% when uniform correlation exceeds 
0.545. Diversification collapses below 5% when correlation exceeds 
0.879. Portfolio requires 3.83x volatility spike to breach 50% 
annualized vol threshold. Removing TLT nearly halves high vol 
diversification benefit from 33% to 19.5%.

## Theory vs Reality

Theory assumes correlation stays stable. In reality SPY/QQQ 20 day 
rolling correlation ranged from 0.41 to 0.99 between 2018 and 2023, a 
swing of 0.58 on a scale from negative 1 to 1.

Theory suggests diversification consistently reduces risk. In practice 
benefit fell from 44.6% in calm periods to 33.0% under stress. TLT 
alone contributed 24% of low vol benefit and 41% of high vol benefit.

Theory treats volatility as the main risk driver. The results show 
diversification breaks down when correlation hits 0.879, not because 
volatility increases. The failure threshold appears at vol multiplier 
1.0 when correlation is already high enough.

Theory assumes returns follow a normal distribution. SPY had beyond 3std 
events on 1.53% of days versus the normal prediction of 0.27%, nearly 
6x more frequent.

## Contradictions and Limitations

The regime finding is probabilistic not deterministic. Individual days 
can contradict the regime average in both directions.

On April 16 2020, classified as high vol, diversification still worked 
extremely well. QQQ rose 1.81% while XOM fell 3.34% and the opposite 
moves nearly cancelled each other out in the portfolio.

On May 22 2018, classified as low vol, diversification completely 
failed. All five assets including TLT moved down together. Since nothing 
diverged nothing cancelled and the portfolio moved just as much as 
individual assets.

## Three Weaknesses

The 0.879 correlation threshold is based on 2018 to 2023. A different 
time period could produce a different threshold. Running the system on 
2000 to 2006 or 2010 to 2016 might show a completely different failure 
point.

The system depends on TLT maintaining negative correlation with equities. 
This broke down in 2022 when rate hikes caused stocks and bonds to fall 
together. If rising rates become the normal environment TLT stops being 
a hedge and the diversification benefit collapses even in calm periods.

The portfolio uses equal weights, 20% per asset. A minimum variance 
portfolio with optimized weights might push the 0.879 failure threshold 
higher. My conclusion could be overly pessimistic because I never tested 
whether smarter weights extend the system's resilience.

## Project Structure

Layer 1: Data foundation, complete
Layer 2: Core metrics engine, complete
Layer 3: Regime system, complete
Layer 4: Failure and instability analysis, complete
Layer 5: Final write-up and visualization, August 2026
