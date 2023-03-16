let n = 10;
do {
    console.log(n);
    n--;
} while (n >= 0);

function getUserDecision(message) {
    const YES = "ja";
    const NO = "nein";
    // Variablen haben einen Gültigkeitsbereich (Scope).
    // Per let und const definierte Variablen sind innerhalb
    // des Blockes gültig, in dem sie definiert wurden. Das
    // schließt sämtliche geschachtelte Blöcke mit ein.
    let inputValid = false;
    // Variablen, die bei ihrer Definition nicht initialisiert werden,
    // haben automatisch den Wert und Typ undefined.
    let userInput;
    do {
        // Eine Variable innerhalb eines Blockes kann eine Variable des äußeren
        // Blockes "überdecken", wenn sie denselben Namen besitzen. Man nennt
        // das "Shadowing".
        userInput = prompt(message);
        if (userInput === null) {
            // return verlässt die Funktion sofort.
            return false;
        }
        // Entferne führende und nachfolgende Leerzeichen. Wandle
        // alle Großbuchstaben in Kleinbuchstaben um.
        userInput = userInput.trim().toLowerCase();
        inputValid = userInput === YES || userInput === NO;
    } while (!inputValid);

    // Wir geben das Ergebnis des Vergleichs direkt als Funktionswert
    // zurück. Eine if-Anweisung ist hierfür nicht notwendig.
    return userInput === YES;
}
