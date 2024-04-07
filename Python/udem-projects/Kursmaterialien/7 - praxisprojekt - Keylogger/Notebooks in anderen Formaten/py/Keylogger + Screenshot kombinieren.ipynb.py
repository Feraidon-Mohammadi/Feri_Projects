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

# In[1]:


import keyboard


# In[10]:


keyboard.unhook_all()

file = open("./log.txt", "w", encoding="utf-8")

def on_key(key):
    file.write(str(key.__dict__) + "\n")
    file.flush()

keyboard.hook(on_key)


# In[ ]:


import datetime
import pyautogui
import time
import os

if not os.path.exists("./screenshots"):
    os.mkdir("./screenshots")

while True:
    time.sleep(10)
    current = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = "./screenshots/" + current + ".jpg"
    pyautogui.screenshot(filename)


