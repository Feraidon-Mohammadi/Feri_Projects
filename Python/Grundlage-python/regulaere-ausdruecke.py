import re

# Eine ausführliche Erklärung der Regular Expression Syntax
# findest du hier: https://docs.python.org/3/library/re.html#module-re

# Da wir diese Regular Expression (Pattern) häufiger
# verwenden, kompilieren wir sie in ein Format,
# welches die Regular Expression Engine ohne vorherige
# Kompilierung benutzen kann.
date_pattern = re.compile(r"\d{1,2}\.\d{1,2}\.\d{4}")

# Die Methode search findet das erste Vorkommen des Musters im Text
print(date_pattern.search("10.01.2000"))         # True
print(date_pattern.search("9.01.2000"))          # True
print(date_pattern.search("xx99.01.2000xx"))     # True!
# Die Methode match sucht das Muster am Anfang des Textes
print(date_pattern.match("xx99.01.2000xx"))      # None!
print(date_pattern.match("99.01.2000xx"))        # True!
print(date_pattern.search("99.01.2000"))         # True
print(date_pattern.search("01.2000"))            # None

# Textmuster für Vor- und Nachnamen
name_pattern = re.compile(
    r"(?P<vorname>[a-zöüäß]{2,})\s+" +
    r"(?P<nachname>[a-zöüäß]{2,})",
    flags=re.IGNORECASE)

match = name_pattern.fullmatch("Max Müller")
print(match)
print(f"'{match.group('vorname')}'")
print(f"'{match.group('nachname')}'")
print(match.groups())

# Textmuster zur Erkennung von numerischen Werten mit Einheit.
# Wir vergeben an die Gruppen (Capture Group) zusätzliche Namen, um sie später
# programmatisch einfacher auslesen zu können.
# Syntax für Gruppenbenennung: (?P<Gruppenname>Muster)
unit_pattern = re.compile(
    r"(?P<value>\d+([.,]\d+)?)\s+(?P<unit>[a-z]{1,6})", flags=re.IGNORECASE)

# fullmatch prüft, ob der gesamte Text auf das Pattern zutrifft.
match = unit_pattern.fullmatch("1280.123 KG")
allowed_units = ["g", "kg", "t", "mg", "l", "ml"]
if match is not None:
    # Ermittle den Text, den die Gruppe "value" abdeckt
    # und wandle ihn in eine Gleitkommazahl um.
    value = float(match.group("value"))
    unit = match.group("unit")
    if unit.lower() in allowed_units:
        print(value, unit)
    else:
        print(f"Unzulässige Einheit: {unit}")
