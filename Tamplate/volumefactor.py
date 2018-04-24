
# coding: utf-8

# In[1]:


def run_formula(dv, param = None):
    defult_param = {'t1': 90, 't2' : 1}
    if not param:
        param = defult_param
    volumefactor = dv.add_formula('volumefactor', 'Log(Ts_Mean(volume, %s)/Delay(volume, %s))'%(param['t1'], param['t2']), add_data = False, is_quarterly = False)
    return(volumefactor)


# In[ ]:




