from functools import reduce


def filtere_gerade_zahlen(gefilterte_liste, zahl):
    print(f"Bisherige Zahlen: {gefilterte_liste} Zu testende Zahl: {zahl}")
    if zahl % 2 == 0:
        gefilterte_liste.append(zahl)
        print(f"{zahl} ist gerade")
    print(f"Neue Zahlenliste: {gefilterte_liste}")
    return gefilterte_liste


gerade_zahlen = reduce(lambda l, z: l if z %
                       2 != 0 else l+[z], [1, 2, 3, 4, 5, 6], [])
print(gerade_zahlen)

quadratzahlen = reduce(lambda liste, zahl: liste + [zahl * zahl], [1,2,3,4,5], [])
print(quadratzahlen)