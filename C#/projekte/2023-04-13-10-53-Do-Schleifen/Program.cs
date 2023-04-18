int n = 10;

while (n >= 0)
{
  if (n == 8)
  {
    n--;
    continue;
  }

  if (n == 2)
  {
    goto abc; // Sollte generell vermieden werden, hat aber einige wenige praktische Anwendungsfälle.
  }

  Console.Write("{0:D2} ", n);
  n--; // n = n - 1;
}

abc:
Console.WriteLine();
int rows = 0;


while (rows < 5)
{
  int columns = 0;
  while (columns < 4)
  {
    Console.Write($"({rows},{columns}) ");

    if (rows == 3 && columns == 2)
    {
      goto end; // break wäre hier nicht ausreichend, da sowohl die innere als auch die äußere Schleife verlassen werden sollen.
    }

    columns++;

  }
  Console.WriteLine();

  rows++;
}

end:
Console.WriteLine("Ende der tabellarischen Ausgabe");


// Challenge:
// Gib die Zahlen 10 bis 00 auf der KOmmandozeile aus. Die 8 soll dabei ausgelassen werden.
int m = 10;
do
{
  m--;
  if (m == 8 - 1)
  {
    continue;
  }

  Console.Write("{0:D2} ", m + 1);
}
while (m >= 0);

Console.WriteLine();
for (int i = 10; i >= 0; i--)
{
  if (i == 8)
  {
    continue;
  }
  Console.Write("{0:D2} ", i);
}

Console.WriteLine();


foreach (char c in "abcdefghöüäß")
{
  Console.WriteLine($"Zeichen: {c} hat den numerischen Wert {(int)c}");
}

foreach (int i in Enumerable.Range(5, 10))
{
  Console.WriteLine(i);
}