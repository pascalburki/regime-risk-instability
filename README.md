# Regime-Based Risk Instability in Financial Markets

**Summary:** This project looks at how the correlation and volatility of assets change across market regimes, and why diversification stops working under stress. The main finding: once the correlation between all assets goes above 0.879, the diversification benefit falls below 5%, no matter how high the volatility is. So correlation, not volatility on its own, is the main reason diversification fails. In real data, correlations moved toward that level during actual stress periods (the 2022 rate-hike shock and COVID-19).

## Assets

SPY, QQQ, GLD, TLT and XOM, daily data, 2018-2023 (1,509 trading days).

## Main finding

Diversification only works while assets react to different things: QQQ to tech earnings, XOM to oil prices, TLT to interest rate expectations. When no single force dominates, these differences let the assets partly cancel each other out. When one big force hits, like a pandemic, a rate shock or a financial crisis, all assets react to that same thing at once, and the independence diversification needs disappears. Two separate results support this, and I keep them apart:

**Theoretical stress test:** when I raise a single correlation for all pairs from 0 to 1, the diversification benefit falls below 5% once the correlation passes 0.879, at any level of volatility.

**What happened in real data:** in 2022, during the rate-hike shock, real correlations moved toward that range. QQQ/XOM rose from 0.1363 to 0.5187, and SPY/QQQ from 0.8526 to 0.9508. At the same time, the diversification benefit fell from 44.6% to 33.0%, a 26% drop.

Volatility alone doesn't explain the failure. Once correlation is high enough, the failure point is already reached at a volatility multiplier of 1.0. So volatility only matters because high-volatility periods usually come with rising correlation, not as a cause on its own. TLT gives the portfolio most of its remaining protection: removing it drops the diversification benefit in high-volatility periods from 33% to 19.5%, so TLT alone provides about 41-42% of it. That is why the portfolio is fragile. It depends on TLT moving opposite to stocks, and that broke down in 2022, when rate hikes made stocks and bonds fall together.

## When it fails

- The diversification benefit drops below 20% once the correlation passes 0.545
- It collapses below 5% once the correlation passes 0.879
- The portfolio needs a 3.83x volatility spike to reach 50% annual volatility on its own
- Removing TLT almost halves the diversification benefit in high-volatility periods (33% to 19.5%)

## Theory vs. reality

- **Stable correlation:** theory assumes correlation stays roughly the same. In reality, SPY/QQQ's 20-day rolling correlation went from 0.41 to 0.99 over 2018-2023, a swing of 0.58 on a scale from -1 to 1.
- **Reliable diversification:** theory says diversification always lowers risk. In practice, the benefit fell from 44.6% in calm periods to 33.0% under stress.
- **Volatility as the main risk:** the data shows diversification fails when correlation passes 0.879, not just because volatility rises. The failure point shows up at a volatility multiplier of 1.0 once correlation is already high.
- **Normal returns:** SPY moved more than 3 standard deviations on 1.53% of days, while a normal distribution predicts 0.27%. That is almost 6 times more often than theory predicts.

## Exceptions and limitations

The regime finding is about averages, not every single day. Some days go against it, in both directions:

- **April 16, 2020 (a high-volatility day):** diversification still worked. QQQ rose 1.81% while XOM fell 3.34%, and they almost cancelled out in the portfolio.
- **May 22, 2018 (a low-volatility day):** diversification failed completely. All five assets, including TLT, went down together, so nothing cancelled out.

## Three weaknesses

1. **It depends on the period.** The 0.879 level comes from 2018-2023 data. A different period, like 2000-2006 or 2010-2016, could give a different number.
2. **It depends on TLT.** The portfolio needs TLT to move opposite to stocks, and that broke down in 2022. If higher interest rates become normal, TLT might stop protecting the portfolio even in calm periods.
3. **Equal weights.** The portfolio puts 20% in each asset. An optimized portfolio, like a minimum-variance one, might push the 0.879 level higher. I haven't tested that, so my conclusion may be more pessimistic than a smarter allocation would give.

## Related work

This project defines regimes with volatility thresholds I set by hand. A follow-up project, K-Means Market Regime Detection, tests whether clustering finds similar regimes directly from the data.

## Project structure

- Layer 1, data foundation: complete
- Layer 2, core metrics: complete
- Layer 3, regime system: complete
- Layer 4, failure and instability analysis: complete
- Layer 5, final write-up and visualization: complete

## How I worked

I chose the project, the questions and what to test, ran the code and checked the results. I used an AI tutor (Claude) to help me learn the methods and to debug the code.
