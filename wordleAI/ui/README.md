# Tkinter UI

This folder contains the graphical user interface for the Wordle AI assistant.

- `tkApp.py`  
  Main entrypoint for the Tkinter application. Creates the root window,
  builds the controller and view, and starts the GUI event loop.

- `wordleView.py`  
  Defines the layout and widgets for the Wordle UI: tiles, controls, status
  labels, buttons, etc. Handles drawing only. Does not contain solver logic.

- `uiController.py`  
  Connects the view to the AI logic. Reacts to button clicks and user input,
  calls the solver to get suggestions, updates the `GameState`, and instructs
  the view to refresh.

- `wordleGameApp.py` 
  The local app version

The UI code depends on the `core/` and `strategies/` modules for all game
reasoning. It should not reimplement Wordle rules or heuristics.
