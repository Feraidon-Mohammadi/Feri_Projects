/* Beispiel für Dynamic Dispatch */

class A {
	int x = 11;

	String m() {
		return "I am A";
	}

	static String sm() {
		return "Static sm from A";
	}
}

class B extends A {
	int x = 99;


	String m() {
		return "I am B";
	}

	static String sm() {
		return "Static sm from B";
	}
	
}


public class Test {
	
	public static void main(String[] args) {
		A a = new B();
		System.out.println(a.x); // statically resolved (11 statt 99)
		System.out.println(a.m()); // dynamically resolved ("I am B")
		System.out.println(a.sm()); // statically resolved ("Static sm from A")
	}

}