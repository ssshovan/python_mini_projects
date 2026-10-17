import random

WORDS = {
    "Animals": ["elephant", "giraffe", "kangaroo", "penguin", "dolphin", "cheetah"],
    "Fruits": ["banana", "mango", "pineapple", "strawberry", "watermelon", "papaya"],
    "Countries": ["india", "brazil", "canada", "germany", "japan", "australia"],
    "Programming": ["python", "variable", "function", "keyboard", "algorithm", "github"],
}

# Hangman drawing for each number of wrong guesses (0 to 6)
STAGES = [
    "\n  +---+\n      |\n      |\n      |\n     ===",
    "\n  +---+\n  O   |\n      |\n      |\n     ===",
    "\n  +---+\n  O   |\n  |   |\n      |\n     ===",
    "\n  +---+\n  O   |\n /|   |\n      |\n     ===",
    "\n  +---+\n  O   |\n /|\\  |\n      |\n     ===",
    "\n  +---+\n  O   |\n /|\\  |\n /    |\n     ===",
    "\n  +---+\n  O   |\n /|\\  |\n / \\  |\n     ===",
]
MAX_WRONG = len(STAGES) - 1


# Show the word with unguessed letters hidden
def masked_word(word, guessed):
    return " ".join(letter if letter in guessed else "_" for letter in word)


# Ask for a single new letter
def get_letter(guessed):
    while True:
        letter = input("Guess a letter: ").strip().lower()
        if len(letter) != 1 or not letter.isalpha():
            print("Please enter a single letter.")
        elif letter in guessed:
            print("You already guessed that letter.")
        else:
            return letter


# Play one game, return True if the player won
def play_game():
    category = random.choice(list(WORDS))
    word = random.choice(WORDS[category])
    guessed = set()
    wrong = 0

    print(f"\nCategory: {category}")
    while wrong < MAX_WRONG:
        print(STAGES[wrong])
        print(f"\nWord: {masked_word(word, guessed)}")
        print(f"Wrong guesses left: {MAX_WRONG - wrong}")
        if guessed:
            print(f"Guessed: {', '.join(sorted(guessed))}")

        letter = get_letter(guessed)
        guessed.add(letter)
        if letter in word:
            print(f"Nice! '{letter}' is in the word.")
            if all(c in guessed for c in word):
                print(f"\nYou won! The word was: {word.upper()}")
                return True
        else:
            wrong += 1
            print(f"Sorry, '{letter}' is not in the word.")

    print(STAGES[wrong])
    print(f"\nGame over! The word was: {word.upper()}")
    return False


def main():
    print("=== Hangman ===")
    wins = losses = 0
    while True:
        if play_game():
            wins += 1
        else:
            losses += 1
        print(f"\nWins: {wins}  Losses: {losses}")
        if input("Play again? (y/n): ").strip().lower() != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
