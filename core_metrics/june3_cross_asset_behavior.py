
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
 
# setup (same as june1) 
dfSPY = yf.download('SPY', '2018-01-01', '2023-12-31')
dfQQQ = yf.download('QQQ', '2018-01-01', '2023-12-31')
dfGLD = yf.download('GLD', '2018-01-01', '2023-12-31')
dfTLT = yf.download('TLT', '2018-01-01', '2023-12-31')
dfXOM = yf.download('XOM', '2018-01-01', '2023-12-31')
 
SPY = dfSPY["Close"]
QQQ = dfQQQ["Close"]
GLD = dfGLD["Close"]
TLT = dfTLT["Close"]
XOM = dfXOM["Close"]
 
combined = pd.concat([SPY, QQQ, GLD, TLT, XOM], axis=1)
combined.columns = ['SPY', 'QQQ', 'GLD', 'TLT', 'XOM']
combined_raw = combined.dropna()
log_returns = np.log(combined_raw / combined_raw.shift(1)).dropna()
 
assets = ['SPY', 'QQQ', 'GLD', 'TLT', 'XOM']
years = ['2018', '2019', '2020', '2021', '2022', '2023']
rf = 0.04
 
# new: sharpe, skew, kurt, best/worst year 
for asset in assets:
    r = log_returns[asset]
    ann_mean = r.mean() * 252
    ann_vol = r.std() * np.sqrt(252)
    sharpe = (ann_mean - rf) / ann_vol
    best_year = max(years, key=lambda y: log_returns[asset].loc[y].mean())
    worst_year = min(years, key=lambda y: log_returns[asset].loc[y].mean())
    print(f"{asset}: mean={round(ann_mean,4)}, vol={round(ann_vol,4)}, sharpe={round(sharpe,4)}, skew={round(r.skew(),4)}, kurt={round(r.kurt(),4)}, best={best_year}, worst={worst_year}")
