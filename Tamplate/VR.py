
# coding: utf-8

# In[2]:


def run_formula(dv, param = None):
    defult_param = {'t': 1, 't1': 24}
    if not param:
        param = defult_param
    
    BVS = dv.add_formula('BVS', 'Ts_Sum(If(close_adj<Delay(close_adj, %s), volume, 0), %s)'%(param['t'],param['t1']), add_data = True, is_quarterly = False)
    AVS = dv.add_formula('AVS', 'Ts_Sum(If(close_adj>Delay(close_adj, %s), volume, 0), %s)'%(param['t'],param['t1']), add_data = True, is_quarterly = False)
    CVS = dv.add_formula('CVS', 'Ts_Sum(If(close == Delay(close, %s), volume, 0), %s)'%(param['t'],param['t1']), add_data = True, is_quarterly = False)
    VR = dv.add_formula('VR1', '(AVS+CVS/2)/(BVS+CVS/2)', add_data = False, is_quarterly = False)
    return(VR)


# In[ ]:




