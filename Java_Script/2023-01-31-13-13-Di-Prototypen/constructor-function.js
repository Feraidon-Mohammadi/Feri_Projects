"use strict";

// Eine Konstruktorfunktion dient zum Erzeugen gleichartiger Objekte.
// Gleichartig bedeutet, dass die erzeugten Objekte die gleichen
// Properties besitzen, also dieselbe Struktur haben.
function Person(firstName, lastName, age) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.age = age;
}

// Das Objekt Person.prototype wird als Prototyp aller von Person
// erzeugten Objekte gesetzt. Dadurch stehen die Properties von
// Person.prototype allen Person-Objekten zur Verfügung.
Person.prototype.getFullName = function () {
    return `${this.firstName} ${this.lastName}`;
};

// Füge ein Getter-Property namens fullName zum Objekt Person.prototype hinzu.
// Das dritte Argument ist ein Accessor/Data Descriptor, der das zu erzeugende
// Property beschreibt. Man spricht von einem Accessor-Descriptor, wenn es
// sich um ein Getter/Setter Property handelt. Man spricht von einem Data Descriptor,
// wenn es sich bei dem Property um ein Property mit einem vordefinierten Wert handelt.
Object.defineProperty(Person.prototype, "fullName", {
    get() {
        return `${this.firstName} ${this.lastName}`;
    },
    enumerable: true,
    configurable: false,
});

// Objekte mit Hilfe der Konstruktorfunktion Person erzeugen.
// Hinweis: Die Verwendung des new-Operators ist notwendig. Der
// Operator erzeugt ein neues, leeres Objekt und übergibt dieses
// an die Konstruktorfunktion Person. Die Konstruktorfunktion
// fügt dann die Properties zum Objekt hinzu
// Der new-Operator setzt den Prototypen des neu erzeugten Objektes
// auf das Objekt Person.prototype.
const max = new Person("Max", "Mustermann", 20);
const alice = new Person("Alice", "Wonderland", 30);
const robin = new Person("Robin", "Hood", 50);

console.log(max.getFullName()); // => Max Mustermann
console.log(alice.getFullName()); // => Alice Wonderland
console.log(robin.getFullName()); // => Robin Hood

// Wir nutzen obiges Konzept aus, um den Datentyp String um eine
// zusätzliche Methode zu erweitern. Hinweis: Zeichenketten haben
// als Prototyp ein Objekt, das per String.prototype referenziert werden kann.
String.prototype.reverse = function () {
    // Wandle string in Array um, reverse den Array und joine zum Schluss
    // seine Elemente.
    return this.split("").reverse().join("");
};

// Nun können wir die neu hinzugefügte Methode mit allen String-Objekten
// verwenden.
console.log("Robin".reverse()); // => niboR
