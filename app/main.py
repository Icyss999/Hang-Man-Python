from utils.word_bank import choose_word
from utils.leaderboard import store_game_event
from utils.game_track import (
    ask_for_user,
    play_round,
    show_leaderboard,
)


def main():
    user = ask_for_user()
    user_id = user["id"]

    while True:
        category, word = choose_word()
        won, seconds, score = play_round(category, word)

        if won:
            try:
                store_game_event(user_id, seconds, score)
            except ValueError as error:
                print("Could not save result: " + str(error))

        show_leaderboard()

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()