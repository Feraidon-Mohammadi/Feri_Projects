package other;

import certification.Parent;

class Child extends Parent {

	public void testIt() {
		// Access through inheritance
		//System.out.println("x is " + this.x); // OK
		
		// Access through an instance of the super class
		//Parent p = new Parent();
		//System.out.println("p.x is " + p.x); // Error

	}

}

enum Animals {
	DOG("woof"), CAT("meow"), FISH("burble");
	String sound;
	
	Animals(String s) {
		sound = s;
	}
}

public class TestEnum {
	static Animals a;

	public static void main(String[] args) {
		System.out.println(a);
		System.out.println(Animals.DOG.sound + Animals.FISH.sound);
	}
	
}

