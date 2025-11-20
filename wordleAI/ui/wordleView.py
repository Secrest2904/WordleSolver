import tkinter as tk

class WordleView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        root.geometry("400x300")

        mainFrame = tk.Frame(root, padx=10, pady=10)
        mainFrame.pack(fill=tk.BOTH, expand=True)

        titleLabel = tk.Label(mainFrame, text="Wordle AI Assistant", font=("Helvetica", 16))
        titleLabel.pack(pady=5)

        # Suggested guess
        self.guessLabel = tk.Label(mainFrame, text="Guess: ----", font=("Helvetica", 14))
        self.guessLabel.pack(pady=5)

        # Feedback input
        feedbackFrame = tk.Frame(mainFrame)
        feedbackFrame.pack(pady=5)

        tk.Label(feedbackFrame, text="Feedback (g/y/.):").pack(side=tk.LEFT)
        self.feedbackEntry = tk.Entry(feedbackFrame, width=5, font=("Consolas", 14))
        self.feedbackEntry.pack(side=tk.LEFT, padx=5)

        # Buttons
        buttonFrame = tk.Frame(mainFrame)
        buttonFrame.pack(pady=5)

        suggestButton = tk.Button(buttonFrame, text="Suggest Guess",
                                  command=self.controller.suggestGuess)
        suggestButton.pack(side=tk.LEFT, padx=5)

        submitButton = tk.Button(buttonFrame, text="Submit Feedback",
                                 command=self._onSubmitFeedback)
        submitButton.pack(side=tk.LEFT, padx=5)

        # History
        self.historyBox = tk.Listbox(mainFrame, height=6)
        self.historyBox.pack(fill=tk.BOTH, expand=True, pady=5)

        # Status line
        self.statusLabel = tk.Label(mainFrame, text="Ready", fg="gray")
        self.statusLabel.pack(pady=5)

    # Methods used by controller

    def showSuggestedGuess(self, guess: str):
        self.guessLabel.config(text=f"Guess: {guess}")
        self.feedbackEntry.delete(0, tk.END)
        self.feedbackEntry.focus_set()

    def setStatus(self, text: str):
        self.statusLabel.config(text=text)

    def clearBoard(self):
        self.guessLabel.config(text="Guess: ----")
        self.feedbackEntry.delete(0, tk.END)
        self.historyBox.delete(0, tk.END)

    def recordRow(self, guess: str, pattern: str):
        self.historyBox.insert(tk.END, f"{guess}  [{pattern}]")

    # Internal callback

    def _onSubmitFeedback(self):
        pattern = self.feedbackEntry.get().strip()
        self.controller.submitFeedback(pattern)
        self.feedbackEntry.delete(0, tk.END)
