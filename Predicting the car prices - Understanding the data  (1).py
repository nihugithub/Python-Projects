#!/usr/bin/env python
# coding: utf-8

# ### We are here to see what characteristics impact the price of the car

# In[1]:


#importing modules required


# In[104]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[105]:


#loading our data into pandas dataframe


# In[106]:


path='https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/automobileEDA.csv'
df= pd.read_csv(path)
df.head()


# ![image.png](attachment:image.png)

# In[107]:


# checking for missing values


# In[108]:


df.isnull()


# ![image.png](attachment:image.png)

# In[109]:


#counting missing data values
missing_data = df.isnull()


for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")  


# ![image.png](attachment:image.png)

# ## We can see that Stroke and Horsepower has 4 and 1 missing values respectively

# In[110]:


#replacing them with their mean values 


# In[111]:


# Stroke replacement


# In[112]:


avg_stroke = df["stroke"].astype("float").mean(axis = 0)


# In[113]:


avg_stroke


# In[114]:


#replacing it, before that we need this 


# In[115]:


df.replace("?",np.NaN, inplace = True)


# In[116]:


df["stroke"].replace(np.NaN,avg_stroke, inplace = True)


# In[117]:


avg_horsepower = df["horsepower"].astype("float").mean(axis=0)


# In[118]:


avg_horsepower


# In[119]:


df["horsepower"].replace(np.NaN,avg_horsepower, inplace = True)


# In[120]:


df.head()


# ![image.png](attachment:image.png)

# ## We eliminated the missing values. 
# ### For the scope of this task, we are skipping normalisation, standerdisation and other cleaning tasks

# In[121]:


df.describe()


# ![image.png](attachment:image.png)

# ## Let's study the pattern using some visualisations

# In[122]:


# installing seaborn


# #### We are using python package manager to install seaborn

# In[123]:


get_ipython().run_cell_magic('capture', '', 'pip install seaborn')


# In[124]:


import seaborn as sns


# In[125]:


# checking for data types before making a decision on type of visualisation to be used


# In[126]:


df.dtypes


# ![image.png](attachment:image.png)

# ## Let's start with correlation function

# In[127]:


df.corr()


# ![image.png](attachment:image.png)

# In[128]:


#understand the relationship of desired variables through scatter plot


# In[129]:


plot1 = sns.regplot(x='engine-size', y = 'price', data = df)
plot1
plt.ylim(0,)


# ![image.png](attachment:image.png)

# We understand the positive co-relation between price and engine-size. As engine-size goes up, price goes up

# In[130]:


#To know more
df[['price','engine-size']].corr() # 0.87 shows high correlation. 


# ![image.png](attachment:image.png)

# ### Now we will do the same for few more variables

# In[131]:


# correlation between price and miles on highway
df[['highway-mpg','price']].corr()


# ![image.png](attachment:image.png)

# ### The above shows negative correlation but high correlation. Therefore, it could be a negative regression.

# In[132]:


# to check for the negative correlation, we do scatter plot


# In[133]:


plot2 = sns.regplot(x='highway-mpg',y = 'price', data = df)
plt.ylim(0,)


# ![image.png](attachment:image.png)

# ## Now lets work on categorical variables 

# ### For categorical variables, we need to use different type of visualisation such as box plot, pivot tables etc

# #### Lets look into them step by step for body style and price

# In[134]:


plot3 = sns.boxplot(x='body-style',y = 'price', data = df)
plot3


# ![image.png](attachment:image.png)

# In[135]:


plot4= sns.boxplot(x = "engine-location", y= "price", data = df)


# ![image.png](attachment:image.png)

# In[136]:


df.dtypes


# In[ ]:





# ## Lets do some descriptive statistical analysis

# In[137]:


df.describe()


# In[138]:


df.describe( include =['object'])


# ![image.png](attachment:image.png)

# In[139]:


df['drive-wheels'].value_counts()


# In[140]:


df['drive-wheels'].value_counts().to_frame()


# In[141]:


# storing it in a frame
drive_wheel_counts = df['drive-wheels'].value_counts().to_frame()


# In[142]:


drive_wheel_counts


# In[143]:


drive_wheel_counts.rename(columns = {'drive-wheels':'value_counts'}, inplace = True)


# In[144]:


#lets name the index


# In[145]:


drive_wheel_counts.index.name = 'Drive'


# ## Grouping 

# In[146]:


df['drive-wheels'].unique()


# In[147]:


df_group = df[['drive-wheels','price','body-style']]


# In[148]:


grouping = df_group.groupby(['drive-wheels'],as_index = False).mean()


# In[149]:


grouping


# From our data analysis, it is evident that 4wd has 10k$, fwd  has 9.2k$ and Rwd has 19.7k$. This indicates that rear wheel drive cars are more on the higher size of the price. 

# In[157]:


grouping1 = df_group.groupby(['drive-wheels','body-style'],as_index = False).mean()


# In[158]:


grouping1


# In[159]:


#pivoting the data for easy visualisation


# In[160]:


pivot_table1 = grouping1.pivot(index = 'drive-wheels', columns = 'body-style')


# In[161]:


pivot_table1 = pivot_table1.fillna(0)
pivot_table1


# ## Group by body style to find average price

# In[171]:


group2 = df[['body-style','price']].groupby(['body-style'], as_index = True).mean()
group2


# In[177]:


plt.pcolor(pivot_table1,cmap = "RdBu")
plt.colorbar()
plt.show()
plt.xlabel


# ![image.png](attachment:image.png)

# ## As expected, this heatmap says nothing about the data.
# 
# ### Therefore, lets rename the columns for our understadning 

# In[180]:


fig, ax = plt.subplots()
im = ax.pcolor(pivot_table1, cmap='RdBu')

#label names
row_labels = pivot_table1.columns.levels[1]
col_labels = pivot_table1.index

#move ticks and labels to the center
ax.set_xticks(np.arange(pivot_table1.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(pivot_table1.shape[0]) + 0.5, minor=False)

#insert labels
ax.set_xticklabels(row_labels, minor=False)
ax.set_yticklabels(col_labels, minor=False)

#rotate label if too long
plt.xticks(rotation=90)

fig.colorbar(im)
plt.show()


# ### Importing scipy module for p value statistics

# In[181]:


from scipy import stats


# ## Wheel-base vs Price
# ### Let's calculate the Pearson Correlation Coefficient and P-value of 'wheel-base' and 'price'.

# In[187]:


pearson_coef, p_value = stats.pearsonr(df['wheel-base'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)

# The Pearson Correlation Coefficient is 0.5846418222655083  with a P-value of P = 8.076488270732873e-20
#which says no correlated.


# ## Lets repeat this process for other variables as well

# In[189]:


p_coef, p_value = stats.pearsonr(df['horsepower'],df['price'])
print (p_coef,p_value)
#0.8095745670036555 6.369057428261186e-48


# In[192]:


p_coef, p_value = stats.pearsonr(df['length'],df['price'])
print(p_coef,p_value)
#0.6906283804483644 8.016477466158188e-30


# ## ANOVA: Analysis of Variance
# The Analysis of Variance (ANOVA) is a statistical method used to test whether there are significant differences between the means of two or more groups. ANOVA returns two parameters:
# 
# F-test score: ANOVA assumes the means of all groups are the same, calculates how much the actual means deviate from the assumption, and reports it as the F-test score. A larger score means there is a larger difference between the means.
# 
# P-value: P-value tells how statistically significant is our calculated score value.
# 
# If our price variable is strongly correlated with the variable we are analyzing, expect ANOVA to return a sizeable F-test score and a small p-value.

# In[206]:


#ANOVA TEST FOR BODY_TYPE and price , Here we dont do mean as ANOVA calculates mean automatically


# In[208]:


group_3 = df[['body-style','price']].groupby(['body-style'])


# In[196]:


group_3


# In[198]:


#Before Anova, we split this group3 in specific body-style groups


# In[214]:


group_conv = group_3.get_group('convertible')['price']
group_conv


# In[215]:


group_hardtop = group_3.get_group('hardtop')['price']
group_hardtop


# In[216]:


group_hatchback = group_3.get_group('hatchback')['price']
group_hatchback


# In[217]:


group_sedan = group_3.get_group('sedan')['price']
group_sedan


# In[218]:


group_wagon= group_3.get_group('wagon')['price']
group_wagon


# In[220]:


#ANOVA on group3 from group_conv,group_hardtop,group_hatchback,group_sedan,group_wagon


# In[221]:


f_val,p_val = stats.f_oneway(group_conv,group_hardtop,group_hatchback,group_sedan,group_wagon)


# In[222]:


f_val,p_val


# ### Here f_value is less where as p value is <0.001, which means there is not much correlation 

# ### Variables that are important from this dataset

# We now have a better idea of what our data looks like and which variables are important to take into account when predicting the car price. We have narrowed it down to the following variables:
# 
# Continuous numerical variables:
# 
# 1) Length
# 2) Width
# 3) Curb-weight
# 4) Engine-size
# 5) Horsepower
# 6) City-mpg
# 7) Highway-mpg
# 8) Wheel-base
# 9) Bore
# Categorical variables:
# 
# 10) Drive-wheels
# As we now move into building machine learning models to automate our analysis, feeding the model with variables that meaningfully affect our target variable will improve our model's prediction performance.

# In[ ]:




