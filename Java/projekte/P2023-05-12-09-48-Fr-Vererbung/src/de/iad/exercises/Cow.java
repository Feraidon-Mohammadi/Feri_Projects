package de.iad.exercises;

public class Cow extends Mammal {

    // Challenge: Überschreibe toString und getOrder. Ordnung ist Paarhufer.

    public Cow(double weight) {
        super(weight); // Aufruf des Konstruktors der Oberklasse (Mammal).
    }

    public Cow() {
        super(0); // Aufruf des Konstruktors der Oberklasse (Mammal).
    }

    @Override
    public String toString() {
        return super.toString() + " -> Cow";
    }

    @Override
    public String getOrder() {
        return "Paarhufer";
    }
}
