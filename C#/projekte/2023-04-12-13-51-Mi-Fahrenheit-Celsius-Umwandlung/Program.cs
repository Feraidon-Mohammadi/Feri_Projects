using System.Globalization;

Console.WriteLine($"Aktuelle Kultur: {CultureInfo.CurrentCulture}");
CultureInfo.CurrentCulture = CultureInfo.GetCultureInfo("en-US");

Console.Write("Gib Temperatur in °C ein: ");
string input = Console.ReadLine()!;
double celsius = double.Parse(input);
//double fahrenheit = celsius * (9 / 5) + 32; Warnung: 9 / 5 ergibt 1, nicht 1.8 (Integer-Division!)
//double fahrenheit = celsius * (9.0 / 5) + 32; OK: Literal 9.0 ist ein Double
double fahrenheit = celsius * (9D / 5.0) + 32; // OK: Literal 9D ist ein Double
Console.WriteLine("{0} °C entsprechen {1} F", celsius, fahrenheit);
Console.WriteLine($"{celsius} °C entsprechen {fahrenheit} F");

double temperature = 12.945;
Console.WriteLine($"{temperature:F2}"); // => 12.95
Console.WriteLine($"{temperature:F1}"); // => 12.9
Console.WriteLine($"{temperature:F0}"); // => 13
Console.WriteLine($"{temperature,10:F2}"); // => _____12.95 (rechtsbündig)
Console.WriteLine($"{temperature,-10:000.00}"); // => 012.95_____ (linksbündig)

string temperatureFormat = "Temperatur: {0:F2}";
Console.WriteLine(temperatureFormat, temperature);

string formattedString = string.Format(temperatureFormat, 5.734);
Console.WriteLine(formattedString);

// Challenge:
// Schreibe ein Programm, das deinen BMI berechnet. Der BMI soll mit exakt 3 Nachkommastellen
// ausgegeben werden.  Formel: bmi = weight / height ^ 2 (Gewicht in kg, Höhe in m)
// Achtung: Gewicht soll als Grammzahl eingelesen werden und Körpergröße als cm (beides sollen Integer sein)
// String nach int parsen!
// Beispiel: weight = 80000 height = 180 ergibt BMI von 24.69
