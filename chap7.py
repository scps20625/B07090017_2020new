#!/usr/bin/env python
# coding: utf-8

# # pandas載入檔案
# ## 本地端載入csv檔案
# ### iris(鳶尾花)資料集
# ### sepal (花萼),petal(花瓣)
# ![iris](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Machine+Learning+R/iris-machinelearning.png)
#  

# In[11]:


import pandas as pd
iris_df=pd.read_csv('iris.csv')
iris_df.head()


# ## 雲端載入csv檔案

# In[12]:


url="https://raw.githubusercontent.com/shhuangmust/python/master/iris.csv"
iris_df=pd.read_csv(url)
iris_df.head()


# ## 雲端載入excel檔案

# In[13]:


url="https://github.com/shhuangmust/python/raw/master/iris.xlsx"
iris_df=pd.read_excel(url)
iris_df.head()


# ## superstore超級商店範例

# In[21]:


url="https://raw.githubusercontent.com/shhuangmust/python/master/superstore.csv"
superstore_df=pd.read_csv(url,encoding="big5")
superstore_df.head()


# ## superstore的資訊

# In[24]:


superstore_df.info()


# In[32]:


st1=superstore_df[['Sales','Quantity','Profit']]
st1.describe()


# # 交易獲利率最高的金額為何

# In[34]:


superstore_df['Profit'].max()


# # 獲利最高前1000筆資料，其平均獲利為和

# In[46]:


st2= superstore_df.sort_values(by='Profit')
#st2.head()#獲利資料由小排到大。要找獲利最高的前1000筆資料，要從後面開始找起
st2.iloc[-1000:]['Profit'].mean() #獲利最高的錢1000筆，其平均獲利是310.485698


# # 單筆總交易金額最高為何

# In[47]:


superstore_df.groupby(by='Order ID').sum()['Sales'].max()


# In[ ]:




