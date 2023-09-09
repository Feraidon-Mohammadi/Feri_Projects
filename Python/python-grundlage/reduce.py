from functools import reduce


def addiere_drauf(alte_summe, zahl):
    neue_summe = alte_summe + zahl
    print(f"{alte_summe} + {zahl} = {neue_summe}")
    return neue_summe


def multipliziere(altes_produkt, zahl):
    neues_produkt = altes_produkt * zahl
    print(f"{altes_produkt} * {zahl} = {neues_produkt}")
    return neues_produkt


def finde_maximum(altes_maximum, zahl):
    if altes_maximum < zahl:
        print(f"{altes_maximum} < {zahl}")
        return zahl
    else:
        print(f"{altes_maximum} >= {zahl}")
        return altes_maximum


def stelle_voran(alt: str, buchstabe: str) -> str:
    neu = buchstabe + alt
    print(f"{buchstabe} + {alt} = {neu}")
    return neu


summe = reduce(addiere_drauf, [1, 2, 3, 4, 5], 0)
print(summe)
produkt = reduce(multipliziere, [3, 6, 10], 1)
print(produkt)
# Fehlt ein explziter Initialwert, benutzt reduce das erste Element als Initialwert.
maximum = reduce(finde_maximum, [5, 1, 3, 7, 2])
print(maximum)
umgekehrt = reduce(stelle_voran, "12345")
print(umgekehrt)
