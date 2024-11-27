import pytest
from bot import Bot
from chessboard import Board, LegalMoveGenerator, Pawn, Bishop, Knight, Queen, King, Rook
import copy
from algebraic_utils import parse_notation

def test_pawn_advance():
    # Initialize the Bot and Board
    bot = Bot()
    pawn = bot.board.position['E2']
    move = (pawn, 'E4')
    notation = bot.create_algebraic_notation(move)
    assert notation == 'e4'

def test_pawn_capture():
    """
    Test a pawn capturing another piece.
    """
    bot = Bot(fen="rnbqkbnr/ppp1pppp/8/8/8/3p4/PPPPPPPP/RNBQKBNR w KQkq - 0 1") 
    pawn = bot.board.position['E2']
    bot.board.position['D3']
    move = (pawn, 'D3')
    result = bot.create_algebraic_notation(move)
    assert result == 'exd3'

def test_knight_move():
    """
    Test a simple knight move from G1 to F3.
    """
    bot = Bot()
    knight = bot.board.position['G1']
    move = (knight, 'F3')
    result = bot.create_algebraic_notation(move)
    assert result == 'Nf3'

def test_knight_capture():
    """
    Test a knight capturing an opposing piece.
    """
    bot = Bot(fen="rnbqkbnr/ppppp1pp/8/8/8/8/PPPPp1PP/RNBQKBNR w KQkq - 0 1")
    knight = bot.board.position['G1']
    move = (knight, 'E2')
    result = bot.create_algebraic_notation(move)
    assert result == 'Nxe2'

def test_castle_kingside():
    """
    Test kingside castling for white.
    """
    bot = Bot(fen="rnbqkb1r/ppp1nppp/3pp3/8/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 0 1")
    king = bot.board.position['E1']
    move = (king, 'G1')
    result = bot.create_algebraic_notation(move)
    assert result == 'O-O'

def test_castle_queenside():
    """
    Test queenside castling for white.
    """
    bot = Bot(fen="rn1qkb1r/pppbnppp/3pp3/8/4PB2/2NP1Q2/PPP2PPP/R3KBNR w KQkq - 0 1")
    king = bot.board.position['E1']
    move = (king, 'C1')
    result = bot.create_algebraic_notation(move)
    assert result == 'O-O-O'

def test_pawn_promotion():
    """
    Test pawn promotion to a queen.
    """
    bot = Bot(fen="rnq3rk/ppp1Pppp/2bpp3/8/5B2/2NPQ3/PPP2PPP/2KR1BNR w - - 0 1")
    pawn = bot.board.position['E7']
    move = (pawn, 'E8')
    result = bot.create_algebraic_notation(move)
    assert result == 'e8=Q'

def test_queen_move():
    """
    Test a simple queen move from D1 to H5.
    """
    bot = Bot()
    queen = Queen(colour='white', occupied_square='D1')
    bot.board.position['D1'] = queen
    move = (queen, 'H5')
    result = bot.create_algebraic_notation(move)
    assert result == 'Qh5'

def test_bishop_capture():
    """
    Test a bishop capturing an opposing piece.
    """
    bot = Bot()
    bishop = Bishop(colour='white', occupied_square='C1')
    bot.board.position['C1'] = bishop
    opponent_piece = Pawn(colour='black', occupied_square='F4')
    bot.board.position['F4'] = opponent_piece
    move = (bishop, 'F4')
    result = bot.create_algebraic_notation(move)
    assert result == 'Bxf4'

def test_queen_move():
    """
    Test a simple queen move from D1 to H5.
    """
    bot = Bot("rnq3rk/ppp1Pppp/2bpp3/8/5B2/2NP4/PPP2PPP/2KQ1BNR w - - 0 1")
    queen = bot.board.position['D1']
    move = (queen, 'H5')
    result = bot.create_algebraic_notation(move)
    assert result == 'Qh5'

def test_bishop_capture():
    """
    Test a bishop capturing an opposing piece.
    """
    bot = Bot(fen="rnq3rk/ppp2ppp/2bp4/8/4Pp2/2NP4/PPP2PPP/1KBQ1BNR w - - 0 1")
    bishop = bot.board.position['C1']
    move = (bishop, 'F4')
    result = bot.create_algebraic_notation(move)
    assert result == 'Bxf4'

def test_knight_capture_shared_rank():
    """
    Test a knight capturing a piece, that could be captured by another knight on the same rank
    """
    bot = Bot(fen="r3kb1r/pppbqppp/2np1n2/4p3/4P3/2PN1N2/PPQP1PPP/R1B1KB1R w KQkq - 0 1")
    knight = bot.board.position['D3']
    move = (knight, 'E5')
    result = bot.create_algebraic_notation(move)
    assert result == 'Ndxe5'

def test_knight_capture_shared_rank_and_file():
    """
    Test a knight capturing a piece, that could be captured by another knight on the same rank and another on the same file
    """
    bot = Bot(fen="r3kb1r/pppNqppp/2np1n2/4p3/4P3/2PN1N2/PPQP1PPP/R1B1KB1R w KQkq - 0 1")
    knight = bot.board.position['D3']
    move = (knight, 'E5')
    result = bot.create_algebraic_notation(move)
    assert result == 'Nd3xe5'

def test_white_en_passant_capture():
    """
    Test a white pawn capturing en passant
    """
    bot = Bot(fen="r3kb1r/ppp1qp1p/2np1n2/4pPpP/3PP3/2P5/PPQ1N1P1/R1B1KB1R w KQkq g6 0 25")
    pawn = bot.board.position['F5']
    move = (pawn, "G6")
    result = bot.create_algebraic_notation(move)
    assert result == 'fxg6'

def test_queen_check():
    """
    Test a queen checking the king
    """
    bot = Bot(fen="r3kb1r/ppp2p2/2npqnp1/4p2P/Q2PP3/2P5/PP2N1P1/R1B1KB1R w KQkq - 2 27")
    queen = bot.board.position['A4']
    move = (queen, "C6")
    result = bot.create_algebraic_notation(move)
    assert result == 'Qxc6+'

def test_checkmate():
    """
    Test a queen checkmating the black king
    """
    bot = Bot(fen="rnq3rk/ppp1Pp2/2bpp2p/7Q/8/2NP4/PPP2PPP/2K2BNR w - - 0 3")
    queen = bot.board.position['H5']
    move = (queen, "H6")
    result = bot.create_algebraic_notation(move)
    assert result == 'Qxh6#'

# ---------------------------- Test parse_and_adjust_move ----------------------------------------

# New tests for parse_and_adjust_move function
def test_normal_pawn_move():
    bot = Bot()
    move = "e4"
    result = bot.parse_and_adjust_move(move)
    assert result == {
        'notation': '',
        'language': 'english',
        'offeredDraw': None,
        'enPassant': None,
        'check': None,
        'checkmate': None,
        'queensideCastle': None,
        'kingsideCastle': None,
        'promotion': None,
        'to': 'E4',
        'capture': None,
        'from': None,
        'piece': 'pawn'
    }

def test_knight_move():
    bot = Bot()
    move = "Nf3"
    result = bot.parse_and_adjust_move(move)
    assert result == {
        'notation': '',
        'language': 'english',
        'offeredDraw': None,
        'enPassant': None,
        'check': None,
        'checkmate': None,
        'queensideCastle': None,
        'kingsideCastle': None,
        'promotion': None,
        'to': 'F3',
        'capture': None,
        'from': None,
        'piece': 'knight'
    }

def test_queenside_castle():
    bot = Bot()
    move = "O-O-O"
    result = bot.parse_and_adjust_move(move)
    assert result == {
        'notation': '',
        'language': 'english',
        'offeredDraw': None,
        'enPassant': None,
        'check': None,
        'checkmate': None,
        'queensideCastle': True,
        'kingsideCastle': None,
        'promotion': None,
        'to': None,
        'capture': None,
        'from': None,
        'piece': 'king'
    }

def test_pawn_capture():
    bot = Bot()
    move = "exd5"
    result = bot.parse_and_adjust_move(move)
    assert result == {
        'notation': '',
        'language': 'english',
        'offeredDraw': None,
        'enPassant': None,
        'check': None,
        'checkmate': None,
        'queensideCastle': None,
        'kingsideCastle': None,
        'promotion': None,
        'to': 'D5',
        'capture': True,
        'from': 'E',
        'piece': 'pawn'
    }

def test_knight_capture():
    bot = Bot()
    move = "Nxe4"
    result = bot.parse_and_adjust_move(move)
    assert result == {
        'notation': '',
        'language': 'english',
        'offeredDraw': None,
        'enPassant': None,
        'check': None,
        'checkmate': None,
        'queensideCastle': None,
        'kingsideCastle': None,
        'promotion': None,
        'to': 'E4',
        'capture': True,
        'from': None,
        'piece': 'knight'
    }

def test_pawn_promotion():
    bot = Bot()
    move = "e8=Q"
    result = bot.parse_and_adjust_move(move)
    assert result == {
        'notation': '',
        'language': 'english',
        'offeredDraw': None,
        'enPassant': None,
        'check': None,
        'checkmate': None,
        'queensideCastle': None,
        'kingsideCastle': None,
        'promotion': 'Queen',
        'to': 'E8',
        'capture': None,
        'from': None,
        'piece': 'pawn'
    }

def test_check_move():
    bot = Bot()
    move = "Qh5+"
    result = bot.parse_and_adjust_move(move)
    assert result == {
        'notation': '',
        'language': 'english',
        'offeredDraw': None,
        'enPassant': None,
        'check': True,
        'checkmate': None,
        'queensideCastle': None,
        'kingsideCastle': None,
        'promotion': None,
        'to': 'H5',
        'capture': None,
        'from': None,
        'piece': 'queen'
    }

def test_checkmate_move():
    bot = Bot()
    move = "Qh5#"
    result = bot.parse_and_adjust_move(move)
    assert result == {
        'notation': '',
        'language': 'english',
        'offeredDraw': None,
        'enPassant': None,
        'check': None,
        'checkmate': True,
        'queensideCastle': None,
        'kingsideCastle': None,
        'promotion': None,
        'to': 'H5',
        'capture': None,
        'from': None,
        'piece': 'queen'
    }

# ----------------------- Test find_moving_piece ---------------------------------
# Helper function for simple searches, when only one piece of the type given can access the 
# given square
def test_normal_pawn_move():
    bot = Bot()
    parsed_move = {
        'notation': '',
        'language': 'english',
        'offeredDraw': None,
        'enPassant': None,
        'check': None,
        'checkmate': None,
        'queensideCastle': None,
        'kingsideCastle': None,
        'promotion': None,
        'to': 'E4',
        'capture': None,
        'from': None,
        'piece': 'pawn'
    }
    result = bot.find_moving_piece(parsed_move=parsed_move, from_square=parsed_move['from'], board=bot.board, user_colour="white")

    assert result == bot.board.position['E2']


def test_knight_move():
    bot = Bot()
    parsed_move = {
        'notation': '',
        'language': 'english',
        'offeredDraw': None,
        'enPassant': None,
        'check': None,
        'checkmate': None,
        'queensideCastle': None,
        'kingsideCastle': None,
        'promotion': None,
        'to': 'F3',
        'capture': None,
        'from': None,
        'piece': 'knight'
    }
    result = bot.find_moving_piece(parsed_move=parsed_move, from_square=parsed_move['from'], board=bot.board, user_colour="white")

    assert result == bot.board.position['G1']

# -------------------------- Test verify_move castling --------------------------------------------
def test_white_queenside_castle_algebraic():
    """
    Test white queenside castle.
    Input -> O-O-O, "white"
    Output -> parsed move dictionary with to and from squares
    """
    bot = Bot(fen="rnbq1rk1/ppp1bppp/3p1n2/4p3/4P3/2NPB3/PPP1QPPP/R3KBNR w KQ - 5 6")
    parsed_move = {
        'notation': '',
        'language': 'english',
        'offeredDraw': None,
        'enPassant': None,
        'check': None,
        'checkmate': None,
        'queensideCastle': True,
        'kingsideCastle': None,
        'promotion': None,
        'to': None,
        'capture': None,
        'from': None,
        'piece': 'king'
    }
    result = bot.verify_move(move="O-O-O", user_colour="white")

    assert result == {
        'notation': '',
        'language': 'english',
        'offeredDraw': None,
        'enPassant': None,
        'check': None,
        'checkmate': None,
        'queensideCastle': True,
        'kingsideCastle': None,
        'promotion': None,
        'to': 'C1',
        'capture': None,
        'from': 'E1',
        'piece': 'king'
    }

def test_black_kingside_castle_algebraic():
    """
    Test black kingside castle.
    Input -> O-O, "black"
    Output -> parsed move dictionary with to and from squares
    """
    bot = Bot(fen="rnbqk2r/ppp1bppp/3p1n2/4p3/4P3/2NPB3/PPP1QPPP/R3KBNR b KQkq - 4 5")
    parsed_move = {
        'notation': '',
        'language': 'english',
        'offeredDraw': None,
        'enPassant': None,
        'check': None,
        'checkmate': None,
        'queensideCastle': None,
        'kingsideCastle': True,
        'promotion': None,
        'to': None,
        'capture': None,
        'from': None,
        'piece': 'king'
    }
    result = bot.verify_move(move="O-O", user_colour="black")

    assert result == {
        'notation': '',
        'language': 'english',
        'offeredDraw': None,
        'enPassant': None,
        'check': None,
        'checkmate': None,
        'queensideCastle': None,
        'kingsideCastle': True,
        'promotion': None,
        'to': 'G8',
        'capture': None,
        'from': 'E8',
        'piece': 'king'
    }

def test_blocked_illegal_kingside_castle_algebraic():
    """
    Test that the function detects a blocked path to castling
    """
    bot = Bot(fen="rnbqkb1r/ppp2ppp/3p1n2/4p3/4P3/2NPBP2/PPP1Q1PP/R3KBNR b KQkq - 0 6")
    parsed_move = {
        'notation': '',
        'language': 'english',
        'offeredDraw': None,
        'enPassant': None,
        'check': None,
        'checkmate': None,
        'queensideCastle': None,
        'kingsideCastle': True,
        'promotion': None,
        'to': None,
        'capture': None,
        'from': None,
        'piece': 'king'
    }
    result = bot.verify_move(move="O-O", user_colour="black")

    assert result == False

def test_in_check_illegal_kingside_castle_algebraic():
    """
    Test that the function detects that a user cannot castle whilst in check
    """
    bot=Bot(fen="rnbqk2r/pppn1ppp/3p4/4P3/4P2b/2N1BP2/PPP1Q1PP/R3KBNR w KQkq - 1 9")
    parsed_move = {
        'notation': '',
        'language': 'english',
        'offeredDraw': None,
        'enPassant': None,
        'check': None,
        'checkmate': None,
        'queensideCastle': True,
        'kingsideCastle': None,
        'promotion': None,
        'to': None,
        'capture': None,
        'from': None,
        'piece': 'king'
    }
    result = bot.verify_move(move="O-O-O", user_colour="white")

    assert result == False

def test_illegal_castle_through_check_algebraic():
    """
    Test that the function prevents castle through or onto a square controlled by an opposing piece
    """
    bot=Bot(fen="rn1qk2r/ppp1bppp/5n2/1b1Pp3/4BP2/5N2/PPPP2PP/RNBQK2R w KQkq - 7 7")
    parsed_move = {
        'notation': '',
        'language': 'english',
        'offeredDraw': None,
        'enPassant': None,
        'check': None,
        'checkmate': None,
        'queensideCastle': None,
        'kingsideCastle': True,
        'promotion': None,
        'to': None,
        'capture': None,
        'from': None,
        'piece': 'king'
    }
    result = bot.verify_move(move="O-O", user_colour="white")

    assert result == False

def test_illegal_castle_lost_rights():
    """
    Test that the function is aware that rights to castle are lost and prevents castling
    """
    bot=Bot(fen="rn1qk2r/pppbbppp/5n2/3Pp3/4BP2/5N2/PPPP2PP/RNBQK2R w kq - 11 9")
    parsed_move = {
        'notation': '',
        'language': 'english',
        'offeredDraw': None,
        'enPassant': None,
        'check': None,
        'checkmate': None,
        'queensideCastle': None,
        'kingsideCastle': True,
        'promotion': None,
        'to': None,
        'capture': None,
        'from': None,
        'piece': 'king'
    }
    result = bot.verify_move(move="O-O", user_colour="white")

    assert result == False

# -------------------------- Test verify_move in check ------------------------------------

def test_illegal_queen_move_in_check():
    """
    Test that the legal moves for white does not include what would have been legal otherwise
    """
    bot=Bot(fen="r2qk2r/pppbbppp/3N1n2/n2Pp3/4BP2/5N2/PPPP2PP/R1BQK2R b kq - 16 11")
    parsed_move = {
        'notation': '',
        'language': 'english',
        'offeredDraw': None,
        'enPassant': None,
        'check': None,
        'checkmate': None,
        'queensideCastle': None,
        'kingsideCastle': True,
        'promotion': None,
        'to': 'b8',
        'capture': None,
        'from': None,
        'piece': 'Queen'
    }
    result = bot.verify_move(move="Qb8", user_colour="black")

    assert result == False

def test_illegal_blocking_move_double_check():
    """
    Test that only the king can move whilst in double check
    """
    bot=Bot(fen="rqk5/4bppr/pN3n1p/n3pb2/4BP2/2QP1N2/PPP3PP/R1B1K2R b - - 3 20")
    parsed_move = {
        'notation': '',
        'language': 'english',
        'offeredDraw': None,
        'enPassant': None,
        'check': None,
        'checkmate': None,
        'queensideCastle': None,
        'kingsideCastle': True,
        'promotion': None,
        'to': 'c8',
        'capture': None,
        'from': None,
        'piece': 'Queen'
    }
    result = bot.verify_move(move="Qb8", user_colour="black")
    king = bot.board.position["C8"]
    print("legal moves: ", bot.board.black_legal_moves)
    assert result == False
    assert bot.board.black_legal_moves == {king : ["D8"]}
    assert len(bot.board.black_legal_moves.keys()) == 1


