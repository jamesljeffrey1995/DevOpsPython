import pytest
from Challengeoftheday import primeNum

def test_endsPy():
    assert primeNum.primeNumber(5) == True
    assert primeNum.primeNumber(6) == False