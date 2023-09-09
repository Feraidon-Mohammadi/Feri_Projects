import math

def betrag(x):
    return -x if x < 0 else x 

def kreisumfang(radius):
    return 2 * math.pi * radius

def minimum(a, b):
    return a if a < b else b

def umdrehen(zeichenkette):
    ergebnis = ""
    for zeichen in zeichenkette:
        ergebnis = zeichen + ergebnis
    return ergebnis

def maximum(zahlenliste):
    max = None
    for zahl in zahlenliste:
        if max is None or zahl > max:
            max = zahl
    return max


print(maximum([8,1,10,4,0]))
print(betrag(-3))
print(betrag(3))
print(betrag(0))
print(kreisumfang(1))
print(minimum(3, 4))
print(minimum(4, 3))
print(minimum(4, 4))
print(umdrehen("abcde"))