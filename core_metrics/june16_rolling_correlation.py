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

corr_20=log_returns['SPY'].rolling(window=20).corr(log_returns['QQQ'])
corr_60=log_returns['SPY'].rolling(window=60).corr(log_returns['QQQ'])
static_corr=log_returns['SPY'].corr(log_returns['QQQ'])

print("max 20 day corr:",round(corr_20.max(),4))
print("min 20 day corr:",round(corr_20.min(),4))
print("range 20:",round(corr_20.max()-corr_20.min(),4))
print("std 20:",round(corr_20.std(),4))

print("max 60 day corr:",round(corr_60.max(),4))
print("min 60 day corr:",round(corr_60.min(),4))
print("range 60:",round(corr_60.max()-corr_60.min(),4))
print("std 60:",round(corr_60.std(),4))

plt.plot(corr_20,color='red',label='20 day window')
plt.plot(corr_60,color='blue',label='60 day window')
plt.axhline(static_corr,color='black',linestyle='--',label='static corr')
plt.xlabel('date')
plt.ylabel('correlation')
plt.legend()
plt.show()
