
# coding: utf-8

# In[1]:


def run_formula(dv, param = None):
    defult_param = {'t1': 1, 't2' : 32, 't3': 16, 't4':32}
    if not param:
        param = defult_param
    RET = dv.add_formula('RET', 'Return(close, %s)'%(param['t1']), add_data = True, overwrite= True, is_quarterly = False)
    alpha117 = dv.add_formula('alpha117', '((Ts_Rank(volume, %s))*(1-Ts_Rank(((close + high)-low), %s))*(1-Ts_Rank(RET, %s)))'%(param['t2'], param['t3'], param['t4']), add_data = False, is_quarterly = False)
    return(alpha117)


# In[ ]:




