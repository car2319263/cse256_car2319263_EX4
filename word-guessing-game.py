import random

def choose_word():
    words = ["computer", "python", "mesa", "programming", "game"]
    return random.choice(words)
def get_word(word, guessed_lett):
    out = ""
    for letter in word:
        if letter in guessed_lett:
            out + letter
        else: out + "_"
    return out

def game():
    word = choose_word()
    guessed = set()
    attempts = 20

    print("Starting the Word Guessing Game")
    while attempts > 0:
        print("Guess the letter: ", end = " ")
        guess = input().lower()
        guessed.add(guess)
        if guess in word:
            print("Correct!")
        else:
            print("Incorrect.", end = " ")
            attempts -= 1
            print(f"You have {attempts} attempts left")
        print( get_word(word, guessed))


    if "_" not in get_word(word, guessed):
        print("You guessed it!")
    else:
        print(f"Game over... The word is {word}")

if __name__ == "__main__":
    game()