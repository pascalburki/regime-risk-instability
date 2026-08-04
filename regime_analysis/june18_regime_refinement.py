import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

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

portfolio_returns=log_returns[assets].mean(axis=1)

vol_10=log_returns['SPY'].rolling(window=10).std()*np.sqrt(252)
vol_20=log_returns['SPY'].rolling(window=20).std()*np.sqrt(252)
vol_60=log_returns['SPY'].rolling(window=60).std()*np.sqrt(252)
composite_vol=(vol_10+vol_20+vol_60)/3
bottom_30=composite_vol.quantile(0.30)
top_30=composite_vol.quantile(0.70)

raw_regime=pd.cut(
composite_vol,
bins=[-float('inf'),bottom_30,top_30,float('inf')], labels=['low','medium','high'])
regime_smoothed=raw_regime.copy()

for i in range(5,len(raw_regime)):
    window=raw_regime.iloc[i-5:i]
    if window.nunique()>1:
        regime_smoothed.iloc[i]=regime_smoothed.iloc[i-1]

changed=(raw_regime!=regime_smoothed)
print("Original regime counts:",raw_regime.value_counts())
print("Refined regime counts:",regime_smoothed.value_counts())
print("Days that changed classification:", changed.sum())

low_vol_dates=regime_smoothed[regime_smoothed=='low'].index
high_vol_dates=regime_smoothed[regime_smoothed=='high'].index

portfolio_high=portfolio_returns.loc[high_vol_dates]
portfolio_low=portfolio_returns.loc[low_vol_dates]

weighted_low=log_returns.loc[low_vol_dates].std().mean()*np.sqrt(252)
portfolio_vol_low=portfolio_low.std()*np.sqrt(252)
benefit_low=(weighted_low-portfolio_vol_low)/weighted_low

weighted_high=log_returns.loc[high_vol_dates].std().mean()*np.sqrt(252)
portfolio_vol_high=portfolio_high.std()*np.sqrt(252)
benefit_high=(weighted_high-portfolio_vol_high)/weighted_high

print("Refined diversification benefit low:", round(benefit_low,4))
print("Refined diversification benefit high:", round(benefit_high,4))

plt.figure(figsize=(12,6))
plt.plot(composite_vol)
plt.axhline(bottom_30,color='green')
plt.axhline(top_30,color='blue')
plt.xlabel('date')
plt.ylabel('composite vol')
plt.show()
