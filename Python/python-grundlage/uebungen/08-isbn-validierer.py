import sys

#print(sys.argv)

# Haben wir weniger als zwei Argumente, hat der Nutzer vergessen
# eine ISBN anzugeben. Beachte: das erste Element ist immer der Pfad
# zum ausgeführten Skript.
if len(sys.argv) < 2:
    print("Es muss eine ISBN-13 angegeben werden!")
    # verlasse das Programm mit Ergebnis-Code 0 (fehlerfreie Ausführung)
    sys.exit(0)

# Entferne alle Bindestriche
isbn = sys.argv[1].replace("-", "")

ziffern = "0123456789"

# Zeichenketten sind Sequenzen und können somit von einer for-in-Schleife
# zeichenweise durchlaufen werden. Die Laufvariable zeichen nimmt in jedem
# Schleifendurchlauf den Wert des nächsten Zeichens der Zeichenkette an.
for zeichen in isbn:
    if zeichen not in ziffern:
        print(f"Das Zeichen {zeichen} ist keine Ziffer!")
        sys.exit(1)

if len(isbn) != 13:
    print("Ungültige Eingabe: Eine ISBN muss aus 13 Ziffern bestehen")
    sys.exit(1)

# Summiere die Ziffern auf. Ziffern, die an einer geraden Position stehen, werden
# mit zuvor mit 3 multpliziert.
summe = 0
for index in range(13):
    zeichen = isbn[index]
    ziffer = int(zeichen)
    if index % 2 != 0:
        ziffer *= 3
    summe += ziffer

# Wenn die Summe ein Vielfaches von 10 ist, handelt es sich um eine gültige ISBN.
if summe % 10 == 0:
    print("Gültig")
else:
    print("Ungültig")


