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


# In[2]:


datetime.datetime.fromtimestamp(1512121241)


# In[3]:


datetime.date.fromtimestamp(1512121241)


# In[5]:


from datetime import date

date.fromtimestamp(1512121241)


# In[6]:


from datetime import datetime

datetime.fromtimestamp(1512121241)


# In[7]:


from datetime import datetime as dt

dt.fromtimestamp(1512121241)


