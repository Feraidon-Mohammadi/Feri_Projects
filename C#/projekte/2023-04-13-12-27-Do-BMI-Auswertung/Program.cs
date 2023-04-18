using System.Globalization; // Direktive

static double calculateBMI(double weightInKilograms, double heightInMeters)
{
  return weightInKilograms / Math.Pow(heightInMeters, 2);
}

// Challenge 2: Schreibe ein Programm, das den Nutzer Gewicht und Körpergröße eingeben lässt.
// Anschließend soll BMI berechnet werden und zuletzt mit Hilfe einer switch-Expression
// eine Beurteilung des BMI erfolgen.
// Folgende Regeln gelten:
// - Liegt BMI zwischen 18 und 25 dann hat man Normalgewicht
// - im Bereich 25 bis 30 hat man Übergewicht
// - ab 30 hat man Fettleibigkeit
// - ansonsten hat man Untergewicht

CultureInfo.CurrentCulture = CultureInfo.InvariantCulture;

Console.Write("Gib dein Gewicht in kg ein: ");
double weightInKg = double.Parse(Console.ReadLine()!);
Console.Write("Gib deine Körpergröße in m ein: ");
double heightInM = double.Parse(Console.ReadLine()!);

double bmi = calculateBMI(weightInKg, heightInM);
string classification = bmi switch
{
  < 18 => "Untergewicht",
  >= 18 and <= 25 => "Normalgewicht",
  <= 30 => "Übergewicht",
  _ => "Fettleibigkeit",
};
Console.WriteLine("Dein BMI beträgt {0:F2}. Das ist {1}.", bmi, classification);