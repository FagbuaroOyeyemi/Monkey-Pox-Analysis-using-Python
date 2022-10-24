#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing the libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
get_ipython().run_line_magic('matplotlib', 'inline')

import warnings
warnings.filterwarnings('ignore')


# In[2]:


#Importing the Datasets

df_worldwide = pd.read_csv('C:\\Users\\HP\\Downloads\\Monkey_Pox_Cases_Worldwide.csv')
df_confirmed = pd.read_csv('C:\\Users\\HP\\Downloads\\Daily_Country_Wise_Confirmed_Cases.csv')
df_timeline = pd.read_csv('C:\\Users\\HP\Downloads\\Worldwide_Case_Detection_Timeline.csv\Worldwide_Case_Detection_Timeline.csv')


# ### Data Overview

# In[3]:


#Viewing the first five rows

df_worldwide.head()


# In[4]:


#Viewing the first five rows

df_confirmed.head()


# In[5]:


df_worldwide.info()


# #### There are 129 rows and 6  columns in the dataset

# In[6]:


#Making a copy of the dataset

df_worldwide2 = df_worldwide.copy()

df_worldwide2.head()


# In[7]:


#Checking for duplicates

df_worldwide.duplicated().sum()

#The output shows that there are no duplicates in the first dataset


# In[8]:


#Checking the Datatypes

df_worldwide.dtypes


# In[9]:


#Changing the datatypes

df_worldwide['Confirmed_Cases'] = df_worldwide['Confirmed_Cases'].astype('int64')
df_worldwide['Suspected_Cases']= df_worldwide['Suspected_Cases'].astype('int64')
df_worldwide['Hospitalized']= df_worldwide['Hospitalized'].astype('int64')
df_worldwide['Travel_History_Yes'] = df_worldwide['Travel_History_Yes'].astype('int64')
df_worldwide['Travel_History_No'] = df_worldwide['Travel_History_No'].astype('int64')

df_worldwide.head()

#Changed the datatype from float to integer


# In[10]:


#Checking the Columns in the dataset

df_worldwide.columns


# In[11]:


#Checking for null values

df_worldwide.isnull().sum()

#The output shows that there are no null values in the dataset


# In[12]:


df_worldwide.describe()


# In[13]:


df_worldwide.shape


# In[14]:


#The Countries in the dataset

df_worldwide.Country.unique()


# In[15]:


Total_confirmed_cases=df_worldwide['Confirmed_Cases'].sum()
Total_suspected_cases=df_worldwide['Suspected_Cases'].sum()
Total_hospitalized_cases=df_worldwide['Hospitalized'].sum()
print('Total Confirmed cases: ', Total_confirmed_cases)
print('Total Suspected Cases: ',Total_suspected_cases)
print('Total Hospitalized cases: ',Total_hospitalized_cases)


# ## Monkey Pox Confirmed cases worldwide

# In[16]:


fig= px.choropleth(df_worldwide,
                  locations='Country',
                  locationmode= 'country names',
                  hover_name= 'Country',
                  color= 'Confirmed_Cases',
                  color_continuous_scale= 'deep')
fig.update_layout(title_text= 'Monkey Pox Confirmed Cases Worldwide')


# ### Top 10 Countries by Confirmed Cases

# In[17]:


sorted_data= df_worldwide.sort_values(by='Confirmed_Cases',ascending=False).reset_index()
sorted_data.head(10)


# In[18]:


plt.figure(figsize=(12,5))
x=sorted_data['Country'][:10]
y=sorted_data['Confirmed_Cases'][:10]
plt.bar(x,y,width=0.5,color='brown')
plt.xlabel('Country')
plt.ylabel('Confirmed_Cases')
plt.title('Top 10 Countries by Confirmed Cases')
plt.show()


# ### Top 5 Countries by Suspected Cases

# In[19]:


sorted_data2= df_worldwide.sort_values(by='Suspected_Cases',ascending=False)                                       
plt.figure(figsize=(10,5))
x=sorted_data2['Country'][:5]
y=sorted_data2['Suspected_Cases'][:5]
plt.bar(x,y,width=0.8,color='brown')
plt.xlabel('Country',fontsize=14)
plt.ylabel('Suspected_Cases',fontsize=14)
plt.title('Top 5 Countries by Suspected Cases',fontsize=20)
plt.show()


# ### Top 10 Countries by Hospitalized Cases

# In[20]:


sorted_data3= df_worldwide.sort_values(by='Hospitalized',ascending=False).reset_index()
plt.figure(figsize=(20,5))
x=sorted_data3['Country'][:10]
y=sorted_data3['Hospitalized'][:10]
plt.bar(x,y,width=0.5,color='brown')
plt.xlabel('Country',fontsize=14)
plt.ylabel('Hospitalized_Cases',fontsize=14)
plt.title('Top 10 Countries by Hospitalized Cases',fontsize=20)
plt.show()


# ### Travel History

# In[21]:


travel_history=df_worldwide[['Travel_History_Yes', 'Travel_History_No']].reset_index().drop(['index'],axis=1).sum()
fig=px.bar(travel_history,width=400)
fig.show()


# #### Total of 274 reported cases of monkey pox had a travel history
# 91 reported cases did not have any travel history

# ### Correlation between Travel History and Confirmed Cases

# In[22]:


sns.scatterplot(x='Confirmed_Cases',y='Travel_History_Yes',data=df_worldwide)
plt.show()


# ### Correlation Betweeen Travel History and Suspected Cases

# In[23]:


sns.scatterplot(x='Suspected_Cases',y='Travel_History_Yes',data=df_worldwide)
plt.show()


# ## Daily Countrywise confirmed cases

# #### Data overview

# In[24]:


df_confirmed.head()


# In[25]:


#Making a copy of the dataset

df_confirmed2=df_confirmed.copy()
df_confirmed2.head()


# In[26]:


df_confirmed.info()


# In[27]:


df_confirmed.shape


# In[28]:


df_confirmed.isna().sum()


# In[29]:


df_confirmed.duplicated().sum()

#No duplicates


# In[30]:


df_confirmed.columns


# In[31]:


#Creating a new column

df_confirmed['Total_case']=df_confirmed.sum(axis=1)


# In[32]:


df_confirmed.head()

#From the output, we can see that the  new column is there


# In[33]:


df_confirmed.to_csv('complete daily countrywise confirmed cases.csv', index=False)


# ## Worldwide Case Detection Timeline

# In[34]:


df_timeline.head()


# In[35]:


df_timeline.info()


# In[36]:


df_timeline.shape


# In[37]:


df_timeline.isnull().sum()


# ### There are over 90% of null values in the dataset

# ## The Symptoms Monkey pox infected people are facing

# In[38]:


df_timeline['Symptoms'].unique()[1:]

