import yfinance as yf
import pandas as pd
import numpy as np
msft = yf.Ticker("MSFT")

# get stock info
msft.info

sticker = np.asarray(['APPL' , 'MSFT' , 'TSLA'])

# get historical market data

for ss in sticker:
    data = yf.download(ss, start="2022-03-13", end="2022-03-23")
    columns = np.asarray(data.columns)
    fields = np.asarray(data.to_numpy() , dtype = 'float32')
    print(columns)
    print(data.to_numpy())

    frame = pd.DataFrame(fields , columns = columns )
    print("frame : ",frame)
    frame.to_csv(ss+'.csv')
