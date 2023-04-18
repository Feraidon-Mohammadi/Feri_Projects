Console.Write("Gib dein Alter ein: ");
int age = int.Parse(Console.ReadLine()!);

// Hinweis: die logischen Operatoren && (and), || (or), ! (not) funktionieren analog
// zu JavaScript
if (age < 13)
{
    Console.WriteLine("Du bist ein Kind");
}
else if (age < 20)
{
    Console.WriteLine("Du bist ein Teenager");
}
else if (age < 40)
{
    Console.WriteLine("Du bist ein junger Erwachsener");
}
else
{
    Console.WriteLine("Du bist schon ziemlich alt ;-)");
}

if (age >= 20 && age < 50)
{
    Console.WriteLine("Du bekommst Eintritt in die \"Junge Erwachsene\" WhatsApp-Gruppe" );
}

// C# unterstützt diverse Formen von sogenannten Patterns. Damit lassen sich teils sehr
// komplexe Fälle in kompakter Form beschreiben.
if (age is >= 20 and < 50 or >= 100) // age >= 20 && age < 50 || age >= 100
{
    Console.WriteLine("Zutritt zur Party gestattet.");
}