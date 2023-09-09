import random
import re

# Diese Konstanten definieren die zu verwendenden Zeichensätze
# Man kann hier auch die Konstanten aus dem Modul string verwenden,
# z.B. string.digits bzw. string.ascii_lowercase
KLEINBUCHSTABEN = "abcdefghijklmnopqrstuvwxyzöüäß"
GROSSBUCHSTABEN = KLEINBUCHSTABEN.upper()
ZIFFERN = "0123456789"
SONDERZEICHEN = "!#$_*"
ALLE_ZEICHEN = KLEINBUCHSTABEN + GROSSBUCHSTABEN + ZIFFERN + SONDERZEICHEN
MINIMALE_PASSWORTLAENGE = 4

# Reguläre Ausdrücke zum Prüfen der Passwortrichtlinie
KLEINBUCHSTABEN_PATTERN = r"[a-zöüäß]"
GROSSBUCHSTABEN_PATTERN = r"[A-ZÖÜÄ]"
ZIFFERN_PATTERN = r"[0-9]"
SONDERZEICHEN_PATTERN = r"[!$_*#]"


# Diese Variante der Passwortüberprüfung verwendet reguläre Ausdrücke.
def ist_gueltiges_passwort3(passwort):
    if len(passwort) < MINIMALE_PASSWORTLAENGE:
        return False

    for pattern in [KLEINBUCHSTABEN_PATTERN, GROSSBUCHSTABEN_PATTERN, ZIFFERN_PATTERN, SONDERZEICHEN_PATTERN]:
        if re.search(pattern, passwort) is None:
            return False

    return True


# Diese Variante der Passwortüberprüfung verwendet List-Comprehensions in Kombination
# mit der eingebauten Funktion any.
def ist_gueltiges_passwort(passwort: str) -> bool:
    if len(passwort) < MINIMALE_PASSWORTLAENGE:
        return False
    hat_kleinbuchstaben = any(
        [KLEINBUCHSTABEN.find(zeichen) >= 0 for zeichen in passwort])
    hat_großbuchstaben = any(
        [GROSSBUCHSTABEN.find(zeichen) >= 0 for zeichen in passwort])
    hat_sonderzeichen = any(
        [SONDERZEICHEN.find(zeichen) >= 0 for zeichen in passwort])
    hat_ziffer = any([ZIFFERN.find(zeichen) >= 0 for zeichen in passwort])
    # return all([hat_kleinbuchstaben, hat_großbuchstaben, hat_ziffer, hat_sonderzeichen])
    return hat_kleinbuchstaben and hat_großbuchstaben and hat_sonderzeichen and hat_ziffer


# Diese Variante der Passwortprüfung verwendet Mengen (engl.: Sets).
def ist_gueltiges_passwort2(passwort: str):
    if len(passwort) < MINIMALE_PASSWORTLAENGE:
        return False

    # Wandle das Passwort in eine Menge von Zeichen um. Dadurch werden automatisch
    # Duplikate entfernt.
    zeichen_menge = set(passwort)
    # Prüfe, ob die Menge der Kleinbuchstaben eine Schnittmenge mit den Passwortbuchstaben hat.
    hat_kleinbuchstaben = len(
        zeichen_menge.intersection(set(KLEINBUCHSTABEN))) > 0
    hat_großbuchstaben = len(
        zeichen_menge.intersection(set(GROSSBUCHSTABEN))) > 0
    hat_sonderzeichen = len(zeichen_menge.intersection(set(SONDERZEICHEN))) > 0
    hat_ziffer = len(zeichen_menge.intersection(set(ZIFFERN))) > 0

    return hat_kleinbuchstaben and hat_großbuchstaben and hat_sonderzeichen and hat_ziffer


def generiere_passwort(laenge):
    if laenge < MINIMALE_PASSWORTLAENGE:
        raise ValueError(f"Mindestlänge beträgt {MINIMALE_PASSWORTLAENGE}")

    passwort = []
    for zeichensatz in [KLEINBUCHSTABEN, GROSSBUCHSTABEN, ZIFFERN, SONDERZEICHEN]:
        passwort.append(random.choice(zeichensatz))

    anzahl_restliche_zeichen = laenge - MINIMALE_PASSWORTLAENGE
    for i in range(anzahl_restliche_zeichen):
        passwort.append(random.choice(ALLE_ZEICHEN))

    random.shuffle(passwort)
    return "".join(passwort)


passwoerter = []
for laenge in [4, 8, 10]:
    passwoerter.append(generiere_passwort(laenge))

print(passwoerter)
print(all([ist_gueltiges_passwort3(p) for p in passwoerter]))
