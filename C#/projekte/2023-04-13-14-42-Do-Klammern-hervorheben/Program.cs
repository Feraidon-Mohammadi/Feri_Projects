ConsoleColor[] colors = { ConsoleColor.White, ConsoleColor.Yellow, ConsoleColor.Red, ConsoleColor.Green, ConsoleColor.Cyan };


//foreach (ConsoleColor color in colors)
//{
//  Console.ForegroundColor = color;
//  Console.WriteLine("Test");
//}

string expression = "((()))()()";

Queue<ConsoleColor> availableColors = new(colors);
Stack<ConsoleColor> usedColors = new();

foreach (char c in expression)
{
  if (c == '(')
  {
    ConsoleColor foregroundColor = availableColors.Dequeue();
    availableColors.Enqueue(foregroundColor);
    Console.ForegroundColor = foregroundColor;
    Console.Write("(");
    usedColors.Push(foregroundColor);
  }
  else if (c == ')')
  {
    if (usedColors.Count == 0)
    {
      Console.WriteLine("Zur schließenden Klammer fehlt eine öffnende Klammer!");
      return;
    }
    ConsoleColor lastColor = usedColors.Pop();
    Console.ForegroundColor = lastColor;
    Console.Write(")");
  }
}