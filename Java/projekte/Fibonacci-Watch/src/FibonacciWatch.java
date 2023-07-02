import java.util.*;

public class FibonacciWatch {

    static final int[] fibonacciNumbers = {1, 1, 2, 3, 5};
    static List<List<Color>> allCombinations;


    public static void main(String[] args) {
        allCombinations = generateCombinations(5, List.of(Color.RED, Color.GREEN, Color.BLUE, Color.WHITE));

        // r, b, g, b, r
        List<Color> combination = List.of( Color.RED, Color.BLUE, Color.GREEN, Color.BLUE, Color.RED );
        // 10:30
        int hours = computeHoursFromCombination(combination);
        int minutes = computeMinutesFromCombination(combination);
        System.out.printf("Uhrzeit: %02d : %02d", hours, minutes);
        System.out.println();

        for (List<Color> aCombination : allCombinations) {
            System.out.println(aCombination);
        }
        System.out.println(allCombinations.size());

//        try (var scanner = new Scanner(System.in)) {
//            System.out.print("Gib Stunden ein: ");
//            int h = Integer.parseInt(scanner.nextLine());
//
//            System.out.print("Gib Minuten ein: ");
//            int m = Integer.parseInt(scanner.nextLine());
//
//            List<Color> foundCombination = findCombinationForTime(h, m);
//            if (foundCombination != null) {
//                System.out.println("Uhrzeit: %02d:%02d Kombination: %s".formatted(h, m, foundCombination));
//            } else {
//                System.out.println("Keine Kombination gefunden");
//            }
//        }

        // Teste, ob es für jede Uhrzeit eine passende Farbkombination gibt.
        for (int h = 0; h <= 12; h++) {
            for (int m = 0; m < 60; m += 5) {
                List<Color> foundCombination = findCombinationForTime(h, m);
                if (foundCombination != null) {
                    System.out.println("Uhrzeit: %02d:%02d Kombination: %s".formatted(h, m, foundCombination));
                } else {
                    System.out.println("Keine Kombination gefunden");
                }
            }
        }
    }

    public static List<Color> findCombinationForTime(int hours, int minutes) {
        // prüfe vorher, ob 0 <= hours <= 12 und 0 <= minutes <= 55, wobei minutes % 5 == 0
        for (List<Color> aCombination : allCombinations) {
            int computedHours = computeHoursFromCombination(aCombination);
            int computedMinutes = computeMinutesFromCombination(aCombination);
            if (hours == computedHours && minutes == computedMinutes) {
                return new ArrayList<>(aCombination);
            }
        }
        return null;
    }

    // Berechnet alle Kombinationen, die mit den vorgegebenen Farben möglich sind. Die Kombinationen
    // enthalten Wiederholungen.
    public static List<List<Color>> generateCombinations(int combinationLength, List<Color> colors) {
        if (combinationLength == 0) {
            return List.of(List.of());
        }

        var partialSolution = generateCombinations(combinationLength - 1, colors);
        var solution = new ArrayList<List<Color>>();

        for (List<Color> smallerCombination : partialSolution) {
            for (Color aColor : colors) {
                List<Color> newCombination = new ArrayList<>(smallerCombination);
                newCombination.add(aColor);
                solution.add(newCombination);
            }
        }

        return solution;
    }

    public static int computeHoursFromCombination(List<Color> combination) {
        int hours = 0;
        for (int i = 0; i < combination.size() && i < fibonacciNumbers.length; ++i) {
            Color color = combination.get(i);
            if (color == Color.RED || color == Color.BLUE) {
                hours += fibonacciNumbers[i];
            }
        }
        return hours;
    }

    public static int computeMinutesFromCombination(List<Color> combination) {
        int minutes = 0;
        for (int i = 0; i < combination.size() && i < fibonacciNumbers.length; ++i) {
            Color color = combination.get(i);
            if (color == Color.GREEN || color == Color.BLUE) {
                minutes += fibonacciNumbers[i];
            }
        }

        return minutes * 5;
    }


}
