from common import *


def comp10001bo_play(player_no, hand, stockpiles, discard_piles, build_piles,
                     play_history):
    """
    ADD FUNCTION DESCRIPTION HERE, AND CODE BELOW
    """



# automatically run each of the examples from the question
if __name__ == "__main__":
    tests = (
        # no possible play
        ((3, None, (None, None)), 0, [], (('7H', 7), ('3C', 8), ('3H', 8), ('KD', 8)), ((['4C'], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), (['2C'], [], [], []), [(0, (2, '2C', (0, 0)))]),

        # play from stockpile to build pile
        ((2, '3C', (0, 0)), 1, [], (('7H', 7), ('3C', 8), ('3H', 8), ('KD', 8)), ((['4C'], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), (['2C'], [], [], []), [(0, (2, '2C', (0, 0))), (0, (3, None, (None, None))), (1, (2, '3C', (0, 0)))]),

        # play from stockpile to build pile
        ((2, '4S', (0, 0)), 1, [], (('7H', 7), ('4S', 7), ('3H', 8), ('KD', 8)), ((['4C'], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), (['2C', '3C'], [], [], []), [(0, (2, '2C', (0, 0))), (0, (3, None, (None, None))), (1, (2, '3C', (0, 0)))]),

        # play from stockpile to build pile, with example play
        ((2, '3S', (0, 0)), 1, [], (('7H', 7), ('3S', 6), ('3H', 8), ('KD', 8)), ((['4C'], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), (['2C', '3C', '4S'], [], [], []), [(0, (2, '2C', (0, 0))), (0, (3, None, (None, None))), (1, (2, '3C', (0, 0))), (1, (2, '4S', (0, 0)))]),

        # no valid play possible
        ((3, None, (None, None)), 1, [], (('7H', 7), ('0D', 5), ('3H', 8), ('KD', 8)), ((['4C'], [], [], []), ([], [], [], []), ([], [], [], []), ([], [], [], [])), (['2C', '3C', '4S'], [], [], []), [(0, (2, '2C', (0, 0))), (0, (3, None, (None, None))), (1, (2, '3C', (0, 0))), (1, (2, '4S', (0, 0))), (1, (2, '3S', (0, 0)))])
    )

    for retval, *args in tests:
        if comp10001bo_play(*args) == retval:
            result = "passed"
        else:
            result = "failed"
        print("Testing comp10001bo_play{} ... {}".format(
            repr(tuple(args)), result))
