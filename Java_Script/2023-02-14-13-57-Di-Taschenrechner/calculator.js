const digits = Array.from("0123456789");
const operators = Array.from("+-*/%");

const numpad = document.querySelector("div.numpad");
const input = document.querySelector("input#input");

numpad.addEventListener("click", (event) => {
  const target = event.target;
  // Wir wollen nur click-Events von Buttons berücksichtigen.
  if (target.nodeName !== "BUTTON") return;
});

let previousInput = input.value;
