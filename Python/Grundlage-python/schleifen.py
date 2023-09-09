alphabet = "abcdefghijklmnopqrstuvwxyzöüäß"
zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rgb_code = (255, 100, 200)
geschlechter = { "m": "männlich", "w": "weiblich", "d": "divers" }

for buchstabe in alphabet:
    print(f"Der Buchstabe {buchstabe} hat die Kodierung {ord(buchstabe)}.")

for zahl in zahlen:
    print(f"Das Quadrat von {zahl} ist {zahl * zahl}")

for code in rgb_code:
    # Gib den Code als Hexadezimalzahl aus.
    # Hänge keinen Zeilenumbruch an die Ausgabe an.
    print(f"{code : X} ", end="")

print()
# Durchläuft man ein Dictionary, erhält man nur dessen Schlüssel.
# Um die Schlüssel-Wert-Paare eines Dictionaries zu durchlaufen,
# muss man die Methode items verwenden.
for kuerzel, bezeichnung in geschlechter.items():
    # die Variable geschlecht besteht aus zwei Komponenten
    # die erste Komponente speichern wir in kuerzel und die zweite in langform
    # kuerzel, langform = geschlecht
    print(f"Das Kürzel {kuerzel} steht für das Geschlecht {bezeichnung}")

# print(geschlechter.keys())
# print(geschlechter.values())

for kuerzel in geschlechter.keys():
    print(kuerzel)

for bezeichnung in geschlechter.values():
    print(bezeichnung)

# Gib alle Zahlen im Bereich 5 bis 10 aus
# Die Funktion range gibt ein Objekt zurück, welches iterable ist.
# Iterable bedeutet, dass es sich um eine aufzählbare Menge handelt.
# Listen, Tupel, Dictionaries, Sets und Strings sind z.B. iterable.
for zahl in range(5, 10 + 1, 1):
    # print(f"{123.23556:10.2f} ", end="")
    print(f"{zahl} ", end="")