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

# ## Python Crashkurs, Teil 2

# In[1]:


l = ["Max", "Monika", "Erik", "Laura"]
print(l)


# In[2]:


print(len(l))


# In[3]:


l.append("Moritz")
print(l)


# In[4]:


print(len(l))


# In[5]:


for element in l:
    print(element)


# In[8]:


sentence = "Ich bin der Satz"
print(len(sentence.split(" ")))


# In[9]:


sentence_list = ["Ich", "bin", "eine", "Liste"]
print(" ".join(sentence_list))


# In[10]:


for c in "Hallo":
    print(c)


