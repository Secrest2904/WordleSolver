# Guessing Strategies

This folder contains the heuristic components of the AI. A "strategy" is a
method for selecting the next guess from the current candidate set.

### Files in this folder:

#### `baseStrategy.py`
Defines the abstract base class for strategies. Each strategy must implement:
`chooseNextGuess(candidateSet, history)`

#### `randomStrategy.py`
Baseline strategy that chooses a word randomly from the current candidates.

#### `freqStrategy.py`
A heuristic that ranks words based on letter frequency (or positional frequency).
Intended to be more efficient than random guessing.

### Purpose of the `strategies` module
This module isolates **how the agent decides** what to guess next. Strategies
use the logic from `core/` but are not responsible for gameplay or
simulation. This makes experimenting with new heuristics easy without touching
the rest of the system.
