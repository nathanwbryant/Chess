from chessboard import Board, LegalMoveGenerator, Pawn, Bishop, Knight, Queen, King, Rook
from fen_utils import board_map, map_to_fen, get_promotion, update_castle_rank, update_fen
from algebraic_utils import parse_notation, is_valid_notation, construct_algebraic_notation
import copy
import random as r

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

class Bot:
    def __init__(self, fen="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"):
        self.game_ongoing = False
        self.colour = None
        self.user_colour = None
        self.turn = None
        self.board = Board(fen=fen)

    def verify_move_og(self, move, board, user_colour):
        
        verification = {
            "verify_type": None,
            "verify_from_square": None,
            "verify_to_square": None,
            }
        
        parsed_move = parse_notation(move)
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



    def create_algebraic_notation(self, move):
        print("creating algebraic move from move=", move)

        validators = {
            "checkmate": None,
            "check": None,
            "kingsideCastle": None,
            "queensideCastle": None,
            "sharedRank": False,
            "sharedFile": False,
            "capture": None,
            "promotion": None,
            "en_passant": None
        }

        piece_moved = move[0]
        to_square = move[1]
        piece_from_sqr = piece_moved.occupied_square

        # Determine if the move is a capture
        validators["capture"] = self.board.position.get(to_square) is not None

        # Check for en passant capture
        if piece_moved.type == "pawn" and to_square[0] != piece_from_sqr[0]:
            validators["capture"] = True

        # Create a temporary board to simulate the move
        temp_board = copy.deepcopy(self.board)

        # re-initialise piece attributes
        temp_piece_moved = copy.deepcopy(piece_moved)
        temp_piece_moved.occupied_square = to_square
        temp_piece_moved.visible_squares = temp_piece_moved.get_visible_squares()

        # Update the temporary board with the move
        temp_board.position[piece_moved.occupied_square] = None  # Remove piece from original square
        temp_board.position[temp_piece_moved.occupied_square] = temp_piece_moved  # Place piece in new square
        print(temp_board.position)

        # Update the active colour in temp_board to the opponent's colour
        temp_board.active_colour = "white" if self.board.active_colour == "black" else "black"

        # Re-initialise the move generator with the updated position and active colour
        temp_board.move_generator = LegalMoveGenerator(
            position=temp_board.position,
            active_colour=temp_board.active_colour,
            en_passant_target=None,
            castling_rights=temp_board.castling_rights,
            opp_king=temp_board.white_king if temp_board.active_colour == "black" else temp_board.black_king
        )


        # Generate legal moves for temp_board
        
        temp_board.move_generator.generate_legal_moves()

        temp_board.white_legal_moves = temp_board.move_generator.white_legal_moves
        temp_board.black_legal_moves = temp_board.move_generator.black_legal_moves
        temp_board.in_check = temp_board.move_generator.get_check_status()
        temp_board.is_checkmate = temp_board.move_generator.get_checkmate_status()

        # Now we can access temp_board.in_check and temp_board.is_checkmate
        validators["checkmate"] = temp_board.is_checkmate
        validators["check"] = temp_board.in_check

        # -------------------- Castling Validation --------------------
        # Kingside castling
        if piece_from_sqr in ["E1", "E8"] and piece_moved.type == "king" and to_square in ["G1", "G8"]:
            if validators['checkmate']:
                return "O-O#"
            elif validators['check']:
                return "O-O+"
            else:
                return "O-O"

        # Queenside castling
        elif piece_from_sqr in ["E1", "E8"] and piece_moved.type == "king" and to_square in ["C1", "C8"]:
            if validators['checkmate']:
                return "O-O-O#"
            elif validators['check']:
                return "O-O-O+"
            else:
                return "O-O-O"
        # -------------------------------------------------------

        # -------- Promotion Validation --------
        if piece_moved.type == "pawn" and (to_square[1] == "8" or to_square[1] == "1"):
            validators['promotion'] = "queen"  # For now, automatically promote to queen

        # -------- Shared Rank and/or File Validation --------
        temp_piece_type = temp_piece_moved.type

        # Get all pieces of this colour with the same type that can move to the same to_square
        same_type_pieces = []
        current_legal_moves = self.board.move_generator.get_legal_moves(self.board.active_colour)

        for piece, legal_moves in current_legal_moves.items():
            if piece.type == piece_moved.type and piece != piece_moved:
                if to_square in legal_moves:
                    same_type_pieces.append(piece)

        if same_type_pieces:
            from_file = piece_from_sqr[0]
            from_rank = piece_from_sqr[1]

            for piece in same_type_pieces:
                piece_file = piece.occupied_square[0]
                piece_rank = piece.occupied_square[1]

                if piece_file == from_file:
                    validators["sharedFile"] = True

                if piece_rank == from_rank:
                    validators["sharedRank"] = True

        # ----------------- Construct the Notation ------------------
        print(f"constructing algebraic notation: piece_type={piece_moved.type},\n piece_from_sqr={piece_from_sqr},\n to_square={to_square},\n validators={validators},\n same_type_pieces={same_type_pieces}, active_colour={self.board.active_colour}")
        algebraic = construct_algebraic_notation(
            piece_type=piece_moved.type,
            piece_from_sqr=piece_from_sqr,
            to_square=to_square,
            validators=validators,
            same_type_pieces=same_type_pieces,
            active_colour=self.board.active_colour
        )

        print("ALGEBRAIC CONVERSION: ", algebraic)
        return algebraic

    def verify_castle(self, parsed_move, user_colour):

        if user_colour == "white":
            print("user colour = white ...")
            king = self.board.position['E1']
            if not isinstance(king, King):
                print("not a king instance")
                return False
            
            legal_moves = self.board.white_legal_moves[king]
            print("legal moves = ", legal_moves)

            if parsed_move["kingsideCastle"]:
                
                if 'G1' not in legal_moves:
                    print("G1 not legal move")
                    return False
                parsed_move["from"] = "E1"
                parsed_move["to"] = "G1"
                return parsed_move
            
            elif parsed_move["queensideCastle"]:
                print("Queenside castle found in parsed move")
                if 'C1' not in legal_moves:
                    print("C1 not legal move")
                    return False
                parsed_move["from"] = "E1"
                parsed_move["to"] = "C1"
                print("parsed move amended: ", parsed_move)
                return parsed_move

             
        elif user_colour == "black":
            print("user colour = black ...")
            king = self.board.position['E8']
            if not isinstance(king, King):
                print("not a king instance")
                return False
            
            legal_moves = self.board.black_legal_moves[king]
            
            if parsed_move["kingsideCastle"]:
                if 'G8' not in legal_moves:
                    return False
                parsed_move["from"] = "E8"
                parsed_move["to"] = "G8"
                return parsed_move
            
            else:
                if 'C8' not in legal_moves:
                    return False
                parsed_move["from"] = "E8"
                parsed_move["to"] = "C8"
                return parsed_move
        
        return parsed_move
                

    def verify_move(self, move, user_colour):
        parsed_move = self.parse_and_adjust_move(move)
        print("parsed move: ", parsed_move)
        if "O-O" or "0-0" in move:
            return self.verify_castle(parsed_move, user_colour)

        if not parsed_move:
            return False

        from_sqr = parsed_move["from"]

        if not (isinstance(from_sqr, str) and len(from_sqr) == 2):
            moved_piece = self.find_moving_piece(parsed_move, from_sqr, self.board, user_colour)

        else: 
            moved_piece = self.board.position[from_sqr]

        if not moved_piece:
            return False

        if not self.is_valid_move(moved_piece, parsed_move, self.board):
            return False

        return parsed_move

    def parse_and_adjust_move(self, move):
        parsed_move = parse_notation(move)
        print("parsing move: ", move, " -> ", parsed_move)

        if "O-O" in move:   # kingside or queenside castling
            return parsed_move
            
        parsed_move["piece"] = parsed_move["piece"].lower().strip()
        parsed_move["to"] = parsed_move["to"].upper().strip()

        from_sqr = parsed_move["from"]

        if isinstance(from_sqr, str):
            parsed_move["from"] = from_sqr.upper()

        return parsed_move

    def find_moving_piece(self, parsed_move, from_square, board, user_colour):
        user_legal_moves = getattr(board, f"{user_colour}_legal_moves")
        print("user legal moves: ", user_legal_moves)

        potential_moved_pieces = [
            piece for piece in user_legal_moves
            if piece.type == parsed_move["piece"] and parsed_move["to"] in user_legal_moves[piece]
        ]
        print("potential moved pieces: ", potential_moved_pieces)

        if len(potential_moved_pieces) == 0:
            return None

        if len(potential_moved_pieces) == 1:
            parsed_move["from"] = potential_moved_pieces[0].occupied_square
            return potential_moved_pieces[0]

        return self.determine_exact_piece(parsed_move, potential_moved_pieces)

    def determine_exact_piece(self, parsed_move, potential_pieces):
        parsed_move_from = parsed_move["from"]

        if parsed_move_from.isalpha():
            from_file = parsed_move_from.upper()
            for piece in potential_pieces:
                piece_file = piece.occupied_square[0]
                if piece_file == from_file:
                    parsed_move["from"] = piece.occupied_square
                    return piece

        elif parsed_move_from.isdigit():
            from_rank = parsed_move_from
            for piece in potential_pieces:
                piece_rank = piece.occupied_square[1]
                if piece_rank == from_rank:
                    parsed_move["from"] = piece.occupied_square
                    return piece

        return None

    def is_valid_move(self, moved_piece, parsed_move, board):
        user_legal_moves = getattr(board, f"{moved_piece.colour}_legal_moves")
        if parsed_move["to"] not in user_legal_moves[moved_piece]:
            print("parsed_move[to] not in legal moves: ", parsed_move["to"], " not in ", user_legal_moves[moved_piece])
            return False
        return True




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
     