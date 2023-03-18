import { printName } from "./anotherLibrary.js";

// Diese Datei ist eine Bibliothek, die von mehreren Programmen
// verwendbar sein soll.

export function greetUser(userName) {
  console.log(`Hallo ${userName}`);
}

// Diese Funktion macht Gebrauch von der Funktion printName
// aus der Bibliothek anotherLibrary.js
export function printNameList(...names) {
  for (const name of names) {
    printName(name);
  }
}
