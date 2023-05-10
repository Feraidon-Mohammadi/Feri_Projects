using System.Globalization;
using System.Text;
using System.Xml.Serialization;

public class Food
{
  public const double ServingSize = 100.0;
  public const double CaloriesFat = 9.0;
  public const double CaloriesProteins = 4.0;
  public const double CaloriesCarbohydrates = 4.0;
  public const double KiloJoulesPerCalorie = 4.2;

  [XmlElement(ElementName = "Fett")]
  public double Fat { get; set; }

  [XmlAttribute(AttributeName = "Proteine")]
  public double Proteins { get; set; }

  public double Carbohydrates { get; set; }

  public string Name { get; set; }

  public double Calories
  {
    get => Fat * CaloriesFat + Proteins * CaloriesProteins + Carbohydrates * CaloriesCarbohydrates;
  }

  public Food() : this(string.Empty)
  {

  }

  public Food(string name, double fat = 0, double proteins = 0, double carbohydrates = 0)
  {
    Name = name;
    Fat = fat;
    Proteins = proteins;
    Carbohydrates = carbohydrates;
  }

  public double CalculateCaloriesForAmount(double amount) => amount / ServingSize * Calories;

  public override string ToString()
  {
    StringBuilder builder = new();
    string properties = $"Name={Name}, Fat={Fat}, Proteins={Proteins}, Carbohydrates={Carbohydrates}";
    builder.AppendFormat("{0}[{1}]", this.GetType().FullName, properties);
    return builder.ToString();
  }
}



