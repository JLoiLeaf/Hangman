# ----------------------------------------------------------------------
# Name:     hangmanGUI
# Purpose:  Creates the GUI of the hangman game and implements the 
#           Hangman game login
#
# Author:   Julie Loi
# ----------------------------------------------------------------------

# Module(s)
from tkinter import *
from tkinter import messagebox
from hangmanGame import *
from hangmanVariables import *

class HangmanGUI:
    '''
    Initialization Function
    Sets up the Hangman GUI and the Hangman game
    '''
    def __init__(self):
        # Hangman Class
        self.hangman = Hangman("wordbank.txt")
        
        # Initial Values
        self.letterBank = []
        self.guessesLeft = 6
        self.setupGame()
        
    '''
    Sets up a new Hangman Game
    '''
    def setupGame(self):
        self.hangman.setupHangman()     # Reset the Hangman Game
        self.letterBank = []
        self.guessesLeft = 6
        self.configureGUI()

    '''
    Configure the GUI
    Sets up the basic GUI and creates the frames in the GUI
    Create the GUI
    '''
    def configureGUI(self):
        # Configure GUI
        self.root = Tk()
        self.root.title("Hangman Game")
        self.root.configure(background=bgColor)
        self.root.geometry(str(windowWidth) + "x" + str(windowHeight)) 
        Label(self.root, text ="Hangman", foreground=txtColor, background=bgColor, font=titleFontStyle).pack(); 

        # Frames
        self.wordFrame()
        self.lettersUsedFrame()
        self.hangmanFrame()
        
        # Create GUI
        self.root.mainloop()

    '''
    The Letters Used Frame (Top Left)
    This is the frame where the used letters will be written
    '''
    def lettersUsedFrame(self):
        midLeftFrame = Frame(self.root, bg=bgColor)   
        midLeftFrame.pack(side=LEFT, anchor=N, expand=True, fill=None)

        # Title Label
        letterBankLabel = Label(midLeftFrame, text="Letter(s) Used", fg=txtColor, bg=bgColor, font=titleFontStyle)
        letterBankLabel.pack()

        # Letters Used Lables
        self.lettersUsedLabel1 = Label(midLeftFrame, text="", foreground=txtColor, background=bgColor, font=basicFontStyle)
        self.lettersUsedLabel2 = Label(midLeftFrame, text="", foreground=txtColor, background=bgColor, font=basicFontStyle)
        self.lettersUsedLabel3 = Label(midLeftFrame, text="", foreground=txtColor, background=bgColor, font=basicFontStyle)
        self.lettersUsedLabel1.pack(side=TOP); self.lettersUsedLabel2.pack(side=TOP); self.lettersUsedLabel3.pack(side=TOP)

    '''
    Updates the letter bank of letters already used
    '''
    def lettersUsed(self, letter):
        # Dynamically Update the  Letter Bank
        bank1 = bank2 = bank3 = ""; count = 0; rowAmount = 6
        self.letterBank.append(letter)
        for l in self.letterBank:
            if count<rowAmount:bank1 = bank1 + l + ", "
            elif count<rowAmount*2: bank2 = bank2 + l + ", "
            elif count<rowAmount*3: bank3 = bank3 + l + ", "
            count = count + 1

        # Reupdate Letters Used
        self.lettersUsedLabel1.config(text=bank1); self.lettersUsedLabel1.pack(side=TOP)
        self.lettersUsedLabel2.config(text=bank2); self.lettersUsedLabel2.pack(side=TOP)
        self.lettersUsedLabel3.config(text=bank3); self.lettersUsedLabel3.pack(side=TOP)

    '''
    The Hangman Frame (Top Right)
    This is the frame where the hangman will be drawn.
    '''
    def hangmanFrame(self):
        # Hangmane Frame
        midRightFrame = Frame(self.root, bg=bgColor)
        midRightFrame.pack(side=LEFT, anchor=N, expand=True, fill=None)

        # Guesses Label
        self.guessesLabel = Label(midRightFrame, text="Guesses Left: " + str(self.guessesLeft), 
            foreground=txtColor, background=bgColor, font=titleFontStyle)
        self.guessesLabel.pack()

        # Canvas
        self.canvasHM = Canvas(midRightFrame, width=(windowWidth/2), height=(windowHeight/1.5), 
            bg=bgColor, highlightbackground=bgColor)

        # Draw Stand
        self.drawStand()
        self.canvasHM.pack()

    '''
    Draw the Hangman
    Drawing the Hangman based on the number of guesses left
    '''
    def drawHangman(self):
        # Guesses Label
        self.guessesLabel.config(text="Guesses Left: " + str(self.guessesLeft))
        self.guessesLabel.pack()

        # Canvas
        canvas = self.canvasHM
        canvas.delete("all") 

        # Draw Hangman Based On Guesses Left
        self.drawStand()

        # Head
        if self.guessesLeft <= 5: canvas.create_oval(hangmanDistance - headWidth, distanceFromTop, 
            hangmanDistance + headWidth, hangmanFromTop + distanceFromTop, fill="white", width=2)

        # Body
        if self.guessesLeft <= 4: canvas.create_line(hangmanDistance, bodyTop, 
            hangmanDistance, bodyBottom, width=2)
        
        # Right Arm
        if self.guessesLeft <= 3: canvas.create_line(hangmanDistance, bodyTop + limbFromTop, 
            hangmanDistance + limbWidth, bodyTop + limbLength, width=2)
            
        # Left Arm
        if self.guessesLeft <= 2: canvas.create_line(hangmanDistance, bodyTop + limbFromTop, 
            hangmanDistance - limbWidth, bodyTop + limbLength, width=2) 
        
        # Right Leg
        if self.guessesLeft <= 1: canvas.create_line(hangmanDistance, bodyBottom, 
            hangmanDistance + limbWidth/1.5, bodyBottom + headWidth, width=2) 

        # Left Leg
        if self.guessesLeft == 0: canvas.create_line(hangmanDistance, bodyBottom, 
            hangmanDistance - limbWidth/1.5, bodyBottom + headWidth, width=2) 

    '''
    Draw the Hangman's stand
    '''
    def drawStand(self):
        canvas = self.canvasHM
        canvas.create_rectangle(standLocation, standBottom, standLocation*2, standBottom - standHeight, fill="brown", outline="brown")
        canvas.create_rectangle(poleLocation - poleWidth, poleBottom, poleLocation + poleWidth, poleTop, fill="brown", outline="brown")
        canvas.create_rectangle(poleLocation - poleWidth, poleTop, hangmanDistance, poleTop - poleWidth*2, fill="brown", outline="brown")
        canvas.create_rectangle(hangmanDistance, poleTop - 10, hangmanDistance, poleTop + hangmanFromTop*2)

    '''
    The Word Frame (Bottom)
    This is the frame where the word to guess is located.
    The entry text box and the submit button is underneath the word to fill in.
    '''
    def wordFrame(self):
        # Secret Word Guess, Entry, Submit Button, New Game Buttoon
        bottomFrame = Frame(self.root, bg=bgColor, pady=10)
        bottomFrame.pack(side=BOTTOM)        

        # Canvas
        self.canvasW = Canvas(bottomFrame, width=windowWidth, height=50, bg=bgColor, highlightbackground=bgColor)
        canvas = self.canvasW

        # Values
        wordLength = len(self.hangman.word)
        distance = 10; lengthX = 30; lengthY = 5
        x0 = 10; y0 = 50; x1 = x0 + lengthX; y1 = y0 - lengthY
        
        # Draw Blank Spaces
        while wordLength>0:
            # Draw Border
            canvas.create_rectangle(x0, y0, x1, y1, fill="black")

            # Update Values
            wordLength = wordLength - 1
            x0 = x1 + distance; x1 = x0 + lengthX

        canvas.pack(side=TOP)

        # Bottom Frame Widget(s)
        self.entry = Entry(bottomFrame, textvariable=input , font=basicFontStyle)
        submit = Button(bottomFrame, text="Submit", command=self.submitInput)
        reset = Button(bottomFrame, text="New Game", command=self.newGame)

        # Pack Widgets
        self.entry.pack(side=LEFT); submit.pack(side=LEFT); reset.pack(side=LEFT)

    '''
    Draws the letters that have been guessed in the secret word
    '''
    def drawWord(self):
        # Hangman Word
        word = self.hangman.word; wordLength = len(word); wordList = []
        for letter in word: wordList.append(letter)

        # Canvas
        canvas = self.canvasW; 
        canvas.delete("all") 

        # Canvas Values
        count = 0
        x0 = 10; y0 = 50; 
        x1 = x0 + blankXLength; y1 = y0 - blankYLength
        
        # Draw Border and Letters
        while wordLength>0:
            # Draw Border
            canvas.create_rectangle(x0, y0, x1, y1, fill="black")

            # Draw the Letter
            letter = wordList[count]
            if (letter in self.hangman.usedLetters): canvas.create_text(x0+blankDistance/2, y1 - blankLetterDistance, anchor=W, font=hangmanFontStyle, text=letter)
            else: canvas.create_text(x0+blankDistance/2, y1 - blankLetterDistance, anchor=W, font=hangmanFontStyle, text="")

            # Update Values
            wordLength = wordLength - 1; count = count + 1
            x0 = x1 + blankDistance; x1 = x0 + blankXLength

        # Redraw Canvas
        canvas.pack(side=TOP)

    '''
    Submit Button
    Checks the input and how many guesses are left
    '''
    def submitInput(self):
        letter = self.entry.get()
        
        # Check Guesses
        if (self.guessesLeft == 0): 
            messagebox.showwarning("No Guesses Left!", "You have no more guesses left. The secret word was " + self.hangman.word + "!")

        # Check if input is a letter
        elif len(letter) == 1 and letter.isalpha(): 
            value = self.hangman.guessLetter(letter)

            # The letter is already in the letter bank
            if value == 0: 
                messagebox.showinfo("Information", "This letter is already in the letter bank.")

            # The secret word has been guessed
            elif value == 1: 
                self.drawWord()
                messagebox.showinfo("Congratulations!", "You have guessed the secret word, " + self.hangman.word + "!")

            # The letter is not in the secret word
            elif value == 2:
                self.guessesLeft = self.guessesLeft - 1
                self.lettersUsed(letter.capitalize())
                self.drawHangman()
                if (self.guessesLeft != 0):
                    messagebox.showinfo("Try Again!", "This letter is not in the secret word.")
                else:
                    messagebox.showwarning("No Guesses Left!", "The secret word was " + self.hangman.word + "!")

            # The letter is in the secret word
            elif value == 3: 
                self.lettersUsed(letter.capitalize())
                self.drawWord()
                messagebox.showinfo("Good Job!", "This letter is in the secret word.")

        # Bad Input (Not a Letter)
        else: messagebox.showerror("Error", "The given input is not a letter.")

        # Clear Entry
        self.entry.delete(0, END)

    '''
    New Game Button
    Starts a new game of hangman
    '''
    def newGame(self):
        MsgBox = messagebox.askyesno("New Game?", "Are you sure you want to start a new game?")
        if MsgBox:
            self.root.destroy()
            self.setupGame()


