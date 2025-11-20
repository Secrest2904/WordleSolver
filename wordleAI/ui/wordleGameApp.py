# wordleAI/ui/wordleGameApp.py

import random
import tkinter as tk
import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(script_dir, ".."))
sys.path.append(parent_dir)

from core.wordList import loadWordList
from core.feedback import computeFeedback, FeedbackColor


class WordleGameUI:
    def __init__(self, root, wordListPath: str):
        self.root = root
        self.root.title("Wordle Game (AI Project Version)")

        # Load word list and choose a secret word
        self.allWords = loadWordList(wordListPath)
        self.secretWord = random.choice(self.allWords)
        # print(self.secretWord)  # uncomment for debugging

        self.currentRow = 0
        self.maxRows = 6
        self.wordLength = 5

        self._buildLayout()

    # ---------- UI layout ----------

    def _buildLayout(self):
        self.root.geometry("420x520")

        mainFrame = tk.Frame(self.root, padx=10, pady=10)
        mainFrame.pack(fill=tk.BOTH, expand=True)

        titleLabel = tk.Label(
            mainFrame,
            text="Wordle (Local Game)",
            font=("Helvetica", 18, "bold")
        )
        titleLabel.pack(pady=(0, 10))

        # Board frame
        boardFrame = tk.Frame(mainFrame)
        boardFrame.pack(pady=5)

        self.tileLabels = []
        for row in range(self.maxRows):
            rowLabels = []
            for col in range(self.wordLength):
                lbl = tk.Label(
                    boardFrame,
                    text="",
                    width=4,
                    height=2,
                    font=("Helvetica", 16, "bold"),
                    relief="solid",
                    borderwidth=1,
                    bg="#ffffff"  # default white
                )
                lbl.grid(row=row, column=col, padx=3, pady=3)
                rowLabels.append(lbl)
            self.tileLabels.append(rowLabels)

        # Guess input
        inputFrame = tk.Frame(mainFrame)
        inputFrame.pack(pady=10)

        tk.Label(inputFrame, text="Guess:").pack(side=tk.LEFT)
        self.guessEntry = tk.Entry(inputFrame, width=8, font=("Consolas", 16))
        self.guessEntry.pack(side=tk.LEFT, padx=5)
        self.guessEntry.bind("<Return>", self._onEnterPressed)

        guessButton = tk.Button(
            inputFrame,
            text="Submit Guess",
            command=self._onSubmitGuess
        )
        guessButton.pack(side=tk.LEFT, padx=5)

        # Status line
        self.statusLabel = tk.Label(mainFrame, text="Type a 5-letter word.", fg="gray")
        self.statusLabel.pack(pady=5)

        # Restart button
        restartButton = tk.Button(
            mainFrame,
            text="New Game",
            command=self._restartGame
        )
        restartButton.pack(pady=(10, 0))

    # ---------- Game logic hooks ----------

    def _onEnterPressed(self, event):
        self._onSubmitGuess()

    def _onSubmitGuess(self):
        if self.currentRow >= self.maxRows:
            return  # game over, ignore

        guess = self.guessEntry.get().strip().lower()
        if len(guess) != self.wordLength:
            self._setStatus("Guess must be 5 letters.", error=True)
            return
        if guess not in self.allWords:
            self._setStatus("Not in word list.", error=True)
            return

        # Place guess letters on the board
        for col, ch in enumerate(guess):
            self.tileLabels[self.currentRow][col].config(text=ch.upper())

        # Compute feedback vs secret
        feedbackColors = computeFeedback(self.secretWord, guess)

        # Color tiles according to feedback
        for col, color in enumerate(feedbackColors):
            if color == FeedbackColor.GREEN:
                bg = "#6aaa64"  # green
            elif color == FeedbackColor.YELLOW:
                bg = "#c9b458"  # yellow
            else:
                bg = "#787c7e"  # grey
            self.tileLabels[self.currentRow][col].config(bg=bg, fg="white")

        # Check win / lose
        if all(c == FeedbackColor.GREEN for c in feedbackColors):
            self._setStatus(f"You win! The word was {self.secretWord.upper()}.", success=True)
            self._endGame()
            return

        self.currentRow += 1
        self.guessEntry.delete(0, tk.END)

        if self.currentRow >= self.maxRows:
            self._setStatus(f"Out of rows! The word was {self.secretWord.upper()}.", error=True)
            self._endGame()
        else:
            self._setStatus(f"{self.maxRows - self.currentRow} guesses left.")

    def _endGame(self):
        # Disable entry
        self.guessEntry.config(state="disabled")

    def _restartGame(self):
        # Reset game state
        self.secretWord = random.choice(self.allWords)
        # print(self.secretWord)  # debugging
        self.currentRow = 0
        self.guessEntry.config(state="normal")
        self.guessEntry.delete(0, tk.END)
        self._setStatus("New game started. Type a 5-letter word.", success=False)

        # Clear board
        for row in range(self.maxRows):
            for col in range(self.wordLength):
                self.tileLabels[row][col].config(
                    text="",
                    bg="#ffffff",
                    fg="black"
                )

    def _setStatus(self, text: str, error: bool = False, success: bool = False):
        if error:
            self.statusLabel.config(text=text, fg="red")
        elif success:
            self.statusLabel.config(text=text, fg="green")
        else:
            self.statusLabel.config(text=text, fg="gray")


def runGame():
    root = tk.Tk()
    # adjust path to your actual data file:
    app = WordleGameUI(root, wordListPath="data/Possiblewords.txt")
    root.mainloop()
