public class allone {
    //   Hier ist ein Beispiel für eine Klasse "Game", die alle 9 Optionen enthält:
    //

    public class Game {
        //  متغیرهای نمونه: متغیرهایی که به هر نمونه از کلاس تعلق دارند
        //  و مقادیر آنها به طور مستقل از همدیگر هستند
        // Instanzvariablen: "title", "releaseYear", "genres" und "rating".
        private String title;
        private int releaseYear;
        private String[] genres;
        private int rating;



        /*
        * primitive Datentypen wie int, double, boolean usw.
        */
        int anzahl = 0;         // Instanzvariable vom Typ int
        boolean istWahr = true; // Instanzvariable vom Typ boolean
        double preis = 9.99;    // Instanzvariable vom Typ double





        /*
        *Referenzdatentypen wie Strings, Arrays, Objekte usw.
        */
        String name = "Max Mustermann";    // Instanzvariable vom Typ String
        int[] zahlen = {1, 2, 3, 4, 5};    // Instanzvariable vom Typ Array
        Object objekt = new Object();      // Instanzvariable vom Typ Object




        public void setName(String neuerName) {
            this.name = neuerName;
        }

        public void setZahlen(int[] neueZahlen) {
            this.zahlen = neueZahlen;
        }

        public void setObjekt(Object neuesObjekt) {
            this.objekt = neuesObjekt;
        }


    /*
     * Weitere komplexe Datentypen wie z.B. Enumeration
     * */
    enum Wochentag { MONTAG, DIENSTAG, MITTWOCH, DONNERSTAG,FREITAG,SAMSTAG,SONNTAG}













        // سازندگان: متد‌های ویژه‌ای هستند که برای ایجاد نمونه‌های جدید کلاس استفاده می‌شوند.
        // Konstruktor: der Konstruktor, um eine neue Instanz von "Game" zu erstellen.
        // 1) Standardkonstruktor (auch Default-Konstruktor genannt)
        // 2) Parameterisierter Konstruktor
        public Game(String title, int releaseYear, String[] genres, int rating) {
            this.title = title;
            this.releaseYear = releaseYear;
            this.genres = genres;
            this.rating = rating;
        }

        // 1) standardkonstruktor
        public class Beispiel {
            private int zahl;
            private String name;


            // standardkonstrukor
            public Beispiel() {
                this.zahl = 0;
                this.name = "";
            }
        }

        // 2) parameterisiserte konstruktor
        public class Beispiel1 {
            private int zahl;
            private String name;

            // Parameterisierter Konstruktor
            public Beispiel1(int zahl, String name) {
                this.zahl = zahl;
                this.name = name;
            }
        }








        private int zahl;
        // متدهای نمونه: متدهایی که می‌توان به یک نمونه خاص از کلاس اعمال کر
        // Instanzmethode: "play()", um das Spiel zu spielen.
        public void play() {
            System.out.println("Playing " + title);
        }

        // Instanzmethode ohne Parameter
        public void erhoeheZahl() {
            this.zahl++;
        }

        // Instanzmethode mit einem Parameter
        public void setzeZahl(int zahl) {
            this.zahl = zahl;
        }

        // Instanzmethode mit einem Rückgabewert und einem Parameter
        public int multipliziereZahl(int faktor) {
            return this.zahl * faktor;
        }














        // متغیرهای کلاس: متغیرهایی که با خود کلاس و نه با یک نمونه از کلاس مرتبط هستند.
        // Klassenvariable: "numberOfGames", um die Anzahl der erstellten Spiele zu zählen.
        // es gibt nur ein typ nicht mehr
        public static int numberOfGames = 0;

        private static int anzahlInstanzen = 0;

        public static int getAnzahlInstanzen() {
            return anzahlInstanzen;
        }











        // متدهای کلاس: متدهایی که می‌توان به کلاس به عنوان یک کل اعمال کرد.
        // Klassenmethode: "displayNumberOfGames()", um die Anzahl der erstellten Spiele anzuzeigen.
        // es gibt nur eins
        public static void displayNumberOfGames() {
            System.out.println("Number of games: " + numberOfGames);
        }




        // بلوک‌های مقدماتی استاتیک: بلوک‌های کدی هستند که یک بار در هنگام بارگذاری کلاس اجرا می‌شوند.
        // Statischer Initialisierungsblock: um den Start der Game-Klasse zu initialisieren.
        static {
            System.out.println("Initializing Game class...");
        }




        // کلاس‌های درونی: کلاس‌هایی هستند که در داخل یک کلاس دیگر تعریف شده‌اند
        // و می‌توانند به ویژگی‌ها و متدهای آن دسترسی داشته باشند.
        // Innere Klasse: "GameStats", um die Statistiken des Spiels anzuzeigen.
        public class GameStats {
            public void displayStats() {
                System.out.println("Title: " + title);
                System.out.println("Release Year: " + releaseYear);
                System.out.println("Genres: " + String.join(", ", genres));
                System.out.println("Rating: " + rating);
            }
        }




        // رابط‌ها: تعریف متد‌هایی هستند که می‌توانند توسط کلاس‌های دیگر پیاده‌سازی شوند
        // تا یک رفتار خاص را فراهم کنند.
        // Schnittstelle: "Playable", um das Spielen des Spiels zu definieren.
        public interface Playable {
            void play();
        }




        // شمارش‌ها: تعریف ثابت‌های پیش‌فرضی هستند که در یک   شیوه شمارش خاص نشان داده می‌شوند
        //  Enumeration: "Genre", um die verschiedenen Genres des Spiels darzustellen.
        public enum Genre {
            ACTION,ADVENTURE,RPG,STRATEGY,SPORTS,SIMULATION,PUZZLE,PLATFORMER,FIGHTING
        }
    }

}
