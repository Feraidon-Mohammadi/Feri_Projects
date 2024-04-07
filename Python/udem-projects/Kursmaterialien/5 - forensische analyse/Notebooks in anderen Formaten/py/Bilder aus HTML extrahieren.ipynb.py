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
# - Extrahieren wir die Bilder aus dem HTML - Code
# 
# Dazu verwenden wir Beautiful Soup (https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

# In[18]:


import requests
from bs4 import BeautifulSoup

url = "http://python.vic-tim.de/images/"
response = requests.get(url)
if response.status_code == 200:
    
    doc = BeautifulSoup(response.text, "html.parser")
    
    images = doc.find_all("img")
    
    for img in images:
        print(img.attrs["src"])


