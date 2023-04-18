// Challenge:
// Schreibe ein Programm, das deinen BMI berechnet. Der BMI soll mit exakt 3 Nachkommastellen
// ausgegeben werden.  Formel: bmi = weight / height ^ 2 (Gewicht in kg, Höhe in m)
// Achtung: Gewicht soll als Grammzahl eingelesen werden und Körpergröße als cm (beides sollen Integer sein)
// String nach int parsen!
// Beispiel: weight = 80000 height = 180 ergibt BMI von 24.69

string horizontalRule = new ('=', 40);
Console.WriteLine($"BMI Berechnung\n{horizontalRule}");

Console.Write("Gib dein Gewicht in Gramm an: ");
int weightInGrams = int.Parse(Console.ReadLine()!);
Console.Write("Gib deine Körpergröße in cm an: ");
int heightInCm = int.Parse(Console.ReadLine()!);

//double bmi = (weightInGrams / 1000.0) / ( (heightInCm / 100.0) * (heightInCm / 100.0) );
double bmi = (weightInGrams / 1000.0) / Math.Pow(heightInCm / 100.0, 2);
//Console.WriteLine($"Dein BMI beträgt {bmi:F3}");
Console.WriteLine("Dein BMI beträgt {0:F3}", bmi);