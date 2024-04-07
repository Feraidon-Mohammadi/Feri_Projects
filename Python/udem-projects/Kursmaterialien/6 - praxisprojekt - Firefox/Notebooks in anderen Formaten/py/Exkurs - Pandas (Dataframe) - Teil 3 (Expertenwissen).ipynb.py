# Diese .py - Datei wurde automatisch aus dem IPython - Notebook (.ipynb) generiert.
# 
# Gelegentlich wurde ich von Teilnehmern gefragt, ob ich die Kursmaterialien nicht 
# auch als normale .py - Datien bereitstellen könne. Dadurch ist es möglich, den Code
# ohne Jupyter zu öffnen, beispielsweise wenn Python-Programme in einem Terminal oder in 
# Eclipse entwickelt werden.
# 
# Dem möchte ich hiermit nachkommen. Ich empfehle dir aber trotzdem, schau' dir lieber die
# IPython - Notebooks direkt an, oder den HTML-Export eben dieser. Dieser reine .py-Export
# ist meiner Meinung nach etwas unübersichtlich.

# coding: utf-8

# In[2]:


import pandas as pd

df = pd.read_csv("./students.csv")


# In[3]:


df.head()


# In[5]:


pd.read_csv("./students_from_excel.csv", delimiter=";")


# In[19]:


df[(df["subject"] == "Mathe") | (df["subject"] == "Informatik")]


# In[21]:


df[(df["semester"] < 5) & (df["semester"] > 2)]


# In[23]:


cs_students = df[df["subject"] == "Informatik"]


# In[24]:


cs_students.head()


# In[25]:


cs_students[cs_students["semester"] == 4]


