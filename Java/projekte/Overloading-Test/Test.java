class Test {

	void m(int a, int b) { System.out.println("m(int,int)"); }
	void m(int a, long b) { System.out.println("m(int,long)"); }

	public static void main(String[] args) {
		Test t = new Test();
		t.m(2,3); 	  // wählt m(int, int) statt m(int, long)
		t.m(2,3L); 	  // wählt m(int, long)
		t.m(2, (short)3); // wählt m(int, int)
	}

}