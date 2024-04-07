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

# ## Python-Exkurs: Objektorientierung (Teil 1)

# In[1]:


hacker1 = {"firstname": "Max", "lastname": "Müller"}


# In[2]:


hacker1["firstname"]


# In[3]:


def hacker_get_name(hacker):
    print(hacker["firstname"] + " " + hacker["lastname"])


# In[4]:


hacker_get_name(hacker1)


# In[5]:


company1 = {"name": "Hacking GmbH"}
def company_get_name(company):
    print(company["name"])
    
company_get_name(company1)


# In[11]:


participants = [
    {"type": "person", "firstname": "Max", "lastname": "Müller"},
    {"type": "company", "name": "Hacking GmbH"}
]


# In[13]:


for participant in participants:
    if participant["type"] == "person":
        hacker_get_name(participant)
    else:
        company_get_name(participant)


