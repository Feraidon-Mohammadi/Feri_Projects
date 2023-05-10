// Challenge:
// - erstelle ein paar Food Objekte und speichere sie in einem Array ab
// - lege ein paar DiaryEntry Objekte an und weise ihnen unterschiedliche FoodObjekte hinzu
// - implementiere ToString-Methoden für die Klassen DiaryEntry und Food
// - erzeuge ein neues DietDiary Objekte und befülle es mit Einträgen
// - füge eine ToString Methode zur Klasse DietDiary hinzu, die alle
//   enthaltenen Einträge tabellarisch ausgibt.
// - teste die FindEntries Methoden, insbesondere FindEntriesByDate

// Challenge 2:
// - Schreibe eine Klasse namens DietDiaryReport, die ein Ernährungstagebuch ausgibt. Diese Klasse erhält
//   ein vollständiges DietDiary Objekt. Sie soll die gesamte Ausgabe als Zeichnkette zurückgeben.
//   Hinweis: Die Angaben von Fett, Kohlenhydrate und Proteine müssen auf die Menge umgerechnet werden,
//   da sie ja nur bezogen auf 100g vorliegen.
// - Füge eine Möglichkeit hinzu, um nur eine begrenzte Anzahl an Tagen auszugeben (Zeitraum, die letzten n Tage etc.)
// - verwende ein paar Konsolenfarben, um den Überblick zu verbessern
// - Stelle dir folgende Fragen:
//   - Welche Konstruktoren werden benötigt?
//   - Welche Methoden werden benötigt?
//   - Braucht man Properties um die Ausgabe ggf. zu konfigurieren?
//   - Wiederholen sich einige Codes immer wieder? Dann lagere sie in kleine Hilfsfunktionen aus!

//   Montag 01.04.2000 (Gesamt kcal: 278kcal, 10g (32.37%), 37g (53.23%), 10g (14.40%))
//   ==================================================================================
//   08:15 Milch     150g  113kcal      5g       7g     10g
//   09:30 Knoppers  120g  165kcal      5g      30g      0g
//   ----------------------------------------------------------------------------------
//         2         370g  278kcal     10g      37g     10g
//                                  32.37%   53.23%  14.40%
//
//   FFFFFFKKKKKKKPPP
//   F: ======
//   K: ===========
//   P: ===
// 
//
//   Sonntag 31.03.2000:  
//   ======================================================================
//   Einträge...
//




using System.Globalization;
using System.Xml.Linq;

CultureInfo.CurrentCulture = CultureInfo.InvariantCulture;

Food banana = new("Banane", 1, 2, 50);
Food apple = new("Apfel", 10, 5, 75);
Food milk = new("Milch") { Carbohydrates = 50, Fat = 20, Proteins = 3 };

Food[] foods = { apple, banana, milk, new Food("Joghurt", 1, 20, 25) };

foreach (Food food in foods)
{
  Console.WriteLine(food);
}

DiaryEntry first = new(banana, 150, new DateTime(2023, 04, 26, 07, 30, 00));
DiaryEntry second = new(banana, 120, DateTime.Today.AddHours(12).AddMinutes(45));
DiaryEntry third = new(milk, 50, DateTime.Today + TimeSpan.FromHours(9));


Console.WriteLine("\n\n");
DietDiary diary = new();
diary.AddEntries(first, second, third);
diary.AddEntry(DateTime.Now, apple, 170);
diary.AddEntry(new DateTime(2023, 4, 20), apple, 300);
diary.AddEntry(new DateTime(2023, 4, 20, 10, 30, 00), milk, 150);
Console.WriteLine(diary);

Console.WriteLine("\n\n");
List<DiaryEntry> foundEntries = diary.FindEntriesByDate(new DateOnly(2023, 4, 20));
foundEntries.ForEach(e => Console.WriteLine(e));


Console.WriteLine("\n\n\n");
DietDiaryReport report = new(diary);
string generatedContent = report.GenerateWithLinq();
Console.WriteLine(generatedContent);

DietDiarySerializer serializer = new();
XDocument document = serializer.Serialize(diary);
document.Save("diary.xml");

DietDiary loadedDiary = serializer.Deserialize("diary.xml");

report.Diary = loadedDiary;
Console.WriteLine(report.GenerateWithLinq());
