# ----------------------------------------------------------------------
# Name:     hangmanVariables
# Purpose:  Contains all of the scalable variables used in hangmanGUI
#
# Author:   Julie Loi
# ----------------------------------------------------------------------

# Window Sizes
windowHeight = 600
windowWidth = 900
cvWidth = (windowWidth/2)       # Half the window width

# Tkinter Styles
bgColor = 'light goldenrod'
txtColor = 'black'
titleFontStyle = ("Times New Roman", 25, "bold", "normal", "underline")
hangmanFontStyle = ("Times New Roman", 25, "bold")
basicFontStyle = ("Times New Roman", 25)

# Hangman Location
hangmanDistance = cvWidth/1.6   # X value of the hangman's location
hangmanFromTop = cvWidth/8      # Y value of the hangman's location

# Hangman Stand Base Location
standLocation = 100                 # X0 value of the stand's location
standBottom = windowHeight/1.5      # Y0 value of the stand's location
standHeight = 25                    # Y1 value of the stand's location

# Hangman Stand Pole
poleWidth = 5                           # Width of the pole
poleLocation = standLocation * 1.5;     # X value of the pole's location (relative to the stand base)
poleBottom = standBottom - standHeight  # Y0 value of the pole's location (relative to stand base)
poleTop = windowHeight/10               # Y1 value of the top of the pole

# Hangman (Person)
distanceFromTop = 150                                   # Y0 value of hangman from the top of the frame
headWidth = cvWidth/16;                                 # Size of hangman's head
bodyTop = cvWidth/8 + distanceFromTop                   # X0 value of hangman's top body
bodyBottom = hangmanFromTop + distanceFromTop + 100     # X1 value of hangman's top body
limbFromTop = 20;                                        # X value of top arm/leg
limbWidth = cvWidth/12;                                  # Width of the arm/leg
limbLength = 10                                          # Y value of top arm/leg

# Draw Word
blankDistance = 10          # Distance between the blank spaces
blankXLength = 30           # Length of the blank space
blankYLength = 5            # Height of the blank space
blankLetterDistance = 15    # Distance between the blank space and a letter