namespace Utils.Date;

// Eine statische Klasse erlaubt keine Objekterzeugung.
// Alle in der Klasse enthaltenen Member (Felder, Properties, Methoden etc.)
// müssen statisch sein.
// Statische Member werden direkt in der Klasse hinterlegt und von allen Objekten der Klasse geteilt.
static class DateUtils
{
  static public int CalculateDifferenceInYears(DateOnly from, DateOnly to)
  {
    if (to < from) throw new ArgumentException($"{to} liegt zeitlich vor {from}!");

    int difference = to.Year - from.Year;

    if (to.Month < from.Month || (to.Month == from.Month && to.Day < from.Day))
    {
      difference--;
    }

    return difference;
  }

}