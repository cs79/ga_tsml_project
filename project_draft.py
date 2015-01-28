'''
Imports:
========

'''

from pandas import DataFrame, Series
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt #maybe
import time #maybe

'''
Declare some global variables:
==============================

slice_length:   a time slice length in minutes to be used to define the primary
                features of each observation

                try: 5, 10, 15 to start

prior_slices:   how many slices prior to the current slice to get summary stats
                for, to be included with the CURRENT slice as additional features

                try: 1, 3, 5, 7 to start

discount_wgt:   a factor by which to downweight prior_slices data

                try: 0.5, 0.3, 0.1 to start
                also probably read some literature on this to understand why /
                how to do it properly

mins_ahead:     how many minutes ahead to set known targets for each observation
                to train against (algos may do better at certain times ahead)

                try: 1, 2, 3 to start

'''

slice_length = 5
prior_slices = 3
discount_wgt = 0.5
mins_ahead = [1, 2, 3]

'''
Fetching and importing raw data:
================================

Max trailing days of tick data is 20 from Google Finance -- started collecting
full sets from January 8, 2015; can add forward from there and re-run generic
data cleaning pipeline and analysis.

Data are being captured for SPX (could try some others but this seems to be a
practical choice for a proof-of-concept like this... except for lack of volume data),
and are stored in /rawdata as .txt files.

Minute-tick data are being obtained from Google Finance for given tickers for a specified historical range using the following URL format to scrape for data:

http://www.google.com/finance/getprices?i=[PERIOD]&p=[DAYS]d&f=d,o,h,l,c,v&df=cpct&q=[TICKER]

* [PERIOD]: Interval/frequency in seconds (60 is the most granular that the data are available for)
* [DAYS]: Integer number of days back in time to fetch data for
* [TICKER]: A valid ticker symbol that you could search for on Google Finance

Saved data filename scheme is:
[Ticker]_[sequence number, starting at 001]_[Mon]_[Day]_[Year].txt
where the date is the start date for that file.

'''

# column format is constant for data fetched from this Google Finance API
cols = ['DATE', 'CLOSE', 'HIGH', 'LOW', 'OPEN', 'VOLUME']
#only have one file for right now so not worrying about splicing things together yet
raw_data = pd.read_table('rawdata/SPX_001_Jan_8_2015.txt', sep=',', header=6, names=cols)

'''
Cleaning the raw data:
======================
Tasks:
        - Separate based on the "date" header
        - Create a datetime index for the data
            - Convert from Unix epoch format where given
            -
        - Figure out which of the columns we want to do stuff with
            - At least one price, volume (probably), some range calculation based on H/L
        - Define graphical parameters (based on summary statistics of variance of slice_length windows over the dataset for max values)
        - Convert the slice_length windows into sparse matrices of data based on graphical parameters
        - Create a new dataframe with the following features:
            - prior_slices summary stats, discounted by discount_wgt
            - sparse matrix data for current slice
            - targets (one for each mins_ahead that can fit into current days' data)
'''

# to convert Unix Epoch stamps:
def convert_ts(stamp):
    stamp = int(stamp) # making sure
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stamp))

'''
TODO:   convert first marked epoch stamp (minus the leading 'a')
        fill down til the NEXT 'a' stamp, incrementing minute
        repeat for all 'a' stamps
        Re-index our dataframe to have a pandas timeseries index based on DATE column
'''

# quick graph for 1/28 progress report, basic exploration:

raw_data[['CLOSE', 'HIGH', 'LOW', 'OPEN']][10:30].plot()
plt.savefig('example_plot.png')

'''
Various cruft from earlier ideas:
=================================

Keeping these around for now, just in case...

dl_datestamp = time.strftime("%c")              # to datestamp downloads

raw_data.to_pickle('data/df_pickle')            # to maintain a static copy of
raw_data = pd.read_pickle('data/df_pickle')     # raw data as feeds change

'''
