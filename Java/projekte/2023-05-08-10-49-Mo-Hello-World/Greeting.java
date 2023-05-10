import java.util.Scanner; // importiere die Klasse java.util.Scanner
import java.io.PrintStream;

public class Greeting {
	
	public static void main(String[] arguments) {
			PrintStream out = new PrintStream(System.out, true, "cp850");
			System.setOut(out);
		
			Scanner scanner = new Scanner(System.in);
			String input = scanner.nextLine();
			System.out.printf("Hallo %s!%n", input);
		
	}
	
	
}