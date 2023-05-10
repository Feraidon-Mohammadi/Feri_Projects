using Introduction.Classes;

UserAccount anyAccount; // uninitialisierte Variable
anyAccount = new UserAccount("M_Mustermann", "0!Abqwertz", "Max Mustermann"); // nachträgliche Initialisierung der Variablen anyAccount.

UserAccount guestAccount = new UserAccount("Gast", "beamMeUp123!", "Gast Gast", "info@cloud.mustermann.io");

anyAccount.Username = "M_Mustermann";
anyAccount.FullName = "  Max    Mustermann  ";
anyAccount.EMail = "Max.Mustermann@cloud.mustermann.io";
Console.WriteLine(anyAccount.EMail);
Console.WriteLine(anyAccount.IsExpired);
Console.WriteLine(anyAccount.IsActive);
//anyAccount.IsActive = true;
Console.WriteLine(anyAccount.FullName);
bool wasChanged = anyAccount.TryChangePassword("qWertz#123456$");
Console.WriteLine($"Passwort wurde geändert: {wasChanged}.");
Console.WriteLine($"Neues Passwort: {anyAccount.GetPassword()}");
Console.WriteLine($"Neues Passwort: {anyAccount.Password}");
//anyAccount.Password = "huhu";
//anyAccount.ExpirationTime = new DateTime(2024, 5, 15);

Console.WriteLine(anyAccount.ToString());

Console.WriteLine($"Account {anyAccount.Username} läuft in " 
  + $"{(anyAccount.ExpirationTime - DateTime.Now).TotalDays} Tagen ab.");

guestAccount.Username = "guest";
guestAccount.ExpirationTime = new DateTime(2100, 12, 31);
Console.WriteLine($"Name des Gastkontos lautet: {guestAccount.Username}");



// Schlüsselwort var sagt dem Compiler, dass er selbst den Datentyp
// für die Variable anhand des Initialisierungswertes bestimmen soll.
// var salesManagerAccount = new UserAccount();
// UserAccount? salesManagerAccount = new UserAccount();

