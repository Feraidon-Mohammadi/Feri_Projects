// Ruft man eine Funktion mit weniger Argumenten auf, als die Funktion
// Parameter besitzt, so werden die restlichen Parameter mit undefined initialisiert.
// Man hat jedoch die Möglichkeit Default-Werte für Parameter zu vergeben.
// Falls der Aufrufer keinen Wert für einen Parameter bereitstellt, wird der
// Default-Wert des Parameters verwendet.
function sum(a, b, c = 0) {
    // Die Variable arguments enthält sämtliche an die Funktion übergebene Argumente.
    // Sie wird automatisch von der JavaScript Runtime bereitgestellt.
    // console.log(arguments);
    let s = a + b + c;
    print(s);
    // Die Return-Anweisung gibt einen Wert an den Aufrufer der Funktion zurück.
    // Erreicht die JS-Runtime die return-Anweisung, wird die aktuelle Funktion
    // sofort beendet und die Ausführung geht beim Aufrufer weiter.
    return s;
}

// Gibt eine Funktion keinen expliziten Wert per return-Anweisung zurück,
// ist der Rückgabwert automatisch undefined.
function print(x) {
    console.log(`Value: ${x}`);
}

console.log("Vor Aufruf von sum");
console.log(sum(1, 2, 10));
console.log("Nach Aufruf von sum");
