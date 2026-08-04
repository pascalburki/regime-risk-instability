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

vol_10=log_returns['SPY'].rolling(window=10).std()*np.sqrt(252)
vol_20=log_returns['SPY'].rolling(window=20).std()*np.sqrt(252)
vol_50=log_returns['SPY'].rolling(window=50).std()*np.sqrt(252)


print("Max 20-day vol:",round(vol_20.max(),2))
print("Min 20-day vol:",round(vol_20.min(),2))
print("Ratio:",round(vol_20.max()/vol_20.min() ,2))


plt.plot(vol_10,color='blue',label='10 day window')
plt.plot(vol_20,color='red',label='20 day window')
plt.plot(vol_50,color='green',label='50 day window')
plt.axhline(log_returns['SPY'].std()*np.sqrt(252),color='black',label='static line',linestyle='--')
plt.xlabel('date')
plt.ylabel('vol')
plt.legend()
plt.show()
