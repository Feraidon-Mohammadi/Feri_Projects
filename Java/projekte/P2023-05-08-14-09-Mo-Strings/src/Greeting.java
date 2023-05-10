import java.util.Scanner;

public class Greeting {
    public static void main(String[] args) {
        System.out.print("Gib deinen Namen ein: ");
        // Ein Scanner-Objekt kann Zahlen und Zeichenketten aus einem Datenstrom lesen.
        // Hier erzeugen wir ein Scanner-Objekt, das vom Standard-Eingabedatenstrom liest.
        Scanner scanner = new Scanner(System.in);
        scanner = null;
        // Die Methode nextLine der Klasse Scanner liest solange Zeichen aus dem zugehörigen Datenstrom,
        // bis ein Zeilenumbruch gelesen wurde. Die gelesenen Zeichen werden als String-Objekt
        // zurückgegeben.
        String input = scanner.nextLine();
        // Der + Operator hängt Zeichenketten aneinander.
        System.out.println("Hallo " + input.toUpperCase() + "!");
        // Mit String-Methode charAt(index) greift man auf einzelne Zeichen einer Zeichenkette zu.
        System.out.println(input.charAt(0));
        // Die Länge einer Zeichenkette ermittelt man mit der Methode length.
        System.out.println(input.length());
        // Auf das letzte Zeichen greifen wir mit length() - 1 zu.
        System.out.println(input.charAt(input.length() - 1));

        int number = 1;
        double ratio = 3.14;
        byte b = 100;
        short s = 10;

        int[] numbers = {1,2,3,4};
    }
}
