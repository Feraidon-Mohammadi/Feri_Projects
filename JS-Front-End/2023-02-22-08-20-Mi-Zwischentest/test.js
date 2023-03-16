// Abschnitt A
// Definiere folgende Variablen
// 1) Variable age mit dem Initalwert 20
// 2) Variable name mit dem Initialwert max mustermann
// 3) Variable vom Typ Array mit den Zahlen 1,2,3
// 4) Variable vom Typ object mit den Properties
//    - name und Initialwert max
//    - age und Initalwert 20
//    - address vom Typ object mit den Properties
//      - street mit Initalwert Maximilian-Welsch-Strasse 2a
//      - city mit Initialwert Erfurt
//      - postalCode und Initialwert 99097

let age = 20;
let name = "max mustermann";
let numbers = [1, 2, 3];
let person = {
  name: "max",
  age: 20,
  address: {
    street: "Maximilian-Welsch-Straße 2a",
    city: "Erfurt",
    postalCode: 99097,
  },
};

// Abschnitt B
// Definiere folgende Funktionen und schreibe für jede Funktion
// einen Beispielaufruf.
// 1) Funktion, die zwei Werte x und y erhält und die Summe zurückliefert.
// 2) Funktion, die einen Array von Zahlen erhält, deren Summe bildet und zurückliefert.
// 3) Funktion, die ein person-Objekt der Form aus Abschnitt A Aufgabe 4 bekommt und folgendes macht:
//    - Ausgabe von name und Adresse auf der Console
//    - Ausgabe einer Zeichenkette der Form: Name ist ?? Jahre alt auf der Console
// 4) Funktion, die einen Array von person-Objekten der Form aus Abschnitt A Aufgabe 4 erhält und
//    einen Array zurückliefert, der nur person-Objekte enthält, deren Property city den Wert "Erfurt" besitzt.
// 5) Eine Arrow-Funktion, die eine Zahl als Parameter erhält, die Zahl verdoppelt und zurückgibt.
// 6) Eine Arrow-Funktion, die keine Parameter besitzt und die Zahl 42 zurückliefert.
// 7) Eine Arrow-Funktion, die zwei Parameter x und y besitzt und beide Parameter auf der Console ausgibt.
//    Hinweis: Die Arrow-Funktion soll mindestens zwei Anweisungen enthalten.
// 8) Eine Arrow-Funktion, die zwei Koordinaten a und b erhält und ein Objekt zurückgibt. Das Objekt
//    besitzt zwei Properties x und y. x soll den Wert von a bekommen und y den Wert von b.

function sum(a, b) {
  return a + b;
}
const result = sum(2, 3);

function sumArray(numbers) {
  let sum = 0;
  // sum = numbers[0] + numbers[1] + ... + numbers[numbers.length - 1];
  for (let index = 0; index < numbers.length; index++) {
    sum += numbers[index];
    // sum = sum + numbers[index];
  }
  return sum;
}

console.log(sumArray([7, 8, 9]));
console.log(sumArray(numbers)); // sumArray([1,2,3]));
console.log(sumArray([7]));
console.log(sumArray([7, 8, 9, 10]));
//sumArray(7,8,9,10); // kein korrekter Aufruf: hier werden 4 Argumente vom Typ number übergeben

function outputPerson(p) {
  console.log(
    `Name: ${p.name}`,
    `Adresse: ${p.address.street} ${p.address.city} ${p.address.postalCode}`
  );
  console.log(`${p.name} ist ${p.age} Jahre alt`);
}

outputPerson(person);
outputPerson({
  name: "Hans",
  age: 30,
  address: {
    street: "Villa Kunterbunt",
    city: "Berlin",
    postalCode: 10100,
  },
});

function getErfurter(personObjects) {
  const erfurter = [];
  for (let index = 0; index < personObjects.length; index++) {
    const person = personObjects[index];
    if (person.address.city === "Erfurt") {
      erfurter.push(person);
    }
  }

  return erfurter;
}

let erfurter = getErfurter([
  person,
  person,
  {
    name: "Maria",
    age: 25,
    address: {
      street: "Villa Kunterbunt",
      city: "Erfurt",
      postalCode: 1234,
    },
  },
]);
console.log(erfurter);

const doubleValue = (a) => a * 2;
console.log(doubleValue(2));

// function doubleValue(a) {
//   return a * 2;
// }

const getNumber = () => 42;
console.log(getNumber());

const outputValues = (x, y) => {
  console.log(x);
  console.log(y);
};

outputValues(3, 4);
outputValues("abc", 3);

// Die runden Klammern um das Objektliteral {x:a, y:b} sind notwendig,
// da der Interpreter ansonsten {} als Deklarationsblock versteht.
const createCoordinate = (a, b) => ({ x: a, y: b });

console.log(createCoordinate(1, 2));
console.log(createCoordinate(0, 1 + 1));

function square(x) {
  return x * x;
}

function pythagoras(a, b) {
  return Math.sqrt(square(a) + square(b));
}

pythagoras(3, 4);

function f(x) {
  console.log("f");
  const s = g(h(x + 1));
  return s;
}

function g(u) {
  console.log("g");
  return 2 * u;
}

function h(a) {
  console.log("h");
  const s = 3 * a;
  return 2 * s;
}

console.log(f(10));
