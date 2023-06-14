package de.iad.programs;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Scanner;

public class PersonalPlanner {

    // throws FileNotFoundException sagt dem Compiler, dass der Aufrufer der main-Methode für die
    // Behandlung einer FileNotFoundException verantwortlich ist. Dies ist erforderlich, da FileNotFoundException
    // eine Ausnhame ist, die im Programm abgefangen werden muss. (checked exception)
    public static void main(String[] args) throws FileNotFoundException, IOException {
        String workingDirectory = System.getProperty("user.dir");
        System.out.println("Arbeitsverzeichnis: %s".formatted(workingDirectory));


        // Aus dem aktuellen Arbeitsverzeichnis und dem relativen Pfad data\personal.txt
        // wird der absolute Pfad von personal.txt gebildet.
        FileInputStream stream = new FileInputStream("data\\personal.txt");

        Scanner scanner = new Scanner(stream, "UTF-8");
        int lineNumber = 0;
        while (scanner.hasNextLine()) {
            lineNumber++;
            String line = scanner.nextLine();
            System.out.println("%02d: %s".formatted(lineNumber, line));
        }

        // Der Scanner schließt den InputStream automatisch mit.
        scanner.close();
        //stream.close();


    }
}
