

#Analyzing US Economic Data and  Building a Dashboard  </h1>
# Description
# 

# Extracting essential data from a dataset and displaying it is a necessary part of data science; therefore individuals can make correct decisions based on the data. In this assignment, you will extract some essential economic indicators from some data, you will then display these economic indicators in a Dashboard. You can then share the dashboard via an URL.
# <p>
# <a href="https://en.wikipedia.org/wiki/Gross_domestic_product"> Gross domestic product (GDP)</a> is a measure of the market value of all the final goods and services produced in a period. GDP is an indicator of how well the economy is doing. A drop in GDP indicates the economy is producing less; similarly an increase in GDP suggests the economy is performing better. In this lab, you will examine how changes in GDP impact the unemployment rate. You will take screen shots of every step, you will share the notebook and the URL pointing to the dashboard.</p>

# 

# <h2 id="Section_1"> Define Function that Makes a Dashboard  </h2>

# We will import the following libraries.

# In[1]:


import pandas as pd
from bokeh.plotting import figure, output_file, show,output_notebook
output_notebook()


# In this section, we define the function <code>make_dashboard</code>. 
# You don't have to know how the function works, you should only care about the inputs. The function will produce a dashboard as well as an html file. You can then use this html file to share your dashboard. If you do not know what an html file is don't worry everything you need to know will be provided in the lab. 

# In[2]:


def make_dashboard(x, gdp_change, unemployment, title, file_name):
    output_file(file_name)
    p = figure(title=title, x_axis_label='year', y_axis_label='%')
    p.line(x.squeeze(), gdp_change.squeeze(), color="firebrick", line_width=4, legend="% GDP change")
    p.line(x.squeeze(), unemployment.squeeze(), line_width=4, legend="% unemployed")
    show(p)


# The dictionary  <code>links</code> contain the CSV files with all the data. The value for the key <code>GDP</code> is the file that contains the GDP data. The value for the key <code>unemployment</code> contains the unemployment data.

# In[3]:


links={'GDP':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_gdp.csv',       'unemployment':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_unemployment.csv'}


# <h3 id="Section_2"> Question 1: Create a dataframe that contains the GDP data and display the first five rows of the dataframe.</h3>

# Use the dictionary <code>links</code> and the function <code>pd.read_csv</code> to create a Pandas dataframes that contains the GDP data.

# <b>Hint: <code>links["GDP"]</code> contains the path or name of the file.</b>

# In[18]:


# Type your code here
Value = links["GDP"]
reading_data = pd.read_csv(Value)
df = pd.DataFrame(reading_data)


# Use the method <code>head()</code> to display the first five rows of the GDP data, then take a screen-shot.

# In[13]:


# Type your code here
df.head(5)


# <h3 id="Section_2"> Question 2: Create a dataframe that contains the unemployment data. Display the first five rows of the dataframe. </h3>

# Use the dictionary <code>links</code> and the function <code>pd.read_csv</code> to create a Pandas dataframes that contains the unemployment data.

# In[21]:


# Type your code here
value_unemp = links["unemployment"]
unemp = pd.read_csv(value_unemp)
df_uemp = pd.DataFrame(unemp)


# Use the method <code>head()</code> to display the first five rows of the GDP data, then take a screen-shot.

# In[30]:


# Type your code here
df_uemp.head()


# <h3 id="Section_3">Question 3: Display a dataframe where unemployment was greater than 8.5%. Take a screen-shot.</h3>

# In[52]:


# Type your code here
df[df_uemp["unemployment"] > 8.5]


# <h3 id="Section_4">Question 4: Use the function make_dashboard to make a dashboard</h3>

# In this section, you will call the function  <code>make_dashboard</code> , to produce a dashboard. We will use the convention of giving each variable the same name as the function parameter.

# Create a new dataframe with the column <code>'date'</code> called <code>x</code> from the dataframe that contains the GDP data.

# In[45]:


# Create your dataframe with column date
x = df[['date']]


# Create a new dataframe with the column <code>'change-current' </code> called <code>gdp_change</code>  from the dataframe that contains the GDP data.

# In[53]:



# Create your dataframe with column change-current

gdp_change = df[['change-current']]


# Create a new dataframe with the column <code>'unemployment' </code> called <code>unemployment</code>  from the dataframe that contains the  unemployment data.

# In[49]:


# Create your dataframe with column unemployment
unemployment = df_uemp[['unemployment']]


# Give your dashboard a string title, and assign it to the variable <code>title</code>

# In[50]:


# Give your dashboard a string title
title = "Dashboard for GDP and Unemployment"


# Finally, the function <code>make_dashboard</code> will output an <code>.html</code> in your direictory, just like a <code>csv</code> file. The name of the file is <code>"index.html"</code> and it will be stored in the varable  <code>file_name</code>.

# In[51]:


file_name = "index.html"


# Call the function <code>make_dashboard</code> , to produce a dashboard.  Assign the parameter values accordingly take a the <b>, take a screen shot of the dashboard and submit it</b>.

# In[54]:


# Fill up the parameters in the following function:
make_dashboard(x= df[['date']], gdp_change= df[['change-current']], unemployment=df_uemp[['unemployment']],
               title="Dashboard for GDP and Unemployment", file_name="index.html")
