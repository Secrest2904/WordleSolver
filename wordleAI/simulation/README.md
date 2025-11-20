# Simulation Tools

This folder contains code for automated evaluation of the AI solver. Nothing
here interacts with users directly—it's for running large batches of games to
test performance.

### Files in this folder:

#### `simulator.py`
Contains functions such as:
- `playSingleGame(secretWord, strategy)`
- `runSimulation(strategy, numGames)`

Used to measure:
- Average guesses to solve
- Maximum guesses
- Fail rate
- Distribution of performance

### Purpose of the `simulation` module
The goal of this module is to evaluate and compare strategies using large-scale,
repeatable experiments. This supports the "analysis" and "data collection"
portion of the project.
