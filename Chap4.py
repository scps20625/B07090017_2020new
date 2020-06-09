#!/usr/bin/env python
# coding: utf-8

# # 第四招：Python物件
# 
# ## List：串列 [ ]
# 
# ## Tuple：不能更新串列 ( )
# 
# ## Dict：有鍵值(key)的串列 { }
# 
# ## List串列

# In[2]:


my_list = []
my_list1 = list()
my_list2 = ['python', 'js', 'SQL']
print(my_list)
print(my_list1)
print(my_list2)
print(my_list2[0])
print(my_list2[1])
print(my_list2[2])


# ### 附加於最後

# In[3]:


my_list2 = ['python', 'js', 'SQL']
my_list2.append('java') #append(附加)
print(my_list2[3])
#長度 Len()
print(len(my_list2))
print(len(my_list2[0]))


# ### 新增至特定位置

# In[4]:


my_list3 = ['python', 'js', 'SQL']
my_list3.insert(0, 'java')
print(my_list3)


# ### 刪除

# In[6]:


my_list4 = ['java', 'python', 'js', 'SQL']
del my_list4[0]
print(my_list4)
del my_list4[-1]
print(my_list4)


# ### 檢查是否存在

# In[7]:


my_list4 = ['java', 'python', 'js', 'SQL']
print('java' in my_list4)
print('go' in my_list4)


# ### 串列重複

# In[8]:


a=[1,2]
print(a*5)


# In[9]:


a=[1,2,3,4,5,6,7,8,9]
b=a[0:3] #範圍取值
print(b)
c=a[0:9:2] #間隔取值
print(c)
del a[7:9] #刪除串列某範圍的值
print(a)
print(min(a)) #串列最小值
print(max(a)) #串列最大值
print(a.index(1)) #1出現的索引位置
print(a.count(1)) #1出現的次數
a.reverse()
print(a)
a.sort() #串列排序
print(a)


# ## Tuple(元組)
# #### Tuple(元組)可視為不可改變的串列，tuple跟 list 很像，但我們 ' 不能新增，刪除或更新tuple的元數，tuple的好處有
# 
# #### 1. 占較少空間
# #### 2. 可當作dictionary(字典)的鍵值
# #### 3. 可當作函示引述

# In[10]:


a_tuple=('python','js','SQL')
print(a_tuple)
b_list=['go','c#','vb']
b_tuple=tuple(b_list)
print(b_tuple)
print(b_tuple[0])


# ## 字典(dictionary-dict)為帶有鍵值(key)的串列(list)

# In[13]:


languages = {}
languages = {'name':'python','version':'3.7'}
print(languages['name'])
print(languages['version'])
a={0:'python',1:'java',2:'SQL'}
print(a[0])
print(a[1])
print(a[2])
print(languages)
print(languages.keys())
print(languages.values())
print(languages.items())
print('name' in languages)


# In[16]:


a={'name':'python','version':'3.7'}
print(a)
b=a.copy()
print(b)
b.clear()
print(b)
print(a['name'])
print(a.get('name'))
a.update({'name':'java'})
print(a)


# 
