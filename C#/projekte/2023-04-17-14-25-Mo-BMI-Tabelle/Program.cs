// Challenge:
// Gib eine BMI Tabelle auf der Kommandozeile aus.
// - keine Achsenbeschriftungen
// - nur Vordergrundfarbe setzen
// - Farbe für Untergewicht, Normalgewicht, Übergewicht, Fettleibigkeit I und Fettleibigkeit II
// - Körpergröße mit 2 Nachkommastellen
// - Gewicht ohne Nachkommastellen
// - BMI Mit einer Nachkommastelle
// - Speichere die BMI Tabelle zunächst in einem double[,] Array (zweidimensionaler Array)
// - minimale und maximale Körpergröße sollen frei wählbar sein. Dasselbe gilt für das Gewicht.
// - Körpergröße wird in 2cm Schritten hochgezählt. Beim Gewicht sind es jeweils 10kg.

PrintBMITable(170, 220, 80, 160);

static void PrintBMITable(int minHeightInCm, int maxHeightInCm, int minWeightInKg, int maxWeightInKg)
{
  const int heightStep = 2;
  const int weightStep = 10;

  int rowCount = (maxHeightInCm - minHeightInCm) / heightStep + 1;
  int columnCount = (maxWeightInKg - minWeightInKg) / weightStep + 1;
  double[,] table = new double[rowCount, columnCount];

  FillTable();
  PrintWeightAxis();
  PrintTable();
  Console.ResetColor();

  void FillTable()
  {
    for (int height = minHeightInCm, rowIndex = 0; rowIndex < table.GetLength(0); rowIndex++, height += heightStep)
    {
      for (int weight = minWeightInKg, columnIndex = 0; columnIndex < table.GetLength(1); columnIndex++, weight += weightStep)
      {
        table[rowIndex, columnIndex] = CalculateBMI(height, weight);
      }
    }
  }

  void PrintWeightAxis()
  {
    Console.Write(new string(' ', 5));
    for (int weight = minWeightInKg; weight <= maxWeightInKg; weight += weightStep)
    {
      Console.Write($"{weight,5} ");
    }
    Console.WriteLine();
  }

  void PrintTable()
  {
    for (int rowIndex = table.GetLength(0) - 1, height = maxHeightInCm; rowIndex >= 0; rowIndex--, height -= heightStep)
    {
      Console.ResetColor();
      Console.Write($"{height / 100.0:F2} ");
      for (int columnIndex = 0; columnIndex < table.GetLength(1); columnIndex++)
      {
        double bmi = table[rowIndex, columnIndex];
        Console.ForegroundColor = bmi switch
        {
          < 18.5 => ConsoleColor.Blue,
          < 25 => ConsoleColor.Green,
          < 30 => ConsoleColor.Yellow,
          < 35 => ConsoleColor.DarkYellow,
          _ => ConsoleColor.Red
        };
        Console.Write($"{bmi,5:F1} ");
      }
      Console.WriteLine();
    }
  }

}

static double CalculateBMI(int heightInCm, int weightInKg) => weightInKg / Math.Pow(heightInCm / 100.0, 2);



