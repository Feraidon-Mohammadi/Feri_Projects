package de.iad.erfurt;

public class Person {
    public int alter;
    public String name;
    public Person partner;

    public String geschlecht = "unbekannt";

    public static String gattung = "Säugetier";

    public static void main(String[] args) {
        Person feri = new Person();
        feri.alter = 29;
        feri.name = "Feri";
        feri.partner = null;

        Person maria = new Person();
        maria.alter = 25;
        maria.name = "Maria";
        maria.partner = feri;

        // Hier rufen wir die Methode getDescription mit this = feri auf.
        String feriDescription = feri.getDescription();
        // Hier rufen wir die Methode getDescription mit this = maria auf.
        String mariaDescriptionj = maria.getDescription();

        // Hier rufen wir die Methode createMale ohne ein Objekt auf. D.h. es gibt kein this.
        Person norman = Person.createMale("Norman", 18);


    }

    // Eine Instanzmethode hat Zugriff auf die Instanzvariablen eines Objektes, aber auch
    // auf die Klassenfelder (statische Felder / statische Variablen).
    public String getDescription() {
        String description = this.name + " " + " ist " + this.alter + " Jahre alt!";
        description += "Gattung: " + Person.gattung;
        return description;
    }

    // Eine Klassenmethode hat nur Zugriff auf Klassenfelder und andere Klassenmethoden. Innerhalb
    // einer Klassenmethode gibt es keinen Objekt-Kontext. Das Schlüsselwort this existiert nicht.
    // Klassenmethoden können ohne Angabe eines Objektes aufgerufen werden.
    public static Person createMale(String name, int age) {
        Person p = new Person();
        p.partner = null;
        p.name = name;
        p.alter = age;
        p.geschlecht = "männlich";

        return p;
    }
}
