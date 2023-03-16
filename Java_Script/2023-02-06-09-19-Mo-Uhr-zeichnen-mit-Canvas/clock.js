const canvas = document.querySelector("#canvas");
const context = canvas.getContext("2d");
let radius = canvas.height / 2;

// Verschiebe Koordinatensystem in den Mittelpunkt der Canvas.
context.translate(radius, radius);
// Radius auf 90% vermindern.
radius *= 0.9;
setInterval(drawClock, 1000); // alle 1000ms = 1sec soll Funktion drawClock ausgeführt werden.

function drawClock() {
  drawFace(context, radius);
  drawNumbers(context, radius);
  drawTime(context, radius);
}

function drawFace(context, radius) {
  context.beginPath();
  // Beginne einen Kreis mit Mittelpunkt (0,0), Startwinkel 0 und Endwinkel 360 Grad.
  context.arc(0, 0, radius, 0, 2 * Math.PI);
  context.fillStyle = "white";
  context.fill();

  // Erstelle einen kreisförmigen Farbverlauf mit 3 Farben.
  const gradient = context.createRadialGradient(0, 0, radius * 0.95, 0, 0, radius * 1.05);
  gradient.addColorStop(0, "#333");
  gradient.addColorStop(0.5, "white");
  gradient.addColorStop(1, "#333");
  context.strokeStyle = gradient;
  context.lineWidth = radius * 0.1;
  // Den aktuellen Pfad mit einem Farbverlauf zeichnen (entspricht einer Kontur).
  context.stroke();

  // Kleinen Innenkreis zeichnen.
  context.beginPath();
  context.arc(0, 0, radius * 0.1, 0, 2 * Math.PI);
  context.fillStyle = "#333";
  context.fill();
}

function drawNumbers(context, radius) {
  const fontSize = radius * 0.15;
  context.font = `${fontSize}px arial`;
  context.textBaseline = "middle";
  context.textAlign = "center";
  for (let i = 1; i <= 12; i++) {
    const angle = (i * Math.PI) / 6; // Math.PI / 6 entspricht 30 Grad.
    context.rotate(angle); // Drehe im Uhrzeigersinn.
    context.translate(0, -radius * 0.85); // Verschiebe Nullpunkt zum Punkt der Ziffer.
    context.rotate(-angle);
    context.fillText(i.toString(), 0, 0);
    context.rotate(angle);
    context.translate(0, radius * 0.85);
    context.rotate(-angle);
  }
}

function drawTime(context, radius) {
  const now = new Date();
  const hours = now.getHours() % 12; // 12:00 Uhr entspricht 0, 13:00 entspricht 1 usw.
  const minutes = now.getMinutes();
  const seconds = now.getSeconds();
  const thirtyDegrees = Math.PI / 6;
  const sixDegrees = Math.PI / 30;

  // Eine Stunde entspricht 30 Grad auf der Uhr.
  // Demzufolge entspricht 1 Minute ein 1/60 von 30 Grad.
  // Demzufolge entspricht 1 Sekunde ein 1/3600 von 30 Grad.
  let angle =
    hours * thirtyDegrees + (minutes * thirtyDegrees) / 60 + (seconds * thirtyDegrees) / 3600;
  drawHand(context, angle, radius * 0.5, radius * 0.07);

  // 60 Minuten entsprechen 360 Grad bzw. 6 Grad pro Minute.
  // 1 Sekunde ist 1/60 einer Minute und damit 6 / 60 = 1/10 Grad.
  angle = minutes * sixDegrees + (seconds * sixDegrees) / 60;
  drawHand(context, angle, radius * 0.8, radius * 0.07);

  // 60 Sekunden entsprechen 360 Grad, d.h. 1 Sekunde entspricht 6 Grad.
  angle = seconds * sixDegrees;
  drawHand(context, angle, radius * 0.9, radius * 0.02);
}

function drawHand(context, angle, length, lineWidth) {
  context.beginPath();
  context.lineWidth = lineWidth;
  context.lineCap = "round"; // Ecken rund zeichnen.
  context.moveTo(0, 0);
  context.rotate(angle);
  context.lineTo(0, -length); // Zeichnet Linie von aktuellem Punkt (0,0) zu (0, -length).
  context.stroke();
  context.rotate(-angle); // Rotation rückgängig machen.
}
