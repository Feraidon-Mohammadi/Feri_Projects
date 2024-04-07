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

# ## Passwort knacken (md5)
# 
# In dieser Lektion werden wir einen Dictionary - Angriff auf ein Passwort starten. Das Dictionary liegt in der Datei `../data/dictionary.txt`.
# 
# ------
# 
# <small>Rechtlicher Hinweis: Das Wörterbuch (../data/dictionary.txt) mit englischen Wörtern wurde aus dem Wordnet - Projekt extrahiert: Princeton University "About WordNet." WordNet. Princeton University. 2010. http://wordnet.princeton.edu </small>

# In[5]:


password_hash = "9e083ec666c9f3db044bb7c38164 0227"


# Zuerst schauen wir uns an, wie wir einen md5 - Hash berechnen können. Das geht mit dem Python - Modul `hashlib` (https://docs.python.org/3.6/library/hashlib.html):

# In[24]:


import hashlib

hashlib.md5("Hallo Welt".encode()).hexdigest()


# Anschließend lesen wir die Datei Zeile für Zeile ein:

# In[36]:


with open("../data/dictionary.txt", "r") as file:
    for line in file:
        word = line.strip()
        print(word)
        break


# Jetzt bauen wir beides zusammen:

# In[6]:


import hashlib

with open("../data/dictionary.txt", "r") as file:
    for line in file:
        word = line.strip()
        
        if hashlib.md5(word.encode()).hexdigest() == "9e083ec666c9f3db044bb7c381640227":
            print(word)
            break

print("Programm fertig!")


