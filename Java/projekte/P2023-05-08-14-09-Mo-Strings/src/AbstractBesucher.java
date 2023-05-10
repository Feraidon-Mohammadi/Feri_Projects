public abstract class AbstractBesucher {

    public AbstractBesucher() {}

    // Abstrakte Methoden müssen in Unterklassen überschrieben werden, da sie keine Logik besitzen.
    public abstract boolean isExpressEingang(boolean istWerktag);

    // In Java darf standardmäßig jede Methode in einer Unterklasse überschrieben werden.
    // Fügt man das Schlüsselwort final hinzu, lässt sich die Methode in Unterklassen _nicht_ mehr überschreiben.
    public double calculatePreis(double basisPreis) {
        return basisPreis;
    }


    public static void main(String[] args) {

    }

}
