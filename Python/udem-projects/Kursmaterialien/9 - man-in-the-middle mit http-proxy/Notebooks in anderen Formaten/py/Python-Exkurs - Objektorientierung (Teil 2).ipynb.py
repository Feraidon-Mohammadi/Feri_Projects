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

# In[12]:


class Hacker:
    def get_name(self):
        print(self.firstname + " " + self.lastname)

hacker1 = Hacker()
hacker1.firstname = "Max"
hacker1.lastname = "Müller"

hacker1.get_name()


# In[13]:


class Company:
    def get_name(self):
        print(self.name)
        
c = Company()
c.name = "Hacking GmbH"
c.get_name()


# In[18]:


participants = [
    hacker1,
    c
]

for participant in participants:
    participant.get_name()


