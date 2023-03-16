const canvas = document.querySelector("#canvas");
const context = canvas.getContext("2d");

// context.translate(50, 100);
// context.rotate(Math.PI / 2);
context.fillStyle = "#ff0000";
context.fillRect(canvas.width / 2, canvas.height / 2, 50, 50);
context.strokeStyle = "rgb(255, 0, 255)";
context.strokeRect(10, 20, 100, 200);
context.font = 'bold 18px "Comic Sans MS"';
context.fillText("JS is awesome", 10, 20);
