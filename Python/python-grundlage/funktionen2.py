def f1(wert):
    print(wert)
    wert = 6
    x = 10
    print(wert)


def f2(liste):
    liste.append(10)
    liste = []

# Es können keine oder beliebig viele Zahlen angegeben werden.


def berechne_summe(*zahlen):
    summe = 0
    for zahl in zahlen:
        summe += zahl
    return summe

# Es muss mindestens eine Zahl angegeben werden.
# Beliebig viele weitere Zahlen können folgen.


def berechne_summe2(zahl, *restliche_zahlen):
    summe = zahl
    for z in restliche_zahlen:
        summe += z
    return summe


print(berechne_summe(100, 200, 1, 2, 3, 4))
print(berechne_summe2(10))


def gib_person_aus(vorname, nachname, wohnort, geschlecht):
    if not isinstance(vorname, (int, str)):
        raise TypeError("Vorname muss Zahl oder Zeichenkette sein")
    print(vorname, nachname, wohnort, f"Geschlecht: {geschlecht}")


gib_person_aus(nachname="müller", vorname=[], 
               geschlecht="männlich", wohnort="berlin")

x = 3
f1(3)
print(x)

y = []
print(y)
f2(y)
print(y)
