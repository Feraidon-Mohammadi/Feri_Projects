public class MolotovCocktail extends AbstractWaffe implements Abwurfbar, Verzoegert {

    @Override
    public void werfen() {
        System.out.println("Its getting hot in here.");
    }

    @Override
    public double gibVerzoegerungInSekunden() {
        return 3;
    }

    @Override
    public void setVerzoegerungInSekunden(double sekunden) {

    }
}
