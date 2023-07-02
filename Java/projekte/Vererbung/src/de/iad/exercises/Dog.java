package de.iad.exercises;

public class Dog extends Mammal {
    public void bark() {
        System.out.println("wuff wuff");
    }

    @Override
    public String getOrder() {
        return "Raubtiere";
    }
}
