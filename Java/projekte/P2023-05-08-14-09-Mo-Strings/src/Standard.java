public class Standard extends AbstractBesucher {
    @Override
    public boolean isExpressEingang(boolean istWerktag) {
        return false;
    }

    @Override
    public double calculatePreis(double basisPreis) {
        return basisPreis;
    }
}
