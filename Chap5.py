#!/usr/bin/env python
# coding: utf-8

# ## Numpy套件

# In[2]:


a=[1, 2, 3, 4]
print(a*3)


# ## numpy套件的ndarray型態，提供element-wise的操作

# In[3]:


import numpy as np
b=np.array([1,2,3,4,5])
print(b*3)


# In[4]:


print(type(b))
print(b.ndim)  #ndarray的維度
print(b.shape) #ndarray的shape
print(b.dtype) #ndarray的資料型態


# In[7]:


print(np.zeros(6)) #產生六個元素均為0的一維array
print(np.zeros((3, 6))) #產生18個元素均為0的二維array
print(np.zeros((2, 6, 3)))


# In[8]:


a=np.zeros(16)
print(a)
print(a.shape)
b=a.reshape((4,4)) #改變資料的維度為4x4
print(b)
print(b.shape)


# ### ndarray的進階操作

# In[10]:


print(np.arange(11)) #產生一個 0~10 的一維陣列


# In[11]:


my_array=np.arange(10)
print(my_array)
print(my_array[0])
print(my_array[0:5]) #取 0, 1, 2, 3, 4位置的值


# In[12]:


a=np.array([[0,1,2,3,4],[5,6,7,8,9]])
print(a)
b=np.array([np.arange(0,5),np.arange(5,10)])
print(b)
c=np.array([np.arange(0,10).reshape(2,5)])
print(c)


# In[ ]:




