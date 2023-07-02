import java.util.List;

public class Program {
    public static void main(String[] args) {

        Granate granate = new Granate(2);
        granate.setName("granny");
        MolotovCocktail cocktail = new MolotovCocktail();
        cocktail.setName("masseltov");

        List<AbstractWaffe> waffen = List.of(new Messer(), granate, cocktail, new Maschinengewehr(2));
        AbstractWaffe eineWaffe = waffen.get(0);

        for (AbstractWaffe waffe : waffen) {
            System.out.printf("Ich bin eine Waffe vom Typ %s und heiße \"%s\". -> ",
                    waffe.getClass().getName(), waffe.getName());
            // Prüfe ob die Klasse des Objektes waffe die Schnittstelle Abwurfbar implementiert.
            // Der instanceof Operator wird zur Laufzeit ausgewertet!
            if (waffe instanceof Abwurfbar) {
                // Caste das Objekt in die Abwurfbar-Schnittstelle, um Zugriff auf deren Methoden zu erhalten.
                ((Abwurfbar) waffe).werfen();
            }
        }
    }

    // Challenge: Füge der Klasse AbstractWaffe ein name-Feld hinzu, welches privat ist. Um den Namen auszulesen
    // und zu ändern, sollen entsprechende Getter und Setter-Methoden implementiert werden.
    // In der Schleife (siehe oben) soll zusätzlich der Name der Waffe ausgegeben werden.



}
