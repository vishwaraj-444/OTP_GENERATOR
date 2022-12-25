#!/usr/bin/env python
# coding: utf-8

# In[24]:


# OTP GENERATOR
import random
numbers=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ,
 '1', '2', '3', '4', '5', '6', '7', '8', '9',
 '~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
length=int(input('Length of your password: '))
password=''
for char in range(1, length+1):
    password+=random.choice(numbers)
print(password)


# In[ ]:





# In[ ]:




