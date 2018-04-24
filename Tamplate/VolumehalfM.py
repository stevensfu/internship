
# coding: utf-8

# In[1]:


def run_formula(dv, param = None):
    defult_param = {'t1': 5, 't2': 30, 't3':30}
    if not param:
        param = defult_param
    VolumehalfM = dv.add_formula('VolumnhalfM', '-((12*(Ts_Sum(volume, %s)/Ts_Sum(volume, %s)))-1)*Return(close_adj, %s)'%(param['t1'], param['t2'], param['t3']),  add_data = False, is_quarterly = False)
    return(VolumehalfM)


# In[ ]:




