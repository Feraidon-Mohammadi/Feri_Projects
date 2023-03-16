const container = document.createElement("div");
container.classList.add("container");
container.append("Ein Text");
// Alternative:
// const textNode = document.createTextNode("Ein Text");
// container.append(textNode)

const nameParagraph = document.createElement("p");
nameParagraph.id = "name";
nameParagraph.innerText = "Name";

const innerDiv = document.createElement("div");
innerDiv.style.width = "200px";
innerDiv.style.height = "200px";
innerDiv.style.backgroundColor = "red";
// Alternative: innerDiv.style = "width: 200px; height: 100px; background-color: red";
// innerDiv.style.width = null; // entfernt Property width aus Inline-Style.

container.append(nameParagraph, innerDiv);
document.body.prepend(container);

// Füge nach dem inneren Div-Element ein Wohnort-Paragraph ein.
const addressParagraph = document.createElement("p");
addressParagraph.innerText = "Wohnort";
innerDiv.after(addressParagraph);
// Alternative: container.append(addressParagraph);
// Alternative: innerDiv.insertAdjacentElement("afterend", addressParagraph);

// Füge vor dem Name-Paragraph ein Anrede-Paragraph ein.
const salutationParagraph = document.createElement("p");
salutationParagraph.innerText = "Anrede";
nameParagraph.before(salutationParagraph);

// Ersetze den ersten Kindknoten durch ein Span-Element.
const formSpan = document.createElement("span");
formSpan.innerText = "Formular";
container.childNodes[0].replaceWith(formSpan);
