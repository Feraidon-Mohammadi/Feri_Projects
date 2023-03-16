// Das ist eine Funktionsdefinition:
// - die Funktion soll greetUser heißen.
// - sie besitzt zwei Parameter
// - der erste Parameter heißt firstName und der zweite lastName
function greetUser(firstName, lastName) {
    console.log(`Hello ${lastName}, ${firstName}!`);
    // console.log("Hello " + lastName + ", " + firstName + "!");
}

function multiply(x, y, z = 1) {
    return x * y * z;
}

function addNumbers() {
    const a = Number(prompt("Erste Zahl eingeben"));
    const b = Number(prompt("Zweite Zahl eingeben"));
    const sum = a + b;
    console.log(`Summe von ${a} und ${b} ist ${sum}`);
}

// Das ist ein Funktionsaufruf:
// - die aufzurufende Funktion heißt greetUser
// - an die Funktion werden die beiden Argumente "Max" und "Mustermann" übergeben.
// - der Parameter firstName erhält den Wert "Max"
// - der Paramter lastName erhält den Wert "Mustermann"
greetUser("Max", "Mustermann");
greetUser("Claire", "Grube");
let product = multiply(2, 4);
//alert(`Produkt ist ${product}`);
console.error(`Produkt ist ${multiply(2, 4, 5)}`);
// Beim Aufruf von Funktionen ohne Parameter ist die Angabe des Call-Operators () trotzdem
// notwendig. Andernfalls würde die JS-Runtime nur das Funktionsobjekt auswerten.
addNumbers();
