#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests as rq
import bs4


# In[3]:


a = input("Enter item to be searched: ")
n = int(input("Number of images (<=20): "))
if n<=20:
    url = "https://depositphotos.com/stock-photos/{}.html?filter=all" .format(a)
    response = rq.get(url)
    soup = bs4.BeautifulSoup(response.content)
    pict_attr = soup.find_all('img')
    pict = pict_attr[1]

    for i,pict in enumerate(pict_attr):
        if i==0:
            continue
        elif i<n+1:
            with open("{}-{}.jpg" .format(a,i),"wb") as file:
                pict_url = pict.attrs['src']
                response = rq.get(pict_url)
                file.write(response.content)
        else:
            break
else:
    print("Enter a Value Less than 20")
    


# In[ ]:





# In[ ]:




