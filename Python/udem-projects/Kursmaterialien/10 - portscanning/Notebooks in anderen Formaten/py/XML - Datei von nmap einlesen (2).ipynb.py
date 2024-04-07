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


from bs4 import BeautifulSoup

with open("./nmap.xml", "r") as file:
    content = file.read()
    
    doc = BeautifulSoup(content, "html.parser")
    
    nmaprun = doc.select("nmaprun")[0]
    print(nmaprun.attrs["args"])
    print(nmaprun.attrs["startstr"])
    
    print("------------------------")
    
    hosts = doc.select("host[endtime]")

    print(len(hosts))
    
    for host in hosts:
        mac = host.select("address[addrtype='mac']")
        if len(mac):
            print(mac[0].attrs["vendor"])
        else:
            print("Mac-Adresse nicht gefunden")


