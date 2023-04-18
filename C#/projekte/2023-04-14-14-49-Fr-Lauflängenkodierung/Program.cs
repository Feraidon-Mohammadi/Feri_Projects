// Challenge 1:
// Schreibe ein Programm, das eine Buchstabenfolge längenkodiert. Wird ein Buchstabe x mindestens 3 mal nacheinander wiederholt
// soll er durch nx kodiert werden, wobei n die Anzahl der Wiederholungen im Bereich 3-9 ist.

// a				          => a
// aa				          => aa
// aaa				        => 3a
// aaaa_aaaa_a 	      => 9a
// aaaa_aaaa_aa	      => 9aa
// aaaa_aaaa_aaa	    => 9aaa
// aaaa_aaaa_aaaa	    => 9a3a
// a_bb_ccc_ddd_e     => abb3c3de
// abbcaaa            => abbc3a

// Challenge 2:
// Schreibe ein Programm, das eine längenkodierte Buchstabenreihenfolge wieder dekodiert.

Console.WriteLine(Decode(Encode("   a   ")));
Console.WriteLine(Decode(Encode("a")));
Console.WriteLine(Decode(Encode("aaa")));
Console.WriteLine(Decode(Encode("aaaaaaaaa")));
Console.WriteLine(Decode(Encode("aaaaaaaaaaa")));
Console.WriteLine(Decode(Encode("aaaaaaaaaaaa")));
Console.WriteLine(Decode(Encode("abbcccddde")));
Console.WriteLine(Decode(Encode("abbcaaa")));
Console.WriteLine(Decode("3caa9b"));


static string Encode(string input)
{
  char previous = '\0';
  int count = 0;
  string encoded = "";

  foreach (char next in input)
  {
    if (next == previous)
    {
      count++;
    }
    else
    {
      encoded += Repeat(previous, count);
      previous = next;
      count = 1;
    }
  }

  encoded += Repeat(previous, count);
  return encoded;
}


static string Repeat(char c, int count)
{
  if (count <= 2)
  {
    return new string(c, count);
  }

  string encoded = "";
  while (count > 0)
  {
      int n = Math.Min(9, count);
      encoded += n >= 3 ? $"{n}{c}" : new string(c, n);
      count -= n;
  }

  return encoded;
}

static string Decode(string input)
{
  string result = "";

  for (int i = 0; i < input.Length; ++i)
  {
    char current = input[i];
    if (char.IsDigit(current))
    {
      int count = int.Parse(current.ToString());
      char next = input[i + 1];
      result += new string(next, count);
      i++;
    }
    else
    {
      result += current;
    }
  }

  return result;
}