#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Covid-19 Analysis Based on World Health Organization's Data set


# In[2]:


import pandas as pd
import numpy as py
import matplotlib as ml


# In[3]:


import pandas as pd
file_path = "D:\covid19 dataset\WHO-COVID-19-global-data (1).csv"

# Skip problematic rows
covid_data = pd.read_csv(file_path, error_bad_lines=False)


# In[4]:


basic_stats = covid_data.describe()


# In[5]:


print(basic_stats)


# In[6]:


import pandas as pd
total_cumulative_cases = covid_data['Cumulative_cases'].sum()
total_cumulative_deaths = covid_data['Cumulative_deaths'].sum()

print(f'Total Cumulative Cases: {total_cumulative_cases}')
print(f'Total Cumulative Deaths: {total_cumulative_deaths}')


# In[7]:


# Convert 'Date_reported' to datetime format
covid_data['Date_reported'] = pd.to_datetime(covid_data['Date_reported'])

# Find the last date in the dataset
last_date = covid_data['Date_reported'].max()

# Filter the dataset for the last date
latest_data = covid_data[covid_data['Date_reported'] == last_date]

# Calculate total cumulative cases and deaths
total_cumulative_cases = latest_data['Cumulative_cases'].sum()
total_cumulative_deaths = latest_data['Cumulative_deaths'].sum()

print(f'Total Cumulative Cases as of {last_date}: {total_cumulative_cases}')
print(f'Total Cumulative Deaths as of {last_date}: {total_cumulative_deaths}')


# In[ ]:





# In[8]:


import matplotlib.pyplot as plt

# Convert 'Date_reported' to datetime
covid_data['Date_reported'] = pd.to_datetime(covid_data['Date_reported'])

# Plotting time series of new cases and deaths
plt.figure(figsize=(14, 8))
plt.plot(covid_data['Date_reported'], covid_data['New_cases'], label='New Cases', marker='o')
plt.plot(covid_data['Date_reported'], covid_data['New_deaths'], label='New Deaths', marker='o')

plt.title('Time Series of New Cases and Deaths')
plt.xlabel('Date Reported')
plt.ylabel('Count')
plt.legend()
plt.show()


# In[9]:


import matplotlib.pyplot as plt

# Plotting time series of new cases and deaths with a secondary y-axis for deaths
fig, ax1 = plt.subplots(figsize=(14, 8))

color = 'tab:blue'
ax1.set_xlabel('Date Reported')
ax1.set_ylabel('New Cases', color=color)
ax1.plot(covid_data['Date_reported'], covid_data['New_cases'], color=color, marker='o')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  
color = 'tab:red'
ax2.set_ylabel('New Deaths', color=color)  
ax2.plot(covid_data['Date_reported'], covid_data['New_deaths'], color=color, marker='o')
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  
plt.title('Time Series of New Cases and Deaths')
plt.show()


# In[10]:


import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter

# Plotting time series of new cases and deaths with a secondary y-axis for deaths
fig, ax1 = plt.subplots(figsize=(14, 8))

color = 'tab:red'
ax1.set_xlabel('Date Reported')
ax1.set_ylabel('New Cases', color=color)
ax1.plot(covid_data['Date_reported'], covid_data['New_cases'], color=color, marker='o')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  
color = 'tab:blue'
ax2.set_ylabel('New Deaths', color=color)  
ax2.plot(covid_data['Date_reported'], covid_data['New_deaths'], color=color, marker='o')
ax2.tick_params(axis='y', labelcolor=color)

# Use EngFormatter to format y-axis labels with appropriate units
ax1.yaxis.set_major_formatter(EngFormatter())
ax2.yaxis.set_major_formatter(EngFormatter())

fig.tight_layout()  
plt.title('Time Series of New Cases and Deaths')
plt.show()


# In[11]:


correlation_matrix = covid_data.corr()


# In[12]:


print(correlation_matrix)


# In[13]:


import matplotlib.pyplot as plt

plt.figure(figsize=(14, 8))
plt.plot(covid_data['Date_reported'], covid_data['New_cases'], label='New Cases', marker='o')
plt.plot(covid_data['Date_reported'], covid_data['New_deaths'], label='New Deaths', marker='o')
plt.title('Time Series of New Cases and Deaths')
plt.xlabel('Date Reported')
plt.ylabel('Count')
plt.legend()
plt.show()


# In[14]:


import seaborn as sns


# In[15]:


covid_data_unique = covid_data.drop_duplicates(subset=['Country', 'Cumulative_cases'])


# In[16]:


import matplotlib.pyplot as plt
import seaborn as sns

# Group the data by country and calculate the total cumulative cases
country_cumulative_cases = covid_data.groupby('Country')['Cumulative_cases'].max().reset_index()

# Sort the data by cumulative cases in descending order and select the top 10
top_10_countries = country_cumulative_cases.sort_values('Cumulative_cases', ascending=False).head(10)

# Plot the bar chart
plt.figure(figsize=(12, 6))
sns.barplot(x='Cumulative_cases', y='Country', data=top_10_countries, palette='viridis')
plt.title('Top 10 Countries with the Highest Cumulative Cases')
plt.xlabel('Cumulative Cases')
plt.ylabel('Country')
plt.show()


# In[17]:


import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(16, 8))
sns.lineplot(x='Date_reported', y='New_cases', data=covid_data)
plt.title('Global Trends in New Cases Over Time')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.xticks(rotation=45)
plt.show()


# In[18]:


plt.figure(figsize=(16, 8))
sns.lineplot(x='Date_reported', y='New_deaths', data=covid_data)
plt.title('Global Trends in New Deaths Over Time')
plt.xlabel('Date')
plt.ylabel('New Deaths')
plt.xticks(rotation=45)
plt.show()


# In[19]:


import pandas as pd
file_path2 = "D:\\covid19 dataset\\vaccination-data (1).csv"

vaccination_data=pd.read_csv(file_path2)


# In[20]:


vaccination_data.describe()


# In[21]:


# Merge the datasets based on the "Country" columns
merged_data = pd.merge(covid_data, vaccination_data, left_on='Country', right_on='COUNTRY', how='inner')

# Display the merged data
merged_data.head()


# In[22]:


import matplotlib.pyplot as plt
import seaborn as sns

# Scatter plot for New_cases and PERSONS_VACCINATED_1PLUS_DOSE
plt.figure(figsize=(12, 6))
sns.scatterplot(data=merged_data, x='New_cases', y='PERSONS_VACCINATED_1PLUS_DOSE')
plt.title('Relationship between New Cases and Vaccination')
plt.xlabel('New Cases')
plt.ylabel('Persons Vaccinated 1+ Dose')
plt.show()

# Scatter plot for Cumulative_cases and TOTAL_VACCINATIONS
plt.figure(figsize=(12, 6))
sns.scatterplot(data=merged_data, x='Cumulative_cases', y='TOTAL_VACCINATIONS')
plt.title('Relationship between Cumulative Cases and Total Vaccinations')
plt.xlabel('Cumulative Cases')
plt.ylabel('Total Vaccinations')
plt.show()

# Scatter plot for New_deaths and PERSONS_BOOSTER_ADD_DOSE
plt.figure(figsize=(12, 6))
sns.scatterplot(data=merged_data, x='New_deaths', y='PERSONS_BOOSTER_ADD_DOSE')
plt.title('Relationship between New Deaths and Booster Doses')
plt.xlabel('New Deaths')
plt.ylabel('Persons Booster Add Dose')
plt.show()

# Scatter plot for Cumulative_deaths and TOTAL_VACCINATIONS_PER100
plt.figure(figsize=(12, 6))
sns.scatterplot(data=merged_data, x='Cumulative_deaths', y='TOTAL_VACCINATIONS_PER100')
plt.title('Relationship between Cumulative Deaths and Total Vaccinations per 100 People')
plt.xlabel('Cumulative Deaths')
plt.ylabel('Total Vaccinations per 100 People')
plt.show()


# In[23]:


import matplotlib.pyplot as plt

# Plot scatter plots for selected columns
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.scatter(merged_data['New_cases'], merged_data['PERSONS_VACCINATED_1PLUS_DOSE'], alpha=0.5)
plt.title('New Cases vs Vaccination')

plt.subplot(2, 2, 2)
plt.scatter(merged_data['Cumulative_cases'], merged_data['TOTAL_VACCINATIONS'], alpha=0.5)
plt.title('Cumulative Cases vs Total Vaccinations')

plt.subplot(2, 2, 3)
plt.scatter(merged_data['New_deaths'], merged_data['PERSONS_BOOSTER_ADD_DOSE'], alpha=0.5)
plt.title('New Deaths vs Booster Doses')

plt.subplot(2, 2, 4)
plt.scatter(merged_data['Cumulative_deaths'], merged_data['TOTAL_VACCINATIONS_PER100'], alpha=0.5)
plt.title('Cumulative Deaths vs Total Vaccinations per 100 People')

plt.tight_layout()
plt.show()


# In[24]:


import matplotlib.pyplot as plt
import seaborn as sns

# Plot scatter plots for selected columns
plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
sns.scatterplot(x='New_cases', y='PERSONS_VACCINATED_1PLUS_DOSE', data=merged_data, alpha=0.5)
plt.title('New Cases vs Vaccination')
plt.xlabel('New Cases')
plt.ylabel('Persons Vaccinated (1+ Dose)')

plt.subplot(2, 2, 2)
sns.scatterplot(x='Cumulative_cases', y='TOTAL_VACCINATIONS', data=merged_data, alpha=0.5)
plt.title('Cumulative Cases vs Total Vaccinations')
plt.xlabel('Cumulative Cases')
plt.ylabel('Total Vaccinations')

plt.subplot(2, 2, 3)
sns.scatterplot(x='New_deaths', y='PERSONS_BOOSTER_ADD_DOSE', data=merged_data, alpha=0.5)
plt.title('New Deaths vs Booster Doses')
plt.xlabel('New Deaths')
plt.ylabel('Persons Booster (Additional Dose)')

plt.subplot(2, 2, 4)
sns.scatterplot(x='Cumulative_deaths', y='TOTAL_VACCINATIONS_PER100', data=merged_data, alpha=0.5)
plt.title('Cumulative Deaths vs Total Vaccinations per 100 People')
plt.xlabel('Cumulative Deaths')
plt.ylabel('Total Vaccinations per 100 People')

plt.tight_layout()
plt.show()


# In[25]:


# Assuming the merged dataset is stored in the variable merged_data
merged_data.to_csv('merged_data.csv', index=False)


# In[ ]:




