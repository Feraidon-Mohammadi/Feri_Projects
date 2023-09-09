# Teilaufgabe 1

import re


def laenge(zeichenkette):
    anzahl_zeichen = 0
    for zeichen in zeichenkette:
        anzahl_zeichen += 1
    return anzahl_zeichen


def laenge2(zeichenkette):
    return sum([1 for zeichen in zeichenkette])


print(laenge("abc"))
print(laenge2("abc"))
print(len("abc"))

# Teilaufgabe 2


def to_upper(zeichenkette):
    # Idee: Verwende eine Abbildungstabelle.
    # Diese hier ist natürlich unvollständig.
    klein_nach_groß = {
        "a": "A",
        "b": "B",
        "c": "C"
    }
    ergebnis = ""
    for zeichen in zeichenkette:
        # Suche nach dem Wert des Schlüssels zeichen.
        # Falls dieser nicht existiert, benutze
        # zeichen als Ersatzwert.
        ergebnis += klein_nach_groß.get(zeichen, zeichen)
    return ergebnis


print("abc".upper())
print(to_upper("aBcd"))

# Teilaufgabe 3
print("Teilaufgabe 3")
print("=" * 20)
# Hinweis: in und not in funktionieren auch bei Listen, Tupeln, Dictionaries und Sets.
print("a" in "abc")     # True
print("d" not in "abc")  # True
print("e" in "abc")     # False
print("bb" in "abba")   # True

print(re.search("a", "abc") is not None)                        # True
print(re.search("a", "Abc", flags=re.IGNORECASE) is not None)   # True
print(re.search("d", "Abc") is not None)                        # False

print("abc".count("a") > 0)                                     # True
print("abc".find("a") >= 0)                                     # True


def enthält_zeichen(zeichenkette, gesuchtes_zeichen):
    for zeichen in zeichenkette:
        if zeichen == gesuchtes_zeichen:
            return True
    return False


print(enthält_zeichen("abc", "b"))                              # True
print(enthält_zeichen("abc", "d"))                              # False

# Teilaufgabe 4

# Hinweis: Es gibt keine Garantie, in welcher Reihenfolge die Elemente eines Sets
# zurückgegeben werden!


def distinct_characters(text: str) -> list[str]:
    # Idee: Erzeuge eine Menge anhand des Textes. Konstruiere anschließend eine
    # Liste der Mengenelemente.
    zeichenmenge = set(text)
    return list(zeichenmenge)


print(distinct_characters("abbac"))

# Teilaufgabe 5

# Berechne die Quadratzahlen von 1 bis 10.
quadrate = [zahl * zahl for zahl in range(1, 11)]
# Wandle jede Quadratzahl in eine Zeichenkette um.
quadrate_zeichenketten = [str(zahl) for zahl in quadrate]
print(",".join(quadrate_zeichenketten))  # 1,4,9,16,25,36,49,64,81,100

# Teilaufgabe 6


def frequency(zeichenkette: str) -> dict[str, int]:
    zeichentabelle = {}
    for zeichen in zeichenkette:
        if zeichen not in zeichentabelle:
            zeichentabelle[zeichen] = 1
        else:
            zeichentabelle[zeichen] += 1
    return zeichentabelle


zeichentabelle = frequency("abbac 123123")
# {'a': 2, 'b': 2, 'c': 1, ' ': 1, '1': 2, '2': 2, '3': 2}
print(zeichentabelle)

abstand = " " * 10
spalte_buchstaben = "BUCHSTABEN"
breite_buchstaben = len(spalte_buchstaben)
spalte_haeufigkeit = "HÄUFIGKEIT"
breite_haufigkeit = len(spalte_haeufigkeit)
print(spalte_buchstaben, spalte_haeufigkeit, sep=abstand)

for buchstabe, haeufigkeit in zeichentabelle.items():
    print(f"{buchstabe:^{breite_buchstaben}}",
          abstand,
          f"{haeufigkeit:>{breite_haufigkeit}}",
          sep="")

# Teilaufgabe 7

def decompose_line(line):
    date_pattern = r"(?P<date>\d{2}\.\d{2}\.\d{4})"
    time_pattern = r"(?P<time>\d{2}:\d{2})"
    category_pattern = r"(?P<category>[a-zA-Z_]{2,})"
    message_pattern = r'(?P<message>".*")'
    line_pattern = rf"{date_pattern}\s+{time_pattern}\s+{category_pattern}\s+{message_pattern}"

    match = re.fullmatch(line_pattern, line)
    if match is None:
        return None
    
    return (match.group("date"), match.group("time"), match.group("category"), match.group("message"))

log_file = open(r'./uebungen/14-log.txt', 'rt', encoding="utf-8")
for line_number, line in enumerate(log_file, start=1):
    line_parts = decompose_line(line.strip())
    if line_parts is None:
        print(f"Zeile {line_number} ist fehlerhaft!")
        continue
    date, time, category, message = line_parts
    print(category, time, date, message)
log_file.close()