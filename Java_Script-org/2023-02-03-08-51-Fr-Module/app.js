// Die import-Anweisungen müssen immer am Anfang eines Modules stehen.
// Module verwenden automatisch den strict-Mode.
// Jedes Modul besitzt einen eigenen Namensraum, d.h. dass die darin
// definierten Bezeichner nicht mit den Bezeichnern anderer Module in Konflikt
// geraten können.
import { greetUser as sayHelloToUser } from "./library.js";
import { printNameList } from "./library.js";

// Die folgende Anweisung importiert alle exportierten Funktionen/Klassen/Variablen
// und stellt sie in einem Objekt namens lib zur Verfügung.
//import * as lib from "./library.js";
//
//lib.printNameList("Zach", "Yve", "Xavier");

// Diese Datei enthält die Programmlogik. Sie verwendet die
// Funktionen und Daten der Bibliothek.

// Die folgenden Funktionen stammen aus der Bibliothek
// library.js
sayHelloToUser("Elon");
printNameList("Alice", "Bob", "Charlie", "Damian");
