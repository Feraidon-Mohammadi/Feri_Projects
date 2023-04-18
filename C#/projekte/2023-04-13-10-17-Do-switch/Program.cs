Console.Write("Gib dein Alter ein: ");
int age = int.Parse(Console.ReadLine()!);

switch (age)
{
  case 8:
  case 9:
  case 10:
    Console.WriteLine("Du bist 8 oder 9 oder 10 Jahre alt");
    break;

  default:
    Console.WriteLine("Zu deinem Alter gibts nichts zu sagen");
    break;

}

switch (age)
{
  case >= 20 and < 50 or >= 100:
    Console.WriteLine("Dein Alter liegt im Bereich [20, 49] oder du bist mindestens 100 Jahre alt");
    break;

  case >= 0 and < 13:
    Console.WriteLine("Du bist unter 13 Jahre alt");
    break;

  default:
    Console.WriteLine("Dein Alter gehört keiner Zielgruppe an");
    break;
}

string output = age switch
{
  >= 20 and < 50 or >= 100 => "Dein Alter liegt im Bereich [20, 49] " + 
  "oder du bist mindestens 100 Jahre",
  >= 0 and < 13 => "Du bist unter 13",
  _ => "Dein Alter gehört keiner Zielgruppe an"
};

Console.WriteLine(output);

// switch Expression als Argument für WriteLine nutzen.
//Console.WriteLine(age switch
//{
//  >= 20 and < 50 or >= 100 => "Dein Alter liegt im Bereich [20, 49] " +
//  "oder du bist mindestens 100 Jahre",
//  >= 0 and < 13 => "Du bist unter 13",
//  _ => "Dein Alter gehört keiner Zielgruppe an"
//});

string message;
if (age >= 20 && age < 50 || age >= 100)
{
  message = "Dein Alter liegt im Bereich [20, 49] oder du bist mindestens 100 Jahre";
}
else if (age >= 0 && age < 13)
{
  message = "Du bist unter 13";
}
else
{
  message = "Dein Alter gehört keiner Zielgruppe an";
}

Console.WriteLine(message);