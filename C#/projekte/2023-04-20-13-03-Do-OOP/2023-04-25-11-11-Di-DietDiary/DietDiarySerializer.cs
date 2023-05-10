using System.Globalization;
using System.Text;
using System.Xml;
using System.Xml.Linq;
using System.Xml.Serialization;

public class DietDiarySerializer
{
  private const string TimestampFormat = "yyyy-MM-dd-HH-mm-ss";

  public DietDiarySerializer()
  {
  }

  public XDocument Serialize(DietDiary diary)
  {
    List<Food> distinctFoods = diary.GetEntries().Select(e => e.Food).Distinct().ToList();
    Dictionary<Food, int> foodToIdMap = new();

    int id = 1;

    foreach (Food food in distinctFoods)
    {
      foodToIdMap[food] = id++;
    }

    XElement foodsElement = new("Foods");
    ToFoodElements(distinctFoods).ForEach(e => foodsElement.Add(e));
    XElement entriesElement = new("Entries");
    ToEntryElements(diary.GetEntries(), foodToIdMap).ForEach(e => entriesElement.Add(e));

    XElement diaryElement = new("Diary", foodsElement, entriesElement);
    XDocument document = new(diaryElement);

    return document;
  }

  private List<XElement> ToEntryElements(IEnumerable<DiaryEntry> entries, Dictionary<Food, int> foodToIdMap)
  {
    List<XElement> elements = new();

    foreach (DiaryEntry entry in entries)
    {
      XElement element = new("Entry",
        new XElement("FoodID", foodToIdMap[entry.Food]),
        new XElement("Amount", entry.Amount),
        new XElement("Timestamp", entry.CreatedAt.ToString(TimestampFormat)));
      elements.Add(element);
    }

    return elements;
  }

  private List<XElement> ToFoodElements(IEnumerable<Food> foods, int startId = 1)
  {
    List<XElement> elements = new();

    int id = startId;
    foreach (Food food in foods)
    {
      XElement element = new("Food",
        new XAttribute("id", id++),
        new XElement("Name", food.Name),
        new XElement("Fat", food.Fat),
        new XElement("Protein", food.Proteins),
        new XElement("Carbohydrates", food.Carbohydrates)
      );
      elements.Add(element);
    }

    return elements;
  }

#nullable disable
  public DietDiary Deserialize(string filename)
  {
    DietDiary diary = new();

    XDocument document = XDocument.Load(filename);
    XElement foods = document.Root.Element("Foods");
    XElement entries = document.Root.Element("Entries");

    // 1) Baue ein Dictionary, welches eine ID auf ein Food Objekt abbildet
    // 2) Erzeuge die DiaryEntry-Objekte und füge sie zum Diary hinzu.

    Dictionary<int, Food> idToFoodMap = new();
    foreach (XElement foodElement in foods.Elements())
    {
      int foodId = int.Parse(foodElement.Attribute("id").Value);
      Food food = new(foodElement.Element("Name").Value)
      {
        Carbohydrates = ParseDouble(foodElement.Element("Carbohydrates")),
        Fat = ParseDouble(foodElement.Element("Fat")),
        Proteins = ParseDouble(foodElement.Element("Protein"))
      };

      idToFoodMap[foodId] = food;
    }

    foreach (XElement entryElement in entries.Elements())
    {
      int foodId = (int)ParseDouble(entryElement.Element("FoodID"));
      DateTime timestamp = DateTime.ParseExact(entryElement.Element("Timestamp").Value, TimestampFormat, CultureInfo.InvariantCulture);
      double amount = ParseDouble(entryElement.Element("Amount"));
      Food food = idToFoodMap[foodId];

      diary.AddEntry(timestamp, food, amount);
    }

    return diary;

    static double ParseDouble(XElement element)
    {
      return double.Parse(element.Value, CultureInfo.InvariantCulture);
    }
  }


}

// Bemerkung: Funktioniert nicht wie gewünscht, da Anforderungen des XmlSerializers nicht erfüllt werden.
// StringBuilder output = new();
// XmlSerializer serializer = new(typeof(DietDiary));
// using XmlWriter writer = XmlWriter.Create(output, new XmlWriterSettings()
// {
//   Indent = true,
//   Encoding = Encoding.UTF8
// });
// serializer.Serialize(writer, diary);
// return output.ToString();