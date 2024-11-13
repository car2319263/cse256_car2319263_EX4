import random

def choose_word():
    words = ["computer", "python", "mesa", "programming", "game"]
    return random.choice(words)
def get_word(word, guessed_lett):
    return "".join([letter if letter in guessed_lett else "_" for letter in word])

def game():
    word = choose_word()
    guessed = set()
    attempts = len(word) + 4

    print("Starting the Word Guessing Game")
    while attempts > 0:
        print("Guess the letter: ", end = " ")
        guess = input().lower()
        if len(guess)!=1:
            print("Invalid input.")
        if guess in guessed:
            print("Letter was already guessed.")
            continue
        guessed.add(guess)
        if guess in word:
            print("Correct!")
        else:
            print("Incorrect.", end = " ")
            attempts -= 1
            print(f"You have {attempts} attempts left")
        print( get_word(word, guessed))
        if "_" not in get_word(word, guessed):
            print(f"You guessed it!")
            break
    else:
        print(f"Game over... The word is {word}")

if __name__ == "__main__":
    game()