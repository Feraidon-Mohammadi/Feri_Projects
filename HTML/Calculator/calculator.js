import { $, $$ } from "./utils.js";

const numpad = $("div.numpad");
const input = $("input#input");
const interimCalculation = $(".interim-calculation");
const historyList = $(".history-list");
const commands = new Map([
  ["operator", applyOperator],
  ["digit", appendDigit],
  ["clear-input", clearInput],
  ["remove-last-input", removeLastInput],
  ["negate", negateOperand],
  ["decimal-point", appendDecimalPoint],
  ["result", computeResult],
  ["+", (left, right) => left + right],
  ["-", (left, right) => left - right],
  ["*", (left, right) => left * right],
  ["/", (left, right) => left / right],
  ["%", (left, right) => left % right],
]);

// Beschreibt ein Muster für Eingaben der Form -0...0 bzw. 0...0
const leadingZerosPattern = /^(?<sign>-)?(?<zeros>0+)$/i;
// Beschreibt ein Muster, das prüft, ob eine Eingabe mit einer Ziffer oder einem Punkt endet.
const endsWithDigitOrDecimalPointPattern = /[0-9.]$/i;
// Enthält sämtliche unterstützte Operatoren.
const operators = Array.from("+-*/%");

numpad.addEventListener("click", (event) => {
  // event.target ist das Element auf dem das click-Event ursprünglich
  // ausgelöst wurde.
  const target = event.target;
  // Wir wollen nur click-Events von Buttons berücksichtigen.
  if (target.nodeName !== "BUTTON") return;

  // Lies das benutzerdefinierte Attribut data-type aus und
  // verwende es als Schlüssel für die Command-Map.
  // Anhand des Schlüssels können wir die aufzurufende Funktion ermitteln
  // und ihr das optionale Attribut data-value übergeben.
  // Hinweis: Der Zugriff auf benutzerdefinierte HTML Attribute erfolgt
  // mittels dataset Property. Der Präfix data- entfällt.
  const command = commands.get(target.dataset.type);
  if (command !== undefined) {
    command(target.dataset.value);
  }
});

function applyOperator(operator) {
  if (input.length === 0) return;
  // Ist im Zwischenergebnis ein Operator enthalten, müssen wir zuerst
  // die aktuell eingegebene Zahl mit der gespeicherten Zahl verrechnen.
  const lastChar = interimCalculation.innerText.at(-1);
  if (operators.includes(lastChar)) {
    computeInterimResult(lastChar, operator);
  } else {
    interimCalculation.innerText = `${input.value} ${operator}`;
  }

  input.value = "";
}

function computeInterimResult(previousOperator, newOperator) {
  const leftOperand = interimCalculation.innerText.slice(0, -1).trim();
  const rightOperand = input.value;
  const operatorFunction = commands.get(previousOperator);
  if (operatorFunction !== undefined) {
    const result = operatorFunction(Number(leftOperand), Number(rightOperand));
    interimCalculation.innerText = `${result} ${newOperator ?? ""}`.trim();
    prependHistoryItem({ leftOperand, rightOperand, operator: previousOperator, result });
    return result;
  }
}

function prependHistoryItem({ leftOperand, rightOperand, operator, result }) {
  const listItem = document.createElement("li");
  listItem.classList.add("history-item");
  listItem.innerHTML = `<span>${leftOperand} ${operator} ${rightOperand} =</span>`;
  listItem.innerHTML += `<span class="result">${result}</span>`;
  historyList.prepend(listItem);
}

function appendDigit(digit) {
  console.log("appendDigit", digit);

  const match = leadingZerosPattern.exec(input.value);
  if (match !== null) {
    // Besteht die Eingabe nur aus einem Vorzeichen und einer oder mehreren Nullen
    // werden die Nullen einfach durch die aktuelle Digit ersetzt und das Vorzeichen
    // beibehalten.
    input.value = (match.groups.sign ?? "") + digit;
  } else {
    input.value += digit;
  }
}

function computeResult() {
  if (input.value.length === 0) return;

  const lastChar = interimCalculation.innerText.at(-1);
  if (operators.includes(lastChar)) {
    const result = computeInterimResult(lastChar, null);
    interimCalculation.innerText = "";
    input.value = result;
  }
}

function clearInput() {
  input.value = "";
}

function removeLastInput() {
  input.value = input.value.slice(0, -1);
  // Falls nach dem Entfernen eines Zeichens nur noch das Minuszeichen
  // übrig bleibt, entfernen wir dieses gleich mit.
  if (input.value === "-") {
    input.value = "";
  }
}

function negateOperand() {
  if (input.value.length === 0) return;

  // Ist ein negatives Vorzeichen vorhanden, entfernen wir es. Andernfalls
  // fügen wir es hinzu.
  if (input.value.at(0) === "-") {
    input.value = input.value.slice(1);
  } else {
    input.value = "-" + input.value;
  }
}

function appendDecimalPoint() {
  if (input.value.includes(".")) return;
  if (input.value.length === 0) return;
  input.value += ".";
}
