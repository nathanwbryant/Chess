import pytest
from algebraic_notation import parse_notation, is_valid_notation

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
    assert parsed['piece'] is None

def test_parse_castles_queenside():
    notation = '0-0-0'
    parsed = parse_notation(notation)
    
    assert parsed['kingsideCastle'] is None
    assert parsed['queensideCastle'] is True
    assert parsed['notation'] == ''
    assert parsed['piece'] is None

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
