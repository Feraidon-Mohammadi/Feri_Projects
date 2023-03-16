// Kopfgesteuerte Schleifen prüfen eine Bedingung vor der Ausführung
// ihres Anweisungsblocks (Schleifenrumpf)
// Ist die Bedingung erfüllt, wird der Anweisungsblock (Schleifenrumpf) ausgeführt.
// Andernfalls wird die Schleife beendet.

// Fußgesteuerte Schleifen führen zuerst ihren Anweisungsblock aus und prüfen
// danach ihre Bedingung. Weil die Bedingung erst am Ende geprüft wird,
// wird der Schleifenrumpf mindestens einmal ausgeführt.

let n = 10;
while (n >= 0) {
    console.log(n);
    n -= 1; // n = n - 1
}
while (n <= 10) {
    console.log(n);
    n++; // n = n + 1
}

let inputValid = false;
let userInput = null;
while (!inputValid) {
    // ! ist der NOT-Operator: Er dreht ein Wahrheitsergebnis um.
    userInput = prompt("Gib ja oder nein ein");
    if (userInput === null) {
        console.warn("Eingabe wurde vom Nutzer abgebrochen");
        break; // break verlässt die aktuelle Schleife.
    }
    // === ist der Vergleichsoperator. Er prüft ob zwei Werte denselben Datentyp
    // besitzen und gleich sind.
    // Der OR-Operator prüft, ob mindestens einer seiner Operanden wahr ist.
    inputValid = userInput === "ja" || userInput === "nein";
}
// !== bedeutet "ungleich". Er ist das Pendant zu ===.
// a !== b ist genau dann wahr, wenn a und b unterschiedliche Werte haben
// oder wenn a und b ungleiche Datentypen haben.
if (userInput !== null) {
    console.log(`Ihre Eingabe lautet: ${userInput}`);
}

n = 10;
while (n >= 0) {
    // Ist n gerade, vermindern wir n um eins und beginnen den nächsten Schleifdurchlauf.
    if (n % 2 === 0) {
        n--;
        continue; // continue beendet den aktuellen Schleifendurchlauf und springt
        // zum Kopf bzw. zum Fuß der Schleife, sofern es sich um eine fußgesteuerte
        // Schleife handelt.
    }

    console.log(n);
    n--;
}

// Mit Hilfe von Labels können sowohl innere als auch die dazugehörigen äußeren Schleifen
// vorzeitig mit break beendet werden. Analog lässt sich in Kombination mit continue
// eine innere Schleife beenden und eine äußere Schleife fortsetzen. Siehe folgendes Beispiel:
let i = 0,
    j = 0;
outerLabel: while (i < 3) {
    innerLabel: j = 0;
    while (j < 3) {
        if (i === 1 && j === 1) {
            i++;
            continue outerLabel;
        }
        console.log(`i = ${i}, j = ${j}`);
        j++;
    }
    i++;
}
