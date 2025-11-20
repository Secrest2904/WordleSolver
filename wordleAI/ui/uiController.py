from wordleAI.core.wordList import loadWordList
from wordleAI.core.gameState import GameState
from wordleAI.core.feedback import patternToColors
from wordleAI.strategies.freqStrategy import FreqStrategy

class UiController:
    def __init__(self, view=None):
        allWords = loadWordList("data/Possiblewords.txt")  # adjust filename if needed
        self.gameState = GameState(allWords)
        self.strategy = FreqStrategy()
        self.view = view
        self.currentGuess = None

    def attachView(self, view):
        self.view = view
        self.view.setStatus(f"Loaded {len(self.gameState.candidateSet)} candidates")

    def newGame(self):
        allCandidates = self.gameState.candidateSet
        self.gameState = GameState(allCandidates)
        self.currentGuess = None
        if self.view:
            self.view.clearBoard()
            self.view.setStatus("New game started")

    def suggestGuess(self):
        guess = self.strategy.chooseNextGuess(self.gameState.candidateSet,
                                              self.gameState.history)
        self.currentGuess = guess
        if guess is None:
            if self.view:
                self.view.setStatus("No candidates left. Check your feedback input.")
            return
        if self.view:
            self.view.showSuggestedGuess(guess)

    def submitFeedback(self, pattern):
        if self.currentGuess is None:
            if self.view:
                self.view.setStatus("Ask for a suggestion first.")
            return

        try:
            feedbackColors = patternToColors(pattern)
        except ValueError as error:
            if self.view:
                self.view.setStatus(str(error))
            return

        self.gameState.applyFeedback(self.currentGuess, feedbackColors)

        remaining = self.gameState.remainingCandidates()
        if self.view:
            self.view.setStatus(f"Remaining candidates: {remaining}")
            self.view.recordRow(self.currentGuess, pattern)

        # Force a new guess next time
        self.currentGuess = None
