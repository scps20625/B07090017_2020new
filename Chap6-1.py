#!/usr/bin/env python
# coding: utf-8

# # Chap6-1:DataFrame loc,iloc
# ### DataFrame比numpy ndarry(element-wise)提供資料統整的功能
# ### DataFrame通常為二維資料
# ### 橫的為列(索引index)，直的為屬(columns)

# In[10]:


# 隨機產生DataFrame資料

import numpy as np
import pandas as pd
frame=pd.DataFrame(np.random.rand(6,6),index=list('abcdef'),
                     columns=list('ABCDEF'))
frame


# # loc用欄位來找出DataFrame的資料
# # iloc用索引來找出DataFrame的資料

# In[11]:


frame.describe()


# In[12]:


frame.loc['a','A']


# In[15]:


# 取前兩列的對應資料
frame.loc['a':'b',:]


# In[17]:


# 取前兩欄的對應資料
frame.loc[:,'A':'B']


# In[21]:


# 取特殊列、欄的資料
frame.loc[['a','c'],:]


# In[25]:


# 取特殊列、欄的資料
print(frame.loc[['a','c'],:])
print(frame.loc[:,['A','C']])
print(frame.loc[['a','d'],['A',"D"]])


# In[30]:


frame


# # iloc是利用列索引與欄索引進行資料定位，都是從0開始

# In[37]:


frame.iloc[0,0]


# In[32]:


# 取前兩列的資料
frame.iloc[0:2,:]


# In[33]:


# 取前兩列、兩欄之資料
frame.iloc[0:2, 0:2]


# In[38]:


# 取特殊列、欄的資料
print(frame.iloc[[0,2],:])
print(frame.iloc[:,[0,2]])
print(frame.iloc[[0,3],[0,3]])


# # Chap6

# In[40]:


# Chap6 的 請複製過去!!!!!
import numpy as np
import pandas as pd
groups = ["Modern Web","DevOps",np.nan,"Big Data","Security","自我挑戰組"]
ironmen = [59,9,19,14,6,np.nan]


# In[41]:


# Chap6 的 請複製過去!!!!!
import numpy as np
import pandas as pd
groups = ["Modern Web","DevOps",np.nan,"Big Data","Security","自我挑戰組"]
ironmen = [59,9,19,14,6,np.nan]
ironmen_dict = {"group":groups,"ironmen":ironmen}
ironmen_df=pd.DataFrame(ironmen_dict)
# print(ironmen_df)
print(ironmen_df.loc[:,"group"].isnull())
print(ironmen_df.loc[:,"ironmen"].notnull())


# In[42]:


# Chap6 的 請複製過去!!!!!
print(ironmen_df.group[ironmen_df.loc[:,"group"].isnull()])
print(ironmen_df.ironmen[ironmen_df.loc[:,"group"].notnull()])


# In[45]:


print(ironmen_df)
ironmen_df_dropped = ironmen_df.dropna() #刪除遺失值
print(ironmen_df_dropped)
ironmen_df_filled = ironmen_df.fillna(0)
print(ironmen_df_filled)
ironmen_df_fillvalue = ironmen_df.fillna({"group":"Cloud","ironmen":71})
print(ironmen_df_fillvalue)


# In[ ]:




