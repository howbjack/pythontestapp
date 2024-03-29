"""Attempt to create a hangman game"""
import random

wordpool = ["welcome","fantasy","noodles","aadvark","unlikely","mississippi"]

def selectword():
    """Select a random word from pool"""
    return wordpool[random.randint(0,5)]

def getemptylist(strlen):
    """Build empty list"""

    my_list = []
    for _ in range(strlen):
        my_list.append('')
    return my_list

def checkposition(letter):
    """Check the position of the guessed letter in selected word """
    for pos,curr_letter in enumerate(gameletters):
        if letter == curr_letter:
            guessletters[pos] = letter

gameletters = list(selectword())
print (gameletters)

guessletters = getemptylist(len(gameletters))
print(guessletters)

while gameletters != guessletters:
    guess = input("Guess a letter: ")
    checkposition(guess)
    print(guessletters)
