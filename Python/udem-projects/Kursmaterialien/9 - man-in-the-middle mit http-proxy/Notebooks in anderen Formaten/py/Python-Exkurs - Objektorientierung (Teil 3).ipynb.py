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


class Hacker:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        
    def get_name(self):
        print(self.firstname + " " + self.lastname)

hacker1 = Hacker("Max", "Müller")
hacker1.get_name()


# In[6]:


a = Hacker("Erika", "Mustermann")
a.get_name()


