# Importiere das Modul namens random. Es enthält eine Funktion namens
# choice, die wir für die Generierung der MAC Adresse benötigen.
import random
import sys

# Syntax für Variablendeklaration:
# variable = wert

# Erzeuge eine zufällige Hexadezimalzahl der Länge `num_digits`.


def generate_hex_number(num_digits):
    # Beachte: Zeichenketten sind unveränderlich (immutable)
    # Zeichenketten sind Sequenzen und lassen sich zeichenweise
    # durchlaufen.
    hex_digits = "0123456789abcdef"
    number = ""
    # Laufvariable i durchläuft nacheinander die Werte 0, 1, ..., num_digits-1
    for i in range(num_digits):
        number += random.choice(hex_digits)
        #number = number + random.choice(hex_digits)
    return number


def generate_mac_address():
    address = ""
    for i in range(6):
        address += generate_hex_number(2) + "-"
    return address[0:-1]  # schneidet letztes Zeichen ab


print(generate_mac_address())
