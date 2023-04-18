Gender gender = Gender.Female;
Console.WriteLine(gender);
Console.WriteLine((int)gender);

//string gender = "m";
//gender = "f";
//gender = "d";
//gender = "afasdf";


//int gender = 0; // bedeutet Männlich
//gender = 1; // bedeutet weiblich
//gender = 2; // bedeutet divers
//gender = 5000;

Contact contact = Contact.EMail | Contact.Messenger;
contact = Contact.ByTelephone;

static void InformCustomer(Contact contact)
{
  if (contact.HasFlag(Contact.EMail))
  {
    // Sende eine eMail an ...
  }
  if (contact.HasFlag(Contact.Messenger))
  {
    // Sende WhatsApp-Nachricht an Kunde
  }
  // Teste ob contact die Flags EMail und Messenger beide besitzt.
  if (contact.HasFlag(Contact.EMail | Contact.Messenger))
  {
    // Schicke EMail UND eine Nachricht an WhatsApp
  }
}

enum Gender
{
  Unknown,
  Male,
  Female,
  Diverse
}

[Flags]
enum Contact : byte
{
  None = 0,
  Mail = 1 << 1,
  EMail = 1 << 2,
  Phone = 1 << 3,
  Mobile = 1 << 4,
  Messenger = 16,
  ByTelephone = Phone | Mobile,
}