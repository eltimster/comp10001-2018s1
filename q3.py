from reference import comp10001bo_match_build, comp10001bo_match_discard

from common import *


def comp10001bo_is_valid_play(play, player_no, hand, stockpiles, discard_piles,
                              build_piles):
    """
    ADD FUNCTION DESCRIPTION HERE, AND CODE BELOW
    """



# automatically run each of the examples from the question
if __name__ == "__main__":
    tests = (
        # NON-FINAL VALID (from hand to build pile 0)
        (VALID_NONFINAL_PLAY, (0, '2C', (0, 0)), 0,
         ['2C', 'AS', '9D', '0D', '0S'],
         (('9C', 8), ('0D', 8), ('3H', 8), ('KD', 8)),
         (([], [], [], []), ([], [], [], []),
          ([], [], [], []), ([], [], [], [])), ([], [], [], [])),

        # INVALID: doesn't hold card
        (INVALID_PLAY, (0, '2C', (0, 0)), 0,
         ['3C', 'AS', '9D', '0D', '0S'],
         (('9C', 8), ('0D', 8), ('3H', 8), ('KD', 8)),
         (([], [], [], []), ([], [], [], []),
          ([], [], [], []), ([], [], [], [])), ([], [], [], [])),

        # INVALID: invalid pile (build pile 4)
        (INVALID_PLAY, (0, '3C', (0, 4)), 0,
         ['3C', 'AS', '9D', '0D', '0S'],
         (('9C', 8), ('0D', 8), ('3H', 8), ('KD', 8)),
         (([], [], [], []), ([], [], [], []), ([], [], [], []),
          ([], [], [], [])), ([], [], [], [])),

        # INVALID: can't play to build pile 0 (can't start with 3)
        (INVALID_PLAY, (0, '3C', (0, 0)), 0,
         ['3C', 'AS', '9D', '0D', '0S'],
         (('9C', 8), ('0D', 8), ('3H', 8), ('KD', 8)),
         (([], [], [], []), ([], [], [], []), ([], [], [], []),
          ([], [], [], [])), ([], [], [], [])),

        # NON-FINAL VALID (from hand to non-empty build pile 0)
        (VALID_NONFINAL_PLAY, (0, '3C', (0, 0)), 0,
         ['3C', 'AS', '9D', '0D', '0S'],
         (('9C', 8), ('0D', 8), ('3H', 8), ('KD', 8)),
         (([], [], [], []), ([], [], [], []), ([], [], [], []),
          ([], [], [], [])), (['2S'], [], [], [])),

        # NON-FINAL VALID (from stockpile to empty build pile 1)
        (VALID_NONFINAL_PLAY, (2, '2C', (0, 1)), 0,
         ['3C', 'AS', '9D', '0D', '0S'],
         (('2C', 8), ('0D', 8), ('3H', 8), ('KD', 8)),
         (([], [], [], []), ([], [], [], []), ([], [], [], []),
          ([], [], [], [])), (['2S'], [], [], [])),

        # INVALID: attempt to play card that is not top card of own stockpile
        (INVALID_PLAY, (2, '2H', (0, 1)), 0,
         ['3C', 'AS', '9D', '0D', '0S'],
         (('2C', 8), ('0D', 8), ('3H', 8), ('KD', 8)),
         (([], [], [], []), ([], [], [], []), ([], [], [], []),
          ([], [], [], [])), (['2S'], [], [], [])),

        # INVALID: attempt to play card that is not top card of
        # own stockpile (despite being top card of someone else's stockpile)
        (INVALID_PLAY, (2, '2H', (0, 1)), 0,
         ['3C', 'AS', '9D', '0D', '0S'],
         (('2C', 8), ('2H', 8), ('3H', 8), ('KD', 8)),
         (([], [], [], []), ([], [], [], []), ([], [], [], []),
          ([], [], [], [])), (['2S'], [], [], [])),

        # NON-FINAL VALID (from stockpile to non-empty build pile)
        (VALID_NONFINAL_PLAY, (2, 'QC', (0, 1)), 0,
         ['3C', 'AS', '9D', '0D', '0S'],
         (('QC', 8), ('0D', 8), ('3H', 8), ('KD', 8)),
         (([], [], [], []), ([], [], [], []), ([], [], [], []),
          ([], [], [], [])), ([], ['KS'], [], [])),

        # NON-FINAL VALID (from stockpile to *empty* build pile 1)
        (VALID_NONFINAL_PLAY, (2, 'KC', (0, 1)), 0,
         ['3C', 'AS', '9D', '0D', '0S'],
         (('KC', 8), ('0D', 8), ('3H', 8), ('KD', 8)),
         (([], [], [], []), ([], [], [], []), ([], [], [], []),
          ([], [], [], [])), ([], [], [], [])),

        # NON-FINAL VALID (from discard pile to empty build pile 0)
        (VALID_NONFINAL_PLAY, (1, '2C', (1, 0), (0, 1)), 0,
         ['3C', 'AS', '9D', '0D', '0S'],
         (('2C', 8), ('0D', 8), ('3H', 8), ('KD', 8)),
         (([], [], [], []), (['3C', '2C'], [], [], []), ([], [], [], []),
          ([], [], [], [])), (['2S'], [], [], [])),

        # INVALID: attempt to access non-top card from
        # discard stack 0 of player 1 
        (INVALID_PLAY, (1, ('3C', (1, 0)), (0, 1)), 0,
         ['3C', 'AS', '9D', '0D', '0S'],
         (('2C', 8), ('0D', 8), ('3H', 8), ('KD', 8)),
         (([], [], [], []), (['3C', '2C'], [], [], []), ([], [], [], []),
          ([], [], [], [])), (['2S'], [], [], [])),

        # INVALID: can't place 2C (from discard stack 0 of Player 1)
        # on 2S (build stack 0)
        (INVALID_PLAY, (1, ('2C', (1, 0)), (0, 0)), 0,
         ['3C', 'AS', '9D', '0D', '0S'],
         (('2C', 8), ('0D', 8), ('3H', 8), ('KD', 8)),
         (([], [], [], []), (['3C', '2C'], [], [], []), ([], [], [], []),
          ([], [], [], [])), (['2S'], [], [], [])),

        # FINAL VALID: can place 9D (from hand) on 5S (discard
        # stack 0 of Player 0), but final play for turn
        (VALID_FINAL_PLAY, (0, '9D', (1, (0, 0))), 0,
         ['AS', '9D', '0D', '0S'],
         (('9C', 8), ('0D', 8), ('3H', 8), ('KD', 8)),
         ((['5S'], [], [], []), ([], [], [], []), ([], [], [], []),
          ([], [], [], [])), ([], [], [], [])),

        # INVALID: can make a number of different plays
        (NO_PLAY, (3, None, (None, None)), 0, 
         ['AS', '9D', '0S'], 
         (('9C', 8), ('0D', 8), ('3H', 8), ('KD', 8)), 
         ((['5S'], [], [], []), ([], [], [], []), ([], [], [], []),
          ([], [], [], [])), ([], [], [], [])),

        # NO_PLAY: no move possible (yes, it's an impossible game
        # state, but it proves a point)
        (NO_PLAY, (None, (None, None)), 0, [], 
         (('9C', 8), ('0D', 8), ('3H', 8), ('KD', 8)), 
         ((['5S'], [], [], []), ([], [], [], []), ([], [], [], []), 
          ([], [], [], [])), ([], [], [], [])),
    )

    for retval, *args in tests:
        if comp10001bo_is_valid_play(*args) == retval:
            result = "passed"
        else:
            result = "failed"
        print("Testing comp10001bo_is_valid_play{} ... {}".format(
            repr(tuple(args)), result))
