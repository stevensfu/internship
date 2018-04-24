
# coding: utf-8

# In[3]:


def run_formula(dv, param = None):
    defult_param = {'t1': 120, 't2' : 30}
    if not param:
        param = defult_param
    Rank4 = dv.add_formula('Rank4', '-Ts_Rank(close_adj - Delay(close_adj, %s), %s)'%(param['t1'], param['t2']), add_data = False, is_quarterly = False)
    return(Rank4)


# In[ ]:




