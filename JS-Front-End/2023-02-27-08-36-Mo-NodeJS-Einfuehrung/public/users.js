import { $, $$ } from "./utils.js";

const userTable = $("#user-table");
let deleteOperationInProgress = false;

userTable.addEventListener("click", async (event) => {
  if (
    event.target instanceof HTMLButtonElement &&
    event.target.classList.contains("delete-button") &&
    !deleteOperationInProgress
  ) {
    const row = event.target.closest("tr");
    const userId = row.dataset.userId;
    deleteOperationInProgress = true;
    const wasDeleted = await deleteUser(userId);
    if (wasDeleted) {
      row.remove();
    } else {
      alert("Konnte Nutzer nicht entfernen");
    }
    deleteOperationInProgress = false;
  }
});

async function deleteUser(userId) {
  const response = await fetch(getDeleteUserURL(userId), {
    method: "DELETE",
  });
  const data = await response.json();
  // return data.result === "success";
  return response.status === 200;
}

function getAllUsersURL() {
  const origin = window.location.origin;
  return `${origin}/users`;
}

function getDeleteUserURL(userId) {
  return `${window.location.origin}/users/${userId}`;
}

async function fetchUsers() {
  const response = await fetch(getAllUsersURL());
  const users = await response.json();

  userTable.querySelector("tbody").innerHTML = "";
  users.forEach((user) => {
    const row = document.createElement("tr");
    row.dataset.userId = user.id;
    row.innerHTML = `<td>${user.id}</td>`;
    row.innerHTML += `<td>${user.name}</td>`;
    row.innerHTML += `<td>${user.city}</td>`;
    row.innerHTML += `<td><button class="delete-button" type="button">❌</button></td>`;
    userTable.querySelector("tbody").append(row);
  });
}

fetchUsers();

/*
 * 1) Hole alle User-Daten mit der fetch-Funktion.
 *    - HTTP Methode muss GET sein
 *    - URL ist http://localhost:8080/users
 * 2) Erzeuge aus den User-Daten UI-Elemente.
 *    - trage in die UI-Elemente die User-IDS ein
 * 3) Registriere einen Event-Listener, der bei Selektion ausgeführt wird.
 *    - ermittle ID des selektieren Nutzers
 *    - mit der fetch-Funktion ein Request an den Server schicken
 *      - HTTP Methode muss DELETE sein
 *      - URL muss http://localhost:8080/users/ID sein
 *    - Response auswerten
 *    - war Response positiv, dann selektierten Listeintrag entfernen
 */
