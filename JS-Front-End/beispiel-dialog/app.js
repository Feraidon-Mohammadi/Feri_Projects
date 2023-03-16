import { $ } from "./utils.js";

const bookDetailsDialog = $("#book-details-dialog");

$("#show-dialog-button").addEventListener("click", () => {
  bookDetailsDialog.showModal();
});

$(".book-details-dialog__close-button").addEventListener("click", () => bookDetailsDialog.close());
$(".book-details-dialog__header-close").addEventListener("click", () => bookDetailsDialog.close());
