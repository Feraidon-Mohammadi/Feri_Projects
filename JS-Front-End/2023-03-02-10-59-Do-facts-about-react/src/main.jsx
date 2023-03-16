import React from "react";
import ReactDOM from "react-dom/client";
import "./styles.css";
import PageHeader from "./PageHeader.jsx";
import PageFooter from "./PageFooter.jsx";
import PageContent from "./PageContent.jsx";
// import defaultExport, { export1 as newNameForExport1 , export2, } from "path/to/module/file"

const root = ReactDOM.createRoot(document.querySelector("#root"));

function Page() {
  return (
    <>
      <PageHeader />
      <PageContent />
      <PageFooter />
    </>
  );
}

// console.log(document.createElement("div"));
// console.log(page);

root.render(<Page />);

// Dateien im public Verzeichnis sind unterhalb des Wurzel-Url-Pfades erreichbar.
// Beispiel: die Datei public/react.svg ist unter URL-Pfad /react.svg abrufbar.
// root.render(<img src="/react.svg" width="60" />);

// Dateien außerhalb des public-Verzeichnis müssen mit dem vollständigen Pfad
// referenziert werden. Ausgangspunkt ist das Projektverzeichnis.
// root.render(<img src="/src/assets/react.svg" width="60" />);

// Man kann sich die URL der Ressource importieren:
// import reactLogoUrl from "./assets/react.svg"
// Dies erzeugt eine Variable namens reactLogoUrl, welche den vollständigen Pfad
// zur Ressource react.svg enthält. Dieser Pfad muss dann mittels {} in JSX eingefügt werden.
// root.render(<img src={reactLogoUrl} width="60" />);
