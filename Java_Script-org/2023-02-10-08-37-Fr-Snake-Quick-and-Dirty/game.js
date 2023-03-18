import { randomNumber, times } from "./utils.js";

const canvas = document.querySelector("#game-screen");
const context = canvas.getContext("2d");

const cellSize = 10;
const boardSize =100;
const framesPerSecond = 10;
let snake;
let foods;
let gameOver;
let score;

function createSnake(row, column, length) {
  // Erzeuge eine Schlange aus length Zellen.
  // Alle Zellen haben dieselbe Koordinate.
  const cells = [];
  for (let i = 0; i < length; ++i) {
    cells.push({ row, column });
  }
  return {
    cells,
    direction: "right",
  };
}

function drawSnake() {
  snake.cells
    .slice()
    .reverse()
    .forEach((cell, index) => {
      const x = cell.column * cellSize;
      const y = cell.row * cellSize;
      const isHead = index === snake.cells.length - 1;
      context.fillStyle = isHead ? "black" : "green";
      context.fillRect(x, y, cellSize, cellSize);
    });
}

function drawFood() {
  foods.forEach((cell) => {
    const x = cell.column * cellSize + cellSize / 2;
    const y = cell.row * cellSize + cellSize / 2;
    context.fillStyle = "red";
    context.beginPath();
    context.arc(x, y, cellSize / 2, 0, Math.PI * 2);
    context.fill();
  });
}

function drawBackground() {
  context.clearRect(0, 0, canvas.width, canvas.height);
  context.fillStyle = "lightgray";
  context.fillRect(0, 0, canvas.width, canvas.height);
}

function moveSnake() {
  const head = snake.cells[0];
  const newHead = { row: head.row, column: head.column };

  if (snake.direction === "up") {
    newHead.row--;
  } else if (snake.direction === "down") {
    newHead.row++;
  } else if (snake.direction === "left") {
    newHead.column--;
  } else if (snake.direction === "right") {
    newHead.column++;
  }

  if (newHead.row < 0) newHead.row += boardSize;
  if (newHead.column < 0) newHead.column += boardSize;
  if (newHead.row >= boardSize) newHead.row -= boardSize;
  if (newHead.column >= boardSize) newHead.column -= boardSize;

  const collides = snake.cells.some(
    (cell) => cell.row === newHead.row && cell.column === newHead.column
  );
  if (collides) {
    gameOver = true;
  }

  const oldFoods = foods.slice();
  foods = foods.filter((cell) => cell.row !== newHead.row || cell.column !== newHead.column);
  const isOnFood = oldFoods.length > foods.length;

  snake.cells.unshift(newHead);

  if (isOnFood) {
    const { row, column } = snake.cells.at(-1); // letzte Zelle
    const count = randomNumber(0, 5);
    times(count, () => snake.cells.push({ row, column })); // count mal Zelle anhängen
    score++;
  } else {
    snake.cells.pop();
  }
}

function onKeyDown(key) {
  if (gameOver) {
    resetGame();
    return;
  }

  const directionMap = new Map();
  directionMap.set("ArrowUp", "up");
  directionMap.set("ArrowDown", "down");
  directionMap.set("ArrowLeft", "left");
  directionMap.set("ArrowRight", "right");

  if (directionMap.has(key)) {
    snake.direction = directionMap.get(key);
  }
}

function placeFood() {
  // Rate solange eine zufällige Koordinate, bis eine Koordinate gefunden wird,
  // die nicht von der Schlange belegt ist.
  while (true) {
    const row = randomNumber(0, boardSize - 1);
    const column = randomNumber(0, boardSize - 1);
    const isOccupied = snake.cells.some((cell) => cell.row === row && cell.column === column);

    if (!isOccupied) {
      foods.push({ row, column });
      return;
    }
  }
}

function drawGameOverScreen() {
  context.save();
  context.textAlign = "center";
  context.font = "bold 24px Consolas";
  context.fillStyle = "black";
  context.fillText("Game Over! Press key to play again", canvas.width / 2, canvas.height / 2);
  context.restore();
}

function resetGame() {
  const center = Math.floor(boardSize / 2);
  snake = createSnake(center, center, 4);
  foods = [];
  score = 0;
  placeFood();
  gameOver = false;
}

function drawStats() {
  context.save();
  context.fillStyle = "black";
  context.textAlign = "right";
  context.textBaseline = "top";
  context.font = "bold 16px Consolas";
  context.fillText(`Score: ${score}`, canvas.width, 0);
  context.restore();
}

function gameLoop() {
  drawBackground();

  if (gameOver) {
    drawGameOverScreen();
    return;
  }

  // Spielzustand aktualisieren
  moveSnake();
  if (foods.length === 0) {
    placeFood();
  }

  // Spiel darstellen
  drawFood();
  drawSnake();
  drawStats();
}

// Haupteinstiegspunkt in das Programm.
function main() {
  canvas.width = boardSize * cellSize;
  canvas.height = canvas.width;
  window.addEventListener("keydown", (event) => onKeyDown(event.key));

  resetGame();
 
  setInterval(gameLoop, 1000 / framesPerSecond);
}

main();
