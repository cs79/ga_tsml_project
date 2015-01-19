## imports

from pandas import DataFrame, Series
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt #maybe
import time

"""
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

"""

slice_length = 5
prior_slices = 3
discount_wgt = 0.5
mins_ahead = [1, 2, 3]

## fetch data -- try getting various days' back to suss out the max obtainable

raw_data = DataFrame()

#code to import .txt from google link as a DataFrame
dl_datestamp = time.strftime("%c") # just to keep track, as linked data will change

"""
Cleaning the raw data:
======================

Tasks:
        - Figure out how to separate based on the "date" header
        - Figure out what format the date headers are in (Unix Epoch ??)
        - Figure out which of the columns we want to do stuff with
            - At least one price, volume (probably), some range calculation based on H/L
        - Figure out if we can create a global index equivalent to datetime
            - Assuming we have the proper date format, and converting the minutes to time
            - If we have this, we can keep this as an ordered global index in new df
        - Define graphical parameters (based on summary statistics of variance of slice_length windows over the dataset for max values)
        - Convert the slice_length windows into sparse matrices of data based on graphical parameters
        - Create a new dataframe with the following features:
            - prior_slices summary stats, discounted by discount_wgt
            - sparse matrix data for current slice
            - targets (one for each mins_ahead that can fit into current days' data)

"""

# ok then
