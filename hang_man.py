"""My attempt to build a hangman game"""
import random

wordpool = ["welcome","fantasy","noodles","aadvark","unlikely","mississippi"]

# This is a comment
# Added another HBJ
# Third line

def selectword():
    """Uses a random number generator to choose the word for the game"""
    return wordpool[random.randint(0,5)]

def getemptylist(strlen):
    """Creates the list that will be filled by the guessed letters"""

    my_list = []
    for _ in range(strlen):
        my_list.append('')
    return my_list

def checkposition(letter):
    """Finds the position of the guessed letter, if it exists"""
    # Check the position of the guessed letter in word
    for i in range(len(gameletters)):
        if letter == gameletters[i]:
            guessletters[i] = letter


gameletters = list(selectword())
print (gameletters)

guessletters = getemptylist(len(gameletters))
print(guessletters)

while gameletters != guessletters:
    guess = input("Guess a letter: ")
    checkposition(guess)
    print(guessletters)
