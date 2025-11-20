# Core Logic

This folder contains the foundational logic needed for the Wordle AI to function.
All code here is **problem-facing**, meaning it directly models the rules of
Wordle and the internal state of the game.

### Files in this folder:

#### `wordList.py`
Loads word lists (answers and allowed guesses). Ensures all words are lowercase,
stripped, and length 5.

#### `feedback.py`
Defines the representation for Wordle feedback:
- GREEN = correct letter in correct position
- YELLOW = correct letter wrong position
- GREY = letter not present
Includes helpers to convert user patterns (like `g.y..`) into internal enums.

#### `constraints.py`
Implements the logic that filters a set of candidate words based on guess
feedback. This is the core constraint-checking system of the solver.

#### `gameState.py`
Tracks the evolving state of a game:
- Current candidate word set
- Guess + feedback history
- Functions for applying feedback and updating state

### Purpose of the `core` module
This module provides the logic that every strategy, UI, or simulation depends on.
It does *not* choose guesses or run games—it only ensures all rules of Wordle
are applied consistently and correctly.
