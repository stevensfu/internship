
# coding: utf-8

# In[3]:


import pandas as pd
import talib
def run_formula(dv, param = None):
    volume1 = dv.get_ts('volume').dropna(how = 'all', axis = 1)
    data1 = []
    for sec_symbols, value in volume1.iteritems():
        data1.append(sec_symbols)
    data2 = {}
    for sec_symbols, value in volume1.iteritems():
        data2[sec_symbols] = value.values
    EMA12_volume = pd.DataFrame({data1[i] : talib.EMA(data2[data1[i]], 12)for i in range(0, len(data1))}, index = volume1.index)
    EMA26_volume = pd.DataFrame({data1[i] : talib.EMA(data2[data1[i]], 26) for i in range(0, len(data1))}, index = volume1.index)
    
    dv.append_df(EMA12_volume,'EMA12_volume')
    dv.append_df(EMA26_volume,'EMA26_volume')
    VDIFF = dv.add_formula('VDIFF1', 'EMA12_volume - EMA26_volume ', add_data = False, is_quarterly = False)
    return(VDIFF)


# In[ ]:




