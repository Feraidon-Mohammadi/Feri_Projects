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

# ## Exkurs: Beautifulsoup (XML)

# In[1]:


from bs4 import BeautifulSoup


# In[4]:


doc = """
<article from="2018-02-02">
    <heading>Große Feier in Berlin</heading>
    <content author="Max Müller">
    
    </content>
</article>
<article from="2018-02-03">
    <heading></heading>
    <content author="Monika Mustermann">
        
    </content>
</article>
"""

d = BeautifulSoup(doc, "html.parser")


# In[7]:


article = d.select("article")[0]


# In[10]:


article.attrs["from"]


# In[15]:


article.select("heading")[0].text


# In[19]:


d.select("article[from='2018-02-03']")


