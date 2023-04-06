from twttr2 import shorten


def test_shorten():
    assert shorten("Twitter") == "Twttr"
    assert shorten("mjølk") == "mjølk"
    assert shorten("CS50") == "CS50"
    assert shorten("AEIOU") == ""