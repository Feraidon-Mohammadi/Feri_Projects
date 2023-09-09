# Übung 01

Hinweis: Nutze für die folgenden Übungen einen Terminal, idealerweise die Powershell.

- lasse dir die Hilfe zum Tool `pyenv` anzeigen
- welche Python-Versionen sind derzeit auf dem System installliert?
- installiere die Python-Version 3.6
- erstelle ein neues Projektverzeichnis, welches standardmäßig Python v3.6 verwendet
    - prüfe, ob der korrekte Python-Interpreter benutzt wird
    - wie lautet der globale Python-Interpreter?
- installiere das Paket `virtualenv` für Python 3.6.0
- erzeuge zwei virtuelle Umgebungen im Projektverzeichnis
    - Umgebung 1 heißt `.env1`
    - Umgebung 2 heißt `.env2`
- aktiviere die Umgebung `.env1` und lasse dir die bereits installierten Pakete mit `pip` anzeigen
- installiere in Umgebung `.env1` ein Paket namens `pendulum`
- lasse dir erneut die installierten Pakete anzeigen
- deaktiviere die Umgebung `.env1`
- aktiviere die Umgebung `.env2` und lasse dir auch hier die bereits installierten Pakete anzeigen
- installiere in Umgebung `.env2` ein Paket namens `pygame`
- lasse dir nochmals die installierten Pakete anzeigen
- deaktiviere die virtuelle Umgebung `.env2`

# Übung 02

Erweitere den MAC-Generator wie folgt:

- der Nutzer kann das Skript mit einem zusätzlichen numerischen Argument aufrufen. Das Argument gibt an, wie viele zufällige MACs generiert werden sollen.
- die generierten MAC-Adressen sollen zeilenweise ausgegeben werden
- gibt der Nutzer kein zusätzliches Argument an, soll nur eine MAC generiert werden

Beispie:

```bash
$ python mac-generator.py 3
d8-92-0f-5b-05-7f
f9-dc-b9-ed-bf-08
7d-71-dc-27-91-3e
$ python mac-generator
7d-71-dc-27-91-3e
```

Implementierungshinweise:

- importiere das Modul `sys`
- nutze die Variable `sys.argv` um eine Liste der übergebenen Argumente zu erhalten
- nutze die Funktion `len`, um die Anzahl der Elemente einer Liste zu ermitteln
- nutze die Funktion `int`, um eine Zeichenkette in einen Integer umzuwandeln

# Übung 03

Erweitere das Programm zur Altersklassifkation um folgende Sonderfälle:

- wenn der Nutzer 14 ist, soll das Progamm ausgeben, dass er "in den Kreis der erwachsenen aufgenommen wird"
- wenn der Nutzer 18 ist, soll das Programm ausgeben, dass er "nun seine Volljährigkeit erreicht hat"
- wenn der Nutzer zwischen 19 und 25 Jahren alt ist, dann gibt das Programm aus, dass der Nutzer ein "junger Erwachsener" ist.

# Übung 04

Schreibe ein Programm, das anhand verschiedener Kriterien entscheidet, ob ein Bewerber ein geeigneter Kandidat für eine Firma ist. Folgende Kriterien sind relevant:

- Geschlecht (männlich, weiblich, divers)
- Alter
- Berufserfahrung
- Gehaltsvorstellung

Ein Bewerber kommt als Kandidat in Frage, wenn mindestens eine der folgenden Bedingungen erfüllt ist:

- Gehaltsvorstellung unter 20.000 (billige Arbeitskraft)
- mindestens 35 Jahre Berufserfahrung (sehr erfahren)
- Gehaltsvorstellung über 60.000, aber mindestens 20 Jahre Berufserfahrung (hohes Gehalt erfordert entsprechende Berufserfahrung)
- Frauen und Diverse im Altersbereich 25 - 35, aber mit höchstens 30.000 Gehaltswunsch
- Männer ab 25 mit mindestens 5 Jahren Berufserfahrung oder mit weniger als 5 Jahren Berufserfahrung aber dafür einem Gehaltswunsch von weniger als 40.000

# Übung 05

Löse folgende Problemstellungen mit Hilfe der `for in` Schleife:

1. Gib folgende Zahlensequenzen aus:
    1. 1 2 3 4 5
    1. 5 4 3 2 1
    1. 1 3 5 7 9
    1. 9 7 5 3 1
    1. 1 -2 3 -4 5 -6
1. Gib folgende Textmuster aus. Nutze verschachtelte Schleifen

    ```
    *
    **
    ***
    ****
    ```

    ```
    ****
    ***
    **
    *
    ```
1. Erzeuge eine Multiplikationstabelle

    ```
    01 02 03 04 05 06 07 08 09 10
    02 04 06 08 10 12 14 16 18 20
    03 06 09 12 15 18 21 24 27 30
    ...
    10 20 30 40 50 60 70 80 90 100 
    ```

# Übung 06

Schreibe ein Programm, das eine gegebene Anzahl von Minuten in

- Tage
- Stunden
- Minuten

zerlegt. Nutze den Modulo-Operator `%` und den Divisionsoperator `//` (Integer-Division).

Beispiel: 1580 Minuten = 1 Tag, 2 Stunden, 20 Minuten

# Übung 07

Schreibe ein Programm, welches eine vierstellige Zahl in 1000er, 100er, 10er und 1er zerlegt. Nutze den Modulo-Operator `%` und den Divisionsoperator `//`.

Beispiel: 9876 = 9 * 1000 + 8 * 100 + 7 * 10 + 6 * 1 

# Übung 08

Schreibe ein Programm, das eine eingegebene ISBN-13 auf Gültigkeit prüft. Eine ISBN-13 ist genau dann gültig, wenn folgende Summe $S = z_1 + z_3 + ... + z_{11} + z_{13} + 3(z_2 + z_4 + ... + z_{12})$ ein Vielfaches von 10 ist. Hinweis: $z_i$ ist die Ziffer an Position $i$, wobei $1\le i \le 13$.

# Übung 09

Berechne folgende Aufgaben:

1. 5 % 3
1. 2 % 5
1. 0 % 5
1. 0 % (-5)
1. 5 % 0
1. 20 % 10
1. 20 % (-10)
1. -20 % 10
1. -20 % -10
1. 10 % 4
1. 10 % -4
1. -10 % 4
1. -10 % -4

Hinweis: `a % b` ist `a - (a // b) * b`. Das Vorzeichen des Ergebnis entspricht dem Vorzeichen von `b`.

# Übung 10

Implementiere das Spiel Zahlenraten.

# Übung 11

Implementiere das Spiel Schere-Stein-Papier.

# Übung 12

Schreibe folgende Funktionen, ohne vordefinierte Python-Funktionen einzusetzen. Die Funktionen sollen ihr Ergebnis an den Aufrufer zurückgeben.

- `betrag(x)` Wenn x < 0 dann gib -x zurück, sonst x
- `kreisumfang(radius)`
- `minimum(a, b)`
- `umdrehen(zeichenkette)` (len und range sind erlaubt)
- `maximum(zahlenliste)` (len und range sind erlaubt)

Führe einen Schreibtischtest für folgende Funktion durch:

```python
def f(a, b):
    if a == 0:
        return b
    while b > 0:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
```

Was macht die Funktion? Teste u.a. mit folgenden Werten:

- a = 8 und b = 12
- a = 0 und b = 3
- a = 16 und b = 8

# Übung 13

Schreibe ein Programm, das ein zufälliges Passwort der Länge n generiert. Die Länge des Passwortes soll per Kommandozeile an das Programm übergeben werden.

Für das generierte Passwort sollen folgende Kriterien gelten:

- mindestens ein Sonderzeichen aus der Menge `!#$_*`
- mindestens eine Ziffer
- mindestens einen Groß und einen Kleinbuchstaben

Beispiel:

```
python password-generator.py 5
--> auX8!
```

Hinweis: Nutze das `random` Modul als Hilfe.

# Übung 14

Löse folgende Aufgaben:

- ermittle die Länge der Zeichenkette `abc`
- wandle die Zeichenkette `abc` in Großbuchstaben um
- wie prüft man, ob ein bestimmtes Zeichen in einer Zeichenkette enthalten ist? Nenne mindestens zwei Möglichkeiten.
- ermittle die verschiedenen Zeichen, die in einer Zeichenkette vorkommen: Schreibe hierfür eine Funktion mit folgender Signatur:

    ```python
    # Ein Funktionsparameter vom Typ str
    # Rückgabewert soll eine Liste der verschiedenen Zeichen sein.
    def distinct_characters(text : str) -> list[str]:
        pass # hier steht deine Implementierung
    ```

- es sollen die Quadrate der Zahlen 1 bis 10 berechnet werden. Nutze hierfür eine sogenannte List-Comprehension. Die Quadrate speicherst du in einer Liste. Anschließend verknüpfst du die Zahlen in der Liste mit dem Separator `,`.
- schreibe eine Funktion, die eine Häufigkeitstabelle einer Zeichenkette erstellt. Verwende folgende Signatur:

    ```python
    def frequency(text : str) -> dict[str, int]:
        pass
    ```

    Beispiel: `frequency("abbac")` liefert ein Dictionary mit den Schlüssel-Wert-Paaren (a, 2), (b, 2) und (c, 1).
- gib das von `frequency` zurückgegebene Dictionary in folgender tabellarischer Form aus:

    ```
    ZEICHEN     HÄUFIGKEIT
    a                    2
    b                    2
    c                    1
    ```

    Hinweis: Nutze formatierte Stringliterale.
- entwerfe einen regulären Ausdruck, um eine Log-Datei in seine einzelnen Bestandteile zu zerlegen. Eine Log-Datei hat Zeilen in folgendem Format:

    ```
    01.02.2022 11:34 FEHLER "Server ist nicht erreichbar"
    ```

    Eine Zeile setzt sich also aus einem Datum, einer Uhrzeit, einer Kategorie (z.B. FEHLER, INFO, WARNUNG) und einem Beschreibungstext zusammen.
- nutze den regulären Ausdruck aus der vorherigen Übung, um eine Log-Zeile in seine einzelnen Komponenten bzw. Bestandteile zu zerlegen. Nutze hierfür benannte Gruppen im regulären Ausdruck.

# Übung 15 (Listen, List-Comprehensions, Filtern, Transformieren)

Löse folgende Teilaufgaben:

- erzeuge eine Liste mit den Werten 0, 7, 14, 21, ... bis 98. Versuche mindestens zwei Möglichkeiten zu finden. Hinweis: Range, List Comprehension
- extrahiere alle Vokale (a,e,i,o,u) aus der Zeichenkette `"Hello, World"` und verbinde sie zu einer neuen Zeichenkette. Hinweis: nutze eine List-Comprehension
- schreibe eine Funktion `maximale_wortlänge(liste)` welche aus einer Wortliste das längste Wort heraussucht und zurückgibt
- gegeben sei folgende Namensliste: `[("Max", "Müller"), ("Egon", "Olsen"), ("Rainer", "Zufall")]`
    - erzeuge daraus eine Liste von Initialien `["M.M", "E.O", "R.Z"]`
    - die Initialen sollen nach dem Buchstaben des Nachnamens absteigend sortiert werden!
    - nutze auch hierfür eine List-Comprehension sowie die Methode `sort`
- gegeben sei folgende Namensliste: `["alice", "bob", "charlie", "damian", "elon", "fred"]`
    - sortiere die Namensliste absteigend nach den letzten Buchstaben der Namen
    - wandle die Anfangsbuchstaben in Großbuchstaben um
    - filtere nur jene Namen heraus die mindestens zwei Vokale enthalten
    - Hinweis: schreibe dir gegebenenfalls Hilfsfunktionen

# Übung 16 (Galgenraten)

Schreibe folgendes Spiel:

- eine Datei namens `worte.txt` enthält pro Zeile ein Wort.
- das Programm liest anfangs diese Datei ein und wählt ein zufälliges Wort aus
- der Spieler hat nun eine begrenzte Anzahl an Möglichkeiten um das Wort zu erraten
- rät er einen korrekten Buchstaben, werden alle Vorkommen des Buchstabens aufgedeckt
- alle noch nicht erratenen Buchstaben werden durch `_` dargestellt.
- nachdem der Spieler das Wort erraten bzw. alle Versuche ausgenutzt hat, fragt ihn das Programm, ob er noch einmal spielen möchte

```
Angenommen, das Lösungswort lautet: SCHNEE

1) _ _ _ _ _ _ (0 / 10 Versuche, 10 verbleibend)
Gib Buchstabe ein: e
2) _ _ _ _ E E (1 / 10 Versuche, 9 verbleibend)
Gib Buchstabe ein: f
Leider war der Buchstabe f nicht dabei!
3) S _ _ _ E E (2 / 10 Versuche, 8 verbleibend)
...
10) S _ _ _ E E (9 / 10 Versuche, 1 verbleibend)
Gib Buchstabe ein: c
Leider hast du das Wort nicht erraten!
Das gesuchte Wort war: SCHNEE
Willst du noch einmal spielen? (j/n):  
```

# Übung 17 (Reduce)

- verwende `reduce` um eine Liste von Zahlen zu filtern. Es sollen nur Zahlen in der Ergebnisliste vorkommen, die gerade sind. Setze kein `filter` ein!
- verwende `reduce` um aus einer Liste von Zahlen deren Quadratzahlen zu bilden. Verwende keine List-Comprehensions und kein `map`.
