#!/usr/bin/env python
# coding: utf-8

# # 流程控制
# ## if else

# In[3]:


A=3
B=4
if A <= B:
    print("B為較大的數")
else:
    print("A為較大的數")


# ## for迴圈

# In[5]:


sum=0
for count in range(1,11,1):  # (初始值,終始值-1,間隔) #1 2 3 4 5 6 7 8 9 10
    sum += count
print(sum)


# In[6]:


sum=0
for count in range(1,11):  # (初始值,終始值-1) #1 2 3 4 5 6 7 8 9 10 (預設間隔為1)
    sum += count
print(sum)


# In[7]:


sum=0
for count in range(11):  # 精簡版
    sum += count
print(sum)


# In[9]:


mylist="for sratement"
for word in mylist:
    print(word)
else:
    print("end list")


# # 雞兔同籠，假設一個農場雞兔共有35頭，94隻腳，請問共有幾隻雞/兔?

# In[11]:


for chicken in range(0,35):
    rabbit = 35 - chicken
    if(2*chicken + 4*rabbit) == 94:
        print("雞有",chicken,"隻","兔子有",rabbit,"隻")
        break
else:
    print("無解")


# In[ ]:




