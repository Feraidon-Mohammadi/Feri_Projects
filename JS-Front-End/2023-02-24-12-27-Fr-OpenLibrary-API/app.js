import { $, $$ } from "./utils.js";

const searchResultTable = $("#result-table");
const searchForm = $("#search-form");
const searchField = $("#search-field");
const searchButton = $("#search-submit-button");
const bookDetailsDialog = $("#book-details-dialog");
const bookDetailsDialogCloseButton = $(".book-details-dialog__close");
const apiFields = ["title", "seed", "publish_year", "author_name", "publisher", "edition_count"];

bookDetailsDialogCloseButton.addEventListener("click", () => {
  bookDetailsDialog.close();
});

searchForm.addEventListener("submit", async (event) => {
  event.preventDefault();

  const searchTerm = searchField.value.trim();
  if (searchTerm.length === 0) return;

  searchButton.disabled = true;
  const searchResults = await fetchSearchResults(searchTerm);
  const mappedSearchResults = searchResults.map((result) => ({
    title: result.title,
    editionCount: result.edition_count,
    publicationYear: result.publish_year,
    publishers: result.publisher?.join("; "),
    authors: result.author_name.join("; "),
    bookId: result.seed[0].split("/").at(-1),
  }));

  renderSearchResults(mappedSearchResults);
  searchButton.disabled = false;
});

searchResultTable.addEventListener("click", async (event) => {
  const tableRow = event.target.closest("tr");
  const bookId = tableRow.dataset.bookId;
  if (bookId === undefined) return;

  const bookDetails = await fetchBookDetails(bookId);
  showBookDetails(bookDetails);
});

function showBookDetails(bookDetails) {
  const content = bookDetailsDialog.querySelector(".book-details-dialog__content");
  content.innerHTML = `<span>Titel:</span> <span>${bookDetails.title}</span>`;
  content.innerHTML += `<span>Seitenzahl:</span> <span>${bookDetails.pageCount}</span>`;
  content.innerHTML += `<span>Fachgebiete:</span> <span>${bookDetails.subjects}</span>`;
  content.innerHTML += `<span>ISBN:</span> <span>${bookDetails.isbn}</span>`;
  content.innerHTML += `<span>Herausgeber:</span> <span>${bookDetails.publishers}</span>`;
  content.innerHTML += `<span>Sprache:</span> <span>${bookDetails.language}</span>`;
  content.innerHTML += `<span>Link:</span> <a target="_blank" href="${getBookLink(
    bookDetails.id
  )}">Originalseite</a>`;
  content.innerHTML += `<span>Cover:</span> <img src="${bookDetails.coverURL}">`;
  bookDetailsDialog.showModal();
}

function getBookLink(bookId) {
  return `https://openlibrary.org/books/${bookId}`;
}

async function fetchBookDetails(bookId) {
  const response = await fetch(getBookDetailsURL(bookId));
  const detailsData = await response.json();
  return {
    id: bookId,
    title: detailsData.title,
    pageCount: detailsData.number_of_pages ?? "keine",
    subjects: detailsData.subjects?.join(", ") ?? "keine",
    isbn: detailsData.isbn_13 ?? detailsData.isbn_10 ?? "keine",
    publishers: detailsData.publishers?.join(", ") ?? "keine",
    coverURL: getBookCoverURL(bookId, "M"),
    language: detailsData.languages?.at(0).key.split("/").at(-1) ?? "keine",
  };
}

function renderSearchResults(searchResults) {
  searchResultTable.querySelector("tbody").innerHTML = "";
  searchResults.forEach((result) => {
    const row = document.createElement("tr");
    row.dataset.bookId = result.bookId;
    row.innerHTML += `<td>${result.title}</td>`;
    row.innerHTML += `<td>${result.editionCount}</td>`;
    row.innerHTML += `<td>${result.publicationYear}</td>`;
    row.innerHTML += `<td>${result.authors}</td>`;
    searchResultTable.querySelector("tbody").append(row);
  });
}

async function fetchSearchResults(searchTerm) {
  const response = await fetch(getSearchURL(searchTerm, apiFields, 20));
  const responseData = await response.json();
  return responseData.docs;
}

function getBookCoverURL(bookId, size = "S") {
  return `https://covers.openlibrary.org/b/olid/${bookId}-${size}.jpg`;
}

function getBookDetailsURL(bookId) {
  return `https://openlibrary.org/books/${bookId}.json`;
}

function getSearchURL(searchTerm, fields, limit = 20) {
  // Format der URL: schema://domain/path?query#fragment
  // Format der Query: name=wert&name=wert&name=wert
  const encodedSearchTerm = encodeURIComponent(searchTerm);
  let url = `https://openlibrary.org/search.json?title=${encodedSearchTerm}`;
  url += "&fields=" + fields.join(",");
  url += `&limit=${limit}`;
  // url += `&sort=new`;
  return url;
}

// console.log(getBookCoverURL("OL9365630M", "M"));
// console.log(getBookDetailsURL("OL9365630M"));
// console.log(
//   getSearchURL("C# in a Nutshell", ["title", "publish_year", "author_name", "language"], 5)
// );
