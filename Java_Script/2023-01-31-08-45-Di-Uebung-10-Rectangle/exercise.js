"use strict";

const rectangle = {
    bottomLeft: {
        x: 5,
        y: -3,
    },

    // Konvention: Properties, die mit einem Unterstrich beginnen, sollten nicht direkt im Code
    // verwendet werden. Sie dienen lediglich internen Zwecken und könnten jederzeit ersetzt werden.
    _width: 0,
    _height: 0,

    set width(value) {
        if (value < 0) {
            throw new Error(`${value} für width ist ungültig. Muss größer oder gleich 0 sein.`);
        }
        this._width = value;
    },

    get width() {
        return this._width;
    },

    get height() {
        return this._height;
    },

    get center() {
        return {
            x: this.bottomLeft.x + this.width / 2,
            y: this.bottomLeft.y + this.height / 2,
        };
    },

    set height(value) {
        if (value < 0) {
            throw new Error(`${value} für height ist ungültig. Muss größer oder gleich 0 sein.`);
        }
        this._height = value;
    },

    // Hinweis: Die geschweiften Klammern nach topLeft definieren einen Anweisungsblock.
    get topLeft() {
        // Hinweis: Die geschweiften Klammern nach return definieren ein Objekt-Literal.
        return {
            x: this.bottomLeft.x,
            y: this.bottomLeft.y + this.height,
        };
    },

    get topRight() {
        return {
            x: this.bottomLeft.x + this.width,
            y: this.bottomLeft.y + this.height,
        };
    },

    get bottomRight() {
        return {
            x: this.bottomLeft.x + this.width,
            y: this.bottomLeft.y,
        };
    },

    get area() {
        return this.width * this.height;
    },

    get perimeter() {
        return 2 * (this.width + this.height);
    },

    // moveBy ist ein Property vom Datentyp function. => Methode.
    moveBy: function (deltaX, deltaY) {
        this.bottomLeft.x += deltaX;
        this.bottomLeft.y += deltaY;
    },
};

console.log(rectangle.bottomLeft.x);
