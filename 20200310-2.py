#!/usr/bin/env python
# coding: utf-8

# # 第二章 Pythony資料表示運算
# # 註解
# 

# In[11]:


#多行註解
'''
第一行
第二行
'''

# 這是單行註解
a=3
b=5
print(a+b)


# In[ ]:


#兩數交換

#原本
x=1
y=10
z=x  #z=1
x=y  #x=10
y=z  #y=1
print(x)
print(y)


# In[4]:


#python的兩數交換(不用這麼複雜)
x=1
y=10
x,y=y,x
print(x)
print(y)


# In[6]:


x, y, z =3, 4, 5
print(x)
print(y)
print(z)


# In[7]:


x, y ,z = 3, 4, 5
x += 1
y *= 2
z **=3 # **= 相等於次方功能
print(x, y ,z )


# ## 變數的應用
# # Q:邊長為3,4,5之三角形，求面積?
# # s=(a+b+c / 2)  面積=s(s-a)(s-b)(s-c)^2

# In[9]:


import math
a, b, c = 3,4,5
s=(a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print(area)


# ## Python使用動態型態變數，變數使用前不需要宣告資料型態

# In[13]:


x=254
print(type(x))  #宣告資料型態
y='covid-19'
print(type(y))
print(id(x),id(y))  #變數的位置?


# ## 數值資料的計算
# ### 半徑為4.5，高度為4.5的圓錐體體面積為何?

# In[14]:


import math
print((4.5*4.5*math.pi*4.5)/3)


# In[17]:


x,y = 16, 3
print(x/y)  #求值
print(x//y) #求商
print(x%y)  #求餘數 


# # 關係運算

# In[19]:


print(20 == 20)  #判斷ture false
x, y = 10, 20
print(x == y)  
x = y
print(x)


# ## 級聯比較

# In[20]:


a, b, c = 10, 20, 30
print(a <= b <= c)


# In[21]:


x=3.141592627
print(x-3.14)


# ## 邏輯運算 閏年範例
# ### 四年一閏 百年不閏 四百年再閏

# In[22]:


y = 2020
print(y % 4 ==0 and y % 100 != 0 or y % 400 == 0)

y = 2000
print(y % 4 ==0 and y % 100 != 0 or y % 400 == 0)

y = 1998
print(y % 4 ==0 and y % 100 != 0 or y % 400 == 0)


# In[ ]:




