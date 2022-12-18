import pandas as pd
from matplotlib import pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf
from pandas_datareader import data
import yfinance as yf
yf.pdr_override()

start_date = '2000-01-01'
end_date = '2000-12-31'

sp500_data = data.get_data_yahoo('^GSPC', start_date, end_date)

sp500_weekly = sp500_data['Adj Close'].resample('W-MON')
sp500_weekly['return'] = sp500_weekly['Adj Close'].pct_change()


sp500_weekly.plot(y='return')
plt.show()