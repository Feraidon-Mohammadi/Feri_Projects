using System.Text;

class Address
{
  public string? Street { get; set; }
  public string? StreetNumber { get; set; }
  public string? ZipCode { get; set; }
  public string? City { get; set; }
  public string? Country { get; set; }

  // Die Methode ToString wurde von der Klasse System.Object
  // geerbt, allerdings besitzt die Methode eine Implementierung,
  // die lediglich den Klassennamen ausgibt. Wir wollen diese
  // Implementierung deshalb "überschreiben" (override).
  public override string ToString()
  {
    StringBuilder builder = new();
    builder.AppendLine($"Street: {Street} {StreetNumber}")
      .AppendLine($"City: {City} ({ZipCode})")
      .AppendLine($"Country: {Country}");
    return builder.ToString();
  }

}