package de.iad.exercises;
public class Mammal extends java.lang.Object {

    private double weight;

    public Mammal(double weight) {
        this.weight = weight;
    }

    public Mammal() {
        this.weight = 0;
    }

    @Override
    public String toString() {
        // Rufe Methode toString der Elternklasse (Java: Superklasse) auf.
        // Hole dir das Ergebnis und hänge eine weitere Zeichenkette an.
        String result = super.toString() + " Mammal";
        return result;
    }

    public String getOrder() {
        return "None";
    }

    public double getWeight() {
        return this.weight;
    }

    public void setWeight(double weight) {
        this.weight = weight;
    }
}
