# Data Files

This folder stores the word lists and any other static data used by the project.

### Common files:

#### `Possiblewords.txt`
The list of all possible Wordle solution words.

#### `allowed_guesses.txt`'
This is for future implementation in the case we want to check the user's guess 
with a different list than just the Possiblewords.txt
All legal guesses the game accepts (including non-solution words).

### Purpose of the `data` module
To keep all static resources separate from code. These files never change at
runtime, and keeping them here avoids cluttering the main package.
