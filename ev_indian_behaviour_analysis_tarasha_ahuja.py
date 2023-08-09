#!/usr/bin/env python
# coding: utf-8

# In[91]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df1 = pd.read_csv("/Users/TT/Desktop/archive/Cheapestelectriccars-EVDatabase 2023.csv")


# In[92]:


df1.head()


# In[93]:


print(df1.columns.tolist())


# In[94]:


#filling empty data with 0

df1=df1.fillna('0')


# In[95]:


df1['Manufacturer'] = df1.Name.str.split(' ', 1, expand=True)[0]


# In[96]:


#cleaning the data

#removing currency sign

PriceinUK=[]
for item in df1['PriceinUK']:
    PriceinUK+=[int(item.replace('£','').replace(',',''))]
df1['PriceinUK']=PriceinUK


# In[97]:


PriceinGermany=[]
for item in df1['PriceinGermany']:
    PriceinGermany+=[int(item.replace('€','').replace(',',''))]
df1['PriceinGermany']=PriceinGermany


# In[98]:


FastChargeSpeed=[]
for item in df1['FastChargeSpeed']:
    FastChargeSpeed+=[int(item.replace(' km/h','').replace('-','0'))]
df1['FastChargeSpeed']=FastChargeSpeed


# In[99]:


Efficiency=[]
for item in df1['Efficiency']:
    Efficiency+=[int(item.replace(' Wh/km',''))]
df1['Efficiency']=Efficiency


# In[100]:


Range=[]
for item in df1['Range']:
    Range+=[int(item.replace(' km',''))]
df1['Range']=Range


# In[101]:


TopSpeed=[]
for item in df1['TopSpeed']:
    TopSpeed+=[int(item.replace(' km/h',''))]
df1['TopSpeed']=TopSpeed


# In[102]:


Acceleration=[]
for item in df1['Acceleration']:
    Acceleration+=[float(item.replace(' sec',''))]
df1['Acceleration']=Acceleration


# In[105]:


Subtitle = []
for item in df1['Subtitle']:
    # Extract the battery capacity part of the subtitle
    capacity_str = item.split(' ')[0]  # This assumes the capacity is the first part of the string
    # Handle the case where capacity is not numeric (e.g., '118 useable battery')
    try:
        capacity = float(capacity_str)
    except ValueError:
        capacity = None  # Assign None if conversion fails
    Subtitle.append(capacity)
df1['Subtitle'] = Subtitle


# In[106]:


df1= df1.rename(columns = {'Subtitle':'KWH'})


# In[107]:


df1.head()


# In[108]:


df1.info()


# In[109]:


df1.corr()


# In[110]:


plt.figure(figsize=(8,6))
sns.heatmap(df1.corr(), annot=True)


# In[111]:


sns.countplot(x = 'Drive', data = df1)


# In[112]:


sns.countplot(x = 'NumberofSeats', data = df1)


# In[113]:


plt.figure(figsize=(8,6))
sns.countplot(x = 'NumberofSeats', hue='Drive', data=df1)


# In[114]:


plt.figure(figsize=(18,10))
sns.countplot(y = 'Manufacturer', data = df1)


# In[115]:


sns.catplot(data=df1, kind="bar", x="NumberofSeats", y="KWH",height=6, hue="Drive")
plt.title("Vehicle KWH Compared with Number of Seats and Drive Type")
plt.show()


# In[116]:


sns.relplot(x="KWH", y="Acceleration", height=6,hue="Drive",data=df1)


# In[117]:


sns.relplot(x="KWH", y="Acceleration", size="NumberofSeats", height=6,sizes=(15, 100),data=df1)


# In[118]:


sns.relplot(x="TopSpeed", y="Range",height=6, hue="Drive",data=df1)


# In[119]:


sns.displot(
    df1, x="TopSpeed", col="Drive", 
    binwidth=3, height=7, facet_kws=dict(margin_titles=True),
)


# In[120]:


sns.displot(
    df1, x="TopSpeed", col="NumberofSeats", 
    binwidth=3, height=7, facet_kws=dict(margin_titles=True),
)


# In[121]:


#relation between price and features

sns.relplot(x="PriceinGermany", y="TopSpeed", height=6,data=df1)


# In[122]:


#relation between price and features

sns.relplot(x="PriceinUK", y="TopSpeed", height=6,data=df1)


# In[123]:


sns.jointplot(x=df1["KWH"], y=df1["Range"], kind="hex", color="#4CB391")


# In[124]:


sns.jointplot(x=df1["KWH"], y=df1["Efficiency"], kind="hex", color="#4CB391")


# In[125]:


sns.relplot(x="FastChargeSpeed", y="Efficiency", height=6,data=df1)


# In[126]:


sns.pairplot(df1[["KWH","Acceleration","TopSpeed","Range","FastChargeSpeed"]])


# In[127]:


df1.head()


# In[ ]:




