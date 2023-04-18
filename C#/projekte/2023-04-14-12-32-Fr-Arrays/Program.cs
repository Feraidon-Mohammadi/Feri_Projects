// Challenge:
// Auf der Kommandozeile sollen dem Programm beliebig viele Zahlen übergeben werden.
// Diese Zahlen sollen aufaddiert und deren Summe ausgegeben werden.


using System.Globalization;
using System.Reflection.Metadata;

CultureInfo.CurrentCulture = CultureInfo.InvariantCulture;


Console.Title = "Summieren";

double sum = 0;

foreach (string argument in args)
{
  if (double.TryParse(argument, out double number))
  {
    sum += number;
  }
  else
  {
    Console.WriteLine($"Ignoriere Eingabe {argument}");
  }

}

Console.WriteLine($"Summe ist {sum:F4}");

int a = 4;
int b = 5;
Add(in a, in b, out int r); // call-by-reference
Console.WriteLine(a);
Console.WriteLine(b);
Console.WriteLine(r);


static int Add(in int first, in int second, out int result)
{
  result = first + second;
  return result;
}

int c = 3;
int q = Square(c); // call-by-value (Standardverhalten)
Console.WriteLine(q); // => 9
Console.WriteLine(c); // => 3

static int Square(int value)
{
  value = value * value;
  return value;
}

int u = 1;
int v = 2;
Console.WriteLine($"u = {u} v = {v}");
SwapInts(ref u,  ref v);
Console.WriteLine($"u = {u} v = {v}");

static void SwapInts(ref int a, ref int b)
{
  int temp = a;
  a = b;
  b = temp;
}

string x = "Hans";
string y = "Wurst";
Console.WriteLine($"x = {x} y = {y}"); // => x = Hans y = Wurst
SwapStrings(ref x, ref y);
Console.WriteLine($"x = {x} y = {y}"); // => x = Wurst y = Hans

static void SwapStrings(ref string a, ref string b)
{
  string temp = a;
  a = b;
  b = temp;
}