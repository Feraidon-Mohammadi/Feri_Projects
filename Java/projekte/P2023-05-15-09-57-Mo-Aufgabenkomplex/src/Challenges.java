import javax.naming.OperationNotSupportedException;
import java.lang.reflect.Array;
import java.util.Arrays;

public class Challenges {

    // Challenge 1: Schreibe eine Methode, die alle Vokale (a,e,i,o,u) einer Zeichenkette auf der Kommandozeile ausgibt.
    // - Welche Signatur muss die Methode haben?
    // - Wie muss die Methode implementiert werden?

    // Challenge 2: Schreibe eine Methode, die aus einer Zeichenkette alle Duplikate entfernt bzw. nur die Unikate ermittelt.
    // Beispiel: "abac1121" -> "abc12"

    // Challenge 3: Schreibe eine Methode namens zipStrings(String first, String second) die zwei Zeichenketten zeichenweise
    // im Reißverschlussverfahren zusammenfügt. Achtung: first und second dürfen unterschiedlich lang sein!
    // Beispiel: mergeStrings("abcd", "WXYZ") => "aWbXcYdZ"
    // Beispiel: mergeStrings("ab", "WXYZ") => "aWbXYZ"

    // Challenge 4: Prüfe, ob in einem Array mindestens n aufeinanderfolgende Elemente gleich sind. Wir beschränken uns der
    // Einfachheit halber auf Arrays von Integern.
    // - Lege eine Signatur der zu schreibenden Methode fest.
    // - Implementiere die Methode.

    // Challenge 5: Prüfe, ob eine Zeichenkette ein Palindrom ist.

    // Challenge 6: Partitioniere einen Array von Zahlen anhand einer Pivotzahl. Die Methode darf nur Vertauschungen innerhalb
    // des Arrays nutzen. Es dürfen keine zusätzlichen Arrays verwendet werden.
    // Beispiel: 3,7,5,2,9,1,0,4 mit Pivotelement 5 =>  3, 2, 1, 0, 4, _5_, 7, 9


    public static void main(String[] args) {
        Challenges.printVowels("abcdefg");
        System.out.println();
        Challenges.printVowels("feri");
        System.out.println();
        Challenges.printVowels("Java ist toll!");
        System.out.println();
        String unique = Challenges.removeDuplicates("Hallo aus Entenhausen!");
        System.out.println(unique);
        System.out.println(Challenges.zipStrings("abc", "12345"));
        System.out.println(Challenges.zipStrings("12345", "abc"));
        int[] numbers = {1, 2, 1, 1, 1, 3, 3, 4, 4, 4, 4, 4, 5};
        System.out.println(Challenges.containsEqualValues(numbers, 0));
        System.out.println(Challenges.containsEqualValues(new int[]{}, 0));
        System.out.println(Challenges.containsEqualValues(numbers, 1));
        System.out.println(Challenges.containsEqualValues(new int[]{4}, 1));
        System.out.println(Challenges.containsEqualValues(numbers, 2));
        System.out.println(Challenges.containsEqualValues(numbers, 3));
        System.out.println(Challenges.containsEqualValues(numbers, 4));
        System.out.println(Challenges.containsEqualValues(numbers, 5));
        System.out.println(Challenges.containsEqualValues(numbers, 6));
        System.out.println();
        System.out.println(Challenges.isPalindrom2("RENTNER"));
        System.out.println(Challenges.isPalindrom2("R"));
        System.out.println(Challenges.isPalindrom2("OTTO"));
        System.out.println(Challenges.isPalindrom2("Feri"));

        numbers = new int[]{5, 2, 3, 7, 1};
        partition(numbers, 2);
        System.out.println(Arrays.toString(numbers));
        numbers = new int[]{5, 2, 3, 7, 1};
        partition(numbers, 0);
        System.out.println(Arrays.toString(numbers));
        numbers = new int[]{5, 2, 3, 7, 1};
        partition(numbers, 4);
        System.out.println(Arrays.toString(numbers));
        numbers = new int[]{5, 2, 3, 7, 1};
        partition(numbers, 3);
        System.out.println(Arrays.toString(numbers));

        numbers = new int[]{5, 2, 3, 7, 1};
        quickSort(numbers, 0);
        System.out.println(Arrays.toString(numbers));

        numbers = new int[]{5, 6, 7, 4, 1, 3};
        int[] partialNumbers = Challenges.createCopy(numbers, 2, 4);
        System.out.println(Arrays.toString(partialNumbers));
        partialNumbers = Challenges.createCopy(numbers, 5, 1);
        System.out.println(Arrays.toString(partialNumbers));

        int[] destination = new int[10];
        System.out.println(Arrays.toString(destination));
        Challenges.copyTo(numbers, destination, 1, 3);
        System.out.println(Arrays.toString(destination));

        numbers = new int[] { 9, 1, 6, 0, 10, 4, 5, 3, 0, 1, 12, 99, 44, 33, 7 };
        System.out.println(Arrays.toString(numbers));
        quickSort(numbers, 0);
        System.out.println(Arrays.toString(numbers));

        numbers = new int[]{5, 2, 10, 1, 0, 7, 13};
//        numbers = new int[]{};
//        numbers = new int[]{1};
        Challenges.maxSort(numbers);
        System.out.println(Arrays.toString(numbers));

        numbers = new int[]{7, 9, 1, 6, 8};
        Challenges.bubbleSort(numbers, false);
        System.out.println(Arrays.toString(numbers));


    }

    public static void printVowels(String s) {
        int position = 0;
        while (position < s.length()) {
            char z = s.charAt(position);
            if (z == 'a' || z == 'e' || z == 'i' || z == 'o' || z == 'u') {
                System.out.print(z);
            }
            position++;
        }
    }

    // Diese Überladung dient einzig dem Zweck einen Default-Wert für den Parameter ignoreCase
    // zu definieren. Java erlaubt leider keine direkten Default-Werte für Methodenparameter.
    public static String removeDuplicates(String input) {
        return Challenges.removeDuplicates(input, false);
    }

    public static String removeDuplicates(String input, boolean ignoreCase) {
        StringBuilder uniqueCharacters = new StringBuilder();

        for (char inputCharacter : input.toCharArray()) {
            boolean found = false;
            // Prüfe, ob das Zeichen schon mal aufgetreten ist.
            for (int i = 0; i < uniqueCharacters.length(); ++i) {
                char unique = uniqueCharacters.charAt(i);
                // Vergleiche die Buchstaben anhand ihrer Kleinbuchstaben, wenn ignoreCase true ist. Andernfalls vergleiche
                // die Buchstaben direkt und berücksichtige ihre Groß und Kleinschreibung.
                boolean areEqual = ignoreCase
                        ? Character.toLowerCase(unique) == Character.toLowerCase(inputCharacter)
                        : unique == inputCharacter;
                if (areEqual) {
                    found = true;
                    break;
                }
            }
            // Füge das Zeichen zur Liste der Unikate hinzu, wenn es bisher noch nicht aufgetreten ist.
            if (!found) {
                uniqueCharacters.append(inputCharacter);
            }
        }

        return uniqueCharacters.toString();
    }

    public static String zipStrings(String first, String second) {
        StringBuilder result = new StringBuilder();
        // Ermittle das Maximum der Längen von first und second.
        int maxLength = first.length() > second.length() ? first.length() : second.length();

        for (int i = 0; i < maxLength; ++i) {
            if (i < first.length()) {
                result.append(first.charAt(i));
            }
            if (i < second.length()) {
                result.append(second.charAt(i));
            }
        }

        return result.toString();
    }

    // Prüft, ob in values mindestens n aufeinanderfolgende gleiche Werte enthalten sind.
    public static boolean containsEqualValues(int[] values, int n) {
        // Spezialfälle
        if (n <= 0) return true;
        if (values.length == 0) return false;
        if (n == 1) return true;

        // Hier gilt: n >= 2, values.length >= 1
        int count = 1;
        int current = values[0];

        for (int i = 1; i < values.length; ++i) {
            int next = values[i];
            if (next == current) {
                count++;
                if (count == n) return true;
            } else {
                count = 1;
                current = next;
            }
        }

        return false;
    }

    public static boolean isPalindrom(String s) {
        for (int i = 0, j = s.length() - 1; i < j; i++, j--) {
            if (s.charAt(i) != s.charAt(j)) return false;
        }
        return true;
    }

    public static boolean isPalindrom2(String s) {
        StringBuilder builder = new StringBuilder(s);
        builder.reverse();
        return builder.toString().equals(s);
    }

    // Vertausche die Zahlen an den Positionen a und b miteinander.
    public static void swap(int[] numbers, int a, int b) {
        // Wir müssen die Zahl an Position a in einer Variable zwischenspeichern,
        // da wir im nächsten Schritt die Zahl an Position b damit überschreiben.
        int backup = numbers[a];
        numbers[a] = numbers[b];
        numbers[b] = backup;
    }

    // Paritioniere den Zahlen-Array und gib die neue Position des Pivotelementes
    // zurück.
    public static int partition(int[] numbers, int pivotIndex) {
        // Wenn wir höchstens eine Zahl im Array haben, ist eine Partition unnötig.
        if (numbers.length <= 1) return 0;

        // Bringe Pivotelement an die erste Stelle im Array.
        int pivot = numbers[pivotIndex];
        Challenges.swap(numbers, 0, pivotIndex);

        int indexOfLastSmallerNumber = 0;
        for (int position = 1; position < numbers.length; position++) {
            if (numbers[position] <= pivot) {
                indexOfLastSmallerNumber++;
                Challenges.swap(numbers, indexOfLastSmallerNumber, position);
            }
        }

        // Tausche Pivotelement an korrekte Position zurück.
        Challenges.swap(numbers, 0, indexOfLastSmallerNumber);
        return indexOfLastSmallerNumber;
    }

    public static void quickSort(int[] numbers, int indentation) {
        String space = " ".repeat(indentation);
        System.out.println(space + "Sortiere " + Arrays.toString(numbers));
        // Haben wir maximal 1 Element im Array, gibt es nichts zu sortieren.
        if (numbers.length <= 1) {
            System.out.println(space + "Keine Sortierung erforderlich da maximal ein Element.");
            return;
        }
        // Das Element, das in der "Mitte" des Arrays steht, wird zum Pivotelement.
        int oldPivotIndex = numbers.length / 2;
        // Partitioniere das Array anhand des gewählten Pivotelements.
        // Durch die Partitionierung erhält das Pivotelement eventuell eine neue
        // Position im Array.
        int newPivotIndex = Challenges.partition(numbers, oldPivotIndex);
        // Erstelle eine Kopie der linken Partition. Es kann vorkommen, dass die linke Partition leer ist.
        int[] leftPartition = newPivotIndex > 0
                ? Challenges.createCopy(numbers, 0, newPivotIndex - 1)
                : new int[]{};
        // Erstelle eine Kopie der rechten Partition. Es kann passieren, dass die rechte Partition leer ist.
        int[] rightPartition = newPivotIndex < numbers.length - 1
                ? Challenges.createCopy(numbers, newPivotIndex + 1, numbers.length - 1)
                : new int[]{};
        System.out.println(space + "Nach Partitionierung: %s %d %s".formatted(
                Arrays.toString(leftPartition), numbers[newPivotIndex], Arrays.toString(rightPartition)
        ));
        // Sortiere linke und rechte Partition.
        quickSort(leftPartition, indentation + 2);
        quickSort(rightPartition, indentation + 2);
        // Erzeuge aus dem Pivotelement und den sortierten Partitionen das sortierte Array.
        System.out.println(space + "Zusammenfügen von %s %d %s".formatted(
                Arrays.toString(leftPartition), numbers[newPivotIndex], Arrays.toString(rightPartition)
        ));
        if (leftPartition.length > 0) {
            Challenges.copyTo(leftPartition, numbers, 0, leftPartition.length);
        }
        if (rightPartition.length > 0) {
            Challenges.copyTo(rightPartition, numbers, newPivotIndex + 1, rightPartition.length);
        }
    }

    // Challenge: Erzeuge ein neues Array, das aus den Zahlen an den Positionen
    // startIndex, startIndex + 1, ..., endIndex im Array numbers besteht.
    public static int[] createCopy(int[] numbers, int startIndex, int endIndex) {
        // Stelle sicher, dass die Parameter startIndex und endIndex gültige Indizes sind.
        if (startIndex < 0 || startIndex >= numbers.length) {
            throw new IndexOutOfBoundsException("StartIndex %d ist ungültig".formatted(startIndex));
        }
        if (endIndex < 0 || endIndex >= numbers.length) {
            throw new IndexOutOfBoundsException("EndIndex %d ist ungültig".formatted(endIndex));
        }
        // 0. Falls endIndex < startIndex sein sollte, vertausche endIndex mit startIndex.
        if (endIndex < startIndex) {
            // 0a. Sichere den Wert von startIndex in einer backup-Variablen.
            int backup = startIndex;
            // 0b Kopiere Wert von endIndex in Variable startIndex.
            startIndex = endIndex;
            // 0c Kopiere Wert von backup (ursprünglich startIndex) in Variable endIndex.
            endIndex = backup;
        }
        // 1. Länge des neuen Arrays berechnen.
        int lengthOfNewArray = endIndex - startIndex + 1;
        // 2. Neues Array erzeugen.
        int[] newArray = new int[lengthOfNewArray];
        // 3. Zahlen von numbers kopieren.
        for (int i = startIndex; i <= endIndex; i++) {
            // 3a Ermittle Zahl an Position i.
            int number = numbers[i];
            // 3b Kopiere Zahl an Position i - startIndex in das neue Array.
            newArray[i - startIndex] = number;
        }
        // 4. Neues Array an den Aufrufer der Methode zurückgeben.
        return newArray;
    }

    // Challenge: Implementiere folgende Methode: Die Zahlen von source sollen in den Array destination kopiert werden,
    // und zwar beginnend an Zielposition startIndex. Es dürfen maximal numberOfElementsToCopy Zahlen kopiert werden.
    public static void copyTo(int[] source, int[] destination, int startIndex, int numberOfElementsToCopy) {
        // Prüfe, ob der StartIndex gültig ist.
        if (startIndex < 0 || startIndex >= destination.length) {
            throw new IndexOutOfBoundsException("Startindex %d ist ungültig".formatted(startIndex));
        }
        // Prüfe, ob destination-Array groß genug ist, um die Elemente aus dem source-Array aufzunehmen.
        int endIndex = startIndex + numberOfElementsToCopy - 1;
        if (endIndex >= destination.length) {
            throw new IndexOutOfBoundsException("Endindex %d ist ungültig".formatted(endIndex));
        }
        // Prüfe, ob der Source-Array genug Elemente bereithält.
        if (source.length < numberOfElementsToCopy) {
            throw new IllegalArgumentException("Source-Array hat unzureichende Länge");
        }

        // Kopiere die Elemente aus source (beginnend an Position 0) nach destination (beginnend an Position startIndex)
        for (int sourceIndex = 0; sourceIndex < numberOfElementsToCopy; ++sourceIndex) {
            int destinationIndex = startIndex + sourceIndex;
            destination[destinationIndex] = source[sourceIndex];
        }

    }

    public static void maxSort(int[] numbers) {

        for (int upperBound = numbers.length - 1; upperBound >= 1; upperBound--) {
            int indexOfMaximum = 0;
            // Finde die Position des Maximums im Teilbereich [0..upperBound].
            for (int position = 1; position <= upperBound; position++) {
                if (numbers[position] > numbers[indexOfMaximum]) {
                    indexOfMaximum = position;
                }
            }
            // Bringe das Maximum an das Ende des Teilbereichs [0..upperBound] durch Vertauschen.
            int backup = numbers[upperBound];
            numbers[upperBound] = numbers[indexOfMaximum];
            numbers[indexOfMaximum] = backup;
        }

    }

    public static void bubbleSort(int[] numbers, boolean sortInAscendingOrder) {
        int upperBound = numbers.length - 1; // größtmöglicher Index
        while (upperBound >= 1) {
            // Bringe das Maximum an die Position upperBound.
            for (int position = 0; position < upperBound; position++) {
                int currentNumber = numbers[position];
                int successor = numbers[position + 1];
                if ((sortInAscendingOrder && currentNumber > successor)
                    || (!sortInAscendingOrder && currentNumber < successor)) {
                    numbers[position] = successor;
                    numbers[position + 1] = currentNumber;
                }
            }
            upperBound--;
        }
    }



}
