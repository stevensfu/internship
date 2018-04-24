
# coding: utf-8

# In[1]:


def run_formula(dv, param = None):
    defult_param = {'t1': 20}
    if not param:
        param = defult_param
    Std20 = dv.add_formula('Std20', '-StdDev(volume, %s)'%(param['t1']), add_data = False, is_quarterly = False)
    return(Std20)


# In[ ]:




