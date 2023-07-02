package pa;

import pc.C;

public class B extends A {

    public int publicFieldOfB;
    protected int protectedFieldOfB;
    int packageFieldOfB;
    private int privateFieldOfB;

    void methodOfB() {
        this.publicFieldOfB = 0;
        this.protectedFieldOfB = 0;
        this.packageFieldOfB = 0;
        this.privateFieldOfB = 0;

        this.publicFieldOfA = 0;
        this.protectedFieldOfA = 0;
        this.packageFieldOfA = 0;
        // this.privateFieldOfA = 0;
    }

    void methodOfB(A a) {
        a.publicFieldOfA = 0;
        a.protectedFieldOfA = 0;
        a.packageFieldOfA = 0;
        //a.privateFieldOfA = 0;
    }

    void methodOfB(B b) {
        b.publicFieldOfA = 0;
        b.protectedFieldOfA = 0;
        b.packageFieldOfA = 0;
        // b.privateFieldOfA = 0;

        b.publicFieldOfB = 0;
        b.protectedFieldOfB = 0;
        b.packageFieldOfB = 0;
        b.privateFieldOfB = 0;

    }

    void methodOfB(C c) {
        c.publicFieldOfA = 0;
        c.protectedFieldOfA = 0;
        // c.packageFieldOfA = 0;
        // c.privateFieldOfA = 0;

        c.publicFieldOfC = 0;
        // c.protectedFieldOfC = 0;
        // c.packageFieldOfC = 0;
        // c.privateFieldOfC = 0;
    }
}
