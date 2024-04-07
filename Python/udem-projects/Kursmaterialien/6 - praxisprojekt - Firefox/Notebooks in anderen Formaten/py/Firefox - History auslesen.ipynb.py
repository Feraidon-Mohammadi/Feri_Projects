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

# ## Weiteres Beispiel: Firefox-History auslesen

# In[22]:


import sqlite3
import pandas as pd

from helper import get_firefox_path

path = get_firefox_path("places.sqlite")
conn = sqlite3.connect(path)

history = pd.read_sql("SELECT * FROM moz_historyvisits", conn)
places = pd.read_sql("SELECT * FROM moz_places", conn)


# In[23]:


history.head()


# In[25]:


places.head()


# In[43]:


# https://docs.python.org/3.6/library/datetime.html?highlight=datetime#strftime-and-strptime-behavior
import datetime

for key, item in history.iterrows():
    place_id = item["place_id"]
    url = places[places["id"] == place_id].iloc[0]["url"]
    
    timestamp = datetime.datetime.fromtimestamp(item["visit_date"] / 1000000)
    
    print(timestamp.strftime("%d.%m.%Y %H:%M") + " - " + url)


