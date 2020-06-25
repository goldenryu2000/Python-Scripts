#!/usr/bin/env python
# coding: utf-8

# # Program To Get Top 3 Search Images from Snapdeal sorted By Popularity:)

# In[1]:


import requests as rq
import bs4


# In[2]:


a = input("Enter Term to be Searched: ")
url = "https://www.snapdeal.com/search?"
para = {
    "Keyword" : a ,
    "sort" : "plrty"
}
response = rq.get(url, params = para)
soup = bs4.BeautifulSoup(response.content) 

pict_attribute = soup.findAll('picture', {'class' : 'picture-elem'})
pict = pict_attribute[0]
for i , pict in enumerate(pict_attribute):
    if i<3:
        with open("Snapdeal-{}-{}.jpg" .format(a,i+1) , "wb") as file:
            pict_url = pict.img.attrs['src']
            response = rq.get(pict_url)
            file.write(response.content)
    else: 
        break


# In[ ]:





# In[ ]:




