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
    
    positions = {}

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
    conflict_rank_num, conflict_file_num = conflict_square_coords
    origin_rank_num, origin_file_num = square_coords

    # Ensure coords are on the same rank only
    if not abs(conflict_file_num - origin_file_num) > 0 or not abs(conflict_rank_num - origin_rank_num) == 0:
        raise ValueError("Coordinates are not on the same rank")
    
    # Determine the direction from origin square
    if origin_file_num < conflict_file_num:
        direction = "ascending"
    
    else:
        direction = "descending"

    # Generate all coordinates on the same rank
    result = []
    for d in range(1,8):
        if direction == "ascending":
            new_file_num = conflict_file_num + d
        
        elif direction == "descending":
            new_file_num = conflict_file_num - d

        if 0 < new_file_num <= 8:
            result.append(f"{chr(origin_rank_num+64)}{new_file_num}")

        else: 
            break

    return result  

def coordinates_on_same_file(square_coords, conflict_square_coords):
    conflict_rank_num, conflict_file_num = conflict_square_coords
    origin_rank_num, origin_file_num = square_coords

    # Ensure coords are on the same file only
    if not abs(conflict_rank_num - origin_rank_num) > 0 or not abs(conflict_file_num - origin_file_num) == 0:
        raise ValueError("Coordinates are not on the same file")
    
    # Determine the direction from origin square
    if origin_rank_num < conflict_rank_num:
        direction = "ascending"
    
    else:
        direction = "descending"

    # Generate all coordinates on the same rank
    result = []
    for d in range(1,8):
        if direction == "ascending":
            new_rank_num = conflict_rank_num + d
        
        elif direction == "descending":
            new_rank_num = conflict_rank_num - d

        if 0 < new_rank_num <= 8:
            result.append(f"{chr(new_rank_num+64)}{origin_file_num}")

        else: 
            break

    return result  



class Piece:
    def __init__(self):
        self.piece_locations = None

    #sets a new current position
    def set_current_positions(self, fen):
        self.piece_locations = pieces_positions(fen)

    def get_current_position(self):
        return self.square

    
class Queen:
    def __init__(self, colour):
        
        self.type = "queen"
        self.colour = colour

    def visible_squares(self, square):
        # the queen can see all squares on it's rank and file as well as diagonals
        list_of_squares = []
        rank = list(square)[0]
        file = list(square)[1]
        
        #append all on the same rank
        for i in range(8):
            list_of_squares.append(f"{rank}{i+1}")
        list_of_squares.remove(square)
        
        #append all on the same file
        for j in ["A", "B", "C", "D", "E", "F", "G", "H"]:
            list_of_squares.append(f"{j}{file}")
        list_of_squares.remove(square)

        #append all on the same diagonals
        diagonals_visible = diagonals[square]
        for square in diagonals_visible:
            list_of_squares.append(square)
        
        return list_of_squares

    def can_attack(self, square, colour):
        pass
        # limit visible squares based on other pieces in the position

class Pawn:
    def __init__(self, colour):
        self.type = "pawn"
        self.colour = colour
        self.moves = 0

    def visible_squares(self, square):
        list_of_squares = []
        rank = list(square)[0]
        file = list(square)[1]
        if self.colour == "white" and (rank != "A" or rank != "H"):
            list_of_squares.append(f"{chr(ord(rank)-1)}{int(file)+1}")
            list_of_squares.append(f"{rank}{int(file)+1}")
            list_of_squares.append(f"{chr(ord(rank)+1)}{int(file)+1}")
        
        elif self.colour == "white" and rank == "A":
            list_of_squares.append(f"{rank}{int(file)+1}")
            list_of_squares.append(f"{chr(ord(rank)+1)}{int(file)+1}")

        elif self.colour == "white" and rank == "H":
            list_of_squares.append(f"{chr(ord(rank)-1)}{int(file)+1}")
            list_of_squares.append(f"{rank}{int(file)+1}")

        elif self.colour == "black" and (rank != "A" and rank != "H"):
            list_of_squares.append(f"{chr(ord(rank)-1)}{int(file)-1}")
            list_of_squares.append(f"{rank}{int(file)-1}")
            list_of_squares.append(f"{chr(ord(rank)+1)}{int(file)-1}")
        
        elif self.colour == "black" and rank == "A":
            list_of_squares.append(f"{rank}{int(file)+1}")
            list_of_squares.append(f"{chr(ord(rank)+1)}{int(file)+1}")

        elif self.colour == "black" and rank == "H":
            list_of_squares.append(f"{chr(ord(rank)-1)}{int(file)+1}")
            list_of_squares.append(f"{rank}{int(file)+1}")




        return list_of_squares

    def can_attack(self, square, colour):
        list_of_squares = []
        rank = list(square)[0]
        file = list(square)[1]


        if colour == "white":
            list_of_squares.append(f"{chr(ord(rank)-1)}{int(file)+1}")
            list_of_squares.append(f"{chr(ord(rank)+1)}{int(file)+1}")

        elif colour == "black":
            list_of_squares.append(f"{chr(ord(rank)-1)}{int(file)-1}")
            list_of_squares.append(f"{chr(ord(rank)+1)}{int(file)-1}")

        return list_of_squares
    
    def is_en_passant(self, square, current_fen, prev_fen, colour):
        pass

    def is_home_square(self, square, colour):
        pass

class Knight:
    def __init__(self, colour):
        self.type = "knight"
        self.colour = colour
       

    def visible_squares(self, square):
        list_of_squares = []
        rank = list(square)[0]
        file = list(square)[1]
        rank_num = ord(rank)-64
        file_num = int(file)
        
        possible_squares = [f"{chr(rank_num+62)}{file_num-1}", f"{chr(rank_num+62)}{file_num+1}", f"{chr(rank_num+63)}{file_num-2}",
         f"{chr(rank_num+63)}{file_num+2}", f"{chr(rank_num+65)}{file_num-2}", f"{chr(rank_num+65)}{file_num+2}",
         f"{chr(rank_num+66)}{file_num+1}",f"{chr(rank_num+66)}{file_num-1}",]

        for square in possible_squares:
            if square in all_squares:
                list_of_squares.append(square)

        return list_of_squares

    def can_attack(self, square):
        pass
        # essentially the same as visible except our own pieces

class Rook:
    def __init__(self, colour):
        
        self.type = "rook"
        self.colour = colour
        

    def visible_squares(self, square):
        list_of_squares = []
        rank = list(square)[0]
        file = list(square)[1]
        
        #append all on the same rank
        for i in range(8):
            list_of_squares.append(f"{rank}{i+1}")
        list_of_squares.remove(square)
        
        #append all on the same file
        for j in ["A", "B", "C", "D", "E", "F", "G", "H"]:
            list_of_squares.append(f"{j}{file}")
        list_of_squares.remove(square)

        return list_of_squares
    
class Bishop:
    def __init__(self, colour):
        
        self.type = "bishop"
        self.colour = colour
        

    def visible_squares(self, square):
        list_of_squares = []
        rank = list(square)[0]
        file = list(square)[1]
        
        diagonals_visible = diagonals[square]
        for square in diagonals_visible:
            list_of_squares.append(square)
        
        return list_of_squares

class King:
    def __init__(self, colour):
        
        self.type = "king"
        self.colour = colour
        

    def visible_squares(self, square):
        list_of_squares = []
        rank = list(square)[0]
        file = list(square)[1]

        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                list_of_squares.append(f"{chr(ord(rank)+i)}{int(file)+j}")
        list_of_squares.remove(square)
        
        return list_of_squares

class Board:
    def __init__(self, turn="white", last_move=None, fen="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"):
        self.turn = turn
        self.opponent_controlled_squares = {}
        self.position = {}
        self.fen = fen
        self.white_moves = 0
        self.black_moves = 0
        self.prev_move = None
        self.en_passant_moves = []
        self.last_move = last_move

    def set_board(self):
        self.positions = pieces_positions(self.fen)
        piece_mapping = {
            "b pawn": lambda: Pawn("black"),
            "w pawn": lambda: Pawn("white"),
            "b rook": lambda: Rook("black"),
            "w rook": lambda: Rook("white"),
            "b knight": lambda: Knight("black"),
            "w knight": lambda: Knight("white"),
            "b king": lambda: King("black"),
            "w king": lambda: King("white"),
            "b queen": lambda: Queen("black"),
            "w queen": lambda: Queen("white"),
            "b bishop": lambda: Bishop("black"),
            "w bishop": lambda: Bishop("white"),
            }
        object_pieces = {}
        for square, piece in self.positions.items():
            if piece in piece_mapping:
                object_pieces[square] = piece_mapping[piece]()
            
        self.position = object_pieces
    
    def check_en_passant(self):
        valid_en_passant = []   # a list of squares that the attacking pawn will be on i.e. the behind the pawn being captured

        # previous move must be a pawn moving two squares from its starting square
        valid_white_prev_moves = ["a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4"]
        valid_black_prev_moves = ["a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5"]

        if self.prev_move in valid_black_prev_moves:
            victim_rank, victim_file = list(self.prev_move).upper()
            attacking_squares = [f"{chr(ord(victim_rank-1))}{victim_file}" if ord(victim_rank-65) > 0 else None, f"{chr(ord(victim_rank+1))}{victim_file}" if ord(victim_rank-72) > 0 else None]
            for square in attacking_squares:
                if self.position[square] == "w pawn":
                    valid_en_passant.append(f"{victim_rank}{int(victim_file)+1}")


        if self.prev_move in valid_white_prev_moves:
            victim_rank, victim_file = list(self.prev_move).upper()
            attacking_squares = [f"{chr(ord(victim_rank-1))}{victim_file}" if ord(victim_rank-65) > 0 else None, f"{chr(ord(victim_rank+1))}{victim_file}" if ord(victim_rank-72) > 0 else None]
            for square in attacking_squares:
                if self.position[square] == "b pawn":
                    valid_en_passant.append(f"{victim_rank}{int(victim_file)-1}")

        for move in valid_en_passant:
            self.en_passant_moves.append(move)

    def get_legal_moves(self):
        legal_moves_dict = {}
        for square, piece in self.position.items():
            origin_square_rank = list(square)[0]
            origin_square_file = list(square)[1]
            visible_squares = piece.visible_squares(square)
            all_squares_visible = True
            
            legal_moves = []
            conflict_squares = []
            
            # checking all the squares it could move to to see if it reaches an occupied square
            for visible_square in visible_squares:
                if visible_square in self.position.keys():
                    #if this is triggered, we save the square
                    conflict_squares.append(visible_square)
                    all_squares_visible = False
                                    
                else:
                    # add every square that isnt occupied, we will exclude blocked squares after
                    legal_moves.append(visible_square)
                    continue
                    
            #if all squares are checked and none are occupied, the entire visible squares list is a legal move
            if all_squares_visible:
                legal_moves_dict[piece] = visible_squares
                continue
                
            # we must now check each conflict square and remove squares behind it
            for conflict_square in conflict_squares:

                # check if we can capture conflict square (different colour)
                if piece.colour != self.position[conflict_square].colour:
                    legal_moves.append(conflict_square)

                conflict_rank = list(conflict_square)[0]
                conflict_file = list(conflict_square)[1]

                #convert our original square to unicode where A = 1, H = 8
                origin_rank_num = ord(origin_square_rank)-64
                origin_file_num = int(origin_square_file)
                                    
                #convert conflict square to unicode where A = 1, H = 8
                conflict_rank_num = ord(conflict_rank)-64
                conflict_file_num = int(conflict_file)

                #convert to coordinates e.g. (2,5), (3,4)
                conflict_square_coords = (conflict_rank_num, conflict_file_num)
                square_coords = (origin_rank_num, origin_file_num)

                # this means its on a diagonal
                if abs(conflict_file_num - origin_file_num) == abs(conflict_rank_num - origin_rank_num):
                                      
                    illegal_squares = coordinates_on_same_diagonal(square_coords, conflict_square_coords)
                                           
                # this means they are on the same rank
                elif origin_rank_num == conflict_rank_num:
                    print("same rank detected")
                    illegal_squares = coordinates_on_same_rank(square_coords, conflict_square_coords)

                # this means they are on the same file
                elif origin_file_num == conflict_file_num:

                    illegal_squares = coordinates_on_same_file(square_coords, conflict_square_coords)

                else:
                    continue

                # take these illegal move squares away from our list of moves for this piece
                for illegal_square in illegal_squares:
                    
                    if illegal_square in legal_moves:
                        legal_moves.remove(illegal_square)

            legal_moves_dict[piece] = legal_moves
        return legal_moves_dict

class Bot:
    def __init__(self, colour):
        self.colour = colour
        self.turn = None

    def play(self):

        board = Board()

        if self.colour.ignorecase() == "white":
            self.turn = True
        else:
            self.turn = False
        
        if not self.turn:
            opponent_move = input("Move: ")

        

        

    



board = Board("8/5p2/3r2p1/4n3/8/3R4/5K2/8 w - - 0 1", "black")
board.set_board()
print()
print()
print()
#print(board.position)
print()
print()
print()
print(board.get_legal_moves())