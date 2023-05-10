using System.Text;
using System.Xml.Serialization;

public class DietDiary
{
  private List<DiaryEntry> entries = new();

  public DietDiary()
  {

  }

  public void AddEntry(DateTime timestamp, Food food, double amount)
  {
    DiaryEntry entry = new(food, amount, timestamp);
    entries.Add(entry);
  }

  public void AddEntries(params DiaryEntry[] entries)
  {
    this.entries.AddRange(entries);
  }

  public void RemoveEntries(Predicate<DiaryEntry> predicate)
  {
    entries.RemoveAll(predicate);
  }

  public List<DiaryEntry> GetEntries()
  {
    return entries.ToList();
  }

  public List<DiaryEntry> FindEntries(Predicate<DiaryEntry> predicate)
  {
    // Filtere alle Elemente aus der entries-Liste, die das angegebene
    // Prädikat erfüllen.
    return entries.Where(entry => predicate(entry)).ToList();
  }

  public List<DiaryEntry> FindEntriesByDate(DateOnly date)
  {
    return FindEntries(entry => DateOnly.FromDateTime(entry.CreatedAt) == date);
  }

  public List<DiaryEntry> FindEntriesInRange(DateOnly from, DateOnly to)
  {
    return entries.Where(e => InRange(e, from, to)).ToList();

    static bool InRange(DiaryEntry entry, DateOnly from, DateOnly to)
    {
      DateOnly date = DateOnly.FromDateTime(entry.CreatedAt);
      return date >= from && date <= to;
    }
  }

  public override string ToString()
  {
    StringBuilder builder = new();
    // Datum Uhrzeit Menge Lebensmittel kcal
    foreach (DiaryEntry entry in entries.OrderByDescending(e => e.CreatedAt))
    {
      builder.Append($"{entry.CreatedAt.ToString("yyyy-MM-dd")} ")
        .Append($"{entry.CreatedAt.ToString("HH:mm")} ")
        .Append($"{entry.Amount.ToString("0.00") + " g",8} ")
        .Append($"{(entry.Food?.Name ?? "-"),-15} ")
        .Append($"{entry.Calories.ToString("0.00") + " kcal", 12} ")
        .AppendLine();
    }
    return builder.ToString();
  }

}
