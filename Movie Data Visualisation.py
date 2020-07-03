#!/usr/bin/env python
# coding: utf-8

# ## Data Visualisation Challenge
# Given a movie dataset, your task is to make a visualisation of :
#     1. Plot the length of movie title names on X-axis
#     2. Frequency Counts on Y-axis,i.e, Number of movies having 'x' characters in their title.
#     

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv("movie_metadata.csv")


# In[3]:


titles = list(df.get('movie_title'))
#Now we make a dictionary to store the length(Key) and Frequency(value)
freq = {}
for title in titles:
    length = len(title)
    if freq.get(length) is None: #if that lenghth does not exist, we make it's frequency as 1
        freq[length]= 1
    else: #if that exists then we raise the count by 1
        freq[length]+=1


# In[4]:


X = np.array(list(freq.keys()))
Y = np.array(list(freq.values()))


# In[6]:


plt.figure(figsize=(10,10))
plt.style.use('seaborn')
plt.xlabel('Length of Title')
plt.ylabel('Frequency')
plt.scatter(X,Y)
plt.show()


# In[ ]:




