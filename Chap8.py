#!/usr/bin/env python
# coding: utf-8

# # 函數
# 
# ## 傳統的寫法

# In[1]:


import math
radius = int(input("請輸入圓的半徑："))
print("圓的面積為",radius * radius * math.pi)


# ### 面積計算函數

# In[3]:


# 自訂函數
import math
def circle_area(radius):
    area = math.pi * radius * radius
    return area

#呼叫自訂函數
print(circle_area(10))


# ### 函數多型

# In[5]:


# 定義一個可以計算面積，以及周長的函數
import math
def circle(radius, area = True):
    circle_area = math.pi * radius * radius
    circle_circum = 2* radius * math.pi
    if area == True:
        return circle_area
    else:
        return circle_circum
    
#呼叫函數
print(circle(10))         #傳回圓面積 
print(circle(10,False))  #傳回周長


# ### 交換排序法(Exchange Sort)

# In[7]:


import random

def exchange_sort(input_list):
    input_list_cloned = input_list
    for x in range(0, len(input_list)-1):
        for y in range(x+1, len(input_list)):
            if input_list_cloned[x] > input_list_cloned[y]:
                temp = input_list_cloned[x]
                input_list_cloned[x] = input_list_cloned[y]
                input_list_cloned[y] = temp
    return input_list_cloned

my_vector = random.sample(range(0,100), 10)  # 宣告名稱 = 亂數名稱.sample(range(初始值, 終使值(不含), 產生亂數個數))
print(my_vector)
print(exchange_sort(my_vector))


# ### 函數多回傳值

# In[10]:


def ironmen_stats(ironmen_list):
    max_ironmen = max(ironmen_list)
    min_ironmen = min(ironmen_list)
    len_ironmen = len(ironmen_list)
    sum_ironmen = sum(ironmen_list)
    return max_ironmen, min_ironmen, len_ironmen, sum_ironmen

ironmen = [58, 10, 21, 17, 32, 9]
max_ironmen, min_ironmen, ttl_groups, ttl_ironmen = ironmen_stats(ironmen)
print(" 最多: ",max_ironmen,"人\n","最少: ",min_ironmen,"人\n","總共: ",
      ttl_groups,"組\n","總共: ",ttl_ironmen,"人\n")


# In[ ]:




