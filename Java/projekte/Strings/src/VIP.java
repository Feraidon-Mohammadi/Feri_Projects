// Die Klasse VIP ist eine konkrete Klasse, da sie keinen abstract-Modifier besitzt.
// VIP ist zudem Unterklasse von AbstractBesucher. Dies wird durch das Schlüsselwort
// extends ausgedrückt.
// Eine Unterklasse erbt sämtliche Felder und Attribute von ihrer Oberklasse bzw. von
// ihren Vorfahren.
// Achtung: Nicht alle Felder und Methoden sind automatisch in der Unterklasse sichtbar.
// Die Sichtbarkeit wird durch die Zugriffsmodifizierer in der Oberklasse definiert.
public class VIP extends AbstractBesucher {

    public String lieblingsgetränk;

    @Override
    public boolean isExpressEingang(boolean istWerktag) {
        return true;
    }

    @Override
    public double calculatePreis(double basisPreis) {
        return 0.9 * basisPreis;
    }
}
