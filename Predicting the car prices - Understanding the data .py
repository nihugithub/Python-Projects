#!/usr/bin/env python
# coding: utf-8

# ### We are here to see what characteristics impact the price of the car

# In[93]:


#importing modules required


# In[94]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[95]:


#loading our data into pandas dataframe


# In[96]:


path='https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/automobileEDA.csv'
df= pd.read_csv(path)
df.head()


# In[97]:


# checking for missing values


# In[98]:


df.isnull()


# In[99]:


#counting missing data values
missing_data = df.isnull()


for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")  


# ## We can see that Stroke and Horsepower has 4 and 1 missing values respectively

# In[100]:


#replacing them with their mean values 


# In[101]:


# Stroke replacement


# In[102]:


avg_stroke = df["stroke"].astype("float").mean(axis = 0)


# In[103]:


avg_stroke


# In[104]:


#replacing it, before that we need this 


# In[105]:


df.replace("?",np.NaN, inplace = True)


# In[106]:


df["stroke"].replace(np.NaN,avg_stroke, inplace = True)


# In[107]:


avg_horsepower = df["horsepower"].astype("float").mean(axis=0)


# In[108]:


avg_horsepower


# In[109]:


df["horsepower"].replace(np.NaN,avg_horsepower, inplace = True)


# In[110]:


df.head()


# ## We eliminated the missing values. 
# ### For the scope of this task, we are skipping normalisation, standerdisation and other cleaning tasks

# In[111]:


df.describe()


# ## Let's study the pattern using some visualisations

# In[112]:


# installing seaborn


# #### We are using python package manager to install seaborn

# In[113]:


get_ipython().run_cell_magic('capture', '', 'pip install seaborn')


# In[114]:


import seaborn as sns


# In[115]:


# checking for data types before making a decision on type of visualisation to be used


# In[116]:


df.dtypes


# ## Let's start with correlation function

# In[117]:


df.corr()


# In[118]:


#understand the relationship of desired variables through scatter plot


# In[119]:


plot1 = sns.regplot(x='engine-size', y = 'price', data = df)
plot1
plt.ylim(0,)


# We understand the positive co-relation between price and engine-size. As engine-size goes up, price goes up

# In[120]:


#To know more
df[['price','engine-size']].corr() # 0.87 shows high correlation. 


# ### Now we will do the same for few more variables

# In[121]:


# correlation between price and miles on highway
df[['highway-mpg','price']].corr()


# ### The above shows negative correlation but high correlation. Therefore, it could be a negative regression.

# In[122]:


# to check for the negative correlation, we do scatter plot


# In[123]:


plot2 = sns.regplot(x='highway-mpg',y = 'price', data = df)
plt.ylim(0,)


# ## Now lets work on categorical variables 

# ### For categorical variables, we need to use different type of visualisation such as box plot, pivot tables etc

# #### Lets look into them step by step for body style and price

# In[124]:


plot3 = sns.boxplot(x='body-style',y = 'price', data = df)
plot3


# In[ ]:




