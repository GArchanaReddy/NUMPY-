#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np


# In[13]:


fpath = "tipsf.csv"


# In[14]:


x = np.genfromtxt(fpath,delimiter= ',',skip_header=True)


# In[15]:


x


# # 1) what is the total bill value

# In[10]:


bill_value = np.sum(x[:,1])
bill_value


# # 2) what is the total tip value

# In[12]:


tip_value = np.sum(x[:,2])
tip_value


# In[13]:


x[:,2]


# # 3) count how many sunday, saturaday, thursday ,friday are there

# In[14]:


np.unique(x[:,5])


# In[16]:


np.unique(x[:,5], return_counts = True)


# # 4) how many smokers are there

# In[17]:


np.unique(x[:,4])


# In[18]:


np.unique(x[:,4],return_counts = True)#non smokers = 0 # smokers = 1


# # 5) what is avg tip is given by the female and male

# In[22]:


gender = (x[:,3])
tip = (x[:,2])
tip_value = np.mean(tip[gender==0])
print(tip_value)
tip_value = np.mean(tip[gender==1])
print(tip_value)


# # 6) How much amount have been spent by females and males

# In[5]:


import numpy as np


# In[16]:


amount = x[:,1]
sex = x[:,3]
tip = x[:,2]
total_tip_male = np.mean(tip[sex == 0])
total_tip_female = np.mean(tip[sex == 1])
total_amount_male = np.sum(amount[sex == 0])+ np.sum(tip[sex == 0]) 
total_amount_female = np.sum(amount[sex == 1])+ np.sum(tip[sex == 1])
print(total_amount_male)
print(total_amount_female)


# # 7) what is the min & maxtip given

# In[17]:


tip=np.min(x[:,2])# min value of tip
tip


# In[18]:


tip=np.max(x[:,2])
tip


# # 8) how many male & female are going for dinner and lunch

# In[19]:


lunch=x[:,6]#how many male and female are going for lunch
sex=x[:,3]
lunch_male = np.sum((sex == 0) & (lunch==0))
lunch_female = np.sum((sex == 1) & (lunch==0))
print('malecount for lunch:',lunch_male)
print('malecount for lunch:',lunch_female)


# # 9) find out the avg  size

# In[20]:


np.mean(x[:,7])


# # 10)how many female smokers  are there and male smokers are there

# In[21]:


smokers=x[:,4]
sex=x[:,3]
male_smokers=np.sum((sex==0)& (smokers == 1))
female_smokers=np.sum((sex==1)& (smokers == 1))
print('male_smokers:',male_smokers)
print('female_smokers:',female_smokers)
                    


# In[ ]:




