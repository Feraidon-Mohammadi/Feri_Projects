from collections import defaultdict

PFAD = r"./mitarbeiter.csv"

mitarbeiter_tabelle = []
datei = open(PFAD, "rt", encoding="utf-8")
for zeile in datei:
    felder = zeile.strip().split(";")
    name, standort, geschlecht = felder
    mitarbeiter_tabelle.append( tuple(felder) )
    # print(name, standort, geschlecht)
datei.close()

gruppen = defaultdict(lambda: []) 
# Hinweis: Ein DefaultDictionary legt bei erstmaligem Zugriff auf einen noch nicht vorhandenen 
# Schlüssel automatisch den Schlüssel mit einem vordefinierten Anfangswert 
# (hier eine leere Liste) an.

for mitarbeiter_datensatz in mitarbeiter_tabelle:
    name, standort, geschlecht = mitarbeiter_datensatz
    gruppen_schluessel = (standort, geschlecht)
    # gruppenmitglieder = gruppen[gruppen_schluessel]
    # gruppenmitglieder.append(mitarbeiter_datensatz)
    gruppen[gruppen_schluessel].append(mitarbeiter_datensatz)

for gruppen_schluessel, gruppen_mitglieder in gruppen.items():
    print(gruppen_schluessel, gruppen_mitglieder)