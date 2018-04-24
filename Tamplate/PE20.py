
# coding: utf-8

# In[1]:


def run_formula(dv, param = None):
    defult_param = {'t1': 20}
    if not param:
        param = defult_param
    PE20 = dv.add_formula('PE20', '-Ts_Rank(PE, %s)'%(param['t1']),  add_data = False, is_quarterly = False)
    return(PE20)


# In[ ]:




