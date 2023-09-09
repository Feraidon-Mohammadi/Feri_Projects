# Tupel sind unveränderliche Listen

namen = ("alice", "bob", "charlie")
print(namen[0], namen[1], namen[2], namen[-1],
      namen[-2])  # alice bob charlie charlie bob
print(namen[-2:])  # die letzten 2 namen, bob und charlie
# namen[0] = "ALICE" # Überschreiben von Werten ist nicht möglich ('tuple' object does not support item assignment)
# del namen[0] Löschen ist nicht möglich (TypeError: 'tuple' object doesn't support item deletion)
# namen.append("damian") Tupel hat keine solche Methode!
print("bob" in namen)  # True
print("damian" not in namen)  # True
# Da Tupel unveränderlich sind, existiert keine sort-Methode. Allerdings kann man aus dem
# Tupel eine neue sortierte Liste erzeugen.
sortierte_namensliste = sorted(namen)
sortiertes_namenstupel = tuple(sortierte_namensliste)
print(sortierte_namensliste, sortiertes_namenstupel)

gewicht = (2, "kg")  # gewicht[0] -> Zahlenwert und gewicht[1] die Einheit
gewicht2 = (2, "t")

# Mit Tupeln lassen sich mehrere Variablen initialisieren
a, b = 1, 2  # bedeutet eigentlich: (a, b) = (1, 2)
print(a, b)
# Das Tauschen von Variablenwerten ist mit Tupeln sehr einfach.
a, b = b, a
print(a, b)
b, a = a, b
print(a, b)

# Vergleiche funktionieren analog zu Listen (Elemente mit gleichem Index werden verglichen)
print((1, 2, 3) < (2, 0))  # True
print((1, 2) < (1, 2, 3))  # True

# Erstellen spezieller Tupel
leeres_tupel = ()  # Klammern sind obligatorisch!
tupel_der_laenge_1 = (1,)  # beachte das Komma!

# Wiederholung der Funktion zip
ergebnis = list(zip("abcd", [1, 2, 3, 4], (9, 8, 7, 6)))
print(ergebnis)
# [('a', 1, 9), ('b', 2, 8), ('c', 3, 7), ('d', 4, 6)]
