
# coding: utf-8

# In[1]:


def run_formula(dv, param = None):
    defult_param = {'t1': 10, 't2': 40}
    if not param:
        param = defult_param
    Volume_adv40 = dv.add_formula('Volume_adv40', '-(Ts_Sum(volume, %s)/(Ts_Mean(volume, %s)))'%(param['t1'], param['t2']),  add_data = False, is_quarterly = False)
    return(Volume_adv40)


# In[ ]:




