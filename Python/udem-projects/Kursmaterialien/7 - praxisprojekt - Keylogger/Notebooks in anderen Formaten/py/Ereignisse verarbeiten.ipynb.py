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


import keyboard

keyevents = keyboard.record(until="Esc")


# In[3]:


# hallo welt


# In[4]:


print(keyevents)


# In[7]:


for key in keyboard.get_typed_strings(keyevents, allow_backspace = False):
    print(key)


# In[8]:


keyevents = keyboard.record(until="Esc")


# In[9]:


# HALLO Hallo !!!


# In[10]:


for key in keyboard.get_typed_strings(keyevents, allow_backspace = False):
    print(key)


# In[11]:


for keyevent in keyevents:
    print(keyevent)


