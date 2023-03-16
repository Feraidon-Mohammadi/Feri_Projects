import React from "react";
import ReactDOM from "react-dom/client";
import "./styles.css";

// Achtung: Die Variable root ist kein HTML-Element!
const root = ReactDOM.createRoot(document.querySelector("#root"));

// Es handelt sich hier um ein React-Element, nicht um ein herkömmliches HTML Element!
const page = (
  <>
    <p>p1</p>
    <p>p2</p>
    <p>p3</p>
    <p>p4</p>
  </>
);

// Funktioniert nicht wie gewünscht, da die append-Methode ein herkömmliches
// Node / HTML Element als Argument erwartet. page ist jedoch ein React-Element.
// document.querySelector("#root").append(page);

root.render(page);

// Exkurs: Objekte in Zeichenketten umwandeln (Serialisieren). Zeichenketten in Objekte umwandeln (Deserialisieren).
// const data = {
//   name: "alice",
//   age: 20,
//   friends: ["bob", "charlie"],
//   address: {
//     city: "berlin",
//     street: "villa kunterbunt 123",
//   },
// };
// const json = JSON.stringify(data); // Serialisieren
// console.log(json);
// const anObject = JSON.parse(json); // Deserialisieren
// console.log(anObject);
