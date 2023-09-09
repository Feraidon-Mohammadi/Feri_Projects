import sys
import re

argumente = sys.argv[1:]
if len(argumente) == 0:
    print("Fehlendes Argument: ISBN")
    sys.exit(0)

isbn = argumente[0].replace("-", "")
if not re.match(r'\d{13}', isbn):
    print("Ungültige Eingabe")
    sys.exit(0)

ziffern = [int(zeichen) for zeichen in isbn]

# z = []
# for zeichen in isbn:
#     z.append(int(zeichen))

summe = sum([ziffern[i] if i % 2 == 0 else ziffern[i]
            * 3 for i in range(len(ziffern))])

if summe % 10 == 0:
    print("Gültig")
else:
    print("Ungültig")
