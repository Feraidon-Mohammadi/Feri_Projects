const names = ["alice", "basti", "bob", "charlie", "damian", "doris", "elon", "jo"];
const numbers = [10, 20, -3, 2, 3, 7, 11];

// Formel: Berechnung des negativen Index: (Länge - positiver-Index) * (-1) bzw. (positiver-Index - Länge)
// Aufgabe 1
//  "basti" hat Index 1, -7
//  "damian" hat Index 4, -4
//  "elon" hat Index 6, -2
// Positiver Index lässt sich auch mittel indexOf ermitteln.

// Aufgabe 3
// let result3 = names.filter((name) => name.length === 3 || name.length === 4);
let result3 = names.filter((name) => [3, 4].includes(name.length));
console.log(result3); // => ["bob", "elon"]

// Aufgabe 4
// Hinweis: -3 % 2 liefert -1, aber 3 % 2 liefert 1
let result4 = numbers.filter((n) => n % 2 !== 0);
console.log(result4); // => [-3, 3, 7, 11]

// Aufgabe 5
//let result5 = numbers.reduce((partialSum, n) => partialSum + n, 0) / numbers.length
let result5 = numbers.reduce((partialSum, n) => partialSum + n) / numbers.length;
console.log(result5); // => 7.142857142857143
// Hinweis: result5.toFixed(4) liefert '7.1429'

// Aufgabe 7
// Hinweis: Das Element "elon" hat den Index 6. Es ist das erste Element, das nicht mehr kopiert werden soll.
let result7 = names.slice(1, 6);
console.log(result7); // => ['basti', 'bob', 'charlie', 'damian', 'doris']

// Aufgabe 8
// Hinweis: Durch slice wird eine Kopie von names erzeugt. Anschließend wird das kopierte Array per splice
// modifiziert.
let result8 = names.slice().splice(1, 3);
console.log(result8); // => ['basti', 'bob', 'charlie']

// Aufgabe 9
let result9 = names.map((name) => name.length);
console.log(result9); // => [5, 5, 3, 7, 6, 5, 4, 2]

// Aufabe 10
let result10 = names.join("  ");
console.log(result10);

// Aufgabe 11
let result11 = names.map((name) => [name, name.length]);
console.log(result11); // => [["alice", 5], ["basti", 5], ["bob", 3], ... ]

function myMap(array, aFunction) {
    const resultArray = [];
    for (const element of array) {
        resultArray.push(aFunction(element));
    }
    return resultArray;
}

// Aufgabe 12
// Hinweis: Die Vergleichsfunktion für sort muss einen negativen Wert zurückliefern,
// wenn der erste Name in der Sortierreihenfolge vor dem zweiten Namen stehen soll.
// Ein positiver Rückgabewert bedeutet, dass der erste Name nach dem zweiten Namen
// im Ergebnis stehen soll. Ergebnis 0 bedeutet, dass beide Namen gleich sind.
let result12 = names.slice().sort((firstName, secondName) => {
    const lastCharOfFirstName = firstName.at(-1);
    const lastCharOfSecondName = secondName.at(-1);
    if (lastCharOfFirstName === lastCharOfSecondName) return 0;
    return lastCharOfFirstName < lastCharOfSecondName ? -1 : 1;
});
console.log(result12); // => ['bob', 'alice', 'charlie', 'basti', 'damian', 'elon', 'jo', 'doris']

// Aufgabe 6
const reverseString = (s) => Array.from(s).reverse().join("");
let result6 = names.map((name, index) => (index % 2 === 0 ? name : reverseString(name).toUpperCase()));
console.log(result6);

// Aufgabe 2
function countCharacter(text, character) {
    return Array.from(text).filter((char) => char === character).length;
}

function countCharacter2(text, character) {
    let count = 0;
    for (let i = 0; i < text.length; ++i) {
        if (text[i] === character) {
            count++;
        }
    }
    return count;
}

let result2 = names.map((name) => countCharacter2(name, "a"));
console.log(names);
console.log(result2); // => [1, 1, 0, 1, 2, 0, 0, 0]

// Die for-of-Schleife durchläuft schrittweise alle Elemente eines Arrays.
// Die Variable value repräsentiert das aktuell in der Schleife betrachtete Element.
// Hinweis: Das Originalelement wird lediglich nach value kopiert.
const sales = [20.14, 200.78, 99, 100];
for (let value of sales) {
    console.log(value);
    value *= 2; // hat keinen Effekt auf das Originalelement
}
// Obige Schleife liese sich auch wie folgt schreiben:
for (let index = 0; index < sales.length; index++) {
    let value = sales[index];
    console.log(value);
    //sales[index] *= 2; // würde Originalelement ändern
}
// sales bleibt unverändert
console.log(sales);

// Alternative zur for-of-Schleife ist die forEach Methode von Arrays
sales.forEach((value, index) => {
    console.log(`Element mit Index ${index} hat Wert ${value}`);
});

// Die Array-Methode entries liefert Wert/Index Paare.
// Damit erhält man gleichzeitig den Index zum Element.
for (const entry of sales.entries()) {
    console.log(`Element mit Index ${entry[0]} hat Wert ${entry[1]}`);
}
