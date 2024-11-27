import pytest
from algebraic_utils import parse_notation, is_valid_notation, construct_algebraic_notation

KING = 'King'
QUEEN = 'Queen'
ROOK = 'Rook'
BISHOP = 'Bishop'
KNIGHT = 'Knight'
PAWN = 'Pawn'

# Test the parsing of different chess notations
def test_parse_knight_move():
    notation = 'Nc3'
    parsed = parse_notation(notation)
    
    assert parsed['piece'] == KNIGHT
    assert parsed['to'] == 'c3'
    assert parsed['from'] is None
    assert parsed['check'] is None
    assert parsed['checkmate'] is None
    assert parsed['capture'] is None

def test_parse_pawn_move():
    notation = 'e4'
    parsed = parse_notation(notation)
    
    assert parsed['piece'] == PAWN
    assert parsed['to'] == 'e4'
    assert parsed['from'] is None
    assert parsed['check'] is None
    assert parsed['checkmate'] is None
    assert parsed['capture'] is None

def test_parse_promotion():
    notation = 'e8=Q'
    parsed = parse_notation(notation)
    
    assert parsed['piece'] == PAWN
    assert parsed['to'] == 'e8'
    assert parsed['promotion'] == QUEEN
    assert parsed['from'] is None

def test_parse_castles_kingside():
    notation = '0-0'
    parsed = parse_notation(notation)
    
    assert parsed['kingsideCastle'] is True
    assert parsed['queensideCastle'] is None
    assert parsed['notation'] == ''
    assert parsed['piece'] == "king"

def test_parse_castles_queenside():
    notation = '0-0-0'
    parsed = parse_notation(notation)
    
    assert parsed['kingsideCastle'] is None
    assert parsed['queensideCastle'] is True
    assert parsed['notation'] == ''
    assert parsed['piece'] == "king"

def test_parse_capture():
    notation = 'Nxe5'
    parsed = parse_notation(notation)
    
    assert parsed['piece'] == KNIGHT
    assert parsed['to'] == 'e5'
    assert parsed['capture'] is True

def test_is_valid_knight_move():
    notation = 'Nc3'
    assert is_valid_notation(notation)

def test_is_valid_pawn_move():
    notation = 'e4'
    assert is_valid_notation(notation)

def test_invalid_promotion():
    notation = 'e8=P'  # Promoting to a pawn is invalid
    assert not is_valid_notation(notation)

def test_is_valid_checkmate():
    notation = 'Qh8#'
    parsed = parse_notation(notation)
    
    assert parsed['checkmate'] is True
    assert parsed['piece'] == QUEEN
    assert parsed['to'] == 'h8'
    assert is_valid_notation(notation)

def test_is_valid_check():
    notation = 'Qh8+'
    parsed = parse_notation(notation)
    
    assert parsed['check'] is True
    assert parsed['piece'] == QUEEN
    assert parsed['to'] == 'h8'
    assert is_valid_notation(notation)

def test_knight_capture_shared_rank():
    notation = 'Ncxd5'
    parsed = parse_notation(notation)

    assert parsed['capture'] is True
    assert parsed['piece'] == KNIGHT
    assert parsed['to'] == 'd5'
    assert parsed['from'] == 'c'
    assert is_valid_notation(notation)

def test_rook_capture_shared_file():
    notation = 'R3d4'
    parsed = parse_notation(notation)

    assert parsed['piece'] == ROOK
    assert parsed['to'] == 'd4'
    assert parsed['from'] == '3'
    assert is_valid_notation(notation)

def test_knight_capture_shared_rank_shared_file():
    notation = 'Nc3xd5'
    parsed = parse_notation(notation)

    assert parsed['capture'] is True
    assert parsed['piece'] == KNIGHT
    assert parsed['to'] == 'd5'
    assert parsed['from'] == 'c3'
    assert is_valid_notation(notation)

def test_capture_shared_diagonal():
    notation = 'Bcxe5'
    parsed = parse_notation(notation)

    assert parsed['capture'] is True
    assert parsed['piece'] == BISHOP
    assert parsed['to'] == 'e5'
    assert parsed['from'] == 'c'
    assert is_valid_notation(notation)


# ------------------------------- Test construct_algebraic_notation --------------------------------


def test_pawn_move():
    algebraic = construct_algebraic_notation(
        piece_type='pawn',
        piece_from_sqr='E2',
        to_square='E4',
        validators={'capture': False, 'check': False, 'checkmate': False},
        same_type_pieces=[],
        active_colour='white'
    )
    assert algebraic == 'e4'

def test_knight_move():
    algebraic = construct_algebraic_notation(
        piece_type='knight',
        piece_from_sqr='G1',
        to_square='F3',
        validators={'capture': False, 'check': False, 'checkmate': False},
        same_type_pieces=[],
        active_colour='white'
    )
    assert algebraic == 'Nf3'

def test_pawn_capture():
    algebraic = construct_algebraic_notation(
        piece_type='pawn',
        piece_from_sqr='E5',
        to_square='D6',
        validators={'capture': True, 'check': False, 'checkmate': False},
        same_type_pieces=[],
        active_colour='white'
    )
    assert algebraic == 'exd6'

def test_piece_capture():
    algebraic = construct_algebraic_notation(
        piece_type='bishop',
        piece_from_sqr='C4',
        to_square='F7',
        validators={'capture': True, 'check': False, 'checkmate': False},
        same_type_pieces=[],
        active_colour='white'
    )
    assert algebraic == 'Bxf7'

def test_disambiguation_file():
    algebraic = construct_algebraic_notation(
        piece_type='knight',
        piece_from_sqr='G5',
        to_square='E4',
        validators={'capture': False, 'check': False, 'checkmate': False, 'sharedFile': True},
        same_type_pieces=[{'occupied_square': 'G3'}],
        active_colour='white'
    )
    assert algebraic == 'N5e4'

def test_disambiguation_rank():
    algebraic = construct_algebraic_notation(
        piece_type='queen',
        piece_from_sqr='A1',
        to_square='A5',
        validators={'capture': False, 'check': False, 'checkmate': False, 'sharedRank': True},
        same_type_pieces=[{'occupied_square': 'E1'}],
        active_colour='white'
    )
    assert algebraic == 'Qaa5'

def test_promotion():
    algebraic = construct_algebraic_notation(
        piece_type='pawn',
        piece_from_sqr='E7',
        to_square='E8',
        validators={'capture': False, 'promotion': 'queen', 'check': False, 'checkmate': False},
        same_type_pieces=[],
        active_colour='white'
    )
    assert algebraic == 'e8=Q'

def test_promotion_with_capture():
    algebraic = construct_algebraic_notation(
        piece_type='pawn',
        piece_from_sqr='E7',
        to_square='F8',
        validators={'capture': True, 'promotion': 'queen', 'check': False, 'checkmate': False},
        same_type_pieces=[],
        active_colour='white'
    )
    assert algebraic == 'exf8=Q'

def test_check():
    algebraic = construct_algebraic_notation(
        piece_type='queen',
        piece_from_sqr='D1',
        to_square='H5',
        validators={'capture': False, 'check': True, 'checkmate': False},
        same_type_pieces=[],
        active_colour='white'
    )
    assert algebraic == 'Qh5+'

def test_checkmate():
    algebraic = construct_algebraic_notation(
        piece_type='queen',
        piece_from_sqr='D1',
        to_square='D8',
        validators={'capture': True, 'checkmate': True},
        same_type_pieces=[],
        active_colour='white'
    )
    assert algebraic == 'Qxd8#'

def test_castle_kingside():
    # Castling is handled separately in create_algebraic_notation, but including for completeness
    # Assuming validators would return 'O-O' directly
    pass  # No need to test here as construct_algebraic_notation is not used for castling moves

def test_castle_queenside():
    # Same as above
    pass  # No need to test here as construct_algebraic_notation is not used for castling moves
