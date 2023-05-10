using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

public class DiaryEntry
{
  private double amount = 0;

  public DateTime CreatedAt { get; set; }

  public double Calories =>
    Food?.CalculateCaloriesForAmount(Amount)
    ?? throw new InvalidOperationException($"Kein Lebensmittel eingetragen, um Kalorien zu berechnen");

  /// <summary>
  /// Berechnet die Menge an Fett, die verzehrt wurde.
  /// Dieser Wert ist abhängig von der gewählten Portionsgröße (Amount).
  /// </summary>
  public double Fat => AdjustToAmount(Food.Fat, Amount);
  public double Proteins => AdjustToAmount(Food.Proteins, Amount);
  public double Carbohydrates => AdjustToAmount(Food.Carbohydrates, Amount);

  public double Amount
  {
    get => amount;
    set
    {
      amount = value >= 0 ? value : throw new ArgumentException("Menge darf nicht negativ sein!");
    }
  }
  public Food Food { get; set; }

  public DiaryEntry(Food food, double amount, DateTime? timestamp = null)
  {
    Food = food;
    Amount = amount;
    CreatedAt = timestamp ?? DateTime.Now;
  }

  public override string ToString()
  {
    StringBuilder builder = new();
    builder.Append($"{nameof(DiaryEntry)}[")
      .Append($"{nameof(Amount)}={Amount:000.00}")
      .Append($", {nameof(CreatedAt)}={CreatedAt.ToString("yyyy-MM-dd-ddd@HH:mm")}")
      .Append($", {nameof(Food)}={Food?.ToString()}")
      .Append($", {nameof(Calories)}={Calories}")
      .Append(']');

    return builder.ToString();
  }

  private static double AdjustToAmount(double amount, double value)
  {
    return amount / Food.ServingSize * value;
  }
}
