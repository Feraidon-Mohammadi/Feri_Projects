"use strict";

// Eine Klasse ist ein Bauplan bzw. eine Fabrik für gleichartige Objekte.
// Hinweis: Klassen werden intern auf Konstruktorfunktionen und Prototypen
// abgebildet.
class Person {
    // Definiere ein Property namens species mit dem Startwert "human".
    // Dieses Property wird auf jedem neu erzeugten Objekt gesetzt.
    species = "human";
    // Definiere ein Property namens gender mit dem Startwert undefined.
    // Dieses Property wird auf jedem neu erzeugten Objekt gesetzt.
    gender;
    // Hinweis: species und gender nennt man auch Class Fields. Class Fields werden
    // immer vor der Konstruktorfunktion erzeugt.

    // Die Konstruktorfunktion
    constructor(firstName, lastName, age) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
    }

    // Definiert ein Getter-Property namens fullName.
    // Dieses Property landet in Person.prototype.
    get fullName() {
        return `${this.firstName} ${this.lastName}`;
    }

    // Definiere Methode toString. Diese Methode landet in
    // Person.prototype.
    // Hinweis: Diese Definition überlagert / überschreibt die Definition aus Object.prototype.
    toString() {
        return (
            `${this.constructor.name} [firstName=${this.firstName}, ` +
            `lastName=${this.lastName}, age=${this.age}]`
        );
    }
}
