from pathlib import Path

def loadWordList(filePath: str | Path = None):
    core_dir = Path(__file__).resolve().parent

    if filePath is None:
        filePath = core_dir / "data" / "Possiblewords.txt"
    else:
        filePath = core_dir / filePath

    with open(filePath, "r") as file:
        words = [
            line.strip().lower()
            for line in file
            if len(line.strip()) == 5
        ]

    return words
