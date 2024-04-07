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

# In[1]:


import datetime


# In[3]:


datum = datetime.datetime.fromtimestamp(1512043274.1808052)


# In[5]:


datum.hour


# Dokumentation: https://docs.python.org/3/library/datetime.html#datetime.datetime.year

# In[10]:


datum.strftime("%d.%m.%Y %H:%M:%S")


# Weitere Informationen zu strftime: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

