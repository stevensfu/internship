
# coding: utf-8

# In[1]:


def run_formula(dv, param = None):
    MA1 = dv.add_formula('MA1', '(MA20 - MA5)/MA5', add_data = False, is_quarterly = False)
    return(MA1)


# In[ ]:




