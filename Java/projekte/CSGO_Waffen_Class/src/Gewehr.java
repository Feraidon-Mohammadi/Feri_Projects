public class Gewehr extends AbstractWaffe {

    protected int verbleibendeMunition;

    public Gewehr(int startMunition) {
        verbleibendeMunition = startMunition;
    }

    public int getVerbleibendeMunition() {
        return verbleibendeMunition;
    }

}
