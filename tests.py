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
        ("""submission.comp10001bo_match_discard('4S', [], 2, 2)""", 1), 
        # INVALID: 4S on empty discard stack of different player
        ("""submission.comp10001bo_match_discard('4S', [], 2, 0)""", 0), 
        # INVALID: can't start a stack from stockpile
        ("""submission.comp10001bo_match_discard('4S', [], 2, 2, True)""", 0), 
        # NON-FINAL VALID: 4S on discard stack with 3H at top (same player)
        ("""submission.comp10001bo_match_discard('4S', ['3H'], 2, 2)""", 1), 
        # NON-FINAL VALID: 4S on discard stack with 3H at top (different player)
        ("""submission.comp10001bo_match_discard('4S', ['3H'], 2, 3)""", 1), 
        # NON-FINAL VALID: 4S on discard stack with 3H at top (different player)
        ("""submission.comp10001bo_match_discard('4S', ['3H'], 2, 3, True)""", 1), 
        # INVALID: can't place Ace on discard stack
        ("""submission.comp10001bo_match_discard('AH', ['KS'], 2, 3)""", 0), 
        # NON-FINAL VALID: wraparound from King to 2
        ("""submission.comp10001bo_match_discard('2H', ['KS'], 2, 3)""", 1), 
        # FINAL VALID: 4S on discard stack with 3H at top (different player)
        ("""submission.comp10001bo_match_discard('4H', ['3H'], 2, 3)""", 2), 
    ],

    "comp10001bo_is_valid_play":
    [
        # NON-FINAL VALID (from hand to build stack 0)
        ("""submission.comp10001bo_is_valid_play((0, '2C', (0, 0)), 0, ['2C', 'AS', '9D', '0D', '0S'], (('9C', 15), ('0D', 15), ('3H', 15), ('KD', 15)), (([], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), ([], [], [], []))""", 1), 
        # INVALID: doesn't hold card
        ("""submission.comp10001bo_is_valid_play((0, '2C', (0, 0)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('9C', 15), ('0D', 15), ('3H', 15), ('KD', 15)), (([], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), ([], [], [], []))""", 0), 
        # INVALID: invalid stack (build stack 4)
        ("""submission.comp10001bo_is_valid_play((0, '3C', (0, 4)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('9C', 15), ('0D', 15), ('3H', 15), ('KD', 15)), (([], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), ([], [], [], []))""", 0), 
        # INVALID: can't play to build stack 0 (can't start with 3)
        ("""submission.comp10001bo_is_valid_play((0, '3C', (0, 0)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('9C', 15), ('0D', 15), ('3H', 15), ('KD', 15)), (([], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), ([], [], [], []))""", 0), 
        # NON-FINAL VALID (from hand to non-empty build stack 0)
        ("""submission.comp10001bo_is_valid_play((0, '3C', (0, 0)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('9C', 15), ('0D', 15), ('3H', 15), ('KD', 15)), (([], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), (['2S'], [], [], []))""", 1), 
        # NON-FINAL VALID (from stockpile to empty build stack 1)
        ("""submission.comp10001bo_is_valid_play((2, '2C', (0, 1)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('2C', 15), ('0D', 15), ('3H', 15), ('KD', 15)), (([], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), (['2S'], [], [], []))""", 1), 
        # INVALID: attempt to play card that is not top card of own stockpile
        ("""submission.comp10001bo_is_valid_play((2, '2H', (0, 1)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('2C', 15), ('0D', 15), ('3H', 15), ('KD', 15)), (([], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), (['2S'], [], [], []))""", 0), 
        # INVALID: attempt to play card that is not top card of own stockpile (despite being top card of someone else's stockpile)
        ("""submission.comp10001bo_is_valid_play((2, '2H', (0, 1)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('2C', 15), ('2H', 15), ('3H', 15), ('KD', 15)), (([], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), (['2S'], [], [], []))""", 0), 
        # NON-FINAL VALID (from stockpile to non-empty build stack)
        ("""submission.comp10001bo_is_valid_play((2, 'QC', (0, 1)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('QC', 15), ('0D', 15), ('3H', 15), ('KD', 15)), (([], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), ([], ['KS'], [], []))""", 1), 
        # INVALID (from stockpile to *empty* build stack 0 of Player 0)
        ("""submission.comp10001bo_is_valid_play((2, 'KC', (1, (0, 0))), 0, ['3C', 'AS', '9D', '0D', '0S'], (('KC', 15), ('0D', 15), ('3H', 15), ('KD', 15)), (([], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), ([], [], [], []))""", 0), 
        # NON-FINAL VALID (from discard pile to empty build stack 0)
        ("""submission.comp10001bo_is_valid_play((1, ('2C', (1, 0)), (0, 1)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('2C', 15), ('0D', 15), ('3H', 15), ('KD', 15)), (([], [], [], []), (['3C', '2C'], [], [], []), ([], [], [], []), ([], [], [], [])), (['2S'], [], [], []))""", 1), 
        # INVALID: attempt to access non-top card from discard stack 0 of player 1 
        ("""submission.comp10001bo_is_valid_play((1, ('3C', (1, 0)), (0, 1)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('2C', 15), ('0D', 15), ('3H', 15), ('KD', 15)), (([], [], [], []), (['3C', '2C'], [], [], []), ([], [], [], []), ([], [], [], [])), (['2S'], [], [], []))""", 0), 
        # INVALID: can't place 2C (from discard stack 0 of Player 1) on 2S (build stack 0)
        ("""submission.comp10001bo_is_valid_play((1, ('2C', (1, 0)), (0, 0)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('2C', 15), ('0D', 15), ('3H', 15), ('KD', 15)), (([], [], [], []), (['3C', '2C'], [], [], []), ([], [], [], []), ([], [], [], [])), (['2S'], [], [], []))""", 0), 
        # FINAL VALID: can place 9D (from hand) on 5S (discard stack 0 of Player 0), but final play for turn
        ("""submission.comp10001bo_is_valid_play((0, '9D', (1, (0, 0))), 0, ['AS', '9D', '0D', '0S'], (('9C', 15), ('0D', 15), ('3H', 15), ('KD', 15)), ((['5S'], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), ([], [], [], []))""", 2), 
    ],


}
