import java.util.List;

public class Besucher {

    // Ein statisches Feld (im Gegensatz zu einem Instanzfeld / Instanzvariable) wird direkt in der
    // Klasse selbst gespeichert. Alle Objekte der Klasse Besucher teilen sich dieses Feld.
    // Auf ein statisches Feld wird anhand der Klasse zugegriffen, nicht jedoch anhand eines Objektes.
    public static double basisPreis = 10.50;

    private String typ; // Das ist eine Instanzvariable.
    // Jedes Objekt vom Typ Besucher hat ein eigenes typ-Feld.

    public Besucher(String typ) {
        // Speichere den Wert des Parameters typ in das Feld typ.
        this.typ = typ;
    }

    public Besucher() {
        this.typ = "STANDARD";
    }

    // Entscheidet, ob der Besucher den Expresseingang benutzen darf.
    public boolean isExpressEingang(boolean isWerktag) {
        // Lösung mit if-else if-else
//        if (this.typ.equals("VIP")) {
//            return true;
//        } else if (this.typ.equals("PREMIUM")) {
//            return isWerktag;
//        } else if (this.typ.equals("STANDARD")) {
//            return false;
//        }
//        return false;

        // Lösung mit switch-Expression
        return switch (this.typ) {
            case "VIP" -> true;
            case "PREMIUM" -> isWerktag;
            case "STANDARD" -> false;
            case "ERMÄSSIGT" -> false;
            default -> false;
        };
    }

    public double calculatePreis(double basisPreis) {
        return switch (this.typ) {
            case "VIP" -> 0.9 * basisPreis;
            case "PREMIUM" -> 0.95 * basisPreis;
            case "ERMÄSSIGT" -> 0.5 * basisPreis;
            default -> basisPreis;
        };
    }

    public static void main(String[] args) {
        Besucher feri = new Besucher("VIP");
        Besucher shalelu = new Besucher("SHALELU");
        Besucher kamil = new Besucher("PREMIUM");
        Besucher tugba = new Besucher("STANDARD");
        Besucher norman = new Besucher("ERMÄSSIGT");
        Besucher maria = new Besucher();

        System.out.println(Besucher.basisPreis);

        // Der Datentyp List<E> ist polymorph, da er je nach Typargument einen
        // anderen Datentyp repräsentiert. Z.B. List<Besucher>, List<Integer>, etc.
        // => List<String> und List<Integer> sind völlig unterschiedliche Datentypen!
        List<Besucher> besucherliste = List.of(feri, maria, kamil);
        List<Integer> zahlen = List.of(1,2,3,4,5);
        List<String> namen = List.of("alice", "bob", "charlie");


    }


}
