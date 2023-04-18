/*
 Schreibe Programm, das prüft ob ein Ausdruck korrekt geklammert ist
         => true
()       => true
)()      => false
(()      => false
(())     => true
()((())) => true
 * 
 * 
 * 
 */

static bool IsCorrect(string expression)
{
  // Idee: Erhöhe Zähler für jede öffnende Klammer und vermindere ihn für jede schließende Klammer.
  // Wird Zähler negativ, wurde versucht eine Klammer zu schließen, die nicht zuvor geöffnet wurde.
  // Ist am Ende der Zähler größer 0, wurden einige Klammern nicht geschlossen.
  int numberOfOpenParenthesis = 0;

  foreach (char c in expression)
  {
    numberOfOpenParenthesis += c switch
    {
      '(' => 1,
      ')' => -1,
      _ => 0,
    };

    if (numberOfOpenParenthesis < 0) return false;
  }

  return numberOfOpenParenthesis == 0;
}

//Console.WriteLine(IsCorrect(""));         // => true
//Console.WriteLine(IsCorrect("()"));       // => true
//Console.WriteLine(IsCorrect(")("));       // => false
//Console.WriteLine(IsCorrect(")()"));      // => false
//Console.WriteLine(IsCorrect("(()"));      // => false
//Console.WriteLine(IsCorrect("(())"));     // => true
Console.WriteLine(IsCorrect("()((()))")); // => true

