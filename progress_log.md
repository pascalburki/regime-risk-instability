## May 31 2026
- Created repository structure
- Uploaded May 7 clean architecture script to data_foundation
- Uploaded May 4 stress testing script to failure_analysis
- Ready to start multi-asset system June 1
## June 1 2026
- Built 5-asset data foundation: SPY, QQQ, GLD, TLT, XOM
- 2018-2023 aligned dataset, 1509 trading days
- Most volatile asset: XOM (0.3256 annualized)
- Most stable asset: GLD (0.1421 annualized)
- Misalignment test: broken correlation differed by up to 0.0339 points
- Script: data_foundation/june1_multi_asset_foundation.py
## June 2 2026
- Tested forward fill vs drop missing on 5-asset dataset
- Vol changed by up to 5.53% between cleaning methods
- Correlation changed by 0.0339 points between cleaning methods
- Key finding: data cleaning decisions are not neutral
- Script: data_foundation/june2_data_sensitivity.py
## June 3 2026
- Extended cross-asset comparison with Sharpe, skewness, kurtosis, yearly vol
- Most volatile: XOM 32.6% annualized
- Most stable: GLD 14.2% annualized  
- Key finding: TLT had negative mean return -1.68% annualized over 2018-2023
- Worst Sharpe: TLT at -0.344
- Best Sharpe: QQQ at 0.500
- Data cleaning changed vol by up to 5.5%, correlation by up to 0.034 points
- Script: core_metrics/june3_cross_asset_behavior.py
## June 4 2026
- Added full correlation matrix and highest/lowest pair identification
- Highest correlation pair: SPY-QQQ (0.9331) — equity assets move together
- Lowest correlation pair: TLT-XOM (-0.2734) — bonds vs energy diverge
- Script: core_metrics/june4_correlation_structure.py
## June 5 2026
- Defined volatility regimes on SPY: low (bottom 30%), medium, high (top 30%)
- Low vol threshold: 0.1095 annualized, High vol threshold: 0.1961 annualized
- Volatility ranges from 0.1095 to 0.1961 across regimes
- High vol regime mean return: -0.0001, Low vol mean return: 0.0007
- Key finding: returns are nearly 7x higher in low vol vs high vol regimes
- Script: regime_analysis/june5_regime_definition.py
## June 6 2026
- Computed correlation matrix by volatility regime
- Low vol correlation range: -0.2784 to 0.8526
- High vol correlation range: -0.3043 to 0.9508
- Largest increase in stress: QQQ-XOM pair, from 0.1363 to 0.5187 (+0.3824)
- Largest decrease in stress: QQQ-TLT pair, from -0.0236 to -0.2450 (-0.2215)
- Key finding: correlations rise sharply in high vol causing diversification to break down when you need it most
- Script: regime_analysis/june6_correlation_by_regime.py
## June 7 2026
- Code cleanup: split all scripts into standalone files by layer
- Updated README with Findings So Far section
## June 8 2026
- Built equal weight portfolio across 5 assets: SPY QQQ GLD TLT XOM
- Diversification benefit in low vol: 44.6%
- Diversification benefit in high vol: 33.0%
- Benefit reduction under stress: 26%
- Key finding: TLT's negative correlation drives large overall benefit
- But benefit still shrinks under stress confirming correlation clustering
- Script: regime_analysis/june8_portfolio_regimes.py
## June 9 2026
- Measured individual asset vol vs portfolio vol by regime
- Biggest diversification contributor: XOM (gap of 0.1461 in low vol, 0.2453 in high vol)
- Benefit with all 5 assets: 44.6% low vol, 33.0% high vol
- Benefit without TLT: 33.87% low vol, 19.5% high vol
- TLT adds ~11% diversification benefit in low vol and ~13.5% in high vol
- Script: regime_analysis/june9_diversification_benefit.py
## June 10 2026
- Tested diversification benefit across uniform correlation 0 to 1
- Benefit drops below 20% at correlation = 0.545
- Real portfolio benefit: 33-44% depending on regime
- Script: failure_analysis/june11_correlation_threshold.py
