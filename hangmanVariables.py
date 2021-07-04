# ----------------------------------------------------------------------
# Name:     hangmanVariables
# Purpose:  Contains all of the scalable variables used in hangmanGUI
#
# Author:   Julie Loi
# ----------------------------------------------------------------------

# Window Sizes
window_height = 600
window_width = 900
canvas_width = (window_width/2)       # Half the window width

# Tkinter Styles
background_color = 'light goldenrod'
text_color = 'black'
title_font_style = ("Times New Roman", 25, "bold", "normal", "underline")
hangman_font_style = ("Times New Roman", 25, "bold")
basic_font_style = ("Times New Roman", 25)
button_font_style = ("Times New Roman", 12, "bold")

# Hangman Location
hangman_x = canvas_width/1.6    # X value of the hangman's location
hangman_y = canvas_width/8      # Y value of the hangman's location

# Hangman Stand Base Location
base_x0 = 100                       # X0 value of the stand's location
base_y0 = window_height/1.5         # Y0 value of the stand's location
base_y1 = 25                        # Y1 value of the stand's location

# Hangman Stand Pole
pole_width = 5                  # Width of the pole
pole_x = base_x0 * 1.5;         # X value of the pole's location (relative to the stand base)
pole_y0 = base_y0 - base_y1     # Y0 value of the pole's location (relative to stand base)
pole_y1 = window_height/10      # Y1 value of the top of the pole

# Hangman (Person)
hangman_figure_y0 = 150                                 # Y0 value of hangman from the top of the frame
hangmane_figure_head_width = canvas_width/16;           # Size of hangman's head
hangman_body_x0 = canvas_width/8 + hangman_figure_y0    # X0 value of hangman's top body
hangman_body_x1 = hangman_y + hangman_figure_y0 + 100   # X1 value of hangman's top body
hangman_limb_x = 20;                                    # X value of top arm/leg
hangman_limb_y = 10                                     # Y value of top arm/leg
hangman_limb_width = canvas_width/12;                   # Width of the arm/leg

# Draw Word Blank Spaces
blank_space_distance = 10       # Distance between the blank spaces
blank_width_length = 30         # Width of the blank space
blank_height_length = 5         # Height of the blank space
blank_letter_distance = 15      # Distance between the blank space and a letter