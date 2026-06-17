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

corr_10=log_returns['SPY'].rolling(window=10).corr(log_returns['QQQ'])
corr_50=log_returns['SPY'].rolling(window=50).corr(log_returns['QQQ'])
corr_100=log_returns['SPY'].rolling(window=100).corr(log_returns['QQQ'])
static_corr=log_returns['SPY'].corr(log_returns['QQQ'])

print("10 day during COVID:", corr_10.loc['2020-02-15':'2020-04-15'].describe())
print("50 day during COVID: ", corr_50.loc['2020-02-15':'2020-04-15'].describe())
print("100 day during COVID:", corr_100.loc['2020-02-15':'2020-04-15'].describe())

plt.plot(corr_10,color='red',label='10 day window')
plt.plot(corr_50,color='blue',label='50 day window')
plt.plot(corr_100,color='purple',label='100 day window')
plt.axhline(static_corr,color='black',linestyle='--',label='static corr')
plt.xlabel('date')
plt.ylabel('correlation')
plt.legend()
plt.show()
