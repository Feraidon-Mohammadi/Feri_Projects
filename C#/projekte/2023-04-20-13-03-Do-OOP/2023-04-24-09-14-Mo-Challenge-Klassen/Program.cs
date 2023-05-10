
// Challenge:
// Entwerfe eine Klasse namens Person. Folgende Informationen sollen in der Klasse deklariert werden
// - Vorname, Nachname, Geburtsdatum, Staatsangehörigkeiten, Geburtsland, Geschlecht 
// - Das Alter der Person soll anhand des Geburtsdatums ermittelt werden -> nutze hierfür ein Property
// - jede Person besitzt einen primären Wohnsitz und optional einen Nebenwohnsitz
// - für den Wohnsitz bzw. Adresse ist eine separate Klasse namens Address zu entwerfen
// - für das Geschlecht ist eine Enumeration zu erzeugen mit den Werten Male, Female, Diverse
// - füge Methode Print hinzu, die alle Informationen zu einer Person auf der Kommandozeile ausgibt
// - entwerfe geeignete Konstruktoren, um Personenobjekte zu erzeugen. Verwende gegebenenfalls Konstruktordelegation.
//
// Folgende Infos sind in der Klasse Address zu verwalten:
// - Straße, Hausnummer, Postleitzahl und Wohnort sowie Land
//
// 

// Mit Hilfe der Object-Initializer-Syntax können wir
// auf komfortable Weise nach dem Konstruktor noch public Properties
// und public Fields initialisieren.
Address work = new()
{
  City = "Erfurt",
  Country = "Deutschland",
  Street = "Maximilian-Welsch-Str.",
  StreetNumber = "2a",
  ZipCode = "99084",
};

Address home = new()
{
  City = "Incognito",
  Country = "Schlaraffenland",
  Street = "Villa Kunterbunt",
  StreetNumber = "123",
  ZipCode = "666777",
};

string[] allNationalities = { "Deutsch", "Türkisch", "Rumänisch", "Iranisch", "Afghanisch" };

Person alice = new()
{
  Birthdate = new DateOnly(2000, 6, 30),
  CountryOfBirth = "Deutschland",
  FirstName = "Alice",
  Gender = Gender.Female,
  LastName = "Wonderland",
  MainAddress = new Address() 
  { 
    City = "Wondercity", 
    Country = "Oz", 
    Street = "Wonder Road",
    StreetNumber = "7",
    ZipCode = "777"
  },
  Nationalities = new string[] { "English" },
};

Person bob = new();
bob.Nationalities = allNationalities;
bob.Nationalities[1] = "Französisch";

int age = 80;
int? amount = null;
bool? isActive = null;

if (amount.HasValue)
{
  Console.WriteLine($"Menge: {amount.Value}");
}

if (amount != null)
{
  Console.WriteLine($"Menge: {amount}");
}

// Console.WriteLine ruft automatisch die ToString Methode der Objekte auf.
Console.WriteLine(alice);
Console.WriteLine(bob);