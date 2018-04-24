
# coding: utf-8

# In[1]:


def run_formula(dv, param = None):
    defult_param = {'t1': 5, 't2':5, 't3': 60, 't4' : 60}
    if not param:
        param = defult_param
    Volumn3M = dv.add_formula('Volumn3M', '((12*(Ts_Sum(volume, %s)/Ts_Mean(Ts_Sum(volume, %s), %s)))-1)*Return(close_adj, %s)'%(param['t1'], param['t2'], param['t3'], param['t4']),  add_data = False, is_quarterly = False)
    return(Volumn3M)


# In[ ]:




