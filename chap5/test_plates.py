from plates2 import is_valid

test = is_valid("CS50")
print(test)


def test_lenght():
    assert is_valid("C") == False
    assert is_valid("CS50000") == False

def test_char():
    assert is_valid("CS%=!") == False

def test_null():
    assert is_valid("0CS50") == False  

def test_true():
    assert is_valid("CS50") == True