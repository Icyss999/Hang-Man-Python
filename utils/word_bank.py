import random

CATEGORIES = {
    "Tourist": ["phnompenh", "siemreap", "passport", "luggage", "souvenir", "airport"],
    "Animals": ["elephant", "lion", "giraffe", "penguin", "dolphin", "kangaroo"],
    "Food": ["noodles", "pizza", "sandwich", "pancake", "chocolate", "dumpling"],
}


def show_categories():
    print("\nChoose a category:")
    names = list(CATEGORIES.keys())
    for number, name in enumerate(names, start=1):
        print(f"{number}. {name}")
    return names


def pick_category():
    names = show_categories()

    while True:
        choice = input("Enter number or name: ").strip().lower()

        if choice.isdigit():
            index = int(choice)
            if 1 <= index <= len(names):
                return names[index - 1]

        for name in names:
            if choice == name.lower():
                return name

        print("Invalid choice, please try again.")


def choose_word():
    category = pick_category()
    word = random.choice(CATEGORIES[category])
    return category, word


if __name__ == "__main__":
    category, word = choose_word()
    print(f"Category: {category}, Word: {word}")
