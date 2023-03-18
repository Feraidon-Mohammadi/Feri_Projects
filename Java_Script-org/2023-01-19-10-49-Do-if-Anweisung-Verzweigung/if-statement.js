const age = Number(prompt("Wie alt sind sie?"));

// Form 1: Nur eine Bedingung mit einem Anweisungsblock.
// Mit dieser Form können Anweisungen optional ausgeführt werden.
// if (age < 18) {
//     alert("Du bist noch nicht volljährig und darfst deshalb diese Seite nicht betreten!");
//     console.log("Anfrage abgewiesen");
// }

// Form 2: Entweder-Oder-Form
// Ist die genannte Bedingung wahr (true) dann wird der erste Block ausgeführt,
// andernfalls der zweite.
// if (age < 18) {
//     alert("Du bist noch nicht volljährig und darfst deshalb diese Seite nicht betreten!");
//     console.error("Anfrage abgewiesen");
// } else {
//     // Wir wissen an dieser Stelle, dass age >= 18 ist.
//     alert("Herzlich willkommen auf unserer Seite. Fühlen sie sich wie zuhause!");
//     console.log("Anfrage angenommen");
// }

// Form 3: Mehrfachauswahl. Hier wird exakt _einer_ der Blöcke ausgeführt.
// Die Bedingungen werden von "oben nach unten" geprüft. Sobald eine Bedingung
// wahr ist, wird der zugehörige Block ausgeführt. Die restlichen Blöcke
// werden übersprungen.
if (age < 18) {
    alert("Du bist noch nicht volljährig und darfst deshalb diese Seite nicht betreten!");
    console.error("Zugang verwehrt");
} else if (age < 30) {
    // Wir wissen hier: age >= 18 und age < 30
    alert("Du bist zwar volljährig, aber noch unter 30. Einige Seiteninhalte bleiben dir deshalb verborgen!");
    console.warn("Zugang teilweise gestattet.");
} else if (age > 60) {
    // Wir wissen hier: age > 60
    alert("Du bist leider zu alt. Diese Seite ist nur für die junge Generation gedacht!");
    console.error("Zugang verweigert");
} else {
    // Wir wissen hier: age >= 30 und age <= 60
    alert("Herzlich willkommen auf unserer Seite. Fühlen sie sich wie zuhause!");
    console.log("Zugang gestattet");
}

// Variante 1
let isAdult;
if (age >= 18) {
    isAdult = true;
} else {
    isAdult = false;
}
console.log("Volljährig:", isAdult);

// Variante 2
// ?: ist ein ternärer Operator, da er 3 Operanden besitzt.
// Der erste Operand wird zu einem Wahrheitswert ausgewertet.
// Meistens ist der erste Operand eine Bedingung.
// Der zweite Operand wird als Ergebnis verwendet, wenn der
// erste Operand wahr gewesen ist.
// Andernfalls wird der dritte Operand als Ergebnis verwendet.
isAdult = age >= 18 ? true : false;
console.log("Volljährig:", isAdult);

// Variante 3
// Ein Vergleichsausdruck liefert immer einen booleschen Wert,
// deshalb brauchen wir keine zusätzliche Fallunterscheidung.
isAdult = age >= 18;
console.log("Volljährig:", isAdult);

// const message =
//     age < 18 ? "Du bist nicht volljährig" : age < 30 ? "Volljährig und unter 30" : age > 60 ? "Zu alt" : "Willkommen";
// alert(message);

console.log("Programmende");
