import pytest
from Challengeoftheday import countVowels

def test_endsPy():
    assert countVowels.countVowelsCalc("ilovepy") == 3
    assert countVowels.countVowelsCalc("ilovveepy") == 4