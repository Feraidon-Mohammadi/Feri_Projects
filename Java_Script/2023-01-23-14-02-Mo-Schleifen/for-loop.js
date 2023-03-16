// Der Kopf der For-Schleife setzt sich aus drei Komponenten
// zusammen: Initialisierungsblock, Bedingung und Iterationsanweisung.
// Alle Komponenten können leer gelassen werden. Dennoch sind sie stets
// per Semikolons voneinander zu trennen.
// Lässt man die Bedingung weg, gilt automatisch true.
for (let n = 10; n >= 0; n--) {
    console.log(n);
}

function getUserDecision(message) {
    const YES = "ja",
        NO = "nein";

    let userInput;
    
    for (let inputValid = false; !inputValid; ) {
        userInput = prompt(message);
        if (userInput === null) {
            return false;
        }
        userInput = userInput.trim().toLowerCase();
        inputValid = userInput === YES || userInput === NO;
    }

    return userInput === YES;
}
