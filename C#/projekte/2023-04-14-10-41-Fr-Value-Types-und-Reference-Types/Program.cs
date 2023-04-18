// Datentyp double ist ein Value-Type. Das heißt, dass der eigentliche
// Wert direkt in der Variablen gespeichert wird und der Wert somit
// im Stack-Speicher hinterlegt ist.
static double CalculateBMI(double weightInGrams, double heightInCentimeters)
{
  // 1) Erzeugen wir eine lokale Variable, wird diese im Stack abgelegt.
  // 2) Ist der Datentyp der Variablen ein Value-Type, dann wird auch der Wert der Variablen
  //    direkt im Stack gespeichert.
  double weightInKilograms = weightInGrams / 1000.0;
  double heightInMeters = heightInCentimeters / 100.0;

  return weightInKilograms / Math.Pow(heightInCentimeters, 2);
}

// Datentyp string ist ein Reference-Type. Eine string-Variable speichert also nicht das String-Objekt selbst,
// sondern lediglich einen Verweis / Referenz auf das string-Objekt im Heap.
static string GetFullName(string firstName, string lastName)
{
  string fullName = $"{firstName} {lastName}";
  return fullName;
}

Console.WriteLine("Programmstart");
//double bmi = CalculateBMI(10, 5); 
//bmi = CalculateBMI(20, 10);

string rainer = "Rainer";
string name = GetFullName(rainer, "Zufall");

Console.WriteLine("Programmende");