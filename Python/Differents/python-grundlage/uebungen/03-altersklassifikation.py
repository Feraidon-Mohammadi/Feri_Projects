# Die eingebaute Funktion input gibt eine Nachricht auf der Konsole aus
# und fordert den Nutzer auf, etwas einzugeben. Das Ergebnis der Funktion
# ist die Eingabe vom Nutzer als Zeichenkette.
eingabe = input("Bitte gib dein Alter ein: ")

# Um aus einer Zeichenkette eine Zahl zu erzeugen, verwenden wir die eingebaute
# Funktion int.
alter = int(eingabe)

def ermittle_altersklasse(alter):
    if alter < 13:
        print(f"Mit {alter} Jahren bist du noch ein Kleinkind.")
        # print("Mit {a} Jahren bist du ein Kleinkind".format(a=alter)):
    elif alter == 14:
        print("Du wirst in den Kreis der Erwachsenen aufgenommen")
    elif alter == 18:
        print("Du hast deine Volljährigkeit erreicht")
    elif 19 <= alter <= 25:
        print(f"Mit {alter} Jahren bist du ein junger Erwachsener")
    elif alter < 20:
        print(f"Mit {alter} Jahren bist du ein Teenager")
    elif alter < 66:
        print(f"Mit {alter} bist du ein gewöhnlicher Erwachsener.")
    else:
        print(f"Du bist schon ein ziemlicher Greis mit deinen {alter} Jahren!")
  
ermittle_altersklasse(alter)