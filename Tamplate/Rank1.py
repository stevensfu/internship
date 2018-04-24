
# coding: utf-8

# In[1]:


def run_formula(dv, param = None):
    defult_param = {'t1': 5, 't2' : 5}
    if not param:
        param = defult_param
    Rank1 = dv.add_formula('Rank1', '-1*(Ts_Min(Rank(Corr(Rank(volume), Rank(close_adj), %s)), %s))'%(param['t1'], param['t2']), add_data = False, is_quarterly = False)
    return(Rank1)


# In[ ]:




