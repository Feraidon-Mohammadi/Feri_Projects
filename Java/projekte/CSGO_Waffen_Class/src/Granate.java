public class Granate extends AbstractWaffe implements Verzoegert, Abwurfbar {

    private double verzoegerung = 0;

    public Granate(double verzoegerung) {
        this.verzoegerung = verzoegerung;
    }

    @Override
    public void werfen() {
        System.out.println("Weeeeeeeee");
    }

    @Override
    public double gibVerzoegerungInSekunden() {
        return verzoegerung;
    }

    @Override
    public void setVerzoegerungInSekunden(double sekunden) {
        verzoegerung = sekunden;
    }
}
