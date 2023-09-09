# Gruppieren von Daten
# https://docs.python.org/3/library/itertools.html
from itertools import groupby


liste = ["bea", "axel", "charlie", "alice",
         "fred", "damian", "elon", "egon", "bob"]

liste.sort(key=lambda name: name[0])
#sorted(liste, key=lambda name: name[0]) # liefert eine sortierte Kopie
gruppen = []
iterator = groupby(liste, key=lambda name: name[0])
# Achtung: iterator und die Gruppen-Iteratoren teilen sich die Datenquelle.
# Holt man das nächste Tupel aus iterator, ist der vorherige Gruppen-Iterator leer!     
for gruppenschluessel, gruppen_mitglieder_iterator in iterator:
    gruppen.append((gruppenschluessel, list(gruppen_mitglieder_iterator)))
# Ergebnis: [('a', ['axel', 'alice']), ('b', ['bea', 'bob']), ('c', ['charlie']), ('d', ['damian']), ('e', ['elon', 'egon']), ('f', ['fred'])]

# Alternative:
liste = ["bea", "axel", "charlie", "alice",
         "fred", "damian", "elon", "egon", "bob"]
gruppen = {} # Schlüssel ist ein Buchstabe, Wert ist eine Liste von Namen.
for name in liste:
    gruppen_schluessel = name[0]
    mitgliederliste = gruppen.get(gruppen_schluessel, [])
    mitgliederliste.append(name)
    gruppen[gruppen_schluessel] = mitgliederliste
    
print(gruppen)
print(gruppen["a"])
print(gruppen["e"])