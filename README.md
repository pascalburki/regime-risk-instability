# Regime-Based Risk Instability in Financial Markets

Summary: A system analyzing how correlation and volatility between assets shift across market regimes, and why portfolio diversification breaks down under stress. Core finding: above a uniform correlation of 0.879, diversification benefit collapses below 5%, regardless of volatility — correlation, not volatility on its own, is the primary driver of diversification failure. Empirically, real cross-asset correlations moved toward this range during actual stress periods (2022 rate-hike shock, COVID-19).

# Assets

SPY, QQQ, GLD, TLT, XOM, daily data, 2018–2023 (1,509 trading days).

# Core Finding

Diversification only works while assets respond to different underlying factors — QQQ to tech earnings, XOM to oil prices, TLT to rate expectations. When no single macro force dominates, these differing sensitivities let assets partially cancel each other out. When one overwhelming force hits (a pandemic, a rate shock, a financial crisis), all assets respond to that same factor simultaneously, and the independence that diversification depends on disappears.
Two separate results support this, and it's worth keeping them distinct:

Theoretical stress test: sweeping a uniform correlation assumption from 0 to 1 across the portfolio shows diversification benefit falls below 5% once correlation exceeds 0.879, regardless of volatility level.
Empirical observation: in real 2022 data, actual asset-pair correlations moved toward this range during the rate-hike shock — QQQ/XOM correlation rose from 0.1363 to 0.5187, and SPY/QQQ rose from 0.8526 to 0.9508. This coincided with diversification benefit dropping from 44.6% to 33.0%, a 26% decline.

Volatility alone doesn't explain the failure: the theoretical failure threshold occurs at a volatility multiplier of just 1.0 once correlation is high enough — meaning volatility matters only insofar as high-vol periods tend to co-occur with rising correlation, not as an independent trigger.
TLT is the single largest driver of the portfolio's remaining protection: removing it drops the high-volatility diversification benefit from 33% to 19.5% — TLT alone accounts for roughly 41-42% of the benefit in high-volatility regimes. This is exactly why the system is fragile: it depends on TLT maintaining negative correlation with equities, which broke down in 2022 when rate hikes caused stocks and bonds to fall together.

# Failure Conditions

Diversification benefit drops below 20% once uniform correlation exceeds 0.545
Diversification collapses below 5% once uniform correlation exceeds 0.879
The portfolio needs a 3.83x volatility spike to breach a 50% annualized volatility threshold on its own
Removing TLT nearly halves the high-volatility diversification benefit (33% → 19.5%)

# Theory vs. Reality

Correlation stability: Theory assumes correlation is roughly stable. In reality, SPY/QQQ's 20-day rolling correlation ranged from 0.41 to 0.99 over 2018–2023 — a swing of 0.58 on a scale from −1 to 1.
Diversification consistency: Theory suggests diversification reliably reduces risk. In practice, benefit fell from 44.6% in calm periods to 33.0% under stress.
Volatility as the main risk driver: The data shows diversification breaks down when correlation crosses 0.879, not simply because volatility rises — the failure threshold appears at a volatility multiplier of 1.0 once correlation is already elevated.
Normality of returns: SPY had returns beyond 3 standard deviations on 1.53% of days, versus a normal distribution's predicted 0.27% — nearly 6x more frequent than theory predicts.

# Contradictions and Limitations

The regime finding is probabilistic, not deterministic — individual days can and do contradict the regime-level average in both directions:

April 16, 2020 (classified high-volatility): diversification still worked well. QQQ rose 1.81% while XOM fell 3.34%, nearly cancelling out in the portfolio.
May 22, 2018 (classified low-volatility): diversification failed completely. All five assets, including TLT, moved down together — nothing diverged, so nothing cancelled.

# Three Weaknesses

Period dependency. The 0.879 threshold is derived from 2018–2023 data. A different period (e.g., 2000–2006, 2010–2016) could produce a different failure point.
TLT dependency. The system relies on TLT holding a negative correlation with equities — a relationship that broke down in 2022. If a higher-rate environment becomes the norm, TLT may stop hedging even in calm periods, and the diversification benefit could collapse regardless of regime.
Equal-weighting assumption. The portfolio uses equal 20% weights per asset. A minimum-variance or optimized-weight portfolio might push the 0.879 failure threshold higher; this hasn't been tested, so the conclusion may be more pessimistic than a smarter allocation would produce.

# Related Work
This project defines regimes using manually-set volatility thresholds. A follow-up project, K-Means Market Regime Detection, tests whether unsupervised clustering identifies similar regime boundaries directly from the data, without manual thresholds.

# Project Structure

Layer 1 — Data foundation: complete
Layer 2 — Core metrics engine: complete
Layer 3 — Regime system: complete
Layer 4 — Failure and instability analysis: complete
Layer 5 — Final write-up and visualization: in progress (August 2026)
