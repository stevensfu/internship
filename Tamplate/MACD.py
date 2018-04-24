
# coding: utf-8

# In[3]:


def run_formula(dv, param = None):
    MACD = dv.add_formula('MACD1', '(DIFF-DEA)*2', add_data = False, is_quarterly = False)
    return(MACD)

