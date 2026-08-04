import numpy as np
import pandas as pd
import yfinance as yf

dfSPY=yf.download('SPY','2018-01-01','2023-12-31')
dfQQQ=yf.download('QQQ','2018-01-01','2023-12-31')
dfGLD=yf.download('GLD','2018-01-01','2023-12-31')
dfTLT=yf.download('TLT','2018-01-01','2023-12-31')
dfXOM=yf.download('XOM','2018-01-01','2023-12-31')

SPY=dfSPY["Close"]
QQQ=dfQQQ["Close"]
GLD=dfGLD["Close"]
TLT=dfTLT["Close"]
XOM=dfXOM["Close"]

combined=pd.concat([SPY,QQQ,GLD,TLT,XOM],axis=1)
combined.columns=['SPY','QQQ','GLD','TLT','XOM']
combined_raw=combined.dropna()
log_returns=np.log(combined_raw/combined_raw.shift(1)).dropna()

assets=['SPY','QQQ','GLD','TLT','XOM']

spy_20=log_returns['SPY'].rolling(window=20).std()*np.sqrt(252)
bottom_30=spy_20.quantile(0.30)
top_30=spy_20.quantile(0.70)

vol_regime=pd.cut(spy_20, bins=[-float('inf'),bottom_30,top_30,float('inf')], labels=['low vol','medium vol','high vol'])

low_vol_dates=vol_regime[vol_regime=='low vol'].index
high_vol_dates=vol_regime[vol_regime=='high vol'].index

portfolio_returns=log_returns[assets].mean(axis=1)
portfolio_high=portfolio_returns.loc[high_vol_dates]
portfolio_low=portfolio_returns.loc[low_vol_dates]

daily_asset_avg_move=log_returns.loc[high_vol_dates][assets].abs().mean(axis=1)
daily_portfolio_move=portfolio_high.abs()
protection_ratio=daily_portfolio_move/daily_asset_avg_move
best_protection_days=protection_ratio.nsmallest(5)

print("Days with strongest diversification protection within high vol regime:")
print(best_protection_days)

daily_asset_avg_move_low=log_returns.loc[low_vol_dates][assets].abs().mean(axis=1)
daily_portfolio_move_low=portfolio_low.abs()
protection_ratio_low=daily_portfolio_move_low/daily_asset_avg_move_low
worst_protection_days=protection_ratio_low.nlargest(5)

print("Days with weakest diversification protection within low vol regime:")
print(worst_protection_days)
print(log_returns.loc['2020-04-16'])
print(log_returns.loc['2018-05-22'][assets])
print(log_returns.loc[low_vol_dates][assets].abs().mean(axis=1).nsmallest(10))
