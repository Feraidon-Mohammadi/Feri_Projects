# Referenzdokumentation:
# https://docs.python.org/3/tutorial/datastructures.html

from itertools import groupby


# eine Liste kann beliebige (heterogene) Werte speichern.
liste = [1, 2.3, "abc", [1, 2]]
print(liste[1])                 # ein Element an Position 1 lesen
print(liste[-1])                # gib letztes Element zurück
print(liste[-2])                # gib vorletztes Element zurück
liste[1] = 10.1                 # ein Element an Position 1 überschreiben
print(len(liste))               # die Anzahl der Elemente in der Liste ermitteln
liste.append("neu")             # ein Element an das Ende einer Liste anfügen
liste += ["alf", "bea"]         # die Elemente einer anderen Liste anhängen
# Hinweis:
# liste.append(["alf", "bea"]) fügt lediglich _ein_ Element (die Liste selbst) ans Ende an.
liste.extend(["bob", "egon"])   # ist äquivalent zu liste += ["bob", "egon"]
liste.clear()                   # alle Elemente aus einer Liste entfernen
liste = ["alice", "bob", "chris", "damian"]
liste.pop()                     # entfernt letztes Element ("damian")
liste.pop(1)                    # entfernt Element an Position 1 ("bob")
liste.pop(0)                    # entfernt erstes Element ("alice")
liste = ["alice", "bob", "chris", "damian"]
liste.insert(0, "max")          # füge Element "max" vor "alice" ein
liste.insert(2, "jan")          # füge Element "jan" vor "bob" ein
liste = []
liste.insert(0, "alice")        # fügt "alice" an Position 0 ein
liste = ["alice", "bob", "chris", "damian"]
# sucht nach Element "chris" und gibt dessen Position (2) zurück
print(liste.index("chris"))
# Hinweis: die Suche beginnt bei Position 0
# Es wird nur die Position des ersten gefundenen Elementes zurückgegeben.
# sucht "bob" beginnend ab Position 2 (liefert ValueError)
liste.index("bob", 2)
liste = ["alice", "bob", "charlie", "damian"]
# sucht "charlie" im Indexbereich [0, 2) (Pos. 2 nicht enthalten)
liste.index("charlie", 0, 2)
liste = ["alice", "charlie", "alice"]
liste.count("alice")            # ermittelt wie oft "alice" vorkommt (2x)
liste.count("damian")           # 0x
liste = ["alice", "charlie", "alice"]
liste.remove("alice")           # entfernt erstes Vorkommen von "alice"
liste = ["alice", "bob", "charlie"]
liste.reverse()                 # kehrt die Reihenfolge der Elemente um
liste = ["alice", "bob", "charlie"]
kopie = liste.copy()            # erzeugt eine "flache" Kopie
liste = [1, 4, 2, 10, 3]
liste.sort()                    # sortiert die Elemente aufsteigend
liste.sort(reverse=True)        # sortiert die Elemente absteigend
liste = ["alice", "bob", "charlie"]


def laenge(zeichenkette):
    return len(zeichenkette)


# sortiere Elemente anhand ihrer Zeichenlänge
liste.sort(key=laenge)
# Ergebnis: ['bob', 'alice', 'charlie']
# sortiert Elemente anhand ihrer Länge absteigend
liste.sort(key=len, reverse=True)
# Ergebnis: ['charlie', 'alice', 'bob']

print("alice" in liste)             # ist "alice" in der Liste enthalten? True
# ist "damian" _nicht_ in der Liste enthalten? True
print("damian" not in liste)

# + hängt zwei Listen aneinander.Ergebnis ist eine _neue_
[1, 2, 3] + [4, 5, 6]
# Liste. Ergebnis: [1,2,3,4,5,6]

liste = ["alice", "bob", "charlie"]
del liste[1]                        # entfernt Element an Position 1 ("bob")

liste = ["alice", "bob", "charlie", "damian", "elon", "fred"]
del liste[1:4]                      # entfernt "bob", "charlie" und "damian"

liste = ["alice", "bob", "charlie", "damian", "elon", "fred"]
# entferne jedes zweite Element, beginnend an Position 0.
del liste[::2]

[1, 2, 3] == [1, 2, 3]              # vergleiche Elemente positionsweise (True)
[1, 2, 3] == [3, 1, 2]              # False, da Reihenfolge falsch
[1, 2, 3] != [3, 1, 2]              # True, da beide Listen ungleich
[2, 3] > [2, 1]                     # True, da 3 > 1 an Position 1
[2, 3] > [2]                        # True, da erste Liste länger
[2, 3] > [2, 4, 5]                  # False, da 3 < 4 an Position 1

liste = ["alice", "bob", "charlie", "damian", "elon", "fred"]
# ersetzt "bob", "charlie", "damian" durch "zack", "yvonne"
liste[1:4] = ["zack", "yvonne"]
# Ergebnis: ['alice', 'zack', 'yvonne', 'elon', 'fred']

liste = ["alice", "bob", "charlie", "damian", "elon", "fred"]
liste[1:3] = []                     # entfernt "bob" und "charlie"
# Ergebnis: ['alice', 'damian', 'elon', 'fred']

liste = ["alice", "bob", "charlie", "damian", "elon", "fred"]


def mein_filter(name):
    return len(name) >= 5


# rufe für jedes Element der liste die Filterfunktion
iterator = filter(mein_filter, liste)
# mein_filter auf. Gibt mein_filter True zurück,
# landet das Element in der Ergebnismenge, andernfalls
# wird es in der Ergebnismenge ausgelassen.
# Hinweis: die Funktion filter liefert nur einen Iterator zurück. Die liste wird schrittweise
# gefiltert, wenn ein "Verbraucher" (z.B. eine for-Schleife oder die Funktion list) gefilterte
# Elemente vom iterator anfordert. Es wäre unklug eine Liste aus 1 Mio. Elementen in einem "Ruck"
# zu filtern, da dies enorm viel Rechen und Speicherkapazität erfordern würde.
# Stattdessen filtert man die Elemente "nach Bedarf", wenn es "an der Zeit ist".
# Stelle dir also vor, dass du eine 4GB Datei zeilenweise verarbeiten möchtest, aber nur bestimmte
# Zeilen für dich von Interesse sind. Du müsstest die 4GB Datei komplett in den Speicher laden,
# dann filtern um die gefilterten Zeilen zu erhalten.
# Besser wäre folgendes: Du liest nur die erste Zeile. Du schaust ob diese Zeile für dich
# relevant ist. Falls ja, machst du etws damit, ansonsten entfernst du sie aus dem Arbeitsspeicher.
# Anschließend lädst du die nächste Zeile aus der Datei in den Arbeitsspeicher und verfährst
# analog.

gefilterte_namen = list(iterator)       # list ist ein "Verbraucher",
# der _alle_ Elemente des iterators _sofort_ anfordert.

# Alternative: der Verbraucher ist hier eine for-Schleife. Sie fordert immer nur das _nächste_ verfügbare
# Element vom iterator an. Wird die Schleife vorzeitig verlassen, dann werden auch nicht alle Elemente
# des Iterators notwendigerweise "konsumiert".
# for name in iterator:
#     print(name)

# Mit einer List-Comprehension können wir _gleichzeitig_ filtern und transformieren.
# Die folgende Anweisung erstellt eine Liste von Namen, deren Länge >= 5 ist und
# transformiert anschließend die Namen in Großbuchstaben.
gefilterte_namen = [name.upper() for name in liste if len(name) >= 5]
# Ergebnis: ['ALICE', 'CHARLIE', 'DAMIAN']

# Mit map(transformationsfunktion, iterableObject) können wir die Elemente eines iterierbaren
# Objektes elementweise transformieren/abbilden/umformen.
liste = ["alice", "bob", "charlie", "damian", "elon", "fred"]
# erzeugt eine Liste mit den Längen der Namen
iterator = map(len, liste)
# Beachte: wir erhalten zunächst nur einen Iterator!

# Mit zip lassen sich zwei oder mehrere iterierbare Objekte miteinander "verschmelzen".
# Ein Element von Liste1 und ein Element von Liste2 werden zu einem Pärchen zusammengeführt.
# Der Vorgang endet, sobald eine Liste "verbraucht" ist.
liste = ["alice", "bob", "charlie", "damian", "elon", "fred"]
iterator = zip(liste, range(1, len(liste)+1))
name_position_liste = list(iterator)
# Ergebnis: [('alice', 1), ('bob', 2), ('charlie', 3), ('damian', 4), ('elon', 5), ('fred', 6)]

liste = ["alice", "bob", "charlie", "damian", "elon", "fred"]
erster, zweiter, *rest = liste
# erster = "alice" zweiter = "bob" rest = ["charlie", "damian", "elon", "fred"]