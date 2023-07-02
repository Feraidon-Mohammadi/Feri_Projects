import java.util.List;

public class Loops {

    public static void main(String[] args) {
//        countToTen();
//        printEvenNumbers();
//        printEvenNumbers(-8, 10);
//        System.out.println(sum());
//        printInReverse("Java ist mega cool!");
//        System.out.println(factorial(20));
//        System.out.println(countVowels("Java ist COOL!"));
//        fibonacci(1);
//        fibonacci(2);
//        fibonacci(3);
//        fibonacci(4);
//        fibonacci(5);
//        fibonacci(6);
//        fibonacci(7);
//        fibonacci(8);
//        sum(List.of(1, 2, 3, 4, 5, 6, 7, 8));
//        printTable2(2, 6);
        printMultiplicationTable();
    }







    public static void countToTen() {
        for (int i = 1; i <= 10; i++) {
            System.out.println(i);
        }
    }

    public static void printEvenNumbers() {
        for (int i = 2; i <= 20; i += 2) {
            System.out.println(i);
        }
    }

    public static void printEvenNumbers(int minimum, int maximum) {
        if (minimum % 2 != 0) throw new RuntimeException("Minimum muss gerade sein!");
        for (int i = minimum; i <= maximum; i += 2) {
            System.out.println(i);
        }
    }

    public static int sum() {
        int sum = 0;
        for (int i = 1; i <= 100; i++) {
            sum += i;
        }
        return sum;
    }

    public static void printInReverse(String s) {
        for (int i = s.length() - 1; i >= 0; i--) {
            System.out.print(s.charAt(i));
        }
    }

    public static int factorial(int n) {
        if (n < 0) throw new RuntimeException("n darf nicht negativ sein!");
        // n! = 1 * 2 * ... * (n-1) * n
        int product = 1;
        for (int i = 2; i <= n; i++) {
            product *= i;
        }
        return product;
    }

    public static int countVowels(String s) {
        final String vowels = "aeiou";
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            // Hole Zeichen an Position i im String s und wandle es ggf. in einen Kleinbuchstaben um.
            char c = Character.toLowerCase(s.charAt(i));
            // Suche Zeichen c im String vowels. Wurde c gefunden, erhöhen wir count und beenden die Schleife vorzeitig
            // mit der Anweisung break.
            for (int j = 0; j < vowels.length(); j++) {
                if (vowels.charAt(j) == c) {
                    count++;
                    break;
                }
            }
        }
        return count;
    }

    public static void fibonacci(int count) {
        int a = 1, b = 1; // entspricht int a = 1; int b = 1;
        for (int i = 0; i < count; i++) {
            System.out.print("%d%s".formatted(a, i == count - 1 ? "" : ", "));
            int sum = a + b;
            a = b;
            b = sum;
        }
        if (count > 0) {
            System.out.println();
        }
    }

    public static int sum(List<Integer> numbers) {
        int sum = 0;
        for (int i = 0; i < numbers.size(); i++) {
            int number = numbers.get(i);
            sum += number;
            System.out.print("%d%s".formatted(number, i+1 == numbers.size() ? "" : ", "));
        }
        System.out.println();
        System.out.println("Summe: %d".formatted(sum));
        return sum;
    }

    public static void printTable() {
        for (int n = 1; n <= 12; n++) {
            System.out.print("%02d ".formatted(n));
            if (n % 4 == 0) {
                System.out.println();
            }
        }

        int n = 1;
        for (int row = 1; row <= 3; row++) {
            for (int column = 1; column <= 4; column++) {
                System.out.print("%02d ".formatted(n));
                n++;
            }
            System.out.println();
        }
    }

    public static void printTable2(int rows, int columns) {
        for (int i = 1; i <= rows; i++) {
            for (int j = 0; j < columns; j++) {
                System.out.print("%4d ".formatted(i + j * rows));
            }
            System.out.println();
        }
    }

    public static void printMultiplicationTable() {
        for (int row = 1; row <= 10; row++) {
            for (int column = 1; column <= 10; column++) {
                System.out.print("%4d ".formatted(row * column));
            }
            System.out.println();
        }
    }



}
