export function randomNumber(from, to) {
  const diff = Math.abs(from - to) + 1;
  return Math.floor(Math.random() * diff + from);
}

// Ruft die Funktion action n mal nacheinander auf.
export function times(n, action) {
  for (let i = 0; i < n; ++i) {
    action();
  }
}
