/* 
Bei der synchronen Ausführung von Anweisungen werden die Anweisungen
nacheinander ausgeführt. Die zweite Anweisung kann erst ausgeführt werden,
wenn die erste abgearbeitet wurde.
*/
console.log("Hello");
console.log("World");

/* 
Diese Schleife führt zu einer leichten Verzögerung im Programm.
Während diese Schleife zählt, kann die Webseite nicht auf Benutzereingaben
reagieren. Deswegen spricht man auch von einer blockierenden Operation.
*/
let i = 0;
for (i = 0; i < 2_000_000_000; ++i) {}
console.log(i);

function hello() {
  console.log("Hello");
}

function world() {
  console.log("World");
}

/* 
Da Funktionsaufrufe herkömmliche Anweisungen sind, blockieren auch diese
den Browser bzw. das Programm. Erst wenn die erste Funktion abgearbeitet wurde,
kann die zweite Funktion aufgerufen werden.

Durch die synchrone Ausführung kann das Ergebnis der ersten Funktion an die zweite
Funktion übergeben werden.
*/
hello();
world();
