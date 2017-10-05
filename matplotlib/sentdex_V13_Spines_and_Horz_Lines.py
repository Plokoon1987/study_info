#python -c "from sentdex_V12_Customization_of_Colors_and_Fills import bytespdate2num, graph_data; graph_data('prueba')"

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
  
    
    #***** AX1 *****
    
    # *** PLOT ***
    
    ax1.plot_date(date, closep, '-', label='Close Price') # Use '-' to make plot_date as plot, as
                                                          # it seems to use scatter by default
    ax1.plot([], [], linewidth=5, label='loss', color='r', alpha=0.5)
    ax1.plot([], [], linewidth=5, label='gain', color='g', alpha=0.5)   
    ax1.axhline(closep[-1], color='k', linewidth=3)
    ax1.fill_between(date, closep, closep[-1], where=(closep>closep[-1]), facecolor='g', alpha = 0.5)  
    # Plots 2 graphs in 1!! plot_date and fill. change colour or use alpha to see both plots
    # same colour is used by default otherwise
    ax1.fill_between(date, closep, closep[-1], where=(closep<closep[-1]), facecolor='r', alpha = 0.5)
    
    # ** AXIS AND GRIDS **
    
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    ax1.grid(True, color='g', linestyle='-', linewidth=1)
#    ax1.xaxis.label.set_color('c')
#    ax1.yaxis.label.set_color('r')
    ax1.set_yticks([0,25,50,75,150,300,450,600])
    
    # * Spines *
    ax1.spines['left'].set_color('c')
    ax1.spines['left'].set_linewidth(5)
    ax1.spines['right'].set_visible(False)
    ax1.spines['top'].set_visible(False)
    
    # * Ticks *
    ax1.tick_params(axis='x', colors='#f06215')  
    
    
    
    #***** PLT *****

    plt.xlabel('Date')
    plt.ylabel('Price')                
    plt.title('Interesting Graph\nCheck it out!!')
    plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
    plt.show()
    
graph_data('Prueba')
