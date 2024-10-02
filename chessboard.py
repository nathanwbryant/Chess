import algebraic_notation
import random as r
import copy

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
    


def pieces_positions(fen):
    # FEN starts at square A8 then B8... then A7, A6... so rank descends and file letter (number) ascends
    rank = 8
    file_num = ord("A")-64  # starts at 1
    
    positions = {"A1": "", "A2": ""}

    for i in fen:
        
        if i.isnumeric():
            file_num += int(i) if file_num+int(i)<9 else 1
            continue
        elif i == "r":
            positions[f"{chr(file_num+64)}{rank}"] = "b rook"
        elif i == "n":
            positions[f"{chr(file_num+64)}{rank}"] = "b knight"
        elif i == "b":
            positions[f"{chr(file_num+64)}{rank}"] = "b bishop"
        elif i == "q":
            positions[f"{chr(file_num+64)}{rank}"] = "b queen"
        elif i == "k":
            positions[f"{chr(file_num+64)}{rank}"] = "b king"
        elif i == "p":
            positions[f"{chr(file_num+64)}{rank}"] = "b pawn"
        elif i == "R":
            positions[f"{chr(file_num+64)}{rank}"] = "w rook"
        elif i == "N":
            positions[f"{chr(file_num+64)}{rank}"] = "w knight"
        elif i == "B":
            positions[f"{chr(file_num+64)}{rank}"] = "w bishop"
        elif i == "Q":
            positions[f"{chr(file_num+64)}{rank}"] = "w queen"
        elif i == "K":
            positions[f"{chr(file_num+64)}{rank}"] = "w king"
        elif i == "P":
            positions[f"{chr(file_num+64)}{rank}"] = "w pawn"
        elif i == "/":
            rank -= 1
            file_num = 1
            continue
        elif i == " ":
            break

        file_num += 1 if file_num+1<9 else 1

    return positions

def find_square_of_piece(positions, piece):
    return [key for key, value in positions.items() if value == piece]
    # takes in a dict in the format {"A1": "w rook", ...} and a piece as in the value and returns a list of all positions

def coordinates_on_same_diagonal(square_coords, conflict_square_coords):
    conflict_rank_num, conflict_file_num = conflict_square_coords
    origin_rank_num, origin_file_num = square_coords

    # Ensure coordinates are on the same diagonal
    if abs(conflict_file_num - origin_file_num) != abs(conflict_rank_num - origin_rank_num): # if 1 doesnt equal 1
        raise ValueError("Coordinates are not on the same diagonal")

    # Determine the direction of the diagonal
    if (conflict_file_num < origin_file_num and conflict_rank_num < origin_rank_num): # conflict is down to the left
        direction = "descending backwards"

    elif (conflict_file_num < origin_file_num and conflict_rank_num > origin_rank_num): # 
        direction = "descending forwards"

    elif (conflict_file_num > origin_file_num and conflict_rank_num > origin_rank_num): # 
        direction = "ascending forwards"

    else:
        direction = "ascending backwards"

    # Generate all coordinates on the same diagonal
    result = []
    for d in range(1, 8):
        if direction == "ascending forwards":
            new_file_num, new_rank_num = conflict_file_num + d, conflict_rank_num + d     
            
        elif direction == "ascending backwards":
            new_file_num, new_rank_num = conflict_file_num + d, conflict_rank_num - d 

        elif direction == "descending backwards":
            new_file_num, new_rank_num = conflict_file_num - d, conflict_rank_num - d     

        else:
            new_file_num, new_rank_num = conflict_file_num - d, conflict_rank_num + d     
            
        if 0 < new_file_num <= 8 and 0 < new_rank_num <= 8:
            result.append(f"{chr(new_rank_num+64)}{new_file_num}")
        
        else:
            break

    return result 

def coordinates_on_same_rank(square_coords, conflict_square_coords):
    origin_file_num, origin_rank_num = square_coords
    conflict_file_num, conflict_rank_num = conflict_square_coords

    # Ensure coords are on the same rank only
    if origin_rank_num != conflict_rank_num:
        raise ValueError("Coordinates are not on the same rank")

    # Determine the direction from the origin square
    if origin_file_num < conflict_file_num:
        direction = "ascending"
    else:
        direction = "descending"

    # Generate all coordinates on the same rank
    result = []
    for d in range(1, 8):
        if direction == "ascending":
            new_file_num = conflict_file_num + d
        else:
            new_file_num = conflict_file_num - d

        if 0 < new_file_num <= 8:
            # Keep the rank constant, change only the file
            result.append(f"{chr(new_file_num + 64)}{origin_rank_num}")
        else: 
            break

    return result


def coordinates_on_same_file(square_coords, conflict_square_coords):
    origin_file_num, origin_rank_num = square_coords
    conflict_file_num, conflict_rank_num = conflict_square_coords

    # Ensure coords are on the same file only
    if origin_file_num != conflict_file_num:
        raise ValueError("Coordinates are not on the same file")

    # Determine the direction from origin square
    if origin_rank_num < conflict_rank_num:
        direction = "ascending"
    else:
        direction = "descending"

    # Generate all coordinates on the same file
    result = []
    for d in range(1, 8):
        if direction == "ascending":
            new_rank_num = conflict_rank_num + d
        else:
            new_rank_num = conflict_rank_num - d

        if 0 < new_rank_num <= 8:
            # Keep the file (column) constant, change only the rank (row)
            result.append(f"{chr(conflict_file_num + 64)}{new_rank_num}")
        else: 
            break

    return result 



class Piece:
    def __init__(self, occupied_square=None):
        
        self.occupied_square = occupied_square

    
class Queen:
    def __init__(self, colour, occupied_square=None):
        self.occupied_square = occupied_square
        self.type = "queen"
        self.colour = colour
        self.capture_squares = []
        self.visible_squares = self.get_visible_squares()
        self.under_attack = []
        self.legal_moves = []

    def __repr__(self) -> str:
        return f"{self.occupied_square} {self.colour} {self.type}"

    def get_visible_squares(self):
        list_of_squares = []
        
        # append squares on the same rank
        for square in ranks[self.occupied_square]:
            list_of_squares.append(square)
        
        # append squares on the same file
        for square in files[self.occupied_square]:
            list_of_squares.append(square)
        
        #append all on the same diagonals
        for square in diagonals[self.occupied_square]:
            list_of_squares.append(square)
        
        return list_of_squares


    def get_legal_moves(self, conflict_sqrs, position):
        """
        legal squares is a list of squares the piece could move to if the board was empty, conflict squares 
        are the locations of other pieces on the board and capture squares are conflict squares with
        opposition pieces on
        """

        legal_moves = []
        file = ord(self.occupied_square[0])  # Convert file (e.g., 'A') to ASCII value for easy iteration
        rank = int(self.occupied_square[1])  # Convert rank (e.g., '1') to an integer

        # Combine both rook-like and bishop-like directions
        directions = [
            (1, 0),   # Right
            (-1, 0),  # Left
            (0, 1),   # Up
            (0, -1),  # Down
            (1, 1),   # Up-right
            (-1, 1),  # Up-left
            (1, -1),  # Down-right
            (-1, -1)  # Down-left
        ]

        for direction in directions:
            d_file, d_rank = direction
            current_file = file
            current_rank = rank
            
            while True:
                current_file += d_file
                current_rank += d_rank
                
                # Check if we've hit the edge of the board
                if not (65 <= current_file <= 72 and 1 <= current_rank <= 8):  # 'A' to 'H' and 1 to 8
                    break
                
                # Convert back to chess notation
                square = f"{chr(current_file)}{current_rank}"
                
                # If we hit a conflict square (either friendly or opponent)
                if square in conflict_sqrs:
                    # Check if it's an opponent's piece (capture possibility)
                    
                    if position[square].colour != self.colour:
                        legal_moves.append(square)  # Capture the opponent's piece
                        
                    # Stop moving in this direction regardless
                    break
                else:
                    # If the square is empty and not blocked, it's a legal move
                    legal_moves.append(square)

        self.legal_moves = legal_moves
        return legal_moves

class Pawn:
    def __init__(self, colour, occupied_square=None):
        self.occupied_square = occupied_square
        self.type = "pawn"
        self.colour = colour
        self.moves = 0
        self.capture_squares = []
        self.visible_squares = self.get_visible_squares()
        self.under_attack = []
        self.legal_moves = []

    def __repr__(self) -> str:
        return f"{self.occupied_square} {self.colour} {self.type}"
    
    def get_visible_squares(self):
        list_of_squares = []
        file = self.occupied_square[0]
        rank = self.occupied_square[1]

        # get direction of movement
        if self.colour == "white":
            d = 1
        else:
            d = -1
            
        # move forward once - no need to consider being on final rank as it will be promoted
        list_of_squares.append(f"{file}{int(rank)+d}")

        # if on origin, can move forward twice
        if self.colour == "white":
            if rank == "2":
                list_of_squares.append(f"{file}{int(rank)+(2*d)}")
        
        else:
            if rank == "7":
                list_of_squares.append(f"{file}{int(rank)+(2*d)}")
        
        # get potential capture square
        attack_rank = int(rank)+d

        if ord(file)>65:
            list_of_squares.append(f"{chr(ord(file)-1)}{attack_rank}") 
        
        if ord(file)<72:
            list_of_squares.append(f"{chr(ord(file)+1)}{attack_rank}")

        return list_of_squares

    def get_legal_moves(self, position, en_passant):
        """
        legal squares is a list of squares the piece could move to if the board was empty, conflict squares 
        are the locations of other pieces on the board and capture squares are conflict squares with
        opposition pieces on
        """


        file = self.occupied_square[0] 
        rank = int(self.occupied_square[1])  # Convert rank (e.g., '2') to an integer

        valid_moves = []
        
        # get direction of movement for white and black
        if self.colour == "white": 
            d = 1       
        else:
            d = -1
            
        blocked = True if position.get(f"{file}{rank+d}") else False           

        for square in self.visible_squares:
            if position.get(square):
                conflict = position[square]

                if conflict.colour == self.colour:
                    # if it on the same file, remove all non capture moves
                    continue
                
                elif conflict.occupied_square[0] != file:
                    # Opponent piece on adjacent file - valid capture
                    valid_moves.append(square)
                else:
                    # opposition on occupied square on the same file, cannot capture
                    continue
            else:
                # Empty square, valid move if it is the same file
                if square[0] == file and not blocked:
                    valid_moves.append(square)
                else:
                    continue
                    

        if en_passant:
            en_passant_file = ord(en_passant[0])
            en_passant_rank = int(en_passant[1])
            # Check if pawn is on the correct rank and can capture en passant
            if rank == en_passant_rank - (1 if self.colour == "white" else -1):
                if ord(file) in [en_passant_file - 1, en_passant_file + 1]:
                    valid_moves.append(en_passant)

        self.legal_moves = valid_moves
        return valid_moves
        

class Knight:
    def __init__(self, colour, occupied_square=None):
        self.occupied_square = occupied_square
        self.type = "knight"
        self.colour = colour
        self.capture_squares = []
        self.visible_squares = self.get_visible_squares()
        self.under_attack = []
        self.legal_moves = []
    
    def __repr__(self) -> str:
        return f"{self.occupied_square} {self.colour} {self.type}"
        
    def get_visible_squares(self):
        visible_squares = []
        file = ord(self.occupied_square[0])  # Convert file (e.g., 'A') to ASCII value
        rank = int(self.occupied_square[1])  # Convert rank (e.g., '1') to an integer

        # Possible knight moves (file, rank changes)
        knight_moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),  # Two squares horizontally, one square vertically
            (1, 2), (1, -2), (-1, 2), (-1, -2)   # Two squares vertically, one square horizontally
        ]

        for move in knight_moves:
            d_file, d_rank = move
            current_file = file + d_file
            current_rank = rank + d_rank

            # Check if the move is within the bounds of the board
            if 65 <= current_file <= 72 and 1 <= current_rank <= 8:
                # Convert back to chess notation
                square = f"{chr(current_file)}{current_rank}"
                visible_squares.append(square)

        return visible_squares

    def get_legal_moves(self, conflict_sqrs, position):
        """
        legal squares is a list of squares the piece could move to if the board was empty, conflict squares 
        are the locations of other pieces on the board and capture squares are conflict squares with
        opposition pieces on
        """

        legal_moves = []
        # If the square is a conflict square (friendly piece), skip it
        for square in self.visible_squares:
            
            if square in conflict_sqrs:
                if position[square].colour == self.colour:
                    continue
                
                # opposing piece, add to moves
                legal_moves.append(square)
            else:
                # either empty or an opposing piece
                legal_moves.append(square)

        self.legal_moves = legal_moves
        return legal_moves

class Rook:
    def __init__(self, colour, occupied_square=None):
        self.occupied_square = occupied_square
        self.type = "rook"
        self.colour = colour
        self.capture_squares = []
        self.visible_squares = self.get_visible_squares()
        self.under_attack = []
        self.legal_moves = []
    
    def __repr__(self) -> str:
        return f"{self.occupied_square} {self.colour} {self.type}"

    def get_visible_squares(self):
        list_of_squares = []
        
        #append all on the same rank
        for square in ranks[self.occupied_square]:
            list_of_squares.append(square)
        
        #append all on the same file
        for square in files[self.occupied_square]:
            list_of_squares.append(square)
        
        return list_of_squares

    def get_legal_moves(self, conflict_sqrs, position):
        """
        legal squares is a list of squares the piece could move to if the board was empty, conflict squares 
        are the locations of other pieces on the board and capture squares are conflict squares with
        opposition pieces on
        """

        legal_moves = []
        file = ord(self.occupied_square[0])  # Convert file (e.g., 'A') to ASCII value for easy iteration
        rank = int(self.occupied_square[1])  # Convert rank (e.g., '1') to an integer

        directions = [
            (1, 0),   # Right (increase file)
            (-1, 0),  # Left (decrease file)
            (0, 1),   # Up (increase rank)
            (0, -1)   # Down (decrease rank)
        ]

        for direction in directions:
            d_file, d_rank = direction
            current_file = file
            current_rank = rank
            
            while True:
                current_file += d_file
                current_rank += d_rank
                
                # Check if we've hit the edge of the board
                if not (65 <= current_file <= 72 and 1 <= current_rank <= 8):  # 'A' to 'H' and 1 to 8
                    break
                
                # Convert back to chess notation
                square = f"{chr(current_file)}{current_rank}"
                
                # Check if there's a piece in the current square
                if square in conflict_sqrs:
                    
                    # If there's a capture piece, save the square
                    if position[square].colour != self.colour:
                        legal_moves.append

                    # otherwise it is friendly, do not save and stop in this direction
                    break

                else:
                    # If the square is empty, it's a legal move
                    legal_moves.append(square)

        self.legal_moves = legal_moves
        return legal_moves

class Bishop:
    def __init__(self, colour, occupied_square=None):
        self.occupied_square = occupied_square
        self.type = "bishop"
        self.colour = colour
        self.capture_squares = []
        self.visible_squares = self.get_visible_squares()
        self.under_attack = []
        self.legal_moves = []

    def __repr__(self) -> str:
        return f"{self.occupied_square} {self.colour} {self.type}"
    
    def get_visible_squares(self):
        list_of_squares = []
        
        for square in diagonals[self.occupied_square]:
            list_of_squares.append(square)
        
        return list_of_squares

    def get_legal_moves(self, conflict_sqrs, position):
        """
        legal squares is a list of squares the piece could move to if the board was empty, conflict squares 
        are the locations of other pieces on the board and capture squares are conflict squares with
        opposition pieces on
        """

        legal_moves = []
        file = ord(self.occupied_square[0])  # Convert file (e.g., 'A') to ASCII value for easy iteration
        rank = int(self.occupied_square[1])  # Convert rank (e.g., '1') to an integer

        # Diagonal directions: (file increment, rank increment)
        directions = [
            (1, 1),    # Up-right
            (-1, 1),   # Up-left
            (1, -1),   # Down-right
            (-1, -1)   # Down-left
        ]

        for direction in directions:
            d_file, d_rank = direction
            current_file = file
            current_rank = rank
            
            while True:
                current_file += d_file
                current_rank += d_rank
                
                # Check if we've hit the edge of the board
                if not (65 <= current_file <= 72 and 1 <= current_rank <= 8):  # 'A' to 'H' and 1 to 8
                    break
                
                # Convert back to chess notation
                square = f"{chr(current_file)}{current_rank}"
                
                # If we hit a conflict square (either friendly or opponent)
                if square in conflict_sqrs:
                    # Check if it's an opponent's piece (capture possibility)
                    if position[square].colour != self.colour:
                        legal_moves.append(square)  # Capture the opponent's piece
                    # Stop moving in this direction regardless
                    break
                else:
                    # If the square is empty and not blocked, it's a legal move
                    legal_moves.append(square)

        self.legal_moves = legal_moves
        return legal_moves


class King:
    def __init__(self, colour, occupied_square=None):
        self.occupied_square = occupied_square
        self.type = "king"
        self.colour = colour
        self.capture_squares = []
        self.visible_squares = self.get_visible_squares()
        self.under_attack = []
        self.legal_moves = []
    
    def __repr__(self) -> str:
        return f"{self.occupied_square} {self.colour} {self.type}"

    def get_visible_squares(self):
        list_of_squares = []
        file_int = ord(self.occupied_square[0])
        rank = int(self.occupied_square[1])

        # King's possible movements (one square in any direction)
        king_moves = [
            (1, 0), (0, 1), (-1, 0), (0, -1),    # Horizontal and vertical moves
            (1, 1), (1, -1), (-1, 1), (-1, -1)   # Diagonal moves
        ]

        for move in king_moves:
            d_file, d_rank = move
            current_file = file_int + d_file
            current_rank = rank + d_rank

            # Check if the move is within the bounds of the board
            if 65 <= current_file <= 72 and 1 <= current_rank <= 8:
                square = f"{chr(current_file)}{current_rank}"
                list_of_squares.append(square)
        
        return list_of_squares
    
    def get_legal_moves(self, conflict_sqrs, position):
        """
        legal squares is a list of squares the piece could move to if the board was empty, conflict squares 
        are the locations of other pieces on the board and capture squares are conflict squares with
        opposition pieces on. a King cannot move into check, this aspect is ignored and considered later
        """

        legal_moves = []
        file = ord(self.occupied_square[0])  # Convert file (e.g., 'A') to ASCII value
        rank = int(self.occupied_square[1])  # Convert rank (e.g., '1') to an integer

        for square in self.visible_squares:

            # If the square is a conflict square
            if square in conflict_sqrs:
                if position[square].colour != self.colour:
                    # potential capture - if not defended, we will check later
                    legal_moves.append(square)
                else:
                    continue
            else:
                # Can move to open squares - unless defended, we will check later
                legal_moves.append(square)

        self.legal_moves = legal_moves
        return legal_moves

class Board:
    def __init__(self, fen="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", active_colour="white"):

        self.opponent_controlled_squares = {}
        self.position = {}      # {"A1": "piece_obj", "A2": None, ...}
        
        self.legal_moves = {}
        self.white_legal_moves = {}
        self.black_legal_moves = {}    #{("rook", "black", "A1"): ["A2", "A3",...], ...}                                                                          

        self.fen = fen
        self.prev_move = None
        self.last_occupied_square = None

        self.active_colour = "white"
        self.white_castle_kingside_rights = True
        self.white_castle_queenside_rights = True
        self.black_castle_kingside_rights = True
        self.black_castle_queenside_rights = True
        self.en_passant_move = None
        self.halfmove_clock = 0
        self.movenumber = 1
        self.set_board_run = False

        self.white_king = None
        self.black_king = None
        self.in_check = False
        self.checking_pieces = []
        self.pinned_pieces = []
        self.checkmate = self.is_checkmate()
              

    def piece_from_char(self, char, square):
        """Helper function to return the correct piece object based on the FEN character."""

        colour = "white" if char.isupper() else "black"
        piece_char = char.lower()
        if piece_char == 'r':
            return Rook(colour, occupied_square=square)
        elif piece_char == 'n':
            return Knight(colour, occupied_square=square)
        elif piece_char == 'b':
            return Bishop(colour, occupied_square=square)
        elif piece_char == 'q':
            return Queen(colour, occupied_square=square)
        elif piece_char == 'k':
            return King(colour, occupied_square=square)
        elif piece_char == 'p':
            return Pawn(colour, occupied_square=square)
        return None

    def pinned_moves(self, pinned_piece, pinner, sqrs_to_king):
        """
        This piece has been detected as absolutely pinned (to king). It can only move where the pin remains
        """
        if pinned_piece.type == "knight":
            # no circumstances in which a knight can move
            return []

        potential_moves = []
        for square in sqrs_to_king:
            if square in pinned_piece.legal_moves:
                potential_moves.append(square)

        # add on the squares to the pinner including that square
        pinner_sqr = pinner.occupied_square
        pinned_piece_sqr = pinned_piece.occupied_square

        pinner_file = pinner_sqr[0]
        pinner_rank =  int(pinner_sqr[1])

        pinned_piece_file = pinned_piece_sqr[0]
        pinned_piece_rank = int(pinned_piece_sqr[1])

        # check if diagonal, file or rank pin
        if pinner_rank == pinned_piece_rank:

            # convert files to A=1, ..., H=8
            pinner_file_int = ord(pinner_file)-64
            pinned_piece_file_int = ord(pinned_piece_file)-64

            #shared file
            for file in range(min(pinned_piece_file_int, pinner_file_int), max(pinned_piece_file_int, pinner_file_int)):
                
                square = f"{pinned_piece_rank}{file}"
                if square in pinned_piece.legal_moves:
                    potential_moves.append(square)

        elif pinner_file == pinned_piece_file:
            # shared rank
            for rank in range(min(pinned_piece_rank, pinner_rank), max(pinned_piece_rank, pinner_rank)):
                
                square = f"{pinned_piece_file}{rank}"
                if square in pinned_piece.legal_moves:
                    potential_moves.append(square)
        
        else:   # diagonally pinned
            
            # rooks and pawns cant move when pinned diagonally
            if pinned_piece.type == "pawn" or pinned_piece.type == "rook":
                return []
            
            # get the direction of the pinner from the pinned square
            x = 1 if ord(pinned_piece_file) < ord(pinner_file) else -1
            y = 1 if pinned_piece_rank < pinner_rank else -1
            
            squares_apart = abs(pinned_piece_rank - pinner_rank)
            square_file = ord(pinned_piece_file) + x
            square_rank = pinned_piece_rank + y
            
            for i in range(1, squares_apart):
                square = f"{chr(square_file)}{square_rank}"
                if square in pinned_piece.legal_moves:
                    potential_moves.append(square)
                    square_file += x
                    square_rank += y
                    
                else:
                    break
                
        if pinned_piece.colour == "white":
            self.white_legal_moves[pinned_piece] = potential_moves
            
        elif pinned_piece.colour == "black":
            self.black_legal_moves[pinned_piece] = potential_moves
            

    def set_pinned_pieces(self):
        """
        Checks for pinned pieces by scanning rows, files, and diagonals from the king's position.
        
        Parameters:
        - king_square: The current position of the king (e.g., "E1")
        """
        
        if self.active_colour == "white":
            king = self.white_king
        else:
            king = self.black_king

        directions = [
            (1, 0),   # up (positive rank)
            (-1, 0),  # down (negative rank)
            (0, 1),   # right (positive file)
            (0, -1),  # left (negative file)
            (1, 1),   # up-right (diagonal)
            (-1, -1), # down-left (diagonal)
            (1, -1),  # up-left (diagonal)
            (-1, 1)   # down-right (diagonal)
        ]

        king_file, king_rank = ord(king.occupied_square[0]), int(king.occupied_square[1])

        # Check each direction
        for direction in directions:
            first_piece = None
            d_file, d_rank = direction
            squares_tracked = []


            
            # Move along the direction until hitting an edge or a second piece
            for i in range(1, 8):
                new_file = chr(king_file + d_file * i)
                new_rank = king_rank + d_rank * i
                
                
                # Ensure new square is within board limits
                if new_file < 'A' or new_file > 'H' or new_rank < 1 or new_rank > 8:
                    break  # Edge of the board

                # Generate new square name (e.g., "E4")
                new_square = f"{new_file}{new_rank}"
                squares_tracked.append(new_square)
                
                # Check if there is a piece on this square
                if self.position.get(new_square):
                    piece = self.position[new_square]

                    if first_piece is None:
                        # First piece found
                        first_piece = piece
                    else:
                        # Found second piece; determine pinning conditions
                        if piece.colour == first_piece.colour:
                            break  # Two friendly pieces found, stop

                        if piece.colour != first_piece.colour:
                            # Friendly then enemy - potential pin
                            
                            if first_piece.occupied_square in piece.legal_moves:
                                # valid pin
                                
                                self.pinned_pieces.append(first_piece)
                                pinned_moves = self.pinned_moves(pinned_piece=first_piece, pinner=piece, sqrs_to_king = squares_tracked)
                                first_piece.legal_moves = pinned_moves

                                if self.active_colour == "white":
                                    self.white_legal_moves[first_piece] = pinned_moves if pinned_moves else []
                                else:
                                    self.black_legal_moves[first_piece] = pinned_moves if pinned_moves else []
                                    
                                break  # Stop searching in this direction


    def is_checkmate(self):
        """
        checkmate checked upon initialisation.
        """
        self.set_legal_moves()
        self.set_pinned_pieces()
        
        # determine if king is under attack
        
        if self.active_colour == "white":
            king = self.white_king
            colour = "white"
            active_user_moves = self.white_legal_moves
            opponent_moves = self.black_legal_moves
        
        else:
            king = self.black_king
            colour = "black"
            opponent_moves = self.white_legal_moves
            active_user_moves = self.black_legal_moves

        for piece, moves in opponent_moves.items():
            if king.occupied_square in moves:
                self.checking_pieces.append(piece)
        
        if self.checking_pieces:
            self.in_check = True
        
        else:
            self.in_check = False
            return False
 
        # In check, so must amend legal moves to get out of it

        legal_moves = {}
 
        king_moves = active_user_moves[king]
        
        if king_moves:
            # eliminate king moves - those that are controlled
            king_move_set = set(king_moves)
            controlled_square_set = set(opponent_moves)

            intersection = king_move_set & controlled_square_set

            for square in intersection:
                king_moves.remove(square)
        
            # if any squares remain, it is not checkmate (at least not this turn)
            if king_moves:
                legal_moves[king] = king_moves

        # the only way to deny checkmate remaining is to capture the attacking piece (if this is only one) or block
        if len(self.checking_pieces) > 1 and not king_moves:

            # this cannot be blocked, the king cannot move so it is checkmate
            self.in_check = False
            return True

        # now we have determined that there is only one checking piece
        checking_piece = self.checking_pieces[0]
        
        # if the piece can be captured, it is not checkmate on this move
        if checking_piece.under_attack:
            for piece in checking_piece.under_attack:
                # add moves to capture the attacking piece
                legal_moves[piece] = [checking_piece.occupied_square]

        # determine if it being attacked on diagonal, row or file
        king_file = king.occupied_square[0]
        king_rank = king.occupied_square[1]
        
        piece_file = checking_piece.occupied_square[0]
        piece_rank = checking_piece.occupied_square[1]

        if king_file == piece_file:
            # share the same file

            start_rank = min(int(king_rank), int(piece_rank))      # integer of the smaller rank number
            end_rank = max(int(king_rank), int(piece_rank))     # integer of the larger rank number
            count_squares_between = end_rank - start_rank
            
            if count_squares_between == 1:
                # no squares to block, if no legal moves already - checkmate immediately
                if not legal_moves:
                    self.in_check = False
                    return True
                
                if self.active_colour == "white":
                    self.white_legal_moves = legal_moves
                    
                else: 
                    self.black_legal_moves = legal_moves
            
                return False
            
            blocking_squares = []
            for i in range(1, count_squares_between):
                blocking_squares.append(f"{king_file}{start_rank+i}")                     

        elif king_rank == piece_rank:
            # share the same rank
            king_int_file = ord(king_file)
            piece_int_file = ord(piece_file)
            
            start_file = min(int(king_int_file), int(piece_int_file))      # integer of the smaller file number
            end_file = max(int(king_int_file), int(piece_int_file))     # integer of the larger rank number
            count_squares_between = end_file - start_file 
            
            if count_squares_between == 1:
                # no squares to block, if no legal moves already - checkmate immediately
                if not legal_moves:
                    self.in_check = False
                    return True
            
                if self.active_colour == "white":
                    self.white_legal_moves = legal_moves
                    
                else: 
                    self.black_legal_moves = legal_moves
            
                return False
            
            blocking_squares = []
            for i in range(1, count_squares_between):
                # convert back to file letter
                file_chr = chr(start_file+i)
                blocking_squares.append(f"{file_chr}{king_rank}")

        else: # share the same diagonal
            
            # we can parse these squares and save those that have a rank and file between our king and piece squares

            # start with ranks, moving from the attacking piece to the king

            king_int_file = ord(king_file)
            piece_int_file = ord(piece_file)

            y_dir = 1 if int(king_rank) > int(piece_rank) else -1
            x_dir = 1 if king_int_file > piece_int_file else -1


            start_rank = min(int(king_rank), int(piece_rank))      # integer of the smaller rank number
            end_rank = max(int(king_rank), int(piece_rank))     # integer of the larger rank number
            count_ranks_between = end_rank - start_rank

            start_file = min(int(king_int_file), int(piece_int_file))      # integer of the smaller file number
            end_file = max(int(king_int_file), int(piece_int_file))     # integer of the larger rank number
            

            if count_ranks_between == 1:
                if not legal_moves:
                    self.in_check = False
                    return True
            
                if self.active_colour == "white":
                    self.white_legal_moves = legal_moves
                    
                else: 
                    self.black_legal_moves = legal_moves
                return False

            blocking_squares = []
            for i in range(1, count_ranks_between):
                validrank = int(piece_rank) + i*y_dir
                validfile = chr(piece_int_file + i*x_dir)
                
                blocking_squares.append(f"{validfile}{validrank}")
                

        # now we have the squares that can be blocked on, we can check if pieces can move there
        if not blocking_squares:
            if not legal_moves:
                self.in_check = False
                return True

            else:            
                if self.active_colour == "white":
                    self.white_legal_moves = legal_moves
                    
                else: 
                    self.black_legal_moves = legal_moves
            
                return False
                
        blocking_set = set(blocking_squares)
        
        for piece, moves in active_user_moves.items():
        
            intersection_moves = blocking_set & set(moves)  # squares that are blocking and have pieces able to move to

            if intersection_moves:
                if legal_moves.get(piece):
                    legal_moves[piece].append(intersection_moves)
                else:
                    legal_moves[piece] = intersection_moves
        

        if not legal_moves:
            self.in_check = False
            return True
    
        if self.active_colour == "white":
            self.white_legal_moves = legal_moves
            
        else: 
            self.black_legal_moves = legal_moves
    
        return False

    def set_board(self): 
        """Set up the board based on the provided FEN string"""

        # Split the FEN into its components
        fen_parts = self.fen.split()
    
        piece_placement = fen_parts[0]  # Board layout
        active_color = fen_parts[1]     # 'w' or 'b'
        castling_rights = fen_parts[2]  # KQkq
        en_passant = fen_parts[3]       # En passant target square
        halfmove_clock = fen_parts[4]   # Halfmove clock
        move_number = fen_parts[5]      # Full move number

        # 1. Set the active color
        self.active_colour = "white" if active_color == 'w' else "black"

        # 2. Set castling rights
        self.white_castle_kingside = 'K' in castling_rights
        self.white_castle_queenside = 'Q' in castling_rights
        self.black_castle_kingside = 'k' in castling_rights
        self.black_castle_queenside = 'q' in castling_rights

        # 3. Set en passant moves (if any)
        if en_passant != '-':
            self.en_passant_moves = en_passant.upper()
        else:
            self.en_passant_moves = None

        # 4. Set halfmove clock and move number
        self.halfmove_clock = int(halfmove_clock)
        self.movenumber = int(move_number)

        # 5. Set up the pieces on the board
        rows = piece_placement.split('/')
        ranks = 8  # Start from rank 8 and go down to 1

        for row in rows:
            file = 65  # ASCII value of 'A'
            for char in row:
                if char.isdigit():
                    # Empty squares, so move the file index forward and create empty squares with None
                    for _ in range(int(char)):
                        square = f"{chr(file)}{ranks}"
                        self.position[square] = None  # Empty square
                        file += 1  # Move to the next file
                else:
                    # Place the piece on the correct square
                    square = f"{chr(file)}{ranks}"
                    self.position[square] = self.piece_from_char(char, square)
                    
                    # Record the king squares while we're here
                    if char == "k":
                        self.black_king = self.position[square]
                    elif char == "K":
                        self.white_king = self.position[square]

                    file += 1  # Move to the next file
            ranks -= 1  # Move to the next rank

        self.set_board_run = True

    def get_destination_square(move):
        """
        Takes a move in algebraic notation and returns the square the piece is moved to.
        """
        move = move.replace('+', '').replace('#', '')  # Remove check or checkmate symbols
        
        # Handle castling
        if move == 'O-O':  # Kingside castling
            return 'g1' if '1' in move else 'g8'
        elif move == 'O-O-O':  # Queenside castling
            return 'c1' if '1' in move else 'c8'
        
        # Handle pawn promotion (e.g., e8=Q or e8Q)
        if '=' in move:
            move = move.split('=')[0]  # Remove the promotion part (e.g., 'e8=Q' -> 'e8')
        elif move[-1].isupper():
            move = move[:-1]  # Remove the promoted piece (e.g., 'e8Q' -> 'e8')

        # For normal moves, the last two characters indicate the destination square
        return move[-2:]  # Return the last two characters as the destination square

    
    def get_en_passant(self):

        # Assuming move exists - self.en_passant != None
        to_square = self.en_passant_move

        # the pawn must occupy one of the two squares adjacent
        file = to_square[0]  
        rank = to_square[1]

        if file not in "ABCDEFGH":
            raise ValueError("Error in check_en_passant rank")

        if rank not in ["4", "5"]:
            raise ValueError("Error in check_en_passant file")
        
        pawn_locations = [f"{chr(ord(file)-1)}{rank}", f"{chr(ord(file)+1)}{rank}"]

        potential_pawns = [
            ("pawn", self.active_colour, pawn_locations[0]),
            ("pawn", self.active_colour, pawn_locations[1]),
        ]

        return potential_pawns
        # return [("pawn", "white", "D5"), ("pawn", "white", "F5")]
        # then we can append E6 onto the moves for that piece, if it already exists in the legal moves dict

    def check_castle(self):
        if self.in_check:
            return False
        
        colour = self.active_colour

        if not getattr(self, f"{self.active_colour}_castle_kingside_rights") or getattr(self, f"{self.active_colour}_castle_queenside_rights"):
            return False
        
        castle_moves = {}

        if colour == "white":
            if self.white_castle_queenside_rights:
                
                w_queenside = True
                
                # check B1, C1, D1 are empty
                # check no black piece has C1, D1 in visible squares
                
                for piece in self.position.keys():
                    if piece[2] in ["B1", "C1", "D1"]:
                        # queenside castle blocked
                        w_queenside = False
                        break

                for squares in self.black_legal_moves.values():
                    if "B1" in squares or "C1" in squares:
                        # castling through or into check, cannot castle
                        w_queenside = False
                        break

                if w_queenside:
                    castle_moves[("king", "white", "E1")] = "C1"

            if self.white_castle_kingside_rights:
                
                w_kingside = True
                
                # check F1, G1 are empty
                # check no black piece has F1, G1 in visisble squares
                
                for piece in self.position.keys():
                    if piece[2] in ["F1", "G1"]:
                        # kingside castle blocked
                        w_kingside = False
                        break
                
                for squares in self.black_legal_moves.values():
                    if "F1" in squares or "G1" in squares:
                        # kingside castle blocked
                        w_kingside = False
                        break

                for squares in self.black_legal_moves.values():
                    if "F1" in squares or "G1" in squares:
                        # castling through or into check, cannot castle
                        w_kingside = False
                        break

                if w_kingside:
                    castle_moves[("king", "white", "E1")] = "G1"

        elif self.active_colour == "b":
            if self.black_castle_queenside_rights:
                
                b_queenside = True
                
                # check B8, C8, D8 are empty
                # check no black piece has C8, D8 in visible squares
                
                for piece in self.position.keys():
                    if piece[2] in ["B8", "C8", "D8"]:
                        # queenside castle blocked
                        b_queenside = False
                        break

                for squares in self.white_legal_moves.values():
                    if "B8" in squares or "C8" in squares:
                        # castling through or into check, cannot castle
                        b_queenside = False
                        break

                if b_queenside:
                    castle_moves[("king", "black", "E8")] = "C8"

            if self.black_castle_kingside_rights:
                
                b_kingside = True
                
                # check F8, G8 are empty
                # check no black piece has F8, G8 in visisble squares
                
                for piece in self.position.keys():
                    if piece[2] in ["F8", "G8"]:
                        # kingside castle blocked
                        b_kingside = False
                        break
                
                for squares in self.white_legal_moves.values():
                    if "F8" in squares or "G8" in squares:
                        # kingside castle blocked
                        b_kingside = False
                        break

                for squares in self.white_legal_moves.values():
                    if "F8" in squares or "G8" in squares:
                        # castling through or into check, cannot castle
                        b_kingside = False
                        break

                if b_kingside:
                    castle_moves[("king", "black", "E8")] = "G8"

    def set_legal_moves(self): # {["rook", "white", "A1"]: ["A2", "A3", ...], ...}
        """
        Gets all the ordinary moves for pieces, run after set_board
        """
        # reset object attributes
        self.white_legal_moves = {}
        self.black_legal_moves = {}

        legal_moves_dict = {}
        king_squares = {}   # keep track of these for later
        
        if not self.set_board_run:      # only want to run once, while legal_moves will happen more
            self.set_board()
        
        for square, piece in self.position.items():
            # {"A1": "Rook obj", ...}
            
            if not piece:
                # empty square
                continue
            
            conflict_squares = []
            
            # checking all the squares it could move to to see if it reaches an occupied square
            for visible_square in piece.visible_squares:
                if self.position.get(visible_square):
                    
                    # if this is triggered, we save the square as a conflict
                    conflict_squares.append(visible_square)

            if piece.type == "pawn":
                legal_moves = piece.get_legal_moves(position=self.position, en_passant=self.en_passant_move)
                        
            elif piece.type == "queen":
                legal_moves = piece.get_legal_moves(conflict_sqrs=conflict_squares, position=self.position)

            elif piece.type == "knight":
                legal_moves = piece.get_legal_moves(conflict_sqrs=conflict_squares, position=self.position)

            elif piece.type == "rook":
                legal_moves = piece.get_legal_moves(conflict_sqrs=conflict_squares, position=self.position)

            elif piece.type == "bishop":
                legal_moves = piece.get_legal_moves(conflict_sqrs=conflict_squares, position=self.position)
                
            elif piece.type == "king":
                legal_moves = piece.get_legal_moves(conflict_sqrs=conflict_squares, position=self.position)
                # wait until the rest of the pieces are set, so we can adjust for moves into check
                king_squares[square] = legal_moves
                setattr(self, f"{piece.colour}_king", piece)
                
            
            if piece.colour == "white":
                self.white_legal_moves[piece] = legal_moves
            
            else:
                self.black_legal_moves[piece] = legal_moves
                
            
            legal_moves_dict[piece] = legal_moves

        # now we can check kings legal moves for defended squares

        for square, moves in king_squares.items():

            king = self.position[square]
            valid_moves = []

            if not moves:
                king.legal_moves = []
                legal_moves_dict[king] = []
                if king.colour == "white":
                    self.white_legal_moves[king] = []
                else:
                    self.black_legal_moves[king] = []

            else:
                
                king_move_set = set(moves)
                # whether or not this square is occupied, we must check if it is controlled
                opposition_controlled_squares = getattr(self, f"{king.colour}_legal_moves")
                controlled_set = set()
                for squares in opposition_controlled_squares.values():
                    controlled_set.update(squares)
                illegal_moves = king_move_set.intersection(controlled_set)

                for square in moves:
                    if square not in illegal_moves:
                        valid_moves.append(square)
                

                king.legal_moves = valid_moves

                if king.colour == "white":
                    self.white_legal_moves[king] = valid_moves

                else:
                    self.black_legal_moves[king] = valid_moves
                       
        # assign piece object capture squares and under attack attributes
        white_piece_set = set(self.white_legal_moves)
        black_piece_set = set(self.black_legal_moves)
        
        for piece, squares in self.white_legal_moves.items():
            squares_set = set(squares)
            capture_squares = squares_set & black_piece_set
            piece.capture_squares = capture_squares
            for square in capture_squares:
                self.position[square].under_attack.append(piece)
            #print(piece, " capture squares: ", piece.capture_squares)
        for piece, squares in self.black_legal_moves.items():
            squares_set = set(squares)
            capture_squares = squares_set & white_piece_set
            piece.capture_squares = capture_squares
            for square in capture_squares:
                self.position[square].under_attack.append(piece)
            #print(piece, " capture squares: ", piece.capture_squares)

        # check for pins 
        self.set_pinned_pieces()
                
        # add en passant move if available
        if self.en_passant_move:
            en_passant_moves = self.get_en_passant()
            for pawn in en_passant_moves:
                if pawn in legal_moves_dict.keys():
                    legal_moves_dict[pawn].append(self.en_passant_move)

                    if self.active_colour == "white":
                        self.white_legal_moves[pawn].append(self.en_passant_move)
                    
                    else: 
                        self.black_legal_moves[pawn].append(self.en_passant_move)

        # add castle move if available
        castle_moves = self.check_castle()
        if castle_moves:
            for king, square in castle_moves:
                legal_moves_dict[king].append(square)
                getattr(self, f"{king[1]}_legal_moves")[king].append(square)
        
        self.legal_moves = legal_moves_dict

        
class Bot:
    def __init__(self):
        self.game_ongoing = False
        self.colour = None
        self.user_colour = None
        self.turn = None
        self.board = None

    def verify_move(self, move, board, user_colour):
        
        verification = {
            "verify_type": None,
            "verify_from_square": None,
            "verify_to_square": None,
            }
        
        parsed_move = algebraic_notation.parse_notation(move)
        print("parsing move: ", move, " -> ", parsed_move)
        
        parsed_move["piece"] = parsed_move["piece"].lower().strip()
        parsed_move["to"] = parsed_move["to"].upper().strip()

        # board state context may be needed
        from_sqr = parsed_move["from"]

        if isinstance(from_sqr, str) and len(from_sqr) == 2:     
            print("from square found: ", from_sqr)
            if from_sqr.upper() in all_squares:
                parsed_move["piece"] = parsed_move["piece"].lower()
                parsed_move["from"] = from_sqr.upper()
                return parsed_move
            else:
                return False

        else:
            # since the function parse_notation cannot know the starting square from the move along we must deduce it here
            
            parsed_move_from = parsed_move["from"]

            user_legal_moves = getattr(board, f"{user_colour}_legal_moves")    
            print("user legal moves: ", user_legal_moves)
            
            # iterate over the pieces to see if there is the same type with a to square in the key
            potential_moved_pieces = []
            
            for piece in user_legal_moves:
                if piece.type == parsed_move["piece"] and parsed_move["to"] in user_legal_moves[piece]:
                    potential_moved_pieces.append(piece)
            
            print("potential moved pieces: ", potential_moved_pieces)
            # in the case there are no pieces that can move to this square
            if len(potential_moved_pieces) == 0:
                return False

            elif len(potential_moved_pieces) == 1:
                piece = potential_moved_pieces[0]
                parsed_move["from"] = piece.occupied_square
                moved_piece = piece
                print("1 potential piece: ", piece, " parsed_move['from']: ", parsed_move["from"], "moved_piece = ", moved_piece)
            
            # if there is more than one piece that fits this criteria, we have to dig deeper to find out which is intended
            else: # > 1
                
                # there are 4 cases we must check and we must determine which is the case by the notation
                # two pieces on the same diagonal, we already have the square
                # the other case are that the pieces share a rank or a file, two pawns able to capture or multiple knights
                if parsed_move_from.isalpha():
                    # we have the unique file of the piece intended
                    
                    from_file = parsed_move_from.upper()
                    for piece in potential_moved_pieces:
                       
                        piece_file = piece.occupied_square
                        
                        if piece_file == from_file:
                            moved_piece = piece
                            parsed_move["from"] = piece.occupied_square
                            break

                    return False
                
                elif parsed_move_from.isnum():
                    # we habe the unique rank of the piece intended

                    from_rank = parsed_move_from
                    for piece in potential_moved_pieces:
                        
                        piece_rank = piece.occupied_square[1]

                        if piece_rank == from_rank:
                            moved_piece = piece
                            parsed_move["from"] = piece.occupied_square
                            break
                    
                    return False
        
        # so now we have the piece and its start and end position we can verify
        
        # first check that the piece exists on from square, is users piece and can access the landing square

        legal_moves = getattr(board, f"{moved_piece.colour}_legal_moves")
        
        if not parsed_move["to"] in legal_moves[moved_piece]:
            print("parsed_move[to] not in legal moves: ", parsed_move["to"], " not in ", legal_moves[moved_piece])
            return False
        print()
        print("Adjusted parsed move: ", parsed_move)
        return parsed_move

    def create_castle_rank(self, move, fen_rank):
        if move == ("king", "E1", "G1"):
            # white kingside castle
            new_rank = fen_rank[:5] + "1RK1"
        
        elif move == ("king", "E1", "C1"):
            # white queenside castle
            new_rank = "2KR1" + fen_rank[6:]

        elif move == ("king", "E8", "G8"):
            # black kingside castle
            new_rank = fen_rank[:5] + "1rk1"

        elif move == ("king", "E8", "C8"):
            # black queenside castle
            new_rank = "2kr1" + fen_rank[6:]
        
        else:
            raise ValueError("Error in create_castle_rank, move not in valid castling set")
        
        return new_rank

    def board_map(self, ranks):
        """ 
        Takes a list of ranks in FEN order: ["rnbqkbnr", "pppppppp", "8", "8", "8", "8", "PPPPPPPP", "RNBQKBNR"] and returns a dictionary of its parts:
        {
            8:{
            "A": "r",
            "B": "n",
            ...
            }
            
            7:{
            "A": "p"
            ...
            }
            ...
        }
        """
        files = ["A", "B", "C", "D", "E", "F", "G", "H"]

        # Mapping rank to a dictionary with files as keys and pieces as values (or 1 for empty squares)
        rank_map = {}
        for i in range(len(ranks)):
            row_dict = {}
            rank = ranks[i]
            file_idx = 0  # To track the file (A, B, C, ...)

            for char in rank:
                if char.isdigit():
                    # If it's a digit, it represents empty squares, assign 1 for empty spaces
                    for _ in range(int(char)):  # Repeat for the number of empty squares
                        row_dict[files[file_idx]] = 1
                        file_idx += 1  # Move to the next file
                else:
                    # Assign the piece to the current file
                    row_dict[files[file_idx]] = char
                    file_idx += 1  # Move to the next file

            # Assign the row dictionary to the rank (8 - i)
            rank_map[8 - i] = row_dict

        return rank_map

    def map_to_fen(self, rank_map):
        fen_rows = []
        
        for rank in range(8, 0, -1):  # Iterate from rank 8 down to 1
            row = rank_map[rank]
            fen_row = ""
            empty_count = 0
            
            for file in ["A", "B", "C", "D", "E", "F", "G", "H"]:
                if row[file] == 1:  # Detect empty squares
                    empty_count += 1
                else:
                    if empty_count > 0:
                        fen_row += str(empty_count)  # Add empty square count
                        empty_count = 0
                    fen_row += row[file]  # Add the piece (letter)
            
            # If the row ends with empty squares, add the count
            if empty_count > 0:
                fen_row += str(empty_count)
            
            fen_rows.append(fen_row)

        # Join the rows with '/' to create the full FEN string
        fen_string = "/".join(fen_rows)
        return fen_string

    def get_promotion(self, promotion_to, pawn):
        promotion_dict = {
            "P": {
                "Queen" :   "Q",
                "Rook"  :   "R",
                "Bishop":   "B",
                "Knight":   "N"
            },
            "p": {
                "Queen" :   "q",
                "Rook"  :   "r",
                "Bishop":   "b",
                "Knight":   "n"
            }
        }
        
        return promotion_dict[pawn][promotion_to]

    def update_fen(self, prev_fen, move):
        """
        takes a algebraic notation dict and the previous fen to create a new fen
        """
        new_fen_components = {
            "piece_placement": None,
            "active_colour": None,
            "castling_rights": None,
            "en_passant": None,
            "halfmove_clock": None,
            "move_number": None
        }
        print("running update_fen")
        move_tuple = (move["piece"].lower(), move["from"], move["to"])
        print("move tuple: ", move_tuple)
        # Split the FEN into its components
        fen_parts = prev_fen.split()
        piece_placement = fen_parts[0]  # Board layout
        active_color = fen_parts[1]     # 'w' or 'b'
        castling_rights = fen_parts[2]  # Castling rights
        en_passant = fen_parts[3]       # En passant target square
        halfmove_clock = fen_parts[4]   # Halfmove clock
        move_number = fen_parts[5]      # Full move number

        # toggle active colour
        new_fen_components["active_colour"] = "w" if active_color == "b" else "b"

        # increment move number
        new_fen_components["move_number"] = str(int(move_number) +1)

        # Board layout
        rows = piece_placement.split('/')       # rows = ["rnbqkbr", "pppppppp", "8", ...]
        
        # get the index of rows that contains our piece        
        piece_from_rank = rows[ int(move_tuple[1][1]) -1]   # One dictionary of files mapped to a piece (or a 1 if unoccupied)

        # Check for castling - we will need to move the rook ********************* needs fixing ************************
        castle_moves = [("king", "E1", "G1"), ("king", "E1", "C1"), ("king", "E8", "G8"), ("king", "E8", "C8")]
        if move_tuple in castle_moves:
            new_rank = self.create_castle_fen(self, move_tuple, fen_rank=piece_from_rank)
            rows[ int(move_tuple[1][1]) -1] = new_rank

            rows_str = "/".join(rows)

        else:
            # map the rows to their corresponding rank
            rank_map = self.board_map(rows)      # {8: {"A": "r", "B": "n", ...}, 7: {"A": "p", "B": "p", ...}, ... }
    
            parsed_from_rank = rank_map[int(move_tuple[1][1])] 

            if len(parsed_from_rank) != 8:
                raise(ValueError("Error in parsing FEN rank - from square"))        

            from_file = move_tuple[1][0].upper()     # "A" or "B" ...

            piece_char = parsed_from_rank[from_file]        # ="p" or "P" or "q" or "Q" etc.
            
            # check for promotion
            if move["promotion"]:
                piece_char = self.get_promotion(promotion_to=move["promotion"], pawn=piece_char)  
                
            # we can repeat the same steps to get the landing square index

            parsed_to_rank = rank_map[ int(move_tuple[2][1]) ]    # {"A": "1", "B": "1", ...}
            
            # check for promotion
            if move["promotion"]:
                piece_char = self.get_promotion(self, promotion_to=move["promotion"], pawn=piece_char)        

            if len(parsed_to_rank) != 8:
                raise(ValueError("Error in parsing FEN rank - to square"))        
            
            to_file = move_tuple[2][0].upper()      # "A" or "B" ...
            
            landing_char = parsed_to_rank[to_file]      # "1" or "2" ...

            new_to_rank = parsed_to_rank
            new_to_rank[to_file] = piece_char

            new_from_rank = parsed_from_rank
            new_from_rank[from_file] = 1

            rank_map[int(move_tuple[1][1])] = new_from_rank
            rank_map[int(move_tuple[2][1])] = new_to_rank
            
            # convert the rank strings back into FEN format
            rows_str = self.map_to_fen(rank_map)
                          
        # By this point, our new rows should be stored in rows
        
        new_fen_components["piece_placement"] = rows_str

        # update halfmove clock
        if landing_char != "1" or piece_char in ["p", "P"]:    
            # if capture or pawn move, reset clock
            new_fen_components["halfmove_clock"] = "0"
        
        else:
            new_fen_components["halfmove_clock"] = str(int(halfmove_clock) +1)

        # check for valid en passant moves
        # the last move had to be a pawn move to the 5th rank if it was black and 4th rank if it was white

        to_rank = move_tuple[2][1]
        from_rank = move_tuple[1][1]

        # pawn has to have move two squares off start square
        black_move_two = move_tuple[0] == "pawn" and active_color == "b" and to_rank == "5" and from_rank == "7"
        white_move_two = move_tuple[0] == "pawn" and active_color == "w" and to_rank == "4" and from_rank == "2"
            
        if black_move_two:
            
            # get adjacent files
            if to_file == "A":
                adj_files = [chr(ord(to_file)+1)]
            
            elif to_file == "H":
                adj_files = [chr(ord(to_file)-1)]
            
            else:
                adj_files = [chr(ord(to_file)-1), chr(ord(to_file)+1)]
                
            for file in adj_files:

                if new_to_rank[file] == "P":
                    # save en passant as the square behind the pawn
                    new_fen_components["en_passant"] = f"{move_tuple[2][0]}{int(move_tuple[2][1]) +1}"

            if not new_fen_components["en_passant"]:
                new_fen_components["en_passant"] = "-"


        elif white_move_two:
            # get adjacent files
            if to_file == "A":
                adj_files = [chr(ord(to_file)+1)]
            
            elif to_file == "H":
                adj_files = [chr(ord(to_file)-1)]
            
            else:
                adj_files = [chr(ord(to_file)-1), chr(ord(to_file)+1)]
            
            for file in adj_files:

                if new_to_rank[file] == "p":
                    # save en passant as the square behind the pawn
                    new_fen_components["en_passant"] = f"{move_tuple[2][0]}{int(move_tuple[2][1]) -1}"

            if not new_fen_components["en_passant"]:
                new_fen_components["en_passant"] = "-"
            
        else:
            new_fen_components["en_passant"] = "-" 

        # check for change in castling rights

        # Only things that change this is if the player moves the king - invalidates all rights, or a rook, invalidates one side

        if castling_rights == "-":
            new_fen_components["castling_rights"] = "-"
            
        elif active_color == "w" and ("K" in castling_rights or "Q" in castling_rights):

            if move_tuple[0] == "king":

                new_fen_components["castling_rights"] = castling_rights.replace("K", "").replace("Q", "")
            
            elif move_tuple[0] == "rook":

                if move_tuple[1] == "A1":
                    new_fen_components["castling_rights"] = castling_rights.replace("Q", "")

                else:
                    new_fen_components["castling_rights"] = castling_rights.replace("K", "")

            else:

                new_fen_components["castling_rights"] = castling_rights

        elif active_color == "b" and ("k" in castling_rights or "q" in castling_rights):
            if move_tuple[0] == "king":
                new_fen_components["castling_rights"] = castling_rights.replace("k", "").replace("q", "")
            
            elif move_tuple[0] == "rook":
                if move_tuple[1] == "A8":
                    new_fen_components["castling_rights"] = castling_rights.replace("q", "")

                else:
                    new_fen_components["castling_rights"] = castling_rights.replace("k", "")
            
            else:
                new_fen_components["castling_rights"] = castling_rights

        else:
            new_fen_components["castling_rights"] = castling_rights
            
        if new_fen_components["castling_rights"] == "":
            new_fen_components["castling_rights"] = "-"
            
        # now we can recombine the FEN parts and return the full str
        components = list(new_fen_components.values())
        new_fen = ' '.join(components)

        return new_fen

    def create_algebraic_notation(self, move):

        print("creating algebraic move from move=", move)

        validators = {
            "checkmate": None,
            "check": None,
            "kingsideCastle": None,
            "queensideCastle": None,
            "sharedRank": None,
            "sharedFile": None,
            "capture": None,
            "promotion": None         
            } 

        validators["capture"] = self.board.position.get(move[1])

        # check and checkmate
        # we will create tempoarary fen and board to get details - even though the move has not yet been validated

        temp_board = copy.deepcopy(self.board)
        piece_moved = move[0]
        
        # save the from square
        piece_from_sqr = piece_moved.occupied_square

        # update our board per this moved piece
        temp_board.position[piece_moved.occupied_square] = None
        
        # copy the piece and move to its new square
        temp_piece_moved = copy.deepcopy(piece_moved)
        temp_piece_moved.occupied_square = move[1]
        temp_board.position[temp_piece_moved.occupied_square] = temp_piece_moved

        validators["checkmate"] = temp_board.is_checkmate()
        validators["check"] = temp_board.in_check
        
        # -------------------- castling validation *************** needs amending **********************************
        # kingside castling
        if piece_from_sqr in ["E1", "E8"] and temp_piece_moved.type == "king" and move[1] in ["G1", "G8"]:
            if validators['checkmate']:
                return "O-O#"
            elif validators['check']:
                return "O-O+"
            else:
                return "O-O"

        # queenside castling
        elif piece_from_sqr in ["E1", "E8"] and temp_piece_moved.type == "king" and move[1] in ["C1", "C8"]:
            if validators['checkmate']:
                return "O-O-O#"
            elif validators['check']:
                return "O-O-O+"
            else:
                return "O-O-O"
        # -------------------------------------------------------


        #  -------- promotion validation - for now will just automatically promote to queen, parsed promotion TBC
        if move[0].type == "pawn" and move[1][1] == "8":
            validators['promotion'] = "queen"

        # -------- capture validation --------


        # -------- shared rank and/or file validation --------
        temp_piece_type = temp_piece_moved.type

        # get all pieces of this colour
        moves = getattr(temp_board, f"{temp_board.active_colour}_legal_moves")    # {("rook", "white", "A1"): ["A2", "A3", ...]}
       
        # first remove our intended move from other moves, will raise an error if it doesnt exist in dict
        del moves[temp_piece_moved]
        
        if moves:
            # check each piece to find the same type
            print("all moves of same colour: ", moves)
            all_valid_pieces = moves.keys()
            same_type_pieces = []
            
            for piece in all_valid_pieces:
                if piece.type == piece_moved.type and move[1] in piece.legal_moves:
                    same_type_pieces.append(piece)
            
            # if there are more than one piece type attacking square, we need to identify by file or rank or both

            # get the rank and file of our intended move from square
            file = piece_from_sqr[0]
            rank = piece_from_sqr[1]
            

            for piece in same_type_pieces:
                piece_file = piece.occupied_square[0]
                piece_rank = piece.occupied_square[1]

                if piece_file == file:
                    validators["sharedFile"] = True
                    print(piece, " and ", temp_piece_moved, "share the same file")
                    
                elif piece_rank == rank:
                    validators["sharedRank"] = True
                    print(piece, " and ", temp_piece_moved, "share the same rank")

        # create the string
        algebraic = ""
        # part 1: piece -> "Q", "q", "K", "k", ... (note: pawns are indicated by absence of this part)
        # part 2 (conditional): rank and/or file of piece if there is a conflict of possible moves
        # part 3 (conditional): x if it is a capture
        # part 4: landing square of the piece -> "b4"
        # part 5 (conditional): promotion "=Q"
        # part 6 (conditional): check -> "+", checkmate -> "#"

        alg_dict = {
            "queen": "q",
            "QUEEN": "Q",
            "pawn": "",
            "PAWN":"",
            "bishop": "b",
            "BISHOP": "B",
            "knight": "n",
            "KNIGHT": "N",
            "king": "k",
            "KING": "K",
            "rook": "r",
            "ROOK": "R"
            }

        # ----------------- from square (if necessary) ------------------
        print("\n SAME TYPE PIECES = ", same_type_pieces)
        if temp_piece_type == "pawn":
            if validators["capture"]:
                algebraic += f"{piece_from_sqr[0].lower()}x{move[1].lower()}"
                
        if not same_type_pieces:
            # there are no conflict so only need letter
            # search for the upper case in dict if white piece, lower if black
            if temp_piece_type != "pawn":
                algebraic += alg_dict[move[0].type.upper()] if self.board.active_colour == "white" else alg_dict[move[0].type.lower()] 

        # verify necessary additions to notation for multiple pieces that can occupy the square
        elif temp_piece_type == "knight":
            # if it is a knight and multiple could move to square
        
            algebraic += "N" if self.board.active_colour == "white" else "n"
            
            if validators["sharedRank"] and validators["sharedFile"]:
                algebraic += piece_from_sqr.lower()
            
            elif validators["sharedRank"] and not validators["sharedFile"]:
                algebraic += piece_from_sqr[0].lower()

            elif validators["sharedFile"] and not validators["sharedRank"]:
                algebraic += piece_from_sqr[1].lower()
            
            else:   # share neither
                algebraic += piece_from_sqr[0].lower()
        
        elif temp_piece_type == "queen" and moves:
            # if it is a queen and multiple could move to square
            algebraic += "Q" if self.board.active_colour == "white" else "q"

            # shared rank and file, add entire from square
            if validators["sharedRank"] and validators["sharedFile"]:
                algebraic += piece_from_sqr.lower()

            # share rank and not file, add from file letter
            elif validators["sharedRank"] and not validators["sharedFile"]:
                algebraic += piece_from_sqr[0].lower()

            # share file and not rank, add from rank number
            elif validators["sharedFile"] and not validators["sharedRank"]:
                algebraic += piece_from_sqr[1].lower()

        elif temp_piece_type == "rook":
            algebraic += "R" if self.board.active_colour == "white" else "r" 

            if validators["sharedFile"]:
                algebraic += piece_from_sqr[0].lower()

            elif validators["sharedRank"]:
                algebraic += piece_from_sqr[1].lower()

        elif temp_piece_type == "bishop":
            algebraic += "B" if self.board.active_colour == "white" else "b"

            if validators['sharedFile'] or validators['sharedRank']:
                algebraic +=piece_from_sqr[0].lower()
        
        # add "x" for captures
        if validators["capture"]:
            algebraic += "x"

        # add landing square
        algebraic += move[1].lower()

        # add promotion if necessary
        if validators["promotion"]:
            algebraic += f"={alg_dict[validators['promotion'].upper()]}" if self.board.active_colour == 'white' else f"={alg_dict[validators['promotion'].upper()]}"

        # add check or checkmate
        if validators["checkmate"]:
            algebraic += "#"
        
        if validators["check"]:
            algebraic += "+"

        print("ALGEBRAIC CONVERSION: ", algebraic)
        print("SELF.BOARD.POSITION: ", self.board.position)
        return algebraic

    def run_user_move(self):
        while True:
            move = input("Make move: ")
            # check that this move is algebraic notation
            if not algebraic_notation.is_valid_notation(move):
                print("Invalid move syntax. Your move must be in algebraic notation")
                continue

            # we must now check that the move is valid specific to our position
            move_verification = self.verify_move(move=move, board=self.board, user_colour=self.user_colour) # return algebraic_notation dictionary with to and from square filled in

            if not move_verification:
                print("Move invalid")  
                continue

            # create a new FEN
            new_fen = self.update_fen(prev_fen=self.board.fen, move=move_verification)
            print("new fen: ", new_fen)
            break
        
        return move_verification, new_fen




    def start_game(self):   
        
        board = Board()
        self.board = board
        self.game_ongoing = True
        # user pics a colour
        while True:
            user_colour = input("Play as white/black? ").lower()
            if user_colour == "black" or user_colour != "white":
                self.colour = "white"
                self.user_colour = "black"
                self.turn = True
                break
            
            elif user_colour == "white":
                self.colour = "black"
                self.user_colour = "white"
                self.turn = False
                break
            
            else:
                print("You must pick black or white")
                

    def make_move(self):
        legal_moves = getattr(self.board, f"{self.colour}_legal_moves")
        # {("rook", "white", "A1"): ["A2", "A3", ...]}    

        # here we can allow for analysis of position to decide a good move to play
        # ooooooooorrrrr randomly pick

        moveable_pieces = [piece for piece, moves in legal_moves.items() if moves]

        if moveable_pieces:
            piece_to_move = r.choice(moveable_pieces)
        
        squares = list(legal_moves[piece_to_move])
        
        move_to_square = r.choice(squares)
        print("piece to move: ", piece_to_move, "move to square: ", move_to_square, " squares: ", squares)
        return (piece_to_move, move_to_square)   # e.g. (Pawn obj, "E4")
    
    def get_checkmate(self):
        if self.board.checkmate:
            self.game_ongoing = False
            print("Game over.")

            if self.colour == self.board.active_colour:
                print("You won!")
                return True

            else:
                print("I won!")
                return True

    def game(self):
        while True:
            if not self.game_ongoing:
                self.start_game()

            if self.get_checkmate():
                break

            if not self.turn:
                print("white legal moves: \n", self.board.white_legal_moves)
                move, new_fen = self.run_user_move()    # move = algebraic_notation dictionary with to and from squares filled in
                
                # After receiving users move, create a new board object, update attributes
                new_board = Board(fen=new_fen, active_colour=self.colour)
                self.board = new_board
                self.fen = new_fen
                self.turn = True
                
                if self.get_checkmate():
                    break

                print("black legal moves: \n", self.board.black_legal_moves)
                
            move = self.make_move()
            print("My move is: ", move)

            algebraic_move = self.create_algebraic_notation(move)
            print("bot algebraic move: ", algebraic_move)
            
            print()
            print("RUNNING VERIFY_MOVE FOR BOT")
            move_verification = self.verify_move(move=algebraic_move, board=self.board, user_colour=self.colour)
            print("bot parsed_move: ", move_verification)
            
            print()
            print("RUNNING UPDATE FEN FOR BOT")
            new_fen = self.update_fen(prev_fen=self.board.fen, move=move_verification)
            print("fen after bot move = ", new_fen)
            
            new_board = Board(fen=new_fen)
            self.board = new_board
            self.fen = new_fen
            self.turn = False
                    

bot = Bot()
bot.game()
