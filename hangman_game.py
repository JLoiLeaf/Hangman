# ----------------------------------------------------------------------
# Name:     hangman_game
# Purpose:  The main code of the hangman game
#           It consists of the logic of the hangman game
#
# Author:   Julie Loi
# ----------------------------------------------------------------------

# Module(s)
import random

class Hangman:

    '''
    Initialization Function
    Sets up a Hangman game and gets a list of random words 
    '''
    def __init__(self, txtFile):
        # Create Wordbank (based on txtfile)
        self.wordBank = set()
        txtfile = open(txtFile)
        for line in txtfile: self.wordBank.add(line.rstrip())
        txtfile.close()
        self.wordBank = tuple(self.wordBank)

    '''
    Sets up a game of hangman
    '''
    def setupHangman(self):
        self.wordLetters = set()    # Set of letters in the word
        self.usedLetters = set()    # Set of letters already used
        self.getRandomWord()        # Secret word in the hangman game

    '''
    Gets a random secret word from the word bank for the player to guess
    Resets the wordLetters set
    '''
    def getRandomWord(self):
        # Gets the random word
        self.word = random.choice(self.wordBank)

        # Reset the set of letters in the secret word
        for letter in self.word: self.wordLetters.add(letter)

    '''
    Hangman checks if the guessed letter is in the secret word
    The return value is used in the submitInput function of the hangmanGUI class in hangmanGUI.py
    '''
    def guessLetter(self, letter):
        if letter in self.usedLetters: return 0
        else:
            self.usedLetters.add(letter)
            if letter in self.wordLetters:
                self.wordLetters.remove(letter)
                if len(self.wordLetters) == 0: return 1
                else: return 3
            else: return 2
    