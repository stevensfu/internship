
# coding: utf-8

# In[1]:


def run_formula(dv, param = None):
    defult_param = {'t1': 5, 't2':5}
    if not param:
        param = defult_param
    APBMA = dv.add_formula('APBMA_1', 'Ts_Mean(Abs(close_adj - Ts_Mean(close_adj, %s)), %s)'%(param['t1'], param['t2']), add_data = False, is_quarterly = False)
    return(APBMA)


# In[ ]:




