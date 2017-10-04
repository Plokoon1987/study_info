#python -c "from sentdex_V14_Candlestick_OHLC import bytespdate2num, graph_data; graph_data('prueba')"

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc # finance.py will be removed, mpl_finance will have to be installed

import numpy as np
import urllib
import matplotlib.dates as mdates

def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    
    return bytesconverter


def graph_data(stock):
    fig = plt.figure()  # figure exists by default, to modify it you have to reference it
    ax1 = plt.subplot2grid((1,1), (0,0)) # First tuple = Shape of Grid, Second tuple = Starting point
    
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    
    source_code = urllib.request.urlopen(stock_price_url).read().decode()

    stock_data = []
    
    split_source = source_code.split('\n')
    
    
    for line in split_source:
        split_line = line.split(',')
        
        if len(split_line) == 7:
            if 'Date' not in line:
                stock_data.append(line)

    date, openp, highp, lowp, closep, adj_closep, volume = np.loadtxt(
        stock_data,
        delimiter=',',
        unpack=True,
        converters={0 : bytespdate2num('%Y-%m-%d')})
    
    
    # ***** CANDLESTICK *****    
    x = 0
    y = 10  # or len(date)
    ohlc = []
    
    while x < y:
        append_me = date[x], openp[x], highp[x], lowp[x], closep[x], adj_closep[x], volume[x]
        ohlc.append(append_me)
        x +=1
    
    candlestick_ohlc(ax1, ohlc, width=0.4, colorup='#77d879', colordown='#db3f3f')
    
    # **** LABELS ****
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
    ax1.grid(True)
    
    
    #***** PLT *****

    plt.xlabel('Date')
    plt.ylabel('Price')                
    plt.title('Interesting Graph\nCheck it out!!')
    plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
    plt.show()
    
graph_data('Prueba')
