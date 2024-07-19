import chess

UNICODE_PIECE_SYMBOLS = {
    "r": "♖", "R": "♜",
    "n": "♘", "N": "♞",
    "b": "♗", "B": "♝",
    "q": "♕", "Q": "♛",
    "k": "♔", "K": "♚",
    "p": "♙", "P": "♟",
}

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

def pieces_positions(fen):
    # FEN starts at square A8 then B8... then A7, A6... so rank descends and file letter (number) ascends
    rank = 8
    file_num = ord("A")-64  # starts at 1
    
    positions = {}

    for i in fen:
        
        if i.isnumeric():
            file_num += int(i) if file_num+int(i)<8 else 1
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
            positions[f"{chr(file_num+64)}{rank}"] = "b King"
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
    # takes in a dict in the format {"A1": "w rook"} and a piece as in the value and returns a list of all positions

class Position:
    def __init__(self, fen):
        self._fen = fen

    def str(self):
        print("--------------------------------------------------------")

        for square in self._fen:
            if square == "/":
                print("|")
                print("--------------------------------------------------------")
            elif square == " ":
                print("|")
                print("--------------------------------------------------------")
                break
            elif square.isnumeric():
                for i in range(int(square)):
                    print("|      ", end="")
            else:
                print(f"|  {UNICODE_PIECE_SYMBOLS[square]}   ", end="")



    @property
    def fen(self):
        return self._fen
    
board = Position("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
board.str()

class Piece:
    def __init__(self, type, fen, square):
        self.type = type
        self.square = square

    #def legal_moves(self, position):

class Bot:
    def __init__(self, fen, colour):
        pass

    def identify_defensive_threats(fen, colour):
        # input of the colour of the opposition, identify attacking moves
        pass

class Tactics:
    def __init__(self, piece, fen):
        self.piece_location = pieces_positions(fen)  #{"A1": "w rook", ...}

    def current_position(self, fen):
        piece_locations = pieces_positions(fen)

    def pin_piece(piece, fen):
        pass
    

diagonals = [
    {
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
    ]
