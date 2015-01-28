## Data Exploration and Analysis Plan
### Alex Lee
### January 28, 2015

#### Data Gathering

I have 20 days' worth of minute-tick data for the S&P 500 index (SPX), and Apple stock as a backup as SPX doesn't have volume data.  

These data have five features: Open, High, Low, and Close price, as well as Volume.

Data were gathered from a Google Finance API that allows for fetching up to 20 days' worth of historical data, so more can be added to the raw dataset every day (or every minute, if desired).  Assuming analysis of 10-minute sliding windows, the data gathered so far are enough to represent 7,900 observations.

I've done some quick graphical explorations of the data, and they appear to have suitable variation for the purposes of my project approach.  See example_plot.png for a quick visualization of SPX price movements over a 20-minute window.

The data are fairly clean as they come from an API; I still need to reformat the date (given as Unix epoch time and then incremental offsets, for each day) into a uniform datetime index across all of the data.  Additionally, I need to generate appropriate features from the data (generating new sliding window observations instead of using the raw data).  

I believe that I will be able to answer my question with these data.  I will continue to gather more data, to hopefully improve the performance of learning algorithms, but believe even 7,900 observations will be sufficient.

There may be an issue with my matrix of observations being non-invertible if I cannot compactly represent sparse pixel features generated from visual analysis of the data, so I am keeping in mind that an alternative approach (but one based on similar analytic principles) may be necessary.

I will use predictive modeling to try to classify target movements (categorically, rather than exactly, as exact prediction seems unfeasible and unlikely to be particularly more useful than classification).  I will try various types of binning (since my target is still quantitative), as well as various "distances to target" to see if the model performs better for nearer-term predictions (which I would expect, but am not sure of).
