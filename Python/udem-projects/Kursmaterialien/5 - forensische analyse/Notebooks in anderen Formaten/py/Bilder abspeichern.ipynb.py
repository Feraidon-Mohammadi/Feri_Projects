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
# - Speichern wir die Bilder auf unserer Festplatte

# In[11]:


import requests
import urllib

from bs4 import BeautifulSoup

url = "http://python.vic-tim.de/images/"
response = requests.get(url)

found_images = []
if response.status_code == 200:
    
    doc = BeautifulSoup(response.text, "html.parser")
    
    images = doc.find_all("img")
    
    for img in images:
        path = urllib.parse.urljoin(url, img.attrs["src"])
        found_images.append(path)


# In[10]:


import os

if not os.path.exists("./images"):
    os.mkdir("./images")


# In[25]:


for found_image in found_images: 
    filename = found_image.split("/")[-1]
    
    response = requests.get(found_image)
    with open("./images/" + filename, "wb") as file:
        file.write(response.content)


