from common import *


def comp10001bo_match_discard(play_card, discard_pile, player_no, to_player_no,
                              from_hand=True):
    """
    ADD FUNCTION DESCRIPTION HERE, AND CODE BELOW
    """



# automatically run each of the examples from the question
if __name__ == "__main__":
    tests = (
        # can start own discard pile with any card from hand (FINAL play)
        (VALID_FINAL_PLAY, '4S', [], 2, 2),

        # can't start the discard pile of another player
        (INVALID_PLAY, '4S', [], 2, 0),

        # can't start a discard stack from the stockpile/build pile
        (INVALID_PLAY, '4S', [], 2, 2, False),

        # can play a black 4 on a red 3 (to own discard pile; NON-FINAL)
        (VALID_NONFINAL_PLAY, '4S', ['3H'], 2, 2),

        # can play a black 4 on a red 3 (to another
        # player's discard pile; NON-FINAL)
        (VALID_NONFINAL_PLAY, '4S', ['3H'], 2, 3),

        # can play a black 4 on a red 3 (from discard/stockpile to
        # own discard pile; NON-FINAL)
        (VALID_NONFINAL_PLAY, '4S', ['3H'], 2, 3, False),

        # can't play an Ace on a discard pile
        (INVALID_PLAY, 'AH', ['KS'], 2, 3),

        # can play a red 2 on a black King (to another
        # player's discard pile; NON-FINAL
        (VALID_NONFINAL_PLAY, '2H', ['KS'], 2, 3),

        # can (illegally) play 2 on Q (from hand to another player's
        # discard pile; FINAL)
        (VALID_FINAL_PLAY, '2H', ['QS'], 2, 3), 

        # can't play 2 on Q (from stockpile/build pile to another player's
        # discard pile; FINAL)
        (INVALID_PLAY, '2H', ['QS'], 2, 3, False), 

        # can (illegally) play red 4 on red 3 (from hand to another player's
        # discard pile; FINAL)
        (VALID_FINAL_PLAY, '4H', ['3H'], 2, 3),

        # can't (illegally) play red 4 on red 3 (from source other
        # than hand to own discard pile; INVALID)
        (INVALID_PLAY, '4H', ['3H'], 2, 2, False),

    )

    for retval, *args in tests:
        if comp10001bo_match_discard(*args) == retval:
            result = "passed"
        else:
            result = "failed"
        print("Testing comp10001bo_match_discard{} ... {}".format(
            repr(tuple(args)), result))
