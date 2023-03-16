/*
Mit Hilfe von sogenannten Promises (dt: Versprechen) lassen
sich asynchrone Funktionen / Operationen deutlich komfortabler
verarbeiten und ggf. auch schreiben.

Durch die Verwendung von Promises wird die Hintereinanderausführung
und Fehlerbehandlung von asynchronen Operationen vereinfacht. Insbesondere
vermeiden Promises die "Pyramid of Doom". Dadurch ist der Code einfacher
zu verstehen und zu schreiben.

Ein Promise repräsentiert grob gesagt eine asynchrone Berechnung, die
irgendwann zu einem Ergebnis gelangt oder die mit einem Fehler abbricht.
*/

// Diese Funktion führt eine andere Funktion mit einer anfänglichen
// Verzögerung aus. Man kann sie sich als Nachbildung von setTimeout
// vorstellen. Allerdings benutzt diese Variante Promises.
function runDelayed(delay, aFunction) {
  // Diese Funktion gibt lediglich ein neues Promise-Objekt zurück.
  return new Promise((resolve, reject) => {
    window.setTimeout(() => {
      const result = aFunction();
      resolve(result);
    }, delay);
  });
}

/* 
Bei Verwendung von Promises entfällt der explizite Aufruf
einer Callback-Funktion.
*/
function function1() {
  console.log("Function 1 begins to work...");
  return runDelayed(2000, () => {
    console.log("Function 1 finished");
    return 42;
  });
}

function function2(result1) {
  console.log("Function 2 begins to work...");
  return runDelayed(1500, () => {
    console.log("Function 2 finished");
    return 42 + result1;
  });
}

function function3(result2) {
  console.log("Function 3 begins to work...");
  return runDelayed(1200, () => {
    console.log("Function 3 finished");
    return 42 + result2;
  });
}

function mightFail() {
  console.log("mightFail begins to work...");
  return new Promise(f);

  function f(resolve, reject) {
    if (Math.random() < 0.5) {
      resolve(42);
    } else {
      reject("Fehlgeschlagen :-(");
    }
  }
}

/* 
Da function1 ein Promise-Objekt zurückliefert, können wir auf diesem Promise-Objekt
die then-Methode aufrufen und eine Funktion übergeben, die aufgerufen werden soll, wenn
das Promise seinen Wert ermittelt hat.
*/
// function1()
//   .then((result1) => function2(result1))
//   .then((result2) => function3(result2))
//   .then((result3) => console.log(`Alle Funktionen fertig. Endresultat ist ${result3}`))
//   .catch((error) => console.error(`Während der Abarbeitung ist ein Fehler aufgetreten: ${error}`));

const p = Promise.all([function1(), function2(0), function3(0), mightFail()]);
p.then((results) =>
  console.log("Alle asynchronen Funktionen sind erfolgreich beendet wurden.")
).catch((error) => console.log("Mindestens eine asynchrone Operation musste abgebrochen werden."));
