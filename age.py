
# coding: utf-8

# In[11]:

import pandas as pd
import numpy as np
import random
import math, numpy
import matplotlib.pyplot as plt
import seaborn as sns

Data = pd.read_excel('Data.xls')


# In[12]:

Data = Data.T.drop_duplicates().T


# In[13]:

Data['Age'] = pd.to_numeric(Data['Age'], errors='coerce')

Data['Age'].plot.hist(bins=20, figsize=(10,5), title='Age')
plt.show()


# In[14]:

col_num = 9
for idx, x in enumerate(Data['Age']):
    if x < 18:
        Data.iat[idx, col_num] = 'NaN'
  
Data['Age'] = ['NaN' if x > (Data['Age'].quantile(0.75) + (1.5*(Data['Age'].quantile(0.75)-Data['Age'].quantile(0.25)))) else x for x in Data['Age']] 


# In[15]:

Data['Age'] = pd.to_numeric(Data['Age'], errors='coerce')

Data['Age'].plot.hist(bins=20, figsize=(10,5), title='Age without outliers')
plt.show()


# In[17]:

conditions = [
    (Data['Age'] >= 18) & (Data['Age'] < 40),
    (Data['Age'] >= 40) & (Data['Age'] < 60),
    (Data['Age'] >= 60)]
choices = ['Young', 'Middle Age', 'Older']

Data['AgeDisc'] = np.select(conditions, choices, default='NA')

Data['AgeDisc'].value_counts().plot.bar(rot=0, figsize=(7,5), title='Age without outliers and discretised')
plt.show()


# In[ ]:



