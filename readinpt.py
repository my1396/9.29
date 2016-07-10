'''
@author Linqi and Menghan
'''
import pandas as pd
import numpy as np

def read_data():
    '''
    read daily price data from excel file
    extract Year and Month info in order to group and sort
    assume the origin company is at the 1st column, 
    other companies are at the following columns
    '''
    df = pd.read_excel("comp_price.xlsx",sheetname="price",index_col=None)
    # add one new column including Year and Month info
    # so that we could group the data by Year and Month
    # to get the monthly correlation coefficients
    df['YM'] = ""
#     print "{:d}-{:d}".format(df['Date'][0].year,df['Date'][0].month)
    for i in range(len(df)):
        df.loc[i,'YM'] = "{:d}{:02d}".format(df.loc[i,'Date'].year,df.loc[i,'Date'].month)
    
    return df

# test code for successfully reading the date
# df = read_data()
# cols_1 = pd.Series(['Date'])
# cols_2 = pd.Series(df.columns[2:-1])
# cols = cols_1.append(cols_2)
# for item in cols:
#     print item


