"use strict";

// Konstruktorfunktion Rectangle
function Rectangle(x, y, width = 0, height = 0) {
    // Füge Property bottomLeft zu this hinzu. Der Wert von bottomLeft
    // ist ein Objekt mit den Properties x und y.
    this.bottomLeft = {
        x: x,
        y: y,
    };
    this._width = Math.max(0, width); // verhindert negative Werte
    this._height = Math.max(0, height);
}

// Methode moveBy zum Objekt Rectangle.prototype hinzufügen.
Rectangle.prototype.moveBy = function (deltaX, deltaY) {
    this.bottomLeft.x += deltaX;
    this.bottomLeft.y += deltaY;
};

// Definiere das Property width mit Getter und Setter.
Object.defineProperty(Rectangle.prototype, "width", {
    get() {
        return this._width;
    },
    set(value) {
        // Übernehme nur den neuen Wert, wenn er positiv ist.
        this._width = value >= 0 ? value : this._width;
    },
});

// Definiere das Property height mit Getter und Setter.
Object.defineProperty(Rectangle.prototype, "height", {
    get() {
        return this._height;
    },
    set(value) {
        // Übernehme nur den neuen Wert, wenn er positiv ist.
        this._height = value >= 0 ? value : this._height;
    },
});

Object.defineProperty(Rectangle.prototype, "topLeft", {
    get() {
        return {
            x: this.bottomLeft.x,
            y: this.bottomLeft.y + this.height,
        };
    },
});

Object.defineProperty(Rectangle.prototype, "area", {
    get() {
        return this._height * this._width;
    },
});
