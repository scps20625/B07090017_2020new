#!/usr/bin/env python
# coding: utf-8

# # Numpy 套件

# In[1]:


a=[1,2,3,4,5]
print(a*3)


# ## numpy套件的ndarray型態，提供element-wise的操作

# In[3]:


import numpy as np
b = np.array([1,2,3,4,5])
print(b*3)


# In[4]:


print(type(b))
print(b.ndim)  #ndarray的維度
print(b.shape) #ndarray的形狀
print(b.dtype) #ndarray的資料型態


# In[6]:


import numpy as np
print(np.zeros(6))   #產生1維度的陣列
print(np.zeros((3,6)))  #產生2維度的陣列
print(np.zeros((2,3,6)))  #產生3維度的陣列|


# In[7]:


a=np.zeros(16)
print(a)
print(a.shape)
b=a.reshape((4,4)) #改變資料的維度為4x4
print(b)
print(b.shape)


# ## ndarray的進階操作

# In[8]:


my_array=np.arange(10)
print(my_array)
print(my_array[0])
print(my_array[0:5])  #取0 1 2 3 4 的位置值


# In[12]:


a=np.array([[(0,1,2,3,4,)],[5,6,7,8,9]])
print(a)
b=np.array([np.arange(0,5),np.arange(5,10)])
print(b)
c=np.array([np.arange(0,10).reshape(2,5)])
print(c)


# ## 二維ndarray取值

# In[15]:


import numpy as np
my_2d_array=np.array(np.arange(0,10).reshape((2,5)))
print(my_2d_array) 
print(my_2d_array[0,:]) #第 0 列的元素  
print(my_2d_array[1,:]) #第 1 列的元素    
print(my_2d_array[:,0]) #第 0 欄的元素    
print(my_2d_array[1,1]) #取第 2 列 第 2 欄的元素    


# ## 假設六組"modern web","Devops","Big Data","cloud","Security"自我挑戰組 
# ## 參與人數分別為56 8 19 14 6 71

# In[16]:


import numpy as np
groups=["modern web","Devops","Big Data","cloud","Security","自我挑戰組"]
ironman=[56,8,19,14,6,71]
groups_array=np.array(groups)
ironman_array=np.array(ironman)
print(groups_array)
print(ironman_array)


# In[18]:


#用人數篩選組別
print(ironman_array >= 10)
print(groups_array[ironman_array >= 10])


# In[20]:


#用組別篩選組別
print(groups_array != "自我挑戰組")
print(ironman_array[groups_array != "自我挑戰組"])


# ### ndarray 空值 nan 無限大 int

# In[21]:


nan_array=np.array([56,8,19,14,6,np.nan])
print(nan_array)


# ## 生成10組標準常態(平均為0 標準差為1的常態變數) 

# In[23]:


normal_samples=np.random.normal(size=10)
print(normal_samples)


# ## 生成10組介於0~1的隨機變數

# In[25]:


uniform_samples=np.random.uniform(size=10)
print(uniform_samples)


# In[ ]:




