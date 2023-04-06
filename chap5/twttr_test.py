from twttr2 import shorten

#Ver obs på try og except ved bruk av pytest
#fordi dej kan gjere koden "feilfri"

#Problemet med input blir køyrt er at
#programma som skal teste eit annet ikke behøver def main

def test_twttr_vowels():
    assert shorten("mamma") == "mmm"
    assert shorten("lol") == "ll"
    assert shorten("OMG") == "MG"
    assert shorten("!?#") == "!?#"
    assert shorten("mjølk") == "mjlk"


