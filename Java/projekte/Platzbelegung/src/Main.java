import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Platzzustand[] belegung = {
                Platzzustand.BELEGT,Platzzustand.FREI,Platzzustand.FREI,Platzzustand.FREI, Platzzustand.FREI,
                Platzzustand.BELEGT,Platzzustand.BELEGT,Platzzustand.BELEGT,Platzzustand.FREI,Platzzustand.FREI
        };
        hatMindestensNFreiePlätze(belegung,7);
        System.out.println(belegung);



        Platzzustand[] belegung2 = {
                Platzzustand.BELEGT,Platzzustand.FREI,Platzzustand.FREI,Platzzustand.FREI, Platzzustand.FREI,
                Platzzustand.BELEGT,Platzzustand.BELEGT,Platzzustand.BELEGT,Platzzustand.FREI,Platzzustand.FREI,
                Platzzustand.FREI,Platzzustand.FREI
                };
        hatMindestensNFreiePlätze2(belegung2,7);
        System.out.println(belegung2);













    }
    public static boolean hatMindestensNFreiePlätze(Platzzustand[] belegung, int n) {
        int zehler = 0;
        for (int platzn = 0; platzn < belegung.length; platzn++) {
            Platzzustand zustand = belegung[zehler];
            if (zustand == Platzzustand.FREI) {
                zehler++;
            } else if (zustand == Platzzustand.BELEGT) {
                zehler = 0;
            }
            if (zehler >= n) {
                return true;
            }
        }
        return false;
    }

    public static boolean hatMindestensNFreiePlätze2(Platzzustand[] sitzreihe, int n) {
        int zehler = 0;
        for (int platzn = 0; platzn < sitzreihe.length; platzn++) {
            Platzzustand zustand = sitzreihe[zehler];
            if (zustand == Platzzustand.FREI) {
                zehler = 0;

                if (sitzreihe.length - platzn - 1 < n) {
                    return false;
                }

            } else if(zustand == Platzzustand.FREI){
                zehler++;
            }
            if(zehler >= n ){
                return true;
            }
        }
        return false;
    }





}