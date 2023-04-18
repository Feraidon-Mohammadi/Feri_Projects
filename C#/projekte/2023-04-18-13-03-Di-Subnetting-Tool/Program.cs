using System.Text.RegularExpressions;


string input = "10.50.200.40/12";

if (TryParseCIDR(input, out int[] address, out int maskLength))
{
  Console.WriteLine($"Address (decimal)     : {string.Join(".", address)}");
  Console.WriteLine($"Address (binary)      : {ToOctetsForm(FromOctetsToNumber(address))}");
  Console.WriteLine($"Subnet Mask Length    : {maskLength}");
  uint subnetMask = CalculateMask(maskLength);
  Console.WriteLine("Subnet Mask (binary)  : " + ToOctetsForm(subnetMask));
}
else
{
  Console.WriteLine($"Ungültiges Format: {input}");
  return -1;
}

return 0;


static bool TryParseCIDR(string input, out int[] address, out int mask)
{
  const string cidrPattern = @"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})/(?<mask>\d{1,2})$";

  address = new int[4];
  mask = 0;

  Match match = Regex.Match(input, cidrPattern);
  if (!match.Success) return false;

  for (int i = 0; i < address.Length; ++i)
  {
    int octet = int.Parse(match.Groups[i + 1].Value);
    if (octet is >= 0 and <= 255)
    {
      address[i] = octet;
    }
    else
    {
      return false;
    }
  }

  mask = int.Parse(match.Groups["mask"].Value);
  return mask is > 0 and < 32;
}

static string ToOctetsForm(uint value)
{
  // Idee: Extrahiere Gruppen von 8 Bits in mehreren Schiebeoperationen
  uint[] octets = new uint[4];
  uint mask = 0b1111_1111;

  foreach (int i in Enumerable.Range(0, octets.Length))
  {
    octets[i] = value & mask;
    value >>= 8;
  }

  Array.Reverse(octets);
  string result = "";
  foreach (uint octet in octets)
  {
    result += Convert.ToString(octet, 2).PadLeft(8, '0') + ".";
  }

  return result[..^1]; // Gebe alle Zeichen bis auf das letzte zurück.
}

static uint CalculateMask(int n)
{
  // Beispiel bezogen auf ein Byte:
  // n = 3. Ziel ist es, die Maske 1110_0000 zu erzeugen.
  // 1) 1 << (8 - 3) ergibt 0010_0000.
  // 2) Subtraktion von 1 ergibt 0001_1111.
  // 3) Negation ergibt 1110_0000.
  return ~((1U << (32 - n)) - 1);
}

static uint FromOctetsToNumber(int[] octets)
{
  double result = 0;
  foreach (int i in Enumerable.Range(0, octets.Length))
  {
    result += octets[i] * Math.Pow(256, octets.Length - 1 - i);
  }

  //return (uint)(octets[0] * Math.Pow(256, 3) + octets[1] * Math.Pow(256, 2) + octets[2] * Math.Pow(256, 1)
  //   + octets[3]);

  return (uint)result;
}