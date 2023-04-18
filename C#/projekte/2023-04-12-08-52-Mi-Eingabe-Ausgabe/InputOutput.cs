Console.Title = "Mein erstes C# Programm";

Console.WriteLine("C# is awesome, right?"); // Das ist ein einzeiliger Kommentar!
// Ein einzeiliger Kommentar // kann verschachtelt werden
Console.WriteLine("Hello, World!");

// Lasse dir Vor und Nachnamen eingeben und gib den gesamten Namen aus.
Console.Write("Gib deinen Vornamen ein: ");
string firstName = Console.ReadLine()!;
Console.Write("Gib deinen Nachnamen ein: ");
string lastName = Console.ReadLine()!;
Console.WriteLine("Hallo " + firstName + " " + lastName + "!");

// Mit Hilfe von String-Interpolation lassen sich Berechnungsausdrücke
// in ein Zeichenkettenliteral einbetten.
Console.WriteLine($"Hallo {firstName.ToUpper()} {lastName}!");

// WriteLine unterstützt Format-Strings. Diese enthalten numerische Platzhalter,
// die bei der Ausgabe durch übergebene Werte ersetzt werden.
Console.WriteLine("Hallo {0} {1}! Wie geht's dir {0}?", firstName.ToUpper(), lastName);

Console.WriteLine ( 'a' ) ;
Console.ReadKey();


/*
 * 
 * Das ist ein mehrzeiliger Kommentar.
 * 
 */
