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

# ## Exkurs: Beautifulsoup

# In[1]:


from bs4 import BeautifulSoup


# In[21]:


doc = """
<p>Ich bin ein <strong>Absatz</strong></p>
<p>Ich bin ein <strong id="important">Absatz</strong></p>
<p>Ich bin ein <strong class="urgent">Absatz</strong></p>

<strong class="urgent">Fettschrift</strong>
"""

print(doc)


# In[22]:


d = BeautifulSoup(doc, "html.parser")


# In[23]:


d.select("#important")


# In[24]:


d.select(".urgent")


