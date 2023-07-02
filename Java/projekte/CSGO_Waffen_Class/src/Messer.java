public class Messer extends AbstractNahkampfwaffe implements Verschleissbar, Abwurfbar {
    @Override
    public void werfen() {
        System.out.println("peeeewwwwwww");
    }

    @Override
    public double gibAbnutzungsgrad() {
        return 0.5;
    }
}
