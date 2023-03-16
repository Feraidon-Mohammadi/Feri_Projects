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
