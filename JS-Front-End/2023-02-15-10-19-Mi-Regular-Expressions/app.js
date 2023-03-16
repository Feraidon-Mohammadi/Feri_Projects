import { $, $$ } from "./utils.js";

const dateForm = $("#date-form");
const dateInput = $("#date-input");

// Syntax für reguläre Ausdrücke lautet: /pattern/modifiers
// Der Datentyp lautet RegExp. (Regular Expression)
const datePattern = /^(?<day>\d{1,2})\.(?<month>\d{1,2})\.(?<year>\d{4})$/;

// Registriere eine Ereignisbehandlungsroutine für das Event input.
// Dieses wird bei jeder Veränderung des Eingabefeldes ausgelöst.
dateInput.addEventListener("input", (event) => {
  // Wende das DatePattern auf den Text des Eingabefeldes an.
  const dateParts = getDateParts(dateInput.value.trim());
  if (dateParts === null) {
    dateInput.setCustomValidity("Falsches Format! TT.MM.JJJJ erwartet");
    return;
  }
  const { day, month, year } = dateParts;
  if (!isValidDate(day, month, year)) {
    dateInput.setCustomValidity("Das eingegebene Datum ist ungültig.");
    return;
  }

  // Alle Tests wurden überstanden. Markiere das Eingabefeld als valide.
  dateInput.setCustomValidity("");
});

// Hinweis: Das submit-Event wird nur ausgelöst, wenn alle Formularfelder
// in einem validen Zustand sind.
dateForm.addEventListener("submit", (event) => {
  event.preventDefault(); // verhindert Abschicken der Formulardaten
  // Mit Hilfe von Destructuring zerlegen wir den Rückgabewert (ein Objekt)
  // in seine einzelnen Bestandteile.
  const { day, month, year } = getDateParts(dateInput.value.trim());
  alert(`${year}-${month}-${day}`);
});

function getDateParts(dateString) {
  const matchResult = datePattern.exec(dateString.trim());
  if (matchResult === null) {
    return null;
  }

  const groups = matchResult.groups;
  const day = groups.day.padStart(2, "0");
  const month = groups.month.padStart(2, "0");
  const year = groups.year;

  return {
    day,
    month,
    year,
  };
}

function isLeapYear(year) {
  /* 
  Every year that is exactly divisible by four is a leap year, 
  except for years that are exactly divisible by 100, 
  but these centurial years are leap years if they are exactly divisible by 400. 
  For example, the years 1700, 1800, and 1900 are not leap years, but the years 1600 and 2000 are. 
  */
  const divisibleBy4 = year % 4 === 0;
  const divisibleBy100 = year % 100 === 0;
  const divisibleBy400 = year % 400 === 0;

  return divisibleBy400 || (divisibleBy4 && !divisibleBy100);
  // return divisibleBy4 && (divisibleBy400 || !divisibleBy100);
  // return year % 4 === 0 && (year % 400 === 0 || year % 100 !== 0);
}

// [1700, 1704, 1800, 1804, 2000, 2004].forEach((y) => console.log(isLeapYear(y)));

function isValidDate(day, month, year) {
  if (day <= 0 || day > 31 || month <= 0 || month > 12 || year < 0) return false;

  const daysPerMonth = [31, isLeapYear(year) ? 29 : 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  return day <= daysPerMonth[month - 1];

  // 1, 3, 5, 7, 8, 10, 12  31 Tage
  // 4, 6, 9, 11 30 Tage
  // 2 hat 28 oder 29 Tage (im Schaltjahr)
  // if ([1, 3, 5, 7, 8, 10, 12].includes(month) && day <= 31) return true;
  // if ([4, 6, 9, 11].includes(month) && day <= 30) return true;
  // return isLeapYear(year) ? day <= 29 : day <= 28;
  // return (
  //   ([1, 3, 5, 7, 8, 10, 12].includes(month) && day <= 31) ||
  //   ([4, 6, 9, 11].includes(month) && day <= 30) ||
  //   (month === 2 && (isLeapYear(year) ? day <= 29 : day <= 28))
  // );
}

// [
//   [29, 2, 2000],
//   [29, 2, 2001],
//   [31, 4, 2000],
// ].forEach((date) => console.log(isValidDate(date[0], date[1], date[2])));
