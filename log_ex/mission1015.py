#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('input.csv', header=None)


# In[3]:


df2 = df[0].str.split('Sending' , expand = True)


# In[4]:


df3 = df2[0].str.split(',', expand = True)


# In[5]:


del df3[1]
del df3[2]
del df3[3]
del df3[4]
del df3[5]


# In[6]:


df3[1] = df2[1]


# In[7]:


df4 = df3.dropna(axis = 0, how = 'any')


# In[8]:


df5 = df4[df4[1].str.contains('date')]


# In[9]:


df5


# In[10]:


df5.to_csv('output.csv')


# In[ ]:




