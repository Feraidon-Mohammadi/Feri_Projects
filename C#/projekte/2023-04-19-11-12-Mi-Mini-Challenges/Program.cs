/* Challenge: Gib folgende Muster auf der Konsole aus
 * 1) Gib Daten mit Hilfe von verschachtelten Schleifen aus.
 *    1 2 3 4 5
 *    1 2 3 4
 *    1 2 3
 *    1 2
 *    1
 * 2) 1 10 2 9 3 8 4 7 5 6 6 5 7 4 8 3 9 2 10 1   (nur eine Schleife notwendig)
 * 3) Gib Daten tabellarisch aus, in dem du eine verschachtelte Schleife nutzt!
 *    0 0 0 0 1 
 *    0 1 0 0 1 
 *    0 0 1 0 1
 *    0 0 0 1 1
 *    1 1 1 1 1
 * 4) Berechne die Fibonacci-Folge f(n) = f(n-2) + f(n-1) wobei f(0) = 0 und f(1) = 1 (nur eine Schleife notwendig)
 *    0 1 1 2 3 5 8 13 21 34 55 89 144
 * 5) 1 2 3 4 5 6 6 5 4  3  2   1 (mit einer Schleife)   
 *    1 2 3 4 5 6 7 8 9 10 11  12
 *    
 *    1 2 3 4 5 5 4 3 2 1
 *    1 2 3 4 5 6 7 8 9 10
 * 6) Mi verschachtelter Schleife:
 *    1 5  9 13
 *    2 6 10 14
 *    3 7 11 15
 *    4 8 12 16
 *    
 */

using System.Text;

Challenge01(5);
Console.WriteLine("\n");
Challenge02(10);
Console.WriteLine("\n");
Challenge03(8);
Console.WriteLine("\n");
Challenge04(1);
Challenge04(2);
Challenge04(3);
Challenge04(4);
Challenge04(5);
Challenge04(6);
Challenge04(7);
Challenge04(8);
Console.WriteLine("\n");
Challenge05(10);
Console.WriteLine("\n");
Challenge06(6);
Console.WriteLine("\n");




int?[,] values = ZigZag(3, 20);
for (int i = 0; i < values.GetLength(0); i++)
{
  for (int j = 0; j < values.GetLength(1); j++)
  {
    int? value = values[i, j];
    if (value.HasValue) Console.Write($"{value:D2} ");

  }
  Console.WriteLine();
}
Console.WriteLine("\n");

int[] numbers = { 5, 8, 2, 0 };
int index = FindMaximum(numbers, out int max);
Console.WriteLine($"Das Maximum von {string.Join(",", numbers)} ist {max}. Es befindet sich an Position {index}.");
Console.WriteLine("\n");

Console.WriteLine(RemoveVowels("Eine wunderschöne Landschaft ist hier zu sehen!"));
Console.WriteLine("\n");


Console.WriteLine(AbbreviateEnd("12345678", 0));
Console.WriteLine(AbbreviateEnd("12345678", 1));
Console.WriteLine(AbbreviateEnd("12345678", 2));
Console.WriteLine(AbbreviateEnd("12345678", 3));
Console.WriteLine(AbbreviateEnd("12345678", 4));
Console.WriteLine(AbbreviateEnd("12345678", 5));
Console.WriteLine(AbbreviateEnd("12345678", 6));
Console.WriteLine(AbbreviateEnd("12345678", 8));
Console.WriteLine(AbbreviateEnd("12345678", 10));
Console.WriteLine(AbbreviateEnd("Maximilian", 6));

Console.WriteLine("\n");
Console.WriteLine(Abbreviate("Maximilian", 5, AbbreviationMode.End));
Console.WriteLine(Abbreviate("Maximilian", 5, AbbreviationMode.Start));
Console.WriteLine(Abbreviate("Maximilian", 5, AbbreviationMode.Center));
Console.WriteLine(Abbreviate("Maximilian", 6, AbbreviationMode.Center));
Console.WriteLine(Abbreviate("Maximilian", 7, AbbreviationMode.Center));

Console.WriteLine(Abbreviate("Maximilian", 2, AbbreviationMode.End));
Console.WriteLine(Abbreviate("Maximilian", 2, AbbreviationMode.Start));
Console.WriteLine(Abbreviate("Maximilian", 2, AbbreviationMode.Center));

Console.WriteLine(Abbreviate("Maximilian", 20, AbbreviationMode.End));
Console.WriteLine(Abbreviate("Maximilian", 20, AbbreviationMode.Start));
Console.WriteLine(Abbreviate("Maximilian", 20, AbbreviationMode.Center));


static void Challenge01(int n)
{
  for (int columnCount = n; columnCount > 0; columnCount--)
  {
    for (int value = 1; value <= columnCount; value++)
    {
      Console.Write($"{value:D2} ");
    }
    Console.WriteLine();
  }
}

static void Challenge02(int n)
{
  for (int i = 1, j = n; i <= n; i++, j--)
  {
    Console.Write($"{i:D2} {j:D2} ");
  }
}

static void Challenge03(int n)
{
  for (int row = 1; row <= n; row++)
  {
    for (int column = 1; column <= n; column++)
    {
      char c = (row == n || column == n || (row == column && row != 1)) ? '1' : '0';
      Console.Write($"{c} ");
    }
    Console.WriteLine();
  }
}

static void Challenge04(int n)
{
  for (int prev = -1, next = 1, k = 1; k <= n; k++)
  {
    int sum = prev + next;
    Console.Write($"{sum:D2} ");
    prev = next;
    next = sum;
  }

  Console.WriteLine();
}

static void Challenge05(int n)
{
  for (int i = 1; i <= 2 * n; i++)
  {
    int value = i <= n ? i : (2 * n + 1 - i);
    Console.Write($"{value:D2} ");
  }
}

static void Challenge06(int n)
{
  int value;
  for (int row = 1; row <= n; row++)
  {
    value = row;
    for (int column = 1; column <= n; column++, value += n)
    {
      Console.Write($"{value:D2} ");
    }
    Console.WriteLine();
  }
}

static int?[,] ZigZag(int maxRows, int maxColumns)
{
  int value = 1;
  int row = 1, column = 1;
  Direction direction = Direction.None;

  int?[,] values = new int?[maxRows, maxColumns];

  do
  {
    values[row - 1, column - 1] = value++;

    bool canGoLeft = column > 1;
    bool canGoRight = column < maxColumns;
    bool canGoDown = row < maxRows;
    bool canGoUp = row > 1;
    bool canGoUpRight = canGoUp && canGoRight;
    bool canGoDownLeft = canGoDown && canGoLeft;

    direction = direction switch
    {
      Direction.None when canGoRight => Direction.Right,
      Direction.UpRight when canGoUpRight => Direction.UpRight,
      Direction.UpRight when canGoRight => Direction.Right,
      Direction.UpRight => Direction.Down,
      Direction.DownLeft when canGoDownLeft => Direction.DownLeft,
      Direction.DownLeft when canGoDown => Direction.Down,
      Direction.DownLeft => Direction.Right,
      Direction.Right when canGoUpRight => Direction.UpRight,
      Direction.Right when canGoDownLeft => Direction.DownLeft,
      Direction.Down when canGoUpRight => Direction.UpRight,
      Direction.Down when canGoDownLeft => Direction.DownLeft,
      _ => Direction.None
    };

    (int deltaColumn, int deltaRow) = direction switch
    {
      Direction.Down => (0, 1),
      Direction.DownLeft => (-1, 1),
      Direction.Right => (1, 0),
      Direction.UpRight => (1, -1),
      _ => (0, 0),
    };

    row += deltaRow;
    column += deltaColumn;


  } while (direction != Direction.None);

  return values;
}

static int FindMaximum(int[] numbers, out int max)
{
  if (numbers.Length == 0) throw new ArgumentException("Keine Zahlen vorhanden");

  int indexOfMax = 0;
  max = numbers[indexOfMax];

  for (int i = 1; i < numbers.Length; ++i)
  {
    int number = numbers[i];
    if (number <= max) continue;
    max = number;
    indexOfMax = i;
  }

  return indexOfMax;
}

static string RemoveVowels(string s)
{
  StringBuilder result = new();
  foreach (char c in s)
  {
    if ("aeiou".Contains(char.ToLower(c))) continue;
    // if (char.ToLower(c) is 'a' or 'e' or 'i' or 'o' or 'u') continue;
    result.Append(c);
  }
  return result.ToString();
}

static string AbbreviateEnd(string s, int maxLength)
{
  if (s.Length <= maxLength) return s;

  const string ellipsis = "...";

  // s.Length > maxLength -> Eine Kürzung ist notwendig!
  if (maxLength <= ellipsis.Length) return ellipsis[..maxLength];
  // maxLength > ellipsis.Length
  return s[0..(maxLength - ellipsis.Length)] + ellipsis;
}

static string Abbreviate(string s, int maxLength, AbbreviationMode mode = AbbreviationMode.End)
{
  if (mode == AbbreviationMode.End) return AbbreviateEnd(s, maxLength);

  if (s.Length <= maxLength) return s;

  const string ellipsis = "...";
  if (maxLength <= ellipsis.Length) return ellipsis[..maxLength];
  
  int remaining = maxLength - ellipsis.Length;

  if (mode == AbbreviationMode.Start)
  {
    return "..." + s[^remaining..];
  }

  if (mode == AbbreviationMode.Center)
  {
    // "abcdefgh", 5 => "a...h"   remaining = 2
    // "abcdefgh", 6 => "ab...h"  remaining = 3
    // "abcdefgh", 7 => "ab...gh" remaining = 4
    // "abcdefgh", 8 => "abcdefgh"

    int fromRight = remaining / 2;
    int fromLeft = remaining - fromRight;

    return s[..fromLeft] + ellipsis + s[^fromRight..];
  }

  throw new ArgumentException($"Ungülter Modus: {mode}");
}


enum Direction
{
  None, Right, Down, UpRight, DownLeft
}

enum AbbreviationMode
{
  Start, Center, End,
}


/* Challenge:
 * 1) Schreibe Funktion, die einen int-Array erhält, darin das Maximum sucht und sowohl das Maximum als auch seine Position zurückgibt.
 *    void FindMaximum(int[] numbers, out int max, out int index)
 * 2) Schreibe eine Funktion, die eine Zeichenkette erhält und nur jene Zeichen zurückgibt, die keine Vokale sind (a,e,i,o,u).
 *    string RemoveVowels(string s)
 * 3) Schreibe eine Funktion, die eine Zeichenkette mit "..." am Ende abkürzt:
 *    string Abbreviate(string s, int maxLength)
 *    Beispiel: Abbreviate("Maximilian", 5) => "Ma..."
 *              Abbreviate("Maximilian", 6) => "Max..."
 *    Hinweis: Ist maxLength <= 3 gib nur die entsprechende Anzahl an Punkten aus oder s selbst, sofern dessen Länge <= maxLength ist.
 *              Abbreviate("Maximilian", 3) => "..."
 *              Abbreviate("Maximilian", 2) => ".." 
 * 4) Erweitere die Funktion Abbreviate wie folgt:
 *    - erstelle eine Enumeration AbbreviationMode mit den Konstanten Start, Center, End
 *    - die Abbreviate Funktion bekommt einen zusätzlichen Parameter mode vom Typ AbbreviationMode
 *    - ist der Mode Start gewählt, muss die Zeichenkette am Anfang gekürzt werden
 *    - ist der Mode Center gewählt, erfolgt die Abkürzung in der Mitte
 *    - im Modus End wird am Ende gekürzt, wie in der vorherigen Implementierung von Abbreviate
 *    
 *    Beispiele:
 *    Abbreviate("Maximilian", 5, AbbreviationMode.Start)  => "...an"
 *    Abbreviate("Maximilian", 7, AbbreviationMode.Start)  => "...lian"
 *    Abbreviate("Maximilian", 5, AbbreviationMode.Center) => "M...n"
 *    Abbreviate("Maximilian", 6, AbbreviationMode.Center) => "Ma...n"
 *    Abbreviate("Maximilian", 7, AbbreviationMode.Center) => "Ma...an"
 *    Abbreviate("Maximilian", 7, AbbreviationMode.End)    => "Maxi..."
 */

/* Challenge:
 * Schreibe eine Funktion, die ein Zick-Zack Muster erzeugt.
 *  1  2  6  7 15
 *  3  5  8 14 16
 *  4  9 13 17 22
 * 10 12 18 21 23
 * 11 19 20 24 25
 */