package de.iad.examples;

import de.iad.erfurt.A;

public class B extends A {

    public void instanzMethode() {
        this.publicFeld = 1;
        this.protectedFeld = 2;
        // this.privateFeld = 3; // Nicht gestattet.
        // this.defaultFeld = 4; // Kein Zugriff außerhalb des Package.


    }

}
