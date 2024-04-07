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

# ## Firefox - Daten auslesen
# 
# In dieser Lektion:
# 
# - Lesen wir die History sowie die Booksmarks von Firefox aus

# In[32]:


import os

profiles = os.listdir("/Users/jannisseemann/Library/Application Support/Firefox/Profiles")


# In[26]:


profile = ""

for element in profiles:
    if element[0] != ".":
        profile = element

print(profile)


# In[27]:


path = "/Users/jannisseemann/Library/Application Support/Firefox/Profiles/" + profile + "/"


# In[30]:


print(path)


