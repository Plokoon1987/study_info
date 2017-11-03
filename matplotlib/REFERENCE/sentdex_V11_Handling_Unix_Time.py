#python -c "from sentdex_V11_Handling_Unix_Time import graph_data; graph_data('prueba')"
# Note: This won't work as url does nost contain unix time for date

import matplotlib.pyplot as plt
import numpy as np
import urllib
import datetime as dt

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
        unpack=True)
        
    dateconv = np.vectorize(dt.datetime.fromtimestamp)
    
    date = dateconv(date)
         
    
    #***** AX1 *****
    
    ax1.plot_date(date, closep, '-', label='Close Price') # Use '-' to make plot_date as plot, as
                                                          # it seems to use scatter by default
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    ax1.grid(True, color='g', linestyle='-', linewidth=5)
    
    #***** PLT *****

    plt.xlabel('Date')
    plt.ylabel('Price')                
    plt.title('Interesting Graph\nCheck it out!!')
    plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
    plt.show()
    
graph_data('prueba')
    
''' 
    # To Practice Unix Time
    
    >>> import datetime as dt
    >>> import time

    >>> print(time.time())
    1505976540.858439

    >>> print(time.time())
    1505976544.7470746

    >>> exampletime = time.time()
    >>> print(exampletime)
    1505976585.6980221
    
    >>> print(dt.datetime.fromtimestamp(exampletime))
    2017-09-21 08:49:45.698022
    
    >>> import numpy as np
    >>> dateconv = np.vectorize(dt.datetime.fromtimestamp)
'''
