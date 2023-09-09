# https://docs.python.org/3/library/stdtypes.html#set

# Ein Set ist eine ungeordnete Menge von Elementen ohne Doppelgänger.
leere_menge = set() # {} würde als Dictionary interpretiert!
zahlenmenge = {1, 2, 3, 3, 2, 1, 0} 
print(zahlenmenge)
# {0, 1, 2, 3}
namen = { "alice", "bob", "charlie" }
namen.add("bob") # hat keinen Effekt, da bob bereits vorhanden
namen.remove("bob") # entfernt bob sofern vorhanden, andernfalls Fehler.
namen.discard("bob") # entfernt bob, sofern vorhanden, andernfalls _kein_ Fehler
namen.clear() # entfernt alle Elemente
namen.copy() # erzeugt flache Kopie
# update fügt die Elemente aller angegebenen Iterables zur Set hinzu
namen.update(["martin", "tobias", "kevin"], ["max", "bea"])
namen.update(["kevin", "ron"])
namen |= set(["george", "henry", "isaac"]) # | steht für "Vereinigung" (union)
namen = namen.union(["jack", "keanu", "larry", "marge"], ("nora", "oprah"))
# namen.update("kevin") Achtung: Die Zeichenkette ist ein Iterable. Also werden die einzelnen
# Buchstaben zur Set hinzugefügt.
print(namen, len(namen))
# namen.pop() # entfernt ein zufällig gewähltes Element und gibt es zurück
