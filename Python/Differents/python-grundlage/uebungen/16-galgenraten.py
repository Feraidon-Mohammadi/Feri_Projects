from typing import List, Tuple
import random

# Fehlerbehandlung wird bewusst vernachlässigt!

LETTERS = tuple("abcdefghijklmnopqrstuvwxyzöüäß")


def read_words_from_file(path: str) -> List[str]:
    """Liest alle Wörter aus einer Textdatei und gibt sie zurück.

    Annahme: 
    - Jede Zeile enthält exakt ein Wort
    - Die Textdatei ist in UTF-8 kodiert
    """
    file = open(path, "rt", encoding="utf-8")
    words = [line.strip() for line in file]
    file.close()
    return words


def choose_random_word(word_list: List[str], min_length: int = None) -> str:
    filtered_words = word_list
    if min_length is not None and min_length >= 1:
        filtered_words = [
            word for word in word_list if len(word) >= min_length]
    return random.choice(filtered_words)


def prompt_user(prompt: str, allowed_inputs: List[str], ignore_case: bool = False) -> str:
    allowed_inputs_lowercase = [input.lower() for input in allowed_inputs]
    while True:
        user_input = input(f"{prompt}: ")
        if ignore_case:
            if user_input.lower() in allowed_inputs_lowercase:
                return user_input
        elif user_input in allowed_inputs:
            return user_input
        print("Invalid input!")


def update_mask(actual_mask: List[str], letter: str, target_word: str) -> List[str]:
    """Deckt alle Vorkommen eines Buchstabens auf."""
    new_mask = actual_mask.copy()
    for i in range(len(target_word)):
        target_letter = target_word[i]
        if target_letter == letter:
            new_mask[i] = letter
    return new_mask


def initialize_game(words: List[str]) -> Tuple[int, int, str, List[str]]:
    max_tries = 5
    target_word = choose_random_word(words, min_length=None)
    mask = list("_" * len(target_word))
    return max_tries, target_word, mask


def play_game(max_tries, target_word, mask):
    has_won = False
    num_tries = 0

    while num_tries < max_tries and not has_won:
        round = num_tries + 1
        remaining_rounds = max_tries - num_tries
        print(
            f"{round:02} {' '.join(mask)} ({num_tries}/{max_tries}, {remaining_rounds})")
        letter = prompt_user("Guess Letter", LETTERS, True).lower()
        num_tries += 1

        if letter not in target_word:
            print("This letter is not contained in the target word")
        elif letter in mask:
            print("You already guessed this letter")
        else:
            # Hier gilt: letter in target_word and letter not in mask
            mask = update_mask(mask, letter, target_word)
            if "".join(mask) == target_word:
                has_won = True
    
    if has_won:
        print(
            f"Congratulations! You found the correct word {target_word}. You needed {num_tries} attempts!")
    else:
        print(f"What a pity. The correct word is {target_word}. Try again!")


def main():
    all_words = read_words_from_file(r"./uebungen/wortliste.txt")
    all_words_lowercase = [word.lower() for word in all_words]
    game_over = False

    while not game_over:
        max_tries, target_word, mask = initialize_game(all_words_lowercase)
        play_game(max_tries, target_word, mask)
        play_again = prompt_user("Play again (y/n)?", ["y", "n"], True).lower()
        if play_again == "n":
            game_over = True

    print("Bye! See you later!")


main()
