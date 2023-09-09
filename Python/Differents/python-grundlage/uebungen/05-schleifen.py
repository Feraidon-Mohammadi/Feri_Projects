for zahl in range(1, 6):
    print(f"{zahl} ", end="")

print()

for zahl in range(5, 0, -1):
    print(f"{zahl} ", end="")

print()

for zahl in range(1, 10, 2):
    print(f"{zahl} ", end="")

print()

for zahl in range(9, 0, -2):
    print(f"{zahl} ", end="")

print()

for zahl in range(1, 7):
    if zahl % 2 == 0:
        zahl *= -1
    print(f"{zahl} ", end="")

print()

# Äußere Schleife durchläuft die Zeilenlängen von 1 bis 4
for laenge in range(1, 5):
    # Die innere Schleife gibt eine komplette Zeile aus
    for i in range(laenge):
        print("* ", end="")
    print()

for laenge in range(4, 0, -1):
    for i in range(laenge):
        print("* ", end="")
    print()

# Alternative Lösung ohne Verwendung von verschachtelten Schleifen
for laenge in range(4, 0, -1):
    zeile = "* " * laenge
    print(zeile)

# Ausgabe von Zahlen statt Sternen.
for laenge in range(4, 0, -1):
    for zahl in range(1, laenge + 1):
        print(f"{zahl} ", end="")
    print()

# Multiplikationstabelle
for zeile in range(1, 11):
    for spalte in range(1, 11):
        produkt = zeile * spalte
        print(f"{produkt:02} ", end="")
    print()