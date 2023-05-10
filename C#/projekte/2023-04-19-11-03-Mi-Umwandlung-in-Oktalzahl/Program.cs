// Challenge:
// Schreibe eine Funktion, die eine positive Zahl n als Eingabe erhält. Diese Zahl soll in Oktalschreibweise ausgegeben werden.
// Benutze hierfür keine im .NET vorhandenen Konvertierungsfunktionen, d.h. implementiere selbst den Algorithmus.
// Die Funktion soll das Ergebnis nicht selbst auf die Konsole schreiben, sondern als string-Objekt zurückgeben.
// Idee: n % 8 => erste Ziffer
//       n = n / 8
//       n % 8 => zweite Ziffer
//       usw.

using System.Text;

Console.WriteLine(ToOctalFormat(215));
Console.WriteLine(ToOctalFormat(0));
Console.WriteLine(ToOctalFormat(64));

static string ToOctalFormat(int n)
{
  StringBuilder result = new();

  do
  {
    int digit = n % 8;
    result.Insert(0, digit);
    n /= 8;
  }
  while (n > 0);

  return result.ToString();
}