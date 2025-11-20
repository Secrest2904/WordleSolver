from pathlib import Path

def loadWordList(filePath: str = None):
    if filePath is None:
        # Default to data/Possiblewords.txt relative to project root
        filePath = Path(__file__).parent.parent.parent / "data" / "Possiblewords.txt"
    
    words = []
    with open(filePath, "r") as file:
        for line in file:
            word = line.strip().lower()
            if len(word) == 5:
                words.append(word)
    return words
