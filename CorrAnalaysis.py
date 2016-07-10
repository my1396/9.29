'''
@author: Linqi and Menghan
'''
import pandas as pd
import numpy as np
from scipy import stats
from readinpt import *

class corr_anlys(object):
    
    def __init__(self):
        self.df = read_data()
        self.tickernum = len(self.df.columns[1:-1]) # since 1st column is Date,
                                                    # last column is YM
                                         
    def comp_corr(self):
        '''
        compute monthly correlation coefficients 
        '''
        bygroup_ym = self.df.groupby(['YM'])
        cols_1 = pd.Series(['Date'])
        cols_2 = pd.Series(self.df.columns[2:-1]) 
        # cols_2 contains all the other competitors or companies for comparing
        cols = cols_1.append(cols_2)
        
        self.df_cor = pd.DataFrame(np.zeros((len(bygroup_ym),self.tickernum)),
                                   columns=cols)
        # excluding the origin company itself and plus the 'Date' column, 
        # the column dimension is the same as the total company numbers 
        
        i = 0
        for k in bygroup_ym.indices:
            self.df_cor.ix[i,'Date'] = k
            for comp in cols_2:
                corr_tmp, pvalue_tmp = stats.pearsonr(bygroup_ym.get_group(k)['PEP'], 
                                                   bygroup_ym.get_group(k)[comp])
                self.df_cor[comp] = self.df_cor[comp].astype(list)
                self.df_cor.set_value(i,comp, [corr_tmp,pvalue_tmp])
            i += 1
        
        self.df_cor['stdd'] = pd.to_datetime(self.df_cor['Date'],format='%Y%m')
        self.df_cor.sort_values('stdd', inplace=True)
        self.df_cor.index = range(len(self.df_cor))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    