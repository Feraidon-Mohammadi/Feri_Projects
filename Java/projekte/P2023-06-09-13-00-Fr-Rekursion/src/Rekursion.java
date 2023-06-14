import java.awt.*;
import java.util.*;
import java.util.List;

public class Rekursion {

    public static void main(String[] args) {
        int[] someNumbers = {9, 2, 10, 1, 5, 3};
        int[] empty = {};
        int[] singleton = {1};
//        System.out.println(findMaximum(someNumbers, 0));
//        System.out.println(sumRecursive2(someNumbers));
//        System.out.println(sumRecursive2(empty));
//        System.out.println(sumRecursive2(singleton));
//        System.out.println(fibonacci(0));
//        System.out.println(fibonacci(1));
//        System.out.println(fibonacci(2));
//        System.out.println(fibonacci(3));
//        System.out.println(fibonacci(4));
//        System.out.println(fibonacci(5));
//        System.out.println(fibonacci(6));
//        System.out.println(fibonacci(7));
//        System.out.println(simpleFibonacci(6));

//        List<Integer> reversed = reverseList2(List.of(9, 8, 7));
//        System.out.println(reversed);
//        System.out.println(factorial(5));
//        System.out.println(greatestCommonDivider(32, 20));
//        System.out.println(greatestCommonDivider(1, 12));
//        System.out.println(greatestCommonDivider(0, 12));
//        System.out.println(greatestCommonDivider(12, 0));
//        System.out.println(greatestCommonDivider(20, 6));
//        System.out.println(greatestCommonDivider(0, 0));

//        List<CoinSelection> selections = coinSelections(16, List.of(Coin.FIVE, Coin.TWO, Coin.TEN));
//        System.out.println(selections);

//        List<List<Integer>> permutations = permutations(List.of(1, 2));
//        System.out.println(permutations.size());
//        System.out.println(permutations);

//        List<List<Integer>> subsets = subsets(List.of(1, 2, 3, 4));
//        List<List<String>> stringSubsets = subsets(List.of("Alice", "Bob", "Charlie"));
//        Comparator<List<?>> sorter = (firstList, secondList) -> firstList.size() - secondList.size();
//        subsets.sort(sorter);
//        System.out.println(subsets);
//        stringSubsets.sort(sorter);
//        System.out.println(stringSubsets);

//        List<List<Integer>> combinations = pay(10, List.of(7, 5, 2, 1));
//        System.out.println(combinations);

        TreeNode root = new TreeNode(1,
            new TreeNode(2,
                    new TreeNode(4,
                            new TreeNode(7),
                            new TreeNode(8)),
                    null),
            new TreeNode(3,
                    new TreeNode(5),
                    new TreeNode(6))
        );

        System.out.println(root.isLeaf());
        System.out.println(root.leftChild.isLeaf());
        root.print();
        System.out.println(root.paths());

    }

    public static int findMaximum(int[] numbers, int indent) {
        if (numbers.length == 0) throw new IllegalArgumentException("Numbers darf nicht leer sein");
        // Trivialfall führt zum Ende der rekursiven Aufrufe.
        String space = " ".repeat(indent);
        System.out.println("%sBerechne Maximum von %s".formatted(space, Arrays.toString(numbers)));
        if (numbers.length == 1) {
            System.out.println("%sProblem ist trivial. Maximum ist %d".formatted(space, numbers[0]));
            return numbers[0];
        }

        // Problem ist zu komplex. Berechne Lösung für weniger komplexes Problem
        int[] partialNumbers = Arrays.copyOfRange(numbers, 1, numbers.length);
        System.out.println("%sProblem ist zu komplex. Berechne Maximum von %s".formatted(space, Arrays.toString(partialNumbers)));
        int maximum = findMaximum(partialNumbers, indent + 2);

        // Berechne komplexe Lösung mit Hilfe der Lösung für das Teilproblem.
        int finalMaximum = numbers[0] > maximum ? numbers[0] : maximum;
        System.out.println("%sMaximum aus Teilproblem ist %d".formatted(space, maximum));
        System.out.println("%sMaximum für komplexeres Problem ist %d".formatted(space, finalMaximum));

        return finalMaximum;
    }

    public static int sum(int[] numbers) {
        int sumOfNumbers = 0;
//        for (int aNumber : numbers) {
//            sumOfNumbers += aNumber;
//        }
        for (int i = 0; i < numbers.length; ++i) {
            sumOfNumbers += numbers[i];
        }

        return sumOfNumbers;
    }

    public static int sumRecursive(int[] numbers) {
        // Trivialfall / Abbruchkriterium
        if (numbers.length == 0) {
            return 0;
        }

        // Kopiere alle Zahlen bis auf die letzte.
        int[] partialNumbers = Arrays.copyOfRange(numbers, 0, numbers.length - 1);
        // Berechne Summe des kürzeren Arrays.
        int partialSum = sumRecursive(partialNumbers);

        // Berechne Summe des gesamte Arrays.
        return numbers[numbers.length - 1] + partialSum;
    }

    public static int sumRecursive2(int[] numbers) {
        if (numbers.length == 0) {
            return 0;
        }
        int middleIndex = numbers.length / 2;
        int[] leftPartition = Arrays.copyOfRange(numbers, 0, middleIndex);
        int[] rightPartition = Arrays.copyOfRange(numbers, middleIndex + 1, numbers.length);
        int leftSum = sumRecursive2(leftPartition);
        int rightSum = sumRecursive2(rightPartition);

        return leftSum + numbers[middleIndex] + rightSum;
    }

    public static int fibonacci(int n) {
        Map<Integer, Integer> results = new HashMap<>();
        results.put(0, 0);
        results.put(1, 1);
        return fibonacci(n, results);
    }

    public static int fibonacci(int n, Map<Integer, Integer> results) {
        System.out.println("Berechne Fib(%d)".formatted(n));
        // Sofern das Ergebnis für n bereits feststeht, führe keine erneute Berechnung durch.
        if (results.containsKey(n)) {
            System.out.println("Fib(%d) wurde bereits berechnet".formatted(n));
            return results.get(n);
        }

        // Berechne Fibonacci-Werte für n-1 und n-2. Trage die erhaltenen Ergebnisse
        // in die Map ein, um redundante Berechnungen einzusparen.
        int previousFibonacci = results.getOrDefault(n - 1, fibonacci(n - 1, results));
        results.put(n - 1, previousFibonacci);
        int secondToLast = results.getOrDefault(n - 2, fibonacci(n - 2, results));
        results.put(n - 2, secondToLast);

        // Berechne aus den Teilergebnissen das Gesamtergebnis und trage es in die Map ein.
        int result = previousFibonacci + secondToLast;
        results.put(n, result);

        return result;
    }

    public static int simpleFibonacci(int n) {
        return simpleFibonacci(n, 0);
    }

    public static int simpleFibonacci(int n, int indent) {
        String space = "-".repeat(indent);
        System.out.println("%sBerechne Fib(%d)".formatted(space, n));
        if (n == 0 || n == 1) {
            return n;
        }
        return simpleFibonacci(n - 1, indent + 2) + simpleFibonacci(n - 2, indent + 2);
    }

    public static List<Integer> reverseList(List<Integer> numbers) {
        if (numbers.isEmpty()) {
            return new ArrayList<>();
        }
        int firstElement = numbers.get(0);
        List<Integer> partialSolution = reverseList(numbers.subList(1, numbers.size()));
        ArrayList<Integer> solution = new ArrayList<>(partialSolution);
        solution.add(firstElement);

        return solution;
    }

    public static List<Integer> reverseList2(List<Integer> numbers) {
        if (numbers.size() < 2) {
            // Erzeuge Kopie von numbers in Form einer ArrayList.
            return new ArrayList<>(numbers);
        }

        List<Integer> partialList = numbers.subList(1, numbers.size() - 1);
        List<Integer> partialSolution = reverseList2(partialList);
        List<Integer> solution = new ArrayList<>(partialSolution);
        solution.add(numbers.get(0));
        solution.add(0, numbers.get(numbers.size() - 1));

        return solution;
    }

    public static int factorial(int number) {
        if (number == 0) {
            return 1;
        }
        return number * factorial(number - 1);
    }

    public static int greatestCommonDivider(int a, int b) {
        if (a == 0 && b == 0) throw new IllegalArgumentException("Mindestens eine Zahl muss ungleich 0 sein");
        if (a == 0) return b;
        if (b == 0) return a;

        // Stelle sicher, dass sich in a die größere der beiden Zahlen befindet.
        if (a < b) {
            int backup = a;
            a = b;
            b = backup;
        }

        int remainder = a % b;
        if (remainder == 0) return b;

        return greatestCommonDivider(b, remainder);
    }

    public static List<List<Integer>> permutations(List<Integer> numbers) {
        // 1. Trivialfälle / Abbruchkriterien definieren.
        if (numbers.isEmpty()) {
            return new ArrayList<>();
        }
        if (numbers.size() == 1) {
            ArrayList<Integer> permutation = new ArrayList<>();
            permutation.add(numbers.get(0));
            return List.of(permutation);
        }

        // 2. Berechne Teillösung für Teilproblem.
        List<Integer> partialList = numbers.subList(1, numbers.size());
        List<List<Integer>> partialSolution = permutations(partialList);

        // 3. Bilde Gesamtlösung mit Hilfe der Teillösungen.
        List<List<Integer>> solution = new ArrayList<>();
        int first = numbers.get(0);
        // Durchlaufe jede Permutation der n-1 Elemente und erzeuge daraus neue Permutationen
        // der Länge n.
        for (List<Integer> partialPermutation : partialSolution) {
            // Die erste Zahl wird an alle gültigen Positionen innerhalb der n-1-Permutation
            // eingefügt. Dadurch entsteht jedes mal eine neue Permutation. Diese neue Permutation
            // muss zur Gesamtlösungsmenge hinzugefügt werden.
            for (int position = 0; position <= partialPermutation.size(); position++) {
                // Erstelle eine Kopie der gerade betrachteten Permutation mit Länge n-1.
                List<Integer> permutation = new ArrayList<>(partialPermutation);
                // Füge Zahl an Position ein.
                permutation.add(position, first);
                // Hänge neu entstandene Permutation an Gesamtergebnismenge an.
                solution.add(permutation);
            }
        }

        return solution;
    }

    public static <E> List<List<E>> subsets(List<E> elements) {
        // Trivialfall / Abbruchkriterium
        if (elements.isEmpty()) {
            return List.of(new ArrayList<>());
        }

        // Bilde Menge aller Elemente bis auf das erste.
        List<E> partialElements = elements.subList(1, elements.size());
        // Berechne alle Teilmengen aus obiger reduzierter Elementmenge.
        List<List<E>> partialSolution = subsets(partialElements);
        // Übernehme alle rekursiv ermittelten Teilmengen in die Gesamtlösung.
        List<List<E>> solution = new ArrayList<>(partialSolution);

        // Ermittle aus den rekursiv ermittelten Teilmengen die Teilmengen mit
        // dem zuvor weggelassenen Element und füge sie zur Gesamtlösung hinzu.
        for (List<E> subset : partialSolution) {
            List<E> newSubset = new ArrayList<>(subset);
            newSubset.add(0, elements.get(0));
            solution.add(newSubset);
        }

        return solution;
    }

    public static List<List<Integer>> pay(int amount, List<Integer> coins) {
        if (amount == 0) {
            List<Integer> zeroCombination = new ArrayList<>();
            for (int coin : coins) zeroCombination.add(0);
            return List.of(zeroCombination);
        }
        if (coins.isEmpty()) {
            return List.of();
        }
        // amount != 0 && coins.size() >= 1
        int coinValue = coins.get(0);
        if (coins.size() == 1) {
            int numberOfCoins = amount / coinValue;
            if (amount % coinValue == 0) {
                return List.of(List.of(numberOfCoins));
            } else {
                return List.of();
            }
        }
        // coins.size() >= 2 && amount != 0
        List<List<Integer>> solution = new ArrayList<>();
        List<Integer> remainingCoins = coins.subList(1, coins.size());
        for (int i = 0; i <= (amount / coinValue); ++i) {
            int remainingAmount = amount - i * coinValue;
            List<List<Integer>> combinationsForRemainingAmount = pay(remainingAmount, remainingCoins);
            for (List<Integer> combination : combinationsForRemainingAmount) {
                List<Integer> newCombination = new ArrayList<>(combination);
                newCombination.add(0, i);
                solution.add(newCombination);
            }
        }

        return solution;
    }





    public static List<CoinSelection> coinSelections(int amount, List<Coin> availableCoins) {
        if (amount == 0) {
            return List.of(CoinSelection.zero());
        }

        if (availableCoins.isEmpty()) {
            return List.of();
        }

        Coin coin = availableCoins.get(0);
        if (availableCoins.size() == 1) {
            if (amount % coin.value() != 0) {
                return List.of();
            }
            return List.of(CoinSelection.zero().add(coin, amount / coin.value()));
        }

        List<CoinSelection> selections = new ArrayList<>();
        List<Coin> remainingCoins = availableCoins.subList(1, availableCoins.size());
        for (int numberOfCoins = 0; numberOfCoins <= (amount / coin.value()); numberOfCoins++) {
            int remaining = amount - numberOfCoins * coin.value();
            List<CoinSelection> partialSelections = coinSelections(remaining, remainingCoins);
            for (CoinSelection partialSelection : partialSelections) {
                selections.add(partialSelection.add(coin, numberOfCoins));
            }
        }

        return selections;
    }

}

enum Coin {

    TEN {
        @Override
        public int value() {
            return 10;
        }
    },
    FIVE {
        @Override
        public int value() {
            return 5;
        }
    },
    TWO {
        @Override
        public int value() {
            return 2;
        }
    },
    ONE {
        @Override
        public int value() {
            return 1;
        }
    };

    public abstract int value();
}

class CoinSelection {

    private final Map<Coin, Integer> amountByCoin = new HashMap<>();

    public CoinSelection() {
        for (Coin coin : Coin.values()) {
            amountByCoin.put(coin, 0);
        }
    }

    public CoinSelection add(Coin coin, int amount) {
        int oldAmount = amountByCoin.get(coin);
        amountByCoin.put(coin, oldAmount + amount);
        return this;
    }

    @Override
    public String toString() {
        StringBuilder builder = new StringBuilder();
        builder.append("[");
        for (Coin coin : amountByCoin.keySet()) {
            builder.append("%s=%d,".formatted(coin.toString(), amountByCoin.get(coin)));
        }
        builder.deleteCharAt(builder.length() - 1);
        builder.append("]");
        return builder.toString();
    }

    public static CoinSelection zero() {
        return new CoinSelection();
    }
}





