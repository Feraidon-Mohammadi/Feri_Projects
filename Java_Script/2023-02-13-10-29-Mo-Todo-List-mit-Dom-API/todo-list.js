const todoList = document.querySelector("#todo-list");
const itemForm = document.querySelector("#item-form");
const filterInput = document.querySelector("#filter-input");

filterInput.addEventListener("input", (event) => {
  filterItems(filterInput.value);
});

itemForm.addEventListener("submit", (event) => {
  // Verhindert das Absenden der Formulardaten an den Server.
  event.preventDefault();
  // Suche nach dem ersten Input-Element im Formular.
  const itemInput = itemForm.querySelector("input");
  // Erzeuge ein neues List-Item und füge es an den Anfang der Todo-Liste an.
  const newItem = createDeletableItem(itemInput.value);
  todoList.prepend(newItem);
  // Eingabefeld leeren.
  itemInput.value = "";
});

function createDeletableItem(text) {
  const newItem = document.createElement("li");
  newItem.innerHTML = `${text} <button class="remove-button">Entfernen</button>`;
  // Selektiere ein Button-Element, dass die Class remove-button besitzt.
  const removeButton = newItem.querySelector("button.remove-button");
  // Beim Klicken auf Entfernen, wird das newItem wieder aus der Liste entfernt.
  removeButton.addEventListener("click", () => newItem.remove());
  return newItem;
}

function filterItems(text) {
  // Suche nach allen li-Elementen in der Liste und wandle die resultierende
  // HTMLCollection in ein richtiges Array-Objekt um.
  const listItems = Array.from(todoList.querySelectorAll("li"));
  listItems.forEach((item) => {
    // Blende Element ein, wenn es den angegebenen Text enthält, andernfalls aus.
    const lowerText = item.innerText.toLowerCase();
    item.hidden = !lowerText.includes(text.toLowerCase());
  });
}

// Lösche gesamten Inhalt des Elements.
todoList.innerHTML = "";
