def berechne_summe(zahlenliste):
    # Triviales Problem - Abbruchbedingung für die Rekursion
    if len(zahlenliste) == 0:
        return 0
    # Das nicht triviale Berechnungsproblem wird reduziert
    # indem wir eine Teillösung für ein weniger komplexes Problem
    # lösen. Hier: die Berechnung einer Teilsumme
    restsumme = berechne_summe(zahlenliste[1:])
    return restsumme + zahlenliste[0]


print(berechne_summe([1, 2, 3, 4, 5]))


def suche_maximum(zahlenliste, level=0):
    abstand = "  " * level
    print(abstand, f"Aufgabe: Suche Maximum aus Liste {zahlenliste}")
    # Trivialer Fall bzw. Abbruchbedingung für Rekursion
    if len(zahlenliste) == 1:
        print(
            abstand, f"Trivialen Fall entdeckt: Maximum ist {zahlenliste[0]}")
        return zahlenliste[0]
    # Nicht-trivialer Fall: Suche Maximum aus Teilliste
    # und vergleiche es mit dem ersten Element.
    erstes_element = zahlenliste[0]
    print(
        abstand, f"Nicht trivialer Fall: Suche zunächst Maximum in {zahlenliste[1:]}")
    maximum_teilliste = suche_maximum(zahlenliste[1:], level + 1)
    if erstes_element > maximum_teilliste:
        print(
            abstand, f"Maximum aus {zahlenliste[1:]} und {erstes_element} ist ", erstes_element)
        return erstes_element
    else:
        print(
            abstand, f"Maximum aus {zahlenliste[1:]} und {erstes_element} ist ", maximum_teilliste)
        return maximum_teilliste


print(suche_maximum([10, 4, 3, 8, 5]))


def suche_zahl(suchzahl, zahlenliste):
    if len(zahlenliste) == 0:
        return -1

    erstes_element = zahlenliste[0]
    if erstes_element == suchzahl:
        return 0
    else:
        index = suche_zahl(suchzahl, zahlenliste[1:])
        if index < 0:
            return -1
        return index + 1


def umkehren(zeichenkette):
    if zeichenkette == "":
        return ""
    return umkehren(zeichenkette[1:]) + zeichenkette[0]


def filtere_liste(filterfunktion, liste):
    if len(liste) == 0:
        return []

    gefiltert = filtere_liste(filterfunktion, liste[1:])
    erstes_element = liste[0]
    if filterfunktion(erstes_element):
        gefiltert.insert(0, erstes_element)
    return gefiltert


zahlen = [1, 20, 3, 10, 20, 30]
print(filtere_liste(lambda x: x > 10, zahlen))
print(zahlen)

print(umkehren("abcdef"))


# umkehren("abcd") => "dcba"

print(suche_zahl(2, [1, 3, 2, 4]))
