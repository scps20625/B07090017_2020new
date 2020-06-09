#!/usr/bin/env python
# coding: utf-8

# # Iterator
# 
# ## python的 iterator 允許物件進行分次處理
# 
# ## 通常會呼叫iter定義iterator物件，搭配next函式進行下一個值呼叫

# In[1]:


# 把參數全print出
mylist = [1, 2, 3, 4]
for i in mylist:
    print(i)


# In[3]:


# 把參數用對號入座方式print
mylist = [1, 2, 3, 4]
mylist_i = iter(mylist)
print(next(mylist_i))
print(next(mylist_i))
print(next(mylist_i))
print(next(mylist_i))


# ### 自訂iterator

# In[8]:


class MyNumbers:
    a = 1
    def __iter__(self):
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x
my_num = MyNumbers()
print(next(my_num))
print(next(my_num))
print(next(my_num))
print(next(my_num))
print(next(my_num))


# In[ ]:





# In[ ]:




