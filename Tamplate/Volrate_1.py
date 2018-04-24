
# coding: utf-8

# In[3]:


def run_formula(dv, param = None):
    defult_param = {'t1': 1}
    if not param:
        param = defult_param
    Volrate =  dv.add_formula('Volrate', '-((VOL10/VOL60) > %s)'%(param['t1']), add_data = False, is_quarterly = False)
    return(Volrate)


# In[ ]:




