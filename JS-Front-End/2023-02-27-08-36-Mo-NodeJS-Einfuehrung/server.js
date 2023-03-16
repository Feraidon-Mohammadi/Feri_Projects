import express from "express"; // Node findet das Paket express anhand des Namens statt eines Pfades.
import {
  getAllUsers,
  createUser,
  findUserById,
  findUserByCredentials,
  deleteUser,
} from "./database.js";

const app = express();

// // Mit einem Router lassen sich spezielle Routen
// // separat verwalten. Das ist zum Beispiel für unterschiedliche
// // API Versionen nützlich.
// const v1Router = express.Router();
// v1Router.get("/users", (request, response) => {
//   response.send("API Version 1");
// });

// const v2Router = express.Router();
// v2Router.get("/users", (request, response) => {
//   response.send("API Version 2");
// });

// app.use("/v1", v1Router);
// app.use("/v2", v2Router);

// Diese Middleware extrahiert Daten aus dem Request-Body
// und stellt sie im Objekt request.body zur Verfügung.
app.use(express.urlencoded({ extended: false }));

// Stelle die Dokumente, die sich im Unterverzeichnis public befinden
// unter der URL / zur Verfügung. Eine Datei namens abc.html im Ordner
// public kann dann mittels URL /abc.html abgerufen werden.
app.use("/", express.static("public"));
// app.use("/wiki/v1", express.static("wiki"));

// Registriere eine Middleware-Funktion. Eine Middleware
// führt einen Bearbeitungsschritt in der Abarbeitung eines
// Requests durch und kann eine Response an den Client schicken
// oder den Request an die nächste Middleware per next Funktion
// weiterreichen.
app.use((request, response, next) => {
  console.log(`Pfad: ${request.path}`, `Query: ${request.query}`, request.body);

  next(); // rufe die nächste Middleware-Funktion in der Pipeline auf.
});

// Wir registrieren für die Route (Pfad) "/" eine Bearbeitungsfunktion. Diese Funktion
// wird nur dann aufgerufen, wenn es sich bei dem Request um ein GET-Request
// handelt.
// app.get("/", (request, response) => {
//   response.json({ x: 10, y: 20 });
// });

app.get("/users", (request, response) => {
  const limit = request.query.limit ?? Number.MAX_SAFE_INTEGER;
  const users = getAllUsers().slice(0, limit);
  response.json(users);
});

// Füge einen neuen Nutzer zur Datenbank hinzu.
// Falls der Nutzername existiert, soll die Seite
// userAlreadyExists.html vom Browser aufgerufen werden.
// Falls der Nutzer noch nicht existierte, soll auf die Seite
// newUserRegistered.html weitergeleitet werden.
app.post("/users", (request, response) => {
  try {
    createUser({
      username: request.body.username,
      password: request.body.password,
      name: request.body.name,
      city: request.body.city,
    });
    response.redirect("/newUserRegistered.html");
  } catch (error) {
    console.log(error.message);
    response.redirect("/userAlreadyExists.html");
  }
});

// Diese Route enthält einen Request-Parameter namens userId.
// Er kann mit Hilfe von request.params gelesen werden.
app.get("/users/:userId", (request, response) => {
  const user = findUserById(Number(request.params.userId));
  if (user !== null) {
    response.json({ name: user.name, id: user.id, city: user.city });
  } else {
    response.status(404);
    response.json({});
  }
});

app.delete("/users/:userId", (request, response) => {
  const wasDeleted = deleteUser(Number(request.params.userId));

  if (wasDeleted) {
    response.json({ result: "success" });
  } else {
    response.status(404);
    response.json({ result: "failure" });
  }

  // Entwickle einen dazugehörigen Frontend-Teil, der sämtliche Nutzer anzeigt.
  // Der Webseiten-Nutzer kann in einer Liste einen Nutzer auswählen und ihn löschen.
  // Um vom Frontend ein DELETE-Request an den Server zu schicken, verwendest du die
  // fetch-Funktion mit einem zweiten Argument:
  // const response = await fetch(url, { method: 'DELETE' });
});

// Registriere eine Route namens /login für den Request-Typ POST.
app.post("/login", (request, response) => {
  const user = findUserByCredentials(request.body.user, request.body.pass);
  return user !== null
    ? response.redirect("/loggedIn.html")
    : response.redirect("/failedLogin.html");
});

const server = app.listen(8080, () => {
  console.log("HTTP Server ist gestartet");
});
