#!/usr/bin/env python
# coding: utf-8

# ## In this exercise, let me demonstrate the veiwers of my github, how to model the problem and predict the car prices

# ### Importing libraries 

# In[45]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[46]:


# path of data 
path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/automobileEDA.csv'


# ### Now lets load this data into our pandas dataframe

# In[47]:


df= pd.read_csv(path)


# In[48]:


df.head()


# ![image.png](attachment:image.png)

# In[49]:


# checking counts for missing values


# In[50]:


df.describe()


# ![image.png](attachment:image.png)

# From the above image, we can see that there are some missing values in stroke, Therefore, for the purpose of this exercise, lets fill those missing values with average of all values in stroke

# In[51]:


#replacing missing values
df.replace("?",np.NaN, inplace = True)


# In[ ]:





# In[52]:


#storing missing data into a variable
missing_data = df.isnull()


# In[53]:


missing_data


# In[54]:


#counting missing values
for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")    


# ![image.png](attachment:image.png)

# In[55]:


#replacing those values with average values
avg_stroke = df['stroke'].astype('float').mean()

#3.2569035532994857


# In[56]:


avg_stroke


# In[57]:


df['stroke'].replace(np.NaN, avg_stroke, inplace = True)


# In[58]:


df.describe()


# ![image.png](attachment:image.png)

# ## All the missing values are replaced from the above data set

# # Now lets continue with modelling

# In[59]:


from sklearn.linear_model import LinearRegression


# In[60]:


lm = LinearRegression()
lm


# In[61]:


X = df[['highway-mpg']]
Y = df['price']


# In[62]:


lm.fit(X,Y)


# In[63]:


yhat = lm.predict(X)
yhat[0:5]


# In[64]:


#Intercept value
lm.intercept_
#38423.305858157386


# In[65]:


#Slope
lm.coef_
#array([-821.73337832])


# ## We therefore got regression equation for 'highway-mpg' and 'price'
# 
# ###  Y = -821.733378 (X) + 38423.30585

# # Now lets see engine size and price

# In[69]:


lm1 = LinearRegression()


# In[70]:


x = df[['engine-size']]
y = df[['price']]


# In[71]:


lm1.fit(x,y)


# In[72]:


y1hat = lm1.predict(x)
y1hat[0:5]


# In[73]:


lm1.coef_

# slope = 166.86001569


# In[74]:


lm1.intercept_

#intercept = 7963.33890628


# ### Therefore, the relation between price and engine size is give by the following equation
# ### Y = 166.860015(X) - 7963.33890628

# # Multiple-linear Regression

# From the previous section we know that other good predictors of price could be:
# 
# Horsepower
# Curb-weight
# Engine-size
# Highway-mpg
# Let's develop a model using these variables as the predictor variables.

# In[75]:


z = df[['horsepower','curb-weight','engine-size','highway-mpg']]


# In[77]:


lm.fit(z,df['price'])


# In[79]:


yhat = lm.predict(z)
yhat[0:5]


# In[80]:


lm.intercept_

# -15806.62462632922


# In[83]:


lm.coef_
# coefficient of each variable is array([53.49574423,  4.70770099, 81.53026382, 36.05748882]) respectively


# ## Model evaluation using visualisation

# In[89]:


import seaborn as sns 
plot1 = sns.regplot(x = 'highway-mpg', y = 'price', data = df)
plt.ylim(0,)


# ![image.png](attachment:image.png)

# We can see from this plot that price is negatively correlated to highway-mpg, since the regression slope is negative. One thing to keep in mind when looking at a regression plot is to pay attention to how scattered the data points are around the regression line. This will give you a good indication of the variance of the data, and whether a linear model would be the best fit or not. If the data is too far off from the line, this linear model might not be the best model for this data. Let's compare this plot to the regression plot of "peak-rpm".

# In[90]:


plot2 = sns.regplot(x = 'peak-rpm', y = 'price', data = df)
plt.ylim(0,)


# ![image.png](attachment:image.png)

# Comparing the regression plot of "peak-rpm" and "highway-mpg" we see that the points for "highway-mpg" are much closer to the generated line and on the average decrease. The points for "peak-rpm" have more spread around the predicted line, and it is much harder to determine if the points are decreasing or increasing as the "highway-mpg" increases.

# In[91]:


# To verify the regression plots above is "peak-rpm" or "highway-mpg" more strongly correlated with "price"


# In[93]:


df[['peak-rpm','highway-mpg','price']].corr()


# ![image.png](attachment:image.png)

# Residual Plot
# A good way to visualize the variance of the data is to use a residual plot.
# 
# What is a residual?
# 
# The difference between the observed value (y) and the predicted value (Yhat) is called the residual (e). When we look at a regression plot, the residual is the distance from the data point to the fitted regression line.
# 
# So what is a residual plot?
# 
# A residual plot is a graph that shows the residuals on the vertical y-axis and the independent variable on the horizontal x-axis.
# 
# What do we pay attention to when looking at a residual plot?
# 
# We look at the spread of the residuals:
# 
# If the points in a residual plot are randomly spread out around the x-axis, then a linear model is appropriate for the data. Why is that? Randomly spread out residuals means that the variance is constant, and thus the linear model is a good fit for this data.

# In[100]:


#residual plot
plt.figure(figsize = (20,10))
plot3 = sns.residplot(x = 'highway-mpg', y = 'price' , data = df)


# ![image.png](attachment:image.png)

# We can see from this residual plot that the residuals are not randomly spread around the x-axis, which leads us to believe that maybe a non-linear model is more appropriate for this data.

# # Multiple Linear Regression 
# 
# How do we visualize a model for Multiple Linear Regression? This gets a bit more complicated because you can't visualize it with regression or residual plot.
# 
# One way to look at the fit of the model is by looking at the distribution plot: We can look at the distribution of the fitted values that result from the model and compare it to the distribution of the actual values.
# 
# First lets make a prediction

# In[103]:


yhat = lm.predict(z)
z


# In[106]:


ax1 = sns.distplot(df['price'], hist = False, color = "r", label = "Actual label")


# ![image.png](attachment:image.png)

# In[112]:


ax1 = sns.distplot(df['price'], hist = False, color = "r", label = "Actual label")
sns.distplot(yhat, hist = False, color = "b", label = "Predicted value", ax= ax1)


# We see that the model output and actual output almost overlaps each other. Hence we can say the model is working correctly

# In[ ]:




