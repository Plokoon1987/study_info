#python -c "from sentdex_V08_and_09_Getting_Data_from_Internet_and_Conversion import bytespdate2num, graph_data; graph_data('prueba')"

import matplotlib.pyplot as plt
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
        # %Y = full year. 2015
        # %y = partial year. 15
        # %m = number month
        # %d = number day
        # %H = hours
        # %M = minutes
        # %S = seconds
        # 12-6-2014
        # %m-%d-%Y       
        converters={0 : bytespdate2num('%Y-%m-%d')})
  
    plt.plot_date(date, closep, '-', label='Close Price') # Use '-' to make plot_date as plot, as
                                                          # it seems to use scatter by default

    plt.xlabel('Date')
    plt.ylabel('Price')                
    plt.title('Interesting Graph\nCheck it out!!')
    plt.legend()
    plt.show()
    
graph_data('prueba')
