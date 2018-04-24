
# coding: utf-8

# In[1]:


def run_formula(dv, param = None):
    defult_param = {'t1': 1, 't2' : 1, 't3': 1, 't4' : 20}
    if not param:
        param = defult_param
    Cor1 = dv.add_formula('Cor1', '-Corr(Delta(Log(volume),%s),(close_adj-Delay(close_adj, %s))/Delay(close_adj, %s), %s)'%(param['t1'], param['t2'], param['t3'], param['t4']), add_data = False, is_quarterly = False)
    return(Cor1)


# In[ ]:




