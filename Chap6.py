#!/usr/bin/env python
# coding: utf-8

# ## Pandas Data Frame
# ### ．Pandas 是 Python 常用的數據分析函式庫，2009年底，提供高效能、簡易使用的資料格式(Data Frame)讓使用者可以快速操作及分析資料
# 
# ### ．在異質數據的讀取、轉換何處理上，都讓分析人員更容易處理，例如：從列、欄資料中找到想要的值
# 
# ### ．Pandas 提供 DataFrame則是用來處理結構化(Table like)的資料，例如：關聯式資料庫、CSV等等。透過載入至Pandas的資料結構物件後，可以透過結構化所提供的方法，來快速地進行資料的前處理，如：資料補植，空值去除或取代等。
# 
# 

# In[1]:


import pandas as pd


# In[3]:


groups = ["Modern Web", "DevOps", "Cloud", "Big Data", "Security", "自我挑戰"]
ironmen = [59, 9, 19, 14, 6, 77]
ironmen_dict = {"groups":groups, "ironmen":ironmen}
ironmen_df = pd.DataFrame(ironmen_dict)
ironmen_df


# In[4]:


print(ironmen_df.sum())       #計算鐵人---總人數
print(ironmen_df.mean())      #計算鐵人---平均人數
print(ironmen_df.median())    #計算鐵人---中位數
print(ironmen_df.describe())  #計算鐵人---統計


# In[8]:


import numpy as np
groups = ["Modern Web", "DevOps", np.nan, "Big Data", "Security", "自我挑戰組"]
ironmen = [59, 9, 19, 14, 6, np.nan]
ironmen_dict = {"groups":groups, "ironmen":ironmen}
ironmen_df = pd.DataFrame(ironmen_dict)
print(ironmen_df)
print("-----------------------------")
print(ironmen_df.loc[:, "groups"].isnull())
print("-----------------------------")
print(ironmen_df.loc[:, "ironmen"].notnull())


# In[10]:


ironmen_df.groups[ironmen_df.loc[:, "groups"].isnull()] = "不知道名字組"
ironmen_df.ironmen[ironmen_df.loc[:, "ironmen"].notnull()] += 10
ironmen_df


# In[ ]:




