class A {

	int x;

	A(int x) { }

	public static void main(String[] args) {
//		x = 2;
		A a = new A(2);
		a.x = 2;

	}

}

class Base {
	int f;
	static int g;
}

class Derived extends Base {
	Derived() {
		super();
		this.f = 2;
		Base.g = 3;
		g = 4;
	}
}
	


class B extends A {
	B() { 
		super(2);
	}
}

class C {

	C() {
		//this("Fred");
	}

	C(String s) {
		this();
	}

}

abstract interface I { }
