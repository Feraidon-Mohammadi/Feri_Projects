using System.Text;

public class DietDiaryReport
{
  private static readonly string ThickRuler = new('=', 100);
  private static readonly string ThinRuler = new('-', 100);

  public DietDiary Diary { get; set; }



  public DietDiaryReport(DietDiary diary)
  {
    Diary = diary;

  }

  public string Generate()
  {
    return Generate(DateOnly.MinValue, DateOnly.MaxValue);
  }

  public string Generate(DateOnly? from = null, DateOnly? to = null)
  {
    if (Diary.GetEntries().Count == 0) return string.Empty;

    List<DiaryEntry> entries = Diary.FindEntriesInRange(from ?? DateOnly.MinValue, to ?? DateOnly.MaxValue);
    List<DiaryEntry> sortedEntries = entries.OrderByDescending(e => e.CreatedAt).ToList();

    DateOnly startDate = DateOnly.FromDateTime(sortedEntries[^1].CreatedAt);
    DateOnly endDate = DateOnly.FromDateTime(sortedEntries[0].CreatedAt);

    StringBuilder output = new();

    for (DateOnly date = endDate; date >= startDate; date = date.AddDays(-1))
    {
      List<DiaryEntry> entriesOnDate = Diary.FindEntriesByDate(date);
      if (entriesOnDate.Count == 0) continue;

      StringBuilder dayOutput = new();
      double totalCalories = 0, totalFat = 0, totalProteins = 0, totalCarbs = 0;

      foreach (DiaryEntry entry in entriesOnDate.OrderBy(e => e.CreatedAt))
      {
        Food food = entry.Food;

        totalCalories += entry.Calories;
        totalFat += entry.Fat;
        totalProteins += entry.Proteins;
        totalCarbs += entry.Carbohydrates;

        dayOutput
          .Append($"{entry.CreatedAt.ToString("HH:mm")} ")
          .Append($"{food.Name,-15} ")
          .Append($"{entry.Amount,10:0.00}")
          .Append($"{entry.Calories,10:0.00}")
          .Append($"{entry.Fat,10:0.00}")
          .Append($"{entry.Proteins,10:0.00}")
          .Append($"{entry.Carbohydrates,10:0.00}")
          .AppendLine();

      }

      dayOutput
        .AppendLine(ThinRuler)
        .Append($"{entriesOnDate.Count:D2} ")
        .Append($"{totalCalories:F2} ")
        .Append($"{totalFat:F2}g ({ToPercent(totalFat * Food.CaloriesFat, totalCalories):F2}) ")
        .Append($"{totalProteins:F2}g ({ToPercent(totalProteins * Food.CaloriesProteins, totalCalories):F2}) ")
        .Append($"{totalCarbs:F2}g ({ToPercent(totalCarbs * Food.CaloriesCarbohydrates, totalCalories):F2}) ")
        .AppendLine();

      dayOutput.Insert(0,
        $"{date:dddd dd.MM.yyyy} {totalCalories} kcal "
        + $"{totalFat}g {totalProteins}g {totalCarbs}g\n{ThickRuler}\n");

      output.Append(dayOutput).AppendLine();
    }

    return output.ToString();



  }

  public string GenerateWithLinq(DateOnly? fromDate = null, DateOnly? toDate = null)
  {
    List<DiaryEntry> entries = Diary.FindEntriesInRange(fromDate ?? DateOnly.MinValue, toDate ?? DateOnly.MaxValue);
    var entryGroups = entries.GroupBy(e => e.CreatedAt.Date).OrderByDescending(g => g.Key).ToList();
    StringBuilder output = new();

    foreach (IGrouping<DateTime, DiaryEntry> entryGroup in entryGroups)
    {
      // Das Objekt entryGroup enthält eine Gruppe von DiaryEntry-Objekten sowie 
      // den gemeinsamen Gruppierschlüssel Key (e.CreatedAt.Date).
      double totalAmount = entryGroup.Sum(e => e.Amount);
      double totalCalories = entryGroup.Sum(e => e.Calories);
      double totalFat = entryGroup.Sum(e => e.Fat);
      double totalFatPercent = ToPercent(totalFat * Food.CaloriesFat, totalCalories);
      double totalProteins = entryGroup.Sum(e => e.Proteins);
      double totalProteinsPercent = ToPercent(totalProteins * Food.CaloriesProteins, totalCalories);
      double totalCarbs = entryGroup.Sum(e => e.Carbohydrates);
      double totalCarbsPercent = ToPercent(totalCarbs * Food.CaloriesCarbohydrates, totalCalories);
      double entryCount = entryGroup.Count();
      DateTime date = entryGroup.Key.Date;

      output.AppendFormat("{0} {1:F2}kcal F={2:F2}g ({3:F2}%) P={4:F2}g ({5:F2}%) K={6:F2}g ({7:F2}%)",
        date.ToString("dddd dd.MM.yyy"),
        totalCalories,
        totalFat, totalFatPercent,
        totalProteins, totalProteinsPercent,
        totalCarbs, totalCarbsPercent);
      output.AppendLine().AppendLine(ThickRuler);

      foreach (DiaryEntry entry in entryGroup.OrderBy(e => e.CreatedAt))
      {
        output.AppendFormat("{0} {1} {2,-15} {3,10:F2} {4,10:F2} {5,10:F2} {6,10:F2} {7,10:F2}",
          entry.CreatedAt.ToString("dd.MM.yyyy"), entry.CreatedAt.ToString("HH:mm"),
          entry.Food.Name, entry.Amount, entry.Calories, entry.Fat, entry.Proteins, entry.Carbohydrates);
        output.AppendLine();
      }

      // Anzahl Menge Kalorien Fette Prots Carbs
      output.AppendLine(ThinRuler)
        .AppendFormat("{6,16} {0,-15} {1,10:F2} {2,10:F2} {3,10:F2} {4,10:F2} {5,10:F2}",
          entryCount, totalAmount, totalCalories, totalFat, totalProteins, totalCarbs, string.Empty)
        .AppendLine();


      output.Append('\n', 3);
    }

    return output.ToString();
  }




  private static double ToPercent(double amount, double total) => amount / total * 100;

  // test
  // var query = from entry in Diary.FindEntriesInRange(fromDate ?? DateOnly.MinValue, toDate ?? DateOnly.MaxValue)
  //            let date = entry.CreatedAt.Date
  //            group entry by date into entryGroup
  //            let date = entryGroup.Key
  //            orderby date descending
  //            select new {
  //              Date = date,
  //              Entries = entryGroup.ToList(),
  //              Calories = entryGroup.Sum(e => e.Calories)
  //            };

}
