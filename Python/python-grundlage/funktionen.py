import random

# Hinweis: Eine Funktionsdefinition wird nur "registriert". Der Code wird aber
# nicht ausgeführt. Eine Funktion wird nur dann ausgeführt, wenn man sie explizit
# aufruft!
# Die Namen der Parameter x und y sind frei wählbar.
# Die Parameter haben die Aufgabe, die vom Aufrufer übergebenen Argumente zu speichern.
def f1(x, y):
    print("Parameter 1:", x)
    print("Parameter 2:", y)


print("Ich liege zwischen zwei Funktionsdefinitionen")

# Die Parameter x und y von f2 haben keinerlei Bezug zu den Parametern x und y von f1!
def f2(x, y):
    return x+y

# Diese Funktion hat keine Parameter. Trotzdem müssen die runden Klammern der Parameterliste
# angegeben werden.
def f3():
    print("Eine Zufallszahl:", random.randint(0, 100))

# Aufruf der Funktion f3. Beachte die Klammern!
f3()

# Die folgende Zeile ruft die Funktion f1 mit den Argumenten 2 und 3 auf.
# Der Code-Block von f1 wird also mit x = 2 und y = 3 einmal ausgeführt.
f1(2, 3)

# Hier folgt ein zweiter Aufruf der Funktion f1. Diesmal haben die Parameter
# folgende Anfangswerte: x = 10, y = 20.
f1(10, 20)

# Auch komplexe Berechnungsausdrücke lassen sich als Argumente an eine Funktion übergeben.
u = 20
v = 30
f1(2 * u + 1, v)

n = f2(4, 5)
print(n)

def quadriere(x):
    return x * x

def ziehe_quadratwurzel(x):
    return x ** 0.5 # ** ist der Potenzierungsoperator

def pythagoras(kathete_a, kathete_b):
    a_quadrat = quadriere(kathete_a)
    b_quadrat = quadriere(kathete_b)
    hypotenuse = ziehe_quadratwurzel(a_quadrat + b_quadrat)
    return hypotenuse

def spiel():
    print("abc")
    spiel() # AUTSCH! 

#spiel()

h = pythagoras(3, 4)
print(h)


def heron(n):
    seite_a = 1
    seite_b = n

    while abs(seite_b - seite_a) >= 0.0000001:
        mittelwert = (seite_a + seite_b) / 2
        seite_a = mittelwert
        seite_b = n / seite_a
    
    return seite_b

print(heron(0.5))