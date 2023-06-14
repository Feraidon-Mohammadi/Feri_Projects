package de.iad.programs;

import de.iad.exercises.Cat;
import de.iad.exercises.Cow;
import de.iad.exercises.Dog;
import de.iad.exercises.Mammal;

public class Program {
    public static void main(String[] args) {
        Mammal m = new Mammal();
        Cat alma = new Cat();
        Cat selma = new Cat();
        Dog charlie = new Dog();
        System.out.println(m.toString()); // toString Methode von Mammal
        System.out.println(alma.toString()); // toString Methode von Cat
        System.out.println(selma.toString()); // toString Methode von Cat
        System.out.println(charlie.toString()); // toString Methode von Mammal!!!

        m = charlie; // Upcasting von Dog -> Mammal
        System.out.println(m.toString()); // toString Methode von Mammal, weil wir toString
        // nicht in Klasse Dog überschrieben haben!
        m = selma; // Upcasting von Cat -> Mammal
        System.out.println(m.toString()); // toString Methode von Cat!!!

        // m.meow(); m.purr() nicht möglich, da diese nicht in Mammal definiert sind.
        alma.meow();
        alma.purr();
        // charlie.meow() nicht möglich, da in Dog keine meow Methode definiert ist.
        charlie.bark();
        m = charlie;
        // m.bark(); nicht möglich, da in Mammal keine bark-Methode definiert ist.

        Dog d = (Dog)m; // expliziter Down-Cast Mammal -> Dog
        d.bark(); // Ok, denn in Klasse Dog ist bark Methode definiert.

        // Beispiel für einen Down-Cast, der zur Laufzeit einen Fehler auslöst.
//        m = selma;
//        d = (Dog)m;
//        d.bark();

        // Obwohl die Methode printMammals Mammal-Objekte erwartet, dürfen wir ihr auch
        // Unterklassen-Objekte von Mammal übergeben, da diese Objekte alle Merkmale von
        // Mammal besitzen.
        // Mit anderen Worten: Up-Casting wird auch bei Methodenaufrufen unterstützt.
        Cow milka = new Cow(500.25);
        selma.setWeight(6.0);
        alma.setWeight(6.7);
        charlie.setWeight(45);
        Program.printMammals(m, selma, charlie, alma, milka);
    }

    public static void printMammals(Mammal ...mammals) {
        for (Mammal m : mammals) {
            System.out.println(m.toString() + " Ordnung: " + m.getOrder() + " Gewicht: " + m.getWeight());
        }
    }
}

// Program.main();