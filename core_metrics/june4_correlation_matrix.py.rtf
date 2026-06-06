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
 
# new: full correlation matrix + highest/lowest pair
corr_matrix = log_returns.corr()
print(corr_matrix.round(4))
 
corr_unstacked = corr_matrix.unstack()
corr_unstacked = corr_unstacked[corr_unstacked < 1.0]
highest_pair = corr_unstacked.idxmax()
lowest_pair = corr_unstacked.idxmin()
print("Highest correlation pair: ", highest_pair, round(corr_unstacked.max(), 4))
print("Lowest correlation pair: ", lowest_pair, round(corr_unstacked.min(), 4))
