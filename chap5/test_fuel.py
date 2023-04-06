from drivstoff import gauge
from drivstoff import convert
import pytest

def test_convert():
    assert convert("3/6") == 50
        

    with pytest.raises(ValueError):
        convert("cat")
"""Dette eksempelet går ikkje
    with pytest.raises(AssertionError):
        convert("3/5") == 50
"""
#Unngå også å bruke try og ecxept når du skal feilsøke.

def test_gauge():
    assert gauge(50) == "G"
    assert gauge(0.5) == "E"
    assert gauge(100) == "F"
    assert gauge(-3) == "E"
