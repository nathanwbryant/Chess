import algebraic_utils
import random as r
import copy
from fen_utils import board_map, map_to_fen

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
        self.conflict_squares = []
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
        Legal squares is a list of squares the piece could move to if the board was empty, conflict squares 
        are the locations of other pieces on the board and capture squares are conflict squares with
        opposition pieces on.
        """
        legal_moves = []
        self.conflict_squares = conflict_sqrs
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
                    # If the square is empty, it's a legal move
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

    def get_legal_moves(self, position, en_passant_target):
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
                    

        if en_passant_target:
            en_passant_file = ord(en_passant_target[0])
            en_passant_rank = int(en_passant_target[1])
            # Check if pawn is on the correct rank and can capture en passant
            if rank == en_passant_rank - (1 if self.colour == "white" else -1):
                if ord(file) in [en_passant_file - 1, en_passant_file + 1]:
                    valid_moves.append(en_passant_target)

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
                        legal_moves.append(square)

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
        return diagonals[self.occupied_square] if self.occupied_square else []

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

class FENParser:
    def __init__(self, fen_string):
        self.fen_string = fen_string
        self.position = {}
        self.active_colour = ''
        self.castling_rights = ''
        self.white_castle_kingside_rights = ''
        self.white_castle_queenside_rights = ''
        self.black_castle_kingside_rights = ''
        self.black_castle_queenside_rights = ''
        self.en_passant_target = ''
        self.halfmove_clock = 0
        self.fullmove_number = 0
        self.white_king = None
        self.white_king_square = None
        self.black_king = None
        self.black_king_square = None
        self.parse_fen()

    def parse_fen(self):
        # Split the FEN into its components
        fen_parts = self.fen_string.split()

        if len(fen_parts) != 6:
            raise ValueError("Invalid FEN string: Incorrect number of fields")
    
        piece_placement = fen_parts[0]  # Board layout
        active_color = fen_parts[1]     # 'w' or 'b'
        castling_rights = fen_parts[2]  # KQkq
        en_passant = fen_parts[3]       # En passant target square
        halfmove_clock = fen_parts[4]   # Halfmove clock
        move_number = fen_parts[5]      # Full move number

        # 1. Set the active color
        if active_color not in ('w', 'b'):
            raise ValueError("Invalid active color: must be 'w' or 'b'")
        self.active_colour = "white" if active_color == 'w' else "black"

        # 2. Set castling rights
        self.castling_rights = castling_rights
        self.white_castle_kingside_rights = True if 'K' in castling_rights else False
        self.white_castle_queenside_rights = True if 'Q' in castling_rights else False
        self.black_castle_kingside_rights = True if 'k' in castling_rights else False
        self.black_castle_queenside_rights = True if 'q' in castling_rights else False

        # 3. Set en passant moves (if any)
        if en_passant != '-':
            self.en_passant_target = en_passant.upper()
        else:
            self.en_passant_target = None

        # 4. Set halfmove clock and move number
        try:
            self.halfmove_clock = int(halfmove_clock)
            self.fullmove_number = int(move_number)
        except ValueError:
            raise ValueError("Halfmove clock and fullmove number must be integers")

        # 5. Set up the pieces on the board
        rows = piece_placement.split('/')
        if len(rows) != 8:
            raise ValueError("Invalid piece placement data: must have 8 rows")
        ranks = 8  # Start from rank 8 and go down to 1

        for row in rows:
            file = 65  # ASCII value of 'A'
            file_count = 0
            for char in row:
                if char.isdigit():
                    # Empty squares, so move the file index forward and create empty squares with None
                    for _ in range(int(char)):
                        square = f"{chr(file)}{ranks}"
                        self.position[square] = None  # Empty square
                        file += 1  # Move to the next file
                        file_count += 1
                elif char.isalpha():
                    # Place the piece on the correct square
                    square = f"{chr(file)}{ranks}"
                    self.position[square] = PieceFactory.create_piece(char, square)
                    
                    # Record the king squares while we're here
                    if char == "k":
                        self.black_king = self.position[square]
                        self.black_king_square = square

                    elif char == "K":
                        self.white_king = self.position[square]
                        self.black_king_square = square

                    file += 1  # Move to the next file
                    file_count += 1
                else:
                    raise ValueError(f"Invalid character in piece placement: {char}")
            if file_count != 8:
                raise ValueError("Invalid piece placement data: each row must have exactly 8 columns")
            ranks -= 1  # Move to the next rank
    
    def get_position(self):
        return self.position

    def get_active_colour(self):
        return self.active_colour

    def get_castling_rights_str(self):
        return self.castling_rights

    def get_castling_rights(self, colour, side):
        return getattr(self, f"{colour}_castle_{side}_rights")

    def get_en_passant_target(self):
        return self.en_passant_target

    def get_halfmove_clock(self):
        return self.halfmove_clock

    def get_fullmove_number(self):
        return self.fullmove_number
    
    def get_king(self, colour):
        return getattr(self, f"{colour}_king")

class PieceFactory:
    PIECE_MAP = {
        'r': Rook,
        'n': Knight,
        'b': Bishop,
        'q': Queen,
        'k': King,
        'p': Pawn,
    }

    @staticmethod
    def create_piece(char, square):
        colour = "white" if char.isupper() else "black"
        piece_char = char.lower()
        piece_class = PieceFactory.PIECE_MAP.get(piece_char)
        if piece_class:
            return piece_class(colour, occupied_square=square)
        else:
            raise ValueError(f"Unknown piece character: {char}")

class LegalMoveGenerator:
    def __init__(self, position, active_colour, en_passant_target, castling_rights, opp_king):
        self.position = position
        self.active_colour = active_colour
        self.en_passant_target = en_passant_target
        self.castling_rights = castling_rights
        self.opp_king = opp_king
        self.in_check = False
        self.is_checkmate = False
        self.checking_pieces = []

        # These will store the results
        self.white_legal_moves = {}
        self.black_legal_moves = {}
        self.legal_moves = {}
        self.white_king = None
        self.black_king = None
        self.generate_legal_moves()
        
    def generate_legal_moves(self):
        """
        Generates all legal moves for the current board position.
        """
        king_squares = {}   # Keep track of kings for later

        for square, piece in self.position.items():
            if not piece:
                continue  # Empty square

            conflict_squares = []

            # Identify conflict squares (squares occupied by any piece)
            for visible_square in piece.visible_squares:
                if self.position.get(visible_square):
                    conflict_squares.append(visible_square)

            # Get legal moves based on piece type
            if piece.type == "pawn":
                legal_moves = piece.get_legal_moves(position=self.position, en_passant_target=self.en_passant_target)
            elif piece.type in ["queen", "rook", "bishop", "knight"]:
                legal_moves = piece.get_legal_moves(conflict_sqrs=conflict_squares, position=self.position)
            elif piece.type == "king":
                legal_moves = piece.get_legal_moves(conflict_sqrs=conflict_squares, position=self.position)
                king_squares[square] = legal_moves
                setattr(self, f"{piece.colour}_king", piece)
            else:
                # Handle other piece types if necessary
                legal_moves = []

            # Store legal moves
            if piece.colour == "white":
                self.white_legal_moves[piece] = legal_moves
            else:
                self.black_legal_moves[piece] = legal_moves

        # Handle king moves to avoid moving into check
        self.adjust_king_moves(king_squares)

        # Assign capture squares and under attack attributes
        self.assign_capture_and_attack_squares()

        # Handle checks
        self.handle_checks()

        # Handle en passant moves
        if self.en_passant_target:
            passant_pawns = self.find_en_passant_moves()

            if passant_pawns:
                if self.active_colour == "white":
                    for piece in passant_pawns:
                        self.white_legal_moves[piece].append(self.en_passant_target)

                else:
                    for piece in passant_pawns:
                        self.white_legal_moves[piece].append(self.en_passant_target)

        # Handle pinned pieces
        self.handle_pinned_pieces()

        # Handle castling moves
        self.handle_castling_moves()

    def handle_checks(self):
        
        print("handling checks...")
        checking_pieces = []
        colour = "white" if self.active_colour == "white" else "black"
        king = getattr(self, f"{colour}_king")
        opp_colour = "white" if self.active_colour == "black" else "black"
        opp_legal_moves = getattr(self, f"{opp_colour}_legal_moves")

        for piece, moves in opp_legal_moves.items():
            if king.occupied_square in moves:
                checking_pieces.append(piece)

        print("checking pieces: ", checking_pieces)
        if checking_pieces:
            print("checking pieces detected, setting self to in check...")
            self.in_check = True
            self.checking_pieces = checking_pieces
            moves = self.generate_in_check_moves()

            if not moves:
                self.is_checkmate = True

            if self.active_colour == "white":
                self.white_legal_moves = moves
            else:
                self.black_legal_moves = moves

    def adjust_king_moves(self, king_squares):
        for square, moves in king_squares.items():
            king = self.position[square]
            valid_moves = []

            if not moves:
                king.legal_moves = []
                if king.colour == "white":
                    self.white_legal_moves[king] = []
                else:
                    self.black_legal_moves[king] = []
            else:
                king_move_set = set(moves)
                # Determine the opponent's controlled squares
                opposition_moves = self.black_legal_moves if king.colour == "white" else self.white_legal_moves
                controlled_set = set()
                for squares in opposition_moves.values():
                    controlled_set.update(squares)
                illegal_moves = king_move_set.intersection(controlled_set)

                for move in moves:
                    if move not in illegal_moves:
                        valid_moves.append(move)

                king.legal_moves = valid_moves
                if king.colour == "white":
                    self.white_legal_moves[king] = valid_moves
                else:
                    self.black_legal_moves[king] = valid_moves

    def assign_capture_and_attack_squares(self):
        white_pieces_positions = {piece.occupied_square for piece in self.white_legal_moves.keys()}
        black_pieces_positions = {piece.occupied_square for piece in self.black_legal_moves.keys()}

        for piece, moves in self.white_legal_moves.items():
            capture_squares = set(moves) & black_pieces_positions
            piece.capture_squares = capture_squares
            for square in capture_squares:
                target_piece = self.position[square]
                if target_piece:
                    target_piece.under_attack.append(piece)

        for piece, moves in self.black_legal_moves.items():
            capture_squares = set(moves) & white_pieces_positions
            piece.capture_squares = capture_squares
            for square in capture_squares:
                target_piece = self.position[square]
                if target_piece:
                    target_piece.under_attack.append(piece)

    def find_en_passant_moves(self):
        
        to_square = self.en_passant_target
        valid_pawns = []

        # the pawn must occupy one of the two squares adjacent
        file = to_square[0]  
        rank = to_square[1]

        if file not in "ABCDEFGH":
            raise ValueError("Error in check_en_passant rank")

        if rank not in ["3", "6"]:
            raise ValueError("Error in check_en_passant file")
        
        squares = [f"{chr(ord(file)-1)}{rank}", f"{chr(ord(file)+1)}{rank}"]

        for square in squares:
            piece = self.position.get(square)
            if piece:
                if piece.type == "pawn" and piece.colour == self.active_colour:
                    valid_pawns.append(piece)
            
        return valid_pawns

    def get_attacked_squares(self, opponent_moves):
        attacked_squares = set()
        for piece_moves in opponent_moves.values():
            attacked_squares.update(piece_moves)
        return attacked_squares

    def handle_castling_moves(self):
        if self.in_check:
            return False

        colour = self.active_colour

        if not self.castling_rights:
            return False

        castle_moves = {}

        # Get all squares attacked by the opponent
        if colour == "white":
            opponent_moves = self.black_legal_moves
            king = self.white_king
        else:
            opponent_moves = self.white_legal_moves
            king = self.black_king

        attacked_squares = self.get_attacked_squares(opponent_moves)

        if colour == "white":
            # White's castling
            if "Q" in self.castling_rights:
                w_queenside = True

                # Check that squares between king and rook are empty
                for square in ["B1", "C1", "D1"]:
                    if self.position[square]:
                        w_queenside = False
                        break

                # Check that squares the king passes through are not attacked
                for square in ["D1", "C1"]:
                    if square in attacked_squares:
                        w_queenside = False
                        break

                # Check that the king would not end up in check
                if "C1" in attacked_squares:
                    w_queenside = False

                if w_queenside:
                    # Update the king's legal moves
                    if king in self.white_legal_moves:
                        self.white_legal_moves[king].append("C1")
                    else:
                        self.white_legal_moves[king] = ["C1"]

            if "K" in self.castling_rights:
                w_kingside = True

                # Check that squares between king and rook are empty
                for square in ["F1", "G1"]:
                    if self.position[square]:
                        w_kingside = False
                        break

                # Check that squares the king passes through are not attacked
                for square in ["F1", "G1"]:
                    if square in attacked_squares:
                        w_kingside = False
                        break

                # Check that the king would not end up in check
                if "G1" in attacked_squares:
                    w_kingside = False

                if w_kingside:
                    # Update the king's legal moves
                    if king in self.white_legal_moves:
                        self.white_legal_moves[king].append("G1")
                    else:
                        self.white_legal_moves[king] = ["G1"]

        else:
            # Black's castling
            if "q" in self.castling_rights:
                b_queenside = True

                for square in ["B8", "C8", "D8"]:
                    if self.position[square]:
                        b_queenside = False
                        break

                for square in ["D8", "C8"]:
                    if square in attacked_squares:
                        b_queenside = False
                        break

                if "C8" in attacked_squares:
                    b_queenside = False

                if b_queenside:
                    if king in self.black_legal_moves:
                        self.black_legal_moves[king].append("C8")
                    else:
                        self.black_legal_moves[king] = ["C8"]

            if "k" in self.castling_rights:
                b_kingside = True

                for square in ["F8", "G8"]:
                    if self.position[square]:
                        b_kingside = False
                        break

                for square in ["F8", "G8"]:
                    if square in attacked_squares:
                        b_kingside = False
                        break

                if "G8" in attacked_squares:
                    b_kingside = False

                if b_kingside:
                    if king in self.black_legal_moves:
                        self.black_legal_moves[king].append("G8")
                    else:
                        self.black_legal_moves[king] = ["G8"]


    def pinned_moves(self, pinned_piece, pinner, sqrs_to_king):
        """
        This piece has been detected as absolutely pinned (to king). It can only move where the pin remains
        """
        if pinned_piece.type == "knight":
            # Knights cannot move when pinned
            return []

        potential_moves = []

        # Add squares between pinned piece and king if they are in legal moves
        for square in sqrs_to_king:
            if square in pinned_piece.legal_moves:
                potential_moves.append(square)

        # Extract positions
        pinner_sqr = pinner.occupied_square
        pinned_piece_sqr = pinned_piece.occupied_square

        pinner_file = pinner_sqr[0]
        pinner_file_int = ord(pinner_file.upper()) - 64
        pinner_rank = int(pinner_sqr[1])

        pinned_piece_file = pinned_piece_sqr[0]
        pinned_file_int = ord(pinned_piece_file.upper()) - 64
        pinned_piece_rank = int(pinned_piece_sqr[1])

        if pinner_rank == pinned_piece_rank:
            # Shared rank (horizontal pin)
            # Determine direction
            step = 1 if pinner_file_int > pinned_file_int else -1
            for file_int in range(pinned_file_int + step, pinner_file_int + step, step):
                file = chr(file_int + 64)
                square = f"{file}{pinned_piece_rank}"
                if square in pinned_piece.legal_moves:
                    potential_moves.append(square)

        elif pinner_file == pinned_piece_file:
            # Shared file (vertical pin)
            # Determine direction
            step = 1 if pinner_rank > pinned_piece_rank else -1
            for rank in range(pinned_piece_rank + step, pinner_rank + step, step):
                square = f"{pinned_piece_file}{rank}"
                if square in pinned_piece.legal_moves:
                    potential_moves.append(square)

        else:  # Diagonal pin
            # Rooks and pawns can't move when pinned diagonally
            if pinned_piece.type == "rook":
                return []

            if pinned_piece.type == "pawn":
                if pinner.occupied_square in pinned_piece.legal_moves:
                    return [pinner.occupied_square]
                else:
                    return []

            # Determine direction
            file_step = 1 if pinner_file_int > pinned_file_int else -1
            rank_step = 1 if pinner_rank > pinned_piece_rank else -1
            num_squares = abs(pinner_file_int - pinned_file_int)

            for i in range(1, num_squares + 1):
                file_int = pinned_file_int + (file_step * i)
                rank = pinned_piece_rank + (rank_step * i)
                file = chr(file_int + 64)
                square = f"{file}{rank}"
                if square in pinned_piece.legal_moves:
                    potential_moves.append(square)

        # Update the piece's legal moves
        pinned_piece.legal_moves = potential_moves

        return potential_moves


    def handle_pinned_pieces(self):
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

                                pinned_moves = self.pinned_moves(pinned_piece=first_piece, pinner=piece, sqrs_to_king = squares_tracked)
                                first_piece.legal_moves = pinned_moves

                                if self.active_colour == "white":
                                    self.white_legal_moves[first_piece] = pinned_moves if pinned_moves else []
                                else:
                                    self.black_legal_moves[first_piece] = pinned_moves if pinned_moves else []
                                    
                                break  # Stop searching in this direction

    def generate_in_check_moves(self):
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
        if len(self.checking_pieces) > 1:
            if not king_moves:
                # this cannot be blocked, the king cannot move so it is checkmate
                return legal_moves

            else:
                return {king: king_moves}


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
                # no squares to block, either capture or move king
                return legal_moves
            
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
                return legal_moves
            
            blocking_squares = []
            for i in range(1, count_ranks_between):
                validrank = int(piece_rank) + i*y_dir
                validfile = chr(piece_int_file + i*x_dir)
                
                blocking_squares.append(f"{validfile}{validrank}")
                

        # now we have the squares that can be blocked on, we can check if pieces can move there
        if not blocking_squares:
            return legal_moves
                
        blocking_set = set(blocking_squares)
        
        for piece, moves in active_user_moves.items():
        
            intersection_moves = blocking_set & set(moves)  # squares that are blocking and have pieces able to move to

            if intersection_moves:
                if legal_moves.get(piece):
                    legal_moves[piece].append(intersection_moves)
                else:
                    legal_moves[piece] = intersection_moves
        
        return legal_moves

    def get_check_status(self):
        return self.in_check
    
    def get_checkmate_status(self):
        print("getting check status...", self.in_check)
        return self.is_checkmate
    
    def get_legal_moves(self, colour):
        return getattr(self, f"{colour}_legal_moves")





class Board:
    def __init__(self, fen="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"):

        self.fen_parser = FENParser(fen)
        self.position = self.fen_parser.get_position()
        self.active_colour = self.fen_parser.get_active_colour()
        self.castling_rights = self.fen_parser.get_castling_rights_str()
        self.white_castle_kingside_rights = self.fen_parser.get_castling_rights("white", "kingside")
        self.white_castle_queenside_rights = self.fen_parser.get_castling_rights("white", "queenside")
        self.black_castle_kingside_rights = self.fen_parser.get_castling_rights("black", "kingside")
        self.black_castle_queenside_rights = self.fen_parser.get_castling_rights("black", "queenside")
        self.en_passant_target = self.fen_parser.get_en_passant_target()
        self.halfmove_clock = self.fen_parser.get_halfmove_clock()
        self.fullmove_number = self.fen_parser.get_fullmove_number()                                                      

        self.fen = fen
        self.prev_move = None
        self.last_occupied_square = None

        self.white_king = self.fen_parser.get_king("white")
        self.black_king = self.fen_parser.get_king("black")

        self.move_generator = LegalMoveGenerator(
            position=self.position, 
            active_colour=self.active_colour, 
            en_passant_target=self.en_passant_target,
            castling_rights=self.castling_rights,
            opp_king=self.white_king if self.active_colour == "black" else self.black_king
            )
        
        self.move_generator.generate_legal_moves()
        
        self.in_check = self.move_generator.get_check_status()
        self.is_checkmate = self.move_generator.get_checkmate_status()
        self.white_legal_moves = self.move_generator.get_legal_moves("white")
        self.black_legal_moves = self.move_generator.get_legal_moves("black")

        
class Bot:
    def __init__(self):
        self.game_ongoing = False
        self.colour = None
        self.user_colour = None
        self.turn = None
        self.board = None

    def run_user_move(self):
        while True:
            move = input("Make move: ")
            # check that this move is algebraic notation
            if not algebraic_utils.is_valid_notation(move):
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
                    

# bot = Bot()
# bot.game()
