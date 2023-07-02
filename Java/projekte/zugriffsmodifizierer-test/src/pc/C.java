package pc;

import pa.A;
import pa.B;

public class C extends A {

    public int publicFieldOfC;
    protected int protectedFieldOfC;
    int packageFieldOfC;
    private int privateFieldOfC;

    @Override
    public Integer protectedMethod(Integer integer) {
        return 0;
    }

    void methodOfC() {
        this.publicFieldOfA = 0;
        this.protectedFieldOfA = 0;
        //this.packageFieldOfA = 0;
        //this.privateFieldOfA = 0;

        this.publicFieldOfC = 0;
        this.protectedFieldOfC = 0;
        this.packageFieldOfC = 0;
        this.privateFieldOfC = 0;
    }

    void methodOfC(A a) {
        a.publicFieldOfA = 0;
        // a.protectedFieldOfA = 0;
        // a.packageFieldOfA = 0;
        // a.privateFieldOfA = 0;
    }

    void methodOfB(B b) {
        b.publicFieldOfA = 0;
        // b.protectedFieldOfA = 0;
        // b.packageFieldOfA = 0;
        // b.privateFieldOfA = 0;

        b.publicFieldOfB = 0;
        // b.protectedFieldOfB = 0;
        // b.packageFieldOfB = 0;
        // b.privateFieldOfB = 0;
    }

    void methodOfB(C c) {
        c.publicFieldOfC = 0;
        c.protectedFieldOfC = 0;
        c.packageFieldOfC = 0;
        c.privateFieldOfC = 0;

        c.publicFieldOfA = 0;
        c.protectedFieldOfA = 0;
        // c.packageFieldOfA = 0;
        // c.privateFieldOfA = 0;
    }
}
