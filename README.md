# Hangman
A simple hangman game created in Python.


## Starting the Game
To run the game, use the following command in the terminal of the project after cloning the repository:
`python hangman.py`

The following window will appear after running the command.

![Default Screen](https://user-images.githubusercontent.com/36089473/124055053-11d0ec00-d9d8-11eb-8a2b-681bae340fb9.PNG)



## Playing the Game
As with normal hangman games, the player start with a secret, hidden word, denoted by the blank spaces at the bottom left of the screen (in red).

The player can guess letters in the word using the text box and submitting the letter using the submit button, or start a new game (in blue).

All letters that have been guessed are shown in the letter bank in the top left-hand side for the player's ease (in green).

The number of guesses left is depicted in the top right along with the hangman that is slowly created as the number of guesses dwindle down (in purple).


![basic game](https://user-images.githubusercontent.com/36089473/124056151-0d0d3780-d9da-11eb-9bbb-260e9297d96b.PNG)

### Guessing Letters
To play the game, you enter a letter in the entry widget. To guess the letter you can press 'Enter' in the entry widget or press the 'Submit button'.

If the input is valid (a letter), the letter is added to the letter bank of letter(s) already used by the player if it has not been used before. If the letter is already in the letter bank, a message box will appear, reminding the player that the letter just guessed has already been guessed in the current game.

For a new guessed letter, if it exists in the secret word, the letter will appear in the given position(s) in the secret word blanks. If not, more of the hangman is draw.

Invalid Input | Valid Input (Incorrect) | Valid Input (Correct)
| :---: | :---: | :---:
| ![invalidInput](https://user-images.githubusercontent.com/36089473/124369219-38806400-dc1e-11eb-9b17-97a41a5fd624.png) | ![validIncorrectInput](https://user-images.githubusercontent.com/36089473/124369233-754c5b00-dc1e-11eb-8157-386d93095804.png) | ![validCorrectInput](https://user-images.githubusercontent.com/36089473/124369225-58b02300-dc1e-11eb-8ad4-fa505c28b890.png)

### Finishing the Game
When playing the game, there are two outcomes for the player: the secret word is guessed before all chances are used or it was not guessed and all chances have been used.

Guessing the Secret Word | Running out of Chances
| :---: | :---: 
| ![image](https://user-images.githubusercontent.com/36089473/124369296-24893200-dc1f-11eb-9940-5ef33f3e3bdc.png) | ![image](https://user-images.githubusercontent.com/36089473/124369254-a6c52680-dc1e-11eb-8d26-25b1c7d137c3.png)


### New Game
The player can begin a new game of hangman at any time by pressing the 'New Game' button.

A message box will appear to ask the player if they would like to play a new game.

![image](https://user-images.githubusercontent.com/36089473/124369325-83e74200-dc1f-11eb-8ef2-7fa490b9ee95.png)


