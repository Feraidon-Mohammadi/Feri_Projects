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

# ## Musterlösung: Passwort knacken (sha256)
# 
# Gegeben sei folgender Hash (den hat z.B. ein Angreifer aus unserer Kundendatenbank extrahiert): 
# 
# > `112aa01926aebb65c5e09cc0a25ce2b5cff2ec5df0e9b123510db6753557e552`
# 
# Es ist bekannt, das wir als Hash-Algorithmus sha256 verwenden.
# 
# Diesmal wissen wir aber, dass das Passwort im Dictioary ist, dem Passwort aber noch 2 Sonderzeichen angehängt sind. Wir möchten folgende Sonderzeichen betrachten: `"!$%&/()=?"`. 
# 
# Wenn du das Programm ausführst - hier muss jetzt schon einiges ausprobiert werden. Ggf. wird das Script bis zu einer Minute bei dir benötigen!
# 
# ------
# 
# <small>Rechtlicher Hinweis: Das Wörterbuch (../data/dictionary.txt) mit englischen Wörtern wurde aus dem Wordnet - Projekt extrahiert: Princeton University "About WordNet." WordNet. Princeton University. 2010. http://wordnet.princeton.edu </small>

# In[2]:


password_hash = "112aa01926aebb65c5e09cc0a25ce2b5cff2ec5df0e9b123510db6753557e552"


# In[5]:


import hashlib

extra_chars = "!$%&/()=?"

with open("../data/dictionary.txt", "r") as file:
    for line in file:
        word = line.strip()
        
        for char in extra_chars:
            for char2 in extra_chars:
                w = word + char + char2
        
                if hashlib.sha256(w.encode()).hexdigest() == password_hash:
                    print(w)

print("Programm fertig!")


