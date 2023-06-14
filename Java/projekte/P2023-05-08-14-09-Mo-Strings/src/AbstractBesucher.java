public abstract class AbstractBesucher {

    public AbstractBesucher() {}

    // Abstrakte Methoden müssen in Unterklassen überschrieben werden, da sie keine Logik besitzen.
    public abstract boolean isExpressEingang(boolean istWerktag);

    // In Java darf standardmäßig jede Methode in einer Unterklasse überschrieben werden.
    // Fügt man das Schlüsselwort final hinzu, lässt sich die Methode in Unterklassen _nicht_ mehr überschreiben.
    public double calculatePreis(double basisPreis) {
        return basisPreis;
    }

    // Eine Fabrikmethode dient der Erstellung neuer Objekte. Sie nutzt intern den Konstruktor der Klasse.
    public static AbstractBesucher createBesucher(String typ) {
        return switch (typ) {
            case "VIP" -> new VIP();
            case "PREMIUM" -> new Premium();
            case "STANDARD" -> new Standard();
            default -> throw new IllegalArgumentException("Nicht unterstützter Typ: %s".formatted(typ));
        };

    }

    public static void main(String[] args) {

       AbstractBesucher vipBesucher = AbstractBesucher.createBesucher("VIP");
       AbstractBesucher premiumBesucher = AbstractBesucher.createBesucher("PREMIUM");
       vipBesucher.isExpressEingang(false);
       premiumBesucher.isExpressEingang(true);

    }

}
