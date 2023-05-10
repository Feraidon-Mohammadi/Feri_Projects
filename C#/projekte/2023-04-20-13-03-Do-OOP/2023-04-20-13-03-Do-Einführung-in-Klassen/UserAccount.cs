using System;
using System.Collections.Generic;
using System.Diagnostics.CodeAnalysis;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace Introduction.Classes;

internal class UserAccount
{
  // Zustand für Objekte (sogenannte Instanzfelder)
  private string username;
  private string password;
  private string fullName;
  private string? emailAddress;
  //private bool isActive;

  // Ein Konstruktor ist eine besondere Methode, die ein neu erzeugtes Objekt
  // in einen validen Anfangszustand versetzt. Der Konstruktor wird vom new
  // Operator aufgerufen. Er kann nicht nachträglich aufgerufen werden.
  public UserAccount(string username, string password, string fullName) 
    : this(username, password, fullName, null)
  {
    // Dieser Konstruktor ruft einen anderen Konstruktor auf.

  }


  public UserAccount(string username, string password, string fullName, string? emailAddress)
  {
    Username = username;
    if (!TryChangePassword(password))
    {
      throw new ArgumentException("Ungültiges Passwort");
    }
    FullName = fullName;
    EMail = emailAddress;
    CreationTime = DateTime.Now;
    ExpirationTime = CreationTime + TimeSpan.FromDays(180);
  }


  // Property namens Password, welches nur lesbar ist.
  // Properties erlauben zusätzliche Logik beim Lesen
  // und Schreiben auszuführen. Sie kombinieren die Syntax
  // von herkömmlichen Feldern mit zusätzlicher Logik.
  // Außerdem erlauben sie die Konfiguration des Lese/Schreib-Zugriffs.
  public string Password
  {
    get { return password; }
  }

  public string Username
  {
    // Code, der beim Lesen des Properties auszuführen ist.
    get
    {
      return username;
    }

    // Code, der beim Schreiben des Properties auszuführen ist.
    [MemberNotNull(nameof(username))]
    set
    {
      // Im Setter können wir mit der Variablen value auf den zu setzenden Wert
      // zugreifen.
      if (string.IsNullOrWhiteSpace(value))
      {
        throw new ArgumentException($"{value} ist ein ungültiger Name.");
      }
      username = value;
    }
  }


  public string FullName
  {
    get
    {
      return fullName.ToUpper();
    }

    [MemberNotNull(nameof(fullName))]
    set
    {
      string[] parts = value.Split(' ').Where(s => s.Length > 0).ToArray();
      if (parts.All(s => s.Length >= 2) && parts.Length >= 2)
      {
        fullName = string.Join(" ", parts);
        return;
      }
      throw new ArgumentException($"Name muss aus mindestens zwei Wörtern mit je mindestens 2 Buchstaben bestehen");
    }
  }

  public DateTime CreationTime { get; }
  
  public DateTime ExpirationTime { get; set; }

  public bool IsExpired
  {
    get
    {
      return DateTime.Now >= ExpirationTime;
    }
  }
  //public bool IsExpired => DateTime.Now >= expirationTime;

  // Ein Automatic-Property lässt den Compiler ein entsprechendes Feld
  // für das Property anlegen. IsActive darf gelesen aber nur intern
  // geschrieben werden.
  public bool IsActive { get; private set; }

  public string? EMail
  {
    get => emailAddress;
    set
    {
      if (value == null)
      {
        emailAddress = null;
        return;
      }

      const string emailPattern = @"^[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+$";
      if (Regex.Match(value, emailPattern).Success)
      {
        emailAddress = value.ToLower();
        return;
      }
      throw new ArgumentException($"Ungültiges Format");
    }
  }

  //public bool IsActive
  //{
  //  get => isActive;
  //  set => isActive = value;
  //}

  // Eine Methode, die das interne Passwort zurückgibt.
  // public string GetPassword() => password;
  public string GetPassword()
  {
    return password;
  }

  // Eine Methode zum Ändern des Passworts.
  [MemberNotNullWhen(true, nameof(password))]
  public bool TryChangePassword(string newPassword)
  {
    if (newPassword.Length < 8) return false;

    const string specialCharacters = @"!$#?";
    bool containsSpecialCharacter = newPassword.Any(specialCharacters.Contains); // some (Any) / every (All)
    bool containsUpperChar = newPassword.Any(char.IsUpper);
    bool containsDigit = newPassword.Any(char.IsDigit);

    //bool containsSpecialCharacters = newPassword.Any(c => specialCharacters.Contains(c));

    //bool containsSpecialChar = false;
    //foreach (char c in specialCharacters)
    //{
    //  containsSpecialChar = containsSpecialChar || newPassword.Contains(c);
    //}
    //if (!containsSpecialChar) return false;

    if (containsSpecialCharacter && containsUpperChar && containsDigit)
    {
      password = newPassword;
      return true;
    }

    return false;
  }
}

// Challenge B:
// Füge ein nur-lesbares bool Property IsExpired hinzu, das prüft, ob das Nutzerkonto
// abgelaufen ist. Füge außerdem ein Property namens IsActive hinzu, welches speichert,
// ob das Nutzerkonto aktuell benutzt werden darf.

// Challenge A:
// Füge ein privates Feld namens fullName hinzu. Füge außerdem ein public Property
// namens FullName hinzu, welches gelesen und geschrieben werden darf.
// Beim Auslesen ist der FullName in Großbuchstaben zurückzugeben.
// Beim Schreiben muss geprüft werden, ob mindestens zwei Wörter angegeben wurden
// und beide Wörter jeweils aus mindestens 2 Buchstaben bestehen.

// Challenge C:
// Füge ein Property namens EMail hinzu. Beim Setzen muss geprüft werden, ob es
// sich um eine valide EMail-Adresse handelt. Verwende hierfür reguläre Ausdrücke.
