from bank2 import value

#Pytest sjekker kun funksjoner med test!!!

def test_hello():
    assert value("hello") == 0

def test_greet_h():
    assert value("hey") == 20

def test_greet_no_h():
    assert value("god dag") == 100
