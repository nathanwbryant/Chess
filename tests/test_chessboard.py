import pytest
import chessboard as c

all_squares = [
    "A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1",
    "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2",
    "A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3",
    "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4",
    "A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5",
    "A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6",
    "A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7",
    "A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8"
]

files = {
    "A1": ["A2", "A3", "A4", "A5", "A6", "A7", "A8"],
    "A2": ["A1", "A3", "A4", "A5", "A6", "A7", "A8"],
    "A3": ["A1", "A2", "A4", "A5", "A6", "A7", "A8"],
    "A4": ["A1", "A2", "A3", "A5", "A6", "A7", "A8"],
    "A5": ["A1", "A2", "A3", "A4", "A6", "A7", "A8"],
    "A6": ["A1", "A2", "A3", "A4", "A5", "A7", "A8"],
    "A7": ["A1", "A2", "A3", "A4", "A5", "A6", "A8"],
    "A8": ["A1", "A2", "A3", "A4", "A5", "A6", "A7"],

    "B1": ["B2", "B3", "B4", "B5", "B6", "B7", "B8"],
    "B2": ["B1", "B3", "B4", "B5", "B6", "B7", "B8"],
    "B3": ["B1", "B2", "B4", "B5", "B6", "B7", "B8"],
    "B4": ["B1", "B2", "B3", "B5", "B6", "B7", "B8"],
    "B5": ["B1", "B2", "B3", "B4", "B6", "B7", "B8"],
    "B6": ["B1", "B2", "B3", "B4", "B5", "B7", "B8"],
    "B7": ["B1", "B2", "B3", "B4", "B5", "B6", "B8"],
    "B8": ["B1", "B2", "B3", "B4", "B5", "B6", "B7"],

    "C1": ["C2", "C3", "C4", "C5", "C6", "C7", "C8"],
    "C2": ["C1", "C3", "C4", "C5", "C6", "C7", "C8"],
    "C3": ["C1", "C2", "C4", "C5", "C6", "C7", "C8"],
    "C4": ["C1", "C2", "C3", "C5", "C6", "C7", "C8"],
    "C5": ["C1", "C2", "C3", "C4", "C6", "C7", "C8"],
    "C6": ["C1", "C2", "C3", "C4", "C5", "C7", "C8"],
    "C7": ["C1", "C2", "C3", "C4", "C5", "C6", "C8"],
    "C8": ["C1", "C2", "C3", "C4", "C5", "C6", "C7"],

    "D1": ["D2", "D3", "D4", "D5", "D6", "D7", "D8"],
    "D2": ["D1", "D3", "D4", "D5", "D6", "D7", "D8"],
    "D3": ["D1", "D2", "D4", "D5", "D6", "D7", "D8"],
    "D4": ["D1", "D2", "D3", "D5", "D6", "D7", "D8"],
    "D5": ["D1", "D2", "D3", "D4", "D6", "D7", "D8"],
    "D6": ["D1", "D2", "D3", "D4", "D5", "D7", "D8"],
    "D7": ["D1", "D2", "D3", "D4", "D5", "D6", "D8"],
    "D8": ["D1", "D2", "D3", "D4", "D5", "D6", "D7"],

    "E1": ["E2", "E3", "E4", "E5", "E6", "E7", "E8"],
    "E2": ["E1", "E3", "E4", "E5", "E6", "E7", "E8"],
    "E3": ["E1", "E2", "E4", "E5", "E6", "E7", "E8"],
    "E4": ["E1", "E2", "E3", "E5", "E6", "E7", "E8"],
    "E5": ["E1", "E2", "E3", "E4", "E6", "E7", "E8"],
    "E6": ["E1", "E2", "E3", "E4", "E5", "E7", "E8"],
    "E7": ["E1", "E2", "E3", "E4", "E5", "E6", "E8"],
    "E8": ["E1", "E2", "E3", "E4", "E5", "E6", "E7"],

    "F1": ["F2", "F3", "F4", "F5", "F6", "F7", "F8"],
    "F2": ["F1", "F3", "F4", "F5", "F6", "F7", "F8"],
    "F3": ["F1", "F2", "F4", "F5", "F6", "F7", "F8"],
    "F4": ["F1", "F2", "F3", "F5", "F6", "F7", "F8"],
    "F5": ["F1", "F2", "F3", "F4", "F6", "F7", "F8"],
    "F6": ["F1", "F2", "F3", "F4", "F5", "F7", "F8"],
    "F7": ["F1", "F2", "F3", "F4", "F5", "F6", "F8"],
    "F8": ["F1", "F2", "F3", "F4", "F5", "F6", "F7"],

    "G1": ["G2", "G3", "G4", "G5", "G6", "G7", "G8"],
    "G2": ["G1", "G3", "G4", "G5", "G6", "G7", "G8"],
    "G3": ["G1", "G2", "G4", "G5", "G6", "G7", "G8"],
    "G4": ["G1", "G2", "G3", "G5", "G6", "G7", "G8"],
    "G5": ["G1", "G2", "G3", "G4", "G6", "G7", "G8"],
    "G6": ["G1", "G2", "G3", "G4", "G5", "G7", "G8"],
    "G7": ["G1", "G2", "G3", "G4", "G5", "G6", "G8"],
    "G8": ["G1", "G2", "G3", "G4", "G5", "G6", "G7"],

    "H1": ["H2", "H3", "H4", "H5", "H6", "H7", "H8"],
    "H2": ["H1", "H3", "H4", "H5", "H6", "H7", "H8"],
    "H3": ["H1", "H2", "H4", "H5", "H6", "H7", "H8"],
    "H4": ["H1", "H2", "H3", "H5", "H6", "H7", "H8"],
    "H5": ["H1", "H2", "H3", "H4", "H6", "H7", "H8"],
    "H6": ["H1", "H2", "H3", "H4", "H5", "H7", "H8"],
    "H7": ["H1", "H2", "H3", "H4", "H5", "H6", "H8"],
    "H8": ["H1", "H2", "H3", "H4", "H5", "H6", "H7"]
}

ranks = {
    "A1": ["B1", "C1", "D1", "E1", "F1", "G1", "H1"],
    "B1": ["A1", "C1", "D1", "E1", "F1", "G1", "H1"],
    "C1": ["A1", "B1", "D1", "E1", "F1", "G1", "H1"],
    "D1": ["A1", "B1", "C1", "E1", "F1", "G1", "H1"],
    "E1": ["A1", "B1", "C1", "D1", "F1", "G1", "H1"],
    "F1": ["A1", "B1", "C1", "D1", "E1", "G1", "H1"],
    "G1": ["A1", "B1", "C1", "D1", "E1", "F1", "H1"],
    "H1": ["A1", "B1", "C1", "D1", "E1", "F1", "G1"],

    "A2": ["B2", "C2", "D2", "E2", "F2", "G2", "H2"],
    "B2": ["A2", "C2", "D2", "E2", "F2", "G2", "H2"],
    "C2": ["A2", "B2", "D2", "E2", "F2", "G2", "H2"],
    "D2": ["A2", "B2", "C2", "E2", "F2", "G2", "H2"],
    "E2": ["A2", "B2", "C2", "D2", "F2", "G2", "H2"],
    "F2": ["A2", "B2", "C2", "D2", "E2", "G2", "H2"],
    "G2": ["A2", "B2", "C2", "D2", "E2", "F2", "H2"],
    "H2": ["A2", "B2", "C2", "D2", "E2", "F2", "G2"],

    "A3": ["B3", "C3", "D3", "E3", "F3", "G3", "H3"],
    "B3": ["A3", "C3", "D3", "E3", "F3", "G3", "H3"],
    "C3": ["A3", "B3", "D3", "E3", "F3", "G3", "H3"],
    "D3": ["A3", "B3", "C3", "E3", "F3", "G3", "H3"],
    "E3": ["A3", "B3", "C3", "D3", "F3", "G3", "H3"],
    "F3": ["A3", "B3", "C3", "D3", "E3", "G3", "H3"],
    "G3": ["A3", "B3", "C3", "D3", "E3", "F3", "H3"],
    "H3": ["A3", "B3", "C3", "D3", "E3", "F3", "G3"],

    "A4": ["B4", "C4", "D4", "E4", "F4", "G4", "H4"],
    "B4": ["A4", "C4", "D4", "E4", "F4", "G4", "H4"],
    "C4": ["A4", "B4", "D4", "E4", "F4", "G4", "H4"],
    "D4": ["A4", "B4", "C4", "E4", "F4", "G4", "H4"],
    "E4": ["A4", "B4", "C4", "D4", "F4", "G4", "H4"],
    "F4": ["A4", "B4", "C4", "D4", "E4", "G4", "H4"],
    "G4": ["A4", "B4", "C4", "D4", "E4", "F4", "H4"],
    "H4": ["A4", "B4", "C4", "D4", "E4", "F4", "G4"],

    "A5": ["B5", "C5", "D5", "E5", "F5", "G5", "H5"],
    "B5": ["A5", "C5", "D5", "E5", "F5", "G5", "H5"],
    "C5": ["A5", "B5", "D5", "E5", "F5", "G5", "H5"],
    "D5": ["A5", "B5", "C5", "E5", "F5", "G5", "H5"],
    "E5": ["A5", "B5", "C5", "D5", "F5", "G5", "H5"],
    "F5": ["A5", "B5", "C5", "D5", "E5", "G5", "H5"],
    "G5": ["A5", "B5", "C5", "D5", "E5", "F5", "H5"],
    "H5": ["A5", "B5", "C5", "D5", "E5", "F5", "G5"],

    "A6": ["B6", "C6", "D6", "E6", "F6", "G6", "H6"],
    "B6": ["A6", "C6", "D6", "E6", "F6", "G6", "H6"],
    "C6": ["A6", "B6", "D6", "E6", "F6", "G6", "H6"],
    "D6": ["A6", "B6", "C6", "E6", "F6", "G6", "H6"],
    "E6": ["A6", "B6", "C6", "D6", "F6", "G6", "H6"],
    "F6": ["A6", "B6", "C6", "D6", "E6", "G6", "H6"],
    "G6": ["A6", "B6", "C6", "D6", "E6", "F6", "H6"],
    "H6": ["A6", "B6", "C6", "D6", "E6", "F6", "G6"],

    "A7": ["B7", "C7", "D7", "E7", "F7", "G7", "H7"],
    "B7": ["A7", "C7", "D7", "E7", "F7", "G7", "H7"],
    "C7": ["A7", "B7", "D7", "E7", "F7", "G7", "H7"],
    "D7": ["A7", "B7", "C7", "E7", "F7", "G7", "H7"],
    "E7": ["A7", "B7", "C7", "D7", "F7", "G7", "H7"],
    "F7": ["A7", "B7", "C7", "D7", "E7", "G7", "H7"],
    "G7": ["A7", "B7", "C7", "D7", "E7", "F7", "H7"],
    "H7": ["A7", "B7", "C7", "D7", "E7", "F7", "G7"],

    "A8": ["B8", "C8", "D8", "E8", "F8", "G8", "H8"],
    "B8": ["A8", "C8", "D8", "E8", "F8", "G8", "H8"],
    "C8": ["A8", "B8", "D8", "E8", "F8", "G8", "H8"],
    "D8": ["A8", "B8", "C8", "E8", "F8", "G8", "H8"],
    "E8": ["A8", "B8", "C8", "D8", "F8", "G8", "H8"],
    "F8": ["A8", "B8", "C8", "D8", "E8", "G8", "H8"],
    "G8": ["A8", "B8", "C8", "D8", "E8", "F8", "H8"],
    "H8": ["A8", "B8", "C8", "D8", "E8", "F8", "G8"]
}

diagonals =     {
    "A1": ['B2', 'C3', 'D4', 'E5', 'F6', 'G7', 'H8'],
    "A2": ['B1', 'B3', 'C4', 'D5', 'E6', 'F7', 'G8'],
    "A3": ['B2', 'C1', 'B4', 'C5', 'D6', 'E7', 'F8'],
    "A4": ['B3', 'C2', 'D1', 'B5', 'C6', 'D7', 'E8'],
    "A5": ['B4', 'C3', 'D2', 'E1', 'B6', 'C7', 'D8'],
    "A6": ['B5', 'C4', 'D3', 'E2', 'F1', 'B7', 'C8'],
    "A7": ['B6', 'C5', 'D4', 'E3', 'F2', 'G1', 'B8'],
    "A8": ['B7', 'C6', 'D5', 'E4', 'F3', 'G2', 'H1'],
    "B1": ['A2', 'C2', 'D3', 'E4', 'F5', 'G6', 'H7'],
    "B2": ['A1', 'C1', 'A3', 'C3', 'D4', 'E5', 'F6', 'G7', 'H8'],
    "B3": ['A2', 'C2', 'D1', 'A4', 'C4', 'D5', 'E6', 'F7', 'G8'],
    "B4": ['A3', 'C3', 'D2', 'E1', 'A5', 'C5', 'D6', 'E7', 'F8'],
    "B5": ['A4', 'C4', 'D3', 'E2', 'F1', 'A6', 'C6', 'D7', 'E8'],
    "B6": ['A5', 'C5', 'D4', 'E3', 'F2', 'G1', 'A7', 'C7', 'D8'],
    "B7": ['A6', 'C6', 'D5', 'E4', 'F3', 'G2', 'H1', 'A8', 'C8'],
    "B8": ['A7', 'C7', 'D6', 'E5', 'F4', 'G3', 'H2'],
    "C1": ['B2', 'A3', 'D2', 'E3', 'F4', 'G5', 'H6'],
    "C2": ['B1', 'D1', 'B3', 'A4', 'D3', 'E4', 'F5', 'G6', 'H7'],
    "C3": ['B2', 'A1', 'D2', 'E1', 'B4', 'A5', 'D4', 'E5', 'F6', 'G7', 'H8'],
    "C4": ['B3', 'A2', 'D3', 'E2', 'F1', 'B5', 'A6', 'D5', 'E6', 'F7', 'G8'],
    "C5": ['B4', 'A3', 'D4', 'E3', 'F2', 'G1', 'B6', 'A7', 'D6', 'E7', 'F8'],
    "C6": ['B5', 'A4', 'D5', 'E4', 'F3', 'G2', 'H1', 'B7', 'A8', 'D7', 'E8'],
    "C7": ['B6', 'A5', 'D6', 'E5', 'F4', 'G3', 'H2', 'B8', 'D8'],
    "C8": ['B7', 'A6', 'D7', 'E6', 'F5', 'G4', 'H3'],
    "D1": ['C2', 'B3', 'A4', 'E2', 'F3', 'G4', 'H5'],
    "D2": ['C1', 'E1', 'C3', 'B4', 'A5', 'E3', 'F4', 'G5', 'H6'],
    "D3": ['C2', 'B1', 'E2', 'F1', 'C4', 'B5', 'A6', 'E4', 'F5', 'G6', 'H7'],
    "D4": ['C3', 'B2', 'A1', 'E3', 'F2', 'G1', 'C5', 'B6', 'A7', 'E5', 'F6', 'G7', 'H8'],
    "D5": ['C4', 'B3', 'A2', 'E4', 'F3', 'G2', 'H1', 'C6', 'B7', 'A8', 'E6', 'F7', 'G8'],
    "D6": ['C5', 'B4', 'A3', 'E5', 'F4', 'G3', 'H2', 'C7', 'B8', 'E7', 'F8'],
    "D7": ['C6', 'B5', 'A4', 'E6', 'F5', 'G4', 'H3', 'C8', 'E8'],
    "D8": ['C7', 'B6', 'A5', 'E7', 'F6', 'G5', 'H4'],
    "E1": ['D2', 'C3', 'B4', 'A5', 'F2', 'G3', 'H4'],
    "E2": ['D1', 'F1', 'D3', 'C4', 'B5', 'A6', 'F3', 'G4', 'H5'],
    "E3": ['D2', 'C1', 'F2', 'G1', 'D4', 'C5', 'B6', 'A7', 'F4', 'G5', 'H6'],
    "E4": ['D3', 'C2', 'B1', 'F3', 'G2', 'H1', 'D5', 'C6', 'B7', 'A8', 'F5', 'G6', 'H7'],
    "E5": ['D4', 'C3', 'B2', 'A1', 'F4', 'G3', 'H2', 'D6', 'C7', 'B8', 'F6', 'G7', 'H8'],
    "E6": ['D5', 'C4', 'B3', 'A2', 'F5', 'G4', 'H3', 'D7', 'C8', 'F7', 'G8'],
    "E7": ['D6', 'C5', 'B4', 'A3', 'F6', 'G5', 'H4', 'D8', 'F8'],
    "E8": ['D7', 'C6', 'B5', 'A4', 'F7', 'G6', 'H5'],
    "F1": ['E2', 'D3', 'C4', 'B5', 'A6', 'G2', 'H3'],
    "F2": ['E1', 'G1', 'E3', 'D4', 'C5', 'B6', 'A7', 'G3', 'H4'],
    "F3": ['E2', 'D1', 'G2', 'H1', 'E4', 'D5', 'C6', 'B7', 'A8', 'G4', 'H5'],
    "F4": ['E3', 'D2', 'C1', 'G3', 'H2', 'E5', 'D6', 'C7', 'B8', 'G5', 'H6'],
    "F5": ['E4', 'D3', 'C2', 'B1', 'G4', 'H3', 'E6', 'D7', 'C8', 'G6', 'H7'],
    "F6": ['E5', 'D4', 'C3', 'B2', 'A1', 'G5', 'H4', 'E7', 'D8', 'G7', 'H8'],
    "F7": ['E6', 'D5', 'C4', 'B3', 'A2', 'G6', 'H5', 'E8', 'G8'],
    "F8": ['E7', 'D6', 'C5', 'B4', 'A3', 'G7', 'H6'],
    "G1": ['F2', 'E3', 'D4', 'C5', 'B6', 'A7', 'H2'],
    "G2": ['F1', 'H1', 'F3', 'E4', 'D5', 'C6', 'B7', 'A8', 'H3'],
    "G3": ['F2', 'E1', 'H2', 'F4', 'E5', 'D6', 'C7', 'B8', 'H4'],
    "G4": ['F3', 'E2', 'D1', 'H3', 'F5', 'E6', 'D7', 'C8', 'H5'],
    "G5": ['F4', 'E3', 'D2', 'C1', 'H4', 'F6', 'E7', 'D8', 'H6'],
    "G6": ['F5', 'E4', 'D3', 'C2', 'B1', 'H5', 'F7', 'E8', 'H7'],
    "G7": ['F6', 'E5', 'D4', 'C3', 'B2', 'A1', 'H6', 'F8', 'H8'],
    "G8": ['F7', 'E6', 'D5', 'C4', 'B3', 'A2', 'H7'],
    "H1": ['G2', 'F3', 'E4', 'D5', 'C6', 'B7', 'A8'],
    "H2": ['G1', 'G3', 'F4', 'E5', 'D6', 'C7', 'B8'],
    "H3": ['G2', 'F1', 'G4', 'F5', 'E6', 'D7', 'C8'],
    "H4": ['G3', 'F2', 'E1', 'G5', 'F6', 'E7', 'D8'],
    "H5": ['G4', 'F3', 'E2', 'D1', 'G6', 'F7', 'E8'],
    "H6": ['G5', 'F4', 'E3', 'D2', 'C1', 'G7', 'F8'],
    "H7": ['G6', 'F5', 'E4', 'D3', 'C2', 'B1', 'G8'],
    "H8": ['G7', 'F6', 'E5', 'D4', 'C3', 'B2', 'A1'],
    }

# Mock piece class to represent other pieces on the board
class MockPiece:
    def __init__(self, colour, occupied_square=None):
        self.colour = colour
        self.occupied_square = occupied_square




# --------------------------------------- Test Queen ----------------------------------------------

def test_queen_initialization():
    queen = c.Queen('white', 'D4')
    assert queen.occupied_square == 'D4'
    assert queen.colour == 'white'
    assert queen.type == 'queen'
    assert queen.legal_moves == []
    assert queen.capture_squares == []
    assert queen.under_attack == []

def test_queen_repr():
    queen = c.Queen('black', 'E5')
    assert repr(queen) == 'E5 black queen'

def test_queen_get_visible_squares():
    queen = c.Queen('white', 'D4')
    expected_squares = set()
    expected_squares.update(ranks['D4'])
    expected_squares.update(files['D4'])
    expected_squares.update(diagonals['D4'])
    visible_squares = set(queen.get_visible_squares())
    assert visible_squares == expected_squares

def test_queen_get_legal_moves_empty_board():
    queen = c.Queen('white', 'D4')
    conflict_sqrs = []  # No other pieces on the board
    position = {}       # Empty board
    legal_moves = queen.get_legal_moves(conflict_sqrs, position)
    expected_moves = set()
    # Queen can move any number of squares in any direction until the edge
    # Collect all squares in ranks, files, and diagonals
    expected_moves.update(ranks['D4'])
    expected_moves.update(files['D4'])
    expected_moves.update(diagonals['D4'])
    assert set(legal_moves) == expected_moves

def test_queen_get_legal_moves_with_blocking_pieces():
    queen = c.Queen('white', 'D4')
    # Place some blocking pieces
    conflict_sqrs = ['D6', 'F4', 'B2']
    position = {
        'D6': MockPiece('white'),  # Friendly piece
        'F4': MockPiece('black'),  # Opponent's piece
        'B2': MockPiece('black'),  # Opponent's piece
    }
    legal_moves = queen.get_legal_moves(conflict_sqrs, position)
    # Expected moves: up to D5 (D6 is blocked by friendly piece)
    expected_moves = [
        'D5',
        # Right direction: E4, capture F4
        'E4',
        'F4',  # Can capture
        # Left-down diagonal: C3, B2 (can capture)
        'C3',
        'B2',  # Can capture
        # Other directions without blockage
        'E5', 'F6', 'G7', 'H8',
        'C4', 'B4', 'A4',
        'D3', 'D2', 'D1',
        'E3', 'F2', 'G1',
        'C5', 'B6', 'A7',
    ]
    assert set(legal_moves) == set(expected_moves)

def test_queen_legal_moves_blocked_check():
    queen = c.Queen('white', 'H5')
    # Place some blocking pieces
    conflict_sqrs = ['H7', 'H2', 'F7']
    position = {
        'H5': queen,  
        'H7': MockPiece('black'),  # Opponent's piece
        'F7': MockPiece('black'),  # Opponent's piece
        'H2': MockPiece('white')   # Friendly piece
    }
    legal_moves = queen.get_legal_moves(conflict_sqrs, position)
    # Expected moves: up to D5 (D6 is blocked by friendly piece)
    expected_moves = [
        'H6', 'H7',  # Up
        'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5',  # left
        'H4', 'H3',  # Down
        'D1', 'E2', 'F3', 'G4',  # Down-Left
        'G6', 'F7'    # Up-Left
    ]
    assert set(legal_moves) == set(expected_moves)


def test_queen_get_legal_moves_at_edge():
    queen = c.Queen('white', 'A1')
    conflict_sqrs = []
    position = {}
    legal_moves = queen.get_legal_moves(conflict_sqrs, position)
    expected_moves = [
        # Up the file
        'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8',
        # Right along the rank
        'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1',
        # Up-right diagonal
        'B2', 'C3', 'D4', 'E5', 'F6', 'G7', 'H8',
    ]
    assert set(legal_moves) == set(expected_moves)

def test_queen_get_legal_moves_surrounded():
    queen = c.Queen('white', 'D4')
    conflict_sqrs = ['D5', 'E5', 'E4', 'E3', 'D3', 'C3', 'C4', 'C5']
    position = {sqr: MockPiece('white') for sqr in conflict_sqrs}
    legal_moves = queen.get_legal_moves(conflict_sqrs, position)
    # Queen should have no legal moves as all directions are blocked by friendly pieces
    assert legal_moves == []

def test_queen_capture_only_opponent_pieces():
    queen = c.Queen('white', 'D4')
    conflict_sqrs = ['D5', 'E5', 'E4', 'E3', 'D3', 'C3', 'C4', 'C5']
    position = {
        'D5': MockPiece('black'),
        'E5': MockPiece('black'),
        'E4': MockPiece('black'),
        'E3': MockPiece('black'),
        'D3': MockPiece('black'),
        'C3': MockPiece('black'),
        'C4': MockPiece('black'),
        'C5': MockPiece('black'),
    }
    legal_moves = queen.get_legal_moves(conflict_sqrs, position)
    # Queen can capture each opponent piece but cannot move beyond
    expected_moves = conflict_sqrs
    assert set(legal_moves) == set(expected_moves)

# ------------------------------------ Test Pawn ----------------------------------------------------

def test_pawn_initialization():
    pawn = c.Pawn('white', 'E2')
    assert pawn.occupied_square == 'E2'
    assert pawn.colour == 'white'
    assert pawn.type == 'pawn'
    assert pawn.moves == 0
    assert pawn.capture_squares == []
    assert pawn.under_attack == []
    assert pawn.legal_moves == []

def test_pawn_repr():
    pawn = c.Pawn('black', 'D7')
    assert repr(pawn) == 'D7 black pawn'

def test_pawn_get_visible_squares_white_pawn_initial_position():
    pawn = c.Pawn('white', 'E2')
    expected_squares = ['E3', 'E4', 'D3', 'F3']
    visible_squares = pawn.get_visible_squares()
    assert set(visible_squares) == set(expected_squares)

def test_pawn_get_visible_squares_black_pawn_initial_position():
    pawn = c.Pawn('black', 'D7')
    expected_squares = ['D6', 'D5', 'C6', 'E6']
    visible_squares = pawn.get_visible_squares()
    assert set(visible_squares) == set(expected_squares)

def test_pawn_get_legal_moves_white_pawn_empty_board():
    pawn = c.Pawn('white', 'E2')
    position = {}  # Empty board
    en_passant = None
    legal_moves = pawn.get_legal_moves(position, en_passant)
    expected_moves = ['E3', 'E4']
    assert set(legal_moves) == set(expected_moves)

def test_pawn_get_legal_moves_black_pawn_empty_board():
    pawn = c.Pawn('black', 'D7')
    position = {}
    en_passant = None
    legal_moves = pawn.get_legal_moves(position, en_passant)
    expected_moves = ['D6', 'D5']
    assert set(legal_moves) == set(expected_moves)

def test_pawn_get_legal_moves_with_blocking_pieces():
    pawn = c.Pawn('white', 'E2')
    # Blocking piece directly ahead
    position = {
        'E3': MockPiece('white', 'E3')
    }
    en_passant = None
    legal_moves = pawn.get_legal_moves(position, en_passant)
    expected_moves = []  # Cannot move forward
    assert legal_moves == expected_moves

def test_pawn_get_legal_moves_with_opponent_in_front():
    pawn = c.Pawn('white', 'E2')
    # Opponent piece directly ahead
    position = {
        'E3': MockPiece('black', 'E3')
    }
    en_passant = None
    legal_moves = pawn.get_legal_moves(position, en_passant)
    expected_moves = []  # Cannot capture forward
    assert legal_moves == expected_moves

def test_pawn_get_legal_moves_with_capture():
    pawn = c.Pawn('white', 'E4')
    position = {
        'D5': MockPiece('black', 'D5'),
        'F5': MockPiece('black', 'F5')
    }
    en_passant = None
    legal_moves = ['E5', 'D5', 'F5']
    assert set(pawn.get_legal_moves(position, en_passant)) == set(legal_moves)

def test_pawn_get_legal_moves_with_friendly_pieces_diagonal():
    pawn = c.Pawn('white', 'E4')
    position = {
        'D5': MockPiece('white', 'D5'),
        'F5': MockPiece('white', 'F5')
    }
    en_passant = None
    legal_moves = ['E5']  # Cannot capture friendly pieces
    assert set(pawn.get_legal_moves(position, en_passant)) == set(legal_moves)

def test_pawn_get_legal_moves_with_en_passant():
    pawn = c.Pawn('white', 'E5')
    position = {
        'D5': MockPiece('black', 'D5'),
        'F5': MockPiece('black', 'F5')
    }
    en_passant = 'D6'  # Assume black pawn moved from D7 to D5 in previous move
    legal_moves = pawn.get_legal_moves(position, en_passant)
    expected_moves = ['E6', 'D6']
    assert set(legal_moves) == set(expected_moves)

def test_pawn_get_legal_moves_promotion():
    pawn = c.Pawn('white', 'E7')
    position = {}
    en_passant = None
    legal_moves = pawn.get_legal_moves(position, en_passant)
    expected_moves = ['E8']
    assert set(legal_moves) == set(expected_moves)

def test_pawn_get_legal_moves_promotion_with_capture():
    pawn = c.Pawn('white', 'E7')
    position = {
        'D8': MockPiece('black', 'D8'),
        'F8': MockPiece('black', 'F8')
    }
    en_passant = None
    legal_moves = pawn.get_legal_moves(position, en_passant)
    expected_moves = ['E8', 'D8', 'F8']
    assert set(legal_moves) == set(expected_moves)

# ------------------------------------------ Test Knight -----------------------------------------------

def test_knight_initialization():
    knight = c.Knight('white', 'B1')
    assert knight.occupied_square == 'B1'
    assert knight.colour == 'white'
    assert knight.type == 'knight'
    assert knight.capture_squares == []
    assert knight.under_attack == []
    assert knight.legal_moves == []

def test_knight_repr():
    knight = c.Knight('black', 'G8')
    assert repr(knight) == 'G8 black knight'

def test_knight_get_visible_squares_center():
    knight = c.Knight('white', 'D4')
    expected_squares = ['E6', 'F5', 'F3', 'E2', 'C2', 'B3', 'B5', 'C6']
    visible_squares = knight.get_visible_squares()
    assert set(visible_squares) == set(expected_squares)

def test_knight_get_visible_squares_corner():
    knight = c.Knight('white', 'A1')
    expected_squares = ['B3', 'C2']
    visible_squares = knight.get_visible_squares()
    assert set(visible_squares) == set(expected_squares)

def test_knight_get_legal_moves_empty_board():
    knight = c.Knight('white', 'D4')
    conflict_sqrs = []  # No other pieces on the board
    position = {}
    legal_moves = knight.get_legal_moves(conflict_sqrs, position)
    expected_moves = ['E6', 'F5', 'F3', 'E2', 'C2', 'B3', 'B5', 'C6']
    assert set(legal_moves) == set(expected_moves)

def test_knight_get_legal_moves_with_friendly_pieces():
    knight = c.Knight('white', 'D4')
    conflict_sqrs = ['E6', 'F5']
    position = {
        'E6': MockPiece('white', 'E6'),
        'F5': MockPiece('white', 'F5'),
    }
    legal_moves = knight.get_legal_moves(conflict_sqrs, position)
    expected_moves = ['F3', 'E2', 'C2', 'B3', 'B5', 'C6']
    assert set(legal_moves) == set(expected_moves)

def test_knight_get_legal_moves_with_opponent_pieces():
    knight = c.Knight('white', 'D4')
    conflict_sqrs = ['E6', 'F5']
    position = {
        'E6': MockPiece('black', 'E6'),
        'F5': MockPiece('black', 'F5'),
    }
    legal_moves = knight.get_legal_moves(conflict_sqrs, position)
    expected_moves = ['E6', 'F5', 'F3', 'E2', 'C2', 'B3', 'B5', 'C6']
    assert set(legal_moves) == set(expected_moves)

def test_knight_get_legal_moves_mixed_pieces():
    knight = c.Knight('white', 'D4')
    conflict_sqrs = ['E6', 'F5', 'C2']
    position = {
        'E6': MockPiece('black', 'E6'),
        'F5': MockPiece('white', 'F5'),
        'C2': MockPiece('black', 'C2'),
    }
    legal_moves = knight.get_legal_moves(conflict_sqrs, position)
    expected_moves = ['E6', 'F3', 'E2', 'C2', 'B3', 'B5', 'C6']
    assert set(legal_moves) == set(expected_moves)

def test_knight_get_legal_moves_at_edge():
    knight = c.Knight('black', 'H8')
    conflict_sqrs = []
    position = {}
    legal_moves = knight.get_legal_moves(conflict_sqrs, position)
    expected_moves = ['F7', 'G6']
    assert set(legal_moves) == set(expected_moves)

def test_knight_get_legal_moves_blocked_by_friendly_pieces():
    knight = c.Knight('black', 'D5')
    conflict_sqrs = ['E7', 'F6', 'F4', 'E3', 'C3', 'B4', 'B6', 'C7']
    position = {square: MockPiece('black', square) for square in conflict_sqrs}
    legal_moves = knight.get_legal_moves(conflict_sqrs, position)
    expected_moves = []
    assert legal_moves == expected_moves

def test_knight_get_legal_moves_blocked_by_opponent_pieces():
    knight = c.Knight('black', 'D5')
    conflict_sqrs = ['E7', 'F6', 'F4', 'E3', 'C3', 'B4', 'B6', 'C7']
    position = {square: MockPiece('white', square) for square in conflict_sqrs}
    legal_moves = knight.get_legal_moves(conflict_sqrs, position)
    expected_moves = conflict_sqrs
    assert set(legal_moves) == set(expected_moves)

# -------------------------------- Test Rook --------------------------------------------------------

# Patch the Rook class to use the mocked ranks and files
def patched_get_visible_squares(self):
    list_of_squares = []
    for square in ranks.get(self.occupied_square, []):
        list_of_squares.append(square)
    for square in files.get(self.occupied_square, []):
        list_of_squares.append(square)
    return list_of_squares

c.Rook.get_visible_squares = patched_get_visible_squares

def test_rook_initialization():
    rook = c.Rook('white', 'A1')
    assert rook.occupied_square == 'A1'
    assert rook.colour == 'white'
    assert rook.type == 'rook'
    assert rook.capture_squares == []
    assert rook.under_attack == []
    assert rook.legal_moves == []

def test_rook_repr():
    rook = c.Rook('black', 'H8')
    assert repr(rook) == 'H8 black rook'

def test_rook_get_visible_squares():
    rook = c.Rook('white', 'D4')
    expected_squares = [
        'A4', 'B4', 'C4', 'E4', 'F4', 'G4', 'H4',
        'D1', 'D2', 'D3', 'D5', 'D6', 'D7', 'D8'
    ]
    visible_squares = rook.get_visible_squares()
    assert set(visible_squares) == set(expected_squares)

def test_rook_get_legal_moves_empty_board():
    rook = c.Rook('white', 'D4')
    conflict_sqrs = []
    position = {}
    legal_moves = rook.get_legal_moves(conflict_sqrs, position)
    expected_moves = [
        'A4', 'B4', 'C4', 'E4', 'F4', 'G4', 'H4',
        'D1', 'D2', 'D3', 'D5', 'D6', 'D7', 'D8'
    ]
    assert set(legal_moves) == set(expected_moves)

def test_rook_get_legal_moves_with_blocking_pieces():
    rook = c.Rook('white', 'D4')
    conflict_sqrs = ['F4', 'D6', 'B4', 'D2']
    position = {
        'F4': MockPiece('black', 'F4'),  # Opponent's piece
        'D6': MockPiece('white', 'D6'),  # Friendly piece
        'B4': MockPiece('black', 'B4'),  # Opponent's piece
        'D2': MockPiece('white', 'D2'),  # Friendly piece
    }
    legal_moves = rook.get_legal_moves(conflict_sqrs, position)
    expected_moves = [
        'E4', 'F4',  # Can capture F4
        'C4', 'B4',  # Can capture B4
        'D5',        # Can move to D5; D6 is blocked
        'D3',        # Can move to D3; D2 is blocked
    ]
    assert set(legal_moves) == set(expected_moves)

def test_rook_get_legal_moves_at_edge():
    rook = c.Rook('white', 'A1')
    conflict_sqrs = []
    position = {}
    legal_moves = rook.get_legal_moves(conflict_sqrs, position)
    expected_moves = [
        'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1',
        'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8'
    ]
    assert set(legal_moves) == set(expected_moves)

def test_rook_get_legal_moves_blocked_all_directions():
    rook = c.Rook('white', 'D4')
    conflict_sqrs = ['C4', 'E4', 'D3', 'D5']
    position = {
        'C4': MockPiece('white', 'C4'),
        'E4': MockPiece('white', 'E4'),
        'D3': MockPiece('white', 'D3'),
        'D5': MockPiece('white', 'D5'),
    }
    legal_moves = rook.get_legal_moves(conflict_sqrs, position)
    expected_moves = []  # All directions blocked by friendly pieces
    assert legal_moves == expected_moves

def test_rook_get_legal_moves_capture_opponent_pieces():
    rook = c.Rook('white', 'D4')
    conflict_sqrs = ['C4', 'E4', 'D3', 'D5']
    position = {
        'C4': MockPiece('black', 'C4'),
        'E4': MockPiece('black', 'E4'),
        'D3': MockPiece('black', 'D3'),
        'D5': MockPiece('black', 'D5'),
    }
    legal_moves = rook.get_legal_moves(conflict_sqrs, position)
    expected_moves = ['C4', 'E4', 'D3', 'D5']
    assert set(legal_moves) == set(expected_moves)

# ----------------------------- Test Bishop ---------------------------------------

def test_bishop_initialization():
    bishop = c.Bishop('white', 'C1')
    assert bishop.occupied_square == 'C1'
    assert bishop.colour == 'white'
    assert bishop.type == 'bishop'
    assert bishop.capture_squares == []
    assert bishop.under_attack == []
    assert bishop.legal_moves == []

def test_bishop_repr():
    bishop = c.Bishop('black', 'F8')
    assert repr(bishop) == 'F8 black bishop'

def test_bishop_get_legal_moves_empty_board():
    bishop = c.Bishop('white', 'D4')
    conflict_sqrs = []
    position = {}
    legal_moves = bishop.get_legal_moves(conflict_sqrs, position)
    expected_moves = bishop.visible_squares
    assert set(legal_moves) == set(expected_moves)

def test_bishop_get_legal_moves_with_blocking_pieces():
    bishop = c.Bishop('white', 'D4')
    conflict_sqrs = ['F6', 'B6', 'F2', 'B2']
    position = {
        'F6': MockPiece('white', 'F6'),  # Friendly piece
        'B6': MockPiece('black', 'B6'),  # Opponent's piece
        'F2': MockPiece('black', 'F2'),  # Opponent's piece
        'B2': MockPiece('white', 'B2'),  # Friendly piece
    }
    legal_moves = bishop.get_legal_moves(conflict_sqrs, position)
    expected_moves = [
        'E5',          # Can move until before F6
        'E3', 'F2',    # Can capture F2 but cannot move beyond
        'C5', 'B6',    # Can capture B6 but cannot move beyond
        'C3'           # Cannot move to B2 (blocked by friendly piece)
    ]
    assert set(legal_moves) == set(expected_moves)

def test_bishop_get_legal_moves_at_corner():
    bishop = c.Bishop('white', 'A1')
    conflict_sqrs = []
    position = {}
    legal_moves = bishop.get_legal_moves(conflict_sqrs, position)
    expected_moves = ['B2', 'C3', 'D4', 'E5', 'F6', 'G7', 'H8']
    assert set(legal_moves) == set(expected_moves)

def test_bishop_get_legal_moves_blocked_all_directions():
    bishop = c.Bishop('white', 'D4')
    conflict_sqrs = ['E5', 'E3', 'C5', 'C3']
    position = {
        'E5': MockPiece('white', 'E5'),
        'E3': MockPiece('white', 'E3'),
        'C5': MockPiece('white', 'C5'),
        'C3': MockPiece('white', 'C3'),
    }
    legal_moves = bishop.get_legal_moves(conflict_sqrs, position)
    expected_moves = []  # All directions blocked by friendly pieces
    assert legal_moves == expected_moves

def test_bishop_get_legal_moves_capture_opponent_pieces():
    bishop = c.Bishop('white', 'D4')
    conflict_sqrs = ['E5', 'E3', 'C5', 'C3']
    position = {
        'E5': MockPiece('black', 'E5'),
        'E3': MockPiece('black', 'E3'),
        'C5': MockPiece('black', 'C5'),
        'C3': MockPiece('black', 'C3'),
    }
    legal_moves = bishop.get_legal_moves(conflict_sqrs, position)
    expected_moves = ['E5', 'E3', 'C5', 'C3']
    assert set(legal_moves) == set(expected_moves)

# ------------------------- Test King -------------------------------------------

def test_king_initialization():
    king = c.King('white', 'E1')
    assert king.occupied_square == 'E1'
    assert king.colour == 'white'
    assert king.type == 'king'
    assert king.capture_squares == []
    assert king.under_attack == []
    assert king.legal_moves == []

def test_king_repr():
    king = c.King('black', 'E8')
    assert repr(king) == 'E8 black king'

def test_king_get_visible_squares_center():
    king = c.King('white', 'D4')
    expected_squares = ['E4', 'E5', 'D5', 'C5', 'C4', 'C3', 'D3', 'E3']
    visible_squares = king.get_visible_squares()
    assert set(visible_squares) == set(expected_squares)

def test_king_get_visible_squares_corner():
    king = c.King('white', 'A1')
    expected_squares = ['A2', 'B2', 'B1']
    visible_squares = king.get_visible_squares()
    assert set(visible_squares) == set(expected_squares)

def test_king_get_legal_moves_empty_board():
    king = c.King('white', 'E1')
    conflict_sqrs = []
    position = {}
    legal_moves = king.get_legal_moves(conflict_sqrs, position)
    expected_moves = king.get_visible_squares()
    assert set(legal_moves) == set(expected_moves)

def test_king_get_legal_moves_with_friendly_pieces():
    king = c.King('white', 'D4')
    conflict_sqrs = ['E4', 'D5']
    position = {
        'E4': MockPiece('white', 'E4'),
        'D5': MockPiece('white', 'D5'),
    }
    legal_moves = king.get_legal_moves(conflict_sqrs, position)
    expected_moves = ['C5', 'E5', 'C4', 'C3', 'D3', 'E3']  
    # Excludes squares with friendly pieces
    
    assert set(legal_moves) == set(expected_moves)

def test_king_get_legal_moves_with_opponent_pieces():
    king = c.King('white', 'D4')
    conflict_sqrs = ['E4', 'D5']
    position = {
        'E4': MockPiece('black', 'E4'),
        'D5': MockPiece('black', 'D5'),
    }
    legal_moves = king.get_legal_moves(conflict_sqrs, position)
    expected_moves = ['C5', 'D5', 'E5', 'C4', 'E4', 'C3', 'D3', 'E3']
    assert set(legal_moves) == set(expected_moves)

def test_king_get_legal_moves_blocked_all_sides():
    king = c.King('white', 'D4')
    conflict_sqrs = ['E4', 'D5', 'C4', 'C3', 'D3', 'E3', 'C5', 'E5']
    position = {square: MockPiece('white', square) for square in conflict_sqrs}
    legal_moves = king.get_legal_moves(conflict_sqrs, position)
    expected_moves = []  # All surrounding squares are blocked by friendly pieces
    assert legal_moves == expected_moves

def test_king_queenside_legal_move():
    conflict_sqrs = ['F1', 'F2', 'E2']
    fen_parser = c.FENParser(fen_string='rnbq1rk1/ppp1bppp/3p1n2/4p3/4P3/2NPB3/PPP1QPPP/R3KBNR w KQ - 5 6')
    position = fen_parser.position
    move_gen = c.LegalMoveGenerator(
        position=position, 
        active_colour='white', 
        en_passant_target=fen_parser.en_passant_target, 
        castling_rights=fen_parser.castling_rights, 
        opp_king=fen_parser.black_king
        )

    legal_moves = move_gen.white_legal_moves[fen_parser.white_king]
    expected_moves = ['D1', 'D2', 'C1']
    assert fen_parser.white_king.type == "king"
    assert fen_parser.white_king.colour == "white"
    assert fen_parser.white_king.occupied_square == "E1"
    assert legal_moves == expected_moves

# ------------------ Test c.c.FENParser ----------------------------------------------------------------------

def test_valid_starting_position():
    """Test parsing the standard starting position FEN."""
    fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    parser = c.FENParser(fen)
    
    # Test active color
    assert parser.get_active_colour() == 'white'
    
    # Test castling rights
    assert parser.get_castling_rights('white', 'kingside') == True
    assert parser.get_castling_rights('white', 'queenside') == True
    assert parser.get_castling_rights('black', 'kingside') == True
    assert parser.get_castling_rights('black', 'queenside') == True
    
    # Test en passant target
    assert parser.get_en_passant_target() == None
    
    # Test halfmove clock and fullmove number
    assert parser.get_halfmove_clock() == 0
    assert parser.get_fullmove_number() == 1
    
    # Test position dictionary
    position = parser.get_position()
    # Verify that A1 is a white rook
    assert isinstance(position['A1'], c.Rook)
    assert position['A1'].colour == 'white'
    # Verify that E1 is a white king
    assert isinstance(position['E1'], c.King)
    assert position['E1'].colour == 'white'
    # Verify that E8 is a black king
    assert isinstance(position['E8'], c.King)
    assert position['E8'].colour == 'black'
    # Verify that D2 is a white pawn
    assert isinstance(position['D2'], c.Pawn)
    assert position['D2'].colour == 'white'
    # Verify that D7 is a black pawn
    assert isinstance(position['D7'], c.Pawn)
    assert position['D7'].colour == 'black'
    # Verify that square E4 is None (empty)
    assert position['E4'] == None

def test_valid_en_passant():
    """Test parsing a FEN string with en passant target square."""
    fen = "rnbqkbnr/pp1ppppp/8/2pP4/8/8/PP1P1PPP/RNBQKBNR b KQkq c6 0 3"
    parser = c.FENParser(fen)
    
    # Test active color
    assert parser.get_active_colour() == 'black'
    
    # Test en passant target
    assert parser.get_en_passant_target() == 'C6'
    
    # Test position
    position = parser.get_position()
    assert isinstance(position['D5'], c.Pawn)
    assert position['D5'].colour == 'white'
    assert isinstance(position['C5'], c.Pawn)
    assert position['C5'].colour == 'black'

def test_valid_castling_rights():
    """Test parsing castling rights."""
    fen = "r3k2r/8/8/8/8/8/8/R3K2R w KQkq - 0 1"
    parser = c.FENParser(fen)
    
    # Test castling rights
    assert parser.get_castling_rights('white', 'kingside') == True
    assert parser.get_castling_rights('white', 'queenside') == True
    assert parser.get_castling_rights('black', 'kingside') == True
    assert parser.get_castling_rights('black', 'queenside') == True

def test_no_castling_rights():
    """Test parsing FEN with no castling rights."""
    fen = "r3k2r/8/8/8/8/8/8/R3K2R w - - 0 1"
    parser = c.FENParser(fen)
    
    # Test castling rights
    assert parser.get_castling_rights('white', 'kingside') == False
    assert parser.get_castling_rights('white', 'queenside') == False
    assert parser.get_castling_rights('black', 'kingside') == False
    assert parser.get_castling_rights('black', 'queenside') == False

def test_invalid_fen_incorrect_fields():
    """Test handling of FEN string with incorrect number of fields."""
    fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0"
    with pytest.raises(ValueError) as exc_info:
        c.FENParser(fen)
    assert str(exc_info.value) == "Invalid FEN string: Incorrect number of fields"

def test_invalid_active_color():
    """Test handling of invalid active color."""
    fen = "8/8/8/8/8/8/8/8 x - - 0 1"
    with pytest.raises(ValueError) as exc_info:
        c.FENParser(fen)
    assert str(exc_info.value) == "Invalid active color: must be 'w' or 'b'"

def test_invalid_halfmove_clock():
    """Test handling of invalid halfmove clock."""
    fen = "8/8/8/8/8/8/8/8 w - - x 1"
    with pytest.raises(ValueError) as exc_info:
        c.FENParser(fen)
    assert str(exc_info.value) == "Halfmove clock and fullmove number must be integers"

def test_invalid_fullmove_number():
    """Test handling of invalid fullmove number."""
    fen = "8/8/8/8/8/8/8/8 w - - 0 y"
    with pytest.raises(ValueError) as exc_info:
        c.FENParser(fen)
    assert str(exc_info.value) == "Halfmove clock and fullmove number must be integers"

def test_invalid_piece_placement():
    """Test handling of invalid piece placement."""
    fen = "8/8/8/8/8/8/8/9 w - - 0 1"  # 9 columns in last row
    with pytest.raises(ValueError) as exc_info:
        c.FENParser(fen)
    assert "Invalid piece placement data" in str(exc_info.value)

def test_invalid_character_in_piece_placement():
    """Test handling of invalid character in piece placement."""
    fen = "8/8/8/8/8/8/8/8 w - - 0 1"
    # Modify the piece placement to include an invalid character
    fen = fen.replace('8', '8$', 1)
    with pytest.raises(ValueError) as exc_info:
        c.FENParser(fen)
    assert "Invalid character in piece placement" in str(exc_info.value)

def test_empty_board():
    """Test parsing an empty board."""
    fen = "8/8/8/8/8/8/8/8 w - - 0 1"
    parser = c.FENParser(fen)
    
    # Test position dictionary
    position = parser.get_position()
    assert all(value is None for value in position.values())
    assert len(position) == 64  # 8x8 board

def test_halfmove_and_fullmove():
    """Test parsing non-zero halfmove clock and fullmove number."""
    fen = "8/8/8/8/8/8/8/8 w - - 5 42"
    parser = c.FENParser(fen)
    assert parser.get_halfmove_clock() == 5
    assert parser.get_fullmove_number() == 42

def test_en_passant_target_none():
    """Test that en passant target is None when not available."""
    fen = "8/8/8/8/8/8/8/8 w - - 0 1"
    parser = c.FENParser(fen)
    assert parser.get_en_passant_target() == None

def test_en_passant_target_available():
    """Test that en passant target is set correctly."""
    fen = "8/8/8/8/8/8/8/8 w - e3 0 1"
    parser = c.FENParser(fen)
    assert parser.get_en_passant_target() == 'E3'

def test_white_and_black_kings():
    """Test that the kings are correctly identified."""
    fen = "4k3/8/8/8/8/8/8/4K3 w - - 0 1"
    parser = c.FENParser(fen)
    assert isinstance(parser.white_king, c.King)
    assert parser.white_king.colour == 'white'
    assert parser.white_king.occupied_square == 'E1'
    assert isinstance(parser.black_king, c.King)
    assert parser.black_king.colour == 'black'
    assert parser.black_king.occupied_square == 'E8'

def test_invalid_en_passant_target():
    """Test handling of invalid en passant target."""
    fen = "8/8/8/8/8/8/8/8 w - xy 0 1"
    parser = c.FENParser(fen)
    assert parser.get_en_passant_target() == 'XY'  # Uppercased, but may not be valid square
    # Depending on implementation, you might want to validate en passant target squares

def test_position_has_correct_number_of_squares():
    """Test that the position dictionary has 64 squares."""
    fen = "8/8/8/8/8/8/8/8 w - - 0 1"
    parser = c.FENParser(fen)
    position = parser.get_position()
    assert len(position) == 64

def test_positions_of_pieces():
    """Test that pieces are placed in correct positions."""
    fen = "r3k2r/8/8/8/8/8/8/R3K2R w KQkq - 0 1"
    parser = c.FENParser(fen)
    position = parser.get_position()
    
    assert isinstance(position['A1'], c.Rook)
    assert position['A1'].colour == 'white'
    assert isinstance(position['H1'], c.Rook)
    assert position['H1'].colour == 'white'
    assert isinstance(position['E1'], c.King)
    assert position['E1'].colour == 'white'
    assert isinstance(position['A8'], c.Rook)
    assert position['A8'].colour == 'black'
    assert isinstance(position['H8'], c.Rook)
    assert position['H8'].colour == 'black'
    assert isinstance(position['E8'], c.King)
    assert position['E8'].colour == 'black'

def test_invalid_fen_extra_fields():
    """Test handling of FEN string with extra fields."""
    fen = "8/8/8/8/8/8/8/8 w - - 0 1 extra_field"
    with pytest.raises(ValueError) as exc_info:
        c.FENParser(fen)
    assert "Invalid FEN string: Incorrect number of fields" in str(exc_info.value)

# ------------------------------- Test PieceFactory --------------------------------------------------------------

def test_create_white_rook():
    rook = c.PieceFactory.create_piece('R', 'A1')
    assert isinstance(rook, c.Rook)
    assert rook.colour == 'white'
    assert rook.occupied_square == 'A1'

def test_create_black_rook():
    rook = c.PieceFactory.create_piece('r', 'A8')
    assert isinstance(rook, c.Rook)
    assert rook.colour == 'black'
    assert rook.occupied_square == 'A8'

def test_create_white_knight():
    knight = c.PieceFactory.create_piece('N', 'B1')
    assert isinstance(knight, c.Knight)
    assert knight.colour == 'white'
    assert knight.occupied_square == 'B1'

def test_create_black_knight():
    knight = c.PieceFactory.create_piece('n', 'B8')
    assert isinstance(knight, c.Knight)
    assert knight.colour == 'black'
    assert knight.occupied_square == 'B8'

def test_create_white_bishop():
    bishop = c.PieceFactory.create_piece('B', 'C1')
    assert isinstance(bishop, c.Bishop)
    assert bishop.colour == 'white'
    assert bishop.occupied_square == 'C1'

def test_create_black_bishop():
    bishop = c.PieceFactory.create_piece('b', 'C8')
    assert isinstance(bishop, c.Bishop)
    assert bishop.colour == 'black'
    assert bishop.occupied_square == 'C8'

def test_create_white_queen():
    queen = c.PieceFactory.create_piece('Q', 'D1')
    assert isinstance(queen, c.Queen)
    assert queen.colour == 'white'
    assert queen.occupied_square == 'D1'

def test_create_black_queen():
    queen = c.PieceFactory.create_piece('q', 'D8')
    assert isinstance(queen, c.Queen)
    assert queen.colour == 'black'
    assert queen.occupied_square == 'D8'

def test_create_white_king():
    king = c.PieceFactory.create_piece('K', 'E1')
    assert isinstance(king, c.King)
    assert king.colour == 'white'
    assert king.occupied_square == 'E1'

def test_create_black_king():
    king = c.PieceFactory.create_piece('k', 'E8')
    assert isinstance(king, c.King)
    assert king.colour == 'black'
    assert king.occupied_square == 'E8'

def test_create_white_pawn():
    pawn = c.PieceFactory.create_piece('P', 'E2')
    assert isinstance(pawn, c.Pawn)
    assert pawn.colour == 'white'
    assert pawn.occupied_square == 'E2'

def test_create_black_pawn():
    pawn = c.PieceFactory.create_piece('p', 'E7')
    assert isinstance(pawn, c.Pawn)
    assert pawn.colour == 'black'
    assert pawn.occupied_square == 'E7'

def test_create_invalid_piece_uppercase():
    with pytest.raises(ValueError) as exc_info:
        c.PieceFactory.create_piece('X', 'E4')
    assert str(exc_info.value) == "Unknown piece character: X"

def test_create_invalid_piece_lowercase():
    with pytest.raises(ValueError) as exc_info:
        c.PieceFactory.create_piece('y', 'E4')
    assert str(exc_info.value) == "Unknown piece character: y"

def test_create_empty_char():
    with pytest.raises(ValueError) as exc_info:
        c.PieceFactory.create_piece('', 'E4')
    assert str(exc_info.value) == "Unknown piece character: "

def test_create_non_alpha_char():
    with pytest.raises(ValueError) as exc_info:
        c.PieceFactory.create_piece('1', 'E4')
    assert str(exc_info.value) == "Unknown piece character: 1"

def test_create_none_char():
    with pytest.raises(AttributeError):
        c.PieceFactory.create_piece(None, 'E4')

def test_create_with_invalid_square():
    # Assuming that the piece classes handle occupied_square validation
    rook = c.PieceFactory.create_piece('R', 'Z9')
    assert isinstance(rook, c.Rook)
    assert rook.occupied_square == 'Z9'  # Adjust based on your implementation

def test_create_with_missing_square():
    with pytest.raises(TypeError):
        c.PieceFactory.create_piece('R')

def test_create_with_additional_arguments():
    with pytest.raises(TypeError):
        c.PieceFactory.create_piece('R', 'A1', 'extra_argument')

# -------------------------- Test LegalMoveGenerator ----------------------------------------------


def setup_board(position_dict):
    """
    Helper function to set up the board from a position dictionary.
    The position dictionary maps square names to piece instances or None.
    """
    position = {}
    for square in [f"{file}{rank}" for rank in range(1, 9) for file in 'ABCDEFGH']:
        position[square] = position_dict.get(square, None)
    return position

def test_pawn_captures():
    """
    Test that pawns can capture enemy pieces diagonally.
    """
    # Set up the board with pawns ready to capture
    position_dict = {
        'D4': c.Pawn('white', 'D4'),
        'C5': c.Pawn('black', 'C5'),
        'E5': c.Pawn('black', 'E5'),
        'E1': c.King('white', 'E1'),
        'E8': c.King('black', 'E8')
    }
    # Set up the board
    board = c.Board()
    board.position = setup_board(position_dict)
    board.white_king = board.position['E1']
    board.black_king = board.position['E8']
    board.active_colour = 'white'
    board.en_passant_target = None
    board.castling_rights = 'KQkq'
    # Generate legal moves
    board.move_generator = c.LegalMoveGenerator(
        position=board.position,
        active_colour=board.active_colour,
        en_passant_target=board.en_passant_target,
        castling_rights=board.castling_rights,
        opp_king=board.black_king
    )
    board.move_generator.generate_legal_moves()
    pawn = board.position['D4']
    legal_moves = board.move_generator.white_legal_moves.get(pawn, [])
    assert set(legal_moves) == {'D5', 'C5', 'E5'}  # Move forward and capture diagonally

def test_en_passant():
    """
    Test that en passant captures are available when appropriate.
    """
    # Set up a position where en passant is possible
    position_dict = {
        'E5': c.Pawn('white', 'E5'),
        'D5': c.Pawn('black', 'D5'),
        'E1': c.King('white', 'E1'),
        'E8': c.King('black', 'E8')
    }
    board = c.Board()
    board.position = setup_board(position_dict)
    board.white_king = board.position['E1']
    board.black_king = board.position['E8']
    board.active_colour = 'white'
    # Black's last move was from D7 to D5, so en passant target is D6
    board.en_passant_target = 'D6'
    board.castling_rights = 'KQkq'
    # Generate legal moves
    board.move_generator = c.LegalMoveGenerator(
        position=board.position,
        active_colour=board.active_colour,
        en_passant_target=board.en_passant_target,
        castling_rights=board.castling_rights,
        opp_king=board.black_king
    )
    board.move_generator.generate_legal_moves()
    pawn = board.position['E5']
    legal_moves = board.move_generator.white_legal_moves.get(pawn, [])
    assert 'D6' in legal_moves  # En passant capture

def test_castling_rights():
    """
    Test that castling is correctly handled.
    """
    # Set up a position where castling is possible
    position_dict = {
        'E1': c.King('white', 'E1'),
        'H1': c.Rook('white', 'H1'),
        'A1': c.Rook('white', 'A1'),
        'E8': c.King('black', 'E8'),
        # Ensure squares between king and rooks are empty
    }
    board = c.Board()
    board.position = setup_board(position_dict)
    board.white_king = board.position['E1']
    board.black_king = board.position['E8']
    board.active_colour = 'white'
    board.en_passant_target = None
    board.castling_rights = 'QK'
    # Generate legal moves
    board.move_generator = c.LegalMoveGenerator(
        position=board.position,
        active_colour=board.active_colour,
        en_passant_target=board.en_passant_target,
        castling_rights=board.castling_rights,
        opp_king=board.black_king
    )
    board.move_generator.generate_legal_moves()
    king = board.position['E1']
    legal_moves = board.move_generator.white_legal_moves.get(king, [])
    assert 'G1' in legal_moves  # Kingside castling
    assert 'C1' in legal_moves  # Queenside castling

def test_pinned_piece_cannot_move():
    """
    Test that a pinned piece cannot move in a way that exposes the king to check.
    """
    # Set up a position where a white bishop is pinned by a black rook
    position_dict = {
        'E1': c.King('white', 'E1'),
        'E2': c.Bishop('white', 'E2'),
        'E8': c.King('black', 'E8'),
        'E7': c.Rook('black', 'E7')
    }
    board = c.Board()
    board.position = setup_board(position_dict)
    board.white_king = board.position['E1']
    board.black_king = board.position['E8']
    board.active_colour = 'white'
    board.en_passant_target = None
    board.castling_rights = ''
    # Generate legal moves
    board.move_generator = c.LegalMoveGenerator(
        position=board.position,
        active_colour=board.active_colour,
        en_passant_target=board.en_passant_target,
        castling_rights=board.castling_rights,
        opp_king=board.black_king
    )
    board.move_generator.generate_legal_moves()
    bishop = board.position['E2']
    legal_moves = board.move_generator.white_legal_moves.get(bishop, [])
    # The bishop can only move along the E-file to block or capture
    assert legal_moves == []

def test_king_cannot_move_into_check():
    """
    Test that the king cannot move into a square attacked by an enemy piece.
    """
    # Set up a position where the black queen attacks squares around the white king
    position_dict = {
        'E1': c.King('white', 'E1'),
        'E8': c.King('black', 'E8'),
        'E5': c.Queen('black', 'E5')
    }
    board = c.Board()
    board.position = setup_board(position_dict)
    board.white_king = board.position['E1']
    board.black_king = board.position['E8']
    board.active_colour = 'white'
    board.en_passant_target = None
    board.castling_rights = ''
    # Generate legal moves
    board.move_generator = c.LegalMoveGenerator(
        position=board.position,
        active_colour=board.active_colour,
        en_passant_target=board.en_passant_target,
        castling_rights=board.castling_rights,
        opp_king=board.black_king
    )
    board.move_generator.generate_legal_moves()
    king = board.position['E1']
    legal_moves = board.move_generator.white_legal_moves.get(king, [])
    # The king cannot move into squares attacked by the black queen
    assert set(legal_moves) == {'D1', 'F1', 'D2', 'F2'}

def test_stalemate():
    """
    Test a stalemate position where the player has no legal moves but is not in check.
    """
    # Set up a stalemate position
    position_dict = {
        'A8': c.King('black', 'A8'),
        'C7': c.Queen('white', 'C7'),
        'B6': c.Queen('white', 'B6'),
        'H1': c.King('white', 'H1')
    }
    board = c.Board()
    board.position = setup_board(position_dict)
    board.white_king = board.position['H1']
    board.black_king = board.position['A8']
    board.active_colour = 'black'
    board.en_passant_target = None
    board.castling_rights = ''
    # Generate legal moves
    board.move_generator = c.LegalMoveGenerator(
        position=board.position,
        active_colour='black',
        en_passant_target=board.en_passant_target,
        castling_rights=board.castling_rights,
        opp_king=board.white_king
    )
    board.move_generator.generate_legal_moves()
    king = board.position['A8']
    legal_moves = board.move_generator.black_legal_moves.get(king, [])
    # Black king has no legal moves
    assert legal_moves == []

def test_checkmate():
    """
    Test a checkmate position where the player has no legal moves and is in check.
    """
    # Set up a checkmate position
    position_dict = {
        'E8': c.King('black', 'E8'),
        'F6': c.Pawn('white', 'F6'),
        'E7': c.Queen('white', 'E7'),
        'E1': c.King('white', 'E1')
    }
    board = c.Board()
    board.position = setup_board(position_dict)
    board.white_king = board.position['E1']
    board.black_king = board.position['E8']
    board.active_colour = 'black'
    board.en_passant_target = None
    board.castling_rights = ''
    # Generate legal moves
    board.move_generator = c.LegalMoveGenerator(
        position=board.position,
        active_colour='black',
        en_passant_target=board.en_passant_target,
        castling_rights=board.castling_rights,
        opp_king=board.white_king
    )

    king = board.position.get('E8')
    # Black king is in check and has no legal moves
    assert len(board.move_generator.checking_pieces) == 1
    assert board.move_generator.is_checkmate == True
    assert board.move_generator.black_legal_moves == False

def test_must_resolve_check():
    """
    Test that only moves that resolve the check are allowed when the king is in check.
    """
    # Set up a position where the white king is in check from a black rook
    position_dict = {
        'E1': c.King('white', 'E1'),
        'F4': c.Knight('white', 'F4'),
        'E8': c.King('black', 'E8'),
        'E5': c.Rook('black', 'E5')
    }
    board = c.Board()
    board.position = setup_board(position_dict)
    board.white_king = board.position['E1']
    board.black_king = board.position['E8']
    board.active_colour = 'white'
    board.en_passant_target = None
    board.castling_rights = ''
    # Generate legal moves
    board.move_generator = c.LegalMoveGenerator(
        position=board.position,
        active_colour='white',
        en_passant_target=board.en_passant_target,
        castling_rights=board.castling_rights,
        opp_king=board.black_king
    )
    board.move_generator.generate_legal_moves()
    knight = board.position['F4']
    legal_moves = board.move_generator.white_legal_moves.get(knight, [])
    # Pawn can only move to E3 to block the check
    assert set(legal_moves) == {'E2'}
    # Other pieces should not have legal moves if they don't resolve the check
    for piece, moves in board.move_generator.white_legal_moves.items():
        if piece != knight and piece != board.white_king:
            assert moves == []

def test_blocking_check():
    """
    Test that pieces can block a check to the king.
    """
    # Set up a position where the black rook checks the white king
    position_dict = {
        'E1': c.King('white', 'E1'),
        'D2': c.Bishop('white', 'D2'),
        'E8': c.King('black', 'E8'),
        'E4': c.Rook('black', 'E4')
    }
    board = c.Board()
    board.position = setup_board(position_dict)
    board.white_king = board.position['E1']
    board.black_king = board.position['E8']
    board.active_colour = 'white'
    board.en_passant_target = None
    board.castling_rights = ''
    # Generate legal moves
    board.move_generator = c.LegalMoveGenerator(
        position=board.position,
        active_colour='white',
        en_passant_target=board.en_passant_target,
        castling_rights=board.castling_rights,
        opp_king=board.black_king
    )
    board.move_generator.generate_legal_moves()
    bishop = board.position['D2']
    legal_moves = board.move_generator.white_legal_moves.get(bishop, [])
    # Bishop can move to E3 to block the check
    assert {'E3'} == set(legal_moves)

def test_double_check():
    """
    Test that only the king can move in double check
    """
    # Set up a position where the black rook checks the white king
    position_dict = {
        'C8': c.King('black', 'C8'),
        'B6': c.Knight('white', 'B6'),
        'E1': c.King('white', 'E1'),
        'C3': c.Queen('white', 'C3'),
        'B8': c.Queen('black', 'B8')
    }
    board = c.Board()
    board.position = setup_board(position_dict)
    board.white_king = board.position['E1']
    board.black_king = board.position['C8']
    board.active_colour = 'black'
    board.en_passant_target = None
    board.castling_rights = ''
    # Generate legal moves
    board.move_generator = c.LegalMoveGenerator(
        position=board.position,
        active_colour='black',
        en_passant_target=board.en_passant_target,
        castling_rights=board.castling_rights,
        opp_king=board.white_king
    )

    king = board.position['C8']
    legal_moves = board.move_generator.black_legal_moves
    print("legal moves: ", legal_moves)
    print("checking pieces: ", board.move_generator.checking_pieces)

    assert board.active_colour == "black"
    assert board.move_generator.in_check == True
    assert {'B7', 'D8'} == set(legal_moves[king])

def test_capture_checking_piece():
    """
    Test that pieces can capture the checking piece.
    """
    # Set up a position where the black queen checks the white king
    position_dict = {
        'E1': c.King('white', 'E1'),
        'D2': c.Bishop('white', 'D2'),
        'E8': c.King('black', 'E8'),
        'E3': c.Queen('black', 'E3')
    }
    board = c.Board()
    board.position = setup_board(position_dict)
    board.white_king = board.position['E1']
    board.black_king = board.position['E8']
    board.active_colour = 'white'
    board.en_passant_target = None
    board.castling_rights = ''
    # Generate legal moves
    board.move_generator = c.LegalMoveGenerator(
        position=board.position,
        active_colour='white',
        en_passant_target=board.en_passant_target,
        castling_rights=board.castling_rights,
        opp_king=board.black_king
    )

    bishop = board.position['D2']
    king = board.position['E1']
    bishop_legal_moves = board.move_generator.white_legal_moves.get(bishop, [])
    king_legal_moves = board.move_generator.white_legal_moves.get(king, [])

    assert board.move_generator.in_check == True
    assert board.move_generator.is_checkmate == False
    assert len(board.move_generator.checking_pieces) > 0
    assert {'D1', 'F1'} == set(king_legal_moves)
    assert {'E3'} == set(bishop_legal_moves)

def test_pinned_knight_cannot_move():
    """
    Test that a pinned knight cannot move.
    """
    # Set up a position where a white knight is pinned by a black bishop
    position_dict = {
        'C1': c.King('white', 'C1'),
        'D2': c.Knight('white', 'D2'),
        'E8': c.King('black', 'E8'),
        'G5': c.Bishop('black', 'G5')
    }
    board = c.Board()
    board.position = setup_board(position_dict)
    board.white_king = board.position['C1']
    board.black_king = board.position['E8']
    board.active_colour = 'white'
    board.en_passant_target = None
    board.castling_rights = ''
    # Generate legal moves
    board.move_generator = c.LegalMoveGenerator(
        position=board.position,
        active_colour='white',
        en_passant_target=board.en_passant_target,
        castling_rights=board.castling_rights,
        opp_king=board.black_king
    )
    board.move_generator.generate_legal_moves()
    knight = board.position['D2']
    legal_moves = board.move_generator.white_legal_moves.get(knight, [])
    # Knight should have no legal moves
    assert legal_moves == []

def test_bishop_pinned_diagonally():
    """
    Test that a bishop pinned diagonally can only move along the line of the pin.
    """
    position_dict = {
        'C1': c.King('white', 'C1'),
        'D2': c.Bishop('white', 'D2'),
        'E3': c.Bishop('black', 'E3'),
        'E8': c.King('black', 'E8')
    }
    board = c.Board()
    board.position = setup_board(position_dict)
    board.white_king = board.position['C1']
    board.black_king = board.position['E8']
    board.active_colour = 'white'
    board.en_passant_target = None
    board.castling_rights = ''
    # Generate legal moves
    board.move_generator = c.LegalMoveGenerator(
        position=board.position,
        active_colour='white',
        en_passant_target=board.en_passant_target,
        castling_rights=board.castling_rights,
        opp_king=board.black_king
    )
    board.move_generator.generate_legal_moves()
    bishop = board.position['D2']
    legal_moves = board.move_generator.white_legal_moves.get(bishop, [])
    # Bishop can only move along the diagonal towards or away from the black bishop
    assert set(legal_moves) == {'E3'}

def test_knight_moves():
    """
    Test that knights have correct legal moves, including capturing enemy pieces.
    """
    position_dict = {
        'E1': c.King('white', 'E1'),
        'E8': c.King('black', 'E8'),
        'D4': c.Knight('white', 'D4'),
        'E6': c.Pawn('black', 'E6'),
        'C6': c.Pawn('white', 'C6')
    }
    board = c.Board()
    board.position = setup_board(position_dict)
    board.white_king = board.position['E1']
    board.black_king = board.position['E8']
    board.active_colour = 'white'
    board.en_passant_target = None
    board.castling_rights = ''
    # Generate legal moves
    board.move_generator = c.LegalMoveGenerator(
        position=board.position,
        active_colour='white',
        en_passant_target=board.en_passant_target,
        castling_rights=board.castling_rights,
        opp_king=board.black_king
    )
    board.move_generator.generate_legal_moves()
    knight = board.position['D4']
    legal_moves = board.move_generator.white_legal_moves.get(knight, [])
    expected_moves = {'B3', 'B5', 'C2', 'C6', 'E2', 'E6', 'F3', 'F5'}
    # Should not include moves to C6 (own pawn)
    expected_moves.discard('C6')
    assert set(legal_moves) == expected_moves - {'C6'}

def test_rook_moves():
    """
    Test that rooks have correct legal moves, including capturing and being blocked by own pieces.
    """
    position_dict = {
        'E1': c.King('white', 'E1'),
        'E8': c.King('black', 'E8'),
        'D4': c.Rook('white', 'D4'),
        'D6': c.Pawn('black', 'D6'),
        'G4': c.Bishop('white', 'G4')
    }
    board = c.Board()
    board.position = setup_board(position_dict)
    board.white_king = board.position['E1']
    board.black_king = board.position['E8']
    board.active_colour = 'white'
    board.en_passant_target = None
    board.castling_rights = ''
    # Generate legal moves
    board.move_generator = c.LegalMoveGenerator(
        position=board.position,
        active_colour='white',
        en_passant_target=board.en_passant_target,
        castling_rights=board.castling_rights,
        opp_king=board.black_king
    )
    board.move_generator.generate_legal_moves()
    rook = board.position['D4']
    legal_moves = board.move_generator.white_legal_moves.get(rook, [])
    expected_moves = {'D5', 'D6', 'D3', 'D2', 'D1', 'C4', 'B4', 'A4', 'E4', 'F4'}
    # Cannot move past own bishop at G4
    assert set(legal_moves) == expected_moves

def test_bishop_moves():
    """
    Test that bishops have correct legal moves, including capturing and being blocked.
    """
    position_dict = {
        'E1': c.King('white', 'E1'),
        'E8': c.King('black', 'E8'),
        'D4': c.Bishop('white', 'D4'),
        'B6': c.Pawn('black', 'B6'),
        'F6': c.Pawn('white', 'F6')
    }
    board = c.Board()
    board.position = setup_board(position_dict)
    board.white_king = board.position['E1']
    board.black_king = board.position['E8']
    board.active_colour = 'white'
    board.en_passant_target = None
    board.castling_rights = ''
    # Generate legal moves
    board.move_generator = c.LegalMoveGenerator(
        position=board.position,
        active_colour='white',
        en_passant_target=None,
        castling_rights={},
        opp_king=board.black_king
    )
    board.move_generator.generate_legal_moves()
    bishop = board.position['D4']
    legal_moves = board.move_generator.white_legal_moves.get(bishop, [])
    expected_moves = {'C5', 'B6', 'E5', 'F2', 'G1', 'B2', 'A1', 'C3', 'E3'}
    # Cannot move to F6 (own pawn)
    expected_moves.discard('F6')
    assert set(legal_moves) == expected_moves

def test_queen_moves():
    """
    Test that queens have correct legal moves, combining rook and bishop movement.
    """
    position_dict = {
        'E1': c.King('white', 'E1'),
        'E8': c.King('black', 'E8'),
        'D4': c.Queen('white', 'D4'),
        'D6': c.Pawn('black', 'D6'),
        'F6': c.Pawn('white', 'F6'),
        'B4': c.Pawn('black', 'B4')
    }
    board = c.Board()
    board.position = setup_board(position_dict)
    board.white_king = board.position['E1']
    board.black_king = board.position['E8']
    board.active_colour = 'white'
    # Generate legal moves
    board.move_generator = c.LegalMoveGenerator(
        position=board.position,
        active_colour='white',
        en_passant_target=None,
        castling_rights={},
        opp_king=board.black_king
    )
    board.move_generator.generate_legal_moves()
    queen = board.position['D4']
    legal_moves = board.move_generator.white_legal_moves.get(queen, [])
    expected_moves = {
        'D5', 'D6', 'D3', 'D2', 'D1', 'C4', 'B4', 'E4', 'F4', 'G4', 'H4',  # Rook-like moves
        'A1', 'B2', 'C3', 'C5', 'B6', 'E5', 'F2', 'E3', 'G1', 'C5', 'B6', 'A7'               # Bishop-like moves
    }
    # Remove moves blocked by own pawn at F6
    expected_moves.discard('F6')
    assert set(legal_moves) == expected_moves

def test_queen_moves2():
    """
    Test that queens have correct legal moves, combining rook and bishop movement.
    """
    position_dict = {
        'C1': c.King('white', 'C1'),
        'H8': c.King('black', 'H8'),
        'H5': c.Queen('white', 'H5'),
        'H7': c.Pawn('black', 'H7'),
        'H2': c.Pawn('white', 'H2'),
        'B4': c.Pawn('black', 'F7')
    }
    board = c.Board(fen='7k/5p1p/8/7Q/8/8/7P/2K5 w - - 0 1')
    board.white_king = board.position['C1']
    board.black_king = board.position['H8']
    board.active_colour = 'white'
    # Generate legal moves
    board.move_generator = c.LegalMoveGenerator(
        position=board.position,
        active_colour='white',
        en_passant_target=None,
        castling_rights={},
        opp_king=board.black_king
    )
    board.move_generator.generate_legal_moves()
    queen = board.position['H5']
    legal_moves = board.move_generator.white_legal_moves.get(queen, [])
    expected_moves = [
        'H6', 'H7',  # Up
        'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5',  # left
        'H4', 'H3',  # Down
        'D1', 'E2', 'F3', 'G4',  # Down-Left
        'G6', 'F7'    # Up-Left
    ]
    assert set(legal_moves) == set(expected_moves)
    assert board.move_generator.get_check_status() == False
