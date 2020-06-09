#!/usr/bin/env python
# coding: utf-8

# In[3]:


x=12
print(type(x))
y=float(x)+0.5
print(type(y))
print(int('123'))
print(float('123'))
print(int(123.333))

x=10*3.25  #32.5
y=200*200  #4000
s='The value of x is ' + str(x) + 'and y is ' + str(y)  #str轉成字串型態
print(s)
print('The value of x is {} and y is {}'.format(x,y))   #型態轉換


# ## 非內置模組

# In[8]:


import math
print(math.pi)
print(math.pow(2,3))
print(8.3*10.58*math.sin(37.0/180*math.pi)/2)
print(math.sqrt(25))


# # 圓面積

# In[9]:


import math
r=input("請輸入半徑：")
area=float(r)*float(r)*math.pi
print('圓面積為：', area)


# In[ ]:




