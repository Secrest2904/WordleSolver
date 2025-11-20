from collections import Counter
from .baseStrategy import BaseStrategy

class FreqStrategy(BaseStrategy):
    """
    Heuristic:
    - Compute letter frequencies over all remaining candidates.
    - For each candidate word, score it as the sum of frequencies of its unique letters.
    - Choose the word with the highest score.
    """

    def chooseNextGuess(self, candidateSet, history):
        if not candidateSet:
            return None

        # Count in how many words each letter appears
        letterCounts = Counter()
        for word in candidateSet:
            for letter in set(word):  # set to avoid double-counting within same word
                letterCounts[letter] += 1

        bestWord = None
        bestScore = -1

        for word in candidateSet:
            uniqueLetters = set(word)
            score = sum(letterCounts[ch] for ch in uniqueLetters)
            if score > bestScore:
                bestScore = score
                bestWord = word

        return bestWord
