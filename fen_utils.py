# fen_utils.py
from typing import List, Dict, Union, Any, Tuple, Optional
import re

valid_pieces = ["K", "k", "Q", "q", "R", "r", "B", "b", "N", "n", "P", "p"]

def board_map(ranks: List[str]) -> Dict[int, Dict[str, Union[str, int]]]:
    """ 
    Converts a list of ranks in FEN order to a board mapping.

    Args:
        ranks (List[str]): A list of rank strings in FEN order (from rank 8 to rank 1). Each string represents a rank in FEN notation.

    Returns:
        Dict[int, Dict[str, Union[str, int]]]: A mapping of ranks to dictionaries that map files to pieces or 1 (for empty squares).
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
                    if file_idx >= 8:
                        raise ValueError(f"Invalid FEN rank: '{rank}'. Too many squares in rank.")
                    row_dict[files[file_idx]] = 1
                    file_idx += 1  # Move to the next file
            else:
                if file_idx >= 8:
                    raise ValueError(f"Invalid FEN rank: '{rank}'. Too many squares in rank.")
                
                # Check for valid piece
                if char not in valid_pieces:
                    raise ValueError(f"Invalid piece: '{char}'.")
                
                # Assign the piece to the current file
                row_dict[files[file_idx]] = char
                file_idx += 1  # Move to the next file

        if file_idx != 8:
            raise ValueError(f"Invalid FEN rank: '{rank}'. Not enough squares in rank.")
        
        # Assign the row dictionary to the rank (8 - i)
        rank_map[8 - i] = row_dict

    if len(rank_map) != 8:
        raise ValueError(f"Invalid FEN input. Expected 8 ranks, got {len(rank_map)}.")

    return rank_map


def map_to_fen(rank_map: Dict[int, Dict[str, Union[str, int]]]) -> str:
    """
    Converts a rank map back into a FEN string.

    Args:
        rank_map (Dict[int, Dict[str, Union[str, int]]]): A mapping of ranks to dictionaries that map files to pieces or 1 (for empty squares).

    Returns:
        str: The FEN string representation of the board.
    """
    fen_rows = []

    rank_count = len(rank_map.keys())

    for rank in range(8, 8-rank_count, -1):  # Iterate from rank 8 down to 1
        
        if set(rank_map[rank].keys()) != {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'}:
            raise ValueError(f"Incomplete files: {list(rank_map[rank].keys())} must be ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']")
        row = rank_map[rank]
        fen_row = ""
        empty_count = 0

        for file in ["A", "B", "C", "D", "E", "F", "G", "H"]:
            square_value = row.get(file)
            if square_value == 1:  # Detect empty squares
                empty_count += 1

            elif square_value not in valid_pieces:
                raise ValueError(f"Invalid piece: '{square_value}'.")
            else:
                if empty_count > 0:
                    fen_row += str(empty_count)  # Add empty square count
                    empty_count = 0
                fen_row += square_value  # Add the piece (letter)

        # If the row ends with empty squares, add the count
        if empty_count > 0:
            fen_row += str(empty_count)

        fen_rows.append(fen_row)

    # Join the rows with '/' to create the full FEN string
    fen_string = "/".join(fen_rows)
    return fen_string


def get_promotion(promotion_to: str, pawn: str) -> str:
    """
    Returns the piece character for pawn promotion.
    If promotion_to is not recognized, defaults to a queen.
    """
    piece_map = {
        "queen": "Q" if pawn.isupper() else "q",
        "rook": "R" if pawn.isupper() else "r",
        "bishop": "B" if pawn.isupper() else "b",
        "knight": "N" if pawn.isupper() else "n",
    }
    if pawn not in ["P", "p"]:
        raise ValueError(f"Invalid promotion. Expected 'p' or 'P' as valid pawn, not {pawn}")
    
    return piece_map.get(promotion_to.lower(), piece_map["queen"])

def update_castle_rank(move_tuple: Tuple[str, str, str], rank: Dict[str, str]) -> Dict[str, str]:
    """
    Updates the rank for a castling move.

    Args:
        move_tuple (Tuple[str, str, str]): A tuple containing (piece_type, from_square, to_square).
        rank (Dict[str, str]): A mapping of file letters to piece symbols for the rank.

    Returns:
        Dict[str, str]: The updated rank after the castling move.
    """
    piece_type, from_square, to_square = move_tuple
    from_file = from_square[0].upper()
    from_rank_number = int(from_square[1])
    to_file = to_square[0].upper()
    to_rank_number = int(to_square[1])

    # Check if it's a castling move
    if piece_type.lower() == "king" and abs(ord(from_file) - ord(to_file)) > 1:
        # Determine the side of castling
        if to_file == 'G':
            # Kingside castling
            if from_rank_number == 1:
                # White kingside castling
                rank['E'] =  1   # E1 now empty
                rank['F'] = 'R'  # Rook moves to F1
                rank['G'] = 'K'  # King moves to G1
                rank['H'] =  1   # H1 now empty
            elif from_rank_number == 8:
                # Black kingside castling
                rank['E'] =  1   # E8 now empty
                rank['F'] = 'r'  # Rook moves to F8
                rank['G'] = 'k'  # King moves to G8
                rank['H'] =  1   # H8 now empty
        elif to_file == 'C':
            # Queenside castling
            if from_rank_number == 1:
                # White queenside castling
                rank['E'] =  1   # E1 now empty
                rank['D'] = 'R'  # Rook moves to D1
                rank['C'] = 'K'  # King moves to C1
                rank['A'] =  1   # A1 now empty
            elif from_rank_number == 8:
                # Black queenside castling
                rank['E'] =  1   # E8 now empty
                rank['D'] = 'r'  # Rook moves to D8
                rank['C'] = 'k'  # King moves to C8
                rank['A'] =  1   # A8 now empty
    else:
        # Not a castling move; no changes to the rank
        pass

    return rank





def update_fen(prev_fen: str, move: Dict[str, Any]) -> str:
    """
    Updates a FEN string based on a move and the previous FEN.

    Args:
        prev_fen (str): The previous FEN string.
        move (Dict[str, Any]): A dictionary representing the move.

    Returns:
        str: The updated FEN string.
    """
    new_fen_components = {
        "piece_placement": None,
        "active_colour": None,
        "castling_rights": None,
        "en_passant": "-",
        "halfmove_clock": None,
        "move_number": None
    }

    move_tuple = (move["piece"].lower(), move["from"], move["to"])

    # Split the FEN into its components
    fen_parts = prev_fen.split(' ')
    piece_placement = fen_parts[0]  # Board layout
    active_color = fen_parts[1]     # 'w' or 'b'
    castling_rights = fen_parts[2]  # Castling rights
    en_passant = fen_parts[3]       # En passant target square
    halfmove_clock = fen_parts[4]   # Halfmove clock
    move_number = fen_parts[5]      # Full move number

    # Toggle active colour
    new_fen_components["active_colour"] = "w" if active_color == "b" else "b"

    # Increment move number if black just moved
    if active_color == "b":
        new_fen_components["move_number"] = str(int(move_number) + 1)
    else:
        new_fen_components["move_number"] = move_number

    # Board layout
    rows = piece_placement.split('/')  # Rows from rank 8 to rank 1

    # Map the rows to their corresponding rank
    rank_map = board_map(rows)  # {8: {"A": "r", "B": "n", ...}, ... }

    # Extract from and to positions
    from_file, from_rank = move_tuple[1][0].upper(), int(move_tuple[1][1])
    to_file, to_rank = move_tuple[2][0].upper(), int(move_tuple[2][1])

    # character of the piece at the from square
    piece_char = rank_map[from_rank][from_file]

    # Check for promotion
    if "promotion" in move and move["promotion"]:
        piece_char = get_promotion(move["promotion"], piece_char)

    # Update rank maps for from and to squares
    rank_map[from_rank][from_file] = 1  # Empty the from square
    rank_map[to_rank][to_file] = piece_char  # Place the piece at the to square

    # catch skipped square for en passant
    if move["enPassant"]:
        rank_map[from_rank][to_file] = 1

    # Handle castling moves
    castle_moves = [
        ("king", "E1", "G1"), ("king", "E1", "C1"),
        ("king", "E8", "G8"), ("king", "E8", "C8")
    ]
    if move_tuple in castle_moves:
        # Update the rank where castling occurs
        castle_rank = update_castle_rank(move_tuple, rank_map[from_rank])
        # Update the rank map for the castling rank
        rank_map[from_rank] = castle_rank

    # Reconstruct the FEN piece placement string
    rows_str = map_to_fen(rank_map)

    new_fen_components["piece_placement"] = rows_str

    # Update halfmove clock
    if piece_char.lower() == 'p' or move["capture"] == True:
        # Reset halfmove clock if a pawn moved or a capture was made
        new_fen_components["halfmove_clock"] = "0"
    
    else:
        new_fen_components["halfmove_clock"] = str(int(halfmove_clock) + 1)

    # Handle en passant target square
    if piece_char.lower() == 'p' and abs(from_rank - to_rank) == 2:
        # Pawn moved two squares; set en passant target square
        en_passant_rank = (from_rank + to_rank) // 2
        new_fen_components["en_passant"] = f"{from_file.lower()}{en_passant_rank}"
    else:
        new_fen_components["en_passant"] = "-"

    # Update castling rights
    new_castling_rights = castling_rights
    if piece_char.lower() == 'k':
        # King moved; remove castling rights for that side
        if active_color == 'w':
            new_castling_rights = new_castling_rights.replace('K', '').replace('Q', '')
        else:
            new_castling_rights = new_castling_rights.replace('k', '').replace('q', '')
    elif piece_char.lower() == 'r':
        # Rook moved; remove castling rights if necessary
        if active_color == 'w':
            if move['from'] == 'A1':
                new_castling_rights = new_castling_rights.replace('Q', '')
            elif move['from'] == 'H1':
                new_castling_rights = new_castling_rights.replace('K', '')
        else:
            if move['from'] == 'A8':
                new_castling_rights = new_castling_rights.replace('q', '')
            elif move['from'] == 'H8':
                new_castling_rights = new_castling_rights.replace('k', '')

    if new_castling_rights == '':
        new_castling_rights = '-'

    new_fen_components["castling_rights"] = new_castling_rights

    # Now we can recombine the FEN parts and return the full string
    components = [
        new_fen_components["piece_placement"],
        new_fen_components["active_colour"],
        new_fen_components["castling_rights"],
        new_fen_components["en_passant"],
        new_fen_components["halfmove_clock"],
        new_fen_components["move_number"]
    ]
    new_fen = ' '.join(item if item is not None else '-' for item in components)

    return new_fen

