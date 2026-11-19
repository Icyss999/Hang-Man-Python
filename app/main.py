from random import choice
import questionary
from utils.word_bank import choose_word
from utils.leaderboard import (store_game_event,display_leaderboard)
from utils.game_track import (
    ask_for_user,
    play_round,
)
from utils.gui import format_time
import sys

# The menu is the central point where it splits 3 components : play game, leaderboard and exit

# 1, Gaming process
def play_game():

    
    key = input("Press enter to start the game ")
    print("Initializing the game....")

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


        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break

# 2, display leaderboard 
def show_leaderboard():
    
        print("\n--- Leaderboard (Top 10) ---")
        try:
            rows = display_leaderboard()
        except ValueError as error:
            print(error)
            return
        for rank, row in enumerate(rows, start=1):
            print(
                str(rank) + ". " + row["name"]
                + "  Time: " + format_time(row["timer"])
                + "  Score: " + str(row["score"])
            )
        
        choice = input("Press ENTER to return back to menu terminal")
        while choice:
            choice = input("Please press enter to return back to the terminal!")
        return
        
        
        
        
        


# 3, Exit 
def exit_game ():
    attempt = 0
    while True:
        choice = input("Please enter either Y or N: ") if attempt > 0 else input("Are you sure? (Y or N) ")
        if choice == "Y":
            break
        elif choice == "N":
            return
        attempt += 1
    print("Bye bye :(")
    sys.exit(0)


#  This is where the real stuff happens
def main():


    # Act a welcome screen for user 
    print("Welcome to our hangman game\nPlease feel free to choose your option!")
    while True:
    #  We just gonna allow user to choose the option 1,2,3
        try:

            print("====== MENU ======")

            option = questionary.select(
                    "Please choose the option below",
                    choices=["Play Game","Display Leaderboard","Exit the game"]
                    ).ask()
            # User must only input the index ONLY
            
            match option:
                    case "Play Game":
                        play_game()
                    case "Display Leaderboard":
                        show_leaderboard()
                    case "Exit the game":
                        exit_game()
        except ValueError:
            print("Please enter the index 1,2,3")
    




if __name__ == "__main__":
    main()
