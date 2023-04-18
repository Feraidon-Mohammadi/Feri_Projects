Console.Write("Gib dein Alter ein: ");
string input = Console.ReadLine()!;

// Explizite Konvertierung eines double Literals in ein int-Wert.
// Die Konvertierung ist im allgemeinen verlustbehaftet, deshalb
// führt der Compiler eine solche Konvertierung nicht implizit (automatisch) durch.
int number = (int)(12.34);
int bigNumber = (int)(2e9); // 2 * (10 hoch 9)
int yetAnotherBigNumber = 1_333_444_555; // Unterstriche dienen nur der Lesbarkeit!
int hexCode = 0xcafebab; // Hexadezimalzahl
int binaryNumber = 0b1000_0000_1010; // Binärzahl
int octalNumber = 018; // kein Support für Oktalzahlen.

// Mit Hilfe von Parsing können wir eine Zeichenkette in einen anderen Datentyp konvertieren.
// int age = (int)input; // es gibt keine explizite Konvertierung von string nach int!
int age = int.Parse(input);

Console.WriteLine($"In {100 - age} Jahren wirst du 100! :-)");

// Schreibe ein kleines Programm, das den Nutzer auffordert eine Temperatur in Celsius anzugeben
// Die Temperatur soll in Fahrenheit umgewandelt und ausgegeben werden.
