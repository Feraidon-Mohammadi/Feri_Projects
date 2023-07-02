interface I1 {
	default int m() { return 1; }
	static int ms() { return 111; }
}

interface I2 {
	default int m() { return 2; }
	static int ms() { return 222; }	
}

public class C implements I1, I2 {

	public static void main(String[] args) {
		C c = new C();
		System.out.println(c.m());

	}

	public int m() {
		return I1.super.m();
//		return I2.ms();
	}

}
