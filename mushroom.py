#!/usr/bin/env python
# coding: utf-8

# In[71]:


import numpy as np
import pandas as pd
import statsmodels.formula.api as stats
from statsmodels.formula.api import ols
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.svm import SVC


# In[2]:


data= pd.read_csv("mushroom.csv")


# In[3]:


data.head()


# In[62]:


x=data.iloc[:,1:23]
y=data.iloc[:,0]


# In[65]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.33, random_state=42)


# In[6]:





# In[7]:


#dropping veil type column 
data.drop("veil-type", axis=1, inplace=True)


# In[26]:


data.isnull().sum()


# In[ ]:


data[column] = [value if letter==i else letter for letter in data[column]]
value += step


# In[31]:


data_check = data.head()
data_check = data_check.append(data.tail())
data_check


# In[76]:


data.describe


# In[77]:


X=data.drop('class',axis=1)
y=data['class']
X.head()


# In[78]:


y


# In[79]:


#poisonus = 1
# eatable=0


# In[ ]:




