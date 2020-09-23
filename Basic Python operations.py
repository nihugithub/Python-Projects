#!/usr/bin/env python
# coding: utf-8

# ### This code is to practice basic functions of data analysis

# In[5]:


#Importing libraries for performing the operations

import pandas as pd
import matplotlib.pylab as plt


# ### File uploading process

# In[6]:


#Our data file is located in the below link.

filename = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"


# In[8]:


# To upload the file into python, we use dataframe method using pandas library and read the first 5 lines after loading
df = pd.read_csv(filename)
df.head()


# ### Headers missing

# In[9]:


# We noticed that the headers are missing from the dataset loaded in pandas dataframe. 
# We will allocate the headers to the column names based on the data description as follows


# In[10]:


headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]


# In[16]:


# Allocating headers to our dataset
df.columns = headers


# In[18]:


# Rechecking if the headers are assigned correctly
df.head(20) # (20) -- > outputs first 20 rows


# We have noticed that there are some ? present in the dataset. These ? are generally considered missing values. We need to eliminate missing values for getting our model correct. 
# 
# In order to remove the missing values, we can replace ? with NaN ( a standard symbol used for missing values)
# 
# 
# Before using replace function from numpy, we need to import the module first.

# In[19]:


#importing numpy module
import numpy as np


# In[20]:


#replacing missing values
df.replace("?",np.NaN, inplace = True)


# In[21]:


#rechecking the data
df.head()


# We notice that our changes has been made successfully

# In[ ]:




