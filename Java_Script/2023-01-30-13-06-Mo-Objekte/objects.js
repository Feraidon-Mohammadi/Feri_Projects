"use strict";
// Standardmäßig werden JavaScript Skripte im Sloppy-Mode ausgeführt.
// In diesem Modus kann man beispielsweise Variablen wieder löschen
// und versehentlich neue Properties im window-Objekt setzen.
// Einige Operationen sind zulässig, aber haben keinen Effekt.
// Der strict-Mode verhindert solche Fehler bzw. löst bei effektlosen Operationen
// entsprechende Meldungen aus.
// Hinweis: In JavaScript-Modulen ist der strict-Mode hingegen standardmäßig aktiviert.

// Ein Objekt ist eine Komposition aus mehreren logisch zusammenhängenden Variablen.
// Objekte lassen sich mit sogenannten Objekt-Literalen { } erzeugen.
const max = {
    age: 10,
    name: "Max Mustermann",
    address: "Villa Kunterbunt 123, Berlin",
    dateOfBirth: new Date(2000, 1, 15),
    // Eine Funktion, die ein Property eines Objektes ist,
    // nennt man auch Methode.
    initials: function () {
        // Trenne den Namen in Vor und Nachnamen auf.
        // Extrahiere aus beiden den Anfangsbuchstaben
        // Füge die Anfangsbuchstaben zusammen.
        return this.name
            .split(" ")
            .map((n) => n[0])
            .join("");
    },
    // Getter-Property
    // Hinweis: Es handelt sich hierbei _nicht_ um eine Funktion!
    // Im Gegensatz zu einem herkömmlichen Property kann ein Getter-Property
    // zusätzliche Logik beim Lesen ausführen (z.B. Caching)
    get lastName() {
        // Teile Namen in einzelne Bestandteile auf und gib das letzte Element zurück.
        return this.name.split(" ").at(-1);
    },

    // Setter-Property
    // Hinweis: keine Funktion
    // Kann im Gegensatz zu einem normalen Property zusätzliche Logik beim Setzen ausführen.
    // Das ist zum Beispiel für Validierung hilfreich.
    set lastName(newLastName) {
        const parts = this.name.split(" ");
        this.name = `${parts[0]} ${newLastName}`;
    },
};

const maria = {
    name: "Maria Luberwald",
};

console.log(max);
console.log(typeof max);
console.log(max.initials());
// console.log(maria.initials()); // liefert Fehler
console.log(max.initials.call(maria)); // Rufe die in max definierte Methode initials mit this = maria auf
maria.name = "Maria Schwarzenegger"; // Dem Property name einen neuen Wertzuweisen
console.log(maria);
console.log(maria.lastName); // Kein Call-Operator notwendig!

// max hat kein Property namens gender. Wir fügen es an dieser Stelle dynamisch hinzu.
max.gender = "male";
console.log(max.gender); // => "male"
// Nun entfernen wir das Property gender.
delete max.gender;
console.log(max.gender); // => undefined
