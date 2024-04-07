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

# In[16]:


import sqlite3
import pandas as pd

from helper import get_firefox_path

path = get_firefox_path("places.sqlite")
conn = sqlite3.connect(path)

bookmarks = pd.read_sql("SELECT * FROM moz_bookmarks", conn)


# In[18]:


places = pd.read_sql("SELECT * FROM moz_places", conn)


# In[19]:


places.head()


# In[21]:


bookmarks


# In[44]:


for key, bookmark in bookmarks[bookmarks["fk"] > 0].iterrows():
    title = bookmark["title"]
    url = places[places["id"] == int(bookmark["fk"])].iloc[0]["url"]
    
    print(title + ": " + url)
    


