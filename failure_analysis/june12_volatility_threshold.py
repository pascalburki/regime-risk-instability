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

real_vols=log_returns.std().values

corr_matrix=log_returns.corr()
corr_unstacked=corr_matrix.unstack()
corr_unstacked=corr_unstacked[corr_unstacked<1.0]
corr_avg=corr_unstacked.mean()

def build_cov_matrix(vols,corr):
    n=len(vols)
    cov=np.zeros((n,n))

    for i in range(n):
        for j in range(n):
            if i==j:
                cov[i,j]=vols[i]**2
            else:
                cov[i,j]=corr*vols[i]*vols[j]

    return cov

def portfolio_vol_from_cov(cov_matrix,weights):
    weights=np.array(weights)
    port_var=weights@cov_matrix@weights
    return np.sqrt(port_var)*np.sqrt(252)

equal_weights=[1/5]*5

vol_multipliers=np.linspace(1,5,100)
port_vols=[]

for v in vol_multipliers:
    multiplied_vols=real_vols*v
    cov=build_cov_matrix(multiplied_vols,corr_avg)
    port_vol=portfolio_vol_from_cov(cov,equal_weights)
    port_vols.append(port_vol)

spy_vol=log_returns['SPY'].std()*np.sqrt(252)

for multiplier,port_vol in zip(vol_multipliers,port_vols):
    if port_vol>0.50:
        print(f"vol multiplier: {round(multiplier,2)}")
        print(f"SPY annualized vol: {round(spy_vol*multiplier*100,2)}%")
        break

plt.plot(vol_multipliers,port_vols)
plt.axhline(y=0.50,color='red',linestyle='--')
plt.xlabel('Volatility Multiplier')
plt.ylabel('Portfolio Annualized Volatility')
plt.show()
