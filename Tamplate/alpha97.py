
# coding: utf-8

# In[4]:


def run_formula(dv, param = None):
    defult_param = {'t1': 10}
    if not param:
        param = defult_param
    
    t = param['t1']
    alpha97 = dv.add_formula('alpha97', 'StdDev(volume, %s)'%(t), add_data = False, is_quarterly = False)
    return(alpha97)


# In[ ]:




