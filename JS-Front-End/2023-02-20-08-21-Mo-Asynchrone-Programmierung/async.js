import { $ } from "./utils.js";

/* 
Hiermit teilen wir dem Browser mit, dass er nach frühestens 2 Sekunden
eine Funktion ausführen soll. Der Browser wird den Funktionsaufruf
als Task an die Task-Queue nach ca. 2 Sekunden anhängen. Der Main-Thread
wird diesen Task dann irgendwann abarbeiten und zwar innerhalb seines Event-Loops.
*/

// window.setTimeout(() => {
//   console.log("Hello, World");
// }, 2000);
// console.log("setTimeout ist fertig");

/* 
Ereignisbehandlungsroutinen (Event Handler) werden stets
asynchron ausgeführt. Das bedeutet, dass der Browser mit der
Ausführung des Skriptes fortfährt und nicht blockiert.

Wenn der Nutzer irgendwann auf den Button klickt, fügt der Browser
einen neuen Task zur Task Queue hinzu. Der Main Thread wird diesen
Task dann irgendwann abarbeiten.
*/

$("#click-me-button").addEventListener("click", () => {
  console.log("Button was clicked");
});

/* 
Eine Hintereinanderausführung von asynchronen Operationen kann schnell
zu einem Phänomen namens Pyramid of Doom führen. Darunter versteht man
eine tiefe Verschachtelung von CallBack-Funktionen.

Callback-Funktionen dienen zur Synchronisierung von asynchronen Operationen.
Wenn eine asynchrone Operation endet, ruft sie eine Callback-Funktion auf,
wodurch das Hauptprogramm über die Beendigung informiert wird und weitere
Operationen starten kann.
*/

// setTimeout(() => {
//   console.log("JavaScript");
//   setTimeout(() => {
//     console.log("is");
//     setTimeout(() => {
//       console.log("very");
//       setTimeout(() => {
//         console.log("awesome!");
//       }, 1000);
//     }, 1000);
//   }, 1000);
// }, 1000);

/* 
 Annahme: alle Funktionen sind asynchron, d.h. sie sind nicht blockierend und
 geben erst nach einer gewissen Dauer ihr Ergebnis zurück.

 function1 -> result1
 function2(result1) -> result2
 function3(result2) -> result3
*/

// Function1 ruft die callback Funktion mit ihrem Ergebnis auf,
// sobald sie fertig ist.
function function1(callback) {
  console.log("Function 1 begins to work...");
  /* 
  Führe eine sehr aufwändige und ggf. langdauernde Berechnung durch. 
  Wir simulieren die langandauernde Berechnung durch einen Timeout.
  */
  setTimeout(() => {
    console.log("Function 1 finished");
    const result = 42;
    callback(result);
  }, 2000);
}

function function2(result1, callback) {
  console.log("Function 2 begins to work...");
  setTimeout(() => {
    console.log("Function 2 finished");
    const result = result1 + 42;
    callback(result);
  }, 1500);
}

function function3(result2, callback) {
  console.log("Function 3 begins to work...");
  setTimeout(() => {
    console.log("Function 3 finished");
    const result = result2 + 42;
    callback(result);
  }, 1200);
}

// Um die asynchronen Operationen function1, ..., function3 hintereinander
// auszuführen, verwenden wir Callback-Funktionen.
function1((result1) => {
  function2(result1, (result2) => {
    function3(result2, (result3) => {
      console.log("All functions finished. End result is " + result3);
    });
  });
});

/* 
Bei dieser Variante werden die Funktionen nur angestartet, aber nicht
synchronisiert. Die Reihenfolge, in der die Funktionen enden, ist ungewiss.
*/
function1(() => {});
function2(0, () => {});
function3(0, () => {});
