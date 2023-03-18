function findElementById(id) {
    const element = document.getElementById(id);
    if (element === null) {
        alert(`Das Element mit ID=${id} konnte nicht gefunden werden`);
    }
    return element;
}

/**
 * Erzeugt eine zufällige ganze Zahl in einem vordefinierten Intervall.
 * @param {number} min Die kleinstmögliche Zahl.
 * @param {number} max Die größtmogliche Zahl.
 * @returns Die Zufallszahl.
 */
function generateRandomNumber(min, max) {
    const difference = max - min + 1;
    return Math.floor(Math.random() * difference + min);
}

/**
 * Setzt das komplette Spiel zurück und navigiert zum Einstellungsfenster.
 */
function resetGame() {
    actualAttempts = 0;
    correctNumber = undefined;
    // Einige HTML-Elemente haben Inhalt, der sich mit dem Property innerHTML
    // auslesen und setzen lässt.
    gameAttemptsElement.innerHTML = "";
    gameMessageElement.innerHTML = "";
    // Die Methode reset setzt alle Eingabefelder eines Formulars zurück.
    gameForm.reset();
    settingsForm.reset();
    // Sichtbarkeit der Formulare setzen
    gameForm.hidden = true;
    settingsForm.hidden = false;
}

/**
 * Eine Ereignisbehandlungsroutine (Event-Handler / Event-Listener) für das Submit-Event
 * des Einstellungsfensters.
 *
 * @param {SubmitEvent} event Das ausgelöste Submit-Event.
 */
function onSubmittingSettingsForm(event) {
    // preventDefault verhindert in diesem Fall das Abschicken der Formulardaten.
    event.preventDefault();

    const min = Number(settingsMinElement.value);
    const max = Number(settingsMaxElement.value);
    correctNumber = generateRandomNumber(min, max);
    console.log(`Korrekte Zahl ist: ${correctNumber}`);

    actualAttempts = 0;
    gameAttemptsElement.innerHTML = actualAttempts;
    settingsForm.hidden = true;
    gameForm.hidden = false;
    // Den Eingabefokus auf das Eingabefeld legen, so dass der Nutzer
    // sofort mit der Eingabe der Zahl beginnen kann.
    gameGuessElement.focus();
}

function onSubmittingGameForm(event) {
    event.preventDefault();

    // Anzahl Versuche erhöhen und in der UI (User Interface) anzeigen.
    actualAttempts++;
    gameAttemptsElement.innerHTML = actualAttempts;

    // Aktuelle Zahl aus dem Eingabefeld lesen und danach das Eingabefeld leeren.
    const guessedNumber = Number(gameGuessElement.value);
    gameGuessElement.value = "";

    if (guessedNumber < correctNumber) {
        gameMessageElement.innerHTML = "Zahl ist zu klein";
    } else if (guessedNumber > correctNumber) {
        gameMessageElement.innerHTML = "Zahl ist zu groß";
    } else {
        alert(`Herzlichen Glückwunsch! Du hast gewonnen und ${actualAttempts} Versuche benötigt!`);
        resetGame();
        return;
    }

    if (actualAttempts >= maxAttempts) {
        alert(`Du hast alle Rateversuche aufgebraucht. Die richtige Zahl lautet: ${correctNumber}.`);
        resetGame();
    }
}

// Namenskonvention: Block Element Modifier Notation (BEM)
// block__element--modifier
const settingsMinElement = findElementById("settings__min");
const settingsMaxElement = findElementById("settings__max");
const gameAttemptsElement = findElementById("game__attempts");
const gameMessageElement = findElementById("game__message");
const gameGuessElement = findElementById("game__guess");
const gameForm = findElementById("game");
const settingsForm = findElementById("settings");
const gameResetElement = findElementById("game__reset");

// Variablen für den Spielzustand
let actualAttempts = 0;
let correctNumber = undefined;
const maxAttempts = 10;

// Das submit-Event wird ausgelöst, wenn das Formular abgeschickt werden soll.
// Beim Auslösen des submit-Ereignis, soll die Funktion onSubmittingSettingsForm
// aufgerufen werden.
// Hinweis: addEventListener ist die bevorzugte Variante, um Ereignisbehandlungsroutinen
// zu registrieren. Die alten Properties onclick, onsubmit etc. sollten nach Möglichkeit
// nicht mehr verwendet werden, da sie nur eine einzige Ereignisbehandlungsroutine
// registrieren können.
settingsForm.addEventListener("submit", onSubmittingSettingsForm);
gameResetElement.addEventListener("click", resetGame);
gameForm.addEventListener("submit", onSubmittingGameForm);
resetGame();
