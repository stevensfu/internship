
# coding: utf-8

# In[1]:


def run_formula(dv, param = None):
    defult_param = {'t1': 20}
    if not param:
        param = defult_param
    Rank3 = dv.add_formula('Rank3', '-1*Rank(open_adj - Delay(close_adj, %s))'%(param['t1']), add_data = False, is_quarterly = False)
    return(Rank3)


# In[ ]:




