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

# We will look into missing data once we set ? to NaN

# In[22]:


#missing data can be found by this
df.isnull()


# True here states that the data is missing and False indicates that the data is not missing

# In[34]:


#storing missing data into a variable
missing_data = df.isnull()


# In[35]:


#checking the data
missing_data.head(5)


# This data is not clear, hence we use for loop to get the count for each column and its missing data 

# In[33]:


#counting missing values
for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")    


# Now we need to deal with these missing values.
# The count is as follows:
# normalized-losses = 40 missing,
# num-of-doors = 2 missing,
# bore = 4 missing, 
# stoke = 4 missing,
# horsepower = 2 missing, 
# peak-rpm = 2 missing and 
# price = 2 missing.
# 
# 
# We can either remove them row or column wise or replace them with average or mode
# 
# For example: Price has 2 missing values, we can drop it as its the target we need to predict

# In[28]:


#Calculating the average of the column to replace the missing value

avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0) # we are converting data type as we need float not int


# In[31]:


# we now use this value and replace it with all the missing values in that column


# In[32]:


df["normalized-losses"].replace(np.NaN,avg_norm_loss,inplace = True)


# ## Bore column is being replaced by mean

# In[37]:


#bore average
avg_bore = df["bore"].astype("float").mean(axis=0)
print (avg_bore)


# In[38]:


#replacing missing values with 3.3290 (the above obtained result)


# In[39]:


df["bore"].replace(np.NaN,avg_bore,inplace= True)


# ## Stroke column is being replaced by mean

# In[42]:


avg_stroke = df["stroke"].astype("float").mean(axis=0)
print(avg_stroke)


# In[43]:


df["stroke"].replace(np.NaN,avg_stroke,inplace= True)


# ## Calculate the mean value for the 'horsepower' column:

# In[44]:


avg_horsepower = df['horsepower'].astype('float').mean(axis=0)
print("Average horsepower:", avg_horsepower)

df['horsepower'].replace(np.nan, avg_horsepower, inplace=True)


# ## Calculate the mean value for 'peak-rpm' column:

# In[45]:


avg_peakrpm=df['peak-rpm'].astype('float').mean(axis=0)
print("Average peak rpm:", avg_peakrpm)

df['peak-rpm'].replace(np.nan, avg_peakrpm, inplace=True)


# ## Number of doors

# In[48]:


df["num-of-doors"].value_counts()


# In[52]:


#to calculate which one is maximum
df["num-of-doors"].value_counts().idxmax()


# In[50]:


# Therefore, we can replace the values in num-of-doors with four


# In[53]:


df["num-of-doors"].replace(np.NaN,"four",inplace = True)


# ## Dropping missing from price (Prediction target value)

# In[57]:


df.dropna(subset=["price"], axis=0, inplace=True)


# In[58]:


# reset index, because we droped two rows
df.reset_index(drop=True, inplace=True)


# In[59]:


df.head()


# ## Cleaning is finised. Checking if the data is correctly mapped with datatypes

# In[63]:


df.dtypes


# In[64]:


# correcting the datatypes
df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")


# In[65]:


df.dtypes


# ## DATA STANDARDIZATION

# In[66]:


# Convert mpg to L/100km by mathematical operation (235 divided by mpg)
df['city-L/100km'] = 235/df["city-mpg"]

# check your transformed data 
df.head()


# In[67]:


# Write your code below and press Shift+Enter to execute 
df["highway-mpg"] = 235/df["highway-mpg"]

# Renaming the column name 
df.rename(columns= {"highway-mpg":"highway-L/100"},inplace = True)


# In[68]:


df.head()


# ## Data Normalization
# Why normalization?
# 
# Normalization is the process of transforming values of several variables into a similar range. Typical normalizations include scaling the variable so the variable average is 0, scaling the variable so the variance is 1, or scaling variable so the variable values range from 0 to 1

# In[70]:


# replace (original value) by (original value)/(maximum value)
df['length'] = df['length']/df['length'].max()
df['width'] = df['width']/df['width'].max()


# ## Binning the categories in various bins

# In[76]:


df["horsepower"].dtypes


# In[81]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.pyplot.hist(df["horsepower"])
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("counts")
plt.pyplot.title("histogram for horsepower")


# In[84]:


# creating bins using numpy
bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)
bins


# In[85]:


group_names = ['Low', 'Medium', 'High']


# In[100]:


df["horsepower-binned"] = pd.cut(df["horsepower"],bins, labels = group_names, include_lowest = True)


# In[102]:


df[["horsepower","horsepower-binned"]].head(100)


# In[103]:


# COUNT
df["horsepower-binned"].value_counts()


# In[111]:


# bar chart
plt.pyplot.bar(group_names, height = df["horsepower-binned"].value_counts())


# In[112]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib as plt
from matplotlib import pyplot


# draw historgram of attribute "horsepower" with bins = 3
plt.pyplot.hist(df["horsepower"], bins = 3)

# set x/y labels and plot title
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")


# ## Indicator variable (or dummy variable)
# What is an indicator variable?
# An indicator variable (or dummy variable) is a numerical variable used to label categories. They are called 'dummies' because the numbers themselves don't have inherent meaning.
# 
# Why we use indicator variables?
# 
# So we can use categorical variables for regression analysis in the later modules.
# 
# Example
# We see the column "fuel-type" has two unique values, "gas" or "diesel". Regression doesn't understand words, only numbers. To use this attribute in regression analysis, we convert "fuel-type" into indicator variables.
# 
# We will use the panda's method 'get_dummies' to assign numerical values to different categories of fuel type.

# In[113]:


df.columns


# In[116]:


dummy_variables1 = pd.get_dummies(df['fuel-type'])
dummy_variables1.head()


# In[119]:


dummy_variables1.rename(columns = {'gas':'fuel-type-gas','diesel':'fuel-type-disel'},inplace = True)
dummy_variables1.head()


# In[120]:


# finally we combine this with df and drop old column


# In[126]:


#combining 
df = pd.concat([df,dummy_variables1],axis = 1)


# In[128]:


#dropping old column
df.drop('fuel-type',axis = 1, inplace= True)


# In[129]:


df.head()


# ## indicator variable to the column of "aspiration": "std" to 0, while "turbo" to 1.

# In[131]:


std_dummy = pd.get_dummies(df["aspiration"])
std_dummy


# In[133]:


#renaming columns
std_dummy.rename(columns = {'std':'aspiration-std', 'turbo':'aspiration-turbo'},inplace = True)


# In[134]:


df = pd.concat([df,std_dummy], axis = 1)


# In[135]:


df.head()


# In[136]:


# Write your code below and press Shift+Enter to execut
df.drop(["aspiration"],axis =1, inplace = True )


# In[139]:


df.to_csv('clean_df.csv')
print("done")


# In[ ]:





# In[ ]:




