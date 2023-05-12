#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pandas


# In[2]:


import pandas as pd

# read data from a CSV file
df = pd.read_csv('Production_Crops_Livestock_E_All_Data.csv', encoding='ISO-8859-1')
df


# In[16]:


# Cleaning the data 
# extract rows that include data for maize (corn), rice, wheat, barley, and sorghum
df = pd.read_csv('Production_Crops_Livestock_E_All_Data.csv', encoding='ISO-8859-1')
# Select the columns you want to extract based on the year
columns_to_extract = ['Item','Element','Area', 'Y2000', 'Y2005', 'Y2010', 'Y2015', 'Y2020']

# Create a new dataframe with the selected years
df_new = df[columns_to_extract]
# Create a new dataframe with the selected years and only production values shown
df_chart = pd.DataFrame(columns=['Item','Element','Area', 'Y2000', 'Y2005', 'Y2010', 'Y2015', 'Y2020'])
for index, row in df.iterrows():


 crop = row['Item']
 if crop in ['Maize (corn)', 'Rice', 'Wheat', 'Barley', 'Sorghum']and row['Element'] == 'Production':
        #print(index,row['Item'],row['Area'],row['Element'],row['Y2005'])
         df_chart.loc[index] = [row['Item'], row['Element'], row['Area'], row['Y2000'], row['Y2005'], row['Y2010'], row['Y2015'], row['Y2020']]
        
      
print(df_chart)
print(df_chart.columns)


# In[ ]:





# In[18]:


# Extract the worlwide production values
# Extract the data for Maize, Rice, Wheat, Barley, and Sorghum
df_crops = df[(df['Item'].isin(['Maize (corn)', 'Rice', 'Wheat', 'Barley', 'Sorghum'])) & (df['Element'] == 'Production')]

# Group the dataframe by crop and year, and then sum the values for each group
df_sum = df_crops.groupby(['Item'])[['Y2000', 'Y2005', 'Y2010', 'Y2015', 'Y2020']].sum()

# Print the result
print(df_sum)
print(df_sum.columns)










# In[19]:


import matplotlib.pyplot as plt

# Transpose the dataframe so that years become rows and crops become columns
df_transposed = df_sum.T

# Plot a line chart for each crop
for crop in df_transposed.columns:
    plt.plot(df_transposed.index, df_transposed[crop], label=crop)

# Set the title, x-axis label, and y-axis label
plt.title('Worldwide Production of Maize, Rice, Wheat, Barley, and Sorghum')
plt.xlabel('Year')
plt.ylabel('Production (tonnes)')

# Add a legend and show the chart
plt.legend()
plt.show()


# In[20]:


df_chart
print(df_chart.columns)


# In[21]:


# create a new dataframe with only the desired columns
df_largest = df_chart.loc[:, ['Item', 'Area', 'Y2020']]

# print the new dataframe
print(df_largest)
print(df_largest.columns)


# In[29]:


df_crops = df[(df['Item'].isin(['Maize (corn)', 'Rice', 'Wheat', 'Barley', 'Sorghum'])) & (df['Element'] == 'Production')]

# Group the dataframe by crop and year, and then sum the values for each group
df_sumlargest = df_crops.groupby(['Item', 'Area'])[['Y2020']].sum()


# Print the result
# Set pandas display options to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df_sumlargest


print(df_sumlargest.columns)


# In[ ]:





# In[12]:


#Remove the column that are unwanted
dg = pd.read_csv('Production_Crops_Livestock_E_All_Data.csv', encoding='ISO-8859-1', skiprows=0, nrows=61273)
print(dg)


# In[43]:


dg = pd.read_csv('Production_Crops_Livestock_E_All_Data.csv', encoding='ISO-8859-1', skiprows=0, nrows=61273)
#print(dg)


dg_crops = dg[(dg['Item'].isin(['Maize (corn)', 'Rice', 'Wheat', 'Barley', 'Sorghum'])) & (dg['Element'] == 'Production')]
#print(dg_crops)
print("here",dg_crops.columns)
# Group the dataframe by crop and year, and then sum the values for each group

dg_sumlargest = dg_crops.groupby(['Item', 'Area'])[['Y2020']].sum().reset_index()
#print(dg_sumlargest )
print("here",dg_sumlargest.columns)

# Print the result
# Set pandas display options to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
#dg_sumlargest

dg_largest = dg_sumlargest.groupby('Item').apply(lambda x: x.nlargest(4, 'Y2020')).reset_index(level=0, drop=True)
#print(dg_largest)
#(dg_largest.columns)


# In[ ]:





# In[44]:


import matplotlib.pyplot as plt

# Define the list of countries and their colors
countries = {
    "Bangladesh": "#8c564b",
    "Brazil": "#1f77b4",
    "Canada": "#ff7f0e",
    "China": "#2ca02c",
    "China, mainland": "#9467bd",
    "Ethiopia": "#e377c2",
    "Germany": "#7f7f7f",
    "India": "#d62728",
    "Nigeria": "#bcbd22",
    "Russian Federation": "#17becf",
    "Spain": "#e377c2",
    "United States of America": "#8c564b"
}

# Pivot the DataFrame to create a wide format suitable for a stacked bar chart

df_pivot = dg_largest.pivot(index='Item', columns='Area', values='Y2020')
print(df_pivot)
# Create a stacked bar chart
df_pivot.plot(kind='bar', stacked=True, color=[countries[c] for c in df_pivot.columns])

# Customize the chart with labels and titles
plt.title('Production of Top 4 Countries per Crop in 2020')
plt.xlabel('Crop')
plt.ylabel('Production (tonnes)')


# Display the chart
plt.show()


# In[55]:


dg = pd.read_csv('Production_Crops_Livestock_E_All_Data.csv', encoding='ISO-8859-1', skiprows=0, nrows=61273)
#print(dg)


dg_crops = dg[(dg['Item'].isin(['Maize (corn)', 'Rice', 'Wheat', 'Barley', 'Sorghum'])) & (dg['Element'] == 'Production')]
#print(dg_crops)
print("here",dg_crops.columns)
# Group the dataframe by crop and year, and then sum the values for each group

dg_sumlargest = dg_crops.groupby(['Item', 'Area'])[['Y2015']].sum().reset_index()
#print(dg_sumlargest )
print("here",dg_sumlargest.columns)

# Print the result
# Set pandas display options to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
#dg_sumlargest

dg_largest = dg_sumlargest.groupby('Item').apply(lambda x: x.nlargest(4, 'Y2015')).reset_index(level=0, drop=True)
#print(dg_largest)
#(dg_largest.columns)



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[56]:


import matplotlib.pyplot as plt

# Define the list of countries and their colors
countries = {
    "Australia": "#8c564b",
    "Brazil": "#1f77b4",
    "China": "#2ca02c",
    "China, mainland": "#9467bd",
    "France": "#7f7f7f",
    "Germany": "#d62728",
    "India": "#e377c2",
    "Indonesia": "#bcbd22",
    "Mexico": "#17becf",
    "Nigeria": "#ff7f0e",
    "Russian Federation": "#4e79a7",
    "United States of America": "#f28e2c"
}

# Pivot the DataFrame to create a wide format suitable for a stacked bar chart

df_pivot = dg_largest.pivot(index='Item', columns='Area', values='Y2015')

# Create a stacked bar chart
df_pivot.plot(kind='bar', stacked=True, color=[countries[c] for c in df_pivot.columns])

# Customize the chart with labels and titles
plt.title('Production of Top 4 Countries per Crop in 2015')
plt.xlabel('Crop')
plt.ylabel('Production (tonnes)')

# Move the legend to the right side
ax = plt.gca()
ax.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))

# Display the chart
plt.show()


# In[ ]:





# In[57]:


dg_crops = dg[(dg['Item'].isin(['Maize (corn)', 'Rice', 'Wheat', 'Barley', 'Sorghum'])) & (dg['Element'] == 'Production')]
#print(dg_crops)
print("here",dg_crops.columns)
# Group the dataframe by crop and year, and then sum the values for each group

dg_sumlargest = dg_crops.groupby(['Item', 'Area'])[['Y2010']].sum().reset_index()
#print(dg_sumlargest )
print("here",dg_sumlargest.columns)

# Print the result
# Set pandas display options to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
#dg_sumlargest

dg_largest = dg_sumlargest.groupby('Item').apply(lambda x: x.nlargest(4, 'Y2010')).reset_index(level=0, drop=True)
#print(dg_largest)
#(dg_largest.columns)
print(dg_largest)


# In[67]:


# Define the list of countries and their colors
countries = {
    "Bangladesh": "#FF5733",
    "Brazil": "#1F618D",
    "Canada": "#F4D03F",
    "China": "#196F3D",
    "China, mainland": "#CD5C5C",
    "Ethiopia": "#A569BD",
    "France": "#F0B27A",
    "Germany": "#6C3483",
    "India": "#DC7633",
    "Indonesia": "#7D3C98",
    "Mexico": "#C39BD3",
    "Nigeria": "#27AE60",
    "Russian Federation": "#3498DB",
    "Ukraine": "#E74C3C",
    "United States of America": "#2ECC71"
}

# Pivot the DataFrame to create a wide format suitable for a stacked bar chart
df_pivot = dg_largest.pivot(index='Item', columns='Area', values='Y2010')

# Create a stacked bar chart
df_pivot.plot(kind='bar', stacked=True, color=[countries[c] for c in df_pivot.columns])

# Customize the chart with labels and titles
plt.title('Production of Top 4 Countries per Crop in 2010')
plt.xlabel('Crop')
plt.ylabel('Production (tonnes)')
# Move the legend to the right side
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# Display the chart
plt.show()



# In[68]:


dg_crops = dg[(dg['Item'].isin(['Maize (corn)', 'Rice', 'Wheat', 'Barley', 'Sorghum'])) & (dg['Element'] == 'Production')]
#print(dg_crops)
print("here",dg_crops.columns)
# Group the dataframe by crop and year, and then sum the values for each group

dg_sumlargest = dg_crops.groupby(['Item', 'Area'])[['Y2005']].sum().reset_index()
#print(dg_sumlargest )
print("here",dg_sumlargest.columns)

# Print the result
# Set pandas display options to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
#dg_sumlargest

dg_largest = dg_sumlargest.groupby('Item').apply(lambda x: x.nlargest(4, 'Y2005')).reset_index(level=0, drop=True)
#print(dg_largest)
#(dg_largest.columns)
print(dg_largest)



# In[ ]:




