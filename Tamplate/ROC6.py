
# coding: utf-8

# In[1]:


def run_formula(dv, param = None):
    defult_param = {'t1': 6}
    if not param:
        param = defult_param
    ROC6 = dv.add_formula('ROC6_1', '((close_adj/Delay(close_adj, %s))-1)*100'%(param['t1']), add_data = False, is_quarterly = False)
    return(ROC6)


# In[ ]:




