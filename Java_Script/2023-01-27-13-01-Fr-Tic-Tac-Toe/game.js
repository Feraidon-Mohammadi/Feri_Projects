// Erzeugt eine Sequenz von Zahlen beginnend bei from und endend bei to.
function numberRange(from, to) {
  const count = Math.abs(to - from) + 1;
  if (from < to) {
    return [...Array(count)].map((_, index) => index + from);
  } else {
    return [...Array(count)].map((_, index) => from - index);
  }
}

class Board {
  #cells;

  // Definiert ein statisches Property mit Startwert 3.
  // Statisch bedeutet, dass das Property direkt im Objekt Board gespeichert wird
  // aber nicht in den von Board erzeugten Objekten.
  static SIZE = 4;
  static EMPTY_CELL = 0;
  static X_CELL = 1;
  static O_CELL = 2;
  static TLBR_DIAGONAL = 3; // Top-Left-To-Bottom-Right Diagonal
  static BLTR_DIAGONAL = 4; // Bottom-Left-To-Top-Right Diagonal

  // Die Konstruktorfunktion dient zur einmaligen Initialisierung eines neu erzeugten
  // Objektes.
  constructor() {
    this.clear();
  }

  /**
   * Erzeugt ein neues Board anhand vordefinierter Zellwerte.
   * @param {number[][]} cells Die Zellwerte, aus denen ein Board erzeugt werden soll.
   * @returns Das neue Board mit den angegebenen Zellwerten.
   */
  static from(cells) {
    const board = new Board();
    board.#cells = cells;
    return board;
  }

  clear() {
    const emptyRow = numberRange(1, Board.SIZE).map((_) => Board.EMPTY_CELL);
    this.#cells = numberRange(1, Board.SIZE).map((_) => emptyRow.slice());
  }

  getCells() {
    // Erzeugt eine Kopie der Zellen und gibt die Kopie zurück.
    return numberRange(0, Board.SIZE - 1).map((n) => this.getRow(n));
  }

  isEmptyCell(rowIndex, columnIndex) {
    // Prüfe, ob eine Zelle leer ist.
    return this.getCell(rowIndex, columnIndex) === Board.EMPTY_CELL;
  }

  setCell(rowIndex, columnIndex, value) {
    this.#cells[rowIndex][columnIndex] = value;
  }

  getCell(rowIndex, columnIndex) {
    return this.#cells[rowIndex][columnIndex];
  }

  getRow(rowIndex) {
    // Gibt eine Kopie einer Zeile zurück.
    return this.#cells[rowIndex].slice();
  }

  getColumn(columnIndex) {
    // Durchlaufe alle Zeilen und extrahiere jeweils die Zelle an Position columnIndex.
    return this.#cells.map((row) => row[columnIndex]);

    // Alternative Implementierung mit for-each-Schleife
    // const column = [];
    // for (const row of this.#cells) {
    //     column.push(row[columnIndex]);
    // }
    // return column;
  }

  getTLBRDiagonal() {
    // Extrahiere Zellen (0,0), (1,1) und (2,2)
    return this.#cells.map((row, rowIndex) => row[rowIndex]);
  }

  getBLTRDiagonal() {
    // Lasse rowIndex die Werte 2, 1, 0 durchlaufen und columnIndex die Werte 0, 1, 2.
    // const diagonal = [];
    // for (let rowIndex = Board.SIZE - 1, columnIndex = 0; rowIndex >= 0; --rowIndex, ++columnIndex) {
    //     diagonal.push(this.getCell(rowIndex, columnIndex));
    // }
    // return diagonal;

    // Extrahiere Zellen (2, 0), (1, 1) und (0, 2).
    // Der Parameter _ soll ausdrücken, dass wir keinen Gebrauch von ihm machen.
    return this.#cells.map((_, rowIndex) => this.getCell(Board.SIZE - rowIndex - 1, rowIndex));
  }

  hasStrikes() {
    const strikes = this.getStrikes();
    return strikes.rows.length > 0 || strikes.columns.length > 0 || strikes.diagonals.length > 0;
  }

  getStrikes() {
    // In dieser Variablen speichern wir alle gefundenen Strikes.
    const strikes = {
      rows: [],
      columns: [],
      diagonals: [],
    };

    // Durchsuche alle Zeilen und Spalten nach Strikes und füge sie zu Variable strikes hinzu.
    for (let i = 0; i < Board.SIZE; ++i) {
      const row = this.getRow(i);
      const column = this.getColumn(i);
      if (this.#isStrike(row)) {
        strikes.rows.push(i);
      }
      if (this.#isStrike(column)) {
        strikes.columns.push(i);
      }
    }

    if (this.#isStrike(this.getTLBRDiagonal())) {
      strikes.diagonals.push(Board.TLBR_DIAGONAL);
    }
    if (this.#isStrike(this.getBLTRDiagonal())) {
      strikes.diagonals.push(Board.BLTR_DIAGONAL);
    }

    return strikes;
  }

  getCoordinatesOfStrikes() {
    const coordinates = [];
    const strikes = this.getStrikes();
    coordinates.push(
      ...strikes.rows.map((rowIndex) =>
        numberRange(0, Board.SIZE - 1).map((n) => new CellCoordinate(rowIndex, n))
      )
    );
    coordinates.push(
      ...strikes.columns.map((columnIndex) =>
        numberRange(0, Board.SIZE - 1).map((n) => new CellCoordinate(n, columnIndex))
      )
    );
    if (strikes.diagonals.includes(Board.TLBR_DIAGONAL)) {
      coordinates.push(numberRange(0, Board.SIZE - 1).map((n) => new CellCoordinate(n, n)));
    }
    if (strikes.diagonals.includes(Board.BLTR_DIAGONAL)) {
      coordinates.push(
        numberRange(Board.SIZE - 1, 0).map((n) => new CellCoordinate(n, Board.SIZE - n - 1))
      );
    }
    return coordinates;
  }

  /**
   * Prüfe, ob eine Sequenz von Zellen gleich sind.
   * @param {number[]} cells Die zu prüfenden Zellen.
   * @returns true, falls alle Zellen denselben Wert besitzen und nicht leer sind.
   */
  #isStrike(cells) {
    return cells.every((cell) => cell === cells[0] && cell !== Board.EMPTY_CELL);
  }

  hasEmptyCells() {
    // Packe alle Zellwerte in ein Array (flat) und prüfe, ob es mindestens
    // eine Zelle gibt, die leer ist.
    return this.#cells.flat().some((cell) => cell === Board.EMPTY_CELL);
  }
}

// Repräsentiert eine Koordinate, bestehend aus Zeilen- und Spaltenindex.
class CellCoordinate {
  #row;
  #column;

  constructor(row, column) {
    if (row < 0 || row >= Board.SIZE) throw new Error(`${row} ist ungültige Zeilen-Koordinate.`);
    if (column < 0 || column >= Board.SIZE)
      throw new Error(`${column} ist ungültige Spalten-Koordinate.`);
    this.#row = row;
    this.#column = column;
  }

  get row() {
    return this.#row;
  }

  get column() {
    return this.#column;
  }

  toIndex() {
    return this.#row * Board.SIZE + this.#column;
  }
}

/**
 * Enthält renderbare Daten für die grafische Schnittstelle. Das ViewModel ist für
 * die Erzeugung des UiState verantwortlich.
 */
class UiState {
  message;
  cells;
  strike;
  isDialogVisible;
  dialogMessage;

  constructor() {
    this.message = '';
    this.cells = null;
    this.strike = null;
    this.isDialogVisible = false;
    this.dialogMessage = null;
  }

  copy() {
    const copy = new UiState();
    copy.message = this.message;
    copy.cells = this.cells?.slice();
    copy.strike = this.strike?.slice();
    copy.isDialogVisible = this.isDialogVisible;
    copy.dialogMessage = this.dialogMessage;
    return copy;
  }
}

/**
 * Implementiert die Applikationslogik und sagt der View, was sie darstellen soll.
 */
class ViewModel {
  #observers;
  #uiState;
  #board;
  #activePlayer;
  #gameOver;
  #notificationEnabled;

  constructor() {
    this.#observers = [];
    this.#notificationEnabled = false;
    this.restartGame();
    this.#notificationEnabled = true;
  }

  //#region Implementierung der Observable Schnittstelle.
  registerObserver(observer) {
    this.#observers.push(observer);
  }

  unregisterObserver(observer) {
    const filtered = this.#observers.filter((o) => o !== observer);
    this.#observers = filtered;
  }

  #notifyObservers() {
    if (!this.#notificationEnabled) return;
    this.#observers.forEach((o) => o.update());
  }
  //#endregion

  setCell(row, column) {
    if (this.#gameOver || !this.#board.isEmptyCell(row, column)) return;

    this.#board.setCell(
      row,
      column,
      this.#activePlayer === R.ids.firstPlayer ? Board.X_CELL : Board.O_CELL
    );

    const hasStrikes = this.#board.hasStrikes();
    const noEmptyCells = !this.#board.hasEmptyCells();

    if (hasStrikes || noEmptyCells) {
      this.#gameOver = true;
      this.#uiState.isDialogVisible = true;
      this.#uiState.dialogMessage = hasStrikes
        ? R.strings.winMessage.replace('%d', this.#activePlayer)
        : R.strings.drawMessage;
      if (hasStrikes) {
        const firstStrike = this.#board.getCoordinatesOfStrikes().at(0);
        this.#uiState.strike = firstStrike.map((coordinate) => coordinate.toIndex());
      }
    } else {
      this.#toggleActivePlayer();
      this.#uiState.message = R.strings.activePlayerMessage.replace('%d', this.#activePlayer);
    }

    this.#uiState.cells = this.#board.getCells().flat();
    this.#notifyObservers();
  }

  #toggleActivePlayer() {
    this.#activePlayer =
      this.#activePlayer === R.ids.firstPlayer ? R.ids.secondPlayer : R.ids.firstPlayer;
  }

  restartGame() {
    this.#board = new Board();
    this.#activePlayer = R.ids.firstPlayer;
    this.#gameOver = false;

    this.#uiState = new UiState();
    this.#uiState.message = R.strings.activePlayerMessage.replace('%d', this.#activePlayer);
    this.#uiState.cells = this.#board.getCells().flat();
    this.#uiState.isDialogVisible = false;
    this.#uiState.strike = [];

    this.#notifyObservers();
  }

  onDialogClosed() {
    this.#uiState.isDialogVisible = false;
    this.#uiState.dialogMessage = null;
  }

  get uiState() {
    return this.#uiState.copy();
  }
}

/**
 * Verwaltet programmweite Ressourcen.
 */
class R {
  static get classSelectors() {
    return {
      board: '.board',
      boardCell: '.board__cell',
      boardCellStriked: '.board__cell--striked',
      gameDetails: '.game-details',
      restartButton: '.restart-button',
    };
  }

  static get classNames() {
    return {
      boardCellStriked: 'board__cell--striked',
    };
  }

  static get strings() {
    return {
      cross: '❌',
      circle: '🔵',
      activePlayerMessage: 'Spieler %d ist am Zug',
      drawMessage: 'Unentschieden: Niemand hat das Spiel gewonnen',
      winMessage: 'Spieler %d hat das Spiel gewonnen.',
    };
  }

  static get ids() {
    return {
      firstPlayer: 1,
      secondPlayer: 2,
    };
  }
}

/**
 * Verwaltet die grafische Darstellung des Spiels (Presentation Logic).
 */
class View {
  #viewModel;
  #boardNode;
  #cellNodes;
  #detailsNode;
  #restartButtonNode;
  #currentUiState;

  constructor(viewModel) {
    this.#viewModel = viewModel;
    this.#boardNode = document.querySelector(R.classSelectors.board);
    this.#cellNodes = Array.from(document.querySelectorAll(R.classSelectors.boardCell));
    this.#detailsNode = document.querySelector(R.classSelectors.gameDetails);
    this.#restartButtonNode = document.querySelector(R.classSelectors.restartButton);
    this.#currentUiState = null;

    this.#boardNode.addEventListener('click', (e) => this.#onCellClicked(e));
    this.#restartButtonNode.addEventListener('click', (e) => this.#onRestartClicked(e));
    this.#viewModel.registerObserver(this);
    this.update();
  }

  #onCellClicked(event) {
    if (!this.#cellNodes.includes(event.target)) return;
    const rowIndex = event.target.dataset.row ?? 0;
    const columnIndex = event.target.dataset.column ?? 0;
    this.#viewModel.setCell(rowIndex, columnIndex);
  }

  #onRestartClicked(event) {
    this.#viewModel.restartGame();
  }

  update() {
    this.#currentUiState = this.#viewModel.uiState;

    this.#detailsNode.innerHTML = this.#currentUiState.message;
    this.#renderCells();
    this.#renderStrike();

    if (this.#currentUiState.isDialogVisible) {
      const message = this.#currentUiState.dialogMessage ?? '';
      setTimeout(() => {
        alert(message);
        this.#viewModel.onDialogClosed();
      }, 50);
    }
  }

  #renderCells() {
    this.#currentUiState.cells.forEach((cellValue, index) => {
      const cellNode = this.#cellNodes[index];
      cellNode.innerHTML = '';
      if (cellValue === Board.O_CELL) {
        cellNode.innerHTML = R.strings.circle;
      } else if (cellValue === Board.X_CELL) {
        cellNode.innerHTML = R.strings.cross;
      }
    });
  }

  #renderStrike() {
    this.#cellNodes.forEach((node) => node.classList.remove(R.classNames.boardCellStriked));
    this.#currentUiState.strike?.forEach((cellIndex) =>
      this.#cellNodes[cellIndex].classList.add(R.classNames.boardCellStriked)
    );
  }
}

function main() {
  const viewModel = new ViewModel();
  const view = new View(viewModel);
}

main();
