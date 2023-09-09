import random
import os

def raten(zufallszahl):
    eingabe = input("Gib Zahl ein: ")
    zahl = int(eingabe)
    if zahl > zufallszahl:
        print("Zahl ist zu groß")
        return False
    elif zahl < zufallszahl:
        print("Zahl ist zu klein")
        return False
    else:
        print("Richtig geraten!")
        return True


def spielen(untergrenze, obergrenze, max_versuche):
    zufallszahl = random.randint(untergrenze, obergrenze)
    anzahl_versuche = 0
    richtig_geraten = False

    while (anzahl_versuche < max_versuche) and not richtig_geraten:
        verbleibende_versuche = max_versuche - anzahl_versuche
        print(f"\nDu hast noch {verbleibende_versuche} Versuch(e) übrig.")
        anzahl_versuche += 1
        richtig_geraten = raten(zufallszahl)

    if richtig_geraten:
        print(f"\nGlückwunsch! Du hast {anzahl_versuche} benötigt.")
    else:
        print("\nSchade. Versuche es doch noch einmal.")


def ermittle_spielkonfiguration():
    eingabe = input("Untergrenze: ")
    untergrenze = int(eingabe)
    eingabe = input("Obergrenze: ")
    obergrenze = int(eingabe)
    eingabe = input("Anzahl Versuche: ")
    versuche = int(eingabe)
    return (untergrenze, obergrenze, versuche)


def main():
    titel = "Zahlenraten"

    while True:
        os.system("cls")
        print(titel.upper())
        print("-" * len(titel))

        untergrenze, obergrenze, max_versuche = ermittle_spielkonfiguration()
        spielen(untergrenze, obergrenze, max_versuche)
       
        eingabe = input("\nWillst du noch mal spielen? (j/n): ")
        if eingabe != "j":
            break
    
    print("Vielen Dank! Bis zum nächsten Mal.")

# Starte die main-Funktion, sofern das Skript nicht als Modul importiert wird.
if __name__ == "__main__":
    main()
