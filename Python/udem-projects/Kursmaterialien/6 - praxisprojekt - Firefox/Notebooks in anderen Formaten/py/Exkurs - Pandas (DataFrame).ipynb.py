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

# ## Exkurs: Pandas (DataFrame)

# In[16]:


import sqlite3

conn = sqlite3.connect("./database.sqlite")


# In[17]:


import pandas as pd

df = pd.read_sql("SELECT * FROM students", conn)


# In[22]:


df.head()


# In[23]:


df["firstname"]


# In[24]:


for col in df:
    print(col)


# In[32]:


df.head()


# In[35]:


for key, item in df.iterrows():
    print(item["firstname"] + " " + item["surname"])


