import random
import os

SCHERE = "schere"
STEIN = "stein"
PAPIER = "papier"

REGELN = {
    (SCHERE, STEIN): ("Stein macht Schere stumpf", False),
    (SCHERE, PAPIER): ("Schere zerschneidet Papier", True),
    (PAPIER, STEIN): ("Papier umwickelt Stein", True)
}

AUSWAHL_MENU = {
    "a": SCHERE,
    "b": STEIN,
    "c": PAPIER
}

def zeige_menue(AUSWAHL_MENU):
    for kuerzel, item_name in AUSWAHL_MENU.items():
        print(f"{kuerzel}) {item_name.upper()}")


def lies_menu_eintrag(AUSWAHL_MENU):
    while True:
        eingabe = input("Bitte wähle dein Item aus: ")
        if eingabe in AUSWAHL_MENU.keys():
            break
    return AUSWAHL_MENU[eingabe]

def finde_regel(item1, item2):
    schluessel = (item1, item2)
    if schluessel in REGELN:
        return REGELN[schluessel]
    else:
        return None

def auswerten(spieler_item, computer_item):
    if spieler_item == computer_item:
        print("Unentschieden! Ihr habt beide das gleiche Item gewählt.")
        return (0, 0)
    
    nachricht = None
    spieler_hat_gewonnen = None

    regel = finde_regel(spieler_item, computer_item)
    if regel is None:
        regel = finde_regel(computer_item, spieler_item)
        spieler_hat_gewonnen = not regel[1]
    else:
        spieler_hat_gewonnen = regel[1]
    nachricht = regel[0]

    if spieler_hat_gewonnen:
        print(f"{nachricht}. Du hast gewonnen!")
        return (1, 0)
    else:
        print(f"{nachricht}. Du hast verloren")
        return (0, 1)


def main():
    punkte_spieler = 0
    punkte_computer = 0
    MAX_PUNKTE = 3

    os.system("cls")
    while punkte_spieler < MAX_PUNKTE and punkte_computer < MAX_PUNKTE:
        print(f"Spielerpunkte: {punkte_spieler} Computerpunkte: {punkte_computer}")
        zeige_menue(AUSWAHL_MENU)
        
        spieler_item = lies_menu_eintrag(AUSWAHL_MENU)
        alle_items = list(AUSWAHL_MENU.values())
        computer_item = random.choice(alle_items * 10)

        print(f"Du hast dich für das Item {spieler_item.upper()} entschieden.")
        print(f"Der Computer hat sich für das Item {computer_item.upper()} entschieden.")

        punktedifferenz_spieler, punktedifferenz_computer = auswerten(spieler_item, computer_item)
        punkte_spieler += punktedifferenz_spieler
        punkte_computer += punktedifferenz_computer
    
    if punkte_spieler > punkte_computer:
        print("Du hast das Spiel gewonnen! Glückwunsch!")
    else:
        print("Leider hast du das Spiel verloren! Versuche es doch noch einmal.")

main()    

