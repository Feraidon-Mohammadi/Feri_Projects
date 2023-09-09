from mimetypes import init
from typing import List, AnyStr

# Teilaufgabe 1

obergrenze = 100

#siebener_reihe = [7 * i for i in range(14 + 1)]
siebener_reihe = [zahl for zahl in range(0, obergrenze+1, 7)]
print(siebener_reihe)

reihe = []
for zahl in range(0, obergrenze+1, 7):
    reihe.append(zahl)

print(reihe)

# Teilaufgabe 2

VOKALE = "aeiou"
extrahierte_vokale = [
    zeichen for zeichen in "Hello, World!" if zeichen.lower() in VOKALE]
print("".join(extrahierte_vokale))

# Teilaufgabe 3


def maximale_wortlänge(wortliste: List[AnyStr]):
    wortliste = wortliste.copy()            # die Originalliste soll unberührt bleiben
    # sortiere absteigend nach Wortlänge
    wortliste.sort(key=len, reverse=True)
    # nach der Sortierung ist erstes Element das längste
    laengstes_wort = wortliste[0]
    # Rückgabe eines Tupels: Länge und Wort
    return len(laengstes_wort), laengstes_wort


namensliste = ["alice", "bob", "charlie", "damian", "elon", "fred"]
laenge, wort = maximale_wortlänge(namensliste)
print(f"Das längste Wort ist {wort} mit einer Länge von {laenge} Zeichen.")
# print(namen)


def maximale_wortlänge_ohne_sort(wortliste: List[AnyStr]):
    max_wort = wortliste[0]
    # durchlaufe die Wortliste ab dem zweiten Element
    for wort in wortliste[1:]:
        if len(wort) > len(max_wort):
            max_wort = wort
    return len(max_wort), max_wort


namensliste = ["alice", "bob", "charlie", "damian", "elon", "fred"]
laenge, wort = maximale_wortlänge_ohne_sort(namensliste)
print(f"Das längste Wort ist {wort} mit einer Länge von {laenge} Zeichen.")

# Teilaufgabe 4

# def erster_buchstabe_des_nachnamens(initalie):
#     return initalie[-1]

personen = [("Max", "Müller"), ("Egon", "Olsen"),
            ("Rainer", "Zufall"), ("Rosa", "Schlüpfer")]
initialien = [f"{vorname[0]}.{nachname[0]}".upper()
              for vorname, nachname in personen]
initialien.sort(key=lambda initialie: initialie[-1], reverse=True)
print(initialien)

# Teilaufgabe 5

namensliste = ["alice", "bob", "charlie", "damian", "elon", "fred"]
namensliste.sort(key=lambda name: name[-1], reverse=True)
#namen = [name[0].upper() + name[1:] for name in namen]
namensliste = [name.capitalize() for name in namensliste]
print(namensliste)
namensliste = [name for name in namensliste if len(
    [buchstabe for buchstabe in name if buchstabe.lower() in "aeiou"]) >= 2]
print(namensliste)

# Alternative Lösung für das Filtern nach Vokalanzahl
namensliste = ["alice", "bob", "charlie", "damian", "elon", "fred"]
gefilterte_namen = []
for name in namensliste:
    anzahl_vokale = 0
    for buchstabe in name:
        if buchstabe.lower() in "aeiou":
            anzahl_vokale += 1
    if anzahl_vokale >= 2:
        gefilterte_namen.append(name)

print(gefilterte_namen)