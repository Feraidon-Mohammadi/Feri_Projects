def ggt(a, b):
    if a == 0:
        return b
    while b > 0:
        # Ziehe von der längeren Seite die kürzere ab
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

print(ggt(44, 12))
print(ggt(12, 44))
print(ggt(3, 0))
print(ggt(0, 3))
print(ggt(4, 3))
