# Carla Aleman
# CIS256 Fall 2024
# EX4 (EX 4)
import random
# Choose a random word from a lsit
def choose_word():
    words = ["computer", "python", "mesa", "programming", "game"]
    return random.choice(words)
# Get the word with the letters guessed, otherwise _
def get_word(word, guessed_lett):
    return "".join([letter if letter in guessed_lett else "_" for letter in word])
# Game logic
def game():
    # Choose a word, set the guessed letters list and attempts
    word = choose_word()
    guessed = set()
    attempts = 15

    print("Starting the Word Guessing Game")
    # While there is attempts left
    while attempts > 0:
        # Prompt for letter
        print("Guess the letter: ", end = " ")
        guess = input().lower()
        # If no letter, invalic
        if len(guess)!=1:
            print("Invalid input.")
        # If letter was already used
        if guess in guessed:
            print("Letter was already guessed.")
            continue
        # Add letter
        guessed.add(guess)
        # Correct guess
        if guess in word:
            print("Correct!")
        # If incorrect, lower the attempts
        else:
            print("Incorrect.", end = " ")
            attempts -= 1
            print(f"You have {attempts} attempts left")
        # Print the word if guessed
        print(get_word(word, guessed))
        if "_" not in get_word(word, guessed):
            print(f"Congratulations! You guessed it!")
            break
    # If not guessed in the attempts, end game
    else:
        print(f"Game over... The word is {word}")

if __name__ == "__main__":
    game()