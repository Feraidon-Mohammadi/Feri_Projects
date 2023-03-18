// Erzeugt eine zufällige Zahl im Bereich [from, to].
function randomNumber(from, to) {
  const diff = Math.abs(from - to) + 1;
  return Math.floor(Math.random() * diff + from);
}

class GameObject {
  x;
  y;
  width;
  height;
  speedX = 0;
  speedY = 0;
  accelerationFactor = 0.05;
  gravitySpeed = 0;
  context;

  constructor(x, y, width, height, context) {
    this.x = x;
    this.y = y;
    this.width = width;
    this.height = height;
    this.context = context;
  }

  update() {}

  move() {
    this.x += this.speedX + this.gravitySpeed;
    this.y += this.speedY;
  }

  // Beschleunigen
  accelerate() {
    this.gravitySpeed += this.accelerationFactor;
  }

  // Entschleunigen / Abbremsen
  decelerate() {
    this.gravitySpeed = Math.max(0, this.gravitySpeed - this.accelerationFactor);
  }

  crashWith(component) {
    const collisionX = this.right >= component.left && this.left <= component.right;
    const collisionY = this.bottom >= component.top && this.top <= component.bottom;
    return collisionX && collisionY;
  }

  get top() {
    return this.y;
  }

  get bottom() {
    return this.y + this.height;
  }

  get left() {
    return this.x;
  }

  get right() {
    return this.x + this.width;
  }

  stopMove() {
    this.speedX = 0;
    this.speedY = 0;
  }
}

// Diese Klasse erbt alle Properties und Methoden der Klasse GameObject.
// Wichtig: Im Constructor muss zuerst der Constructor der Superklasse GameObject aufgerufen werden.
// Hierfür verwenden wir das Schlüsselwort super.
class Block extends GameObject {
  color;

  constructor(x, y, width, height, color, context) {
    super(x, y, width, height, context); // ruft GameObject.constructor auf
    this.color = color;
  }

  // Wir verwenden eine alternative Implementierung für die geerbte Methode update.
  // Man nennt das Overriding.
  update() {
    this.context.fillStyle = this.color;
    this.context.fillRect(this.x, this.y, this.width, this.height);
  }
}

class Text {
  fontFamily;
  fontSize;
  color;
  x;
  y;
  text;
  context;

  constructor(x, y, fontSize, fontFamily, color, text, context) {
    this.x = x;
    this.y = y;
    this.fontSize = fontSize;
    this.fontFamily = fontFamily;
    this.color = color;
    this.text = text;
    this.context = context;
  }

  update() {
    this.context.font = `${this.fontSize}px ${this.fontFamily}`;
    this.context.textAlign = "right";
    this.context.textBaseline = "top";
    this.context.fillStyle = this.color;
    this.context.fillText(this.text, this.x, this.y);
  }
}

class Sprite extends GameObject {
  url;
  #image;

  constructor(x, y, width, height, url, context) {
    super(x, y, width, height, context);
    this.url = url;
    this.#image = new Image();
    this.#image.src = this.url;
  }

  update() {
    this.context.drawImage(this.#image, this.x, this.y, this.width, this.height);
  }
}

let gamePiece;
let backgroundSprites = [];
let obstacles = [];
let frameComponent;
let scoreComponent;
let isButtonPressed = false;
const defaultSpeed = -2;
const upButton = document.querySelector("#button-up");
const downButton = document.querySelector("#button-down");
const leftButton = document.querySelector("#button-left");
const rightButton = document.querySelector("#button-right");

upButton.addEventListener("mousedown", () => (gamePiece.speedY -= 1));
upButton.addEventListener("mouseup", () => gamePiece.stopMove());

downButton.addEventListener("mousedown", () => (gamePiece.speedY += 1));
downButton.addEventListener("mouseup", () => gamePiece.stopMove());

leftButton.addEventListener("mousedown", () => (gamePiece.speedX -= 1));
leftButton.addEventListener("mouseup", () => gamePiece.stopMove());

rightButton.addEventListener("mousedown", () => (gamePiece.speedX += 1));
rightButton.addEventListener("mouseup", () => gamePiece.stopMove());

// Registriere für jeden Button zwei weitere Ereignisbehandlungsroutinen, die
// ein Statusflag ein und ausschalten.
[upButton, downButton, leftButton, rightButton].forEach((button) => {
  button.addEventListener("mousedown", () => {
    isButtonPressed = true;
    console.log("Button pressed");
  });
  button.addEventListener("mouseup", () => {
    isButtonPressed = false;
    console.log("Button released");
  });
});

window.addEventListener("keydown", (event) => {
  myGameArea.keys = myGameArea.keys ?? new Map();
  myGameArea.keys.set(event.key, true); // Merke dir, welche Tasten gedrückt sind.
});
window.addEventListener("keyup", (event) => {
  myGameArea.keys = myGameArea.keys ?? new Map();
  myGameArea.keys.set(event.key, false);
});

const myGameArea = {
  // Erzeuge ein neues canvas-Element und speichere es im Property canvas.
  canvas: document.createElement("canvas"),
  // Initialisiert die Zeichenfläche.
  start() {
    // Konfiguriere das neu erstellte canvas-Element und füge es in das HTML-Dokument als erstes Element ein.
    this.canvas.width = 480;
    this.canvas.height = 270;
    this.context = this.canvas.getContext("2d");
    document.body.insertBefore(this.canvas, document.body.childNodes[0]);
    this.interval = setInterval(updateGameArea, 20); // alle 20ms updateGameArea aufrufen
  },
  // Bereinigt die Zeichenfläche.
  clear() {
    this.context.clearRect(0, 0, this.canvas.width, this.canvas.height);
  },
  // Beendet den wiederholenden Aufruf von updateGameArea.
  stop() {
    clearInterval(this.interval);
  },
  // Speichert Informationen über gedrückte Tasten
  keys: new Map(),
  // Die Frames, die bisher gerendert wurden.
  frameNumber: 0,
  // Punktezahl
  score: 0,
};

function startGame() {
  myGameArea.start();
  gamePiece = new Sprite(10, 120, 50, 21, "car-50x21.png", myGameArea.context);

  // Background Sprites initialisieren
  const spriteWidth = 318;
  const spriteCount = Math.ceil(myGameArea.canvas.width / spriteWidth) + 1;
  for (let i = 0; i < spriteCount; ++i) {
    backgroundSprites.push(
      new Sprite(
        i * spriteWidth,
        0,
        spriteWidth,
        myGameArea.canvas.height,
        "background-318x159.png",
        myGameArea.context
      )
    );
    backgroundSprites[i].speedX = defaultSpeed;
  }

  frameComponent = new Text(
    myGameArea.canvas.width,
    myGameArea.canvas.height - 12,
    12,
    "Consolas",
    "white",
    "0",
    myGameArea.context
  );
  scoreComponent = new Text(
    myGameArea.canvas.width,
    0,
    16,
    "Consolas",
    "white",
    "0",
    myGameArea.context
  );
}

function handleKeyboardInput() {
  gamePiece.stopMove();
  if (myGameArea.keys.get("ArrowUp")) {
    gamePiece.speedY = defaultSpeed;
  } else if (myGameArea.keys.get("ArrowDown")) {
    gamePiece.speedY = -defaultSpeed;
  }
  if (myGameArea.keys.get("ArrowLeft")) {
    gamePiece.speedX = defaultSpeed;
  } else if (myGameArea.keys.get("ArrowRight")) {
    gamePiece.speedX = -defaultSpeed;
  }
  if (myGameArea.keys.get(" ")) {
    gamePiece.accelerate();
  } else {
    gamePiece.decelerate();
  }
}

function createObstacle() {
  const gap = randomNumber(50, 200);
  const newHeight = randomNumber(20, 200);
  const remainingHeight = Math.max(0, myGameArea.canvas.height - newHeight - gap);
  const upperObstacle = new Block(
    myGameArea.canvas.width,
    0,
    10,
    newHeight,
    "green",
    myGameArea.context
  );

  if (remainingHeight === 0) {
    upperObstacle.speedX = defaultSpeed;
    return [upperObstacle];
  }

  const lowerObstacle = new Block(
    myGameArea.canvas.width,
    newHeight + gap,
    10,
    remainingHeight,
    "green",
    myGameArea.context
  );
  upperObstacle.speedX = defaultSpeed;
  lowerObstacle.speedX = defaultSpeed;

  return [upperObstacle, lowerObstacle];
}

function drawBackground() {
  const firstSprite = backgroundSprites.at(0);
  const lastSprite = backgroundSprites.at(-1);

  if (firstSprite.right < 0) {
    backgroundSprites.shift();
    backgroundSprites.push(firstSprite);
    firstSprite.x = lastSprite.x + lastSprite.width;
  }

  backgroundSprites.forEach((s) => s.update());
}

function playSound(url) {
  const audio = new Audio(url);
  audio.addEventListener("canplaythrough", () => audio.play());
}

// Das ist die Spielschleife. Sie wird ca. alle 20ms automatisch aufgerufen.
function updateGameArea() {
  myGameArea.clear();
  const frame = ++myGameArea.frameNumber;
  frameComponent.text = `Frames: ${frame}`;

  // Alle 150 Frames erzeugen wir ein neues Obstacle.
  if (frame === 1 || frame % 150 === 0) {
    console.log("Frame: ", frame);
    obstacles.push(...createObstacle());
  }
  // Nicht mehr sichtbare Obstacles entfernen
  myGameArea.score += obstacles.filter((o) => o.right < 0).length;
  scoreComponent.text = `Score: ${myGameArea.score}`;
  obstacles = obstacles.filter((o) => o.right >= 0);

  if (!isButtonPressed) {
    handleKeyboardInput();
  }

  // Objekte bewegen
  [gamePiece, ...obstacles, ...backgroundSprites].forEach((o) => o.move());

  // Kollisionserkennung
  const collisionDetected = obstacles.some((o) => gamePiece.crashWith(o));

  // Objekte darstellen
  if (collisionDetected) {
    // Sprite stauchen und dadurch Aufprall simulieren.
    gamePiece.width = 25;
    gamePiece.x += 25;
  }
  drawBackground();
  [gamePiece, ...obstacles, frameComponent, scoreComponent].forEach((o) => o.update());

  // Spiel ggf. beenden
  if (collisionDetected) {
    // playSound("crash.mp3");
    myGameArea.stop();
  }
}

startGame();
