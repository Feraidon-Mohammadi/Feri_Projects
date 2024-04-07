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

# ## Bilder herunterladen + Metadaten auslesen
# 
# In dieser Lektion: 
# 
# - Lädst du den HTML - Code der Seite herunter

# In[1]:


url = "http://python.vic-tim.de/images/"


# In[2]:


# python-requests.org

import requests


# In[5]:


response = requests.get(url)

if response.status_code == 200:
    
    print(response.text)


