from common import *

def comp10001bo_match_build(play_card, build_pile):
    """
    ADD FUNCTION DESCRIPTION HERE, AND CODE BELOW
    """


# automatically run each of the examples from the question
if __name__ == "__main__":
    tests = ((True, '2S', []),
             (True, '3C', ['2C']),
             (True, 'AH', ['2D', '3H']),
             (False, '3H', ['2D', '3H']),
             (False, '4C', ['2D', '3H']))    
    for retval, *args in tests:
        if comp10001bo_match_build(*args) == retval:
            result = "passed"
        else:
            result = "failed"
        print(f"Testing comp10001bo_match_build{repr(tuple(args))}) ... {result}")
