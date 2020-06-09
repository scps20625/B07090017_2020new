#!/usr/bin/env python
# coding: utf-8

# In[8]:


class MyNumbers:
    def __init__(self):
        self.a = 1    
    def __iter__(self):
        return self    
    def __next__(self):
        x = self.a
        self.a += 1
        return x 
    
myclass = MyNumbers()

print(next(myclass))
print(next(myclass))
print(next(myclass))
print(next(myclass))
print(next(myclass))


# In[ ]:




