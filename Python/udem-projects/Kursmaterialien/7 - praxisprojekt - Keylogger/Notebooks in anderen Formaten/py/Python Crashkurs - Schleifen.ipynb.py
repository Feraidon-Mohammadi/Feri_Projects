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

# ## Python Crashkurs: Schleifen

# In[1]:


students = ["Mark", "Monika", "Erik"]

for student in students:
    print(student)


# In[2]:


for i in range(0, 10):
    print(i)


# In[3]:


c = 5

while c < 1000:
    c = c + 100

print(c)


# In[5]:


c = 5
while c > 0:
    c = c + 100


