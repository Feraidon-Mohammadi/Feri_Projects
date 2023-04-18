// Ein Array mit 3 Elementen. Jedes Element ist eine
// Referenz auf einen Array von int. Die Elemente haben
// zu Beginn den Wert null.
int[][] table = new int[3][]; // => { null, null, null }
table[1] = new int[5] { 10, 20, 30, 40, 50 };

int[][] table2 = new int[3][]
{
  new int[] {},
  new int[] { 10, 20, 30, 40, 50 },
  new int[] { }
};

// Hier handelt es sich um ein Array, das aus 3 Elementen besteht. Jedes Element ist
// eine Referenz auf ein Array, welches int-Werte speichert.
int[][] board = new int[3][];
for (int i = 0; i < board.Length; ++i)
{
  board[i] = new int[4];
}
(board[1])[2] = 99;

for (int row = 0; row < board.Length; row++)
{
  for (int column = 0; column < board[row].Length; column++)
  {
    Console.Write($"{board[row][column]:D2} ");
  }
  Console.WriteLine();
}

Console.WriteLine();

// Hier handelt es sich um ein Array, das aus 3 * 4 = 12 int-Werten besteht.
int[,] rectangularBoard = new int[3, 4];
rectangularBoard[1, 2] = 77;
for (int row = 0; row < rectangularBoard.GetLength(0); row++)
{
  for (int column = 0; column < rectangularBoard.GetLength(1); column++)
  {
    Console.Write($"{rectangularBoard[row, column]:D2} ");
  }
  Console.WriteLine();
}