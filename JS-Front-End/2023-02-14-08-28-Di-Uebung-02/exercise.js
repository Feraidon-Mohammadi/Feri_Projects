// Das Ergebnis von querySelectorAll ist ein Objekt vom Typ NodeList.
const h1Elements = document.querySelectorAll("h1");
h1Elements[0].innerText = "Angaben zur Person";
h1Elements[1].innerText = "Schulischer und beruflicher Werdegang";

h1Elements.forEach((h1) => {
  h1.outerHTML = `<h2>${h1.innerHTML}</h2>`;
  // Alternative:
  // const h2 = document.createElement("h2");
  // h2.innerText = h1.innerText;
  // h1.replaceWith(h2);
});

// Obige Anweisung lässt sich auch so schreiben:
// for (const h1 of h1Elements) {
//   h1.outerHTML = `<h2>${h1.innerHTML}</h2>`;
// }

// Selektiere alle li-Elemente, die
// 1) ...direkte Kinder von einer ul-Liste mit Id=career sind UND
// 2) ...eine Klasse namens education besitzen.
const educationItems = document.querySelectorAll("ul#career > li.education");
// Alternative: Funktioniert nur, sofern keine anderen Elemente mit
// der Klasse education hinzugefügt werden.
// document.querySelectorAll(".education");

// Umschließe den Text mit einem b-Element.
educationItems.forEach((item) => {
  item.innerHTML = `<b>${item.innerHTML}</b>`;
});

// Füge die Klassen data und personal zu jedem p-Element hinzu.
document.querySelectorAll("p").forEach((p) => {
  p.classList.add("data", "personal");
});

// Die Variablen $ und $$ sind Kürzel für die Methoden document.querySelector und querySelectorAll.
const $ = (selector) => document.querySelector(selector);
const $$ = (selector) => document.querySelectorAll(selector);

// Fasse die Texte der p und li-Elemente zusammen und schreibe
// sie in die TextArea.
const summaryElement = $("textarea");
summaryElement.value = "";
$$("p").forEach((p) => (summaryElement.value += `${p.innerText}\n`));
$$("#career > li").forEach((listItem) => {
  summaryElement.value += `${listItem.innerText}\n`;
});
