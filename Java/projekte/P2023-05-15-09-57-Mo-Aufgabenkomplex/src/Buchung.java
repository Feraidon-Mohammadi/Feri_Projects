import java.time.LocalDate;

public class Buchung {

    private LocalDate startDatum;
    private LocalDate endDatum;


    public static void main(String[] args) {
        Buchung ersteBuchung = new Buchung(LocalDate.of(2023, 05, 24), LocalDate.of(2023, 05, 28));
        Buchung zweiteBuchung = new Buchung(LocalDate.of(2023, 05, 20), LocalDate.of(2023, 05, 29));
        Buchung dritteBuchung = new Buchung(LocalDate.of(2023, 05, 25), LocalDate.of(2023, 05, 26));
        Buchung vierteBuchung = new Buchung(LocalDate.of(2023, 04, 25), LocalDate.of(2023, 04, 26));
        Buchung fünfteBuchung = new Buchung(LocalDate.of(2023, 06, 25), LocalDate.of(2023, 06, 26));
        Buchung sechsteBuchung = new Buchung(LocalDate.of(2023, 05, 25), LocalDate.of(2023, 06, 26));
        Buchung siebteBuchung = new Buchung(LocalDate.of(2023, 04, 25), LocalDate.of(2023, 05, 26));

        System.out.println(ersteBuchung.überschneidetSichMit(ersteBuchung));   // T
        System.out.println(ersteBuchung.überschneidetSichMit(zweiteBuchung));  // T
        System.out.println(ersteBuchung.überschneidetSichMit(dritteBuchung));  // T
        System.out.println(ersteBuchung.überschneidetSichMit(vierteBuchung));  // F
        System.out.println(ersteBuchung.überschneidetSichMit(fünfteBuchung));  // F
        System.out.println(ersteBuchung.überschneidetSichMit(sechsteBuchung));  // T
        System.out.println(ersteBuchung.überschneidetSichMit(siebteBuchung));  // T

        System.out.println(ersteBuchung.überschneidetSichMit(ersteBuchung));   // T
        System.out.println(zweiteBuchung.überschneidetSichMit(ersteBuchung));  // T
        System.out.println(dritteBuchung.überschneidetSichMit(ersteBuchung));  // T
        System.out.println(vierteBuchung.überschneidetSichMit(ersteBuchung));  // F
        System.out.println(fünfteBuchung.überschneidetSichMit(ersteBuchung));  // F
        System.out.println(sechsteBuchung.überschneidetSichMit(ersteBuchung));  // T
        System.out.println(siebteBuchung.überschneidetSichMit(ersteBuchung));  // T

        Buchung[] buchungen = new Buchung[] { zweiteBuchung, dritteBuchung, vierteBuchung, fünfteBuchung,sechsteBuchung, siebteBuchung};
        System.out.println(ersteBuchung);
        System.out.println(istBuchungMöglich(buchungen, ersteBuchung));
        ersteBuchung = new Buchung(LocalDate.of(2023, 1, 10), LocalDate.of(2023, 02, 3));
        System.out.println(ersteBuchung);
        System.out.println(istBuchungMöglich(buchungen, ersteBuchung));
    }

    public static boolean istBuchungMöglich(Buchung[] buchungen, Buchung neueBuchung) {
        for (Buchung eineBuchung : buchungen) {
            if (eineBuchung.überschneidetSichMit(neueBuchung)) {
                System.out.println("Überschneidung mit %s".formatted(eineBuchung));
                return false;
            }
        }
        return true;
    }

    @Override
    public String toString() {
        return "Buchung vom %s bis %s".formatted(this.startDatum, this.endDatum);
    }

    public Buchung(LocalDate startDatum, LocalDate endDatum) {
        if (endDatum.isBefore(startDatum)) throw new IllegalArgumentException("Enddatum liegt vor Startdatum");
        this.startDatum = startDatum;
        this.endDatum = endDatum;
    }

    public boolean überschneidetSichMit(Buchung eineBuchung) {
//        if (this.endDatum.isBefore(eineBuchung.startDatum)) return false;
//        if (this.startDatum.isAfter(eineBuchung.endDatum)) return false;
//        return true;


        // compareTo liefert den Wert 0 wenn erstes und zweites Datum gleich sind. CompareTo liefert einen negativen Wert, wenn
        // erstes Datum vor dem zweiten Datum liegt. Ein positiver Wert bedeutet, dass das erste Datum zeitlich nach dem zweiten Datum kommt.
        return this.endDatum.compareTo(eineBuchung.startDatum) >= 0 && this.startDatum.compareTo(eineBuchung.endDatum) <= 0;
    }


}
