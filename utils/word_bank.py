import random

import questionary

CATEGORIES = {
    "Tourist": ["phnompenh", "siemreap", "passport", "luggage", "souvenir", "airport"],
    "Animals": ["elephant", "lion", "giraffe", "penguin", "dolphin", "kangaroo"],
    "Food": ["noodles", "pizza", "sandwich", "pancake", "chocolate", "dumpling"],
}


def show_categories():
    print("\nChoose a category:")
    option =  questionary.select(
                    "Please choose the option below",
                    choices= list(CATEGORIES.keys())
                    ).ask()


    return option





def choose_word():
    category = show_categories()
    word = random.choice(CATEGORIES[category])
    return category, word


if __name__ == "__main__":
    category, word = choose_word()
    print(f"Category: {category}, Word: {word}")
