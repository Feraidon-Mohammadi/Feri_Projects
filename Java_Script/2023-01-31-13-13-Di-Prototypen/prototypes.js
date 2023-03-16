"use strict";

const personPrototype = {
    get fullName() {
        return `${this.firstName} ${this.lastName}`;
    },
};

const max = {
    firstName: "Max",
    lastName: "Mustermann",
    age: 20,
};

const wilma = {
    firstName: "Wilma",
    lastName: "Rein",
    age: 30,
};

// Weder max noch sein Prototyp haben das Property fullName.
// Daher ist das Ergebnis undefined.
console.log(max.fullName); // => undefined

// Weise den Objekten max und wilma einen neuen Prototyp zu.
Object.setPrototypeOf(max, personPrototype);
Object.setPrototypeOf(wilma, personPrototype);

// Der Zugriff auf fullName funktioniert, da der Prototyp von
// max dieses Property besitzt.
console.log(max.fullName); // => Max Mustermann
