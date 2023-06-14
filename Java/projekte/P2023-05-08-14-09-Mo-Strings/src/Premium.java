public class Premium extends AbstractBesucher{
    @Override
    public boolean isExpressEingang(boolean istWerktag) {
        return istWerktag;
        // if (istWerktag) { return true } else { return false; }
    }

    @Override
    public double calculatePreis(double basisPreis) {
        return 0.95 * basisPreis;
    }
}
