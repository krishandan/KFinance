import urllib.request


###
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
###





def grabQuandl(ticker):

    netIncomeAr = []
    revAr = []
    ROCAr = []
    
    
#     endLink = 'sort_order=asc'
    datacolumn = 'column_index=4'
    authkey = '&api_key=verQEVug7z8nVnKFfyxp'
    try:
        urlAttempt = 'https://www.quandl.com/api/v3/datasets/WIKI/'+ticker+'.json?'+datacolumn+authkey


        incomeDate, income = np.loadtxt(netIncomeAr, delimiter=',', unpack=True,
                                        converters={ 0: mdates.strpdate2num('%Y-%m-%d')})

    
        fig = plt.figure()
        ax1 = plt.subplot2grid((6,4), (0,0), rowspan=6, colspan=4)
        ax1.plot(incomeDate,income)
        plt.show()
        


    except (IOError, ValueError):
        print('An I/O error or a ValueError occurred')

grabQuandl('YHOO')