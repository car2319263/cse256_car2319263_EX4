import random

def choose_word():
    words = ["Computer", "Python", "Mesa", "Programming", "Game"]
    return random.choice(words)
def get_word(word, guessed_lett):
    return
    #for each letter in word:
    # if lett in guessed_lett
    #       return lett
    #      else return "_"

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
        print(f"Game over. The word is {word}")
