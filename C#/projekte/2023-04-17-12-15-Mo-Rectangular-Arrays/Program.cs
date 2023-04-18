// Erste Dimension = 2; => 2 Elemente
int[] oneDimensionalArray = { 1, 2 };
Console.WriteLine(oneDimensionalArray[0]); // => 1
Console.WriteLine(oneDimensionalArray[1]); // => 2

// Erste Dimension = 4, Zweite Dimension = 2
// => 4 * 2 = 8 Elemente
int[,] twoDimensionalArray = { { 1, 2 }, { 3, 4 }, { 5, 6 }, { 7, 8 } };
Console.WriteLine(twoDimensionalArray[2, 1]); // => 6
Console.WriteLine(twoDimensionalArray[1, 0]); // => 3


// Erste Dimension = 3, Zweite Dimension = 4, Dritte Dimension = 2
// => 3 * 4 * 2 = 24 Elemente
int[,,] threeDimensionalArray =
{
  {
    { 1, 2 }, { 3, 4 }, { 5, 6 }, { 7, 8 }
  },
  {
    { 9, 10 }, { 11, 12 }, { 13, 14 }, { 15, 16 }
  },
  {
    { 17, 18 }, { 19, 20 }, { 21, 22 }, { 23, 24 }
  }
};
Console.WriteLine(threeDimensionalArray[1, 2, 0]); // => 13


// Erste Dimension = 2, Zweite Dimension = 3, Dritte Dimension = 4, Vierte Dimension = 2
// => 2 * 3 * 4 * 2 = 48 Elemente, die direkt nacheinander im Speicher stehen.
int[,,,] fourDimensionalArray =
{
  {
    {
      { 1, 2 }, { 3, 4 }, { 5, 6 }, { 7, 8 }
    },
    {
      { 9, 10 }, { 11, 12 }, { 13, 14 }, { 15, 16 }
    },
    {
      { 17, 18 }, { 19, 20 }, { 21, 22 }, { 23, 24 }
    }
  },
  {
    {
      { 1, 2 }, { 3, 4 }, { 5, 6 }, { 7, 8 }
    },
    {
      { 9, 10 }, { 11, 12 }, { 13, 14 }, { 15, 16 }
    },
    {
      { 17, 18 }, { 19, 20 }, { 21, 22 }, { 23, 24 }
    }
  }
};
Console.WriteLine(fourDimensionalArray[1, 1, 1, 0]); // => 11
Console.WriteLine(fourDimensionalArray[1, 2, 0, 1]); // => 18


int[,] table = new int[5, 4]; // initialisiert alle 20 Elemente mit 0.
Console.WriteLine(table.GetLength(0)); // => 5
Console.WriteLine(table.GetLength(1)); // => 4
Console.WriteLine(table.Length); // => 5 * 4 = 20 Elemente
Console.WriteLine(table.Rank); // => 2 (zwei Dimensionen)

// Challenge: Initialisiere alle Zellen der Tabelle table, in dem du sie absteigend durchnummerierst.
int n = 20;
for (int row = 0; row < table.GetLength(0); ++row)
{
  for (int column = 0; column < table.GetLength(1); ++column)
  {
    //table[row, column] = table.Length - (row * table.GetLength(1)) - column;
    table[row, column] = n--;
  }
}

Console.WriteLine(table);

string[] names = { "alice", "bob", "charlie", "damian" };
Array.Reverse(names);
Console.WriteLine(string.Join(",", names));

// Challenge: Schreibe eine Methode, die die Reihenfolge der Elemente eines Arrays umkehrt.
// Bemerkung: nutze nur Indizes, Schleifen und Zuweisungen. Das Original-Array soll modifiziert werden.

string[] pets = { "ape", "bear", "cat", "dog" };
ReverseStringArray(pets);
Console.WriteLine(string.Join(", ", pets));
static void ReverseStringArray(string[] array)
{
  for (int i = 0, j = array.Length - 1; i < array.Length / 2; i++, j--)
  {
    string temporary = array[i];
    array[i] = array[j];
    array[j] = temporary;
  }
}