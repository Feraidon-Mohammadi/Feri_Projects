using System.Text;
using Utils.Date;

class Person
{
  public string FirstName { get; set; } = string.Empty;
  public string LastName { get; set; } = string.Empty;

  // Nullable<Birthdate>
  public DateOnly? Birthdate { get; set; } = null;
  public Gender Gender { get; set; } = Gender.Unknown;
  public string CountryOfBirth { get; set; } = string.Empty;
  public Address? MainAddress { get; set; }
  public Address? SecondaryAddress { get; set; }

  private string[] nationalities = Array.Empty<string>();
  public string[] Nationalities
  {
    get => nationalities;
    set
    {
      //nationalities = value; // Würde nur die Referenz kopieren!
      this.nationalities = new string[value.Length];
      Array.Copy(value, this.nationalities, value.Length);
    }
  }

  public int Age
  {
    get
    {
      if (!Birthdate.HasValue)
      {
        throw new InvalidOperationException("Alter nicht berechenbar, da kein Geburtsdatum vorhanden ist.");
      }
      return DateUtils.CalculateDifferenceInYears(Birthdate.Value, DateOnly.FromDateTime(DateTime.Today));
    }
  }
  // public int Age
  // {
  //   get { return DateUtils..... }
  // }

  // Bevor der Konstruktor seine Aufgabe beginnt, werden alle Feld und Property-Initialisierer
  // ausgeführt.
  public Person()
  {

  }

  public Person(string first, string last, Gender gender)
  {
    this.FirstName = first;
    this.LastName = last;
    this.Gender = gender;
  }



  // Hinweis: this bezieht sich auf das Objekt, auf dem
  // die Methode aufgerufen wurde.
  public override string ToString()
  {
    string gender = Gender switch
    {
      Gender.Diverse => "divers",
      Gender.Female => "weiblich",
      Gender.Male => "männlich",
      _ => "unbekannt"
    };

    StringBuilder builder = new();
    builder
      .AppendFormat("Name: {0}, {1}\n", check(LastName), check(FirstName))
      .AppendFormat("Geburtsdatum: {0}\n", check(Birthdate?.ToString("dd.MM.yyyy")))
      .AppendFormat("Alter: {0}\n", Birthdate.HasValue ? $"{Age} Jahre" : "unbekannt")
      .AppendLine($"Geschlecht: {gender}")
      .AppendLine($"Geburtsland: {check(CountryOfBirth)}")
      .AppendLine($"Staatsangehörigkeiten: {string.Join(", ", Nationalities)} ")
      .AppendLine($"Hauptwohnsitz:\n{check(MainAddress, "keiner")}")
      .AppendLine($"Nebenwohnsitz:\n{check(SecondaryAddress, "keiner")}");


    return builder.ToString();

    static string check(object? anObject, string defaultValue = "unbekannt")
    {
      if (anObject is string s && string.IsNullOrWhiteSpace(s)) return defaultValue;
      return anObject?.ToString() ?? defaultValue;
    }


  }


  // Kurzform: MainAddress?.ToString() ?? "keiner"
  // Langform:
  // string? result = null;
  // if (MainAddress != null)
  // {
  //   result = MainAddress.ToString();
  // }
  // if (result == null)
  // {
  //   result = "keiner";
  // }

}