# ----------------------------------------------------------------------
# Name:     hangman_gui
# Purpose:  Creates the GUI of the hangman game and implements the 
#           Hangman game login
#
# Author:   Julie Loi
# ----------------------------------------------------------------------

# Module(s)
from tkinter import *
from tkinter import messagebox
from playsound import playsound
from hangman_game import *
from hangman_variables import *

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
        self.root.configure(background=background_color)
        self.root.geometry(str(window_width) + "x" + str(window_height)) 
        Label(self.root, text ="Hangman", foreground=text_color, background=background_color, font=title_font_style).pack(); 

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
        midLeftFrame = Frame(self.root, bg=background_color)   
        midLeftFrame.pack(side=LEFT, anchor=N, expand=True, fill=None)

        # Title Label
        letterBankLabel = Label(midLeftFrame, text="Letter(s) Used", fg=text_color, bg=background_color, font=title_font_style)
        letterBankLabel.pack()

        # Letters Used Lables
        self.lettersUsedLabel1 = Label(midLeftFrame, text="", foreground=text_color, background=background_color, font=basic_font_style)
        self.lettersUsedLabel2 = Label(midLeftFrame, text="", foreground=text_color, background=background_color, font=basic_font_style)
        self.lettersUsedLabel3 = Label(midLeftFrame, text="", foreground=text_color, background=background_color, font=basic_font_style)
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
        midRightFrame = Frame(self.root, bg=background_color)
        midRightFrame.pack(side=LEFT, anchor=N, expand=True, fill=None)

        # Chances Label
        self.chancesLabel = Label(midRightFrame, text="Chances Left: " + str(self.guessesLeft), 
            foreground=text_color, background=background_color, font=title_font_style)
        self.chancesLabel.pack()

        # Canvas
        self.canvasHM = Canvas(midRightFrame, width=(window_width/2), height=(window_height/1.5), 
            bg=background_color, highlightbackground=background_color)

        # Draw Stand
        self.drawStand()
        self.canvasHM.pack()

    '''
    Draw the Hangman
    Drawing the Hangman based on the number of guesses left
    '''
    def drawHangman(self):
        # Guesses Label
        self.chancesLabel.config(text="Chances Left: " + str(self.guessesLeft))
        self.chancesLabel.pack()

        # Canvas
        canvas = self.canvasHM
        canvas.delete("all") 

        # Draw Hangman Based On Guesses Left
        self.drawStand()

        # Head
        if self.guessesLeft <= 5: canvas.create_oval(hangman_x - hangmane_figure_head_width, hangman_figure_y0, 
            hangman_x + hangmane_figure_head_width, hangman_y + hangman_figure_y0, fill="white", width=2)

        # Body
        if self.guessesLeft <= 4: canvas.create_line(hangman_x, hangman_body_x0, 
            hangman_x, hangman_body_x1, width=2)
        
        # Right Arm
        if self.guessesLeft <= 3: canvas.create_line(hangman_x, hangman_body_x0 + hangman_limb_x, 
            hangman_x + hangman_limb_width, hangman_body_x0 + hangman_limb_y, width=2)
            
        # Left Arm
        if self.guessesLeft <= 2: canvas.create_line(hangman_x, hangman_body_x0 + hangman_limb_x, 
            hangman_x - hangman_limb_width, hangman_body_x0 + hangman_limb_y, width=2) 
        
        # Right Leg
        if self.guessesLeft <= 1: canvas.create_line(hangman_x, hangman_body_x1, 
            hangman_x + hangman_limb_width/1.5, hangman_body_x1 + hangmane_figure_head_width, width=2) 

        # Left Leg
        if self.guessesLeft == 0: canvas.create_line(hangman_x, hangman_body_x1, 
            hangman_x - hangman_limb_width/1.5, hangman_body_x1 + hangmane_figure_head_width, width=2) 

    '''
    Draw the Hangman's stand
    '''
    def drawStand(self):
        canvas = self.canvasHM
        canvas.create_rectangle(base_x0, base_y0, base_x0*2, base_y0 - base_y1, fill="brown", outline="brown")
        canvas.create_rectangle(pole_x - pole_width, pole_y0, pole_x + pole_width, pole_y1, fill="brown", outline="brown")
        canvas.create_rectangle(pole_x - pole_width, pole_y1, hangman_x, pole_y1 - pole_width*2, fill="brown", outline="brown")
        canvas.create_rectangle(hangman_x, pole_y1 - 10, hangman_x, pole_y1 + hangman_y*2)

    '''
    The Word Frame (Bottom)
    This is the frame where the word to guess is located.
    The entry text box and the submit button is underneath the word to fill in.
    '''
    def wordFrame(self):
        # Secret Word Guess, Entry, Submit Button, New Game Buttoon
        bottomFrame = Frame(self.root, bg=background_color, pady=10)
        bottomFrame.pack(side=BOTTOM)        

        # Canvas
        self.canvasW = Canvas(bottomFrame, width=window_width, height=50, bg=background_color, highlightbackground=background_color)
        canvas = self.canvasW

        # Values
        wordLength = len(self.hangman.word)
        x0 = 10; y0 = 50; x1 = x0 + blank_width_length; y1 = y0 - blank_height_length
        
        # Draw Blank Spaces
        while wordLength>0:
            # Draw Border
            canvas.create_rectangle(x0, y0, x1, y1, fill="brown")

            # Update Values
            wordLength = wordLength - 1
            x0 = x1 + blank_space_distance; x1 = x0 + blank_width_length

        canvas.pack(side=TOP)

        # Bottom Frame Widget(s)
        self.entry = Entry(bottomFrame, textvariable=input , font=basic_font_style)
        submit = Button(bottomFrame, text="Submit", command=self.submitInput, font=button_font_style)
        self.entry.bind('<Return>', self.submitEnter)
        reset = Button(bottomFrame, text="New Game", command=self.newGame, font=button_font_style)

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
        x1 = x0 + blank_width_length; y1 = y0 - blank_height_length
        
        # Draw Border and Letters
        while wordLength>0:
            # Draw Border
            canvas.create_rectangle(x0, y0, x1, y1, fill="brown")

            # Draw the Letter
            letter = wordList[count]
            if (letter in self.hangman.usedLetters): canvas.create_text(x0+blank_space_distance/2, y1 - blank_letter_distance, anchor=W, font=hangman_font_style, text=letter)
            else: canvas.create_text(x0+blank_space_distance/2, y1 - blank_letter_distance, anchor=W, font=hangman_font_style, text="")

            # Update Values
            wordLength = wordLength - 1; count = count + 1
            x0 = x1 + blank_space_distance; x1 = x0 + blank_width_length

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
                playsound('success_sfx.mp3', block=0)
                messagebox.showinfo("Congratulations!", "You have guessed the secret word, " + self.hangman.word + "!")

            # The letter is not in the secret word
            elif value == 2:
                self.guessesLeft = self.guessesLeft - 1
                self.lettersUsed(letter.capitalize())
                self.drawHangman()
                if (self.guessesLeft != 0):
                    playsound('incorrect_sfx.wav', block=0)
                else:
                    playsound('fail_sfx.mp3', block=0)
                    messagebox.showwarning("No Guesses Left!", "The secret word was " + self.hangman.word + "!")

            # The letter is in the secret word
            elif value == 3: 
                self.lettersUsed(letter.capitalize())
                self.drawWord()
                playsound('correct_sfx.mp3', block=0)

        # Bad Input (Not a Letter)
        else: messagebox.showerror("Error", "The given input is not a letter.")

        # Clear Entry
        self.entry.delete(0, END)

    '''
    Entry Widget Enter Key
    Calls the submitInput function when you press 'Enter' in the entry
    '''
    def submitEnter(self, random):
        self.submitInput()

    '''
    New Game Button
    Starts a new game of hangman
    '''
    def newGame(self):
        MsgBox = messagebox.askyesno("New Game?", "Are you sure you want to start a new game?")
        if MsgBox:
            self.root.destroy()
            self.setupGame()


