"""
File: hangman.py
Description: Hangman game using the dictionary txt file given
"""

import random
import string

def main():
    """ Main program provides an outline of the program"""
    hangmanList = getDict()
    length, word = getWord(hangmanList)
    turns = getTurns()
    win = startGame(word, turns)
    displayResults(win, word)
    
def __init__():
    dictionary = open("dictionary.txt", "r")
    hangmanList = {}

def getDict():
    """Inserts each dictionary word with the key being the amount of letters
    and value being the word"""
    dictionary = open("dictionary.txt", "r")
    hangmanList = {}
    for line in dictionary:
        hangmanList.setdefault(len(line.replace("\n", "")), []).append(line.replace("\n", ""))
    return hangmanList

def getWord(hangmanList):
    """Prompts user for word selection by asking the amount letters they wish the word to have"""
    while True:
        length = input("Enter a number for the length of word: ")
        try:
            length = int(length)
        except ValueError:
            print("Value Error detects that is not an integer")
        if length in hangmanList.keys():
            print(f'Length {length} works!')
            break
        else:
            print("Please enter a length that is in our dictionary(Try a number between 2-29)")
            continue
    word = random.choice(hangmanList.get(length))
    
    return length, word

def getTurns():
    """Get amount of turns wanted by user"""
    while True:
        turns = input("Enter a number of turns > 0 and <= 26: ")
        try:
            turns = int(turns)
        except ValueError:
            print("Value Error detects that is not an integer")
        if 0 < turns < 27:
            break
        else:
            print(f'Please enter an integer between 1-26, {turns} does not work')
            continue
    return turns

def startGame(word, turns):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    print("Game beginning")
    print(f'You have {turns} turn(s) remaining')
    print(word_completion)
    while not guessed and turns > 0:
        guess = input("Guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f'You have already tried {guess}')
            elif guess not in word:
                print(f'{guess} is not in the word!')
                turns -= 1
                print(f'You have {turns} turn(s) remaining')
                guessed_letters.append(guess)
            else:
                turns -= 1
                print(f'You have {turns} turn(s) remaining')
                print(f'{guess} is in the word!')
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indexs = [i for i, letter in enumerate(word) if letter == guess]
                for index in indexs:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
                print(word_completion)
        else:
            print("ValueError detects your guess is a number or longer than one letter!")
            continue
    #win or lose
    if guessed:
        win = True
    else:
        win = False
    return win

def displayResults(win, word):
    """for debugging
    print(hangmanList.get(length))
    print(length)
    print(turns)
    print(word)
    """
    if win == True:
        print(f'Congrats you guess the word {word} right!')
    elif win == False:
        print(f'Sorry but you lost, the word was {word}!')

main()
