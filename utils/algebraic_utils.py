KING = 'King'
QUEEN = 'Queen'
ROOK = 'Rook'
BISHOP = 'Bishop'
KNIGHT = 'Knight'
PAWN = 'Pawn'

pieces = {
    'english': {
        'K': KING, 'Q': QUEEN, 'R': ROOK, 'B': BISHOP, 'N': KNIGHT, 'P': PAWN,
        'k': KING, 'q': QUEEN, 'r': ROOK, 'b': BISHOP, 'n': KNIGHT, 'p': PAWN,
    },
}

def remove_draw_offer(parse_obj):
    """
    e5= -> e5
    """
    if parse_obj['notation'].endswith(' (=)'):
        parse_obj['offeredDraw'] = True
        parse_obj['notation'] = parse_obj['notation'][:-4]
    return parse_obj

def remove_en_passant(parse_obj):
    """
    exd5 e.p. -> exd5
    """
    if parse_obj['notation'].endswith(' e.p.'):
        parse_obj['enPassant'] = True
        parse_obj['notation'] = parse_obj['notation'][:-5]
    return parse_obj

def remove_checks(parse_obj):
    """
    e5++, e5# -> e5
    these are checkmate
    
    e5+ -> e5
    this is a check
    """
    if parse_obj['notation'].endswith('++'):
        parse_obj['checkmate'] = True
        parse_obj['notation'] = parse_obj['notation'][:-2]
    elif parse_obj['notation'].endswith('#'):
        parse_obj['checkmate'] = True
        parse_obj['notation'] = parse_obj['notation'][:-1]
    elif parse_obj['notation'].endswith('+'):
        parse_obj['check'] = True
        parse_obj['notation'] = parse_obj['notation'][:-1]
    return parse_obj

def remove_castles(parse_obj):
    """
    0-0-0, 0-0 -> ''
    Three 0s denotes 'long castle (queenside)' and two denotes 'short castle (kingside)'
    """
    if parse_obj['notation'] in ['0-0-0', 'O-O-O']:
        parse_obj['queensideCastle'] = True
        parse_obj['notation'] = ''
        parse_obj['piece'] = 'king'
    elif parse_obj['notation'] in ['0-0', 'O-O']:
        parse_obj['kingsideCastle'] = True
        parse_obj['notation'] = ''
        parse_obj['piece'] = 'king'
    return parse_obj

def remove_promotion(parse_obj):
    """
    e8=Q -> e8
    """
    possible_piece = parse_obj['notation'][-1]  # last char
    has_equal = parse_obj['notation'][-2:-1] == '='     # second to last char

    if possible_piece in pieces[parse_obj['language']]:
        notation = parse_obj['notation'][:-2] if has_equal else parse_obj['notation'][:-1]      # remove last two chars if there is an '=' else remove only last one char
        parse_obj['promotion'] = pieces[parse_obj['language']][possible_piece]
        parse_obj['notation'] = notation
    return parse_obj

def remove_to(parse_obj):
    if parse_obj['notation'][-2:].isalnum():
        parse_obj['to'] = parse_obj['notation'][-2:]
        parse_obj['notation'] = parse_obj['notation'][:-2]
    return parse_obj

def remove_capture(parse_obj):
    if parse_obj['notation'].endswith('x'):
        parse_obj['capture'] = True
        parse_obj['notation'] = parse_obj['notation'][:-1]
    return parse_obj

def remove_from(parse_obj):
    if len(parse_obj['notation']) >= 2 and parse_obj['notation'][-2:].isalnum():
        parse_obj['from'] = parse_obj['notation'][-2:]
        parse_obj['notation'] = parse_obj['notation'][:-2]
    elif parse_obj['notation'][-1:].isalnum():
        parse_obj['from'] = parse_obj['notation'][-1]
        parse_obj['notation'] = parse_obj['notation'][:-1]
    return parse_obj

def remove_piece(parse_obj):
    # Check the first character for the piece (not the whole notation)
    piece_char = parse_obj['notation'][0]
    if piece_char in pieces[parse_obj['language']]:
        parse_obj['piece'] = pieces[parse_obj['language']][piece_char]
        parse_obj['notation'] = parse_obj['notation'][1:]  # Remove the first character (the piece)
    else:
        parse_obj['piece'] = PAWN  # Default to pawn if no piece identifier is found
    return parse_obj

def is_valid_draw(parse_obj):
    return not (parse_obj.get('offeredDraw') and parse_obj.get('checkmate'))

def is_valid_en_passant(parse_obj):
    if not parse_obj.get('enPassant'):
        return True
    if parse_obj.get('queensideCastle') or parse_obj.get('kingsideCastle'):
        return False
    if parse_obj.get('piece') != PAWN:
        return False
    if not parse_obj.get('to'):
        return False
    if not parse_obj['to'].endswith(('6', '3')):
        return False
    if not parse_obj.get('capture'):
        return False
    return True

def is_valid_check(parse_obj):
    if not (parse_obj.get('check') or parse_obj.get('checkmate')):
        return True
    if not parse_obj.get('from'):
        return True
    if not parse_obj.get('to') and not (parse_obj.get('queensideCastle') or parse_obj.get('kingsideCastle')):
        return False
    if parse_obj.get('piece') == KING:
        if parse_obj.get('from')[0] == parse_obj.get('to')[0]:
            return False
    return True

def is_valid_promotion(parse_obj):
    if not parse_obj.get('promotion'):
        return True
    if parse_obj['promotion'] == PAWN:
        return False
    if not parse_obj.get('to'):
        return False
    if not parse_obj['to'].endswith(('8', '1')):
        return False
    if parse_obj.get('piece') != PAWN:
        return False
    return True

def is_valid_capture(parse_obj):
    if parse_obj.get('from') and parse_obj.get('to') and parse_obj.get('capture') and parse_obj.get('piece') == PAWN:
        if parse_obj['from'][0] == parse_obj['to'][0]:
            return False
    return True

def is_valid_move(parse_obj):
    if parse_obj.get('queensideCastle') or parse_obj.get('kingsideCastle'):
        return True
    if not parse_obj.get('to'):
        return False
    if parse_obj.get('from') == parse_obj.get('to'):
        return False
    return True

def parse_notation(notation, language='english'):
    parse_obj = {
        'notation': notation,
        'language': language,
        'offeredDraw': None,
        'enPassant': None,
        'check': None,
        'checkmate': None,
        'queensideCastle': None,
        'kingsideCastle': None,
        'promotion': None,
        'to': None,
        'capture': None,
        'from': None,
        'piece': None,
    }

    # Adjust the order of parsing
    parse_obj = remove_piece(parse_obj)        # Piece needs to be identified first
    parse_obj = remove_draw_offer(parse_obj)
    parse_obj = remove_en_passant(parse_obj)
    parse_obj = remove_checks(parse_obj)
    parse_obj = remove_castles(parse_obj)
    if parse_obj["notation"] == "":
        # castling detected, can break and return now
        return parse_obj
    parse_obj = remove_promotion(parse_obj)
    parse_obj = remove_to(parse_obj)
    parse_obj = remove_capture(parse_obj)
    parse_obj = remove_from(parse_obj)

    return parse_obj

def is_valid_parsed_notation(parse_obj):
    return (
        is_valid_draw(parse_obj) and
        is_valid_en_passant(parse_obj) and
        is_valid_check(parse_obj) and
        is_valid_promotion(parse_obj) and
        is_valid_capture(parse_obj) and
        is_valid_move(parse_obj)
    )

def is_valid_notation(notation, language='english'):
    return is_valid_parsed_notation(parse_notation(notation, language))

print(parse_notation("Qb8"))








def construct_algebraic_notation(
    piece_type: str,
    piece_from_sqr: str,
    to_square: str,
    validators: dict,
    same_type_pieces: list,
    active_colour: str
) -> str:
    """
    Constructs the algebraic notation string for a move.

    Args:
        piece_type (str): The type of the piece being moved (e.g., 'pawn', 'knight').
        piece_from_sqr (str): The starting square of the piece (e.g., 'E2').
        to_square (str): The destination square of the piece (e.g., 'E4').
        validators (dict): A dictionary containing flags for special move conditions.
        same_type_pieces (list): List of other pieces of the same type that can move to the to_square.
        active_colour (str): The active player's colour ('white' or 'black').

    Returns:
        str: The algebraic notation string for the move.
    """
    algebraic = ""
    alg_dict = {
        "queen": "Q",
        "pawn": "",
        "bishop": "B",
        "knight": "N",
        "king": "K",
        "rook": "R",
    }

    temp_piece_type = piece_type.lower()

    # Part 1: Piece symbol (absent for pawns)
    if temp_piece_type != "pawn":
        piece_symbol = alg_dict[temp_piece_type]
        algebraic += piece_symbol

    # Part 2: Disambiguation
    if same_type_pieces and temp_piece_type != "pawn":
        from_file = piece_from_sqr[0].lower()
        from_rank = piece_from_sqr[1]
        shared_file = validators.get("sharedFile", False)
        shared_rank = validators.get("sharedRank", False)

        if shared_file and shared_rank:
            algebraic += piece_from_sqr.lower()
        elif shared_file:
            algebraic += from_rank
        elif shared_rank:
            algebraic += from_file
        else:
            algebraic += from_file

    # For pawn captures, include the from file
    if temp_piece_type == "pawn" and validators.get("capture"):
        algebraic += piece_from_sqr[0].lower()

    # Part 3: Capture indicator
    if validators.get("capture"):
        algebraic += "x"

    # Part 4: Destination square
    algebraic += to_square.lower()

    # Part 5: Promotion
    if validators.get("promotion"):
        promotion_piece = validators["promotion"].lower()
        algebraic += f"={alg_dict[promotion_piece]}"

    # Part 6: Check or Checkmate
    if validators.get("checkmate"):
        algebraic += "#"
    elif validators.get("check"):
        algebraic += "+"

    return algebraic













