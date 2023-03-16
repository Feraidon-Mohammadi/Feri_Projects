"use strict";

class Rectangle {
    bottomLeft;
    // Steht ein # vor dem Namen eines Properties, so ist dieses Property
    // von außen nicht zu erreichen, d.h. der Zugriff ist nur innerhalb der Klassendefinition erlaubt.
    #width;
    #height;

    constructor(x, y, width, height) {
        this.bottomLeft = {
            x: x,
            y: y,
        };
        this.#width = Math.max(0, width);
        this.#height = Math.max(0, height);
    }

    get width() {
        return this.#width;
    }

    set width(value) {
        this.#width = Math.max(0, value);
    }

    get height() {
        return this.#height;
    }

    set height(value) {
        this.#height = Math.max(0, value);
    }

    get area() {
        return this.width * this.height;
    }

    get perimeter() {
        return 2 * (this.width + this.height);
    }

    get topLeft() {
        return {
            x: this.bottomLeft.x,
            y: this.bottomLeft.y + this.height,
        };
    }

    // Methode moveBy
    moveBy(deltaX, deltaY) {
        this.bottomLeft.x += deltaX;
        this.bottomLeft.y += deltaY;
    }
} // Ende der Klassendefinition
