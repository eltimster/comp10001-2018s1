# dictionary of tests, one for each function in the project spec; in each case, list a number of function calls (as a str), and the correct output for each

# Version: 1.0
# Created 28/4/18




test_cases = {
    "comp10001bo_match_build":
    [
        # VALID: 2S on empty build stack
        ("""submission.comp10001bo_match_build('2S', [])""", True), 
        # VALID: KH on empty build stack
        ("""submission.comp10001bo_match_build('KH', [])""", True), 
        # INVALID: AH on empty build stack (ace can't start stack)
        ("""submission.comp10001bo_match_build('AH', [])""", False), 
        # VALID: 3S on build stack with 2C at top
        ("""submission.comp10001bo_match_build('3C', ['2C'])""", True), 
        # VALID: 4H on build stack with 3H at top
        ("""submission.comp10001bo_match_build('4H', ['2D', '3H'])""", True), 
        # VALID: 2H on build stack with 3H at top
        ("""submission.comp10001bo_match_build('2H', ['2D', '3H'])""", True), 
        # VALID: AH on build stack with 3H at top
        ("""submission.comp10001bo_match_build('AH', ['2D', '3H'])""", True), 
        # INVALID: AS on build stack with 3H at top (colour mismatch)
        ("""submission.comp10001bo_match_build('AS', ['2D', '3H'])""", False), 
        # VALID: 5S on empty build stack
        ("""submission.comp10001bo_match_build('5S', [])""", False), 
        # INVALID: 3H on build stack with 3H at top (value mismatch)
        ("""submission.comp10001bo_match_build('3H', ['2D', '3H'])""", False), 
        # INVALID: 4C on build stack with 3H at top (colour mismatch)
        ("""submission.comp10001bo_match_build('4C', ['2D', '3H'])""", False), 
    ],    

    "comp10001bo_match_discard":
    [
        # NON-FINAL VALID: 4S on empty discard stack of that player
        ("""submission.comp10001bo_match_discard('4S', [], 2, 2)""", 2), 
        # INVALID: 4S on empty discard stack of different player
        ("""submission.comp10001bo_match_discard('4S', [], 2, 0)""", 0), 
        # INVALID: can't start a stack from anything other than hand
        ("""submission.comp10001bo_match_discard('4S', [], 2, 2, False)""", 0), 
        # NON-FINAL VALID: 4S on discard stack with 3H at top (same player)
        ("""submission.comp10001bo_match_discard('4S', ['3H'], 2, 2)""", 1), 
        # NON-FINAL VALID: 4S on discard stack with 3H at top (different player)
        ("""submission.comp10001bo_match_discard('4S', ['3H'], 2, 3)""", 1), 
        # NON-FINAL VALID: 4S on discard stack with 3H at top (different player)
        ("""submission.comp10001bo_match_discard('4S', ['3H'], 2, 3, False)""", 1), 
        # INVALID: can't place Ace on discard stack
        ("""submission.comp10001bo_match_discard('AH', ['KS'], 2, 3)""", 0), 
        # NON-FINAL VALID: wraparound from King to 2
        ("""submission.comp10001bo_match_discard('2H', ['KS'], 2, 3)""", 1), 
        # FINAL VALID: Queen and 2 not adjacent
        ("""submission.comp10001bo_match_discard('2H', ['QS'], 2, 3)""", 2), 
        # FINAL VALID: 4 and 2 not adjacent
        ("""submission.comp10001bo_match_discard('2H', ['4S'], 2, 3)""", 2), 
        # FINAL VALID: 4S on discard stack with 3H at top (different player)
        ("""submission.comp10001bo_match_discard('4H', ['3H'], 2, 3)""", 2), 
        # INVALID: can't illegaly place card if not from hand
        ("""submission.comp10001bo_match_discard('4H', ['3H'], 2, 2, False)""", 0), 
    ],

    "comp10001bo_is_valid_play":
    [
        # NON-FINAL VALID (from hand to build stack 0)
        ("""submission.comp10001bo_is_valid_play((0, '2C', (0, 0)), 0, ['2C', 'AS', '9D', '0D', '0S'], (('9C', 8), ('0D', 8), ('3H', 8), ('KD', 8)), (([], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), ([], [], [], []))""", 1), 
        # INVALID: doesn't hold card
        ("""submission.comp10001bo_is_valid_play((0, '2C', (0, 0)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('9C', 8), ('0D', 8), ('3H', 8), ('KD', 8)), (([], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), ([], [], [], []))""", 0), 
        # INVALID: invalid stack (build stack 4)
        ("""submission.comp10001bo_is_valid_play((0, '3C', (0, 4)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('9C', 8), ('0D', 8), ('3H', 8), ('KD', 8)), (([], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), ([], [], [], []))""", 0), 
        # INVALID: can't play to build stack 0 (can't start with 3)
        ("""submission.comp10001bo_is_valid_play((0, '3C', (0, 0)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('9C', 8), ('0D', 8), ('3H', 8), ('KD', 8)), (([], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), ([], [], [], []))""", 0), 
        # NON-FINAL VALID (from hand to non-empty build stack 0)
        ("""submission.comp10001bo_is_valid_play((0, '3C', (0, 0)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('9C', 8), ('0D', 8), ('3H', 8), ('KD', 8)), (([], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), (['2S'], [], [], []))""", 1), 
        # NON-FINAL VALID (from stockpile to empty build stack 1)
        ("""submission.comp10001bo_is_valid_play((2, '2C', (0, 1)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('2C', 8), ('0D', 8), ('3H', 8), ('KD', 8)), (([], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), (['2S'], [], [], []))""", 1), 
        # INVALID: attempt to play card that is not top card of own stockpile
        ("""submission.comp10001bo_is_valid_play((2, '2H', (0, 1)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('2C', 8), ('0D', 8), ('3H', 8), ('KD', 8)), (([], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), (['2S'], [], [], []))""", 0), 
        # INVALID: attempt to play card that is not top card of own stockpile (despite being top card of someone else's stockpile)
        ("""submission.comp10001bo_is_valid_play((2, '2H', (0, 1)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('2C', 8), ('2H', 8), ('3H', 8), ('KD', 8)), (([], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), (['2S'], [], [], []))""", 0), 
        # NON-FINAL VALID (from stockpile to non-empty build stack)
        ("""submission.comp10001bo_is_valid_play((2, 'QC', (0, 1)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('QC', 8), ('0D', 8), ('3H', 8), ('KD', 8)), (([], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), ([], ['KS'], [], []))""", 1), 
        # INVALID (from stockpile to *empty* discard stack 0 of Player 0)
        ("""submission.comp10001bo_is_valid_play((2, 'KC', (1, (0, 0))), 0, ['3C', 'AS', '9D', '0D', '0S'], (('KC', 8), ('0D', 8), ('3H', 8), ('KD', 8)), (([], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), ([], [], [], []))""", 0), 
        # NON-FINAL VALID (from discard pile to empty build stack 0)
        ("""submission.comp10001bo_is_valid_play((1, ('2C', (1, 0)), (0, 1)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('2C', 8), ('0D', 8), ('3H', 8), ('KD', 8)), (([], [], [], []), (['3C', '2C'], [], [], []), ([], [], [], []), ([], [], [], [])), (['2S'], [], [], []))""", 1), 
        # INVALID: attempt to access non-top card from discard stack 0 of player 1 
        ("""submission.comp10001bo_is_valid_play((1, ('3C', (1, 0)), (0, 1)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('2C', 8), ('0D', 8), ('3H', 8), ('KD', 8)), (([], [], [], []), (['3C', '2C'], [], [], []), ([], [], [], []), ([], [], [], [])), (['2S'], [], [], []))""", 0), 
        # INVALID: can't place 2C (from discard stack 0 of Player 1) on 2S (build stack 0)
        ("""submission.comp10001bo_is_valid_play((1, ('2C', (1, 0)), (0, 0)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('2C', 8), ('0D', 8), ('3H', 8), ('KD', 8)), (([], [], [], []), (['3C', '2C'], [], [], []), ([], [], [], []), ([], [], [], [])), (['2S'], [], [], []))""", 0), 
        # FINAL VALID: can place 9D (from hand) on 5S (discard stack 0 of Player 0), but final play for turn
        ("""submission.comp10001bo_is_valid_play((0, '9D', (1, (0, 0))), 0, ['AS', '9D', '0D', '0S'], (('9C', 8), ('0D', 8), ('3H', 8), ('KD', 8)), ((['5S'], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), ([], [], [], []))""", 2), 
        # INVALID: can make a number of different plays
        ("""submission.comp10001bo_is_valid_play((3, None, (None, None)), 0, ['AS', '9D', '0S'], (('9C', 8), ('0D', 8), ('3H', 8), ('KD', 8)), ((['5S'], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), ([], [], [], []))""", 0), 
        # VALID: no move possible (yes, it's an impossible game state, but it proves a point)
        ("""submission.comp10001bo_is_valid_play((3, None, (None, None)), 0, [], (('9C', 8), ('0D', 8), ('3H', 8), ('KD', 8)), ((['5S'], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), ([], [], [], []))""", 3), 
        # INVALID (attempt to move card from discard pile back to same discard pile)
        ("""submission.comp10001bo_is_valid_play((1, '2C', (1, 0), (1, (1, 0))), 0, ['3C', 'AS', '9D', '0D', '0S'], (('2C', 8), ('0D', 8), ('3H', 8), ('KD', 8)), (([], [], [], []), (['3C', '2C'], [], [], []), ([], [], [], []), ([], [], [], [])), (['2S'], [], [], []))""", 0),

    ],


    "comp10001bo_play":
    # note: test cases require deterministic behaviour, meaning hand must be empty (or could place card from hand onto *any* discard stack)
    [
        # no possible play
        ("""submission.comp10001bo_play(0, [], (('7H', 7), ('3C', 8), ('3H', 8), ('KD', 8)), ((['7H'], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), (['2C'], [], [], []), [(0, (2, '2C', (0, 0)))])""", (3, None, (None, None))),
        # play from stockpile to build pile
        ("""submission.comp10001bo_play(1, [], (('7H', 7), ('3C', 8), ('3H', 8), ('KD', 8)), ((['7H'], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), (['2C'], [], [], []), [(0, (2, '2C', (0, 0))), (0, (3, None, (None, None))), (1, (2, '3C', (0, 0)))])""", (2, '3C', (0, 0))), 
        # play from stockpile to build pile
        ("""submission.comp10001bo_play(1, [], (('7H', 7), ('4S', 7), ('3H', 8), ('KD', 8)), ((['7H'], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), (['2C', '3C'], [], [], []), [(0, (2, '2C', (0, 0))), (0, (3, None, (None, None))), (1, (2, '3C', (0, 0)))])""", (2, '4S', (0, 0))), 
        # play from stockpile to build pile, with example play
        ("""submission.comp10001bo_play(1, [], (('7H', 7), ('3S', 6), ('3H', 8), ('KD', 8)), ((['7H'], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), (['2C', '3C', '4S'], [], [], []), [(0, (2, '2C', (0, 0))), (0, (3, None, (None, None))), (1, (2, '3C', (0, 0))), (1, (2, '4S', (0, 0)))])""", (2, '3S', (0, 0))),
        # no valid play possible
        ("""submission.comp10001bo_play(1, [], (('7H', 7), ('0D', 5), ('3H', 8), ('KD', 8)), ((['7H'], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), (['2C', '3C', '4S'], [], [], []), [(0, (2, '2C', (0, 0))), (0, (3, None, (None, None))), (1, (2, '3C', (0, 0))), (1, (2, '4S', (0, 0))), (1, (2, '3S', (0, 0)))])""", (3, None, (None, None))),
    ]
}
