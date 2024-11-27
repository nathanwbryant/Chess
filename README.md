# chessboard.py

## Overview

`chessboard.py` is a Python library for modeling and analyzing chess gameplay mechanics, providing tools to represent chess pieces, evaluate their movement, and generate legal moves based on board positions defined in FEN (Forsyth–Edwards Notation). The library uses object-oriented design principles and includes logic for complex game states such as checks, pins, and castling.

---

## Features

- **Chessboard Representation**:  
  Represents an 8x8 chessboard with files (A-H) and ranks (1-8).

- **Chess Pieces**:  
  Classes for individual chess pieces, including:
  - **Pawn**
  - **Rook**
  - **Knight**
  - **Bishop**
  - **Queen**
  - **King**

- **FEN Parsing**:  
  Parse FEN strings to initialize board states and extract information:
  - Piece placement
  - Active player
  - Castling rights
  - En passant target squares
  - Move counters

- **Legal Move Generation**:  
  Calculates legal moves for all pieces, accounting for:
  - Basic movement rules
  - Captures
  - Pins
  - Castling conditions
  - En passant

- **Advanced Gameplay Mechanics**:  
  - Check and checkmate detection
  - Pinned piece handling
  - Under-attack square evaluation

---

# bot.py

## Overview

`bot.py` is a Python module that integrates with a chess engine to implement a chess bot capable of simulating and analyzing chess games. It handles move validation, FEN updates, and game mechanics like checkmate, castling, and en passant. The bot uses both random move selection and position analysis to play chess against a human opponent or simulate games.

---

## Features

- **Chess Game Simulation**:
  - Supports full chess game mechanics, including check, checkmate, castling, and en passant.

- **Move Parsing and Validation**:
  - Converts user-input moves into algebraic notation.
  - Validates moves based on the board state and rules of chess.

- **Legal Move Generation**:
  - Works in conjunction with the `chessboard` library to generate legal moves for all pieces.

- **FEN String Handling**:
  - Parses and updates FEN strings to reflect the current game state after each move.

- **Random Move Generation**:
  - Selects legal moves randomly for the bot, enabling flexible gameplay simulations.

- **Interactive Gameplay**:
  - Allows users to play as white or black while the bot takes the opposing side.

---

## Installation

Clone the repository to your local machine:

```bash
git clone <repository

cd chessboard
