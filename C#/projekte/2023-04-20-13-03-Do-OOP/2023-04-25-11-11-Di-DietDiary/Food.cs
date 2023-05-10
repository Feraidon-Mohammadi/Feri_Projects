public class Food
{
  public const double ServingSize = 100.0;
  public const double CaloriesFat = 9.0;
  public const double CaloriesProteins = 4.0;
  public const double CaloriesCarbohydrates = 4.0;
  public const double KiloJoulesPerCalorie = 4.2;

  public double Fat { get; set; }

  public double Proteins { get; set; }

  public double Carbohydrates { get; set; }

  public string Name { get; set; }

  public double Calories
  {
    get => Fat * CaloriesFat + Proteins * CaloriesProteins + Carbohydrates * CaloriesCarbohydrates;
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
    return $"{nameof(Food)}[Fat={Fat:00.00}, Proteins={Proteins:00.00}, Carbs={Carbohydrates:00.00}, Name={Name}]";
  }

}



