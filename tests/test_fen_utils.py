import pytest
from fen_utils import board_map, map_to_fen, update_fen, update_castle_rank, get_promotion

# ---------------------------------- Test board_map -------------------------------------------------
def test_initial_position():
    """
    Test that the initial chess position generates the correct board mapping.
    """
    ranks = ["rnbqkbnr", "pppppppp", "8", "8", "8", "8", "PPPPPPPP", "RNBQKBNR"]
    expected = {
        8: {'A': 'r', 'B': 'n', 'C': 'b', 'D': 'q', 'E': 'k', 'F': 'b', 'G': 'n', 'H': 'r'},
        7: {'A': 'p', 'B': 'p', 'C': 'p', 'D': 'p', 'E': 'p', 'F': 'p', 'G': 'p', 'H': 'p'},
        6: {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1, 'H': 1},
        5: {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1, 'H': 1},
        4: {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1, 'H': 1},
        3: {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1, 'H': 1},
        2: {'A': 'P', 'B': 'P', 'C': 'P', 'D': 'P', 'E': 'P', 'F': 'P', 'G': 'P', 'H': 'P'},
        1: {'A': 'R', 'B': 'N', 'C': 'B', 'D': 'Q', 'E': 'K', 'F': 'B', 'G': 'N', 'H': 'R'},
    }
    result = board_map(ranks)
    assert result == expected

def test_empty_board():
    """
    Test that an empty board is correctly mapped.
    """
    ranks = ["8"] * 8
    expected = {
        rank: {file: 1 for file in ["A", "B", "C", "D", "E", "F", "G", "H"]}
        for rank in range(8, 0, -1)
    }
    result = board_map(ranks)
    assert result == expected

def test_partial_board():
    """
    Test mapping of a partial board with mixed pieces and empty squares.
    """
    ranks = ["rnbqkbnr", "pppppppp", "8", "3P4", "8", "8", "PPPPPPPP", "RNBQKBNR"]
    expected = {
        8: {'A': 'r', 'B': 'n', 'C': 'b', 'D': 'q', 'E': 'k', 'F': 'b', 'G': 'n', 'H': 'r'},
        7: {'A': 'p', 'B': 'p', 'C': 'p', 'D': 'p', 'E': 'p', 'F': 'p', 'G': 'p', 'H': 'p'},
        6: {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1, 'H': 1},
        5: {'A': 1, 'B': 1, 'C': 1, 'D': 'P', 'E': 1, 'F': 1, 'G': 1, 'H': 1},
        4: {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1, 'H': 1},
        3: {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1, 'H': 1},
        2: {'A': 'P', 'B': 'P', 'C': 'P', 'D': 'P', 'E': 'P', 'F': 'P', 'G': 'P', 'H': 'P'},
        1: {'A': 'R', 'B': 'N', 'C': 'B', 'D': 'Q', 'E': 'K', 'F': 'B', 'G': 'N', 'H': 'R'},
    }
    result = board_map(ranks)
    assert result == expected

def test_invalid_input_too_few_ranks():
    """
    Test that the function raises an error when given too few ranks.
    """
    ranks = ["8"] * 7  # Only 7 ranks
    with pytest.raises(ValueError) as exc_info:
        board_map(ranks)
    assert "Expected 8 ranks" in str(exc_info.value)

def test_invalid_input_too_many_squares_in_rank():
    """
    Test that the function raises an error when a rank has too many squares.
    """
    ranks = ["9"] + ["8"] * 7
    with pytest.raises(ValueError) as exc_info:
        board_map(ranks)
    assert "Too many squares in rank" in str(exc_info.value)

def test_invalid_input_not_enough_squares_in_rank():
    """
    Test that the function raises an error when a rank has too few squares.
    """
    ranks = ["7"] + ["8"] * 7
    with pytest.raises(ValueError) as exc_info:
        board_map(ranks)
    assert "Not enough squares in rank" in str(exc_info.value)

def test_invalid_character_in_rank():
    """
    Test that the function raises an error when a rank contains invalid characters.
    """
    ranks = ["rnbqkbnr", "pppppppp", "8", "4X3", "8", "8", "PPPPPPPP", "RNBQKBNR"]
    with pytest.raises(ValueError) as exc_info:
        board_map(ranks)
    assert "Invalid piece: 'X'." == str(exc_info.value)

# ----------------------------- Test map_to_fen ------------------------------------------------------

def test_map_to_fen_initial_position():
    """
    Test that the initial chess position rank map converts back to the correct FEN string.
    """
    rank_map = {
        8: {'A': 'r', 'B': 'n', 'C': 'b', 'D': 'q', 'E': 'k', 'F': 'b', 'G': 'n', 'H': 'r'},
        7: {'A': 'p', 'B': 'p', 'C': 'p', 'D': 'p', 'E': 'p', 'F': 'p', 'G': 'p', 'H': 'p'},
        6: {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1, 'H': 1},
        5: {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1, 'H': 1},
        4: {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1, 'H': 1},
        3: {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1, 'H': 1},
        2: {'A': 'P', 'B': 'P', 'C': 'P', 'D': 'P', 'E': 'P', 'F': 'P', 'G': 'P', 'H': 'P'},
        1: {'A': 'R', 'B': 'N', 'C': 'B', 'D': 'Q', 'E': 'K', 'F': 'B', 'G': 'N', 'H': 'R'},
    }
    expected_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
    result = map_to_fen(rank_map)
    assert result == expected_fen

def test_map_to_fen_empty_board():
    """
    Test that an empty rank map converts to the correct FEN string.
    """
    rank_map = {
        rank: {file: 1 for file in ["A", "B", "C", "D", "E", "F", "G", "H"]}
        for rank in range(1, 9)
    }
    expected_fen = "8/8/8/8/8/8/8/8"
    result = map_to_fen(rank_map)
    assert result == expected_fen

def test_map_to_fen_partial_board():
    """
    Test that a partial rank map with mixed pieces and empty squares converts correctly.
    """
    rank_map = {
        8: {'A': 'r', 'B': 1, 'C': 'b', 'D': 1, 'E': 'k', 'F': 1, 'G': 'n', 'H': 'r'},
        7: {'A': 'p', 'B': 'p', 'C': 1, 'D': 'p', 'E': 'p', 'F': 'p', 'G': 1, 'H': 'p'},
        6: {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 'b', 'F': 1, 'G': 1, 'H': 1},
        5: {'A': 1, 'B': 1, 'C': 1, 'D': 'Q', 'E': 1, 'F': 1, 'G': 1, 'H': 1},
        4: {'A': 1, 'B': 1, 'C': 'P', 'D': 1, 'E': 1, 'F': 1, 'G': 1, 'H': 1},
        3: {'A': 1, 'B': 'N', 'C': 1, 'D': 1, 'E': 1, 'F': 'B', 'G': 1, 'H': 1},
        2: {'A': 'P', 'B': 'P', 'C': 1, 'D': 'P', 'E': 'P', 'F': 'P', 'G': 1, 'H': 'P'},
        1: {'A': 'R', 'B': 1, 'C': 'B', 'D': 1, 'E': 'K', 'F': 1, 'G': 'N', 'H': 'R'},
    }
    expected_fen = "r1b1k1nr/pp1ppp1p/4b3/3Q4/2P5/1N3B2/PP1PPP1P/R1B1K1NR"
    result = map_to_fen(rank_map)
    assert result == expected_fen

def test_map_to_fen_incomplete_rank_map():
    """
    Test that the function raises an error when the rank map is incomplete.
    """
    rank_map = {
        8: {'A': 'r', 'B': 'n', 'C': 'b', 'D': 'q'},  # Missing files E-H
        # Missing ranks 7-1
    }
    with pytest.raises(ValueError) as exc_info:
        map_to_fen(rank_map)
    assert "Incomplete files:" in str(exc_info.value)  # KeyError for missing files in rank

def test_map_to_fen_invalid_square_value():
    """
    Test that the function raises an error when a square has an invalid value.
    """
    rank_map = {
        8: {'A': 'r', 'B': 'n', 'C': 'b', 'D': 'q', 'E': 'k', 'F': 'b', 'G': 'n', 'H': 'r'},
        # All other ranks filled with valid data...
    }
    # Introduce an invalid value
    rank_map[7] = {'A': 'p', 'B': 'p', 'C': 'invalid', 'D': 'p', 'E': 'p', 'F': 'p', 'G': 'p', 'H': 'p'}
    for rank in range(6, 0, -1):
        rank_map[rank] = {file: 1 for file in ["A", "B", "C", "D", "E", "F", "G", "H"]}
    with pytest.raises(ValueError) as exc_info:
        map_to_fen(rank_map)
    assert "Invalid piece: 'invalid'." == str(exc_info.value)

def test_map_to_fen_missing_file():
    """
    Test that the function raises an error when a file is missing in a rank.
    """
    rank_map = {
        rank: {file: 1 for file in ["A", "B", "C", "D", "F", "G", "H"]}  # Missing 'E' file
        for rank in range(1, 9)
    }
    with pytest.raises(ValueError) as exc_info:
        map_to_fen(rank_map)
    assert f"Incomplete files: {list(rank_map[1].keys())} must be ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']" == str(exc_info.value)

def test_map_to_fen_additional_file():
    """
    Test that the function ignores extra files in a rank.
    """
    rank_map = {
        rank: {**{file: 1 for file in ["A", "B", "C", "D", "E", "F", "G", "H"]}, 'I': 1}  # Extra file 'I'
        for rank in range(1, 9)
    }
    expected_fen = "8/8/8/8/8/8/8/8"

    with pytest.raises(ValueError) as exc_info:
        map_to_fen(rank_map)
    assert f"Incomplete files: {list(rank_map[1].keys())} must be ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']" == str(exc_info.value)


def test_map_to_fen_invalid_rank_number():
    """
    Test that the function raises an error when the rank numbers are invalid.
    """
    rank_map = {
        9: {file: 1 for file in ["A", "B", "C", "D", "E", "F", "G", "H"]},  # Invalid rank number
        **{
            rank: {file: 1 for file in ["A", "B", "C", "D", "E", "F", "G", "H"]}
            for rank in range(1, 8)
        }
    }
    with pytest.raises(KeyError) as exc_info:
        map_to_fen(rank_map)
    assert "8" in str(exc_info.value)

# ----------------------------------- Test get_promotion -------------------------------------------

def test_get_promotion_white_pawn_to_queen():
    assert get_promotion("queen", "P") == "Q"

def test_get_promotion_white_pawn_to_rook():
    assert get_promotion("rook", "P") == "R"

def test_get_promotion_white_pawn_to_bishop():
    assert get_promotion("bishop", "P") == "B"

def test_get_promotion_white_pawn_to_knight():
    assert get_promotion("knight", "P") == "N"

def test_get_promotion_black_pawn_to_queen():
    assert get_promotion("queen", "p") == "q"

def test_get_promotion_black_pawn_to_rook():
    assert get_promotion("rook", "p") == "r"

def test_get_promotion_black_pawn_to_bishop():
    assert get_promotion("bishop", "p") == "b"

def test_get_promotion_black_pawn_to_knight():
    assert get_promotion("knight", "p") == "n"

def test_get_promotion_invalid_promotion_to():
    # Should return the original pawn character
    assert get_promotion("unicorn", "P") == "Q"
    assert get_promotion("dragon", "p") == "q"

def test_get_promotion_invalid_pawn_character():
    # Even with an invalid pawn character, the function should return the mapped promotion piece
    with pytest.raises(ValueError):
        get_promotion("queen", "X")
    with pytest.raises(ValueError):
        get_promotion("queen", "x")
        
def test_get_promotion_empty_strings():
    # Test with empty strings
    assert get_promotion("", "P") == "Q"
    with pytest.raises(ValueError):
        get_promotion("queen", "")    

def test_get_promotion_non_alphabetical_pawn():
    # Non-alphabetical pawn characters
    with pytest.raises(ValueError):
        get_promotion("queen", "1")
    with pytest.raises(ValueError):
        get_promotion("queen", "!")

def test_get_promotion_case_insensitivity():
    # Test different cases for promotion_to
    assert get_promotion("Queen", "P") == "Q"
    assert get_promotion("QUEEN", "P") == "Q"
    assert get_promotion("QuEeN", "P") == "Q"

def test_get_promotion_pawn_case_sensitivity():
    # Test with pawn characters of different cases
    assert get_promotion("queen", "p") == "q"
    assert get_promotion("queen", "P") == "Q"

def test_get_promotion_none_inputs():
    # Test with None inputs
    with pytest.raises(AttributeError):
        get_promotion(None, "P")
    with pytest.raises(AttributeError):
        get_promotion("queen", None)



# ----------------------------------- Test update_castle_rank ---------------------------------

def test_update_castle_rank_white_kingside():
    """
    Test white kingside castling rank update.
    """
    move_tuple = ("king", "E1", "G1")
    rank = {"A": "R", "B": "N", "C": "B", "D": "Q", "E": "K", "F": 1, "G": 1, "H": "R"}
    expected_rank = {"A": "R", "B": "N", "C": "B", "D": "Q", "E": 1, "F": "R", "G": "K", "H": 1}
    result = update_castle_rank(move_tuple, rank.copy())
    assert result == expected_rank

def test_update_castle_rank_white_queenside():
    """
    Test white queenside castling rank update.
    """
    move_tuple = ("king", "E1", "C1")
    rank = {"A": "R", "B": "N", "C": "B", "D": "Q", "E": "K", "F": 1, "G": 1, "H": "R"}
    expected_rank = {"A": 1, "B": "N", "C": "K", "D": "R", "E": 1, "F": 1, "G": 1, "H": "R"}
    result = update_castle_rank(move_tuple, rank.copy())
    assert result == expected_rank

def test_update_castle_rank_black_kingside():
    """
    Test black kingside castling rank update.
    """
    move_tuple = ("king", "E8", "G8")
    rank = {"A": "r", "B": "n", "C": "b", "D": "q", "E": "k", "F": 1, "G": 1, "H": "r"}
    expected_rank = {"A": "r", "B": "n", "C": "b", "D": "q", "E": 1, "F": "r", "G": "k", "H": 1}
    result = update_castle_rank(move_tuple, rank.copy())
    assert result == expected_rank

def test_update_castle_rank_black_queenside():
    """
    Test black queenside castling rank update.
    """
    move_tuple = ("king", "E8", "C8")
    rank = {"A": "r", "B": "n", "C": "b", "D": "q", "E": "k", "F": 1, "G": 1, "H": "r"}
    expected_rank = {"A": 1, "B": "n", "C": "k", "D": "r", "E": 1, "F": 1, "G": 1, "H": "r"}
    result = update_castle_rank(move_tuple, rank.copy())
    assert result == expected_rank


def test_update_castle_rank_non_castling():
    """
    Test that non-castling moves do not alter the rank.
    """
    move_tuple = ("king", "E1", "E2")
    rank = {"A": "R", "B": "N", "C": "B", "D": "Q", "E": "K", "F": 1, "G": 1, "H": "R"}
    expected_rank = rank.copy()  # No change expected
    result = update_castle_rank(move_tuple, rank.copy())
    assert result == expected_rank


# ---------------------------------- Test update_fen --------------------------------------------

# test_fen_utils.py

import pytest
from fen_utils import update_fen, board_map, map_to_fen

def test_pawn_move():
    """
    Test a simple pawn move.
    """
    prev_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    move = {
        "piece": "pawn",
        "from": "E2",
        "to": "E4",
        "capture": False,
        "promotion": None,
        "enPassant": False
    }
    expected_fen = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1"
    result = update_fen(prev_fen, move)
    assert result == expected_fen

def test_capture():
    """
    Test a capture move.
    """
    prev_fen = "rnbqkb1r/pppppppp/5n2/4P3/8/8/PPPP1PPP/RNBQKBNR w KQkq - 1 2"
    move = {
        "piece": "pawn",
        "from": "E5",
        "to": "F6",
        "capture": True,
        "promotion": None,
        "enPassant": False
    }
    expected_fen = "rnbqkb1r/pppppppp/5P2/8/8/8/PPPP1PPP/RNBQKBNR b KQkq - 0 2"
    result = update_fen(prev_fen, move)
    assert result == expected_fen

def test_pawn_promotion():
    """
    Test a pawn promotion.
    """
    prev_fen = "rnbqkbnr/ppPpp1pp/5p2/8/8/8/PP1PPPPP/RNBQKBNR w KQkq - 0 2"
    move = {
        "piece": "pawn",
        "from": "C7",
        "to": "D8",
        "capture": True,
        "promotion": "queen",
        "enPassant": False
    }
    expected_fen = "rnbQkbnr/pp1pp1pp/5p2/8/8/8/PP1PPPPP/RNBQKBNR b KQkq - 0 2"
    result = update_fen(prev_fen, move)
    assert result == expected_fen

def test_castling_kingside_white():
    """
    Test white kingside castling.
    """
    prev_fen = "rnbqkbnr/p1pp2pp/1p3p2/4p3/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 0 4"
    move = {
        "piece": "king",
        "from": "E1",
        "to": "G1",
        "capture": False,
        "promotion": None,
        "enPassant": False
    }
    expected_fen = "rnbqkbnr/p1pp2pp/1p3p2/4p3/2B1P3/5N2/PPPP1PPP/RNBQ1RK1 b kq - 1 4"
    result = update_fen(prev_fen, move)
    assert result == expected_fen

def test_castling_queenside_black():
    """
    Test black queenside castling.
    """
    prev_fen = "r3kbnr/pppn1ppp/8/3Pp3/6bq/1PNP4/P1P1NPPP/R1BQKB1R b KQkq - 0 6"
    move = {
        "piece": "king",
        "from": "E8",
        "to": "C8",
        "capture": False,
        "promotion": None,
        "enPassant": False
    }
    expected_fen = "2kr1bnr/pppn1ppp/8/3Pp3/6bq/1PNP4/P1P1NPPP/R1BQKB1R w KQ - 1 7"
    result = update_fen(prev_fen, move)
    assert result == expected_fen

def test_en_passant():
    """
    Test en passant move.
    """
    prev_fen = "rnbqkbnr/ppp2ppp/4p3/3pP3/8/8/PPPP1PPP/RNBQKBNR w KQkq d6 0 3"
    move = {
        "piece": "pawn",
        "from": "E5",
        "to": "D6",
        "capture": True,
        "enPassant": True
    }
    expected_fen = "rnbqkbnr/ppp2ppp/3Pp3/8/8/8/PPPP1PPP/RNBQKBNR b KQkq - 0 3"
    result = update_fen(prev_fen, move)
    assert result == expected_fen

def test_halfmove_and_fullmove():
    """
    Test that halfmove clock and fullmove number are updated correctly.
    """
    prev_fen = "rnbqkbnr/pppppppp/8/8/8/4P3/PPPP1PPP/RNBQKBNR b KQkq - 0 1"
    move = {
        "piece": "pawn",
        "from": "D7",
        "to": "D6",
        "capture": False,
        "promotion": None,
        "enPassant": False
    }
    expected_fen = "rnbqkbnr/ppp1pppp/3p4/8/8/4P3/PPPP1PPP/RNBQKBNR w KQkq - 0 2"
    result = update_fen(prev_fen, move)
    assert result == expected_fen

def test_update_castling_rights():
    """
    Test that castling rights are updated when the rook moves.
    """
    prev_fen = "rnbqkbnr/1ppppppp/8/p7/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2"
    move = {
        "piece": "rook",
        "from": "A8",
        "to": "A6",
        "capture": False,
        "promotion": None,
        "enPassant": False
    }
    expected_fen = "1nbqkbnr/1ppppppp/r7/p7/4P3/5N2/PPPP1PPP/RNBQKB1R w KQk - 2 3"
    result = update_fen(prev_fen, move)
    assert result == expected_fen



