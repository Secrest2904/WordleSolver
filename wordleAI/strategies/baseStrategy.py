from abc import ABC, abstractmethod

class BaseStrategy(ABC):
    @abstractmethod
    def chooseNextGuess(self, candidateSet, history):
        """
        candidateSet: list[str]
        history: list[(guess: str, feedbackColors: list[FeedbackColor])]
        """
        pass
