function add(a, b, c) {
    // Ist c undefined / null dann verwende als Ersatzwert die 0.
    // Andernfalls verwende einfach den Wert, der in c steht.
    // Alte Variante: c = c || 0;
    // Alternative: c = (c === undefined || c === null) ? 0 : c;

    // Der Nullish Coalescing Operator liefert seinen rechten Operanden,
    // sofern sein linker Operand null / undefined ist. Andernfalls liefert
    // er seinen linken Operanden. Im Gegensatz zur obigen Variante mit dem
    // || Operator, versucht der ??-Operator keine Typkonvertierung.
    c = c ?? 0;
    return a + b + c;
}

console.log(add(1, 2, 3));
console.log(add(1, 2));
console.log(true && "abc"); // => "abc", da rechter Operand ausgewertet wird
console.log(false && "abc"); // => false, da rechter Operand nicht ausgewertet wird
console.log(0 && "abc"); // => 0, da 0 nach false konvertierbar.
console.log(1 && "abc"); // => "abc", da linker Ausdruck zu true konvertierbar ist
