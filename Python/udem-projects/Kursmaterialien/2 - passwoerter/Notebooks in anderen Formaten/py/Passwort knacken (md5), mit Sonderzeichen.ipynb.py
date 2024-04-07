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

# ## Passwort knacken (md5), mit einem Sonderzeichen
# 
# In dieser Lektion werden wir einen Dictionary - Angriff auf ein Passwort starten. Das Dictionary liegt in der Datei `../data/dictionary.txt`.
# 
# Diesmal wissen wir aber, dass das Passwort im Dictioary ist, dem Passwort aber noch ein Sonderzeichen angehängt ist. Wir möchten folgende Sonderzeichen betrachten: `"!§$%&/()=?"`
# 
# ------
# 
# <small>Rechtlicher Hinweis: Das Wörterbuch (../data/dictionary.txt) mit englischen Wörtern wurde aus dem Wordnet - Projekt extrahiert: Princeton University "About WordNet." WordNet. Princeton University. 2010. http://wordnet.princeton.edu </small>

# In[10]:


password_hash = "1e3bf495a62012e7caf5fdd25624605f"


# In[15]:




# In[16]:




