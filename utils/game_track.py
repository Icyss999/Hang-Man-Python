import time

from utils.gui import (
    MAX_WRONG,
    draw_screen,
    show_win_screen,
    show_lose_screen,
    mask_word,
)
from utils.leaderboard import store_user, display_leaderboard

def make_hint(word):
    return "Starts with '" + word[0] + "' and has " + str(len(word)) + " letters."


def is_solved(word, guessed):
    for ch in word:
        if ch not in " -" and ch not in guessed:
            return False
    return True


def calculate_score(word, wrong):
    # More points for longer words and fewer mistakes
    return len(word) * 10 + (MAX_WRONG - wrong) * 5


def play_round(category, word):
    """Plays one round. Returns (won, seconds, score)."""
    guessed = set()
    wrong_letters = []
    show_hint = False
    hint = make_hint(word)
    message = ""
    start = time.time()

    while True:
        seconds = int(time.time() - start)
        wrong = len(wrong_letters)

        if is_solved(word, guessed):
            score = calculate_score(word, wrong)
            show_win_screen(word, seconds)
            print("Score: " + str(score))
            return True, seconds, score

        if wrong >= MAX_WRONG:
            show_lose_screen(word)
            return False, seconds, 0

        draw_screen(
            category,
            mask_word(word, guessed),
            " ".join(wrong_letters),
            wrong,
            MAX_WRONG,
            seconds,
            show_hint,
            hint,
        )
        if message:
            print(message)
        message = ""

        guess = input("Guess a letter (? for hint): ").strip().lower()

        if guess == "?":
            show_hint = True
        elif len(guess) != 1 or not guess.isalpha():
            message = "Please enter a single letter."
        elif guess in guessed or guess in wrong_letters:
            message = "You already guessed '" + guess + "'."
        elif guess in word:
            guessed.add(guess)
        else:
            wrong_letters.append(guess)


def ask_for_user():
    while True:
        name = input("Enter your name: ").strip()
        try:
            return store_user(name)
        except ValueError as error:
            print(error)



