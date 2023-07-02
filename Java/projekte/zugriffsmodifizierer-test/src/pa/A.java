package pa;

import pc.C;

public class A {

    public int publicFieldOfA;
    protected int protectedFieldOfA;
    int packageFieldOfA;
    private int privateFieldOfA;

    protected Number protectedMethod(Integer integer) {
        return 0;
    }

    public void methodOfA(A a) {
        a.publicFieldOfA = 0;
        a.protectedFieldOfA = 0;
        a.packageFieldOfA = 0;
        a.privateFieldOfA = 0;
    }

    public void methodOfA(B b) {
        b.publicFieldOfA = 0;
        b.protectedFieldOfA = 0;
        b.packageFieldOfA = 0;
        //b.privateFieldOfA = 0;

        b.publicFieldOfB = 0;
        b.protectedFieldOfB = 0;
        b.packageFieldOfB = 0;
        //b.privateField2 = 0;
    }

    public void methodOfA(C c) {
        c.publicFieldOfA = 0;
        c.protectedFieldOfA = 0;
        // c.packageFieldOfA = 0;
        // c.privateFieldOfA = 0;

        c.publicFieldOfC = 0;
        //c.protectedFieldOfC = 0;
        //c.packageFieldOfC = 0;
        //c.privateFieldOfC = 0;

    }
}




