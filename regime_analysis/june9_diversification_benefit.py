import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

dfSPY = yf.download('SPY', '2018-01-01', '2023-12-31')
dfQQQ = yf.download('QQQ', '2018-01-01', '2023-12-31')
dfGLD = yf.download('GLD', '2018-01-01', '2023-12-31')
dfTLT = yf.download('TLT', '2018-01-01', '2023-12-31')
dfXOM = yf.download('XOM', '2018-01-01', '2023-12-31')

combined = pd.concat([dfSPY["Close"], dfQQQ["Close"], dfGLD["Close"], dfTLT["Close"], dfXOM["Close"]], axis=1)
combined.columns = ['SPY', 'QQQ', 'GLD', 'TLT', 'XOM']
combined_raw = combined.dropna()
log_returns = np.log(combined_raw / combined_raw.shift(1)).dropna()

assets = ['SPY', 'QQQ', 'GLD', 'TLT', 'XOM']

spy_20 = log_returns['SPY'].rolling(window=20).std() * np.sqrt(252)
bottom_30 = spy_20.quantile(0.30)
top_30 = spy_20.quantile(0.70)
vol_regime = pd.cut(spy_20, bins=[-float('inf'), bottom_30, top_30, float('inf')], labels=['low vol', 'medium vol', 'high vol'])

low_vol_dates = vol_regime[vol_regime == 'low vol'].index
high_vol_dates = vol_regime[vol_regime == 'high vol'].index

portfolio_returns = log_returns[assets].mean(axis=1)
portfolio_low = portfolio_returns.loc[low_vol_dates]
portfolio_high = portfolio_returns.loc[high_vol_dates]

# individual asset vol vs portfolio vol by regime
print("low vol regime: ")
for asset in assets:
    asset_vol = log_returns.loc[low_vol_dates][asset].std()*np.sqrt(252)
    print(f"asset vol: {round(asset_vol, 4)}")
print(f"portfolio vol: {round(portfolio_low.std()*np.sqrt(252), 4)}")

print("high vol regime: ")
for asset in assets:
    asset_vol = log_returns.loc[high_vol_dates][asset].std()*np.sqrt(252)
    print(f"asset vol: {round(asset_vol, 4)}")
print(f"portfolio vol: {round(portfolio_high.std()*np.sqrt(252), 4)}")

for asset in assets:
    low_asset_vol = log_returns.loc[low_vol_dates][asset].std() * np.sqrt(252)
    high_asset_vol = log_returns.loc[high_vol_dates][asset].std() * np.sqrt(252)
    print(f"{asset}: low vol gap: {round(low_asset_vol - portfolio_low.std()*np.sqrt(252), 4)}, high vol gap: {round(high_asset_vol - portfolio_high.std()*np.sqrt(252), 4)}")

# without TLT comparison
assets_no_tlt = ['SPY', 'QQQ', 'GLD', 'XOM']
portfolio_no_tlt = log_returns[assets_no_tlt].mean(axis=1)
portfolio_no_tlt_low = portfolio_no_tlt.loc[low_vol_dates]
portfolio_no_tlt_high = portfolio_no_tlt.loc[high_vol_dates]

weighted_no_tlt_low = log_returns.loc[low_vol_dates][assets_no_tlt].std().mean()*np.sqrt(252)
benefit_no_tlt_low = (weighted_no_tlt_low - portfolio_no_tlt_low.std()*np.sqrt(252)) / weighted_no_tlt_low * 100

weighted_no_tlt_high = log_returns.loc[high_vol_dates][assets_no_tlt].std().mean()*np.sqrt(252)
benefit_no_tlt_high = (weighted_no_tlt_high - portfolio_no_tlt_high.std()*np.sqrt(252)) / weighted_no_tlt_high * 100

print(f"low vol benefit without tlt: {round(benefit_no_tlt_low, 2)}%")
print(f"high vol benefit without tlt: {round(benefit_no_tlt_high, 2)}%")
