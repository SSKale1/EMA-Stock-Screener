from typing import Counter
from matplotlib import colors
from numpy.core.fromnumeric import size
from yahoo_fin.stock_info import *
from datetime import date,datetime
import matplotlib.pyplot as plt


today=date.today()
ed_date=today.strftime("%m/%d/%Y")
m=today.month-3
if(m/10<1):
    m='0'+str(m)
st_date=str(m)+ed_date[2:]
ticker_list=['BAJAJ-AUTO.NS', 'BAJAJFINSV.NS', 'BAJFINANCE.NS', 'BHARTIARTL.NS', 'BRITANNIA.NS', 'CIPLA.NS', 'COALINDIA.NS', 'GRASIM.NS', 'HDFCLIFE.NS', 'HEROMOTOCO.NS', 'HINDALCO.NS', 'ICICIBANK.NS', 'INDUSINDBK.NS', 'ITC.NS', 'KOTAKBANK.NS', 'LT.NS']#, 'MARUTI.NS', 'M&M.NS', 'NESTLEIND.NS', 'NTPC.NS', 'ONGC.NS', 'RELIANCE.NS', 'SHREECEM.NS', 'TATACONSUM.NS', 'TATASTEEL.NS', 'TCS.NS', 'TECHM.NS', 'TITAN.NS', 'ULTRACEMCO.NS', 'WIPRO.NS']
#ticker_list=['IRCTC.NS', 'BAJAJFINSV.NS', 'BAJFINANCE.NS', 'BHARTIARTL.NS', 'BRITANNIA.NS', 'CIPLA.NS', 'COALINDIA.NS', 'GRASIM.NS', 'HDFCLIFE.NS', 'HEROMOTOCO.NS', 'HINDALCO.NS', 'ICICIBANK.NS', 'INDUSINDBK.NS', 'ITC.NS', 'KOTAKBANK.NS', 'LT.NS', 'MARUTI.NS', 'M&M.NS', 'NESTLEIND.NS', 'NTPC.NS', 'ONGC.NS', 'RELIANCE.NS', 'SHREECEM.NS', 'TATACONSUM.NS', 'TATASTEEL.NS', 'TCS.NS', 'TECHM.NS', 'TITAN.NS', 'ULTRACEMCO.NS', 'WIPRO.NS']

now=datetime.now()
historical_datas = {}
ema26={}
ema13={}
ema5={}

for ticker in ticker_list:
    historical_datas[ticker] = get_data(ticker, start_date = st_date, end_date = ed_date, index_as_date = True, interval='1d')
    ema26[ticker] = historical_datas[ticker]['close'].ewm(span=26).mean()
    ema13[ticker] = historical_datas[ticker]['close'].ewm(span=13).mean()
    ema5[ticker] = historical_datas[ticker]['close'].ewm(span=5).mean()
hist_dates=historical_datas['BAJAJ-AUTO.NS'].index

dates=[]

t=None
for d in hist_dates:
    tm=d.month
    td=d.day
    dates.append(str(td)+'/'+str(tm))

print('\ndates formatting complete\n')

plots=[]
for i in range(0,4):
    for j in range(0,4):
        plots.append(plt.subplot2grid((4, 4), (i, j)))   #Change HERE


for ticker in ticker_list:
    cur_plot=plots.pop()
    cur_plot.plot(dates, ema5[ticker], color='r', label='ema5')
    cur_plot.plot(dates, ema13[ticker], color='b', label='ema13')
    cur_plot.plot(dates, ema26[ticker], color='g', label='ema26')
    cur_plot.set_title(ticker)

plt.tight_layout()
plt.show()

