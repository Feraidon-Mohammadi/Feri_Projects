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

# ## Exkurs Python: Funktionen

# In[5]:


def f():
    print("Hallo Welt")
    print("Hallo Welt")


# In[6]:


f()


# In[7]:


f()


# ## Exkurs Python: Auf Variablen zugreifen

# In[24]:


sentence = "Hallo Welt"

def multiple_print():    
    print(sentence)
    print(sentence)
    print(sentence)
    print(sentence)
    print(sentence)
    


# In[25]:


multiple_print()


# In[27]:


sentence = "Hallo Welt123"
multiple_print()


# ## Exkurs Python: Auf Variablen zugreifen

# In[29]:


def multiple_print(sentence, name):
    print(sentence)
    print(sentence)
    print(sentence)
    print(sentence)
    print(sentence)
    print(name)
    
multiple_print("Hallo Welt", "NAME!!!")


# In[30]:


multiple_print("Hallo Mars", "-- Elon Musk")


