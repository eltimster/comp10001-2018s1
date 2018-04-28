# dictionary of tests, one for each function in the project spec; in each case, list a number of function calls (as a str), and the correct output for each

# Version: 1.0
# Created 28/4/18




test_cases = {
    "card_match_build":
    [
        # VALID: 2S on empty build stack
        ("""submission.card_match_build('2S', [])""", True), 
        # VALID: KH on empty build stack
        ("""submission.card_match_build('KH', [])""", True), 
        # INVALID: AH on empty build stack (ace can't start stack)
        ("""submission.card_match_build('AH', [])""", False), 
        # VALID: 3S on build stack with 2C at top
        ("""submission.card_match_build('3C', ['2C'])""", True), 
        # VALID: 4H on build stack with 3H at top
        ("""submission.card_match_build('4H', ['2D', '3H'])""", True), 
        # VALID: 2H on build stack with 3H at top
        ("""submission.card_match_build('2H', ['2D', '3H'])""", True), 
        # VALID: AH on build stack with 3H at top
        ("""submission.card_match_build('AH', ['2D', '3H'])""", True), 
        # INVALID: AS on build stack with 3H at top (colour mismatch)
        ("""submission.card_match_build('AS', ['2D', '3H'])""", False), 
        # VALID: 5S on empty build stack
        ("""submission.card_match_build('5S', [])""", False), 
        # INVALID: 3H on build stack with 3H at top (value mismatch)
        ("""submission.card_match_build('3H', ['2D', '3H'])""", False), 
        # INVALID: 4C on build stack with 3H at top (colour mismatch)
        ("""submission.card_match_build('4C', ['2D', '3H'])""", False), 
    ],    

    "card_match_discard":
    [
        # NON-FINAL VALID: 4S on empty discard stack of that player
        ("""submission.card_match_discard('4S', [], 2, 2)""", 1), 
        # INVALID: 4S on empty discard stack of different player
        ("""submission.card_match_discard('4S', [], 2, 0)""", 0), 
        # INVALID: invalid player number
        ("""submission.card_match_discard('4S', [], 2, 5)""", 0), 
        # INVALID: invalid card
        ("""submission.card_match_discard('PS', [], 2, 0)""", 0), 
        # NON-FINAL VALID: 4S on discard stack with 3H at top (same player)
        ("""submission.card_match_discard('4S', ['3H'], 2, 2)""", 1), 
        # NON-FINAL VALID: 4S on discard stack with 3H at top (different player)
        ("""submission.card_match_discard('4S', ['3H'], 2, 3)""", 1), 
        # NON-FINAL VALID: KS on discard stack with AH at top (different player)
        ("""submission.card_match_discard('KS', ['AH'], 2, 3)""", 1), 
        # NON-FINAL VALID: AH on discard stack with KS at top (different player)
        ("""submission.card_match_discard('AH', ['KS'], 2, 3)""", 1), 
        # FINAL VALID: AS on discard stack with KS at top (different player)
        ("""submission.card_match_discard('AS', ['KS'], 2, 3)""", 2), 
        # FINAL VALID: 4S on discard stack with 3H at top (different player)
        ("""submission.card_match_discard('4H', ['3H'], 2, 3)""", 2), 
    ],

    "is_valid_play":
    [
        # NON-FINAL VALID (from hand to empty stack)
        ("""submission.is_valid_play((0, '2C', (0, 0)), 0, ['2C', 'AS', '9D', '0D', '0S'], (('9C', 15), ('0D', 15), ('3H', 15), ('KD', 15)), (([], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), ([], [], [], []))""", 1), 
        # NON-FINAL VALID: doesn't hold card
        ("""submission.is_valid_play((0, '2C', (0, 0)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('9C', 15), ('0D', 15), ('3H', 15), ('KD', 15)), (([], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), ([], [], [], []))""", 0), 
        # NON-FINAL VALID: invalid card
        ("""submission.is_valid_play((0, 'GC', (0, 0)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('9C', 15), ('0D', 15), ('3H', 15), ('KD', 15)), (([], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), ([], [], [], []))""", 0), 
        # NON-FINAL VALID: invalid stack
        ("""submission.is_valid_play((0, 'GC', (0, 4)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('9C', 15), ('0D', 15), ('3H', 15), ('KD', 15)), (([], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), ([], [], [], []))""", 0), 
        # NON-FINAL VALID: can't play to stack (can't start with 3)
        ("""submission.is_valid_play((0, '3C', (0, 0)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('9C', 15), ('0D', 15), ('3H', 15), ('KD', 15)), (([], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), ([], [], [], []))""", 0), 
        # NON-FINAL VALID (from hand to non-empty stack)
        ("""submission.is_valid_play((0, '3C', (0, 0)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('9C', 15), ('0D', 15), ('3H', 15), ('KD', 15)), (([], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), (['2S'], [], [], []))""", 1), 
        # NON-FINAL VALID (from stockpile to empty stack)
        ("""submission.is_valid_play((2, '2C', (0, 1)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('2C', 15), ('0D', 15), ('3H', 15), ('KD', 15)), (([], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), (['2S'], [], [], []))""", 1), 
        # NON-FINAL VALID: not top card of stockpile
        ("""submission.is_valid_play((2, '2H', (0, 1)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('2C', 15), ('0D', 15), ('3H', 15), ('KD', 15)), (([], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), (['2S'], [], [], []))""", 0), 
        # NON-FINAL VALID: not top card of (own) stockpile
        ("""submission.is_valid_play((2, '2H', (0, 1)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('2C', 15), ('2H', 15), ('3H', 15), ('KD', 15)), (([], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), (['2S'], [], [], []))""", 0), 
        # NON-FINAL VALID (from stockpile to non-empty build stack)
        ("""submission.is_valid_play((2, 'QC', (0, 1)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('QC', 15), ('0D', 15), ('3H', 15), ('KD', 15)), (([], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), ([], ['KS'], [], []))""", 1), 
        # NON-FINAL VALID (from stockpile to empty discard stack)
        ("""submission.is_valid_play((2, 'KC', (1, (0, 0))), 0, ['3C', 'AS', '9D', '0D', '0S'], (('KC', 15), ('0D', 15), ('3H', 15), ('KD', 15)), (([], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), ([], [], [], []))""", 0), 
        # NON-FINAL VALID (from discard pile to empty stack)
        ("""submission.is_valid_play((1, ('2C', (1, 0)), (0, 1)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('2C', 15), ('0D', 15), ('3H', 15), ('KD', 15)), (([], [], [], []), (['3C', '2C'], [], [], []), ([], [], [], []), ([], [], [], [])), (['2S'], [], [], []))""", 1), 
        # NON-FINAL VALID: incorrect card
        ("""submission.is_valid_play((1, ('3C', (1, 0)), (0, 1)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('2C', 15), ('0D', 15), ('3H', 15), ('KD', 15)), (([], [], [], []), (['3C', '2C'], [], [], []), ([], [], [], []), ([], [], [], [])), (['2S'], [], [], []))""", 0), 
        # NON-FINAL VALID: can't place 2C on 2S in case of build stack
        ("""submission.is_valid_play((1, ('2C', (1, 0)), (0, 0)), 0, ['3C', 'AS', '9D', '0D', '0S'], (('2C', 15), ('0D', 15), ('3H', 15), ('KD', 15)), (([], [], [], []), (['3C', '2C'], [], [], []), ([], [], [], []), ([], [], [], [])), (['2S'], [], [], []))""", 0), 
        # FINAL VALID: can place 9D on 5S in case of discard stack, but final play
        ("""submission.is_valid_play((0, '9D', (1, (0, 0))), 0, ['AS', '9D', '0D', '0S'], (('9C', 15), ('0D', 15), ('3H', 15), ('KD', 15)), ((['5S'], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), ([], [], [], []))""", 2), 
    ],


}
