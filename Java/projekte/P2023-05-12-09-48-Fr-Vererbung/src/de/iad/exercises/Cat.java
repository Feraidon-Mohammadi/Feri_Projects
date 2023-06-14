package de.iad.exercises;

public class Cat extends Mammal {

    public void meow() {
        System.out.println("Miauuuuu");
    }

    public void purr() {
        System.out.println("Schnurrrrrrr");
    }

    @Override
    public String getOrder() {
        return "Raubtiere";
    }

    @Override
    public String toString() {
        String result = super.toString() + " -> Cat";
        return result;
    }
}
