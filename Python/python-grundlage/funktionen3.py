import math


def erstelle_neue_funktion(basis_funktion, zahl):
    def neue_funktion(eingabe): return basis_funktion(eingabe * zahl)
    return neue_funktion


berechne_dreifache_laenge = erstelle_neue_funktion(len, 3)
# entspricht:  lambda eingabe: len(eingabe * 3)
print(berechne_dreifache_laenge("abc"))

berechne_doppelte_summe = erstelle_neue_funktion(sum, 2)
# enstpricht:   lambda eingabe: sum(eingabe * 2)
print(berechne_doppelte_summe([1, 2, 3]))


def berechne_summe(a, b, c, d):
    return a + b + c + d


def berechne_summe2(a, c):
    return berechne_summe(a, 1, c, 2)


def erstelle_summenfunktion(wert_b, wert_d):
    return lambda a, c: berechne_summe(a, wert_b, c, wert_d)


print(berechne_summe(1, 2, 3, 4))
print(berechne_summe2(1, 3))

berechne_summe_mit_b1_und_d2 = erstelle_summenfunktion(1, 2)
berechne_summe_mit_b5_und_d3 = erstelle_summenfunktion(5, 3)
print(berechne_summe_mit_b1_und_d2(3, 7))
print(berechne_summe_mit_b5_und_d3(3, 7))


def erstelle_hintereinanderausführung(f1, f2, f3):
    return lambda x: f3(f2(f1(x)))


def erstelle_pipeline(*funktionen):
    # definiere eine lokale Funktion. Der Name der Funktion ist
    # der Name der lokalen Variablen.
    def pipeline(eingabe):
        resultat = eingabe
        for funktion in funktionen:
            resultat = funktion(resultat)
        return resultat

    return pipeline


pipeline = erstelle_hintereinanderausführung(
    lambda s: s.strip(),
    lambda s: s.upper(),
    lambda s: s[::-1])

print(pipeline(" abc   "))
print(pipeline("A"))
print(pipeline("Martin"))

pipeline2 = erstelle_hintereinanderausführung(
    lambda s: s.lower().split(),
    lambda liste: sorted(liste),
    lambda liste: "--".join(liste)
)

print(pipeline2("Python ist cool. Oder?"))

pipeline3 = erstelle_pipeline(lambda s: s.lower().split(),
                              lambda liste: sorted(liste))

print(pipeline3("Python ist cool. Oder?"))


pipeline4 = erstelle_pipeline(
    lambda zahlenliste: [zahl for zahl in zahlenliste if zahl % 2 != 0],
    lambda zahlenliste: [zahl * zahl for zahl in zahlenliste],
    sum
)

print(pipeline4([1, 2, 3, 4, 5, 6, 7]))  # 84
print(sum([z * z for z in [1, 2, 3, 4, 5, 6, 7] if z % 2 != 0]))


def vereinige_mengen(*mengen):
    leere_menge = set()
    gesamt_menge = leere_menge.union(*mengen)
    return gesamt_menge


pipeline5 = erstelle_pipeline(
    lambda liste: [[b for b in w if b in "aeiou"] for w in liste],
    lambda mengen: vereinige_mengen(*mengen)
)

print(pipeline5(["alice", "bob", "charlie", "ute"]))


# Diese Funktion erstellt eine neue Funktion f', welche zwei Eingabe
# Parameter x, y besitzt und folgenden Wert berechnet:
# f1(x) * f1(x) + f2(y) * f2(y)
def erstelle_funktion(f1, f2):
    def f(x, y):
        return f1(x) * f1(x) + f2(y) * f2(y)
    return f

f = erstelle_funktion(math.sin, math.cos)
print(f(math.pi / 2, 0))  # berechnet: sin(pi/2)*sin(pi/2)+cos(0)*cos(0)