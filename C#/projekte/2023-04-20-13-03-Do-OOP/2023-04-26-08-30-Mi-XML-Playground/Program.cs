using System.Globalization;
using System.Text;
using System.Xml;
using System.Xml.Linq;
using System.Xml.Serialization;

CultureInfo.CurrentCulture = CultureInfo.InvariantCulture;


Food banana = new("Banane", fat: 0.2, carbohydrates: 22, proteins: 1.1);
Food apple = new("Apfel")
{
  Carbohydrates = 14,
  Proteins = 0.3,
};

//SerializeFood(apple, "apple.xml");
//SerializeFood(banana, "banana.xml");

//if (DeserializeFoodFromXMLFile("apple.xml") is Food f)
//{
//  Console.WriteLine(f);
//}
//else
//{
//  Console.WriteLine($"Konnte apple nicht deserialisieren");
//}

XDocument appleDocument = SerializeFoodToXMLDocument(apple);
appleDocument.Root?.Add(new XElement("appendedChildElement", "Some content"));
appleDocument.Root?.AddFirst(new XElement("prependedChildElement", "Some content"));
appleDocument.Save(Path.Combine("data", "xapple.xml"));

appleDocument = XDocument.Load(Path.Combine("data", "xapple.xml"));
Console.WriteLine(appleDocument);
Console.WriteLine("\n");

var elementsWithAttributes = appleDocument.Root?.Descendants().Where(e => e.Attributes().Any());

var query = from element in appleDocument.Root?.Descendants()
            where element.HasAttributes
            orderby element.Name.ToString() descending
            select element.Name.ToString().ToUpper();

var query2 = query.Select(s => s.Length);

appleDocument.Root?.Descendants()
  .Where(e => e.HasAttributes)
  .OrderByDescending(e => e.Name.ToString())
  .Select(e => e.Name.ToString().ToUpper());

foreach (XName name in query)
{
  Console.WriteLine(name);
}


static XDocument SerializeFoodToXMLDocument(Food food)
{
  XDocument document = new(
    new XElement("rootElement", 
      new XElement("childElement"),
      new XComment("This is a xml comment"),
      new XElement("childElement2", new XAttribute("attributeName", "attributeValue")),
      new XElement("childElement3",
        new XElement("childElement", "Some <test> text content"),
        new XAttribute("timestamp", DateTime.Now.ToString("yyyy-MM-dd-HH-mm-ss")),
        new XAttribute("isEnabled", true)
      )
    )  
  );

  return document;
}

static Food? DeserializeFoodFromXMLFile(string filename)
{
  XmlSerializer serializer = new(typeof(Food));
  using var reader = XmlReader.Create(filename);
  return (Food?)serializer.Deserialize(reader);
}


static void SerializeFoodToXMLFile(Food food, string filename)
{
  XmlSerializer serializer = new(typeof(Food));
  XmlWriterSettings writerSettings = new()
  {
    Encoding = Encoding.UTF8,
    Indent = true,
    NewLineChars = Environment.NewLine,
  };

  // Mit dem using-Statement stellen wir sicher, dass Disposable-Objects
  // automatisch freigegeben werden. Das ist wichtig, da ansonsten Ressourcen
  // in Benutzung bleiben könnten, die eigentlich nicht mehr benötigt werden.
  // (Speicher, Dateizugriffe, Netzwerkverbindungen etc.)
  using (XmlWriter writer = XmlWriter.Create(filename, writerSettings))
  {
    serializer.Serialize(writer, food);
  }
}



