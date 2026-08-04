import numpy as np
import pandas as pd
import yfinance as yf

dfSPY=yf.download('SPY','2018-01-01','2023-12-31')
dfQQQ=yf.download('QQQ','2018-01-01','2023-12-31')
dfGLD=yf.download('GLD','2018-01-01','2023-12-31')
dfTLT=yf.download('TLT','2018-01-01','2023-12-31')
dfXOM=yf.download('XOM','2018-01-01','2023-12-31')

combined=pd.concat([
dfSPY["Close"],
dfQQQ["Close"],
dfGLD["Close"],
dfTLT["Close"],
dfXOM["Close"]
],axis=1)

combined.columns=['SPY','QQQ','GLD','TLT','XOM']
log_returns=np.log(
combined.dropna()/combined.dropna().shift(1)).dropna()

assets=['SPY','QQQ','GLD','TLT','XOM']

spy_20=log_returns['SPY'].rolling(window=20).std()*np.sqrt(252)
bottom_30=spy_20.quantile(0.30)
top_30=spy_20.quantile(0.70)

vol_regime=pd.cut(spy_20, bins=[-float('inf'),bottom_30,top_30,float('inf')], labels=['low vol','medium vol','high vol'])

low_vol_dates=vol_regime[vol_regime=='low vol'].index
high_vol_dates=vol_regime[vol_regime=='high vol'].index

portfolio_returns=log_returns[assets].mean(axis=1)
portfolio_low=portfolio_returns.loc[low_vol_dates]
portfolio_high=portfolio_returns.loc[high_vol_dates]
weighted_low=log_returns.loc[low_vol_dates].std().mean()*np.sqrt(252)
portfolio_vol_low=portfolio_low.std()*np.sqrt(252)

benefit_low=(weighted_low-portfolio_vol_low)/weighted_low*100
weighted_high=log_returns.loc[high_vol_dates].std().mean()*np.sqrt(252)
portfolio_vol_high=portfolio_high.std()*np.sqrt(252)

benefit_high=(weighted_high-portfolio_vol_high)/weighted_high*100
portfolio_mean_low=portfolio_low.mean()*252
portfolio_mean_high=portfolio_high.mean()*252

print("Portfolio mean return low vol:",round(portfolio_mean_low,4))
print("Portfolio mean return high vol:",round(portfolio_mean_high,4))

rf=0.04
sharpe_low=(portfolio_mean_low-rf)/(portfolio_low.std()*np.sqrt(252))
sharpe_high=(portfolio_mean_high-rf)/(portfolio_high.std()*np.sqrt(252))

print("Portfolio Sharpe low vol:",round(sharpe_low,4))
print("Portfolio Sharpe high vol:",round(sharpe_high,4))
print(f"low vol: return={round(portfolio_mean_low,4)}, vol={round(portfolio_vol_low,4)}, sharpe={round(sharpe_low,4)}, diversification benefit={round(benefit_low,2)}%")
print(f"high vol: return={round(portfolio_mean_high,4)}, vol={round(portfolio_vol_high,4)}, sharpe={round(sharpe_high,4)}, diversification benefit={round(benefit_high,2)}%")
