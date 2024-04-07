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

# ## EXIF - Informationen (Metadaten) aus Bildern auslesen
# 
# Mit dem Python - Modul "exifread" können wir EXIF - Metadaten aus Bildern auslesen.
# 
# Das müssen wir aber noch kurz installieren:

# In[5]:




# In[26]:


print(192/5)


# In[24]:


import exifread

with open("./images/img-1.jpg", "rb") as file:
    tags = exifread.process_file(file)
    for key, value in tags.items():
        print(str(key) + ": " + str(value))
        
# 28°12'37.14"N 16°39'38.4"W


