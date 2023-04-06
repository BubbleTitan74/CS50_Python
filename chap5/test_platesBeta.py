from platesBeta import is_valid



def test_correct():
    assert is_valid("CS50") == True

def test_length():
    assert is_valid("CSGOKJKJLKJ") == False
    assert is_valid("C") == False


def test_char():
    assert is_valid("aa. !") == False

