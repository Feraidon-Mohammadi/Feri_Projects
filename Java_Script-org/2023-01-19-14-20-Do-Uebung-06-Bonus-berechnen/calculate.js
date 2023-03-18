function calculateBonus(yearsOfEmployment, age, sales, averageSales) {
    let bonus = 0;
    const bonusPerYear = 50;

    // bonus = bonus + yearsOfEmployment * 50;
    bonus += yearsOfEmployment * bonusPerYear;
    //bonus += age < 25 ? 100 : age <= 60 ? 150 : 0;

    if (age < 25) {
        bonus += 100;
    } else if (age <= 60) {
        bonus += 150;
    }

    if (sales > 2 * averageSales) {
        bonus += 500;
    } else if (sales >= averageSales) {
        bonus += 250;
    } else {
        bonus -= bonusPerYear;
    }

    return bonus;
}

// Globale Variablen für den Zugriff auf wichtige Elemente.
const employeeYears = document.getElementById("employee-years");
const employeeAge = document.getElementById("employee-age");
const employeeSales = document.getElementById("employee-sales");
const employeeAverageSales = document.getElementById("employee-average-sales");
const calculateBonusButton = document.getElementById("calculate-bonus");
const bonusForm = document.getElementById("bonus-form");
const errorDialog = document.getElementById("error-dialog");
const errorDialogMessage = document.getElementById("error-dialog-message");
const errorDialogHeader = document.querySelector(".error-dialog-header");
const errorDialogCloseButton = errorDialog.querySelector("button");
const errorDialogXButton = errorDialog.querySelector("#error-dialog-x-button");
const overlay = document.querySelector("#overlay");
console.log(errorDialog, errorDialogMessage, errorDialogHeader, errorDialogCloseButton);

function showDialog(message, title) {
    overlay.style.display = "block";
    errorDialog.style.display = "flex";
    errorDialogMessage.innerHTML = message;
    errorDialogHeader.children[0].innerHTML = title;
}

function hideDialog() {
    overlay.style.display = "none";
    errorDialog.style.display = "none";
}

function main() {
    hideDialog();
    errorDialogCloseButton.addEventListener("click", hideDialog);
    errorDialogXButton.addEventListener("click", hideDialog);

    // Wir registrieren eine anonyme Funktion (Arrow-Function), die beim Auftreten
    // des click-Events des Buttons ausgeführt werden soll.
    calculateBonusButton.addEventListener("click", () => {
        if (bonusForm.checkValidity() === false) {
            showDialog(
                "Bonusberechnung ist nicht möglich, da das Formular ungültige Eingaben enthält.",
                "Validierung fehlerhaft"
            );
            return;
        }

        let years = Number(employeeYears.value);
        let age = Number(employeeAge.value);
        let sales = Number(employeeSales.value);
        let averageSales = Number(employeeAverageSales.value);

        let bonus = calculateBonus(years, age, sales, averageSales);
        alert(`Der Mitarbeiter erhält einen Bonus von ${bonus} Euro`);
    });
}

main();
